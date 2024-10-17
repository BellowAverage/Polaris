
--- 
title:  cache的基本概念原理扫盲 
tags: []
categories: [] 

---
>  
 <font color="purple" size="5">**快速链接:**</font> .   
 -  <font color="red" size="3">**【购买须知】:**</font>- -  ----<font color="red" size="3">**联系方式-加入交流群**</font> 


>  
 **引流关键词**:缓存,高速缓存,cache, CCI,CMN,CCI-550,CCI-500,DSU,SCU,L1,L2,L3,system cache, Non-cacheable,Cacheable, non-shareable,inner-shareable,outer-shareable, optee、ATF、TF-A、Trustzone、optee3.14、MMU、VMSA、cache、TLB、arm、armv8、armv9、TEE、安全、内存管理、页表… 




#### 目录
- <ul><li><ul><li><ul><li>- - - <ul><li>- - - - - - 


本文转自 周贺贺，baron，代码改变世界ctw，Arm精选， armv8/armv9，trustzone/tee，secureboot，资深安全架构专家，11年手机安全/SOC底层安全开发经验。擅长trustzone/tee安全产品的设计和开发。

##### 1、cache是多级相连的

cache是多级的，在一个系统中你可能会看到L1、L2、L3, 当然越靠近core就越小，也是越昂贵。 一般来说，对于`big.LITTLE`架构中，在L1是core中，L1又分为L1 data cache和 L1 Instruction cache， L2 cache在cluster中，L3则在BUS总线上。 <img src="https://img-blog.csdnimg.cn/9a20a239133a43e8b307e2ac08e7db8b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_12,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

##### 2、cache一般是和MMU结合在一起使用的

很多时候cache都是和MMU一起使用的(即同时开启或同时关闭)，因为MMU页表的entry的属性中控制着内存权限和cache缓存策略等 <img src="https://img-blog.csdnimg.cn/20201110194457471.png#pic_center" alt="在这里插入图片描述"> 在ARM架构中，L1 cache都是VIPT的，也就是当有一个虚拟地址送进来，MMU在开始进行地址翻译的时候，Virtual Index就可以去L1 cache中查询了，MMU查询和L1 cache的index查询是同时进行的。如果L1 Miss了，则再去查询L2，L2还找不到则再去查询L3。 注意在arm架构中，仅仅L1 cache是VIPT，L1L2和L3都是PIPT。 <img src="https://img-blog.csdnimg.cn/326e800f196a419cb3065dc7bc2daf57.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

##### 3、硬件架构基础介绍

`big.LITTLE`架构 和 `DynamIQ`架构 的cache是有区别的 <img src="https://img-blog.csdnimg.cn/57dd1ee6a32747598687a14a186aaff0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
- 在`big.LITTLE` 架构中，大核小核在不同的cluster中，做为两个不同的ACE或CHI Master，连接到缓存一致性总线上(CCI或CMN)。大核cluster和小核cluster的缓存一致性，也需要通过一致性总线来解决。- 到了`DynamIQ` 架构中，大核和小核都是一个DSU cluster中，一个DSU cluster最多可以支持8个core。如果你的系统是8个core，那么一个DSU就够了，那么系统中也就只有一个ACE或CHI Master，大核和小核之间的一致性，都在DSU cluster内完成了。
###### 3.1 `big.LITTLE`架构的cache

在`big.LITTLE`的架构中，L1是在core中的，是core私有的；L2是在cluster中的，对cluster中的core是共享的；L3则对所有cluster共享。`big.LITTLE`的架构的一个cache层级关系图如下所示： <img src="https://img-blog.csdnimg.cn/5d4f4420f879471d823f906e64b73f4c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 3.2 `DynamIQ`架构架构的cache

在`dynamIQ`的架构中，L1和L2都在core中的，都是core私有的；L3则是在cluster中的，对cluster中的core是共享的；如有L3或system cache，则是所有cluster共享。`dynamIQ`的架构的一个cache层级关系图如下所示。 注意，一般来说一个DSU Cluster就可以做到支持8个core，以下只是举一个极端的例子，在硬件设计时，我非要放置两个DSU cluster 可不可以？两个DSU Cluster做为两个ACE Master连接到了CCI一致性总线上。 <img src="https://img-blog.csdnimg.cn/4ce4c9807b174e2c82265a460b97307c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 3.3 缓存一致性总线-CCI

用于ACE Master缓存一致性总线有`CCI-550`、`CCI-500`、`CCI-400`。 <img src="https://img-blog.csdnimg.cn/ca54081b972e499ca32688fe31ea419a.png" alt="在这里插入图片描述"> 它的主要作用是可以互联多个`ACE Master`、`ACE-lite Master`，然后通过ACE接口协议，做到多个Master之间的缓存一致性。CCI最多支持2个`ACE Master`，共计支持8个`ACE Master`+`ACE-lite Master`。 所以呢，如果是`big.LITTLE`架构的，那么最多支持两个cluster互联，每个cluster 8个core，所以最多支持8个core；如果是`dynamIQ`架构的，那么最多支持两个DSU cluster互联，每个cluster 8个core，所以最多支持16个core <img src="https://img-blog.csdnimg.cn/0d9dc6092bca45c2846b85219d1e8c70.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 3.4 缓存一致性总线-CMN

用于CHI Master缓存一致性总线有`CMN-700`、`CMN-600`. <img src="https://img-blog.csdnimg.cn/2117b969310b4ec4a978ea1092cb1ef4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 它的主要作用是可以互联多个`CHI Master`、`ACE-lite Master`，然后通过CHI接口协议，做到多个Master之间的缓存一致性。CCI-600最多支持8个`CHI Master`，共计支持8个`CHI Master`+`ACE-lite Master`。

<img src="https://img-blog.csdnimg.cn/92279a681a914f46b4aa2c67d66f6410.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 3.5 `big.LITTLE`架构中的cluster interface

在`big.LITTLE`架构中，cluster连接到一致性总线的接口，可以是ACE，也可以是CHI，所以big.LITTLE cluster既可以做为ACE Master连接到总线，也可以做为CHI Master连接到总线。 <img src="https://img-blog.csdnimg.cn/0703e8d6b2d3434489de56f2bb4d81de.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 3.6 `dynamIQ`架构中的DSU interface

2017年引入dynamIQ架构， 在DSU(dynamIQ Share Unit)规范中，连接到一致性总线的接口，可以是ACE，也可以是CHI，所以DSU cluster既可以做为ACE Master连接到总线，也可以做为CHI Master连接到总线。 <img src="https://img-blog.csdnimg.cn/297fa9117c9a48cfac35e329127460bd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

而在DSU-110中， 连接到一致性总线的接口可以是CHI ,但不再有ACE了。如果你使用的是DSU-110，DSU Cluster做为CHI Master了，那么你一定是采用CMN的总线互联方式。 <img src="https://img-blog.csdnimg.cn/65c46af308e3431ba743c433f4bfb0ce.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 3.7 架构图示例

所以呢，你看到的系统架构图(也是近几年最常用的)，可能是下面这个样子的，所有的core都在一个DSU cluster中，所有core共享L3 cache，DSU接到CCI或CMN缓存互联一致性总线上，可以和其它ACE-Lite Master(如 GPU)共享缓存数据 <img src="https://img-blog.csdnimg.cn/84ce4ba91f494949b4cf0d0752da76d3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 当然了，举个稍微极端的例子，如下连接架构图也不是不可能，系统中有两个DSU cluster，DSU接到CCI或CMN缓存互联一致性总线上。 <img src="https://img-blog.csdnimg.cn/415c7ef3ff3f42979bf4ba1e8c04d567.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 事实上big.LITTLE架构的cluster，也是可以做为CHI Master。下面这种超极端的例子，技术理论上也是可行的(当然可能不会有人用)。 <img src="https://img-blog.csdnimg.cn/37459dc325124cce8c6d720988ed51a1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

##### 4、L1/L2/L3 cache的大小

可以参考ARM文档，
- 对于`big.LITTLE`架构的core，其cache大小基本是固定的。- 对于`dynamIQ`架构的core，其L1和L2 cache大小基本是固定的。但对于L2 cache 则是可选择可配置的 <img src="https://img-blog.csdnimg.cn/311684aecdbe4c1691a530dfe7e58425.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 另外查阅DSU TRM文档，可以看到L3 Cache可以配置 0 - 16MB的大小。 <img src="https://img-blog.csdnimg.cn/cbd05ff369ca4d03a77aef243c09bf56.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_8,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
##### 5、cache的组织形式(index, way, set)

cache的组织形式有：
- 全相连- 直接相连- 多路组相连（如4路组相连）
<img src="https://img-blog.csdnimg.cn/c56298d109564f9588796a89eeeafb01.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 在一个core中一个架构中一个SOC中，所有cache的组织形式并不是都一样的。即使L1 D-cache和L1 I-cache的组织形式，也都可能不是一样的的。 具体的组织形式是怎样的，需要查询你的core trm手册。

例如我们查询到Cortex-A53的cache信息如下：

>  
 **L1 I-Cache** 
 - 可配:8KB, 16KB, 32KB, or 64KB- cacheline:64bytes- 2路组相连- 128-bit的读L2 memory的接口  
 **L1 D-Cache** 
 - 可配:8KB, 16KB, 32KB, or 64KB- cacheline:64bytes- 4路组相连- 256-bit的写L2 memory的接口- 128-bit的读L2 memory的接口- 64-bit的读L1到datapath- 128-bit的写datapath到L1  
 **L2 cache** 
 - 可配置的: 128KB, 256KB, 512KB, 1MB and 2MB.- cacheline:64bytes- Physically indexed and tagged cache（PIPT）- 16路组相连的结构 


因为有了多路组相连这个cache，所以也就有了一些术语概念：
- index ： 用白话理解，其实就是在一块cache中，一行一行的编号(事实是没有编号/地址的)- Set ：用index查询到的cache line可能是多个，这些index值一样的cacheline称之为一个set- way：用白话来说，将cache分成了多个块（多路），每一块是一个way- cache TAG ：查询到了一行cache后，cachelne由 TAG + DATA组成- cache Data ：查询到了一行cache后，cachelne由 TAG + DATA组成- cache Line 和 entry 是一个概念
<img src="https://img-blog.csdnimg.cn/6f61c4c7a7b6470486a0b5e2427251a8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

##### 6、cache的种类(VIVT,PIPT,VIPT)

cache一般是有如下种类；
- PIPT- VIVT- VIPT
在一个core中一个架构中一个SOC中，你所使用的cache是哪种类型的，都是固定的，是软件改不了的。<font color="red" size="4"> **在ARM架构中，一般L1 cache都是VIPT的，其余的都是PIPT的**</font>。 VIPT和PIPT的原理，基本也都是一样的，只是硬件查询时稍微有一丁点的区别，在后续讲cache查询时会再次介绍。

那么，你还学什么VIVT？你为什么还要去理解VIVT的原理？你为什么还要去分析cache同名、重名的问题？ 这样的问题，在armv7/armv8/armv9架构中都是不存在的

##### 7、cache的分配策略(alocation,write-through, write-back)
-  <font color="blue" size="4"> **读分配(read allocation)**</font> 当CPU读数据时，发生cache缺失，这种情况下都会分配一个cache line缓存从主存读取的数据。默认情况下，cache都支持读分配。 -  <font color="blue" size="4"> **写分配(write allocation)**</font> 当CPU写数据发生cache缺失时，才会考虑写分配策略。当我们不支持写分配的情况下，写指令只会更新主存数据，然后就结束了。当支持写分配的时候，我们首先从主存中加载数据到cache line中（相当于先做个读分配动作），然后会更新cache line中的数据。 -  <font color="blue" size="4"> **写直通(write through)**</font> 当CPU执行store指令并在cache命中时，我们更新cache中的数据并且更新主存中的数据。cache和主存的数据始终保持一致。 -  <font color="blue" size="4"> **写回(write back)**</font> 当CPU执行store指令并在cache命中时，我们只更新cache中的数据。并且每个cache line中会有一个bit位记录数据是否被修改过，称之为dirty bit（翻翻前面的图片，cache line旁边有一个D就是dirty bit）。我们会将dirty bit置位。主存中的数据只会在cache line被替换或者显示的clean操作时更新。因此，主存中的数据可能是未修改的数据，而修改的数据躺在cache中。cache和主存的数据可能不一致 <img src="https://img-blog.csdnimg.cn/45e412e4b3a543eeb73fea1778adea4e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 
##### 8、架构中定义的cache的范围(inner, outer)

对于cacheable属性，inner和outer描述的是cache的定义或分类。比如把L1/L2看做是inner cache，把L3看做是outer cache。

通常，内部集成的cache属于inner cache，外部总线AMBA上的cache属于outer cache。例如:
- 对于big.LITTLE架构（A53为例)中，L1/L2属于inner cache，如果SOC上挂了L3的话，则其属于outer cache- 对于DynamIQ架构（A76为例)中，L1/L2/L3属于inner cache，如果SOC上挂了System cache（或其它名称）的话，则其属于outer cache
然后我们可以对每类cache进行单独是属性配置，例如：
- 配置 inner Non-cacheable 、配置 inner Write-Through Cacheable 、配置 inner Write-back Cacheable- 配置 outer Non-cacheable 、配置 outer Write-Through Cacheable 、配置 outer Write-back Cacheable <img src="https://img-blog.csdnimg.cn/d186c9acac7c434ea94396654ad9d19d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
对于shareable属性，inner和outer描述的是cache的范围。比如inner是指L1/L2范围内的cache，outer是指L1/L2/L3范围内的cache <img src="https://img-blog.csdnimg.cn/d1cc5bfadae84e958680558dbe1b3516.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

##### 9、架构中内存的类型

在arm架构中，将物理内存分成了device和normal两种类型 <img src="https://img-blog.csdnimg.cn/867c94c8049840cea325e83c29ed0ce8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

而是每种的内存下(device和normal)又分出了多种属性。ARM提供一个`MAIR`寄存器, 将一个64位的寄存器分成8个attr属性域，每个attr属性域有8个比特，可配置成不同的内存属性。 也就是说，在一个arm core，最多支持8中物理内存类型。 <img src="https://img-blog.csdnimg.cn/cd457fc58c6b490dbbeb91d4e78d96ad.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 而我们在MMU使用的页表的entry中的属性位中，BIT[4:2]占3个比特，表示index，其实就是指向MAIR寄存器中的attr。 （Attribute fields in stage 1 VMSAv8-64 Block and Page descriptors） <img src="https://img-blog.csdnimg.cn/2818b0bfe5ae43d2b7ea0d1c44df6a98.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 - **PBHA**, bits[62:59] ：for FEAT_HPDS2- **XN or UXN**, bit[54] ： Execute-never or Unprivileged execute-never- PXN, bit[53] ：Privileged execute-never- **Contiguous**, bit[52] ： translation table entry 是连续的，可以存在一个TLB Entry中- **DBM**, bit[51] ：Dirty Bit Modifier- **GP**, bit[50] ：for FEAT_BTI- **nT**, bit[16] ：for FEAT_BBM- **nG**, bit[11] ：缓存在TLB中的翻译是否使用ASID标识- **AF**, bit[10] ： Access flag, AF=0后，第一次访问该页面时，会将该标志置为1. 即暗示第一次访问- **SH**, bits[9:8] ：shareable属性- **AP**[2:1], bits[7:6] ：Data Access Permissions bits,- **NS**, bit[5] ：Non-secure bit- <font color="red" size="3">**AttrIndx**[2:0], bits[4:2] </font> 


也就是说，页表的每一个entry中，都指向MAIR寄存器中的一个属性域。也就是页表的每一个entry都配置了一种内存类型。 如下所示，便很好的展示了，MMU页表的每一个page descriptor(也叫entry)都指向一个内存属性类型。 <img src="https://img-blog.csdnimg.cn/9cb93e0f283d480ca40d35e0511e9c79.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

##### 推荐
-  --博客专栏-  --大课程-  --入门课程