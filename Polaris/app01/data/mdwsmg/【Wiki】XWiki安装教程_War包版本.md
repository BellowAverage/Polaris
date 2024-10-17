
--- 
title:  【Wiki】XWiki安装教程_War包版本 
tags: []
categories: [] 

---


#### 目录
- - - <ul><li>- - - - - - - - <ul><li>- 


## 0、XWiki说明

XWiki为主题使用java开发的开源wiki，官网地址如下： 

>  
 提供Docker安装，本篇为Linux环境下war包形式安装。所有内容、说明均可在官网找到。 


## 1、war包安装说明

### 1.1、环境说明

截止2023年1月10日，xwiki长期支持版本为14.10.2 <img src="https://img-blog.csdnimg.cn/f9deda95a2ea42e59169bcac12f19c29.png" alt="在这里插入图片描述">
- 环境需求、物料包如下
|需求环境|说明
|------
|Java|版本14.10.2需要java11+ （ ）
|tomcat|官方推荐tomcat9.0.69（不推荐9.0.70与tomcat10，官方说会有问题，没测。jetty之类的servlet容器都可以）
|PostgreSQL|PostgreSQL依据java版本来就好，需要准备好jar包。也可以使用Mysql、HSQLDB、MariaDB、H2等数据库
|xwiki本体|下载对应war包与xip包

### 1.2、如果懒得下载可以使用这边准备好的物料包汇总

链接：https://pan.baidu.com/s/1Vaju923bCoUbN7sA8UOLrg 提取码：moyu

## 2、war包安装

### 2.1、Tomcat安装

解压tomcat包到任意位置

```
tar -zxvf

```

使用pwd获取路径（cd进去有bin目录的路径，比如/home/lihua/tomcat/bin，那就取/home/lihua/tomcat,后面java同理），并记住，等下写/etc/profile要用

### 2.2、java安装(需要root权限)

解压java到任意位置

```
tar -zxvf

```

使用pwd获取路径后填充到 /etc/profile文件

```
export CATALINA_HOME=前面的tomcat安装路径
export JAVA_HOME=你的java解压路径
export PATH=$PATH:${JAVA_HOME}/bin:${CATALINA_HOME}/bin
export CLASSPATH=$CLASSPATH:${JAVA_HOME}/lib:${CATALINA_HOME}/lib

```

### 2.3 、使用 source /etc/profile 刷新linux配置

```
source /etc/profile

```

刷新配置后，使用 java -version查看java版本，如果没有显示，请重新连接linux会话

### 2.4、数据库安装

略

### 2.5、解压war包与xip

**创建tomcat下应用目录与其他任意位置的持久化目录**,创建持久化目录后在持久化目录下创建 extension/repository

```
mkdir  tomcat/webapps/xwiki 
mkdir -p 你的持久化路径/extension/repository

```

使用mv 命令修改 .xip 为 .zip,并解压

```
mv xwiki-platform-distribution-flavor-xip-14.10.2.xip xwiki-platform-distribution-flavor-xip-14.10.2.zip
unzip xwiki-platform-distribution-flavor-xip-14.10.2.zip -d 你的持久化路径/extension/repository

```

解压war包到xwiki目录下

```
unzip xwiki-platform-distribution-war-14.10.2.war -d 你的tomcat路径/webapps/xwiki

```

### 2.6、修改配置文件

#### 2.6.1、修改WEB-INF/hibernate.cfg.xml

注释掉100行开始的default database，关键词搜索找到数据库配置位置，放开postgresql注释，配置如下

```
	&lt;property name="hibernate.connection.url"&gt;jdbc:postgresql://127.0.0.1:5432/xwiki&lt;/property&gt;
    &lt;property name="hibernate.connection.username"&gt;xwiki&lt;/property&gt;
    &lt;property name="hibernate.connection.password"&gt;xwiki&lt;/property&gt;
    &lt;property name="hibernate.connection.driver_class"&gt;org.postgresql.Driver&lt;/property&gt;
    &lt;property name="hibernate.jdbc.use_streams_for_binary"&gt;false&lt;/property&gt;
    &lt;property name="xwiki.virtual_mode"&gt;schema&lt;/property&gt;

    &lt;property name="hibernate.connection.charSet"&gt;UTF-8&lt;/property&gt;
    &lt;property name="hibernate.connection.useUnicode"&gt;true&lt;/property&gt;
    &lt;property name="hibernate.connection.characterEncoding"&gt;utf8&lt;/property&gt;

    &lt;mapping resource="xwiki.postgresql.hbm.xml"/&gt;
    &lt;mapping resource="feeds.hbm.xml"/&gt;
    &lt;mapping resource="instance.hbm.xml"/&gt;
    &lt;mapping resource="notification-filter-preferences.hbm.xml"/&gt;
    &lt;mapping resource="mailsender.hbm.xml"/&gt;

```

#### 2.6.1、修改xwiki.properties

设置持久化目录位置,增加下列行

```
environment.permanentDirectory=你的持久化路径

```

如果创建目录和启动应用的用户权限不一致，记得赋权

```
chown -R  低权限用户名:低权限用户名 /data/local/xwiki

```

### 2.7、启动tomcat

```
sh /tomcat/bin/startup.sh

```

### 2.8、打开xwiki

在浏览器输入 http://服务器Ip:8080/xwiki 即可打开，比较慢，可能要等一分钟，然后开始xwiki初始化
