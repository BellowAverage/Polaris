
--- 
title:  Tomcat环境搭建及相关优化 
tags: []
categories: [] 

---
## Tomcat环境搭建及相关优化



#### 文章目录
- - <ul><li>- - - - <ul><li>- 


### 前言：

自 2017 年 11 月编程语言排行榜 Java 占比 13%，高居榜首，Tomcat 也一度成为 Java 开发人员的首选。其开源、占用系统资源少、跨平台等特性被深受喜爱。

### 1、Tomcat简介：

Tomcat 服务器是一个免费的开放源代码的Web 应用服务器，属于轻量级应用服务器， 在中小型系统和并发访问用户不是很多的场合下被普遍使用，是开发和调试JSP 程序的首选。 Tomcat和IIS等Web服务器一样，具有处理HTML页面的功能，另外它还是一个Servlet和JSP容器，独立的Servlet容器是Tomcat的默认模式。 Tomcat处理静态HTML的能力不如Apache服务器，但动态处理能力是非常优秀的。

Tomcat核心组件：
1. Web 容器：完成 Web 服务器的功能。1. Servlet 容器：名字为 catalina，用于处理 Servlet 代码。1. JSP 容器：用于将 JSP 动态网页翻译成 Servlet 代码。
### 2、实际操作安装tomcat

```
#安装JDK包
[root@localhost ~]#rpm -ivh jdk-8u201-linux-x64.rp
[root@localhost ~]#cd /usr/java/jdk1.8.0_201-amd64/
[root@localhost jdk1.8.0_201-amd64]#vim /etc/profile
#添加环境变量
export JAVA_HOME=/usr/java/jdk1.8.0_201-amd64
export CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
export PATH=$JAVA_HOME/bin:$PATH
[root@localhost jdk1.8.0_201-amd64]#source /etc/profile
#刷新配置文件
[root@localhost tomcat]#tar zxf apache-tomcat-9.0.16.tar.gz 
[root@localhost tomcat]#cp -r apache-tomcat-9.0.16 /usr/local/tomcat
[root@localhost tomcat]#cd /usr/local/tomcat/
[root@localhost tomcat]#/usr/local/tomcat/bin/startup.sh
#启动tomcat
Using CATALINA_BASE:   /usr/local/tomcat
Using CATALINA_HOME:   /usr/local/tomcat
Using CATALINA_TMPDIR: /usr/local/tomcat/temp
Using JRE_HOME:        /usr/java/jdk1.8.0_201-amd64
Using CLASSPATH:       /usr/local/tomcat/bin/bootstrap.jar:/usr/local/tomcat/bin/tomcat-juli.jar
Tomcat started.
[root@localhost ~]# /usr/local/tomcat/bin/shutdown.sh 
#关闭服务
添加到
[root@localhost bin]#useradd -s /sbin/nologin tomcat
#新建用户
[root@localhost local]#chown tomcat:tomcat tomcat/ -R
#修改属主和属组

[root@localhost ~]#vim /etc/systemd/system/tomcat.service
#编写tomcat.service文件
[Unit]
Description=Tomcat
#After=syslog.target network.target remote-fs.target nss-lookup.target
After=syslog.target network.target

[Service]
Type=forking
ExecStart=/usr/local/tomcat/bin/startup.sh
ExecStop=/usr/local/tomcat/bin/shutdown.sh
RestartSec=3
PrivateTmp=true
User=tomcat
Group=tomcat

[Install]
WantedBy=multi-user.target
                                       
[root@localhost local]#systemctl daemon-reload
[root@localhost local]#systemctl start tomcat
[root@localhost local]#ss -ntap |grep 8080

```

### 3、配置文件介绍及核心组件

#### 3.1、配置文件

**安装目录下 文件介绍**

|目录名字|功能
|------
|bin|存放启动和关闭 Tomcat 的脚本文件，比较常用的是 catalina.sh、startup.sh、shutdown.sh 三个文件
|conf|存放 Tomcat 服务器的各种配置文件，比较常用的是 server.xml、context.xml、tomcat-users.xml、web.xml 四个文件。
|lib|存放 Tomcat 服务器的 jar 包，一般不作任何改动，除非连接第三方服务，比如 redis，那就需要添加相对应的 jar 包
|logs|存放 Tomcat 日志
|temp|存放 Tomcat 运行时产生的文件
|webapps|存放项目资源的目录
|work|Tomcat 工作目录，一般清除 Tomcat 缓存的时候会使用到

**conf子目录**

|文件名|说明
|------
|server.xml|主配置文件
|web.xml|每个webapp只有“部署"后才能被访问,它的部署方式通常由web.xml进行定义,其存放位置为WEB-INF/目录中;此文件为所有的webapps提供默认部署相关的配置,每个web应用也可以使用专用配置文件,来覆盖全局文件
|context.xml|用于定义所有web应用均需加载的Context配置,此文件为所有的webapps提供默认配置,每个web应用也可以使用自已专用的配置,它通常由专用的配置文件context.xml来定义,其存放位置为WEB-INF/目录中,覆盖全局的文件
|tomcat-users.xml|用户认证的账号和密码文件
|catalina.policy|当使用security选项启动omcat时,用于为tomcat设置安全策略
|catalina.properties|Tomcat环境变量的配置,用于设定类加载器路径，以及一些与JVM调优相关参数
|logging.properties|Tomcat日志系统相关的配置，可以修改日志级别和日志路径等

<font color="red">注意配置文件对于大小写敏感</font>。

#### 3.2核心组件

|名称|说明
|------
|server|服务器，Tomcat运行的进程实例，一个Server中可以有多个service，但通常就一个
|service|服务，用来组织Engine和Connector的对应关系，一个service中只有一个Engine
|connector|连接器，负责客户端的HTTP、HTTPS、AJP等协议连接。一个Connector只属于某一个Engine
|Engine|即引擎，用来响应并处理用户请求。一个Engine上可以绑定多个Connector
|Host|即虚拟主机,可以实现多虚拟主机,例如使用不同的主机头区分
|Context|应用的上下文，配置特定url路径映射和目录的映射关系: url =&gt; directory

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;Server port="8005" shutdown="SHUTDOWN"&gt;
   &lt;Service name="Catalina"&gt;
     &lt;Connector port="8080" protocol="HTTP/1.1"connectionTimeout="20000"
               redirectPort="8443" /&gt;
       &lt;Connector port="8009" protocol="AJP/1.3" redirectPort="8443" /&gt;
          &lt;Engine name="Catalina" defaultHost="localhost"&gt;
             &lt;Host name="localhost"  appBase="webapps"unpackWARs="true" autoDeploy="true"&gt;
           &lt;Context &gt;
                &lt;Context /&gt;
 &lt;/Host&gt;
    &lt;/Engine&gt;
  &lt;/Service&gt;
&lt;/Server&gt;


```

**tomcat 处理请求过程：**

请求来自于 http://locahost:8080/test/index.html
- Tomcat启动一个Server进程。可以启动多个Server，即tomcat的多实例,但一般只启动一个- 创建一个Service提供服务。可以创建多个Service，但一般也只创建一个- 每个Service中，是Engine和其连接器Connector的关联配置- 可以为这个Service提供多个连接器Connector，这些Connector使用了不同的协议，绑定了不同的端口。其作用就是处理来自客户端的不同的连接请求或响应- Service 内部还定义了Engine，引擎才是真正的处理请求的入口，其内部定义多个虚拟主机Host- Engine对请求头做了分析，将请求发送给相应的虚拟主机- 如果没有匹配，数据就发往Engine上的defaultHost缺省虚拟主机- Engine上的缺省虚拟主机可以修改- Host定义虚拟主机，虚拟主机有name名称，通过名称匹配- Context定义应用程序单独的路径映射和配置<li>
通常意义上的 Web 服务器接受请求后，只是单纯地响应静态资源，如 HTML 文件，图片 文件等，不能在后端进行一定的处理操作。 Tomcat 是 Apache 下的一个子项目，它具备 Web 服务器的所有功能，不仅可以监听接受请求并响应静态资源，而且可以在后端运行特定规范 的 Java 代码 Servlet，同时将执行的结果以 HTML 代码的形式反回客户端。

```
 Tomcat 由一系列的组件构成，其中核心的组件有三个：
1）Web 容器：完成 Web 服务器的功能。（https请求）
2）Servlet 容器：名字为 catalina，用于处理 Servlet 代码。(具体的任务)
3）JSP 容器：用于将 JSP 动态网页翻译成 Servlet 代码。

① Web容器
   负责底层的HTTP协议
② Servlet容器
  由catalina脚本帮忙处理的servlet代码，主要处理后端逻辑业务
  catalina实际处理的是Servlet代码，而Servlet代码是由Java编写的
③ JSP容器（JAVA Scripts page）
JSP：在正常的html标签中嵌入一些java代码
这些JSP最终会被翻译成Servlet代码被执行
主要提供提供前端页面展示&lt;% %&gt;

```

​ 小结：tomcat就是一个容器，在这个容器中有三大核心组件： ​ WEB、Servlet 和JSP，所以Tomcat是极其轻量级别的，核心组件都是支持基本运行的组件。

**磁盘文件 和访问的url对应关系**

```
apache：
/var/www/html/index.html  -----&gt;   http://www.kgc.com/index.html
/var/www/html/test/index.html  -----&gt;   http://www.kgc.com/test/index.html

tomcat:
/usr/local/tomcat/webapps     

/usr/local/tomcat/webapps/ROOT/index.jsp  -----&gt; http://www.kgc.com/index.jsp
/usr/local/tomcat/webapps/test/index.jsp  -----&gt; http://www.kgc.com/test/index.jsp


http://192.168.91.103:8080/docs/


[root@localhost webapps]# cd /usr/local/tomcat/webapps
[root@localhost webapps]#mkdir blog
[root@localhost webapps]#vim blog/index.html
/usr/local/tomcat/webapps/blog/index.html

http://192.168.91.103:8080/blog/

```

**主页文件的优先级**
- index.html- index.htm- index.jsp
```
[root@localhost conf]#vim /usr/local/tomcat/conf/web.xml
&lt;welcome-file-list&gt;
        &lt;welcome-file&gt;index.html&lt;/welcome-file&gt;
        &lt;welcome-file&gt;index.htm&lt;/welcome-file&gt;
        &lt;welcome-file&gt;index.jsp&lt;/welcome-file&gt;
    &lt;/welcome-file-list&gt;



[root@localhost blog]#chown tomcat:tomcat WEB-INF/ -R


```

**打包jar包实际操作**

jar包，war包

```
[root@localhost conf]#cd /data/
[root@localhost data]#ls
[root@localhost data]#mkdir app1
[root@localhost data]#cd app1/
[root@localhost app1]#ls
[root@localhost app1]#vim test.html
&lt;h1&gt; test &lt;/h1&gt;
[root@localhost app1]#vim test.jsp
&lt;%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8"%&gt;
&lt;! DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
	&lt;meta charset="utf-8"&gt;
	&lt;title&gt;jsp例子&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
后面的内容是服务器端动态生成字符串，最后拼接在一起
&lt;%
out.println ("test jsp");
%&gt;
%&lt;br&gt;
&lt;%=request.getRequestURL()%&gt;
&lt;/body&gt;
&lt;/html&gt;
[root@localhost app1]#jar cvf /opt/app1.war *
#打包
[root@localhost opt]#cp app1.war /usr/local/tomcat/webapps/
[root@localhost opt]#ll /usr/local/tomcat/webapps/

http://192.168.91.103:8080/app1/test.jsp
http://192.168.91.103:8080/app1/test.html
#####下线只要删除war包直接自动删除

[root@localhost opt]#cd /opt
[root@localhost opt]#mv app1.war app1.war.zip
[root@localhost opt]#unzip app1.war.zip 
Archive:  app1.war.zip
   creating: META-INF/
  inflating: META-INF/MANIFEST.MF    
  inflating: test.html               
  inflating: test.jsp                
[root@localhost opt]#ls
apache-tomcat-9.0.16.tar.gz  META-INF      nginx-1.12.0.tar.gz  test.html
app1.war.zip                 nginx-1.12.0  rh                   test.jsp

```

```
[root@localhost webapps]#ln -s /usr/local/tomcat/webapps/jpress-v4.1.4 jpress
[root@localhost ~]# wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
[root@localhost ~]# yum -y install mysql57-community-release-el7-10.noarch.rpm
[root@localhost ~]# yum -y install mysql-community-server
[root@localhost ~]# systemctl start  mysqld.service

mysql&gt; CREATE DATABASE bbs;  //创建一个数据库//

mysql&gt; GRANT all ON bbs.* TO 'bbsuser'@'%' IDENTIFIED BY 'admin123';   //把bbs数据库里面所有表的权限授予给bbsuser,并设置密码//

mysql&gt;flush privileges; //刷新数据库//


```

### 4.虚拟主机配置

可能有时候公司会有多个项目需要运行，那么肯定不可能是一台服务器上运行多个 Tomcat 服务，这样会消耗太多的系统资源。此时，就需要使用到 Tomcat 虚拟主机。例如现在新增两个域名 www.kgc.com，www.accp.com希望通过这两个域名访问到不同的项目内容。

```
[root@localhost webapps]#mkdir kgc accp
[root@localhost webapps]#echo "this is kgc web !" &gt; kgc/index.jsp
[root@localhost webapps]#echo "this is accp web !" &gt; accp/index.jsp
[root@localhost webapps]#cat accp/index.jsp kgc/index.jsp 
this is accp web ls
this is kgc web ls

#http://tomcat.apache.org/tomcat-8.5-doc/index.html
#配置文件的详解
[root@localhost ~]# vim /usr/local/tomcat/conf/server.xml 
&lt;Host name="www.kgc.com" appBase="/usr/local/tomcat/webapps"
            unpackWARs="true" autoDeploy="true" xmlValidation="false"
            xmlNamespaceAware="false"&gt;
                &lt;Context docBase="/usr/local/tomcat/webapps/kgc"
                path="" reloadable="true" /&gt;
      &lt;/Host&gt;

      &lt;Host name="www.accp.com" appBase="/usr/local/tomcat/webapps"
            unpackWARs="true" autoDeploy="true" xmlValidation="false"
            xmlNamespaceAware="false"&gt;
                &lt;Context docBase="/usr/local/tomcat/webapps/accp"
                path="" reloadable="true" /&gt;
      &lt;/Host&gt;
      
[root@localhost ~]#systemctl restart tomcat

##更改hosts文件##  C:\Windows\System32\drivers\etc  改hosts文件
192.168.91.103	www.kgc.com	www.accp.com

http://www.kgc.com:8080/kgc/
http://www.kgc.com:8080/accp/

```

### 5Tomcat 配置文件参数优化

关于 Tomcat 主配置文件 server.xml 里面很多默认的配置项，但并不能满足业务需求， 常用的优化相关参数如下

【maxThreads】Tomcat 使用线程来处理接收的每个请求，这个值表示 Tomcat 可创建的最 大的线程数，默认值是 200。

【minSpareThreads】最小空闲线程数，Tomcat 启动时的初始化的线程数，表示即使没有 人使用也开这么多空线程等待，默认值是 10

【maxSpareThreads】最大备用线程数，一旦创建的线程超过这个值，Tomcat 就会关闭不 再需要的 socket 线程。默认值是-1（无限制）。一般不需要指定

【URIEncoding】指定 Tomcat 容器的 URL 编码格式，语言编码格式这块倒不如其它 Web 服务器软件配置方便，需要分别指定utf-8

【connnectionTimeout】网络连接超时，单位：毫秒，设置为 0 表示永不超时，这样设置 有隐患的。通常默认 20000 毫秒（20秒）就可以

【enableLookups】是否反查域名，以返回远程主机的主机名，取值为：true 或 false， 如果设置为 false，则直接返回 IP 地址，为了提高处理能力，应设置为 false。

【disableUploadTimeout】上传时是否使用超时机制。应设置为 true。

【connectionUploadTimeout】上传超时时间，毕竟文件上传可能需要消耗更多的时间， 这个根据你自己的业务需要自己调，以使 Servlet 有较长的时间来完成它的执行，需要 与上一个参数一起配合使用才会生效

【acceptCount】指定当所有可以使用的处理请求的线程数都被使用时，可传入连接请求 的最大队列长度，超过这个数的请求将不予处理，默认为 100 个。

【compression】是否对响应的数据进行 GZIP 压缩，off：表示禁止压缩；on：表示允许 压缩（文本将被压缩）、force：表示所有情况下都进行压缩，默认值为 off，压缩数据 后可以有效的减少页面的大小，一般可以减小 1/3 左右，节省带宽。

【compressionMinSize】表示压缩响应的最小值，只有当响应报文大小大于这个值的时候 才会对报文进行压缩，如果开启了压缩功能，默认值就是 2048

【compressableMimeType】压缩类型，指定对哪些类型的文件进行数据压缩。

【noCompressionUserAgents=“gozilla, traviata”】对于以下的浏览器，不启用压缩

如果已经对代码进行了动静分离，静态页面和图片等数据就不需要 Tomcat 处理了，那 么也就不需要在 Tomcat 中配置压缩了。因为这里只有一台 Tomcat 服务器，而且压测的是 Tomcat 首页，会有图片和静态资源文件，所以这里启用压缩。

以上是一些常用的配置参数，还有好多其它的参数设置，还可以继续深入的优化，HTTP Connector 与 AJP Connector 的参数属性值，可以参考官方文档的详细说明进行学习。链 接 地 址 http://tomcat.apache.org/tomcat-9.0-doc/config/http.html ， 下 面 开 始 对 Tomcat 配置文件优化进行前后的对比

```
&lt;Connector port="8080" protocol="HTTP/11.1" 
connectionTimeout="20000" 
redirectPort="8443" 
minSpareThreads="50" 
enableLookups="false" 
disableUploadTimeout="true" 
acceptCount="300" 
maxThreads="500" 
processorCache="500"
URIEncoding="UTF-8" 
compression="on" 
compressionMinSize="2048" 
compressableMimeType="text/html,text/xml,text/javascript,text/css,text/plain,image/gif,image /jpg,image/png"/&gt;

```
