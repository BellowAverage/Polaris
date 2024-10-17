
--- 
title:  Linux之milvus向量数据库安装 
tags: []
categories: [] 

---
## 一、milvus简介

  Milvus是一个开源的向量相似度搜索引擎，主要用于大规模向量数据的存储和查询。它支持多种向量类型，包括稠密向量、稀疏向量、二进制向量等，并提供了多种相似度度量方法，如欧氏距离、余弦相似度、Jaccard相似度等。Milvus支持分布式部署，可以在多台服务器上搭建分布式搜索集群，支持高并发查询和批量查询。Milvus通过提供简单易用的API，可以轻松地与各种应用程序集成，如图像搜索、推荐系统、自然语言处理等领域。此博文以centos环境下安装milvus为例进行介绍，博文实验环境如下：
- 操作系统：centos7.9- docker版本：23.0.1- milvus版本：2.2.9
## 二、安装环境要求

  如下是以单机节点部署方式的软硬件安装要求。

### 1、硬件要求

<th align="left">序号</th><th align="left">硬件类型</th><th align="left">最低配置要求</th><th align="left">推荐配置</th><th align="left">备注</th>
|------
<td align="left">1</td><td align="left">CPU</td><td align="left">intel二代以上CPU</td><td align="left">4核以上CPU</td><td align="left">目前不支持AMD CPU类型</td>
<td align="left">2</td><td align="left">CPU指令集</td><td align="left">SSE4.2、AVX、AVX2、AVX-512</td><td align="left">SSE4.2、AVX、AVX2、AVX-512</td><td align="left">确保CPU至少支持一个列出的SIMD扩展</td>
<td align="left">3</td><td align="left">内存</td><td align="left">8G</td><td align="left">16G</td><td align="left"></td>
<td align="left">4</td><td align="left">硬盘驱动</td><td align="left">SATA 3.0 SSD或者更高</td><td align="left">NVMe SSD或者更高</td><td align="left"></td>

### 2、软件要求

  对于单机部署来说主要满足满足docker和docker compose组件版本要求就可以，另外几个相关软件是在通过docker compose安装milvus时自动安装的。

<th align="left">序号</th><th align="left">软件</th><th align="left">要求</th><th align="left">备注</th>
|------
<td align="left">1</td><td align="left">Linux系统</td><td align="left">Docker 19.03以上版本，Docker Compose 1.25.1以上版本</td><td align="left"></td>
<td align="left">2</td><td align="left">etcd</td><td align="left">3.5.0</td><td align="left">对集群性能至关重要，与磁盘性能相关</td>
<td align="left">3</td><td align="left">MinIO</td><td align="left">RELEASE.2023-03-20T20-16-18Z</td><td align="left"></td>
<td align="left">4</td><td align="left">Pulsar</td><td align="left">2.8.2</td><td align="left"></td>

## 三、安装步骤

### 1、安装docker

  docker的安装见博文，这里不再赘述。

### 2、安装fio命令

>  
 [root@yws55 home]# yum install -y fio 


### 3、磁盘性能测试

  理想情况下，磁盘的IOPS应超过500，而fsync延迟的99%以上应低于10ms。

<img src="https://img-blog.csdnimg.cn/1c7ff7d4af184c6fa28cc2350c78e5ef.png" alt="在这里插入图片描述">

### 4、检查CPU支持的指令集

  我们使用lscpu命令可以查看CPU支持的指令集，Flags的参数值就是该服务器支持的CPU指令集。 <img src="https://img-blog.csdnimg.cn/17150b89a65443c59703ea3000de4c01.png" alt="在这里插入图片描述">

### 5、检查docker版本

  根据milvus安装要求，docker版本要求是19.03以上版本，我们这里安装的docker版本为23.0.1，满足要求。

>  
 [root@yws55 test-data]# docker -v Docker version 23.0.1, build a5ee5b1 


### 6、安装docker compose组件

  根据milvus安装要求，docker compose版本要求是1.25.1以上，我们这里安装的版本是1.29.2，满足要求。

>  
 [root@yws55 home]# yum -y install python3-pip [root@yws55 home]# pip3 install --upgrade pip [root@yws55 home]# pip install docker-compose [root@yws55 home]# docker-compose version … docker-compose version 1.29.2, build unknown … 


### 7、下载YAML文件

  在/home目录下创建一个docker目录，当然这个可以自定义，这个目录将用于存储我们的milvus容器的volumes数据。

>  
 [root@yws55 home]# mkdir docker [root@yws55 home]# cd docker/ [root@yws55 docker]# wget https://github.com/milvus-io/milvus/releases/download/v2.2.9/milvus-standalone-docker-compose.yml -O docker-compose.yml 


### 8、安装milvus容器

  在下载存储docker-compose.yml文件的目录下执行docker-compose up -d 命令开始安装milvus容器。

>  
 [root@yws55 docker]# docker-compose up -d … Creating milvus-minio … done Creating milvus-etcd … done Creating milvus-standalone … done [root@yws55 docker]# ll total 4 -rw-r–r-- 1 root root 1356 Jun 5 10:35 docker-compose.yml drwxr-xr-x 5 root root 45 Jun 13 14:52 volumes 


### 9、查看milvus容器运行状态

  使用docker-compose安装完成milvus后自动启动了，可以使用命令docker ps或者docker-compose ps命令查看容器运行状态。看到milvus-etcd 、milvus-minio 、milvus-standalone三个容器说明安装成功。 <img src="https://img-blog.csdnimg.cn/fd2f7289c76248e293cf4137fec0dee1.png" alt="在这里插入图片描述">

### 10、milvus数据库连接测试

  使用浏览器访问连接地址http://ip:9091/api/v1/health，返回{“status”:“ok”}说明milvus数据库服务器运行正常。 <img src="https://img-blog.csdnimg.cn/aec40d0b8fc341d38c683ff38622e3e6.png" alt="在这里插入图片描述">

### 11、milvus数据库服务管理
- 停止milvus容器
>  
 [root@yws55 docker]# docker-compose stop 

- 启动milvus容器
>  
 [root@yws55 docker]# docker-compose start 

- 删除milvus容器 使用docker-compose down命令会停止milvus容器并删除，然后我们可以rm -rf volumes删除milvus数据。
>  
 [root@yws55 docker]# docker-compose down 

- 重启milvus容器
>  
 [root@yws55 docker]# docker-compose restart 

- 查看milvus容器日志
>  
 [root@yws55 docker]# docker-compose logs 


### 12、更多milvus知识

  更多milvus知识见。
