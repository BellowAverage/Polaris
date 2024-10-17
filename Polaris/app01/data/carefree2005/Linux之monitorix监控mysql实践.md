
--- 
title:  Linux之monitorix监控mysql实践 
tags: []
categories: [] 

---
## 一、monitorix监控mysql环境说明

  Monitorix是一个免费、开源、轻量级的系统监控工具，旨在监控尽可能多的服务和系统资源。它是为在生产Linux/UNIX服务器下使用而创建的，但由于它的简单性和小尺寸，也可以在嵌入式设备上使用。关于monitorix的安装见博文：。除了监控linux服务器基础指标，我们还可以与其他软件结合使用，用于监控软件相关数据指标。此博文将介绍如何使用monitorix监控mysql服务。只需要在mysql数据库实例上创建一个普通账户，我们就可以通过monitorix监控mysql连接数、流量、打开表的数量、整体统计情况等。博文实验环境：
- linux版本：centos7.6- monitorix版本：3.14.0- mysql版本：5.7.26
## 二、配置步骤

### 1、mysql实例创建一个普通账户

>  
 mysql&gt; create user ‘test’@‘%’ identified by ‘Test123’; mysql&gt; flush privileges; 


### 2、配置monitorix.conf

  主要修改&lt;graph_enable&gt;属性中mysql的值，默认是禁用，将n改为y启用mysql监控图形。另外修改MYSQL graph配置中关于mysql实例的信息，list表示mysql实例列表的主机名，desc中是mysql实例远程连接的端口号、用户名、密码。

>  
 [root@s142 ~]# vim /etc/monitorix/monitorix.conf … mysql = y … list = s210 &lt;desc&gt; s210 = 3306, test, password &lt;/desc&gt; <img src="https://img-blog.csdnimg.cn/435bcf412c414b19985f4c1509dc7720.png" alt="在这里插入图片描述"> 


### 3、配置主机名

>  
 [root@s142 ~]# vim /etc/hosts … 192.168.0.210 s210 


### 4、重启monitorix服务

>  
 [root@s142 ~]# systemctl restart monitorix 


### 5、查看mysql监控页

<img src="https://img-blog.csdnimg.cn/2b98b253863941039fbe63f5fe692eca.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/925c4f6021ca496d984bb457e8c31cdb.png" alt="在这里插入图片描述">

### 6、配置多mysql主机监控

<img src="https://img-blog.csdnimg.cn/1bb0bf70395a48989501cd60a31d4b1e.png" alt="在这里插入图片描述">

### 7、重启monitorix服务

>  
 [root@s142 ~]# systemctl restart monitorix 


### 8、查看监控数据

  配置多个mysql实例会有多个mysql监控图形框。每个实例监控值为6个参数。 <img src="https://img-blog.csdnimg.cn/07feaf6ed4384e618414a706e302f492.png" alt="在这里插入图片描述">

## 三、mysql监控内容说明

### 1、监控图形介绍

<img src="https://img-blog.csdnimg.cn/99c4f5811f2148c48ce4493cc200e2a2.png" alt="在这里插入图片描述">

### 2、mysql overall stats指标介绍
- 线程缓存命中率 Thread Cache Hit Rate (1 - (Threads_created / Connections)) * 100- 查询缓存命中率 Query Cache Hit Rate Qcache_hits / (Qcache_hits + Com_select) * 100- 查询缓存使用情况 Query Cache Usage (1 - (Qcache_free_memory / query_cache_size)) * 100- 连接使用情况 Connections Usage (Max_used_connections / max_connections) * 100- 密钥缓冲区使用 Key Buffer Usage (Key_blocks_used / (Key_blocks_used + Key_blocks_unused)) * 100- InnoDB缓冲池使用情况 InnoDB Buffer Pool Usage (1 - (Innodb_buffer_pool_pages_free / Innodb_buffer_pool_pages_total)) * 100- 临时表使用情况 Temp. Tables To Disk (Created_temp_disk_tables / Created_temp_disk_tables + Created_temp_tables)) * 100