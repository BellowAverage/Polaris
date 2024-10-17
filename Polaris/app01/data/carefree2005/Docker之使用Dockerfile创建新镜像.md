
--- 
title:  Docker之使用Dockerfile创建新镜像 
tags: []
categories: [] 

---
## 一、Docker镜像简介

  Docker镜像是Docker容器的基础，可以理解为是一个只读的模板，包含了运行Docker容器所需的所有文件、配置和依赖关系。镜像可以从一个或多个Dockerfile构建而来，也可以从其他镜像构建而来。Docker镜像可以被存储、分享和重复使用，可以在不同的环境中部署相同的应用程序，从而实现快速、可靠的部署。Docker Hub是一个公共的镜像仓库，包含了数以万计的Docker镜像，开发者可以在其中找到自己需要的镜像，并在自己的项目中使用它们。 创建docker镜像主要有如下四种方式：
- 从已有的镜像创建：可以使用docker pull命令从Docker Hub或其他镜像仓库中拉取镜像，然后使用docker run命令创建容器。- 使用Dockerfile创建：Dockerfile是一个文本文件，包含了一系列指令，用于构建Docker镜像。可以使用docker build命令根据Dockerfile创建镜像。- 从容器创建：可以使用docker commit命令从一个运行中的容器创建一个新的镜像。- 使用外部文件创建：可以使用docker import命令从一个本地文件或远程URL创建一个新的镜像。
  博文实验内容是介绍使用Dockerfile文件创建新镜像，博文实验环境信息如下：
- 操作系统：centos7.9- docker版本：23.0.1- docker基础镜像：Ubuntu22.04- NGINX软件版本：1.18.0
## 二、创建步骤

### 1、镜像源说明

  运行一个Ubuntu基础镜像容器，登录后我们可以确认，基础镜像中继没有wget命令，也没有查看ip地址的命令，也没有NGINX命令，时区是UTC时区。接来下我们将基于Ubuntu基础镜像，通过dockerfile的方式创建一个包含nginx并包含wget和ip addr命令的镜像文件。并给镜像设置时区为中国上海的时区。

>  
 [root@yws55 ~]# docker run -itd --name utest ubuntu:latest c4b4e6b8e891a489f0a0c60737ce34e6a4accf13adbe4b64915ee95b915d59c9 [root@yws55 ~]# docker --version Docker version 23.0.1, build a5ee5b1 [root@yws55 ~]# docker exec -it utest /bin/bash root@c4b4e6b8e891:/# which wget root@c4b4e6b8e891:/# ip addr bash: ip: command not found root@c4b4e6b8e891:/# nginx -t bash: nginx: command not found root@c4b4e6b8e891:/# date Thu Jun 8 06:52:14 UTC 2023 


### 2、创建dockerfile文件

  编辑创建一个dockerfile文件，文件是以FROM开头，选择我们的基础镜像，RUN是我们需要执行的指令，就是在基础镜像的基础上需要执行的指令，比如设置时区，安装wget、NGINX等；EXPOSE指令是需要暴露的端口；CMD命令是容器运行的时候执行的命令，这里是启动NGINX。 <img src="https://img-blog.csdnimg.cn/2455b9de5a78489fa705d11b68fbc69d.png" alt="在这里插入图片描述">

```
# 基于Ubuntu镜像创建
FROM ubuntu:latest

# 安装NGINX和wget
RUN apt-get update &amp;&amp; apt-get install -y wget iproute2 net-tools nginx

# 安装完成tzdata工具并设置时区为上海时区
RUN apt-get install -y tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 暴露80端口
EXPOSE 80

# 启动NGINX服务
CMD ["nginx","-g", "daemon off;"]

```

### 3、构建镜像

  使用docker build命令构建镜像，-t参数设置新镜像的标签，最后参数为dockerfile文件所在目录，博文实验环境这里是当前目录，所以是个点。 <img src="https://img-blog.csdnimg.cn/3f5e0fd0f54349b6b6f6f8a49015879d.png" alt="在这里插入图片描述">

### 4、查看镜像

  构建完成后我们使用docker images命令查看镜像。 <img src="https://img-blog.csdnimg.cn/ecd4d1f209a64ad695c8f25a73be151c.png" alt="在这里插入图片描述">

### 5、使用新镜像启动一个容器

>  
 [root@yws55 ~]# docker run -itd -p 8080:80 --name nginxtest ubuntu:nginx 8325a1f2eb49c48c26587976abde8120e401049a9fb21affd583522478bec976 


### 6、验证镜像内容

  使用docker exec登录容器，然后验证是否正确的安装wget、ip addr、netstat命令，以及是否安装NGINX软件并启动服务。验证下来发现已经完全安装dockerfile文件要求执行了 <img src="https://img-blog.csdnimg.cn/67c8b83e9dfa4302866f12d2087b717f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/46e0372be4754874b903dc2f538cbe67.png" alt="在这里插入图片描述">

>  
 [root@yws55 ~]# docker exec -it nginxtest /bin/bash root@26513e9f71e3:/# which wget /usr/bin/wget root@26513e9f71e3:/# ip addr … root@26513e9f71e3:/# netstat -tnpl Active Internet connections (only servers) Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name tcp 0 0 0.0.0.0:80 0.0.0.0:* LISTEN 1/nginx: master pro tcp6 0 0 :::80 ::😗 LISTEN 1/nginx: master pro root@26513e9f71e3:/# nginx -V nginx version: nginx/1.18.0 (Ubuntu) built with OpenSSL 3.0.2 15 Mar 2022 TLS SNI support enabled root@9ff3f74302cf:/# date Thu Jun 8 15:59:43 CST 2023 … 


## 三、DockerFile文件指令说明

<th align="left">指令</th><th align="left">指令说明</th>
|------
<td align="left">FROM</td><td align="left">指定基础镜像，用于构建新镜像。</td>
<td align="left">MAINTAINER</td><td align="left">指定镜像的维护者信息。</td>
<td align="left">RUN</td><td align="left">在镜像中执行命令。</td>
<td align="left">CMD</td><td align="left">指定容器启动时要执行的命令。</td>
<td align="left">EXPOSE</td><td align="left">指定容器暴露的端口。</td>
<td align="left">ENV</td><td align="left">设置环境变量。</td>
<td align="left">ADD</td><td align="left">将本地文件或目录复制到镜像中。</td>
<td align="left">COPY</td><td align="left">将本地文件或目录复制到镜像中。</td>
<td align="left">ENTRYPOINT</td><td align="left">指定容器启动时要执行的命令。</td>
<td align="left">VOLUME</td><td align="left">指定容器挂载的数据卷。</td>
<td align="left">USER</td><td align="left">指定运行容器的用户名或UID。</td>
<td align="left">WORKDIR</td><td align="left">指定容器中的工作目录。</td>
<td align="left">ARG</td><td align="left">定义构建时的参数。</td>
<td align="left">ONBUILD</td><td align="left">定义在当前镜像被用作其他镜像的基础镜像时要执行的操作。</td>
<td align="left">STOPSIGNAL</td><td align="left">指定容器停止时要发送的信号。</td>
<td align="left">LABEL</td><td align="left">为镜像添加元数据。</td>
