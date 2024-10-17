
--- 
title:  VirtualBox新建虚拟机 
tags: []
categories: [] 

---
**目录**







### 引言

新建虚拟机之前需要确保已下载iso镜像文件，以前下载过没有删除的，可以重复使用

iso是系统镜像，里面只有系统的安装程序，虚拟机装完，可进行删除

iso镜像文件官方下载网址：

<img alt="" height="684" src="https://img-blog.csdnimg.cn/1d5e1d7c5cde42dbb27cb207fd429ba6.png" width="1200">

若官网下载过慢，可点击该网址：

进入网址文档，有其他网址可供选择 

### 一、新建虚拟机

点击新建

<img alt="" height="740" src="https://img-blog.csdnimg.cn/c1bf3638ac62460eb7342573c6000de9.png" width="1200">

输入名字，选择系统，以及存放的文件夹

注意：文件夹必须是新建文件夹 若为上一个虚拟机所存放的文件夹 则会报错

<img alt="" height="772" src="https://img-blog.csdnimg.cn/194e6a71333c41918f0b0d331efe8dae.png" width="676">

分配内存大小

<img alt="" height="772" src="https://img-blog.csdnimg.cn/c20b0580730d44b4b72f71eb7a41b9a6.png" width="676">

创建虚拟硬盘

<img alt="" height="772" src="https://img-blog.csdnimg.cn/12c098aafea14091b5bb17c8ba875a15.png" width="676">

选择硬盘文件类型

<img alt="" height="892" src="https://img-blog.csdnimg.cn/ccf9339a99f94ea0b2c12764627d33d4.png" width="676">

>  
 上面的虚拟硬盘共有三种，这三种格式区别如下： 
 VDI，是 vbox 自己的虚拟硬盘格式 VHD ，是 Microsoft 支持的虚拟硬盘文件格式 vmdk，是 VMWare 等其他虚拟化厂商支持的虚拟硬盘格式 三种如何选择，可以看图片上面给出了导向提示：如果您不需要其他虚拟化软件使用它，可以保持默认配置，也就是，看你是否会使用其他软件比如 VM 来使用虚拟硬盘。一般默认选择 VDI 即可。 


选择分配方式 默认动态即可

<img alt="" height="892" src="https://img-blog.csdnimg.cn/df5f1f254abc4dc4bee80f7b7cf30556.png" width="676">

虚拟硬盘的位置默认即可 硬盘大小根据自己需要 自由设置

不过这里建议，在主机磁盘空间足够的情况下，尽量分配充足的空间，避免后续虚拟机硬盘空间不足的情况，到时候再扩容比较麻烦

<img alt="" height="892" src="https://img-blog.csdnimg.cn/575394b507144d6cb16061a8ccaed263.png" width="676">

###  二、虚拟机系统安装

启动新建的ubuntu虚拟机

<img alt="" height="626" src="https://img-blog.csdnimg.cn/2ed50a5896df4964be3e01f796ab0971.png" width="644">

选择启动盘是选择已经准备好的系统镜像（iso)，点击启动，开始安装系统 

<img alt="" height="746" src="https://img-blog.csdnimg.cn/385c75102e2344e6b7f08b337eb0c195.png" width="804">

 点击安装Ubuntu

<img alt="" height="746" src="https://img-blog.csdnimg.cn/c4c28dcb25274c22b43465da9ef5eabf.png" width="804">

这里建议选择“最小安装”，速度快，再就是没必要默认装那些乱七八糟的东西占用空间。

<img alt="" height="746" src="https://img-blog.csdnimg.cn/ca9cfce359b646188c25e3e0234e8e90.png" width="804">若窗口过小 无法显示下面的继续选项 win+鼠标右键 即可进行拖拽<img alt="" height="746" src="https://img-blog.csdnimg.cn/e7509405fb9e44ad8081078d8300fdf8.png" width="804">

 设置用户名以及密码

<img alt="" height="746" src="https://img-blog.csdnimg.cn/7fa21134dfae443aa2af0f3e90bdd91c.png" width="804">

等待系统安装

<img alt="" height="746" src="https://img-blog.csdnimg.cn/d9e2b21517fe4d46a9984f9b47aed879.png" width="804"> 安装完毕

<img alt="" height="746" src="https://img-blog.csdnimg.cn/67720921f65d48f3bc83b1d1fcb16c6e.png" width="804">

 不用重启，直接点击退出虚拟机

<img alt="" height="274" src="https://img-blog.csdnimg.cn/b955c1aae12a4ff899b6bb600d8aba14.png" width="876">

 再次启动即可正常使用

<img alt="" height="746" src="https://img-blog.csdnimg.cn/e440927fbd864b10be221dc5b1849892.png" width="804">

 ctrl+c键可以切换大小屏  注意ctrl一定是位于键盘右侧的才可以
