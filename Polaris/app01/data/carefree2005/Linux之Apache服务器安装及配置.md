
--- 
title:  Linux之Apache服务器安装及配置 
tags: []
categories: [] 

---
## 一、Apache服务器简介

  Apache HTTP Server（简称Apache）是Apache软件基金会的一个开放源码的网页服务器，可以在大多数计算机操作系统中运行，由于其多平台和安全性被广泛使用。Apache曾经是世界使用排名第一的Web服务器软件（2019年4月后nginx第一）。它可以运行在几乎所有广泛使用的计算机平台上。Apache 源于NCSAhttpd服务器，经过多次修改，成为世界上最流行的Web服务器软件之一。Apache取自“a patchy server”的读音，意思是充满补丁的服务器，因为它是自由软件，所以不断有人来为它开发新的功能、新的特性、修改原来的缺陷。Apache的特点是简单、速度快、性能稳定，并可做代理服务器来使用。当前最新稳定版是2.4.52，博文实验环境：
- 操作系统：centos7.6- Apache版本：2.4.6
## 二、YUM安装Apache

  在另外一篇博文中介绍了如何源码编译安装Apache服务，如果对于版本没有特别要求，centos环境下最简单快捷的安装方式还是yum安装，centos7环境下yum安装版本为2.4.6。

### 1、YUM安装Apache

>  
 [root@s152 ~]# yum install -y httpd 


### 2、查看版本

>  
 [root@s152 ~]# httpd -v Server version: Apache/2.4.6 (CentOS) Server built: May 30 2023 14:01:11 


### 3、服务管理

>  
 #启动服务 [root@s152 /]# systemctl start httpd #停止服务 [root@s152 /]# systemctl stop httpd #服务开机自启动 [root@s152 /]# systemctl enable httpd #查看服务状态 [root@s152 /]# systemctl status httpd #检查配置文件 [root@s152 /]# httpd -t Syntax OK #重载配置文件，不重启服务，如下三种方式都可以 [root@s152 /]# httpd -k graceful [root@s152 /]# apachectl graceful [root@s152 /]# systemctl reload httpd 


## 三、常见配置参数说明

  如下是Apache服务器安装完成后的默认配置文件，这里我们只针对其中常用的配置参数进行释义说明。

### 1、默认httpd.conf配置

```
[root@s152 ~]# cat /etc/httpd/conf/httpd.conf |grep -Ev "^$|#"
ServerRoot "/etc/httpd"
Listen 80
Include conf.modules.d/*.conf
User apache
Group apache
ServerAdmin root@localhost
&lt;Directory /&gt;
    AllowOverride none
    Require all denied
&lt;/Directory&gt;
DocumentRoot "/var/www/html"
&lt;Directory "/var/www"&gt;
    AllowOverride None
    Require all granted
&lt;/Directory&gt;
&lt;Directory "/var/www/html"&gt;
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
&lt;/Directory&gt;
&lt;IfModule dir_module&gt;
    DirectoryIndex index.html
&lt;/IfModule&gt;
&lt;Files ".ht*"&gt;
    Require all denied
&lt;/Files&gt;
ErrorLog "logs/error_log"
LogLevel warn
&lt;IfModule log_config_module&gt;
    LogFormat "%h %l %u %t \"%r\" %&gt;s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
    LogFormat "%h %l %u %t \"%r\" %&gt;s %b" common
    &lt;IfModule logio_module&gt;
      LogFormat "%h %l %u %t \"%r\" %&gt;s %b \"%{Referer}i\" \"%{User-Agent}i\" %I %O" combinedio
    &lt;/IfModule&gt;
    CustomLog "logs/access_log" combined
&lt;/IfModule&gt;
&lt;IfModule alias_module&gt;
    ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"
&lt;/IfModule&gt;
&lt;Directory "/var/www/cgi-bin"&gt;
    AllowOverride None
    Options None
    Require all granted
&lt;/Directory&gt;
&lt;IfModule mime_module&gt;
    TypesConfig /etc/mime.types
    AddType application/x-compress .Z
    AddType application/x-gzip .gz .tgz
    AddType text/html .shtml
    AddOutputFilter INCLUDES .shtml
&lt;/IfModule&gt;
AddDefaultCharset UTF-8
&lt;IfModule mime_magic_module&gt;
    MIMEMagicFile conf/magic
&lt;/IfModule&gt;
EnableSendfile on
IncludeOptional conf.d/*.conf

```

### 2、常用参数释义

<th align="left">参数</th><th align="left">参数说明</th><th align="left">配置示例</th>
|------
<td align="left">ServerRoot</td><td align="left">Apache服务器的根目录</td><td align="left">ServerRoot “/etc/httpd”</td>
<td align="left">Listen</td><td align="left">指定Apache监听的IP地址和端口</td><td align="left">Listen 80</td>
<td align="left">DocumentRoot</td><td align="left">指定Web服务器的文档根目录，即网站文件存放的位置</td><td align="left">DocumentRoot “/var/www/html”</td>
<td align="left">Directory</td><td align="left">配置目录的权限和特性</td><td align="left">&lt;Directory “/var/www/html”&gt;  Options Indexes FollowSymLinks  AllowOverride None  Require all granted  &lt;/Directory&gt;</td>
<td align="left">DirectoryIndex</td><td align="left">指定当访问一个目录时默认显示的文件</td><td align="left">DirectoryIndex index.html、</td>
<td align="left">AllowOverride</td><td align="left">指定是否允许使用.htaccess文件覆盖目录配置</td><td align="left">AllowOverride All</td>
<td align="left">LogLevel</td><td align="left">设置日志级别，用于记录错误和警告信息</td><td align="left">LogLevel warn</td>
<td align="left">ErrorLog</td><td align="left">指定错误日志文件的路径</td><td align="left">ErrorLog “/var/log/httpd/error_log”</td>
<td align="left">CustomLog</td><td align="left">指定访问日志文件的路径和格式</td><td align="left">CustomLog “/var/log/httpd/access_log” combined</td>
<td align="left">ServerSignature</td><td align="left">控制服务器生成的错误页面中是否包含服务器的签名信息</td><td align="left">ServerSignature Off</td>
<td align="left">KeepAlive</td><td align="left">启用或禁用Keep-Alive功能，决定是否保持持久连接</td><td align="left">KeepAlive On</td>
<td align="left">Timeout</td><td align="left">设置服务器等待客户端请求的超时时间</td><td align="left">Timeout 300</td>
<td align="left">MaxClients</td><td align="left">限制同时连接到服务器的最大客户端数</td><td align="left">MaxClients 150</td>
<td align="left">IncludeOptional</td><td align="left">Apache主配置文件中引入其他配置文件</td><td align="left">IncludeOptional conf.d/*.conf</td>
<td align="left">User</td><td align="left">httpd服务运行用户</td><td align="left">User apache</td>
<td align="left">Group</td><td align="left">httpd服务所属群组</td><td align="left">Group apache</td>
<td align="left">ServerName</td><td align="left">虚拟服务器主机名和端口，主机名可以是IP地址也可以是域名</td><td align="left">ServerName 192.168.0.152:80</td>

## 四、服务配置举例

  这里我们以部署为例，介绍如何在Apache服务上部署服务。

### 1、创建一个虚拟主机配置文件

  进入/etc/httpd/conf.d/目录下创建一个虚拟主机配置文件，主机名为mytest.com，对应监听的80端口，如果需要更换其他端口需要在主文件中listen添加或者修改，这是与nginx不同的地方。

```
[root@s152 mytest]# cd /etc/httpd/conf.d/
[root@s152 conf.d]# cat test.conf 
&lt;VirtualHost *:80&gt;
    # 设置虚拟主机的域名
    ServerName mytest.com
    ServerAlias www.mytest.com

    # 设置文档根目录
    DocumentRoot "/var/www/mytest"

    # 日志文件
    ErrorLog "/var/log/httpd/mytest_error_log"
    CustomLog "/var/log/httpd/mytest_access_log" combined

    # 目录权限
    &lt;Directory "/var/www/mytest"&gt;
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    &lt;/Directory&gt;

    # 可以添加其他定制的配置项，如重定向、代理等

&lt;/VirtualHost&gt;

```

### 2、将猜拳服务代码打包上传到Directory

  配置文件中虚拟服务目录位于/var/www/mytest目录下，我们创建该目录后将软件包上传到该目录下。

>  
 [root@s152 www]# mkdir mytest [root@s152 www]# cd mytest/ [root@s152 mytest]# ll 总用量 40 drwxr-xr-x. 2 root root 100 11月 1 2022 caiquan -rw-r–r–. 1 root root 38541 11月 29 15:33 caiquan.zip 


### 3、重启httpd服务

  使用httpd -t检查配置文件，检查无误后我们重启服务或者重新加载配置文件。

>  
 [root@s152 conf.d]# httpd -t Syntax OK [root@s152 conf.d]# systemctl restart httpd 


### 4、修改hosts文件

  这里实验用的域名非正式域名，我们需要在hosts文件添加自定义解析。 <img src="https://img-blog.csdnimg.cn/direct/53a0376cc0df4d59ae4812a8fe6dc90d.png" alt="在这里插入图片描述">

### 5、访问验证

  打开浏览器，通过域名和路径就可以访问我们的猜拳游戏内容啦！ <img src="https://img-blog.csdnimg.cn/direct/89d5d60ecee042ee9b4b35db65a4ca8a.png" alt="在这里插入图片描述">

## 五、QA

### 1、启动报错httpd: Could not reliably determine the server’s fully qualified domain name
- 报错信息：httpd: Could not reliably determine the server’s fully qualified domain name- 报错原因：httpd.conf配置文件中未配置ServerName- 解决方案：修改httpd.conf配置文件，添加ServerName = domain.com:80 参数配置
### 2、启动报错httpd (pid xxxxx) already running导致无法启动
- 报错信息：httpd (pid xxxxx) already running 和 httpd.service: control process exited, code=exited status=1- 报错原因：httpd服务未正常退出导致无法启动- 解决方案：执行pgrep -f httpd |xargs kill后再次启动。