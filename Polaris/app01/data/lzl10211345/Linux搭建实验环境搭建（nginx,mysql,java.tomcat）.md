
--- 
title:  Linux搭建实验环境搭建（nginx,mysql,java.tomcat） 
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





















第一台centos7搭建lnmp平台 192.168.220.128

### 1、安装Nginx：

yum -y install epel-release yum install nginx -y systemctl start nginx systemctl enable nginx

###  2、使用第三方扩展epel源安装PHP7.2：

复制php-rpm文件夹到虚拟机/root

cd /root/php-rpm yum -y localinstall *.rpm   systemctl start php-fpm systemctl enable php-fpm

### 3、安装mysql:

 复制mysql5.6-rpm文件夹到/root cd /root/mysql5.6-rpm yum -y localinstall *.rpm

systemctl start mysqld systemctl enable mysqld  

### 4.应用:搭建wordpress

（1）下载wordpress源码包 （2）复制wordpress安装包，到虚拟机/，解压并赋权     unzip wordpress-5.4.2-zh_CN.zip     chmod -R 777 /wordpress      （3）创建虚拟主机配置文件     vim /etc/nginx/conf.d/blog.conf     添加：     server {<!-- -->         listen 80;         server_name blog.benet.com;         root /wordpress;         index index.php index.html;

        location ~ \.php$ {<!-- -->                 root /wordpress;                 fastcgi_pass 127.0.0.1:9000;                 fastcgi_index index.php;                 fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;                 include fastcgi_params;         }     }     保存退出     systemctl restart nginx

    注：如果启动不了80端口，使用nginx -t检查配置文件

（4）创建blog数据库和管理用户     登录数据库：mysql     创建数据库：create database blog;     设置管理用户及密码：grant all on blog.* to lisi@localhost identified by '123.com';      （5）客户端通过域名访问blog,安装并配置     http://192.168.220.128



=========================================================================== 第二台centos7 tomcat安装 192.168.220.129

### 1.部署java环境

 java -version

### 2.部署tomcat

复制tomcat软件包到/root cd /root tar zxf apache-tomcat-8.5.66.tar.gz mv apache-tomcat-8.5.66 /opt/tomcat /opt/tomcat/bin/startup.sh             

netstat -lntup|grep 8080   

### 3.启动和关闭tomcat

/opt/tomcat/bin/startup.sh /opt/tomcat/bin/shutdown.sh

### 4.搭建jpress部署实践

1.复制mysql5.6-rpm文件夹到/root cd /root/mysql5.6-rpm yum -y localinstall *.rpm

systemctl start mysqld systemctl enable mysqld

mysqladmin -uroot -p password 123.com 回车修改密码

mysql -uroot -p123.com &gt; create database jpress default charset utf8; &gt;  flush privileges;

2.上传jpress代码 mv jpress.war /opt/tomcat/webapps/ cd /opt/tomcat/webapps cp -a jpress/*  ROOT/

3.web页面配置jpress 打开浏览器：http://192.168.220.129:8080 安装过程，数据库用户使用root



 ##############################################################

nginx反向代理(192.168.220.130)

###  1..安装配置nginx

 yum -y install epel-release yum -y install nginx

3.创建代理配置文件

 vim  /etc/nginx/conf.d/proxy.conf 添加： upstream nginx {<!-- -->     server 192.168.220.128:80; } upstream java {<!-- -->     server 192.168.220.129:8080; } server {<!-- -->     listen       80;     server_name  www.blog.com;     root   html;     index  index.html index.htm;     location / {<!-- -->         proxy_pass http://nginx;         proxy_set_header Host $http_host;         proxy_set_header X-Real-IP $remote_addr;         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;     } } server {<!-- -->     listen       80;     server_name  www.jpress.com;     root   html;     index  index.html index.htm;     location / {<!-- -->         proxy_pass http://java;         proxy_set_header Host $http_host;         proxy_set_header X-Real-IP $remote_addr;         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;     } } 保存退出

4.检查并启动nginx nginx -t systemctl start nginx

5.修改客户机192.168.220.130 hosts，域名访问 vim  /etc/hosts 192.168.220.130 www.jpress.com www.blog.com

打开浏览器：www.jpress.com

>  
 ♥️关注，就是我创作的动力 
 ♥️点赞，就是对我最大的认可 
 ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 

