
--- 
title:  银河麒麟之命令行下配置网卡及DNS 
tags: []
categories: [] 

---
## 一、环境说明

  银河麒麟操作系统版本为桌面版V10.1。

>  
 root@kylinvm:~# lsb_release -a No LSB modules are available. Distributor ID: Kylin Description: Kylin V10.1 Release: v10.1 Codename: juniper 


>  
 root@kylinvm:~# cat /etc/.kyinfo [dist] name=Kylin milestone=Desktop-V10.1-Release-Build1-20201128 arch=x86_64 beta=False time=2020-11-28 18:45:04 dist_id=Kylin-Desktop-V10.1-Release-Build1-20201128-x86_64-2020-11-28 18:45:04  [servicekey] key=0050026  [os] to= term=2022-03-01 


## 二、配置步骤

  桌面版可以通过编辑网卡配置进行设置，配置方式可以参考我的另外一篇博文《银河麒麟之esxi6.5环境下安装桌面版V10.1》，本文主要介绍命令行下如何配置网卡及DNS。如下命令如果使用普通用户执行，命令前请加sudo。

### 1、通过ip add命令确认网卡名称

  本示例环境网卡名称为ens160。

>  
 root@kylinvm:~# ip addr 1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00 inet 127.0.0.1/8 scope host lo valid_lft forever preferred_lft forever inet6 ::1/128 scope host valid_lft forever preferred_lft forever 2: ens160: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc mq state UP group default qlen 1000 link/ether 00:0c:29:9e:35:34 brd ff:ff:ff:ff:ff:ff inet 192.168.0.138/24 brd 192.168.0.255 scope global ens160 valid_lft forever preferred_lft forever inet6 fe80::20c:29ff:fe9e:3534/64 scope link valid_lft forever preferred_lft forever 


### 2、配置网卡

  使用如下命令编辑网卡配置，然后保存。

>  
 #vim /etc/network/interfaces <img src="https://img-blog.csdnimg.cn/20210123205632202.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NhcmVmcmVlMjAwNQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 


### 3、配置DNS

  使用如下命令配置DNS，然后保存。

>  
 #vim /etc/systemd/resolved.conf <img src="https://img-blog.csdnimg.cn/20210123205951386.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NhcmVmcmVlMjAwNQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 


### 4、重启网络服务

  使用如下命令重启网络服务。

>  
 root@kylinvm:~# /etc/init.d/networking force-reload Reloading networking configuration (via systemctl): networking.service. root@kylinvm:~# /etc/init.d/networking restart Restarting networking (via systemctl): networking.service. root@kylinvm:~# 


### 5、访问网络验证

<img src="https://img-blog.csdnimg.cn/2021012321051920.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NhcmVmcmVlMjAwNQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
