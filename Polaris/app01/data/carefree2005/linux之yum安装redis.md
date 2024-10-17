
--- 
title:  linux之yum安装redis 
tags: []
categories: [] 

---
## 一、redis简介

  Redis（Remote Dictionary Server )，即远程字典服务。Redis是一个开源（BSD许可）的内存数据结构存储，用作数据库、缓存、消息代理和流引擎。Redis提供了字符串、哈希、列表、集合、带范围查询的排序集合、位图、超日志、地理空间索引和流等数据结构。Redis具有内置复制、Lua脚本、LRU逐出、事务和不同级别的磁盘持久性，并通过Redis Sentinel和Redis Cluster自动分区提供高可用性。您可以对这些类型运行原子操作，如附加到字符串；增加哈希中的值；将元素推送到列表；计算集合交集、并集和差集；或者获得排序集合中排名最高的成员。为了获得最佳性能，Redis使用内存数据集。根据您的使用情况，Redis可以通过定期将数据集转储到磁盘或将每个命令附加到基于磁盘的日志中来持久化数据。如果您只需要功能丰富的网络内存缓存，也可以禁用持久性。Redis支持异步复制，具有快速的非阻塞同步和自动重新连接，并在网络拆分时进行部分重新同步。博文发布时最新的官方文档版本是7.0.9版本，一般使用源码安装的方式，可以参照博文：。源码安装最新版步骤也很简单：

>  
 #wget https://download.redis.io/redis-stable.tar.gz #tar -zxvf redis-stable.tar.gz #cd redis-stable #源码安装需要安装gcc #yum install -y gcc #需要指定参数，否则会报错fatal error: jemalloc/jemalloc.h: No such file or directory #make MALLOC=libc #/src/redis-cli --version redis-cli 7.0.9 #./src/redis-server --version Redis server v=7.0.9 sha=00000000:0 malloc=libc bits=64 build=2c5fd1d5dfcd6b69 


  博文是在centos7.6环境完成的安装测试及验证。

## 二、yum安装redis3

  如果不是必须安装最新版，还有更简单的安装方式，可以使用yum方式安装redis，通过epel扩展源安装redis，但是此方式只可以安装redis3的版本，直接yum安装当前安装的是3.2.12版本。

### 1、安装epel扩展源

>  
 [root@s142 yum.repos.d]# yum install -y epel-release 


### 2、yum安装redis3

>  
 [root@s142 yum.repos.d]# yum install -y redis … Installed: redis.x86_64 0:3.2.12-2.el7  Dependency Installed: jemalloc.x86_64 0:3.6.0-1.el7  Complete! 


### 3、查看redis版本

>  
 [root@s142 yum.repos.d]# redis-server --version Redis server v=3.2.12 sha=00000000:0 malloc=jemalloc-3.6.0 bits=64 build=7897e7d0e13773f 


## 三、yum安装redis7

### 1、下载第三方扩展源rpm

>  
 [root@s142 yum.repos.d]# wget http://rpms.famillecollet.com/enterprise/remi-release-7.rpm 


### 2、安装remi.repo

>  
 [root@s142 yum.repos.d]# rpm -ivh remi-release-7.rpm 


### 3、更新yum缓存

>  
 [root@s142 yum.repos.d]# yum clean all [root@s142 yum.repos.d]# yum makecache 


### 4、安装redis7

  因为多个扩展源包含了redis源，默认epel源优先，我们可以使用–enablerepo参数指定安装源。

>  
 [root@s142 yum.repos.d]# yum --enablerepo=remi install -y redis … 已安装: redis.x86_64 0:7.0.8-1.el7.remi  完毕！ 


### 5、版本查看

>  
 [root@s152 yum.repos.d]# redis-server --version Redis server v=7.0.8 sha=00000000:0 malloc=jemalloc-5.2.1 bits=64 build=2e3cf6f897ee69aa 


### 6、指定版本安装

  如果不想安装最新版，我们也可以指定近期的版本安装。yum安装可以完成次新版7.0.8版本的安装，也可以安装其他临近的版本，只要安装源维持了该版本。

>  
 [root@s142 yum.repos.d]# yum --enablerepo=remi install -y redis-6.2.9 <img src="https://img-blog.csdnimg.cn/b94a8ec371334aeba21b5757c31c5568.png" alt="在这里插入图片描述"> 

