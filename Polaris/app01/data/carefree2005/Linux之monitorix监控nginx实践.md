
--- 
title:  Linux之monitorix监控nginx实践 
tags: []
categories: [] 

---
## 一、monitorix简介

  Monitorix是一个免费、开源、轻量级的系统监控工具，旨在监控尽可能多的服务和系统资源。它是为在生产Linux/UNIX服务器下使用而创建的，但由于它的简单性和小尺寸，也可以在嵌入式设备上使用。关于monitorix的安装见博文：。除了监控linux服务器基础指标，我们还可以与其他软件结合使用，用于监控软件相关数据指标。此博文将介绍如何使用monitorix监控nginx服务。博文实验环境：
- linux版本：centos7.6- monitorix版本：3.14.0- nginx版本：1.22.0
## 二、编译安装nginx

  为了使用monitorix监控nginx，我们需要编译的时候加上with-http_stub_status_module模块，nginx源码编译安装可以参考博文。

### 1、安装gcc

>  
 [root@s142 src]# yum install -y gcc* 


### 2、安装依赖包

>  
 [root@s142 src]# yum -y install pcre-devel openssl openssl-devel 


### 3、下载nginx

>  
 [root@s142 src]# wget http://nginx.org/download/nginx-1.22.0.tar.gz [root@s142 src]# tar -zxvf nginx-1.22.0.tar.gz 


### 4、编译

>  
 [root@s142 src]# cd nginx-1.22.0 [root@s142 nginx-1.22.0]# ./configure --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --with-http_stub_status_module 


### 5、安装

>  
 [root@s142 nginx-1.22.0]# make … make[1]: Leaving directory `/usr/local/src/nginx-1.22.0’ [root@s142 nginx-1.22.0]# make install … <img src="https://img-blog.csdnimg.cn/1e8a53dccafb4bff9d07fcbc641e3e8c.png" alt="在这里插入图片描述"> 


  经测试验证使用yum安装nginx的方式也已经安装了with-http_stub_status_module模块，所以我们也可以使用yum方式方案nginx。或者说我们一般的nginx安装都包含了此模块，我们只需要修改nginx和monitorix配置文件即可。

## 三、配置monitorix监控nginx

### 1、修改monitorix配置

>  
 [root@s142 nginx]# vim /etc/monitorix/monitorix.conf <img src="https://img-blog.csdnimg.cn/37275d36fb6d4977afb66cc2a879ae0d.png" alt="在这里插入图片描述"> 


### 2、修改nginx配置

>  
 [root@s142 nginx]# vim /etc/nginx/nginx.conf #在配置文件中加入如下内容，其中allow是我们允许访问的IP地址白名单。 location /nginx_status {<!-- --> stub_status on; access_log off; allow 192.168.0.32; deny all; } 


### 3、重启服务

>  
 [root@s142 nginx]# systemctl restart monitorix [root@s142 nginx]# nginx -t … [root@s142 nginx]# nginx -s reload 


### 4、访问监控页

  monitorix监控nginx实际上就是利用with-http_stub_status_module插件模块功能，将数据进行图形化展示。 <img src="https://img-blog.csdnimg.cn/2d7503bfa62d4a9ab35dc735feef52b3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/30080ffe595f49518a0331aa0ba56e98.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/a717fd0ae87c4ae0944291b60220dfcc.png" alt="在这里插入图片描述">

## 四、QA

### 1、检查nginx配置的时候报错nginx: [emerg] getpwnam(“nginx”) failed
- 报错原因：未创建nginx账户- 解决方案：创建nginx账户
>  
 [root@s142 nginx]# useradd nginx -s /sbin/nologin -M 

