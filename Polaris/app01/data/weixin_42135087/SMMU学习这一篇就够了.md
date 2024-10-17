
--- 
title:  SMMU学习这一篇就够了 
tags: []
categories: [] 

---
>  
 <font color="purple" size="5">**快速链接:**</font> .   
 -  <font color="red" size="3">**【购买须知】:**</font>- -  ----<font color="red" size="3">**联系方式-加入交流群**</font> 


>  
 **引流关键词**: SMMU，mmu500,mmu600,mmu700,system mmu,Non-cacheable,Cacheable, non-shareable,inner-shareable,outer-shareable, optee、ATF、TF-A、Trustzone、optee3.14、MMU、VMSA、cache、TLB、arm、armv8、armv9、TEE、安全、内存管理、页表… 


<img src="https://img-blog.csdnimg.cn/c1c680b0da63410f9b23203b3aadf60a.jpg?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="请添加图片描述"> 

#### 目录
- <ul><li><ul><li><ul><li>- - <ul><li>- - - - - - - <ul><li>- - - - - 


##### 前言

最近朋友圈、微信群(`ARM-Trustzone-TEE-AT`)掀起一阵学习SMMU的热潮，作为一名安全领域的<font color="red" size="4">渣渣</font> ，势必要蹭一蹭这个“热点”，也学习一下吧，反正早晚都要学，因为它和安全的关系还是比较大的。学习是一件长期的过程，本文就先简单理一下概念吧。

##### 1、SMMU总结

###### 1.1、SMMU的timeline

<img src="https://img-blog.csdnimg.cn/0d2b5335e7e544e88c41c00320e88bfa.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 1.2、SMMU的简介

SMMU的全称是System Memory Management Units， 它属于Arm的System IP， 主要给其他Master来使用，其连页表格式和Core MMU是一样的，理论上可以让Core的MMU和SMMU使用同一套页表.

<font color="blue" size="4"> 那么SMMU都是用在哪些地方呢？</font>*以下展示了一个usecase，来自arm官方博客（February 17, 2014），也是比较早期的一个Sample case <img src="https://img-blog.csdnimg.cn/6325c5c31809490a997daef8f64c8294.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 1.3、为什么要使用SMMU?
-  访问非连续的地址 现在系统中很少再预留连续的memory，如果Master需要很多memory，可以通过SMMU把一些非连续的PA映射到连续的VA，例如给DMA，VPU，DPU使用。 -  32位转换成64位 现在很多系统是64位的，但是有些Master还是32位的，只能访问低4GB空间，如果访问更大的地址空间需要软硬件参与交换memory，实现起来比较复杂，也可以通过SMMU来解决，Master发出来的32位的地址，通过SMMU转换成64位，就很容易访问高地址空间。 -  限制Master的访问空间 Master理论上可以访问所有的地址空间，可以通过SMMU来对Master的访问进行过滤，只让Master访问受限的区域，那这个区域也可以通过CPU对SMMU建立页表时动态控制。 -  用户态驱动 现在我们也看到很多系统把设备驱动做在用户态，调用驱动时不需要在切换到内核态，但是存在一些安全隐患，就是用户态直接控制驱动，有可能访问到内核空间，这种情况下也可以用SMMU来实现限制设备的访问空间 -  设备虚拟化 例如设备虚拟化有多种方式，Emulate，Para-virtualized，以及Pass-through，用SMMU可以实现Pass though，这样无论是性能，还是软件的改动都是比较小的。 -  一些不支持TrustZone的Master，可以利用SMMU支持Trustzone 
##### 2. SMMU原理解读

###### 2.1. SMMU的使用模型

SMMU全称System Memory Management Unit，其实SMMU和MMU具有同样的作用，区别是供给Master使用，同样提供页表转换工作，Master可通过页表转换访问物理地址，达到Master一样使用虚拟地址

<img src="https://img-blog.csdnimg.cn/91d55c54f32a4404b238f25bb8a4b757.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_16,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

官方给出的示例图如下所示： <img src="https://img-blog.csdnimg.cn/cd8087a14d97468f83f116bee1204163.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 示例图2： <img src="https://img-blog.csdnimg.cn/101656d1f7d347bfa25af9ed0a17e790.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 2.2. SMMU的硬件原理图

学过MMU的人都知道，MMU是由 `TLB + Address Translation`, 那么对于SMMU呢？ 它是由TBU + TCU组成，其中TBU中含有TLB， TCU缓存地址翻译。 DTI则是SMMU内部的连接总线的协议。 <img src="https://img-blog.csdnimg.cn/7631029e1d2e41a38e1f8ccb5b5e9205.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

而一个SMMU中可以放置多个`ACE-Lite TBU`模块，也可以放置`LTI TBU` <img src="https://img-blog.csdnimg.cn/18ca1bbae21543908b086c77104b892f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

TBU原理图 <img src="https://img-blog.csdnimg.cn/0ff7afc7fc984322bc09c2d8d5f82939.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

LTI TBU的原理图 <img src="https://img-blog.csdnimg.cn/b250d8ab9d2c4a0f9c47b59076495688.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_16,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> TCU的原理图 <img src="https://img-blog.csdnimg.cn/bf6e890fdbd6449b88662ea94001e67c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 2.3. StreamID

###### 2.4 STE Table 和 STE format

STE Table 分为`Linear Stream Table`和`mutil-level Stream Table`，这是由于`STRTAB_BASE_CFG`中的比特位配置

###### 2.4.1 一个 Linear Stream Table的示例

这种查询方式很简单，根据streamID的数值，直接查询到对应的STE（streamID entry） <img src="https://img-blog.csdnimg.cn/9d3cf7a648544df1a269e9f6c6167fb8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_7,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 2.4.2 一个 2-level Stream Table 的示例

<img src="https://img-blog.csdnimg.cn/f56ea5c1821c4e0db35fa8482975abd7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7673c671fa994cdeb6a55b486da79adf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 2.4.3 Multi-level Stream and CD tables

而事实上，一个STE，又可以对应多个Context Descriptor <img src="https://img-blog.csdnimg.cn/000055185ccc4d33b721ab34e702d14d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 这里小小总结一下： 这里的一个Context Descriptor 就相当于 MMU系统中的 TTBRx + TCR寄存器。 这里Stage 1 Transslation tables的格式和MMU页表的格式一致。

###### 2.4.4 Translation stages and addresses

地址翻译也是份stage1和stage2的，这和MMU也是一致的。 <img src="https://img-blog.csdnimg.cn/6d9ac7290b384b119d58aecd7b45eaf0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_9,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 2.4.5 Configuration and translation lookup sequence

SMMU地址翻译的原理或数据里如下图所示，这是在学习MMU的时候未曾见过的那么细致的图。 <img src="https://img-blog.csdnimg.cn/51cf7dc9c99249f98418a0aa69f54412.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 2.4 寄存器的介绍

SMMU寄存器都是memory-map的 <img src="https://img-blog.csdnimg.cn/8eab3125bd6a4123bc28fabed54c09eb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

SMMU里有两套寄存器，一套是给安全master用的，一套是给非安全master用的。 其实就相当于有两个SMMU了。如下我也列举了几个特别的寄存器，带S的是给安全用的，不带S的是给非安全用的。所以，硬件仅仅有一块SMMU，但从软件的视角来看，有两块SMMU
- SMMU_STRTAB_BASE- SMMU_S_STRTAB_BASE- SMMU_STRTAB_BASE_CFG- SMMU_S_STRTAB_BASE_CFG
##### 2.5 Stream Table Entry

<img src="https://img-blog.csdnimg.cn/a6b4bdb7a41740cc9ed47113428a87b0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

###### 2.6 Context Descriptor table

可以看出，这里的Context Descriptor 就有点类似于MMU里的 TTBRx + TCR寄存器的味道 <img src="https://img-blog.csdnimg.cn/ce0a4a91ab6a4eafbd01cad79e05b968.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Luj56CB5pS55Y-Y5LiW55WMY3R3,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/461ab09d460342c6b0c0e97499bb4299.png" alt="在这里插入图片描述">

##### 3. 总结
- （1）MMU 只能给 一个core用。而SMMU想给多个master用，多个master又对应不同的表。所以就搞了个STE。每一个STE entry里，都可以指向多个context descriptor （我觉得一般也就只用一个吧），然后每一个context descriptor 就相当于 MMU的TTBRx + TCR寄存器。 context Descriptor之后，就和普通的MMU一样- （2）SMMU里有两套寄存器，一套是给安全master用的，一套是给非安全master用的。从软件视角来看，其实就相当于有两个SMMU了。但这不是banked，他们的寄存器名字不一样，一类带了S，一类不带S。而且寄存器memory-map的地址还不一样。- （3）SMMU又有Secure STE 和 Non-secure STE的概念， Secure STE 后面的页表/地址转换，可以转secure memory，也可以转non-secure memory。Non-Secure STE 后面的页表/地址转换，只可以转non-secure memory。 这和MMU里的Descriptor里的NS比特也是一样的。
##### 推荐
-  --博客专栏-  --大课程-  --入门课程