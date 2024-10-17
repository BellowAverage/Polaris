
--- 
title:  Linux之网络流量监控工具ntopng源码编译安装 
tags: []
categories: [] 

---
## 一、ntopng简介

  Ntop是一种监控网络流量工具，用ntop显示网络的使用情况比其他一些网络管理软件更加直观、详细。Ntop甚至可以列出每个节点计算机的网络带宽利用率。他是一个灵活的、功能齐全的，用来监控和解决局域网问题的工具；尤其当ntop与nprobe配合使用，其功能更加显著。它同时提供命令行输入和web页面，可应用于嵌入式web服务。NTOP于2011年已经停止更新，NTOPNG是NTOP的新一代版本，ntopng最新稳定版本是5.4。安装环境说明：
- 操作系统：centos7.6- ntopng版本：5.4- nDPI版本：4.5
## 二、安装步骤

### 1、下载最新稳定版

>  
 [root@s142 opt]# wget https://github.com/ntop/ntopng/archive/refs/heads/5.4-stable.zip 


### 2、安装unzip命令

>  
 [root@s142 opt]# yum install -y zip unzip 


### 3、解压软件包

>  
 [root@s142 opt]# unzip 5.4-stable.zip [root@s142 opt]# ln -s ntopng-5.4-stable ntopng [root@s142 opt]# cd ntopng 


### 4、查看ntopng安装前的依赖

  安装前我们需要仔细阅读此文件，查看编译要求以及不同系统环境下的安装步骤和命令。

>  
 [root@s142 ntopng]# cat doc/README.compilation |more <img src="https://img-blog.csdnimg.cn/db6315da4cbc40afa55aa135506734f2.png" alt="在这里插入图片描述"> 


### 5、安装依赖包

  安装依赖包之间确认是否安装yum扩展源，如果未安装请先安装，因为部分软件包（如zerozmq-devel）需要扩展源中才有。

>  
 #扩展源安装命令 #yum -y install epel-release [root@s142 ntopng]# yum groupinstall “Development tools” -y … [root@s142 ntopng]# yum install -y git autoconf automake autogen bison flex libpcap-devel libmaxminddb-devel hiredis-devel redis glib2-devel libxml2-devel sqlite-devel gcc-c++ libtool wget libcurl-devel pango-devel cairo-devel libpng-devel mysql-devel libnetfilter_queue-devel zlib-devel which libcap-devel readline-devel zeromq-devel json-c-devel 


### 6、执行autogen.sh脚本

  autogen.sh脚本是用于检查依赖包是否安装并生成configure文件，检查不通过会根据检查情况报告错误信息，检查通过后提示我们可以运行./configure命令。

>  
 [root@s142 ntopng]# sh autogen.sh 


### 7、安装nDPI

>  
 [root@s142 opt]# git clone https://github.com/ntop/nDPI.git [root@s142 opt]# cd nDPI [root@s142 nDPI]# ./autogen.sh [root@s142 nDPI]# ./configure [root@s142 nDPI]# make 


### 8、执行configure配置

  配置过程中如果遇到报错记得先处理相关报错，否则编译会出问题，也有可能到最后web访问出现问题。

>  
 [root@s142 ntopng-2.0-stable]# ./configure <img src="https://img-blog.csdnimg.cn/9569492ebac248a5bb784a733b668ccb.png" alt="在这里插入图片描述"> 


### 9、编译

>  
 [root@s142 ntopng]# make 


### 10、安装

>  
 [root@s142 ntopng]# make install … [root@s142 ntopng]# which ntopng /usr/local/bin/ntopng 


### 三、ntopng启动

### 1、查看ntopng版本

>  
 [root@s142 ntopng]# ntopng -V Version: 5.4.230119 [Community build] GIT rev: :5.4.230119 


### 2、启动redis

>  
 [root@s142 ntopng]# systemctl start redis <img src="https://img-blog.csdnimg.cn/e3602b7fb3ce4a3db45e6396fb304dcb.png" alt="在这里插入图片描述"> 


### 3、创建配置文件

>  
 [root@s142 ntopng]# mkdir -p /etc/ntopng [root@s142 ntopng]# cp ./packages/etc/ntopng/ntopng.conf /etc/ntopng/ntopng.conf 


### 4、启动ntopng

>  
 [root@s142 ntopng]# ntopng /etc/ntopng/ntopng.conf 


### 5、访问web管理页

<img src="https://img-blog.csdnimg.cn/b4ebabfc95964a1c9ca85c30eb8d2372.png" alt="在这里插入图片描述">

### 6、修改admin密码

  初次登陆使用默认账号密码admin/admin，登陆之后要求修改初始密码。 <img src="https://img-blog.csdnimg.cn/bcda0f5744df4caba69696420898e385.png" alt="在这里插入图片描述">

### 7、界面展示

  下面就是登陆之后的主界面了，具体的使用我们另外出博文介绍。 <img src="https://img-blog.csdnimg.cn/5f79f1554d6c4aee808114df998e435c.png" alt="在这里插入图片描述">

## 四、QA

### 1、configure报错zmq未安装
- 报错信息：ZMQ not present or too old (&lt; v. 3.x)- 报错原因：因为没有安装yum扩展源，安装依赖时未成功安装zmq- 解决方案：安装yum扩展源，然后重新安装依赖软件包，见步骤5。