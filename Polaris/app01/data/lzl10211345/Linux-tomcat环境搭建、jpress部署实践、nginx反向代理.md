
--- 
title:  Linux-tomcat环境搭建、jpress部署实践、nginx反向代理 
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























































### tomcat是什么？

>  
 Tomcat是Apache 软件基金会（Apache Software Foundation）的Jakarta 项目中的一个核心项目，由Apache、Sun 和其他一些公司及个人共同开发而成。由于有了Sun 的参与和支持，最新的Servlet 和JSP 规范总是能在Tomcat 中得到体现，Tomcat 5支持最新的Servlet 2.4 和JSP 2.0 规范。因为Tomcat 技术先进、性能稳定，而且免费，因而深受Java 爱好者的喜爱并得到了部分软件开发商的认可，成为比较流行的Web 应用服务器。Tomcat 服务器是一个免费的开放源代码的Web 应用服务器，属于轻量级应用服务器，在中小型系统和并发访问用户不是很多的场合下被普遍使用，是开发和调试JSP 程序的首选。对于一个初学者来说，可以这样认为，当在一台机器上配置好Apache 服务器，可利用它响应HTML（标准通用标记语言下的一个应用）页面的访问请求。实际上Tomcat是Apache 服务器的扩展，但运行时它是独立运行的，所以当公司运行tomcat 时，它实际上作为一个与Apache 独立的进程单独运行的。诀窍是，当配置正确时，Apache 为HTML页面服务，而Tomcat 实际上运行JSP 页面和Servlet。另外，Tomcat和IIS等Web服务器一样，具有处理HTML页面的功能，另外它还是一个Servlet和JSP容器，独立的Servlet容器是Tomcat的默认模式。不过，Tomcat处理静态HTML的能力不如Apache服务器。Tomcat最新版本为10.0.23。 


### tomcat安装

#### 1.部署java环境

yum install java-1.8.0 -y java -version

#### 2.部署tomcat

mkdir /data/soft -p cd /data/soft/ 复制tomcat包到/data/soft

tar zxf apache-tomcat-8.5.64.tar.gz -C /opt/ cd /opt ln -s apache-tomcat-8.5.64 tomcat /opt/tomcat/bin/startup.sh                 #启动tomcat

netstat -lntup|grep 8080                #查看端口 tail -1 /opt/tomcat/logs/catalina.out            #查看日志 curl -I 127.0.0.1:8080                    #本机访问测试

#### 3.tomcat目录介绍

总目录

cd /opt/tomcat/ tree -L 1 ├── bin             #用以启动,关闭Tomcat或其他脚本功能的脚本(.bat和.sh) ├── conf            #用以配置Tomcat的XML及DTD文件 ├── lib             #存放web应用能访问的JAR包 ├── logs            #Catalina和其他web应用程序的日志文件 ├── temp            #临时文件 ├── webapps         #Web应用程序根目录 └── work            #用以产生有JSP编译出的Servlet的.java和.class文件

webapps目录 cd webapps/ ll 总用量 8 drwxr-x--- 14 root root 4096 8月  10 16:37 docs          #tomcat帮助文档 drwxr-x---  6 root root   78 8月  10 16:37 examples      #web应用 drwxr-x---  5 root root   82 8月  10 16:37 host-manager  #管理 drwxr-x---  5 root root   97 8月  10 16:37 manager       #管理 drwxr-x---  3 root root 4096 8月  10 16:37 ROOT          #默认网站根目录

bin目录 脚本                 作用 startup.sh           开启tomcat脚本 shutdown.sh          关闭tomcat脚本 catalina.sh          核心管理脚本,以后jvm优化参数及相关配置,修改tomcat启动参数

#### 4.启动和关闭tomcat

脚本方式： /opt/tomcat/bin/startup.sh /opt/tomcat/bin/shutdown.sh

###  5.添加tomcat系统服务

cat &gt;&gt; /opt/tomcat/bin/setenv.sh &lt;&lt; "END" # 设置tomcat pid CATALINA_PID="$CATALINA_BASE/tomcat.pid" # 设置java参数，提高性能 JAVA_OPTS="-server -XX:MetaspaceSize=256M -XX:MaxMetaspaceSize=1024m -Xms512M -Xmx1024M -XX:MaxNewSize=256m" END

#设置权限 chmod +x /opt/tomcat/bin/setenv.sh #创建tomcat用户和组 groupadd -r tomcat useradd -r -d /opt/tomcat -s /bin/nologin -g tomcat tomcat chown -R tomcat:tomcat /opt/tomcat

#配置systemctl管理tomcat cat &gt;&gt; /usr/lib/systemd/system/tomcat.service &lt;&lt; "END" [Unit] Description=Apache Tomcat 8 After=syslog.target network.target   [Service] Type=forking PIDFile=/opt/tomcat/tomcat.pid ExecStart=/opt/tomcat/bin/startup.sh ExecReload=/bin/kill -s HUP $MAINPID ExecStop=/bin/kill -s QUIT $MAINPID PrivateTmp=true User=tomcat Group=tomcat

[Install] WantedBy=multi-user.target END

启动tomcat： systemctl start tomcat

注：如果报错，启动不了： chmod -R 777 /opt/tomcat ############################################################################# 搭建jpress部署实践

#### 1.安装配置mariadb数据库

rpm -ivh http://repo.mysql.com/yum/mysql-5.6-community/el/7/x86_64/mysql-community-release-el7-5.noarch.rpm yum install mysql-community-server -y systemctl start mysqld systemctl enable mysqld mysqladmin -uroot -p password 123456

mysql -uroot -p123456 &gt; create database jpress default charset utf8; &gt;  flush privileges;

#### 2.上传jpress代码

mv jpress.war /opt/tomcat/webapps/

#### 3.web页面配置jpress

打开浏览器：http://192.168.8.129:8080/jpress/ 安装过程，数据库用户使用root

后台登陆页面:http://192.168.8.129:8080/jpress/admin

 ##############################################################

### tomcat多实例

###### 1.tomcat多实例介绍

其本质就是复制多个tomcat目录，然后修改为不同的端口并启动 代码一致，但是公用一个数据库

##### 2.复制目录

cd /opt/ cp -a apache-tomcat-8.5.66 tomcat1 cp -a apache-tomcat-8.5.66 tomcat2 删除tomcat1和tomcat2的webapps里的jpress rm -rf /opt/tomcat1/webapps/jpress* rm -rf /opt/tomcat2/webapps/jpress*

##### 3.修改配置文件

修改端口号 sed -i 's#8005#8006#g'  tomcat1/conf/server.xml sed -i 's#8009#8010#g'  tomcat1/conf/server.xml sed -i 's#8080#8081#g'  tomcat1/conf/server.xml sed -i 's#8005#8007#g'  tomcat2/conf/server.xml sed -i 's#8009#8011#g'  tomcat2/conf/server.xml sed -i 's#8080#8082#g'  tomcat2/conf/server.xml

##### 4.启动多实例

/opt/tomcat1/bin/startup.sh

/opt/tomcat2/bin/startup.sh

#####  5.查看服务是否启动

netstat -anput |grep java

##### 6.复制新的jpress到webapps

cp /data/soft/jpress.war  /opt/tomcat1/webapps/ cp /data/soft/jpress.war  /opt/tomcat1/webapps/

##### 7.mysql新建数据库，jpress1和jpress2

mysql -uroot -p123456 create database jpress1 default charset utf8; create database jpress2 default charset utf8;

##### 8.客户端访问8081、8082，安装jpress

##### 9.复制jpress文件内容到ROOT

cp -a  /opt/tomcat1/webapps/jpress/*   /opt/tomcat1/webapps/ROOT cp -a  /opt/tomcat1/webapps/jpress/*   /opt/tomcat1/webapps/ROOT

######################################################################################

### nginx反向代理(192.168.8.128)

##### 1.实验环境准备

a.多实例tomcat 8081 8082 b.数据库使用共有的db 192.168.8.129:3306 c.代码使用各自目录的jpress d.使用nginx反向代理到后端的2个端口

### 2.安装配置nginx

yum -y install epel-release yum -y install nginx

#### 3.创建代理配置文件

vim  /etc/nginx/conf.d/proxy.conf 添加： upstream java {<!-- -->     server 192.168.8.129:8081;     server 192.168.8.129:8082; } server {<!-- -->     listen       80;     server_name  www.jpress.com;     root   html;     index  index.html index.htm;     location / {<!-- -->         proxy_pass http://java;         proxy_set_header Host $http_host;         proxy_set_header X-Real-IP $remote_addr;         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;     } } 保存退出

#### 4.检查并启动nginx

nginx -t systemctl start nginx

##### 5.修改客户机192.168.8.128 hosts，域名访问

vim  /etc/hosts 192.168.8.128 www.jpress.com

打开浏览器：www.jpress.com

>  
 ♥️关注，就是我创作的动力 
 ♥️点赞，就是对我最大的认可 
 ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 

