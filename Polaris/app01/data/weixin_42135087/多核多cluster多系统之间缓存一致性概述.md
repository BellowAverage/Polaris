
--- 
title:  多核多cluster多系统之间缓存一致性概述 
tags: []
categories: [] 

---
>  
 <font color="purple" size="5">**快速链接:**</font> .   
 -  <font color="red" size="3">**【购买须知】:**</font>- -  ----<font color="red" size="3">**联系方式-加入交流群**</font> 


>  
 **引流关键词**:缓存,高速缓存,cache, CCI,CMN,CCI-550,CCI-500,DSU,SCU,L1,L2,L3,system cache, Non-cacheable,Cacheable, non-shareable,inner-shareable,outer-shareable, optee、ATF、TF-A、Trustzone、optee3.14、MMU、VMSA、cache、TLB、arm、armv8、armv9、TEE、安全、内存管理、页表… 


>  
  
  
  <h4>目录</h4> 
  - <ul><li><ul><li><ul><li>- - <ul><li>- -  
      </li>- - - - - </ul> 
    </li></ul> 
   </li></ul> 
  </li></ul> 
  
  


本文转自 周贺贺，baron，代码改变世界ctw，Arm精选， armv8/armv9，trustzone/tee，secureboot，资深安全架构专家，11年手机安全/SOC底层安全开发经验。擅长trustzone/tee安全产品的设计和开发。

##### 1. 思考和质疑

在一个大架构大系统中，有哪些一致性需要维护？我们先看如下一张架构图。 <img src="https://img-blog.csdnimg.cn/0a1010eedaed414e85bf3039b3f1d286.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 然后请思考：
- (1)、core0中的L1和L2 cache有一致性的要求吗？缓存和替换策略是怎样的？- (2)、core0 cache 和 core1 cache的一致性是谁来维护？ 遵从MESI协议吗？- (3)、core0 cache 和 core4 cache的是怎么维护一致性的呢？- (4)、custer0 L3 cache 和 cluster1 L3 cache的一致性是谁来维护？遵从什么协议吗？- (5)、custer0 L3 cache 和 GPU的L2一致性呢？遵从什么协议？- (6)、custer0 L3 cache 和 其它的`I/O device Master`一致性呢？遵从什么协议？- (7)、DSU、ACE、CHI、CCI、CMN的概念？
网上的好多篇博文，一提Cache的多核一致性就**必然**提到`MESI、MOESI` ，然后就开始讲`MESI、MOESI`维护性原理？试问一下，您是真的不理解MESI吗？您真的需要学习MESI？你不理解的是架构吧，而不是学什么协议. 既然要学习MESI，那么这里也继续提出一些问题：
- (1)、ARM架构中真的使用MESI了吗？ 或者是哪一级cache使用了，哪一级cache没有使用？- (2)、MESI是一个协议？ 是谁来维护的？总得有个硬件实现这个协议吧，是在ARM Core实现？DSU实现？- (3)、MESI的四种状态，分别记录在哪里的？- (4)、arm现在主流的core，到底使用的是MESI，还是MOESI？
##### 2. 怎样去维护多核多系统缓存的一致性

**有三种机制可以保持一致性：**
- <font color="blue" size="4"> 禁用缓存</font>是最简单的机制，但可能会显着降低 CPU 性能。为了获得最高性能，处理器通过管道以高频率运行，并从提供极低延迟的缓存中运行。缓存多次访问的数据可显着提高性能并降低 DRAM 访问和功耗。将数据标记为“非缓存”可能会影响性能和功耗。- <font color="blue" size="4"> 软件管理的一致性</font>是数据共享问题的传统解决方案。在这里，软件（通常是设备驱动程序）必须清除或刷新缓存中的脏数据，并使旧数据无效，以便与系统中的其他处理器或主设备共享。这需要处理器周期、总线带宽和功率。- <font color="blue" size="4"> 硬件管理的一致性</font>提供了一种简化软件的替代方案。使用此解决方案，任何标记为“共享”的缓存数据将始终自动更新。该共享域中的所有处理器和总线主控器看到的值完全相同。
然而，我们在ARM架构中，默认使用的却是第三种<font color="blue" size="4"> 硬件管理的一致性</font>, 意思就是：做为一名软件工程师，我们啥也不用管了，有人帮我们干活，虽然如此，但我们还是希望理解下硬件原理。

再讲原理之前，我们先补充一个场景: 假设在某一操作系统中运行了一个线程，该线程不停着操作0x4000_0000地址处内存（所以我们当然期望，它总是命中着），由于系统调度，这一次该线程可能跑在cpu0上，下一次也许就跑在cpu1上了，再下一次也许就是cpu4上了(其实这种行为也叫做CPU migration)

或者举个这样的场景也行： 在Linux Kernel系统中，定义了一个全局性的变量，然后多个内核线程(多个CPU)都会访问该变量.

在以上的场景中，都存在一块内存(如0x4000_0000地址处内存)被不同的ARM CORE来访问，这样就会出现了该数据在main-memory、cluster cache、core cache不一致的情况, 复杂点场景可能还会考虑cluster chache和other Master(如GPU) cache的一致性情况。

既然出现了数据在内存和不同的cache中的不一致的情况，那么就需要解决这个问题（也叫维护cache一致性），那么怎么维护的呢，上面也说了“使用<font color="blue" size="4"> 硬件管理的一致性</font>”，下面就以直接写答案的方式，告诉你硬件是怎样维护一致性的。

###### 2. 1 多核缓存一致性

同一个cluster中多core之间的缓存一致性由DSU(big.LITTLE叫SCU)来维护，遵循MESI协议。 <img src="https://img-blog.csdnimg.cn/8ce7a0b38988477f8ffdd16b1b1e3971.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 2. 2 多Master之间的缓存一致性

在讲述多Master之间的缓存一致性之前，我们先将Master分为以下几类：
- ACE Master : 如 big.LITTLE cluster 或 DSU cluster- CHI Master : 如 big.LITTLE cluster 或 DSU cluster- ACE-lite Master： 如 GPU cluster- I/O Device Master : 如 DMA
<img src="https://img-blog.csdnimg.cn/70d3baaccbf84ba18539a09ec4788ba5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 以下是多Master之间的缓存一致性的结论：
- 首先，CHI/ACE总线都是支持MESI协议数据传输的- Master与I/O Device Master之间没有一致性，因为I/O Device没有链接到CCI/CMN缓存互联总线上。- 多个ACE/CHI Master之间的缓存一致性，是否遵循MESI，要具体情况具体分析，简而言之就是： (1) 如果两个Master都支持带MESI状态位，支持带有MESI信号的读写，那么这两个Master缓存一致性是遵从MESI协议的 (2) 如果有一个Master不支持带MESI状态位，那么这个Master就无法支持带有MESI信号的读写，那么这两个Master缓存一致性是不遵从MESI协议的 (3) Master的MESI状态位，是在该Master的cache的TAG中。- ACE/CHI Master和ACE-lite Master之间的缓存一致性，是不遵从MESI协议的。这主要是因为ACE/CHI Master无法snoop ACE-lite Master的内存，而ACE-lite Master却可以snoop ACE/CHI Master的内存，总得来说，这不是一个完整的MESI协议。
举一个最常见的例子：两个DSU cluster的L3 cache中的TAG中，是有MESI比特位的，这两个DSU通过ACE/CHI 接口发起的读写是带有MESI信号的，所以他们是支持MESI协议的。 <img src="https://img-blog.csdnimg.cn/9976088e44304550b424e6b02cddf48e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_14,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

再举一个例子，一个DSU cluster 和一个接到SMMU上的DMA，此时正好对应一个是ACE/CHI Master，一个ACE-lite Master，由于DMA/SMMU中并没有MESI状态位，他们也不会发起带有MESI信号的读写，所以这两个Master之间是不支持MESI协议的。 <img src="https://img-blog.csdnimg.cn/d81af6bedfb84a41ad133ef19eb7ff58.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_14,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 2. 3 `dynamIQ`架构同一个core中的L1和L2 cache

`dynamIQ`架构core中的L1和L2 cache不存在缓存一致性的问题，但有分配和替换策略。

我们先看一下DynamIQ架构中的cache中新增的几个概念：
- (1) **Strictly inclusive**: 所有存在L1 cache中的数据，必然也存在L2 cache中- (2) **Weakly inclusive**: 当miss的时候，数据会被同时缓存到L1和L2，但在之后，L2中的数据可能会被替换- (3) **Fully exclusive**: 当miss的时候，数据只会缓存到L1
其实inclusive/exclusive属性描述的正是是 L1和L2之间的替换策略，这部分是硬件定死的，软件不可更改的。

我们再以 `ARMV9 cortex-A710 `为例，查看其TRM手册，得知： <img src="https://img-blog.csdnimg.cn/517d77523f154934b294dbc264631e9e.png" alt="在这里插入图片描述">
- L1 I-cache和L2之间是 weakly inclusive的- L1 D-cache和L2之间是 strictly inclusive的
也就是说：
- 当发生D-cache发生miss时，数据缓存到L1 D-cache的时候，也会被缓存到L2 Cache中，当L2 Cache被替换时，L1 D-cache也会跟着被替换- 当发生I-cache发生miss时，数据缓存到L1 I-cache的时候，也会被缓存到L2 Cache中，当L2 Cache被替换时，L1 I- cache不会被替换
所以总结一下就是 ： L1 和 L2之间的cache的替换策略，针对I-cache和D-cache可以是不同的策略，每一个core都有每一个core的做法，这部分是硬件决定的，请查阅你使用core的TRM手册。

##### 3. MESI协议的介绍

本协议适用于：
- big.LITTLE架构中多核缓存一致性- dynamIQ架构中多核缓存一致性- 多cluster之间缓存一致性 <img src="https://img-blog.csdnimg.cn/c7b2c52cb1ec4bedb212fde066ea6e81.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_10,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 其实也适用于：- 不同cluster之间多核的缓存一致性 <img src="https://img-blog.csdnimg.cn/489870a3edda41f99314c42d76071eda.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
然后接下来，我们开始学习MESI协议，注意着仅仅是一个协议 ，它既不是软件也不是硬件，算上一个标准吧。 首先是Modified Exclusive Shared Invalid (MESI) 协议中定义了4个状态:

<th align="left">MESI State</th><th align="left">Definition</th>
|------
<td align="left">**Modified (M)**</td><td align="left">这行数据有效，数据已被修改，和内存中的数据不一致，数据只存在于该高速缓存中</td>
<td align="left">**Exclusive (E)**</td><td align="left">这行数据有效，数据和内存中数据一致，数据只存在于该高速缓存中</td>
<td align="left">**Shared (S)**</td><td align="left">这行数据有效，数据和内存中数据一致，多个高速缓存有这行数据的副本</td>
<td align="left">**Invalid (I)**</td><td align="left">这行数据无效</td>

其次，在ARM的部分的core中，定义了第五种状态`Shared Modified`，这种称之为`MOESI `协议. 我查询大量的Core的TRM手册，信息如下：
- 使用MESI协议的core有：A710 A510 A78 A77 A76 A75 A72 A57 A55…- 使用MOESI协议的core有：A7 A15 A53
发现问题了没？ 并不是网上主流博客所说，arm一般都用MOESI。<font color="red" size="4">**请记住arm主流core在使用的是MESI**</font>。所以接下来，我们也不会再介绍和学习MOESI了。

然后我们通过数据流图的方式，观看下**MESI这四种状态**的情况: <img src="https://img-blog.csdnimg.cn/cafdc00ad36644bf9b8bf6bef56872b0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **MESI状态之间的切换:** <img src="https://img-blog.csdnimg.cn/990eafc68ded48289fc00d578b8e3a8f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 **Events:** RH = Read Hit RMS = Read miss, shared RME = Read miss, exclusive WH = Write hit WM = Write miss SHR = Snoop hit on read SHI = Snoop hit on invalidate LRU = LRU replacement  **Bus Transactions:** Push = Write cache line back to memory Invalidate = Broadcast invalidate Read = Read cache line from memory 


学到这里，我们对多核之间缓存一致性也有了大概的理解，我们也知道了MESI是干啥的了，那么我们继续抛几个问题： (1)、为什么说“多核之间的缓存一致性，遵从MESI协议，是DSU/SCU来维护”的？

其实吧，这也不是我说的，这来自ARM官方文档：

对于big.LITTLE架构，SCU是这样描述的： <img src="https://img-blog.csdnimg.cn/09ec4dde5cdf4a3e9ab9ea310ad25ce4.png" alt="在这里插入图片描述"> 对于dynamIQ架构，DSU文档中这样描述的： <img src="https://img-blog.csdnimg.cn/51b490d558e5437cbed41c54d6661e97.png" alt="在这里插入图片描述">

(2)、MESI的状态位记录在哪里的？ 以 `ARMV9 cortex-A710 `为例，记录在core cache的TAG中的BIT[1:0]中，即在TAG中。 <img src="https://img-blog.csdnimg.cn/7bfb5ce112c84dcfb54ea18c4b310b35.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_19,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 对于big.LITTLE架构SCU的L2 cache、dynamIQ架构的DSU L3 cache中的TAG中，也都是有MESI比特位的，不过这一点在`arm ARMs`和`trm`文档都是找不到的，不过在一些的PPT上是可以看到的。 <img src="https://img-blog.csdnimg.cn/7c069ad9c6314b4b8b23d9d6d2b82f4d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

##### 4、ACE维护的缓存一致性

ACE master是接到 CCI 缓存互联总线上的， 在 CCI Interconnect中，其实也是有一个Snoop Filter单元。 ACE协议和Snoop filter单元一起来完成了ACE Master之间的缓存一致性。 <img src="https://img-blog.csdnimg.cn/0d075b59aa6a449e937a28f098b5bf47.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> snoop filter的主要作用：用于记录存储在ACE中的缓存。

Snoop Filter可以在未命中的情况下响应侦听事务，并侦听适当的主控只有在命中的情况下。Snoop Filter条目通过观察来自 ACE 主节点的事务来维护以确定何时必须分配和取消分配条目。

Snoop Filter可以响应多个一致性请求，而无需向所有master广播ACE 接口。例如，如果地址不在任何缓存中，则Snoop Filter会以未命中和将请求定向到内存。如果地址在处理器缓存中，则请求被视为命中，并且指向在其缓存中包含该地址的 ACE 端口。

以下也举了一个多cluster之间缓存一致性的示例，A53 cluster读取A57 cluster缓存一致性数据。 <img src="https://img-blog.csdnimg.cn/a52df7be37184f00975f48fa99db4a41.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_11,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
- (1). Cortex-A53 cluster 发出 Coherent Read Request。- (2). CCI-400 将请求传递Request以窥探 Cortex-A57 cluster 缓存。- (3). 收到请求后，Cortex-A57 cluster会检查其数据缓存的可用性并以所需信息进行响应。- (4). 如果请求的数据在缓存中，CCI-400 将数据从 Cortex-A57 cluster移动到 Cortex-A53 cluster，从而导致 Cortex-A53 cluster中的缓存行填充。
##### 5、软件定义的缓存和替换策略

以上的multi cores、multi cluster、system之间的缓存策略或协议，都是由硬件决定，软件改不了。那么**我们软件可以做什么呢？** 其实，在软件的MMU页表的entry中的属性位中，是可以定义该页面内存的缓存策略的。 如果软件定义了内存位non-cacheable或non-shareable，那么以上的"硬件维护的一致性"将不会生效。 接下来对，软件定义的缓存策略做了一个小小的总结。

<img src="https://img-blog.csdnimg.cn/debcbe1bd7d044d7b9eb50d36c20efa2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_16,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 总结了一下shareable、cacheable属性对缓存策略的影响：

<th align="left"></th><th align="left">Non-cacheable</th><th align="left">write-back cacheable</th><th align="left">write-through cacheable</th>
|------
<td align="left">**non-shareable**</td><td align="left"><font color="red" size="4">数据不会缓存到cache</font><font color="purple" size="3">（对于观察则而言，又相当于outer-shareable）</font></td><td align="left"><font color="blue" size="3">core访问该内存时，数据只缓存的到Core的 cache 中，不会缓存到其它cache中</font></td><td align="left">同左侧</td>
<td align="left">**inner-shareable**</td><td align="left"><font color="red" size="4">数据不会缓存到cache</font><font color="purple" size="3">（对于观察则而言，又相当于outer-shareable）</font></td><td align="left"><font color="blue" size="3">core访问该内存时，数据只会缓存到core的cache和 cluster的 cache中，该地址的TAG也不会存到snoop filter中，即不会被其它ACE Master snoop</font></td><td align="left">同左侧</td>
<td align="left">**outer-shareable**</td><td align="left"><font color="red" size="4">数据不会缓存到cache</font><font color="purple" size="3">（对于观察则而言，又相当于outer-shareable）</font></td><td align="left"><font color="blue" size="3">core访问该内存时，数据只会缓存到core的cache和 cluster的 cache中，该地址的TAG会存到snoop filter中，会被其它ACE Master snoop</font></td><td align="left">同左侧</td>

##### 6、动图示例

>  
 **前置条件：** dynamIQ架构、L1 Data weakly inclusive、读写的内存配置位outer-shareable/write-back cacheable  **步骤:** 
 - (1)、core0 读取了一行数据，数据缓存到了core0的L1 Dcache、L2 cache- (2)、随后core0的L2 中的数据是有可能会被替换出- (3)、core1 也读取了该行数据，数据缓存到了core1的L1 Dcache、L2 cache、L3 cache- (4)、随后core1的L2 中的数据也是有可能会被替换出- (5)、core4 也读取了该行数据，数据缓存到了core4的L1 Dcache、L2 cache- (6)、随后core4的L2 中的数据也是有可能会被替换出- (7)、至此，core0的L1、core1的L1、cluster0的L3、core4的L1 中都缓存了该数据。core0的L2、core1的L2、core4的L2 可能缓存了该行数据 


<img src="https://img-blog.csdnimg.cn/36b1438f4eaa4b88be77024d64876ab8.gif" alt="请添加图片描述">

##### 推荐
-  --博客专栏-  --大课程-  --入门课程