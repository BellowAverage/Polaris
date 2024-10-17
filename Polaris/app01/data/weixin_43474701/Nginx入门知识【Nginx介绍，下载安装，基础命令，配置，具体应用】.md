
--- 
title:  Nginx入门知识【Nginx介绍，下载安装，基础命令，配置，具体应用】 
tags: []
categories: [] 

---


#### Nginx入门知识
- <ul><li>- - - - - 


### 1、Nginx介绍

Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器。其特点是<font color="red">占有内存少，并发能力强，</font>事实上nginx的并发能力在同类型的网页服务器中表现较好，中国大陆使用nginx的网站有：百度、京东、新浪、网易、腾讯、淘宝等。

Nginx是由伊戈尔·赛索耶夫为俄罗斯访问量第二的Rambler.ru站点（俄文：Рамблер）开发的，第一个公开版本0.1.0发布于2004年10月4日。

官网：

### 2、Nginx下载和安装

可以到Nginx官方网站下载Nginx的安装包，地址为： <img src="https://img-blog.csdnimg.cn/6d2955b46ee74772bb55176e330d82b3.png" alt="在这里插入图片描述"> **安装过程：** 1、安装依赖包 yum -y install gcc pcre-devel zlib-devel openssl openssl-devel <img src="https://img-blog.csdnimg.cn/b9faafad2f9a4abdb7ffe8469f97af8a.png" alt="在这里插入图片描述">

2、下载Nginx安装包wget https://nginx.org/download/nginx-1.16.1.tar.gz <img src="https://img-blog.csdnimg.cn/358c4e4c40c9459d8e98e7a4ef5f2e3e.png" alt="在这里插入图片描述">

```
   需先安装wget------- yum install wget

```

3、解压 tar -zxvf nginx-1.16.1.tar.gz 4、cd nginx-1.16.1 5、./configure --prefix=/usr/local/nginx 安装之前做一些检查性的工作 6、make &amp;&amp; make install

### 3、Nginx概述

Nginx目录结构 安装完Nginx后，我们先来熟悉一下Nginx的目录结构，如下图： <img src="https://img-blog.csdnimg.cn/0d88f5885ce34fbd9a81c40fde1bb15c.png" alt="在这里插入图片描述">

重点目录/文件： conf/nginx.conf nginx配置文件 html 存放静态文件（html、CSS、Js等） logs 日志目录，存放日志文件 sbin/nginx 二进制文件，用于启动、停止Nginx服务

### 4、Nginx命令
-  **查看版本** 查看Nginx版本可以使用命令： <font color="red">./nginx -v</font> <img src="https://img-blog.csdnimg.cn/18bbed6238814f6694007829f58fc3e1.png" alt="在这里插入图片描述"> -  **检查配置文件正确性** 在启动Nginx服务之前，可以先检查一下conf/nginx.conf文件配置的是否有错误，命令如下：<font color="red"></font> <font color="red">./nginx -t</font> <img src="https://img-blog.csdnimg.cn/0c13cbd1d5b84f8eb3fe5b6f1a43d775.png" alt="在这里插入图片描述"> -  **启动和停止** 启动Nginx服务使用如下命令： <font color="red">./nginx</font> 停止Nginx服务使用如下命令： <font color="red">./nginx -s stop</font> 启动完成后可以查看Nginx进程： <font color="red">ps -ef | grep nginx</font> -  **重新加载配置文件** 当修改Nginx配置文件后，需要重新加载才能生效，可以使用下面命令重新加载配置文件： <font color="red">./nginx -s reload</font> 
### 5、Nginx配置文件结构

<img src="https://img-blog.csdnimg.cn/a512e67600ad4d22aee3abdc1e035252.png" alt="在这里插入图片描述">

### 6、Nginx具体应用

**部署静态资源** Nginx可以作为静态web服务器来部署静态资源。静态资源指在服务端真实存在并且能够直接展示的一些文件，比如常见的html页面、css文件、js文件、图片、视频等资源。 相对于Tomcat，Nginx处理静态资源的能力更加高效，所以在生产环境下，一般都会将静态资源部署到Nginx中。 将静态资源部署到Nginx非常简单，只需要将文件复制到Nginx安装目录下的html目录中即可。

```
server {<!-- -->
    listen 80;	#监听端口	
    server_name localhost;	服务器名称
    location / {<!-- -->	#匹配客户端请求url
        root html;	#指定静态资源根目录
        index index.html;	#指定默认首页
    }
}

```

**正向代理** 是一个位于客户端和原始服务器(origin server)之间的服务器，为了从原始服务器取得内容，客户端向代理发送一个请求并指定目标(原始服务器)，然后代理向原始服务器转交请求并将获得的内容返回给客户端。 正向代理的典型用途是为在防火墙内的局域网客户端提供访问Internet的途径。 正向代理一般是在客户端设置代理服务器，通过代理服务器转发请求，最终访问到目标服务器。 <img src="https://img-blog.csdnimg.cn/4e2204f3db784671b3db34898efe2812.png" alt="在这里插入图片描述"> **反向代理** 反向代理服务器位于用户与目标服务器之间，但是对于用户而言，反向代理服务器就相当于目标服务器，即用户直接 访问反向代理服务器就可以获得目标服务器的资源，反向代理服务器负责将请求转发给目标服务器。 用户不需要知道目标服务器的地址，也无须在用户端作任何设定。 <img src="https://img-blog.csdnimg.cn/cc58b772c0234e37b844e583b4269f78.png" alt="在这里插入图片描述"> **配置反向代理**

```
server {<!-- -->
    listen 82;
    server_name localhost;
    location / {<!-- -->
        proxy_pass http://192.168.138.101:8080; #反向代理配置，将请求转发到指定服务
    }
}

```

<img src="https://img-blog.csdnimg.cn/25551d7928b849e985454e7969d6ca82.png" alt="在这里插入图片描述"> **负载均衡** 早期的网站流量和业务功能都比较简单，单台服务器就可以满足基本需求，但是随着互联网的发展，业务流量越来越大并且业务逻辑也越来越复杂，单台服务器的性能及单点故障问题就凸显出来了，因此需要多台服务器组成应用集群，进行性能的水平扩展以及避免单点故障出现。 应用集群：将同一应用部署到多台机器上，组成应用集群，接收负载均衡器分发的请求，进行业务处理并返回响应数据 负载均衡器：将用户请求根据对应的负载均衡算法分发到应用集群中的一台服务器进行处理 <img src="https://img-blog.csdnimg.cn/5efa6aa2c365420b802141b39de3cd14.png" alt="在这里插入图片描述"> **配置负载均衡：**

```
upstream targetserver{<!-- -->	#upstream指令可以定义一组服务器
    server 192.168.138.101:8080 weight=10;
    server 192.168.138.101:8081 weight=5;
}
server {<!-- -->
    listen       8080;
    server_name  localhost;
    location / {<!-- -->
        proxy_pass http://targetserver;
    }
}

```

**负载均衡策略：** <img src="https://img-blog.csdnimg.cn/90095b5ee3c349b8b499dc6972a0b8da.png" alt="在这里插入图片描述">
