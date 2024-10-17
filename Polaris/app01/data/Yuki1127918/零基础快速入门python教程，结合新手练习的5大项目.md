
--- 
title:  零基础快速入门python教程，结合新手练习的5大项目 
tags: []
categories: [] 

---
### 适合Python初学者的5大项目

在练手项目的选择上，还存在疑问？不知道要从哪种项目先下手？

**首先有两点建议：**

最好不要写太应用的程序练手，要思考什么更像是知识，老只会写写爬虫是无用的，但是完全不写也不行。

对于练手的程序，要注意简化和抽象，但是如果简化不得当的话，很容易看几篇教程就被懒得下手了。

接下来就给大家介绍几种适合新手的练手项目。

**0.算法系列－排序与查找**

Python写swap很方便，就一句话（a， b = b， a），于是写基于比较的排序能短小精悍。刚上手一门新语言练算法最合适不过了，还能顺便刷题，利于找工作。简单的练习，让你受益无穷。

**1.编译系列**

<img src="https://img-blog.csdnimg.cn/80a16f88fe5548cbb8171d436bc925b7.jpeg#pic_center" alt="在这里插入图片描述">

这个系列的重点就是前面说到的简化，但是不要指望一口气写一个完整的C编译器，即使只针对C一个很小的子集。所以我们需要一步一步来，写一个计算器的解释器是很好的开始，再进一步可以写一个极简语言的解释器，譬如brainfuck。

再进一步你可以扩展已有的计算器解释器，譬如加入声明、赋值与运算、循环、流程控制， 构成一个简单的LL（1）语法，然后递归下降分析，这就可以搞一个简易同时又图灵完备的玩具语言出来了。

**2.分布式系统/计网系列**

<img src="https://img-blog.csdnimg.cn/7ef5871cb08a40ed941fd392500fd573.jpeg#pic_center" alt="在这里插入图片描述">

这系列的项目，第一步可以从写一个简单的HTTP客户端开始，原因很简单，因为HTTP大概是最简单的应用层协议了。然后可以考虑实现一个基本的ssh，你大概每天都会用ssh，难道不想做一个自己的简易版本吗？

然后可以考虑分布式系统课上的经典作业，譬如写一个简单的RPC。可以参考Java的RPC原理以及Google的RPC框架（有Python版）。

**3.操作系统系列**

<img src="https://img-blog.csdnimg.cn/c2048ab667994cff937f885e0e8738ba.jpeg#pic_center" alt="在这里插入图片描述">

操作系统系列，可以尝试写一个简单的存储管理的文件系统。第一步的简化就是用一个大的空文件作为磁盘，把对磁盘的读写抽象成对这个文件的读写。基本就是实现下inode，然后包装成一个shell，支持下最基本的命令，新建、追加、读写、删除之类的操作。这个练习最有趣也最有意义的地方在于多级索引的实现，

**4.周边系列**

<img src="https://img-blog.csdnimg.cn/d91a4ff802f04323b1e42aac73502b4c.jpeg#pic_center" alt="在这里插入图片描述">

你也可以试试Jython，IronPython之类的，看看和CPython比如何。然后再试试Pypy，必然是一开始很高兴，最后发现各种常见库不支持，最后还是转回CPython

### 关于Python技术储备

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

#### 一、Python所有方向的学习路线

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。

<img src="https://img-blog.csdnimg.cn/img_convert/9f49b566129f47b8a67243c1008edf79.png" alt="">

#### 二、学习软件

工欲善其事必先利其器。学习Python常用的开发软件都在这里了，给大家节省了很多时间。

<img src="https://img-blog.csdnimg.cn/img_convert/8c4513c1a906b72cbf93031e6781512b.png" alt="">

#### 三、入门学习视频

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

<img src="https://img-blog.csdnimg.cn/afc935d834c5452090670f48eda180e0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56iL5bqP5aqb56eD56eD,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="">

#### 四、实战案例

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/img_convert/252731a671c1fb70aad5355a2c5eeff0.png" alt="">

#### 五、面试资料

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自阿里、腾讯、字节等一线互联网大厂最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/img_convert/6c361282296f86381401c05e862fe4e9.png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/d2d978bb523c810abca3abe69e09bc1a.png" alt="">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">
