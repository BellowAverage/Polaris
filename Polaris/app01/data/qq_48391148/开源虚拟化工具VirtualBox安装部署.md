
--- 
title:  开源虚拟化工具VirtualBox安装部署 
tags: []
categories: [] 

---
### 什么是Virtualbox 

>  
 **VirtualBox是一款由Oracle开发和维护的免费开源虚拟化软件，用于在一台计算机上创建和管理多个虚拟机。它允许用户在单个物理计算机上运行多个操作系统，例如Windows、Linux、macOS等。VirtualBox提供了一个虚拟化环境，使用户可以在虚拟机中安装和运行不同的操作系统，并在它们之间进行快速切换。 VirtualBox提供了一系列功能，包括虚拟机快照、网络配置和共享、虚拟硬盘管理、剪贴板共享等。用户可以根据自己的需求调整虚拟机的硬件资源分配，例如内存、处理器核心数量、网络适配器等。虚拟机的运行和控制可以通过VirtualBox的图形用户界面（GUI）进行操作，也可以通过命令行界面进行管理。 通过VirtualBox，用户可以进行多种用途，包括软件开发和测试、操作系统学习和实验、应用程序兼容性测试等。它还可以用于创建隔离的测试环境、快速部署虚拟机、远程访问虚拟机等。 总的来说，VirtualBox是一个功能强大、易于使用的虚拟化软件，可以帮助用户轻松地创建和管理多个虚拟机，并在不同操作系统之间进行无缝切换和交互。** 


>  
 **VirtualBox是完全免费的虚拟化软件。Oracle以GNU通用公共许可证（GPL）版本2的条款将VirtualBox发布为开源软件，这意味着任何人都可以免费下载、使用和修改VirtualBox的源代码。您可以从VirtualBox官方网站上获取免费版本，并在个人或商业环境中使用它。虽然VirtualBox提供了一些高级功能的付费版本，但免费版本已经非常强大且功能齐全，适合大多数用户的需求。 ** 


### VirtualBox下载网站：



>  
 **windows版本：** 




<img alt="" height="28" src="https://img-blog.csdnimg.cn/bbee471ca8a74368974174911ca04692.png" width="624"> 

<img alt="" height="399" src="https://img-blog.csdnimg.cn/90bcf2892e1045149b03277462d9c043.png" width="509">

<img alt="" height="399" src="https://img-blog.csdnimg.cn/5f410f9986b7479ba88f16901f9fc74d.png" width="509"> 

>  
 **后面没什么要注意的地方，一直点下一步即可，直到安装完成，然后打开virtualbox** 


<img alt="" height="739" src="https://img-blog.csdnimg.cn/21cc8f1bed3342c1bde42e3d8ff49e52.png" width="1200">

>  
 ** 修改虚拟机默认位置，不修改默认会放在C盘下面。** 


<img alt="" height="739" src="https://img-blog.csdnimg.cn/b474f38bae7f4a989fa678484499d52c.png" width="1200">

 新建一台虚拟机，配置名字，镜像。 

<img alt="" height="644" src="https://img-blog.csdnimg.cn/74af87920a244bd99412917f9dfb86a2.png" width="1200">

 <img alt="" height="385" src="https://img-blog.csdnimg.cn/cc7a8e803c354da183be9d811800a807.png" width="729">

<img alt="" height="385" src="https://img-blog.csdnimg.cn/3205bf7d04a7415c83e4b0528c26a7bb.png" width="729"> 

<img alt="" height="385" src="https://img-blog.csdnimg.cn/addb3319570a41dfa7d6b172adafc1b1.png" width="729"> <img alt="" height="739" src="https://img-blog.csdnimg.cn/fcb91c3c2b154258b01ef0137f55e4a2.png" width="1200">

>  
 ** 然后按照正常流程去安装一个centos7的系统就ok了** 


<img alt="" height="678" src="https://img-blog.csdnimg.cn/5e69d7dcc8d34028b9f402f73b93ef08.png" width="816">

### <img alt="" height="678" src="https://img-blog.csdnimg.cn/0251b82e27074c28896bfd3c0f8cd468.png" width="816">** 热键设置：**

>  
 **        virtualbox用起来挺简单，但是这里会有一个鼠标抢占的问题，即鼠标点入虚拟机以后，就会被虚拟机抢占，除非关闭虚拟机，不然鼠标就无法退出来了，所以有一个热键功能，使用快捷键以后就会自动退出虚拟机，我这里设置的是F1自动退出。** 


<img alt="" height="678" src="https://img-blog.csdnimg.cn/fa04480e6912447495e10c74bcb34f7e.png" width="816">

 <img alt="" height="404" src="https://img-blog.csdnimg.cn/7dd958d949ca4ef48a331d50e39e3b5f.png" width="446">

###  快照设置

>  
 **virtualbox也提供了快照功能，可以迅速的对系统当前状态进行一个备份，并在需要的时候返回至系统备份前的状态。** 


<img alt="" height="739" src="https://img-blog.csdnimg.cn/dece868f28e64f5caa095c2823707c39.png" width="1200">

 

 

 

 
