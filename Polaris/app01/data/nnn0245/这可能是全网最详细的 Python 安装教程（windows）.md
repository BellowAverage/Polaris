
--- 
title:  这可能是全网最详细的 Python 安装教程（windows） 
tags: []
categories: [] 

---
Python 是这两年来比较流行的一门编程语言，主要卖点是其相对简单的语法以及丰富的第三方库，下面我来带大家安装、配置 Python。

（文章最后有各种疑难杂症的解决方法！）

###  大体步骤有两步：
1. 安装 Python，让电脑学会这门语言1. 配置编辑器，方便我们编辑代码、调动 Python
## **安装 Python**

（Python、Sublime 官方下载地址是外国的服务器，所以会很慢，下载有问题的私聊我拿网盘链接） 很多人会推荐 Anaconda（400M以上），但实际上原版 Python（26M）对新手来说就足够了 直接官网下载： 有部分喜欢用360安装的电脑小白，建议改掉这个坏习惯，因为360可能会夹带私货，对软件进行改装，官网它不香吗？ 点开上面的链接，会发现有很多版本

<img alt="" height="396" src="https://img-blog.csdnimg.cn/4d5d521fa62a4c1fafc796eedc14daf2.png" width="604">

首先看版本，x86-64是64位版本，x86是32位版本，你需要下载跟你电脑系统一致的版本。

怎么看自己的电脑是什么版本？

## 

## 右键计算机-属性

 <img alt="" height="348" src="https://img-blog.csdnimg.cn/4cb0988a28bc4eeabcd77d41d701fb6d.png" width="332">

查看系统类型

<img alt="" height="175" src="https://img-blog.csdnimg.cn/2c6aa4ca1e204dbca5ee4e699d1e4a8f.png" width="638">

## 然后再看文件类型

<img alt="" height="247" src="https://img-blog.csdnimg.cn/7a7cbe6bc64b4b6385ec9482f6c62d47.png" width="415">



embeddable zip file 是压缩包版本，即便携版，解压可用

executable installer 是可执行的安装版本，即离线版，下载到本地后可以直接安装

web-based installer 是联网安装版，体积很小，但需要保持网络畅通



建议使用离线安装版（executable installer），这样软件会帮你设置系统变量，否则需要自己添加，对新手来说当然越傻瓜化越好

## 下载后打开

 <img alt="" height="420" src="https://img-blog.csdnimg.cn/329c18ffc5db481cbe8f4cf4e86bf2f1.png" width="671">

如果出现上面这个界面的话，说明你的电脑已经安装过 Python 了，直接关掉窗口，跳到教程的下一步。

如果你是第一次安装，应该是这个界面：

<img alt="" height="425" src="https://img-blog.csdnimg.cn/91debe80122b48ba8dcce7fa71172840.png" width="683">

 <img alt="" height="424" src="https://img-blog.csdnimg.cn/d7a68197f1dd408a998fe9f49f356686.png" width="678">

<img alt="" height="421" src="https://img-blog.csdnimg.cn/09d743ddf4d6454f85721a58ca2a656c.png" width="678">

<img alt="" height="422" src="https://img-blog.csdnimg.cn/5ca1928ace0141fcbca29fbad0b757e5.png" width="677">

<img alt="" height="419" src="https://img-blog.csdnimg.cn/1845d4aee65943868e864f718d9bb4bf.png" width="674">



## 成功！



测试一下，能否调用，同时按下win+R（win就是开始菜单那个键）

 <img alt="" height="307" src="https://img-blog.csdnimg.cn/f868ad9dbae44633beaee63dfc2ddfe5.png" width="540">

进入命令行，输入python，出现这样的界面则表示成功安装

<img alt="" height="201" src="https://img-blog.csdnimg.cn/e7ceebf8a4e1439683c7453e0f6a69d3.png" width="664">

这样我们第一步就完成了！电脑已经成功学会了Python语言！

（要是我们学语言也这么快就好了）



输入 print('Hello,World!')，写下你的第一句 Python 代码

 <img alt="" height="196" src="https://img-blog.csdnimg.cn/cd07f9f0478c4828b50fcc5df1e28fb0.png" width="671">

欢迎来到 Python 的世界！

当然，我们以后是不可能在这个黑框框里写代码的，多不方便啊，所以还要另外安装编辑器



ctrl+Z，回车即退出 Python 环境

<img alt="" height="234" src="https://img-blog.csdnimg.cn/d120377965564382925a5d0b71bea4c2.png" width="664">

另外，我们还要测试一下 pip 有没有安装好，pip 是用来安装第三方库的神器，这个我们以后会接触到。

退出了 Python 环境后，我们输入 pip 回车

 <img alt="" height="305" src="https://img-blog.csdnimg.cn/1207b9bc6e7b459f9a8e5d96bf5db07a.png" width="648">

<img alt="" height="45" src="https://img-blog.csdnimg.cn/2cd78f7e74ad4ffcbe9c14f682ee08b6.png" width="512">






