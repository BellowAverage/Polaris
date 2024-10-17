
--- 
title:  Centos8之系统升级 
tags: []
categories: [] 

---
## 一、centos8系统简介

  CentOS 8是一个基于Red Hat Enterprise Linux（RHEL）源代码构建的开源操作系统。它是一款稳定、可靠、安全的服务器操作系统，适合用于企业级应用和服务的部署。CentOS 8采用了最新的Linux内核和软件包管理系统，提供了更好的性能和安全性，同时还支持Docker和Kubernetes等容器化技术，方便用户进行应用程序的部署和管理。CentOS 8还提供了多种桌面环境，适合各种用户需求。Centos 8官方已于2021年12月31日以后停止Centos 8支持，转至Centos 8 Stream项目支持。

## 二、centos8.0升级到centos8.5

  centos8.3以上的版本无法直接升级到centos8 stream，所以我们先将centos8升级到最新的centos8.5。

### 1、查看系统版本

>  
 [root@sys41 ~]# cat /etc/centos-release CentOS Linux release 8.0.1905 (Core) 


### 2、注释mirrorlist

>  
 [root@sys41 ~]# sed -i ‘s/mirrorlist/#mirrorlist/g’ /etc/yum.repos.d/CentOS-*.repo 


### 3、指向baseurl至vault.epel.cloud存储库

>  
 [root@sys41 ~]# sed -i ‘s|#baseurl=http://mirror.centos.org|baseurl=http://vault.epel.cloud|g’ /etc/yum.repos.d/CentOS-*.repo 


### 4、升级系统至centos8.5

>  
 [root@sys41 ~]# yum update -y 


### 6、查看升级后的系统版本

>  
 [root@sys41 ~]# cat /etc/centos-release CentOS Linux release 8.5.2111 


## 三、centos8.5升级到centos8-stream

### 1、替换默认镜像仓库

  centos8升级为centos8-stream，我们需要替换镜像源。

>  
 [root@sys41 yum.repos.d]# dnf --disablerepo ‘*’ --enablerepo extras swap centos-linux-repos centos-stream-repos <img src="https://img-blog.csdnimg.cn/6c94e662e791441c87ecf610ce408e8a.png" alt="在这里插入图片描述"> 


### 2、更新至稳定发行版

>  
 [root@sys41 yum.repos.d]# dnf distro-sync 


### 3、重启系统

>  
 <blockquote> 
  [root@sys41 yum.repos.d]# reboot 
 

### 4、查看系统版本

>  
 [root@sys41 yum.repos.d]# cat /etc/centos-release CentOS Stream release 8 


## 四、centos8 stream升级到centos9 stream

  博主从centos8-stream升级到centos9-stream失败了，升级dnf -y --releasever=9 --allowerasing --setopt=deltarpm=false distro-sync执行到这一步报错Fatal glibc error: CPU does not support x86-64-v2，因为博主的测试环境是Intel i3的CPU，也就是说i3 cpu不支持centos9-stream系统版本。博主是参考了知乎https://zhuanlan.zhihu.com/p/571394959博主的升级操作，为了不迷路，留下此链接找环境再行尝试吧。

## 五、QA

### 1、升级为centos8-stream后系统使用reboot命令无法重启

解决方案：博主是在虚拟机环境下，控制台强制关机重启。
