
--- 
title:  二、mysql进程之间关系、配置文件、文件socket、网络socket、mysql密码破解 
tags: []
categories: [] 

---
**目录**































1.  mysql的进程关系

### 1.1  查看进程之间的关系

**mysql 官方文档： **

使用 **pstree -p** 来查看进程树

<img alt="" height="653" src="https://img-blog.csdnimg.cn/44c264fd25bb4e7f9dc96dd8cb2d95be.png" width="1156">

 <img alt="" height="176" src="https://img-blog.csdnimg.cn/4923fc45bf5f4bf7b8e6ef6a7d693a45.png" width="1200">



** 父子进程，mysqld_safe进程管理mysqld进程**

**mysqld进程是工作进程**

**###############################################**

## 2. mysql配置文件

因为我们在刚才的一键安装脚本里面指定了mysql的配置文件以及内容，所以配置文件的路径应该是**/etc/my.conf**

<img alt="" height="416" src="https://img-blog.csdnimg.cn/4e92c6f624bb4d1485f5bfb740e7bc97.png" width="583">

**###############################################** 

###  2.1 配置文件的含义

```
[mysqld_safe]

[client]
socket=/data/mysql/mysql.sock

[mysqld]
socket=/data/mysql/mysql.sock
port = 3306
open_files_limit = 8192
innodb_buffer_pool_size = 512M
character-set-server=utf8

[mysql] 
auto-rehash  
prompt=\u@\d \R:\m  mysql&gt;  

```

**[client]** : 给其他客服端传参，mysql命令就属于一个客户端的命令，告诉** [mysql] **客户端

本机的mysql登录会自动到配置文件的client来找socket文件的路径，这样就不用我们指定了。

**mysql.sock**文件的路径在哪里

**port **: 端口号

**open_files_limit ** : 打开文件数限制

**innodb_buffer_pool_size** ：缓存池大小

**prompt=\u@\d \R:\m mysql&gt; :**

**               \u : 用户     \d：当前正在使用的数据库   \R:\m  :当前时间   **



**配置文件就是给mysql进程传递参数的。**

<img alt="" height="642" src="https://img-blog.csdnimg.cn/953929e0ec8b4c0e8df75cda2d52713f.png" width="1016">



socket是进程和进程之间的一种通信方式，mysqld进程打开了一个socket文件在/data/mysql/mysql.sock路径下面，mysql想连过来，就会加载client的配置，因为mysql属于一个客户端的命令，就会加载这段配置，这样mysql就知道mysqld进程的socket文件在哪里，两个进程就通过socket连接起来了。



**  查看mysql里面的变量：**

**root@(none) 22:08  mysql&gt;show variables \G**

```
root@(none) 22:08  mysql&gt;show variables \G
*************************** 515. row ***************************
Variable_name: version_comment
        Value: MySQL Community Server (GPL)
*************************** 516. row ***************************
Variable_name: version_compile_machine
        Value: x86_64
*************************** 517. row ***************************
Variable_name: version_compile_os
        Value: linux-glibc2.12
*************************** 518. row ***************************
Variable_name: wait_timeout
        Value: 28800
*************************** 519. row ***************************


```

**查看mysql里支持哪些字符集：**

**root@mysql 22:14  mysql&gt;show character set;**

```
root@mysql 22:14  mysql&gt;show character set;
+----------+---------------------------------+---------------------+--------+
| Charset  | Description                     | Default collation   | Maxlen |
+----------+---------------------------------+---------------------+--------+
| big5     | Big5 Traditional Chinese        | big5_chinese_ci     |      2 |
| dec8     | DEC West European               | dec8_swedish_ci     |      1 |
| cp850    | DOS West European               | cp850_general_ci    |      1 |
| hp8      | HP West European                | hp8_english_ci      |      1 |
| koi8r    | KOI8-R Relcom Russian           | koi8r_general_ci    |      1 |
| latin1   | cp1252 West European            | latin1_swedish_ci   |      1 |
| latin2   | ISO 8859-2 Central European     | latin2_general_ci   |      1 |
| swe7     | 7bit Swedish                    | swe7_swedish_ci     |      1 |
| ascii    | US ASCII                        | ascii_general_ci    |      1 |
| ujis     | EUC-JP Japanese                 | ujis_japanese_ci    |      3 |
| sjis     | Shift-JIS Japanese              | sjis_japanese_ci    |      2 |
| hebrew   | ISO 8859-8 Hebrew               | hebrew_general_ci   |      1 |
| tis620   | TIS620 Thai                     | tis620_thai_ci      |      1 |
| euckr    | EUC-KR Korean                   | euckr_korean_ci     |      2 |
| koi8u    | KOI8-U Ukrainian                | koi8u_general_ci    |      1 |
| gb2312   | GB2312 Simplified Chinese       | gb2312_chinese_ci   |      2 |
| greek    | ISO 8859-7 Greek                | greek_general_ci    |      1 |
| cp1250   | Windows Central European        | cp1250_general_ci   |      1 |
| gbk      | GBK Simplified Chinese          | gbk_chinese_ci      |      2 |
| latin5   | ISO 8859-9 Turkish              | latin5_turkish_ci   |      1 |
| armscii8 | ARMSCII-8 Armenian              | armscii8_general_ci |      1 |
| utf8     | UTF-8 Unicode                   | utf8_general_ci     |      3 |
| ucs2     | UCS-2 Unicode                   | ucs2_general_ci     |      2 |
| cp866    | DOS Russian                     | cp866_general_ci    |      1 |
| keybcs2  | DOS Kamenicky Czech-Slovak      | keybcs2_general_ci  |      1 |
| macce    | Mac Central European            | macce_general_ci    |      1 |
| macroman | Mac West European               | macroman_general_ci |      1 |
| cp852    | DOS Central European            | cp852_general_ci    |      1 |
| latin7   | ISO 8859-13 Baltic              | latin7_general_ci   |      1 |
| utf8mb4  | UTF-8 Unicode                   | utf8mb4_general_ci  |      4 |
| cp1251   | Windows Cyrillic                | cp1251_general_ci   |      1 |
| utf16    | UTF-16 Unicode                  | utf16_general_ci    |      4 |
| utf16le  | UTF-16LE Unicode                | utf16le_general_ci  |      4 |
| cp1256   | Windows Arabic                  | cp1256_general_ci   |      1 |
| cp1257   | Windows Baltic                  | cp1257_general_ci   |      1 |
| utf32    | UTF-32 Unicode                  | utf32_general_ci    |      4 |
| binary   | Binary pseudo charset           | binary              |      1 |
| geostd8  | GEOSTD8 Georgian                | geostd8_general_ci  |      1 |
| cp932    | SJIS for Windows Japanese       | cp932_japanese_ci   |      2 |
| eucjpms  | UJIS for Windows Japanese       | eucjpms_japanese_ci |      3 |
| gb18030  | China National Standard GB18030 | gb18030_chinese_ci  |      4 |
+----------+---------------------------------+---------------------+--------+
41 rows in set (0.00 sec)

```

 

**查看mysql有哪些用户登录**

root@mysql 22:14  mysql&gt;show processlist;

```
root@mysql 22:14  mysql&gt;show processlist;
+----+--------+--------------------+---------+---------+------+----------+------------------+
| Id | User   | Host               | db      | Command | Time | State    | Info             |
+----+--------+--------------------+---------+---------+------+----------+------------------+
|  5 | root   | localhost          | mysql   | Query   |    0 | starting | show processlist |
|  9 | liming | 192.168.44.1:51433 | student | Sleep   |   24 |          | NULL             |
| 10 | liming | 192.168.44.1:51434 | NULL    | Sleep   |  150 |          | NULL             |
+----+--------+--------------------+---------+---------+------+----------+------------------+
3 rows in set (0.00 sec)

```

 

**###############################################**

#### 2.1.1  socket是什么？

socket是进程与进程之间一种通信方式

socket分文件socket和网络socket两种

**文件socket**：

        是实现一台电脑里的不同进程之间通信的文件

```
[root@localhost ~]# mysql -u root -p'Sanchuang123#' -S /data/mysql/mysql.sock
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.34 MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

root@(none) 22:30  mysql&gt;

```

在my.cnf配置文件里打开下面的配置，在使用mysql客户端命令连接的时候，就不需要接-S指定socket文件的路径了。

```
[client]
socket=/data/mysql/mysql.sock

```

**###############################################** 

**网络socket**

        是ip + port  --》格式ip:port     **例：  192.168.44.170:3306**

        网络中通过ip地址找到对方，实现不同电脑之间的不同进之间的通信。

```
[root@localhost ~]# mysql -h 192.168.44.170 -P3306 -u root -p'Sanchuang123#'

```

-h  指定主机名（ip） host

-P  port端口

<img alt="" height="716" src="https://img-blog.csdnimg.cn/da2bc17aa72e4d16bb0f793af31566fe.png" width="1200">

**###############################################** 

####  2.1.2  检验我们的mysql服务是使用文件socket还是网络socket

我们可以将mysql配置文件my.cnf注释掉，再来登录mysql服务

mysql -u -p 的方式进行连接，默认是通过socket连接的。

<img alt="" height="150" src="https://img-blog.csdnimg.cn/7b0b6cc0ae374fe2aef610517b3edc0d.png" width="924">

 <img alt="" height="169" src="https://img-blog.csdnimg.cn/129a9d1c971e497db4249a32afbe612f.png" width="1170">

 可以看到，错误信息显示无法连接到本地mysql服务，通过socket，

因为mysql服务会默认到配置文件里面去找socket文件，然后去/tmp/下去寻找socket文件

没有找到socket文件的话mysql进程是无法找到mysqld这个工作进程的，也就无法登陆了。

如果我们在登陆的时候指定socket文件，还是可以正常登陆的。

<img alt="" height="442" src="https://img-blog.csdnimg.cn/2f0e06f4e4ad4ca48c4fbfb06390a306.png" width="1162">

** 我们也可以通过网络socket连接mysql**

**因为mysql不允许root用户远程登录，所以我们通过网络socket连接的时候可以连接本机。**

<img alt="" height="359" src="https://img-blog.csdnimg.cn/276a8c4bf9cf44cc89b3c3486f3b4365.png" width="1153">

 **###############################################**

### 2.2  给一个用户授权，让其可以远程登录



```
root@(none) 22:05  mysql&gt;grant all on *.* to 'liming'@'%' identified by 'liming123456';
Query OK, 0 rows affected, 1 warning (0.00 sec)

```

**grant **是授权的命令

**all** 表示所有的权限：select， insert， update， delete等

**on *.*  **表示在所有的库里的所有的表 第一个 * 表示库  第2个*表示表

        库理解为一个文件夹， 表理解为文件夹里的文件

**to ‘cali’@‘%’**  允许cali用户从任何地方的客户机连接过来登录

                        % 在MYSQL是通配符，代表任意字符串

identfied by ‘’

MYSQL里一个完整的用户格式是 用户名@允许访问的ip或者域名

 **###############################################**

**测试连接**

在windows里使用sqlyog远程连接mysql

测试连接，发现连接成功

<img alt="" height="564" src="https://img-blog.csdnimg.cn/5c0096c796ea42629d866da721fc0869.png" width="909">

 

 可以看到我们已经成功远程连接到了mysql

<img alt="" height="732" src="https://img-blog.csdnimg.cn/63083bb68803481aab68f083b0927194.png" width="1154">

 

**###############################################** 

## 3.0  mysql密码破解

### 3.1  普通用户密码破解

使用超级用户登录，然后去修改密码就可以了。

```
alter user 'cali'@'%' identified by '123456'
```

**###############################################** 

### 3.2  root用户密码破解

#### 1、停止mysql进程的运行

```
service mysqld stop

```

**###############################################** 

#### 2、修改配置文件

```
[root@localhost ~]#vim /etc/my.cnf
[mysqld]
user=mysql #指定启动mysql进程的用户
skip-grant-tables #跳过密码验证
#validate-password=off #禁用密码复杂性策略

```

**###############################################** 

#### 3、启动mysql进程

```
[root@localhost ~]#service mysqld start
```

**###############################################** 

#### 4、登录mysql，不接密码

<img alt="" height="224" src="https://img-blog.csdnimg.cn/aec553eac61c4653b7d9df7b875db2d0.png" width="817">

**###############################################** 

####  5、修改root用户密码

可以用命令修改root用户的密码

```
alter user 'root'@'localhost' identified by '123456'
```

但是直接敲这条命令会报错，我们要刷新一下权限（会加载原来没有加载的权限表 --》用户名和密码所在的表user等）

```
flush privileges;
```

然后修改密码。密码修改成功后将配置文件里面的跳过密码验证注释

```
[root@localhost ~]#vim /etc/my.cnf
[mysqld]
user=mysql #指定启动mysql进程的用户
#skip-grant-tables #跳过密码验证
#validate-password=off #禁用密码复杂性策略
```

**###############################################**
