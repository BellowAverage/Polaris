
--- 
title:  centos8与centos7对比 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong>**</strong> 
 ♥️**每天分享云计算网络运维课堂笔记，努力不一定有收获，但一定会有收获加油！一起努力，共赴美好人生！** 
 ♥️**夕阳下，是最美的绽放，树高千尺，落叶归根人生不易，人间真情** 


**前言**

所有的努力和收获是成正比的，好好看好好学，干货满满！

<img alt="" src="https://img-blog.csdnimg.cn/9bc525928ce54ea0ae7903f56e4bbe74.png">



**目录**

















































### 镜像下载地址

>  
 CentOS 8 下载：https://centos.org/download/ 
 国内镜像下载：https://mirrors.tuna.tsinghua.edu.cn/centos/ 
 国内yum源：http://mirrors.aliyun.com/repo/Centos-8.repo 


### 1.1 默认的文件系统

RHEL8与RHEL7都是采用XFS

### 1.2 RHEL8与RHEL7的内核版本分别是多少

关于内核版本，RHEL8和7的区别如下：

RHEL8采用4.18.0-x

RHEL7采用3.10-0-x

### 1.3 内核代码名字

>  
 关于内核代码，RHEL8和7的区别如下： 
 RHEL8采用2019-05-07 (Kernel Version 4.18.0-80) 
 RHE7采用2014-06-09 (Kernel Version 3.10.0-123) 


### 1.4 标准/默认的仓库频道

关于仓库频道，RHEL8和7的区别如下：

RHEL8

Repo ID: rhel-8-for-x86_64-appstream-rpms

Repo Name: Red Hat Enterprise Linux 8 for x86_64 - AppStream (RPMs)

Repo ID: rhel-8-for-x86_64-baseos-rpms

Repo Name: Red Hat Enterprise Linux 8 for x86_64 - BaseOS (RPMs)

RHEL7

Repo ID: rhel-7-server-rpms

Repo Name: Red Hat Enterprise Linux 7 Server (RPMs)

### 1.5 网络时间同步

关于网络时间同步，RHEL8和7的区别如下：

RHEL8

只使用Chronyd，不支持NTP部署。

RHEL7

Chronyd与NTP两者都支持

### 1.6 支持最大的文件

关于支持最大的文件，RHEL8和7的区别如下：

RHEL8

XFS文件系统支持的最大文件大小已从500 TiB增加到1024 TiB。

(此最大文件大小仅适用于64位机器。Red Hat Enterprise Linux不支持32位机器上的XFS.)

RHEL7

最大. (单独) 文件大小= 500TiB

最大. 文件系统大小 = 500TiB

### 1.7 软件包管理

关于软件包管理，RHEL8和7的区别如下：

红帽8

包管理由DNF (YUMv4)完成。

yum4基于DNF技术，yum4命令提供了与早期版本中使用的Yum v3的向后兼容性。yum命令只是到dnf的一个符号链接。

红帽7

yum基于3.0.x版本

### 1.8 最大支持的内存

关于最大支持的内存，RHEL8和7的区别如下：

红帽8

24TB，64位架构

红帽7:

只支持12TB

### 1.9 默认的网络数据包过滤

关于默认的网络数据包过滤，RHEL8和7的区别如下：

RHEL8使用nftables取代了iptables框架

nftables是默认的网络包过滤，它取代了以前的iptables框架。firewalld守护进程现在使用nftables作为默认后端。

这将取代以前使用的“iptables”、“ip6tables”、“arptables”和“ebtables”工具。“nftables”确实为IPv4和IPv6协议提供了一个单一的框架。

而RHEL7 firewalld守护进程使用iptables作为其默认后端。

### 1.10 默认的数据库

关于默认的数据库，RHEL8和7的区别如下：

RHEL8默认支持的数据库：

MySQL 8.0

MariaDB 10.3

PostgreSQL 10 and PostgreSQL 9.6

Redis 5.0

MariaDB是Red Hat Enterprise Linux 7中MySQL的默认实现

### 1.11 支持的硬件架构

关于支持的硬件架构，RHEL8和7的区别如下：

RHEL8支持以下硬件架构

AMD and Intel 64-bit architectures

The 64-bit ARM architecture

IBM Power Systems, Little Endian

IBM Z

RHEL7支持以下硬件架构：

64-bit AMD

64-bit Intel

IBM POWER7

IBM System z

### 1.12 可供安装的ISO镜像类型

关于可供安装的ISO镜像类型，RHEL8和7的区别如下：

RHEL 8可以使用以下类型的ISO镜像安装:

Binary(二进制) DVD ISO

Boot ISO

在RHEL7中，可以使用以下可用的ISO镜像进行安装:

Boot ISO

Binary(二进制) DVD ISO

Supplementary(追加的) Binary DVD

### 1.13 默认情况下的Cockpit web控制台的安装状态*****

关于默认情况下的Cockpit web控制台的安装状态，RHEL8和7的区别如下：

在RHEL8中，Cockpit是默认安装和可用的。这将在非最小模式下自动安装，并在防火墙中启用所需端口。

Cockpit提供了一个增强的框架，可以用来访问/编辑/更改许多系统设置。这提供了通过web接口的访问，可以使用浏览器访问url地址http://:9090进行管理。

在RHEL7系统中，Cockpit默认情况下没有安装，需要通过启用extra和optional存储库通道来安装。

### 1.14 默认虚拟机管理

关于默认虚拟机管理，RHEL8和7的区别如下：

在RHEL8系统中，默认情况下，它由Cockpit管理。如果需要，还可以安装virt-manager。

而在RHEL7系统中virt-manager将用于基于KVM的虚拟系统管理。

### 1.15 RPM 版本的改进

关于RMP版本的改进，RHEL8和7的区别如下：

Red Hat Enterprise Linux 8是用RPM 4.14发布的。现在，RPM在开始安装之前验证整个包的内容。

这有很多改进，其中一些值得注意的功能是:

debuginfo包可以并行安装

支持弱依赖关系

支持丰富的或布尔依赖

支持封装文件超过4 GB的大小

支持文件触发器

构建在RHEL8上的包在压缩负载上使用一个新的SHA-256散列。

而Red Hat Enterprise Linux 7是用RPM 4.11发布的。在RHEL7上，RPM实用程序在解压时验证单个文件的有效负载内容。

### 1.16 CUPS日志

关于CUPS日志，RHEL8和7的区别如下：

RHEL8所有类型的CUPS日志都与来自其他程序的日志一起集中记录在systemd journald守护进程中。要访问CUPS日志，请使用“journalctl -u CUPS”命令。

而RHEL7系统上，CUPS日志被存储中 /var/log/cups directory.

nobody用户替换nfsnobody

rhel8系统上，nobody和nfsnobody用户和组合并到nobodyID(65534)中。

在Red Hat Enterprise Linux 7中，有:

ID为99的nobody用户和组

nfsnobody用户和组对的ID为65534，这也是默认的内核溢出ID。

### 1.17 默认版本的控制系统

关于默认版本的控制系统，RHEL8和7的区别如下：

RHEL 8提供以下版本控制系统:

Git 2.18

Mercurial 4.8

Subversion 1.10

并发版本系统(CVS)和版本控制系统(RCS)在RHEL8中都不可用。

而Red Hat Enterprise Linux 7与三个最流行的开源修订控制系统一起发布:Git、SVN和CVS。

### 1.18 编程语言版本

>  
 关于编程语言版本，RHEL8和7的区别如下： 
 RHEL8新版本编程语言 
 Python 3 
 PHP 7.2 
 Ruby 2.5 
 Node.js 10 
 而RHEL7支持以下编辑语言 
 Python 2 ( 2.7.X) 
 PHP 5.4 
 Ruby 2.0.0 


### 1.19 关于容器技术的支持*****

关于容器技术的支持，RHEL8和7的区别如下：

Docker不包括在RHEL 8.0中。使用容器时，需要使用podman、buildah、skopeo和runc工具。

podman工具已经作为一个完全支持的特性发布了。

Docker和Docker Registry是Red Hat Enterprise Linux 7中的Extras订阅频道的一部分。

### 1.20 开发工具支持

关于开发工具支持，RHEL8和7的区别如下：

RHEL 8提供OpenJDK 11、OpenJDK 8、IcedTea-Web和各种Java工具，如Ant、Maven或Scala。

在RHEL7中，OpenJDK8用作默认的Java开发工具包(JDK)，而Java 8用作默认的Java版本。

### 1.21 NFS配置对比

关于NFS配置对比，RHEL8和7的区别如下：

RHEL8的NFS配置文件是/etc/NFS.conf。

当从RHEL7升级时，Red Hat Enterprise Linux 8尝试自动将所有选项从/etc/sysconfig/nfs转换为/etc/nfs。并不再支持NFS/UDP。

而RHEL7中，默认的NFS配置文件是/etc/sysconfig/NFS

### 1.22 默认的显示服务器

关于默认的显示服务器，RHEL8和7的区别如下：

在RHEL 8中，Gnome display Manager使用的默认显示服务器是Wayland。

X.org服务器是RHEL 7中的默认显示服务器

>  
 <blockquote> 
  ♥️关注，就是我创作的动力 
  ♥️点赞，就是对我最大的认可 
  ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 
 




