
--- 
title:  Linux之LNMP在线安装 
tags: []
categories: [] 

---
## 一、LNMP简介

  LNMP一键安装包是一个用Linux Shell编写的可以为CentOS/RHEL/Fedora/Debian/Ubuntu/Raspbian/Deepin/Alibaba/Amazon/Mint/Oracle/Rocky/Alma/Kali/UOS/银河麒麟/openEuler/Anolis OS Linux环境下安装Nginx、MySQL、PHP等生产环境的Shell程序。
- LNMP(Nginx/MySQL/PHP)- LNMPA(Nginx/MySQL/PHP/Apache)- LAMP(Apache/MySQL/PHP)
  编译安装需要输入大量的命令，如果是配置生产环境需要耗费大量的时间。LNMP一键安装包帮助我们简化了这些工作，无需一个一个的输入命令，无需值守，编译安装优化编译参数，提高性能，解决不必要的软件间依赖，特别针对配置自动优化。LNMP一键安装包支持自定义Nginx、PHP编译参数及网站和数据库目录、支持生成BuyPass等免费SSL证书、支持无人值守、LNMP模式支持多PHP版本、支持单独安装Nginx/MySQL/MariaDB/Pureftpd服务器，同时提供一些实用的辅助工具如：虚拟主机管理、FTP用户管理、Nginx、MySQL/MariaDB、PHP的升级、常见PHP模块exif、fileinfo、ldap、bz2、sodium、imap和swoole的一键安装、常用缓存组件Redis/Xcache等的安装、重置MySQL root密码、502自动重启、日志切割、SSH防护DenyHosts/Fail2Ban、备份等许多实用脚本。   在线安装模式要求我们的服务器主机处于联网状态，安装脚本需要在线联网下载相关软件包及其依赖包等。

## 二、LNMP下载及安装

### 1、安装包下载

  我们可以在免费下载各版本的软件包，博文发布时当前最新的稳定版本为1.9。

>  
 [root@s142 opt]# wget http://soft.vpser.net/lnmp/lnmp1.9.tar.gz 


### 2、解压软件包

  解压软件包，我们可以看到目录下的内容如下，包括安装脚本、卸载脚本、升级脚本、安装pureftpd脚本、相关配置文件等。

>  
 [root@s142 opt]# tar -zxvf lnmp1.9.tar.gz … [root@s142 opt]# cd lnmp1.9 <img src="https://img-blog.csdnimg.cn/3e17bdb4b2ed4fc6b977cf9994518ca6.png" alt="在这里插入图片描述"> 


### 3、获取安装脚本帮助

  可以使用-help查看命令帮助，命令使用方式为./install.sh 参数，参数只支持lnmp、lnmpa、lamp、nginx、db、mphp，实际上并没有–help这个参数，查看脚本内容我们会发现你输入除指定的六个参数外的任何内容都会显示如下信息。

>  
 [root@s142 lnmp1.9]# ./install.sh --help <img src="https://img-blog.csdnimg.cn/f3a49041d1284c68beec5ac14f09b15c.png" alt="在这里插入图片描述"> 


### 4、安装lnmp

>  
 [root@s142 lnmp1.9]# ./install.sh lnmp 


### 5、选择数据库安装版本

  选择要安装的数据库版本，支持mysql和mariadb，默认安装mysql5.5版本。 <img src="https://img-blog.csdnimg.cn/6626f4d4021942d984992d54c5ff2f10.png" alt="在这里插入图片描述">

### 6、选择PHP安装版本

  选择我们需要安装的PHP版本，后续博主准备安装WordPress环境，要求PHP版本7.4以上，所以这里选择安装PHP 7.4.30版本。选择完php还需要选择是否安装内存优化器，博主这里选择了不安装。 <img src="https://img-blog.csdnimg.cn/978c32d624574b0c9f80117bfd3c601d.png" alt="在这里插入图片描述">

### 7、安装完成

<img src="https://img-blog.csdnimg.cn/cb74790e343c487eb5a3a664b3c62a78.png" alt="在这里插入图片描述">

## 三、LNMP运维管理相关服务

  lnmp不仅仅给我们简化了安装nginx、php、mysql的过程，也简化了这软件的运维管理，全部可以使用lnmp命令完成日常管理。可以使用lnmp实现这几个软件服务的一键启停，也可以单独执行某个软件发启停。还可以用于添加nginx的配置，添加和删除mysql数据库实例、添加和管理ftp账户。

### 1、查看lnmp运行状态

>  
 [root@s142 lnmp1.9]# lnmp status ±------------------------------------------+ | Manager for LNMP, Written by Licess | ±------------------------------------------+ | https://lnmp.org | ±------------------------------------------+ nginx (pid 3840) is running… php-fpm is runing! SUCCESS! MySQL running (4413) 


### 2、获取lnmp命令帮助

>  
 [root@s142 lnmp1.9]# lnmp --help ±------------------------------------------+ | Manager for LNMP, Written by Licess | ±------------------------------------------+ | https://lnmp.org | ±------------------------------------------+ Usage: lnmp {start|stop|reload|restart|kill|status} Usage: lnmp {nginx|mysql|mariadb|php-fpm|pureftpd} {start|stop|reload|restart|kill|status} Usage: lnmp vhost {add|list|del} Usage: lnmp database {add|list|edit|del} Usage: lnmp ftp {add|list|edit|del|show} Usage: lnmp ssl add Usage: lnmp {dnsssl|dns} {cx|ali|cf|dp|he|gd|aws} Usage: lnmp onlyssl {cx|ali|cf|dp|he|gd|aws} 


### 3、停止lnmp

>  
 [root@s142 lnmp1.9]# lnmp stop ±------------------------------------------+ | Manager for LNMP, Written by Licess | ±------------------------------------------+ | https://lnmp.org | ±------------------------------------------+ Stoping LNMP… Stoping nginx… done Shutting down MySQL… SUCCESS! Gracefully shutting down php-fpm . done 


### 4、启动lnmp

>  
 [root@s142 lnmp1.9]# lnmp start ±------------------------------------------+ | Manager for LNMP, Written by Licess | ±------------------------------------------+ | https://lnmp.org | ±------------------------------------------+ Starting LNMP… Starting nginx… done Starting MySQL… SUCCESS! Starting php-fpm done 


### 5、重启nginx

>  
 [root@s142 lnmp1.9]# lnmp nginx restart ±------------------------------------------+ | Manager for LNMP, Written by Licess | ±------------------------------------------+ | https://lnmp.org | ±------------------------------------------+ Stoping nginx… done Starting nginx… done 


### 6、查看nginx vhost

>  
 [root@s142 lnmp1.9]# lnmp vhost list ±------------------------------------------+ | Manager for LNMP, Written by Licess | ±------------------------------------------+ | https://lnmp.org | ±------------------------------------------+ Nginx Virtualhost list: www.sun-site.com.cn 


### 7、添加一个数据库

>  
 [root@s142 lnmp1.9]# lnmp database add ±------------------------------------------+ | Manager for LNMP, Written by Licess | ±------------------------------------------+ | https://lnmp.org | ±------------------------------------------+ Enter current root password of Database (Password will not shown): OK, MySQL root password correct. Enter database name: wuhstest Your will create a database and MySQL user with same name: wuhstest Please enter password for mysql user wuhstest: 123456 Your password: 123456 Add database Sucessfully. 


### 8、查看数据库列表

>  
 [root@s142 lnmp1.9]# lnmp database list ±------------------------------------------+ | Manager for LNMP, Written by Licess | ±------------------------------------------+ | https://lnmp.org | ±------------------------------------------+ Enter current root password of Database (Password will not shown): OK, MySQL root password correct. ±-------------------+ | Database | ±-------------------+ | information_schema | | mysql | | performance_schema | | sys | | wuhstest | ±-------------------+ List all databases Sucessfully. 


## 四、升降级软件版本

  运维工作中难免会遇到升级软件版本的情况，lnmp的upgrade.sh脚本不仅仅可以升级软件版本，也可以降级软件版本。进行软件版本升降级之前，我们可以去nginx、mysql等相关软件官网查看正确的版本号。升降级的时候我们只需要输入正确的版本号即可实现版本的升降级啦。

### 1、升级nginx

>  
 [root@s142 lnmp1.9]# nginx -V nginx version: nginx/1.22.0 … [root@s142 lnmp1.9]# ./upgrade.sh ±----------------------------------------------------------------------+ | Upgrade script for LNMP V1.9, Written by Licess | ±----------------------------------------------------------------------+ | A tool to upgrade Nginx,MySQL/Mariadb,PHP for LNMP/LNMPA/LAMP | ±----------------------------------------------------------------------+ | For more information please visit https://lnmp.org | ±----------------------------------------------------------------------+ 1: Upgrade Nginx 2: Upgrade MySQL 3: Upgrade MariaDB 4: Upgrade PHP for LNMP 5: Upgrade PHP for LNMPA or LAMP 6: Upgrade MySQL to MariaDB 7: Upgrade phpMyAdmin 8: Upgrade Multiple PHP exit: Exit current script ################################################### Enter your choice (1, 2, 3, 4, 5, 6, 7 or exit): 1 Current Nginx Version:1.22.0 You can get version number from http://nginx.org/en/download.html Please enter nginx version you want, (example: 1.20.2): 1.23.0 … Program will display Nginx Version… nginx version: nginx/1.23.0 ======== upgrade nginx completed ====== [root@s142 lnmp1.9]# nginx -V nginx version: nginx/1.23.0 


### 2、降级mysql

>  
 [root@s142 lnmp1.9]# mysql -V mysql Ver 14.14 Distrib 5.7.38, for linux-glibc2.12 (x86_64) using EditLine wrapper … [root@s142 lnmp1.9]# ./upgrade.sh mysql ±----------------------------------------------------------------------+ | Upgrade script for LNMP V1.9, Written by Licess | ±----------------------------------------------------------------------+ | A tool to upgrade Nginx,MySQL/Mariadb,PHP for LNMP/LNMPA/LAMP | ±----------------------------------------------------------------------+ | For more information please visit https://lnmp.org | ±----------------------------------------------------------------------+ Enter current root password of Database (Password will not shown): OK, MySQL root password correct. Current MYSQL Version:5.7.38 You can get version number from http://dev.mysql.com/downloads/mysql/ Please input MySQL Version you want. (example: 5.5.60 ): 5.7.29 Using Generic Binaries [y/n]: y You will install MySQL 5.7.29 Using Generic Binaries. =========================== Do you want to install the InnoDB Storage Engine? (Default yes,if you want please enter: y , if not please enter: n): y You will install the InnoDB Storage Engine ================================================== You will upgrade MySQL Version to 5.7.29 ==================================================  Press any key to start…or Press Ctrl+c to cancel … [root@s142 lnmp1.9]# mysql -V mysql Ver 14.14 Distrib 5.7.29, for linux-glibc2.12 (x86_64) using EditLine wrapper 


## 五、其他

### 1、卸载lnmp

>  
 [root@s142 lnmp1.9]# ./uninstall.sh <img src="https://img-blog.csdnimg.cn/6f5871989dfb427aa6cf99380e80c709.png" alt="在这里插入图片描述"> 


### 2、单独安装某个软件

  我们可以使用lnmp安装nginx、php、mysql其中一个软件，下面以安装nginx为例。

>  
 [root@s142 lnmp1.9]# ./install.sh nginx … Add iptables service at system startup… ============================== Check install ============================== Checking … Nginx: OK [root@s142 lnmp1.9]# nginx -V nginx version: nginx/1.22.0 


### 3、各软件安装路径
- Nginx 目录: /usr/local/nginx/- MySQL 目录 : /usr/local/mysql/- MySQL数据库所在目录：/usr/local/mysql/var/- MariaDB 目录 : /usr/local/mariadb/- MariaDB数据库所在目录：/usr/local/mariadb/var/- PHP目录 : /usr/local/php/- 多PHP版本目录 : /usr/local/php5.5/ 其他版本前面5.5的版本号换成其他即可- Nginx日志目录：/home/wwwlogs/- /root/vhost.sh添加的虚拟主机配置文件所在目录：/usr/local/nginx/conf/vhost/- PureFtpd 目录：/usr/local/pureftpd/
### 4、配置文件存储路径
- LNMP相关配置文件位置- Nginx主配置(默认虚拟主机)文件：/usr/local/nginx/conf/nginx.conf- 添加的虚拟主机配置文件：/usr/local/nginx/conf/vhost/域名.conf- MySQL配置文件：/etc/my.cnf- PHP配置文件：/usr/local/php/etc/php.ini- php-fpm配置文件：/usr/local/php/etc/php-fpm.conf- PureFtpd配置文件：/usr/local/pureftpd/pure-ftpd.conf 1.3及更高版本：/usr/local/pureftpd/etc/pure-ftpd.conf
### 5、操作日志存储路径

  使用安装、升级、卸载脚本执行的日志记录存储在执行账户家目录下。 <img src="https://img-blog.csdnimg.cn/34cdf997992f4090914e81d53db20ec0.png" alt="在这里插入图片描述">
