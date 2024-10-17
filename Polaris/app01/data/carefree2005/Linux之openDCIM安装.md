
--- 
title:  Linux之openDCIM安装 
tags: []
categories: [] 

---
## 一、openDCIM简介

  openDCIM是一个开源的数据中心基础设施管理（DCIM）软件，用于管理和监控数据中心的物理基础设施，包括机架、设备、电源、网络和空调等。openDCIM提供了一个集中的管理平台，使用户能够追踪和监控数据中心中的所有设备和资源。它可以记录设备的位置、电源需求、网络连接和其他相关信息，并提供实时的监控和警报功能。openDCIM还提供了一些高级功能，如容量规划、电源管理、网络拓扑图和报告生成等。用户可以根据自己的需求自定义和配置这些功能，以满足不同的数据中心管理需求。   作为开源软件，openDCIM可以免费下载和使用。它的源代码也是公开的，用户可以根据自己的需求进行修改和定制。这使得openDCIM成为一个灵活和可扩展的解决方案，适用于各种规模和类型的数据中心。总而言之，openDCIM是一款功能强大的开源DCIM软件，可以帮助用户有效地管理和监控数据中心的物理基础设施。

## 二、安装要求

  博文以centos7环境下安装openDCIM 23.02为例介绍安装步骤，环境要求如下：
- 要求安装Apache2.x及以上版本，并支持SSL；- 要求安装mysql5.x以上版本；- 要求安装PHP8.0以上版本；- 用户验证- Web客户端- 操作系统要求centos7或者Ubuntu18.04以上版本。
## 三、安装步骤

### 1、安装LAMP

  截止2023年11月最新稳定版本为lnmp2.0版本，下载lnmp2.0并安装，然后根据安装要求安装Apache2.4，mysql5.7，PHP8.2，安装方式可以参考博文。实际上lnmp安装脚本不仅可以安装lnmp，也可以安装LAMP。

>  
 [root@s152 opt]# wget https://soft.lnmp.com/lnmp/lnmp2.0.tar.gz -O lnmp2.0.tar.gz &amp;&amp; tar zxf lnmp2.0.tar.gz &amp;&amp; cd lnmp2.0 &amp;&amp; ./install.sh lamp … 


### 2、查验LAMP版本

>  
 [root@s152 opt]# which httpd /usr/bin/which: no httpd in (/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin) [root@s152 opt]# /usr/local/apache/bin/httpd -v Server version: Apache/2.4.57 (Unix) Server built: Nov 30 2023 17:26:35 [root@s152 opt]# php -v PHP 8.2.6 (cli) (built: Nov 30 2023 17:31:21) (ZTS) Copyright © The PHP Group Zend Engine v4.2.6, Copyright © Zend Technologies [root@s152 opt]# mysql -V mysql Ver 14.14 Distrib 5.7.42, for linux-glibc2.12 (x86_64) using EditLine wrapper [root@s152 opt]# cat /etc/centos-release CentOS Linux release 7.6.1810 (Core) 


### 3、下载openDCIM

  官网下载软件包，境外网站，下载速度可能会有点慢。

>  
 wget https://www.opendcim.org/packages/openDCIM-23.04.tar.gz 


### 4、解压openDCIM

  将openDCIM软件包解压到Apache的根目录下，/var/www/html是Apache默认根目录，当然这里也可以自定义。

>  
 [root@s152 opt]# tar -zxvf openDCIM-23.02.tar.gz -C /var/www [root@s152 opt]# cd /var/www/ [root@s152 www]# ln -s openDCIM-23.02 opendcim 


### 5、创建opendcim库及用户

  登录安装的mysql实例，创建一个opendcim库。

>  
 mysql&gt; create database opendcim; Query OK, 1 row affected (0.03 sec) <img src="https://img-blog.csdnimg.cn/direct/1af3d228933740abbcf81e397e5872cd.png" alt="在这里插入图片描述"> 


### 6、修改 db.inc.php配置

  通过复制创建db.inc.php文件，并根据实际创建的数据库名、用户、密码等修改配置参数。

>  
 [root@s152 opendcim]# cp db.inc.php-dist db.inc.php <img src="https://img-blog.csdnimg.cn/direct/4a6c1464c2d84d0ba43598c6c961a7d8.png" alt="在这里插入图片描述"> 


### 6、创建htpasswd认证

  如果找不到htpasswd命令那应该是没有添加/usr/local/apache/bin到环境变量中，可以切换到该路径下执行或者添加到环境变量中就可以执行httpd相关命令了。

>  
 [root@s152 conf.d]# touch /var/www/.htpasswd [root@s152 conf.d]# htpasswd /var/www/.htpasswd admin New password: Re-type new password: Adding password for user admin 


### 7、创建Apache虚拟主机配置

  完成虚拟主机配置后记得重启Apache服务。

```
[root@s152 conf.d]# cd /usr/local/apache/conf/vhost/
[root@s152 vhost]# cat dcim.conf 
&lt;VirtualHost *:80&gt;
    # 设置虚拟主机的域名
    ServerName mytest.com
    ServerAlias www.mytest.com

    # 设置文档根目录
    DocumentRoot "/var/www/opendcim"

    # 日志文件
    ErrorLog "/var/log/httpd/mytest_error_log"
    CustomLog "/var/log/httpd/mytest_access_log" combined

    # 目录权限
    &lt;Directory "/var/www/opendcim"&gt;
        AllowOverride All
        AuthType Basic
        AuthName "openDCIM"
        AuthUserFile /var/www/.htpasswd
        Require valid-user
    &lt;/Directory&gt;

&lt;/VirtualHost&gt;


```

>  
 [root@s152 vhost]# lnmp httpd resart 


### 8、登录

  输入第六步设置的Apache验证账户和密码登录系统。 <img src="https://img-blog.csdnimg.cn/direct/c726d88a69d14d77a680bfe74f8607ed.png" alt="在这里插入图片描述">

### 9、安装完成

  登录之后会进行数据库初始化等，需要1分钟左右，待初始化完成之后就会自动跳转到index.php页面。 <img src="https://img-blog.csdnimg.cn/direct/2f37430cd88a40aab7af79f8676a75bd.png" alt="在这里插入图片描述">   看到如上页面就说明openDCIM安装成功啦，关于openDCIM的配置和使用博主有空的时候另外出博文进行介绍。
