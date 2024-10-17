
--- 
title:  Linux-现实环境模拟（apache、MySQL、PHP、discuz） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**努力不一定有回报，但一定会有收获加油！一起努力，共赴美好人生！** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 **♥️小刘私信可以随便问，只要会绝不吝啬，感谢CSDN让你我相遇！** 


**目录**















### **linux是什么？**

Linux，全称GNU/Linux，是一种免费使用和自由传播的操作系统，其内核由（Linus Benedict Torvalds）于1991年10月5日首次发布，它主要受到和思想的启发，是一个基于的多用户、、支持和多的。它支持和硬件，能运行主要的工具软件、应用程序和网络协议。Linux继承了Unix以网络为核心的设计思想，是一个性能稳定的多用户网络操作系统。Linux有上百种不同的发行版，如基于社区开发的、，和基于商业开发的、、等。2022年11月20日，Linux 提交了最后一批 drm-intel-next 功能补丁，Linux 6.2将迎来对英特尔锐炫独显的正式支持。

LAMP平台（分布式） 环境：三台服务器，关闭防火墙和selinux httpd: 192.168.8.128 myql:  192.168.8.129 php :  192.168.8.130

### 一、安装Apache(192.168.8.128)

    yum -y install make gcc gcc-c++ kernel-devel m4 ncurses-devel openssl-devel

编写脚本安装前提软件： mkdir /sh cd /sh vim qianti.sh 添加： #!/bin/bash cd /usr/src tar zxf apr-1.5.2.tar.gz cd apr-1.5.2 ./configure --prefix=/usr/local/apr &amp;&amp; make &amp;&amp; make install

cd .. tar zxf apr-util-1.5.4.tar.gz cd apr-util-1.5.4 ./configure --prefix=/usr/local/apr-util --with-apr=/usr/local/apr &amp;&amp; make &amp;&amp; make install

cd .. yum -y install zlib-*

tar zxf pcre-8.39.tar.gz cd pcre-8.39 ./configure --prefix=/usr/local/pcre &amp;&amp; make &amp;&amp; make install

cd .. tar zxf openssl-1.0.1u.tar.gz cd openssl-1.0.1u ./config -fPIC --prefix=/usr/local/openssl enable-shared &amp;&amp; make &amp;&amp; make install 保存退出

执行脚本：sh qianti.sh           3.安装Apache主程序 cd /sh vim httpd.sh 添加： #!/bin/bash cd /usr/src tar zxf httpd-2.4.25.tar.gz cd httpd-2.4.25 ./configure --prefix=/usr/local/httpd --enable-so --enable-cgi --enable-cgid --enable-ssl --with-ssl=/usr/local/openssl --enable-rewrite --with-pcre=/usr/local/pcre --with-apr=/usr/local/apr --with-apr-util=/usr/local/apr-util --enable-modules=most --enable-mods-shared=most --enable-mpms-shared=all --with-mpm=event --enable-proxy --enable-proxy-fcgi --enable-expires --enable-deflate &amp;&amp; make &amp;&amp; make install

 保存退出

4.优化链接 ln -s /usr/local/httpd/bin/* /usr/local/bin

添加系统服务 cp /usr/local/httpd/bin/apachectl /etc/init.d/httpd vim /etc/init.d/httpd 定位到第二行：修改为 # chkconfig: 35 85 15            \\声明服务启动级别，开机启动顺序，关机关闭顺序 # description: apache 2.4.25    \\服务声明，简要信息 保存退出 chkconfig --add httpd            \\添加httpd到系统服务 chkconfig httpd on                \\设置服务开机自启（等同于：systemctl enable httpd） systemctl start httpd            \\开启服务（等同于：service httpd start）

###  二、安装mysql（另起一台centos7）

 1.复制mysql5.6-rpm包到虚拟机/root cd /root/mysql5.6-rpm yum -y localinstall *.rpm systemctl start mysqld

### 三、安装php

1.安装前提软件  yum -y install epel-release  yum -y install gcc gcc-c++ libxml2-devel lzip2-devel libcurl-devel libmcrypt-devel openssl-devel bzip2-devel

2.复制libmcrpt和php包到/usr/src,安装libmcrypt和PHP mkdir /sh vim php.sh 添加： #!/bin/bash cd /usr/src tar zxf libmcrypt-2.5.7.tar.gz cd libmcrypt-2.5.7/ ./configure --prefix=/usr/local/libmcrypt &amp;&amp; make &amp;&amp; make install

cd /usr/src tar zxf php-5.6.27.tar.gz cd php-5.6.27/ ./configure --prefix=/usr/local/php5.6 --with-mysql=mysqlnd --with-pdo-mysql=mysqlnd --with-mysqli=mysqlnd --with-openssl --enable-fpm --enable-sockets --enable-sysvshm --enable-mbstring --with-freetype-dir --with-jpeg-dir --with-png-dir --with-zlib --with-libxml-dir=/usr --enable-xml --with-mhash --with-mcrypt=/usr/local/libmcrypt --with-config-file-path=/etc --with-config-file-scan-dir=/etc/php.d --with-bz2 --enable-maintainer-zts &amp;&amp; make &amp;&amp; make install

保存退出

sh php.sh

 4.提供 php 配置文件 cp /usr/src/php-5.6.27/php.ini-production /etc/php.ini

5.为 php-fpm 提供脚本 cd /usr/src/php-5.6.27/ cp sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm chmod +x /etc/init.d/php-fpm chkconfig --add php-fpm chkconfig php-fpm on

6.提供 php-fpm 配置文件并编辑 cp /usr/local/php5.6/etc/php-fpm.conf.default /usr/local/php5.6/etc/php-fpm.conf vim /usr/local/php5.6/etc/php-fpm.conf 修改内容如下： pid = run/php-fpm.pid listen = 192.168.8.130:9000 pm.max_children = 50 pm.start_servers = 5 pm.min_spare_servers = 5 pm.max_spare_servers = 35 保存退出

7.启动php-fpm服务 systemctl start php-fpm

###  四.测试Apache与php的静/动分离

1.启用Apache服务的代理转发 vim /usr/local/httpd/conf/httpd.conf 找到下面三行，去除#号： LoadModule proxy_module modules/mod_proxy.so LoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so Include conf/extra/httpd-vhosts.conf

找到AddType所在行，添加： AddType application/x-httpd-php .php AddType application/x-httpd-php-source .phps

定位至 DirectoryIndex，改为： DirectoryIndex index.php index.html

保存退出 systemctl restart httpd

2.配置虚拟主机文件  vim /usr/local/httpd/conf/extra/httpd-vhosts.conf 改为： &lt;VirtualHost *:80&gt;  ServerAdmin webmaster@benet.com  DocumentRoot "/wwwroot"  ServerName www.benet.com  ServerAlias benet.com  ErrorLog "logs/benet.com-error_log"  CustomLog "logs/benet.com-access_log" common  ProxyRequests Off  ProxyPassMatch ^/(.*\.php(/.*)?)$ fcgi://192.168.8.130:9000/wwwroot/$1

&lt;Directory "/wwwroot"&gt;  Options FollowSymLinks  AllowOverride None  Require all granted &lt;/Directory&gt; &lt;/VirtualHost&gt; 保存退出

systemctl restart httpd

#### 五.部署Discuz论坛

 （1）复制Discuz包到apache服务器的/usr/src目录,解压并重命名赋权（步骤一样） mkdir -p /wwwroot cd /usr/src unzip Discuz_X3.3_SC_UTF8.zip mv upload/ /wwwroot/bbs chmod -R 777 /wwwroot/bbs scp -rp /wwwroot/   root@192.168.8.130:/

 （2）在php服务器修改配置文件，重启服务 vim /etc/php.ini 找到下行并改为： short_open_tag = On 保存退出 service php-fpm restart

（3）在mysql服务器上创建bbs数据库及用户 mysql&gt; create database bbsdb; mysql&gt; grant all on bbsdb.* to runbbs@'%' identified by 'pwd@123';

（4）访问Apache，安装discuz论坛 http://192.168.8.128/bbs

>  
 ♥️关注，就是我创作的动力 
 ♥️点赞，就是对我最大的认可 
 ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 



