
--- 
title:  银河麒麟之NVIDIA GeForce显卡驱动安装 
tags: []
categories: [] 

---
## 一、银河麒麟系统介绍

  银河麒麟桌面版V10SP1是一款基于Linux操作系统的桌面操作系统，由中国科学院软件研究所开发。该版本在V10的基础上进行了优化和升级，提供更稳定、更高效的桌面体验。银河麒麟桌面版V10SP1集成了大量常用的应用程序和工具，包括办公软件、多媒体播放器、浏览器等，满足用户日常办公和娱乐需求。同时，该版本还支持多种硬件设备和外部设备的连接，提供更好的兼容性和易用性。银河麒麟桌面版V10SP1还具有良好的安全性和稳定性，内置防火墙、杀毒软件等安全工具，保护用户的数据安全。同时，该版本还提供了丰富的定制和个性化功能，用户可以根据自己的需求对系统进行自定义设置。目前银河麒麟桌面版V10SP1已经广泛部署在国产信创环境和政府办公终端。博主实验环境说明：
- 操作系统：银河麒麟桌面版V10.1- 显卡：NVIDIA GeForce GTX 1060- 显卡驱动版本：550.54.14
## 二、安装步骤

### 1、查看系统版本

>  
 bdsc@s225:~$ cat /etc/os-release <img src="https://img-blog.csdnimg.cn/direct/b9319287adaa4b33905e0faad63bd74e.png" alt="在这里插入图片描述"> 


### 2、检查gcc和make

>  
 root@kylin:~# gcc --version gcc (Ubuntu 9.3.0-10kylin2) 9.3.0 Copyright © 2019 Free Software Foundation, Inc. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. root@kylin:~# make --version GNU Make 4.2.1 … 


### 3、安装wget

>  
 root@kylin:~# apt-get install -y wget 


### 4、下载显卡驱动

  访问NVIDIA官网，根据型号搜索驱动程序，复制链接后使用wget命令下载。博主习惯下载较新，但是不是最新的版本。下载什么样的版本大家可以根据自己的喜欢选择，不建议下载太老旧的版本。如果以前安装了旧版本，我们安装新版本会提示并覆盖旧版本，当前最新版本是550.54.14。 <img src="https://img-blog.csdnimg.cn/direct/595765cf9c8e4da3884aeef3f158a753.png" alt="在这里插入图片描述">

>  
 root@kylin:/opt# wget https://download.nvidia.com/XFree86/Linux-x86_64/545.23.06/NVIDIA-Linux-x86_64-545.23.06.run 


### 5、给驱动程序添加执行权限

>  
 root@kylin:/opt# chmod u+x NVIDIA-Linux-x86_64-545.23.06.run 


### 6、设置系统为多用户模式启动

  修改完模式后重启机器，如果是图形化界面启动，安装驱动的时候会提示需要关闭x-server。

>  
 root@kylin:/opt# systemctl set-default multi-user.target Created symlink /etc/systemd/system/default.target → /lib/systemd/system/multi-user.target 


### 7、提示未检测到NVIDIA显卡

  博主在实验的时候发现bios优先使用独显的信号输出，如果显卡驱动未安装会出现无信号输出的问题，所以博主在进行U盘装机的时候先把独显拔除，装机完成后安装驱动然后再关机安装显卡。安装驱动的时候如果提示未检测到显卡，我们这里回车继续即可，这只是一个warning，不影响安装。 <img src="https://img-blog.csdnimg.cn/direct/69d8c7d6b83949c4bfe417956397686e.png" alt="在这里插入图片描述">

### 8、提示检测到旧显卡驱动

  博士实验的主机原来有一块2G独显，所以提示存在旧的显卡驱动，新版显卡为GTX 1060，这里选择继续安装。 <img src="https://img-blog.csdnimg.cn/direct/8126d8efb4954fa4884df1be88a8d2b9.png" alt="在这里插入图片描述">

### 9、安装32位lib包

  虽然现在基本上都是64位系统，为了更好的兼容，我们选择yes。 <img src="https://img-blog.csdnimg.cn/direct/f059eddbfdfa4a3cb8d12e34d3532011.png" alt="在这里插入图片描述">

### 10、是否安装DKMS

  这里我们选择no，不自动更新。 <img src="https://img-blog.csdnimg.cn/direct/e52a99aedf5f4adabbe1b66bd085e7d3.png" alt="在这里插入图片描述">

### 11、提示libglvnd未找到

  提示libglvnd未找到只是一个warning，不影响使用，我们回车继续。 <img src="https://img-blog.csdnimg.cn/direct/014a17dd4e6f47578b1442b4ed28a665.png" alt="在这里插入图片描述">

### 12、完成安装

<img src="https://img-blog.csdnimg.cn/direct/f72338f1ed5440d2ba8811a069052cc7.png" alt="在这里插入图片描述">

### 13、重启系统

  关机后插上NVIDIA显卡，然后重新启动系统。

>  
 root@kylin:/opt# reboot 


### 14、验证驱动程序

  使用命令nvidia-smi验证驱动是否安装成功，如果可以看到驱动程序版本、显卡型号、显存容量等信息说明安装成功。博主首先安装的545.23.06，后面测试过程中又升级到了550.54.14。

>  
 root@kylin:/opt# nvidia-smi <img src="https://img-blog.csdnimg.cn/direct/b9de053f8f724f60a550f8db65bf16e2.png" alt="在这里插入图片描述"> 


## 三、经验总结

  博主这次在银河麒麟系统下安装NVIDIA显卡驱动还是遇到了不少问题，经验总结如下：
- bios环境下主板优先输出独显信号，除非无独立显卡，信号输出到主板集成显卡；在系统启动完成后才会两个信号通道都显示。所以如果需要U盘装机，需要主板已经安装合适驱动或者去除独显先安装系统和驱动。- 银河麒麟安装的时候建议选择英文。博主在选择中文语言安装的时候，插上独显启动界面有看到银河麒麟图标后下方有一行字乱码，这一个页面快速闪过后屏幕就没有任何输出了，拔除显卡系统可以正常启动。博主重新安装为英文的时候启动正常。