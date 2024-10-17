
--- 
title:  Tomcat之多JAVA环境JVM版本查看及使用优先级 
tags: []
categories: [] 

---
## 一、前言

  业务系统包含PC端和移动端，移动端为微信小程序。在小程序客户端发送消息未得到回应，查询系统后台日志发现报错日志。JDK或者JRE中自带的“local_policy.jar ”和“US_export_policy.jar”是支持128位密钥的加密算法，而当我们要使用256位密钥算法的时候，已经超出它的范围，无法支持，所以才会报：“java.security.InvalidKeyException: Illegal key size or default parameters”的异常。根据百度查询处理博主替换了jdk中相关的两个jar包，重启系统，发现还是报这个错误。博主进一步排查发现原来博主部署方式是tomcat多实例部署，替换的也是该实例下的jar包，但是在操作系统层面也安装了jdk8版本，并且配置了jre环境变量，而tomcat运行时优先使用jre环境变量中的java版本，找不到JRE_HOME环境变量的情况下使用JAVA_HOME环境变量中的java版本。这就是这篇博文的由来因果。

## 二、解决微信小程序加解密报错

### 1、微信小程序后端报错

>  
 报错信息：Forwarding to error page from request [/wx/*******/callback/] due to exception [java.security.InvalidKeyException: Illegal key size] <img src="https://img-blog.csdnimg.cn/61b1a757d01a4626a37ede54dad9de52.png" alt="在这里插入图片描述"> 


### 2、检查JAVA环境变量

>  
 $ echo $JRE_HOME $ echo $JAVA_HOME <img src="https://img-blog.csdnimg.cn/b3e687b717064741ae46f0fb527b3eb5.png" alt="在这里插入图片描述"> 


### 3、检查java版本

>  
 $ java -version 


### 4、下载支持256位加解密算法的环境变量

  可以从官网或者CSDN下载支持256位加解密算法的两个jar包（local_policy.jar和US_export_policy.jar），CSDN下载链接：。

### 5、将下载jar包替换现有jar包

  将下载的jar包上传到服务器上，根据第二步查看的java环境变量情况，确定需要替换的目录，如果有JRE_HOME环境变量则优先替换JRE_HOME环境变量路径下的jar包，如果没有则替换JAVA_HOME环境变量路径下的jar包。

<img src="https://img-blog.csdnimg.cn/cb505431c64c4160ab1f14ca79a657e0.png" alt="在这里插入图片描述">

### 6、重启应用

  替换后重启系统服务，再次发起消息，查看系统后台日志不再报错，客户端也可以正常收到消息回复啦！

>  
 $ ./bin/shutdown.sh $ ./bin/startup.sh 


## 三、tomcat运行依赖java环境变量优先级实验

  博主实际运行环境比较特殊，为了验证tomcat对应java环境的使用优先级顺序，博主准备了两个java版本，并配置启用了manager服务。通过manager服务可以查看tomcat实例依赖的JVM环境java版本。

### 1、上传两个java版本到服务器

>  
 [root@s142 local]# ll |grep -E “java|jdk” lrwxrwxrwx. 1 root root 12 Apr 6 15:34 java -&gt; jdk1.8.0_291 lrwxrwxrwx. 1 root root 12 Apr 6 15:34 java241 -&gt; jdk1.8.0_241 drwxr-xr-x. 7 root root 245 Dec 11 2019 jdk1.8.0_241 drwxr-xr-x. 8 root root 273 Apr 8 2021 jdk1.8.0_291 -rw-r–r–. 1 root root 194545143 Mar 13 2020 jdk-8u241-linux-x64.tar.gz -rw-r–r–. 1 root root 144935989 Jun 16 2021 jdk-8u291-linux-x64.tar.gz 


### 2、配置java环境变量

  操作系统安装两个java版本，一个用于指定JAVA_HOME环境变量，一个用于配置JRE_HOME环境变量配置。我们在操作系统查看现在的java版本都是JAVA_HOME环境变量配置的版本。

>  
 [root@s142 local]# cat /etc/profile … #java env test export JAVA_HOME=/usr/local/java export JRE_HOME=/usr/local/java241/jre export PATH=${JAVA_HOME}/bin:$PATH … 


>  
 (base) [wuhs@s142 tomcat8]$ java -version java version “1.8.0_291” Java™ SE Runtime Environment (build 1.8.0_291-b10) Java HotSpot™ 64-Bit Server VM (build 25.291-b10, mixed mode) 


### 3、部署一个tomcat实例

  部署一个tomcat实例，如何部署manager见博文。

### 4、启动服务

>  
 (base) [wuhs@s142 tomcat8]$ java -version java version “1.8.0_291” Java™ SE Runtime Environment (build 1.8.0_291-b10) Java HotSpot™ 64-Bit Server VM (build 25.291-b10, mixed mode) (base) [wuhs@s142 tomcat8]$ ./bin/startup.sh 


### 5、查看JVM版本

  启动tomcat实例，我们可以看到tomcat实例运行在JRE_HOME环境变量的java版本上。 <img src="https://img-blog.csdnimg.cn/9037900a89014a3bac3097a8963d93ec.png" alt="在这里插入图片描述">

### 6、修改环境变量

  我们修改环境变量配置，取消JRE_HOME环境变量配置。 [root@s142 local]# cat /etc/profile …

>  
 #java env test export JAVA_HOME=/usr/local/java #export JRE_HOME=/usr/local/java241/jre export PATH=${JAVA_HOME}/bin:$PATH [root@s142 local]# java -version java version “1.8.0_291” Java™ SE Runtime Environment (build 1.8.0_291-b10) Java HotSpot™ 64-Bit Server VM (build 25.291-b10, mixed mode) 


### 7、重启服务

>  
 (base) [wuhs@s142 tomcat8]$ ./bin/shutdown.sh (base) [wuhs@s142 tomcat8]$ ./bin/startup.sh 


### 8、再次查看JVM版本

  此时可以看到JVM版本是JAVA_HOME配置指定的版本。 <img src="https://img-blog.csdnimg.cn/af9a5531dfcc486ab7a4e2044fef770a.png" alt="在这里插入图片描述">

### 9、启动日志查看

  实际上，在单实例运行中，我们可以看到启动日志已经将环境变量设置显示了出来，不管如何配置tomcat内部使用的都是JRE_HOME这个配置，只是在找不到操作系统JRE_HOME配置的时候，JRE_HOME配置就会取JAVA_HOME的值赋值给JRE_HOME。

>  
 (base) [wuhs@s142 tomcat8]$ ./bin/startup.sh Using CATALINA_BASE: /home/wuhs/tomcat8 Using CATALINA_HOME: /home/wuhs/tomcat8 Using CATALINA_TMPDIR: /home/wuhs/tomcat8/temp Using JRE_HOME: /usr/local/java Using CLASSPATH: /home/wuhs/tomcat8/bin/bootstrap.jar:/home/wuhs/tomcat8/bin/tomcat-juli.jar Using CATALINA_OPTS: Tomcat started. 


### 10、总结

  实际上Tomcat实例运行时依赖的java环境是取值于JRE_HOME，如果找不到则使用JAVA_HOME赋值给JRE_HOME。如果是多实例环境运行，为了减少系统可能的多java版本带来的影响，建议使用JRE_HOME定义java环境。
