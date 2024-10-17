
--- 
title:  Linux之iDrac服务模块安装 
tags: []
categories: [] 

---
## 一、需求说明

  通过iDrac带外管理Dell服务器的时，点击主机操作系统提示“访问RAC0690: 服务器的操作系统中未安装 iDRAC Service Module。 安装服务模块，然后重试该操作”。这是因为操作系统未安装dell官方的iDRAC Service Module模块，安装完成模块后就可以查看相关信息了。 <img src="https://img-blog.csdnimg.cn/85daa6372d654f5e8d59a3f58840a406.png" alt="在这里插入图片描述">

## 二、安装步骤

### 1、下载软件包

  访问官网链接https://www.dell.com/support/home/zh-cn/drivers/driversdetails?driverid=rx6p0，点击下载按钮将软件包下载到本地，下载的版本是Dell EMC iDRAC Service Module for Linux，v4.2.0.0。centos7操作系统最高可以安装V4.2，iDrac Service Module V4.3以上版本只支持centos8以上的操作系统。 <img src="https://img-blog.csdnimg.cn/67cf044c340a49b39ed93428965b0743.png" alt="在这里插入图片描述">

### 2、上传软件包并验证

  将下载的软件包上传到服务器并验证MD5值是否为3f982a7b0b62e6c36e49a319f68107c3 。验证对比与官网值一致说明下载的软件包完整且安全。

>  
 [root@s100 opt]# ll OM*.tar.gz -rw-r–r-- 1 root root 26576318 Oct 12 09:31 OM-iSM-Dell-Web-LX-4200-2581_A00.tar.gz [root@s100 opt]# md5sum OM-iSM-Dell-Web-LX-4200-2581_A00.tar.gz 3f982a7b0b62e6c36e49a319f68107c3 OM-iSM-Dell-Web-LX-4200-2581_A00.tar.gz 


### 3、解压软件包

>  
 [root@s100 opt]# mkdir idracservice [root@s100 opt]# tar -zxvf OM-iSM-Dell-Web-LX-4200-2581_A00.tar.gz -C idracservice/ 


### 4、安装依赖包

  直接执行安装脚本会报错“ usbutils is needed by dcism-4.2.0.0-2581.el7.x86_64”，我们先安装usbutils依赖包。

>  
 [root@s100 idracservice]# yum install usbutils -y … Installed: usbutils.x86_64 0:007-5.el7  Dependency Installed: libusbx.x86_64 0:1.0.21-1.el7  Complete! 


### 5、执行安装脚本

  进入解压目录后，sh setup.sh执行安装脚本，实际上主要安装两个rpm文件，dcism-osc-6.2.0.0-117和dcism-4.2.0.0-2581.el7。

>  
 [root@s100 opt]# cd idracservice/ [root@s100 idracservice]# ll total 100 -rwxr-xr-x 1 root root 1120 Jan 4 2022 install.ini drwxr-xr-x 2 root root 81 Jan 4 2022 OSC drwxr-xr-x 3 root root 111 Jan 4 2022 prereq drwxr-xr-x 3 root root 20 Jan 4 2022 RHEL7 drwxr-xr-x 3 root root 20 Jan 4 2022 RHEL8 -rwxr-xr-x 1 root root 94300 Jan 4 2022 setup.sh drwxr-xr-x 3 root root 20 Jan 4 2022 SLES15 drwxr-xr-x 3 root root 20 Jan 4 2022 UBUNTU20 [root@s100 idracservice]# sh setup.sh 


### 6、输入y,i后开始安装

  启动安装脚本后输入y接受协议，输入i开始安装。需要安装的组件我们可以通过数字选择，输入数字回车表示选择或者取消，x表示选择安装，空表示不安装。这里我们选择默认内容，直接输入i开始安装。 <img src="https://img-blog.csdnimg.cn/bebd653b6cad424eb96dbcf7aff503a0.png" alt="在这里插入图片描述">

### 7、安装完成后启动服务

  安装完成之后会提示是否启动服务，输入y或者yes可以启动服务。 <img src="https://img-blog.csdnimg.cn/ca6d47f26ede4ae891f6ce138418c085.png" alt="在这里插入图片描述">

### 8、查看检查服务

  通过ps -ef |grep iSM查看服务进程，也可以通过systemctl status dcismeng查看服务状态。 <img src="https://img-blog.csdnimg.cn/e2fbe97ddc2847a684a44399d60e4ecb.png" alt="在这里插入图片描述">

## 三、验证和管理iDrac Service Module服务

### 1、验证iDrac Service Module服务

  根据官网介绍iDRAC Service Module (iSM) 是轻量级软件服务，可更好地集成操作系统 (OS) 功能与 iDRAC，并且可以安装在戴尔的 yx2x 或更高版本的 PowerEdge 服务器上。iSM 可向 iDRAC 提供操作系统相关的信息，并且添加了向操作系统日志复制 LC 日志事件、WMI 支持（包括存储）、iDRAC SNMP 提醒（通过操作系统）、iDRAC 硬重置以及远程完全重启等功能。iSM 可自动执行 SupportAssist 报告收集流程，以便 iDRAC 可以更快地解决问题。iSM 对主机处理器的影响非常小，并且与 Dell EMC OpenManage Server Administrator (OMSA) 等“带内”代理相比占用的内存空间更少，因此可以将 iDRAC 管理扩展到受支持的主机操作系统。通过带外地址登录服务器，再次点击主机操作系统，可以看到网络接口信息，博主的实验环境是centos7、iDrac 7版，该模块只能查看主机的网卡配置和状态信息。实际上我们通过虚拟控制台也可以查看服务器IP地址，可以实现类本地连接，不过此功能需要购买licence，而iDrac Service Module模块是免费的。 <img src="https://img-blog.csdnimg.cn/dbf47dbbb1ac4dd28386d65841ccb56f.png" alt="在这里插入图片描述">

### 2、管理iDrac Service Module服务
- 启动服务
>  
 [root@s100 idracservice]# systemctl start dcismeng 

- 停止服务
>  
 [root@s100 idracservice]# systemctl stop dcismeng 

- 查看服务状态
>  
 [root@s100 idracservice]# systemctl status dcismeng 

