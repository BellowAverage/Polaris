
--- 
title:  比Python快6.8万倍的新语言开放下载了yyds 
tags: []
categories: [] 

---
来源丨量子位

什么编程语言，敢号称是高性能版的“Python++”？

新语言**Mojo**，来自LLVM之父和Swift之父Chris Lattner，性能可达到目前版本Python的**68000**倍。

<img src="https://img-blog.csdnimg.cn/img_convert/d4a9f0cbe7d394e5f986e0704c0c66f6.png" alt="d4a9f0cbe7d394e5f986e0704c0c66f6.png">

你没看错，几个月前团队还宣称是35000倍，换了台机器测评就成了68000倍。

现在，Mojo终于开放编译器和完整本地开发环境的下载，首日就在开发社区引发轰动。

<img src="https://img-blog.csdnimg.cn/img_convert/a9130938d5473ec96fc1158d95e712e1.png" alt="a9130938d5473ec96fc1158d95e712e1.png">

它语法像Python一样简单，跑起来像C++一样快，更重要的是可以与任何Python库无缝交互。

<img src="https://img-blog.csdnimg.cn/img_convert/876325a82da47424434fd170addb4ef0.png" alt="876325a82da47424434fd170addb4ef0.png">

由于Numpy、Pandas、SciPy这些大家已经熟悉的老朋友都能继续用，受到AI开发者的格外关注，英伟达科学家范麟熙表示：

>  
  可能是Python生态系统多年来最重要的升级，等了很久，终于来了！ 
 

<img src="https://img-blog.csdnimg.cn/img_convert/7b245744ca963898728d397de0097723.png" alt="7b245744ca963898728d397de0097723.png">

### 创始人：Mojo对Python不是威胁，C++们应该害怕

Mojo是如何做到比Python快这么多倍的？团队写了3篇技术解读，简单总结如下：

第1步，通过**类型注释**消除Python动态类型的损失，并做**代数简化**（algebraic simplifications），避免开方运算以及简化复数平方运算，达到**89****倍**加速。

第2步，通过向量化实现**SIMD**（单指令多数据）的并行计算，并让向量宽度以匹配CPU的FMA（浮点乘法累加单元）数量，达到**874倍**。

第3步，把前两步开发好的单线程实现改成**多核并行化**，对于88核的系统再获得30倍加速，与原始Python相比已经到了**26000倍**。

第4步，解决并行化中的**加载不均衡**问题，让线程从池中动态获取任务，得到最终结果**68000****倍**。

<img src="https://img-blog.csdnimg.cn/img_convert/9fe0975c4baa9412b5d71d7ca975d724.png" alt="9fe0975c4baa9412b5d71d7ca975d724.png">

这与之前宣传的35000倍不同，主要是中途换过一次测评基准系统，从32核的英特尔至强金牌6455B换成了88核的英特尔至强白金8481C。

此前，Mojo已可通过在线Playground形式试用，4个月来已积攒**12万开发者**。

<img src="https://img-blog.csdnimg.cn/img_convert/37ff9bc8798fe654cdc8881800646281.png" alt="37ff9bc8798fe654cdc8881800646281.png">

这一次是Mojo编译器和IDE工具首次开放本地下载，从Linux开始，后续将添加Mac和Windows支持。

<img src="https://img-blog.csdnimg.cn/img_convert/bc9cf3f09846a2bf7a039ce2949a1b00.png" alt="bc9cf3f09846a2bf7a039ce2949a1b00.png">

一同开放的还有支持语法高亮和代码补全等实用功能的**VSCode插件**。

<img src="https://img-blog.csdnimg.cn/img_convert/a38a8e4e208f66a8c0d09a0571921510.png" alt="a38a8e4e208f66a8c0d09a0571921510.png">

甚至可以像Python一样在**Jupyter**里交互式操作。

<img src="https://img-blog.csdnimg.cn/img_convert/1bf7e66914ed7f6fde85f387801895bc.png" alt="1bf7e66914ed7f6fde85f387801895bc.png">

手快的网友已经在争相晒各种版本的“Hello world”。

<img src="https://img-blog.csdnimg.cn/img_convert/469136ae9c0c16478c1783753a021249.png" alt="469136ae9c0c16478c1783753a021249.png">

<img src="https://img-blog.csdnimg.cn/img_convert/cc95ae50d21ecbd3b5291de20f989702.png" alt="cc95ae50d21ecbd3b5291de20f989702.png">

对于“Python会被取代吗这样的讨论”，Mojo创始人Chris Lattner本人认为：

>  
  Mojo并不是对Python的威胁，而是给Python开发者增加超能力。 
  如果谁应该害怕，应该是C++这种不易用的高速语言。 
 

<img src="https://img-blog.csdnimg.cn/img_convert/a1abaea016aa35ab319f1d5c44db90f6.png" alt="a1abaea016aa35ab319f1d5c44db90f6.png">

虽然Mojo很强大，但还是被网友发现一个“致命”缺点。

作为一门新语言，**AI们还没学会，**想学习就得靠自己了。

不过应该也可以把文档发给AI，让它现学试试？

### 背后公司Modular融资1亿美元

**Chris Lattner**毕业于波特兰大学，领导了LLVM、Clang等知名编译器项目，并牵头开发苹果Swift语言。

2017年离开苹果后，他先后在特斯拉短暂领导过自动驾驶Autopilot软件团队，在谷歌负责Tensorflow基础设施，在RISC-V架构的领军公司SiFive负责工程和产品团队。

<img src="https://img-blog.csdnimg.cn/img_convert/184ecc1e8cb1b3d1480014d4dfa61c34.png" alt="184ecc1e8cb1b3d1480014d4dfa61c34.png">

也是在这一时期，他透露自己正在搞AI基础设施方向的创业。

新公司**Modular**，致力于构建出模块化、可组合和分层架构的AI基础设施。

包括创建编译器、运行时环境，为异构计算设计、边缘和数据中心并重，并专注于可用性。

共同创始人**Tim Davis**，此前在谷歌团队参与了TF Lite、 Android ML、NNAPI等项目的编译器开发。

2023年8月，Modular获得1亿美元融资，总融资额达1.3亿美元。

<img src="https://img-blog.csdnimg.cn/img_convert/a3538891c6fb7119ff94475595030f18.png" alt="a3538891c6fb7119ff94475595030f18.png">

为AI开发者创建结合Python的可用性与C++的性能的Mojo语言是其第一步。

今后在Modular创建的AI引擎中，所有代码都可以用Mojo一种语言编写，无需再使用C、C++或CUDA编程。

那么，你会尝试使用这款新语言么？

参考链接：[1]https://www.modular.com/blog/mojo-its-finally-here[2]https://www.modular.com/blog/mojo-a-journey-to-68-000x-speedup-over-python-part-3[3]https://x.com/DrJimFan/status/1699841214416318672****










