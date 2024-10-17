
--- 
title:  银河麒麟之Workstation安装 
tags: []
categories: [] 

---
## 一、VMware Workstation简介

  VMware Workstation是一款由VMware公司开发的虚拟化软件，它允许用户在一台物理计算机上运行多个操作系统，并在每个操作系统中运行多个虚拟机。VMware Workstation提供了一个可视化的用户界面，使用户可以轻松创建、配置和管理虚拟机。   VMware Workstation支持多种操作系统，包括Windows、Linux和Mac OS X。它提供了许多高级功能，如快照、克隆、网络模拟和虚拟机共享。用户可以使用快照功能来捕捉虚拟机的状态，并在需要时恢复到该状态。克隆功能允许用户创建虚拟机的副本，以便在不同的环境中使用。网络模拟功能使用户能够模拟不同的网络环境，以测试和调试网络应用程序。虚拟机共享功能允许用户共享虚拟机，以便其他用户可以在其计算机上运行虚拟机。VMware Workstation还支持与其他VMware产品的集成，如vSphere和vCloud Air。这使用户可以轻松地将虚拟机从工作站移动到服务器或云环境中。环境说明：
- 操作系统：银河麒麟桌面版v10- Workstation版本：17 Pro
## 二、银河麒麟系统下Workstation安装步骤

### 1、下载workstations软件包

  访问VMware官网，找到Workstation 17 Pro for Linux，点击立即下载。 <img src="https://img-blog.csdnimg.cn/direct/ec265ff27d8e4f5ea067f5dcfa231576.png" alt="在这里插入图片描述">

### 2、添加可执行权限

  给下载的软件包VMware-Workstation-Full-17.5.0-22583795.x86_64.bundle添加可执行权限

>  
 root@wuhs-pc:/home/wuhs/Downloads# chmod u+x VMware-Workstation-Full-17.5.0-22583795.x86_64.bundle 


### 3、执行安装

  执行软件的安装需要root权限，我们可以切换root用户或者使用sudo执行，输入yes后开始安装。 <img src="https://img-blog.csdnimg.cn/direct/ff2f382a84464370bc1c8e38afac19d4.png" alt="在这里插入图片描述">

### 4、启动Workstation

  点击启动任务栏，点击VMware workstation启动应用程序。

<img src="https://img-blog.csdnimg.cn/direct/e0e2bd187dc7423db7e738f42cdf8bcb.png" alt="在这里插入图片描述">

### 5、接受协议

  弹窗是否接受VMware使用协议，这里选择接受，然后下一步。 <img src="https://img-blog.csdnimg.cn/direct/ecc18f67504442679f38ad729831f4f6.png" alt="在这里插入图片描述">

### 6、启动的时候是否检查更新

  设置程序是否启动的时候检查程序更新，我们这里选择否。 <img src="https://img-blog.csdnimg.cn/direct/0b57f4cd919343c48c056ee188f43a3d.png" alt="在这里插入图片描述">

### 7、是否加入用户体验计划

  是否加入用户体验计划，就是在遇到程序出错的时候可能会上传错误日志到VMware等，这里我们选择否。 <img src="https://img-blog.csdnimg.cn/direct/03639c31795c486a97204fd43ccd849a.png" alt="在这里插入图片描述">

### 8、是否马上激活

  是否激活，如果有授权licence，可以选择yes并输入授权码，博主没有licence，这里选择no。 <img src="https://img-blog.csdnimg.cn/direct/21f2d7ef2fcd4b72987960f01887af1b.png" alt="在这里插入图片描述">

### 9、输入sudo密码授权

  设置完成会要求输入管理员账户密码，这是因为我们登录的是普通用户，需要用户拥有sudo权限，输入用户密码完成授权。 <img src="https://img-blog.csdnimg.cn/direct/f1efef11ac034de49b4983c43b8cce86.png" alt="在这里插入图片描述">

### 10、开始使用

  看到如下界面说明VMware workstation在银行麒麟系统下安装完成。 <img src="https://img-blog.csdnimg.cn/direct/fb67019b165f4c46b49b682e925fa133.png" alt="在这里插入图片描述">

## 三、Workstation下安装虚拟机

### 1、上传一个操作系统iso文件到主机

  下载一个操作系统的iso文件并上传到主机上。

### 2、创建一个新虚拟机

  点击create按钮创建一个新虚拟机。 <img src="https://img-blog.csdnimg.cn/direct/b8bc60dbef634da5be467a6fd0c8cbf0.png" alt="在这里插入图片描述">

### 3、选择设置

  选择经典设置或者高级设置。 <img src="https://img-blog.csdnimg.cn/direct/908b3e1d434d4b178ea564ca97415f54.png" alt="在这里插入图片描述">

### 4、选择安装介质

  这里我们可以选择设置一个空白虚拟机，也可以选择安装介质，待启动的时候开始安装系统。 <img src="https://img-blog.csdnimg.cn/direct/0fc241e4e3c343fc92e5167c4dbf9e37.png" alt="在这里插入图片描述">

### 5、选择系统类型

  根据上传的介质设置系统类型，博主上传的是win7系统，这里选择window。 <img src="https://img-blog.csdnimg.cn/direct/ab3e19f18e944bdea21b3106f2681da0.png" alt="在这里插入图片描述">

### 6、设置虚拟机名称

  这一步设置虚拟机名称和存储路径。 <img src="https://img-blog.csdnimg.cn/direct/92ba075d563c461a93852b1e733daf0c.png" alt="在这里插入图片描述">

### 7、设置存储空间大小

  这里设置存储空间大小，这里设置为30G，并将虚拟机磁盘拆分成多个文件。 <img src="https://img-blog.csdnimg.cn/direct/b9efc08e1caf42a49f2488b87f1b47f0.png" alt="在这里插入图片描述">

### 8、虚拟机硬件配置

  设置虚拟机内存大小、网卡模式等硬件配置，内存默认2G，这里设置为4G。 <img src="https://img-blog.csdnimg.cn/direct/fe7cecf847f245a29293c02bcc94f8c8.png" alt="在这里插入图片描述">

### 9、启动安装报错

  博主这里的银河麒麟系统本身是运行在虚拟机上的，虚拟机上安装workstation基础上再安装虚拟机报错。这个错误通常是由于主机不支持Intel VT-x虚拟化技术引起的。虚拟化技术是一种在物理主机上创建和管理虚拟机的技术，需要主机的处理器支持。有条件的网友可以在物理机上安装银河麒麟系统，然后再安装workstation，再安装虚拟机，理论上跟windows系统环境下workstation安装虚拟机是一样的。 <img src="https://img-blog.csdnimg.cn/direct/690453a4db7e43f0882b5c1afb1ce32a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/cfdc806835504c639b4fae2da052447b.png" alt="在这里插入图片描述">
