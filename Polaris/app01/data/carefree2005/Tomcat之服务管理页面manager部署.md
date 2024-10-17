
--- 
title:  Tomcat之服务管理页面manager部署 
tags: []
categories: [] 

---
## 一、tomcat服务管理页面manager简介

  Tomcat的管理页面Manager是一个Web应用程序，用于管理Tomcat服务器的部署和操作。它提供了一个易于使用的界面，可以通过Web浏览器访问。Manager可以帮助管理员对Tomcat服务器进行以下操作：
1. 部署/卸载Web应用程序1. 查看Web应用程序的运行状态和统计信息1. 启动/停止Web应用程序1. 查看Tomcat服务器的状态和运行日志1. 管理Tomcat服务器的用户和角色1. 配置Tomcat服务器的安全性和访问控制
  通过Manager，管理员可以轻松地管理Tomcat服务器的多个Web应用程序，并且可以根据需要添加、删除或更新这些应用程序。它还提供了一些有用的工具，如日志查看器和Web应用程序监视器，可以帮助管理员更好地了解Tomcat服务器的性能和运行情况。

## 二、配置步骤

  此博文以在centos7.6环境下安装配置tomcat8.5.87为例进行说明介绍。

### 1、下载tomcat

>  
 (base) [wuhs@s142 ~]$ wget https://dlcdn.apache.org/tomcat/tomcat-8/v8.5.87/bin/apache-tomcat-8.5.87.tar.gz 


### 2、解压tomcat

>  
 (base) [wuhs@s142 ~]$ tar -zxvf apache-tomcat-8.5.87.tar.gz (base) [wuhs@s142 ~]$ ln -s apache-tomcat-8.5.87 tomcat8 


### 3、启动tomcat服务

>  
 (base) [wuhs@s142 tomcat8]$ ./bin/startup.sh 


### 4、修改登录源地址限制

  修改如下两个文件，将如下参数allow=“127.\d+.\d+.\d+|::1|0:0:0:0:0:0:0:1"修改为allow=“192.168.0.x”或者allow=”^.*$"。建议仅允许信任源主机访问，如果是有多个信任源主机则使用|隔开。

>  
 (base) [wuhs@s142 tomcat8]$ vim webapps/manager/META-INF/context.xml (base) [wuhs@s142 tomcat8]$ vim webapps/host-manager/META-INF/context.xml 


### 5、配置登录账户及密码

  配置tomcat-users.xml文件，在tomcat-users组件内添加如下几行，设置管理员角色和账户密码。其中manager-gui是查看服务器状态需要的角色，admin-gui是查看host-manager需要的角色。

>  
 (base) [wuhs@s142 tomcat8]$ vim conf/tomcat-users.xml … &lt;role rolename=“manager-gui”/&gt; &lt;role rolename=“manager-jmx”/&gt; &lt;role rolename=“manager-status”/&gt; &lt;role rolename=“admin-gui”/&gt; &lt;role rolename=“admin-script”/&gt; &lt;role rolename=“manager-gui”/&gt; &lt;user username=“admin” password=“admin” roles=“manager-gui,manager-script,manager-jmx,manager-status,admin-gui,admin-script”/&gt; 


  各角色说明如下：
1. manager-gui: 允许用户通过Web界面管理Tomcat服务器。这个角色可以查看应用程序列表、启动和停止应用程序，以及查看Tomcat的当前状态。1. manager-script: 允许用户通过脚本或命令行管理Tomcat服务器。这个角色可以执行与manager-gui相同的操作，但是通过脚本或命令行。1. manager-jmx: 允许用户通过Java管理扩展（JMX）管理Tomcat服务器。这个角色可以查看和修改Tomcat的运行时状态，包括线程池、JVM参数和内存使用情况等。1. manager-status: 允许用户查看Tomcat服务器的运行状态。这个角色可以查看Tomcat的当前状态，包括内存使用情况、线程池和连接池等。1. admin-gui: 允许用户通过Web界面管理Tomcat服务器的全局配置。这个角色可以查看和修改Tomcat的全局配置，包括端口、SSL证书和安全设置等。1. admin-script: 允许用户通过脚本或命令行管理Tomcat服务器的全局配置。这个角色可以执行与admin-gui相同的操作，但是通过脚本或命令行。
### 6、设置服务端口

  tomcat默认服务端口8080，可以自定义端口，根据服务器端口规划设置指定监听端口。 <img src="https://img-blog.csdnimg.cn/462b3c51904e43c4915e7ce9b9a24356.png" alt="在这里插入图片描述">

### 7、访问tomcat页面

<img src="https://img-blog.csdnimg.cn/915b894641f5438f831cde87be364cca.png" alt="在这里插入图片描述">

### 8、登录管理页面

  点击Server Status、Manager App等管理项弹窗要求输入用户密码，将设置好的用户名密码输入后即可登录。 <img src="https://img-blog.csdnimg.cn/0fc806479cd64be69e67791ac6a3b57a.png" alt="在这里插入图片描述">

### 9、查看服务器状态

  查看服务器状态可以看到java版本、操作系统内核版本、内存使用情况等信息。 <img src="https://img-blog.csdnimg.cn/126c950c1ce84054bd4d41f7c338a659.png" alt="在这里插入图片描述">

### 10、WEB应用程序管理

  WEB应用程序管理可以管理webapp下面的各服务的启停、重载配置、更新部署等。 <img src="https://img-blog.csdnimg.cn/99ec47f13e294fb683b59790e1539017.png" alt="在这里插入图片描述">

### 11、host-manager页面

  Tomcat虚拟主机管理员的主要用途是管理Tomcat服务器上的虚拟主机。虚拟主机是指在同一台服务器上运行多个网站，每个网站都有自己的域名和IP地址，但它们共享同一个服务器资源。虚拟主机管理员可以通过Tomcat虚拟主机管理工具来创建、配置和管理虚拟主机，包括设置虚拟主机的域名、IP地址、端口号、SSL证书等。此外，虚拟主机管理员还可以监控虚拟主机的运行状态、查看虚拟主机的访问日志、清理虚拟主机的缓存等。通过Tomcat虚拟主机管理员，企业可以更加灵活地管理和利用服务器资源，提高网站的可用性和性能。 <img src="https://img-blog.csdnimg.cn/e2cefce2ee404da5ad2f71fe4539591b.png" alt="在这里插入图片描述">

## 三、QA

### 1、访问manager页面报错403
-  报错信息 <img src="https://img-blog.csdnimg.cn/37aae8cbe8a2493dad3f0237f7a21b8d.png" alt="在这里插入图片描述"> -  报错原因 manager页面默认只允许本机浏览器访问，访问源地址限制为了127.0.0.1 <img src="https://img-blog.csdnimg.cn/2cb101c2cbf643d7bd17f14cf9047cae.png" alt="在这里插入图片描述"> -  解决方案 修改源地址为可信地址（建议）或者任意地址，允许远程访问manager。 参照配置步骤中的第4步。 
### 2、访问host-manager页面报错403
- 报错信息 <img src="https://img-blog.csdnimg.cn/d842f88f05e44a2fa9524c4665ce1281.png" alt="在这里插入图片描述">- 报错原因 没有权限访问该页面- 解决方案 设置账户角色，并授权。 参照配置步骤中的第5步。