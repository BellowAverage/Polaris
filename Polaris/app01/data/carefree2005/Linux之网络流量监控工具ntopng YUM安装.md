
--- 
title:  Linux之网络流量监控工具ntopng YUM安装 
tags: []
categories: [] 

---
## 一、ntopng简介

  Ntop是一种监控网络流量工具，用ntop显示网络的使用情况比其他一些网络管理软件更加直观、详细。Ntop甚至可以列出每个节点计算机的网络带宽利用率。他是一个灵活的、功能齐全的，用来监控和解决局域网问题的工具；尤其当ntop与nprobe配合使用，其功能更加显著。它同时提供命令行输入和web页面，可应用于嵌入式web服务。NTOP于2011年已经停止更新，NTOPNG是NTOP的新一代版本，ntopng最新稳定版本是5.4。

## 二、YUM安装ntopng

  使用源码编译安装方式安装很容易报错，因为版本兼容性问题各种报错，我们需要根据报错进行一个个处理，yum安装可以帮助我们简化这个过程。

### 1、下载yum扩展源ntop.repo

>  
 [root@s142 ~]# cd /etc/yum.repos.d/ [root@s142 yum.repos.d]# wget --no-check-certificate https://packages.ntop.org/centos-stable/ntop.repo -O ntop.repo 


### 2、清理YUM缓存并更新

>  
 [root@s142 yum.repos.d]# yum clean all [root@s142 yum.repos.d]# yum --exclude=kernel* update 


### 3、添加epel yum扩展源

  安装ntopng的时候有些依赖源需要通过epel扩展源才可以安装成功，所以我们添加epel yum扩展源。

>  
 [root@s142 ~]# yum install -y epel-release 


### 4、yum安装ntopng

  准备就绪后我们就可以安装ntopng了。

>  
 [root@s142 ~]# yum install -y pfring-dkms n2disk nprobe ntopng cento 


### 5、修改ntopng.conf配置

  我们编辑ntopng.conf配置文件，指定ntopng服务监听的网卡以及允许访问的本地地址段。

>  
 [root@s142 ~]# vim /etc/ntopng/ntopng.conf #增加如下两行 <img src="https://img-blog.csdnimg.cn/1b2cc6c947dc49babeb78693831d518d.png" alt="在这里插入图片描述"> 


### 6、启动redis

  yum安装ntopng的时候自动安装依赖就会安装redis等，我们可以通过systemctl命令启动redis。

>  
 [root@s142 ~]# systemctl start redis<img src="https://img-blog.csdnimg.cn/dfc6d73e080f4c589a8f73c8ad15c915.png" alt="在这里插入图片描述"> 


### 7、启动ntopng

  同理我们也可以使用systemctl命令启动、停止、查看ntopng状态。

>  
 [root@s142 ~]# systemctl start ntopng [root@s142 ~]# systemctl status ntopng <img src="https://img-blog.csdnimg.cn/5f89dc8063df43169787604db34b2c7e.png" alt="在这里插入图片描述"> 


### 8、查看服务端口

  检查监听端口我们可以看到服务端口3000已经监听，我们可以访问ntopng的管理页面了。当然如果操作系统启用了防火墙我们可以需要开放3000端口或者关闭防火墙。

>  
 [root@s142 ~]# netstat -tnpl <img src="https://img-blog.csdnimg.cn/c25485abe0434fccaaec9b769ff64786.png" alt="在这里插入图片描述"> 


### 9、访问管理页

  YUM安装方式可以极大的简化我们的安装步骤，自动处理安装所需依赖关系并安装。 <img src="https://img-blog.csdnimg.cn/1ac7bd1351b0418ab66382acf56e21d2.png" alt="在这里插入图片描述">
