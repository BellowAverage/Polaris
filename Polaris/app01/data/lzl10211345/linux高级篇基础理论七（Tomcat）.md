
--- 
title:  linux高级篇基础理论七（Tomcat） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


**目录**





















Tomcat是 软件基金会（Apache Software Foundation）的 项目中的一个核心项目，由、Sun 和其他一些公司及个人而成。由于有了Sun 的参与和支持，最新的Servlet 和 规范总是能在Tomcat 中得到体现，Tomcat 5支持最新的Servlet 2.4 和JSP 2.0 规范。因为Tomcat 技术先进、性能稳定，而且免费，因而深受 爱好者的喜爱并得到了部分软件开发商的认可，成为比较流行的Web 。

Tomcat 服务器是一个免费的的 应用服务器，属于轻量级应用服务器，在中小型系统和并发访问用户不是很多的场合下被普遍使用，是开发和调试JSP 程序的首选。对于一个初学者来说，可以这样认为，当在一台机器上配置好Apache 服务器，可利用它响应（下的一个应用）页面的访问请求。实际上Tomcat是Apache 服务器的扩展，但它是独立运行的，所以当公司运行tomcat 时，它实际上作为一个与Apache 独立的进程单独运行的。

诀窍是，当配置正确时，Apache 为HTML页面服务，而Tomcat 实际上运行JSP 页面和Servlet。另外，Tomcat和IIS等Web服务器一样，具有处理HTML页面的功能，另外它还是一个Servlet和JSP容器，独立的Servlet容器是Tomcat的默认模式。不过，Tomcat处理静态的能力不如Apache服务器。Tomcat最新版本为10.0.23。

### 一、Tomcat

### 1、Tomcat的作用：

主要为java语言开发的web站点提供运行环境

### 2、Tomcat服务说明

主配置文件： /usr/local/tomcat8/conf/server.xml 启动服务：/usr/local/tomcat8/bin/startup.sh 停止服务：/usr/local/tomcat8/bin/shutdown.sh 端口号：tcp  8080

### 二、Tomcat使用

Tomcat的最大作用是对java编写的网页进行解析

查看JDK是否安装

运行java-version命令查看Java是否安装。如果没有安装需要自行下载安装。

<img alt="" height="131" src="https://img-blog.csdnimg.cn/direct/32cb6581e84143719f1d9e312d46c0e1.png" width="673">

##### (1)安装配置Tomcat 解压apache--tomcat--8.5.16.tar.gz包。

<img alt="" height="55" src="https://img-blog.csdnimg.cn/direct/1c2f26c490bc46999951572e081ce6f8.png" width="631">

##### (2)解压后生成

apache--tomcat--8.5.16文件夹，将该文件夹移动到/usr/local/下，并改名为tomcat8。

##### (3)启动tomcat

<img alt="" height="273" src="https://img-blog.csdnimg.cn/direct/3c695c4fb4144e9fa51f9ad9594ca962.png" width="907">

Tomcat默认运行在8080端口，运行netstat命令查看8080端口监听的信息。

<img alt="" height="74" src="https://img-blog.csdnimg.cn/direct/323a5b8525124d6da4df15e89604cd73.png" width="654">

###### 4)打开浏览器访问测试：

http://172.16.16.172:8080/,如果出现所示的界面，则 表示Tomcat已经启动成功。

<img alt="" height="451" src="https://img-blog.csdnimg.cn/direct/7d564195c1954324ad92c2f7fd5eb596.png" width="752">



Tomcat配置相关说明 Tomcat的主目录为/usr/local/tomcat8/。

<img alt="" height="365" src="https://img-blog.csdnimg.cn/direct/08d9a6edcbd449ebb60224f612b3be0d.png" width="624">

#### (1)主要目录说明。

---bin/:：存放Windows或Linux平台上启动和关闭Tomcat的脚本文件， ---conf/:存放Tomcat服务器的各种全局配置文件，其中最重要的是server.xml和web.xml。 ---lib/:存放Tomcat运行需要的库文件(JARS)。 ---logs:存放Tomcat执行时的LOG文件。 --webapps:Tomcat的主要Web发布目录（包括应用程序示例）. ---work:存放JSP编译后产生的class文件。
