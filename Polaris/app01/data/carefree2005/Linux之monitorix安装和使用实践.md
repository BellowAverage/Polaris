
--- 
title:  Linux之monitorix安装和使用实践 
tags: []
categories: [] 

---
## 一、monitorix简介

  Monitorix是一个免费、开源、轻量级的系统监控工具，旨在监控尽可能多的服务和系统资源。它是为在生产Linux/UNIX服务器下使用而创建的，但由于它的简单性和小尺寸，也可以在嵌入式设备上使用。   它主要由两个程序组成：一个称为monitorix的收集器，它是一个Perl守护进程，与任何其他系统服务一样自动启动，另一个名为monitorix.CGI的CGI脚本。Monitorix包含自己内置的HTTP服务器（默认情况下在端口8080/TCP上侦听），以查看统计图，因此您不必安装第三方web服务器来使用它。只需将浏览器指向http://ip:8080/monitorix。   monitorix优势是保持持续更新中，博文发布时最新版本为3.14.0，发布时间是2022年6月18日，如果想了解更多信息可以访问。

## 二、安装步骤

### 1、安装yum扩展源

>  
 [root@s142 tmp]# yum install -y epel-release 


### 2、安装依赖包

  使用yum方式安装，这一步可以跳过，如果我们使用rpm包的方式安装则需要先安装这些依赖包。

>  
 [root@s142 tmp]# yum install rrdtool rrdtool-perl perl-libwww-perl perl-MailTools perl-CGI perl-DBI perl-XML-Simple perl-Config-General perl-IO-Socket-SSL perl-HTTP-Server-Simple wget 


### 3、安装monitorix

>  
 [root@s142 tmp]# yum install -y monitorix … Installed: monitorix.noarch 0:3.14.0-1.el7 … <img src="https://img-blog.csdnimg.cn/ef90ed8520354c7598f77bdb5a3f9b8d.png" alt="在这里插入图片描述"> 


### 4、修改配置文件

>  
 [root@s142 tmp]# vim /etc/monitorix/monitorix.conf … title = s142服务器监控 hostname = s142 … &lt;httpd_builtin&gt; … port = 8888 … 


### 5、启动服务

>  
 #启动服务 [root@s142 tmp]# systemctl start monitorix #设置为开机自启动 [root@s142 tmp]# systemctl enable monitorix 


## 三、使用简介

### 1、浏览器访问监控页

  如果是在web服务器上部署为了避免端口冲突，默认是8080端口，我们需要自定义服务端口。如果开启了防火墙我们还需要关闭防火墙或者开放8888端口，访问http://x.x.x.x:8888/monitorix，界面如下。 <img src="https://img-blog.csdnimg.cn/24b2c6f1ccd54c22a4637cb09e7e78b4.png" alt="在这里插入图片描述">

### 2、系统负载平均值和使用率

<img src="https://img-blog.csdnimg.cn/a5b7c4615f774482b68fabc1c68efa29.png" alt="在这里插入图片描述">

### 3、内核CPU使用情况

<img src="https://img-blog.csdnimg.cn/c25ddc40a4d742aab47b6f8174d6e05b.png" alt="在这里插入图片描述">

### 4、I/O使用情况

<img src="https://img-blog.csdnimg.cn/e7f482c8a8874077aac4912187f5f7ab.png" alt="在这里插入图片描述">

### 5、网卡流量及使用率

<img src="https://img-blog.csdnimg.cn/4dcea66dd3934dd89d3571b47fbd2399.png" alt="在这里插入图片描述">

### 6、网络连接情况

<img src="https://img-blog.csdnimg.cn/61f705b56a8e494f9b960aeb3efbd56a.png" alt="在这里插入图片描述">

### 7、查看各服务端口流量

<img src="https://img-blog.csdnimg.cn/ac2d1621a0bb4a5285898d7ff7cc6ae2.png" alt="在这里插入图片描述">

### 8、设置允许访问白名单

  为了数据安全，我们可以设置运行访问监控页的IP地址白名单，配置deny所有，允许指定IP地址就可以完成IP地址白名单配置。

>  
 [root@s142 tmp]# vim /etc/monitorix/monitorix.conf … hosts_deny = all hosts_allow = 192.168.0.19 … [root@s142 tmp]# systemctl restart monitorix <img src="https://img-blog.csdnimg.cn/948b643513ab438289d0fab8d8208a6d.png" alt="在这里插入图片描述"> 


### 9、配置登录验证账户

  IP地址白名单还不满足安全要求，我们还可以配置账户验证，将auth参数中的enabled由n改为y即可。另外我们需要在/var/lib/monitorix/htpasswd文件中配置登录账户，格式为：user:passswd，其中passwd为加密格式，我们可以使用openssl命令实现密码加密并写入到该文件中，可以配置多个账号，一行表示一个账号。

>  
 [root@s142 tmp]# openssl passwd 123123 &gt;&gt; /var/lib/monitorix/htpasswd [root@s142 tmp]# vim /var/lib/monitorix/htpasswd wuhs:zAyYdRtMtEOLs #使用用户名:密码的方式配置验证文件，配置完成后保存文件 [root@s142 tmp]# vim /etc/monitorix/monitorix.conf … &lt;auth&gt; enabled = y … [root@s142 tmp]# systemctl restart monitorix <img src="https://img-blog.csdnimg.cn/5907a7be907f44269a649d9463839089.png" alt="在这里插入图片描述"> 


### 10、监控其他

  在配置文件中我们可以看到monitorix.conf配置文件中是可以包含其他配置文件的，实际上monitorix这个工具除了监控服务器基础指标外还可以监控nginx、Apache、mysql、pgsql等，这个需要我们单独配置，结合相关软件一起使用。关于如何使用monitorix监控nginx、mysql博主将单独写文章进行介绍。 <img src="https://img-blog.csdnimg.cn/95f4bcdb6b6b4d12a2aaeca5b3351fea.png" alt="在这里插入图片描述">
