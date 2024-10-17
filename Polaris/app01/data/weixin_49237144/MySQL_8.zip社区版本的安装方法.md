
--- 
title:  MySQL_8.zip社区版本的安装方法 
tags: []
categories: [] 

---
#### 1.MySQL官网下载zip包，解压zip包。

Hello小伙伴们，你们好，又是日常get新技能的一天，0基础入门，趁着热乎，快上车啦 ~~。 今天，咱们来整一下如何安装MySQL_8.zip社区版本~。 MySQL官网：

>  
  


<img src="https://img-blog.csdnimg.cn/6d0b66c181ef40a4885ca288f0046f1b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">  <img src="https://img-blog.csdnimg.cn/f2b42f5578cd4a29a68ce01b966733d2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

解压下载好的文件后目录如下图

<img src="https://img-blog.csdnimg.cn/216ea7dd7b2e4a64b1f2a1ce2630a84b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 

#### 2.创建并配置my.ini文件（放在bin同级目录）

basedir=文件解压后的路径 （重点）

```
[mysqld]
##设置3306端口
port=3306
##设置mysql的安装目录
basedir=D:\mysql-8.0.21-winx64\
##设置mysql数据库的数据的存放目录
datadir=D:\mysql-8.0.21-winx64\Data
##允许最大连接数
max_connections=200
##允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统
max_connect_errors=10
##服务端使用的字符集默认为UTF8
character-set-server=utf8
##创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
##默认使用“mysql_native_password”插件认证
default_authentication_plugin=mysql_native_password
[mysql]
##设置mysql客户端默认字符集
default-character-set=utf8
[client]
##设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8

```

##### 2.1 配置环境变量path（方便cmd操作数据库）

路径：“计算机”–》“属性”–》“高级系统设置”–》“高级”–》“环境变量”–》“系统变量”–》“path”

变量名：path

变量值：;D:\mysql-8.0.21-winx64;（自己的mysql的安装目录win7用;分隔，win10则不用）

#### 3.初始化mysql服务。

​ **以管理员身份**进入**cmd**：mysqld --initialize --console 一定要记住初始化密码！！！！（重点！重点！重点！） <img src="https://img-blog.csdnimg.cn/1529293b5d1d4e7d80b97e7d2b883261.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

#### 4.安装与启动mysql服务。

​ 安装mysql服务：mysqld --install ​ 启动mysql服务：net start mysql <img src="https://img-blog.csdnimg.cn/36f47273933c4ba98350ae9bd8170c5a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

#### 5.修改初始化的密码。

登录MySQL（密码是初始化的密码）

```
mysql&gt;mysql -uroot -p

```

修改初始化的密码

```
​mysql&gt;alter user root@localhost identified by '123456';

```

<img src="https://img-blog.csdnimg.cn/f35ff9765fc94e82b4d7bbca3fc32e12.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5aOs5p2w,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 6.导入别人数据库

​ – 复制数据库, ​ – 前提是先创建一个跟数据库名.sql文件里面一致的数据库名 ​ – 在 mysql&gt; create database 数据库名; ​ – 在 mysql&gt; use 数据库名; ​ – 在 mysql&gt; source .sql文件路径（一定不能有中文）

##### 注意：mysql_8 不用自己创建data文件，否则很有可能安装失败

##### 有区别与mysql5.6的版本需要自己创建data文件.
