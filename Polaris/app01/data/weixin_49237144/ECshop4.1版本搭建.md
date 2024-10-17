
--- 
title:  ECshop4.1版本搭建 
tags: []
categories: [] 

---
## ECshop电商平台的搭建

**Hello小伙伴们，你们好，又是日常get新技能的一天，0基础入门，趁着热乎，快上车啦** ~~

**今天，咱们就来实践一下如何使用PHP+Apache+MySQL项目部署到Linux服务器的** ~~



#### 文章目录
- - <ul><li><ul><li>- - - - - - <ul><li>- - - - - - - - - - - - 


cat /etc/redhat-release



#### 1. 检查系统是否已经安装了Apache HTTP Server

```
# 第一种查看方式
[root@localhost ~]# yum list installed | grep httpd

# 第二种查看方式
[root@localhost ~]# rpm -qa | grep httpd

# 第三种查看方式 -v 或者 -version 都可以
[root@localhost ~]# httpd -version
-bash: httpd: command not found


```

#### 2. 如果没有安装，执行下面命令安装Apache HTTP Server

```
[root@localhost ~]# yum install httpd -y

```

#### 3. 查看httpd如果返回如下内容，说明已经安装

```
# 如果返回如下内容，说明已经安装号Apache HTTP Server
[root@localhost ~]# httpd -version

Server version: Apache/2.4.6 (CentOS)

Server built:   Mar 24 2022 14:57:57

```

#### 4. 检查系统是否已经安装了PHP和插件

```
# 如果返回如下内容，说明已经安装PHP和插件
[root@localhost ~]# php -v
PHP 5.4.16 (cli) (built: Apr  1 2020 04:07:17) 
Copyright (c) 1997-2013 The PHP Group
Zend Engine v2.4.0, Copyright (c) 1998-2013 Zend Technologies


[root@localhost ~]# rpm -qa | grep php-gd
php-gd-5.4.16-46.1.el7_7.x86_64

[root@localhost ~]# rpm -qa|grep php-mysql
php-mysql-5.4.16-46.1.el7_7.x86_64

```

#### 5. 如果没有安装，执行下面命令安装

```
[root@localhost ~]# yum install php php-gd php-mysql -y

```

#### 6. 安装MySQL5.7

​ 总技术路线：借助rpm安装加上yum安装

```
小插曲：
	在centos 6 安装 mysql-server是直接使用命令 yum -y install mysql-server ，
	但是在CentOS 7 中出现了 No package mysql-server available. Error: Nothing to do 错误。

	简单来说，MariaDB 是 MySQL 的fork，两者关系就好比 Red Hat 和 CentOS 的关系。从 MySQL 变成了 Oracle 甲骨文公司的产后，MySQL 就已经从 RHEL 和 CentOS 所提供的套件清单移除了。

```

##### 6.1 第一先通过wget命令下载官网MySQL5.7版本的rpm包

```
[root@localhost ~]# yum install wget -y
[root@localhost ~]# wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm

```

##### 6.2 安装官网MySQL5.7版本的rpm包

```
安装这个包后，会获得两个mysql的yum repo源：/etc/yum.repos.d/mysqlcommunity.repo，/etc/yum.repos.d/mysql-community-source.repo。
[root@localhost ~]# yum -y install mysql57-community-release-el7-10.noarch.rpm

```

##### 6.3 备份repo源

```
[root@localhost ~]# cp /etc/yum.repos.d/mysql-community.repo /etc/yum.repos.d/mysql-community.repo.bak

```

##### 6.4 通过sed写入MySQL官方源和清华镜像源

```
[root@localhost ~]# sed -i 's#http://repo.mysql.com/#https://mirrors.tuna.tsinghua.edu.cn/mysql/#g' /etc/yum.repos.d/mysql-community.repo

[root@localhost ~]# sed -i 's#/el/7/#-el7-#g' /etc/yum.repos.d/mysql-community.repo

```

##### 6.5 是将服务器上的软件包信息进行本地缓存

```
[root@localhost ~]# yum makecache

```

##### 6.6 安装MySQL server

```
[root@localhost ~]# yum -y install mysql-community-server
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
Importing GPG key 0x5072E1F5:
 Userid     : "MySQL Release Engineering &lt;mysql-build@oss.oracle.com&gt;"
 Fingerprint: a4a9 4068 76fc bd3c 4567 70c8 8c71 8d3b 5072 e1f5
 Package    : mysql57-community-release-el7-10.noarch (@/mysql57-community-release-el7-10.noarch)
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-mysql

Public key for mysql-community-common-5.7.38-1.el7.x86_64.rpm is not installed
 Failing package is: mysql-community-common-5.7.38-1.el7.x86_64
 GPG Keys are configured as: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql

```

##### 6.7 上面安装MySQL服务的时候，可能会出现密钥的问题，就导入官方GPG

```
[root@localhost ~]# rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022

```

##### 6.8 开启MySQL服务

```
[root@localhost ~]# systemctl start mysqld.service

# 查看MySQL服务的状态
[root@localhost ~]# systemctl status mysqld.service

```

##### 6.9 查看MySQL的初始化密码，如：root@localhost: vx&lt;I7q_ltict

```
[root@localhost ~]# grep "password" /var/log/mysqld.log
2022-05-17T07:43:27.367757Z 1 [Note] A temporary password is generated for root@localhost: vx&lt;I7q_ltict

```

##### 6.10 登录MySQL

```
[root@localhost ~]# mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.38

```

##### 6.11 MySQL5.7 修改密码四种方法

```
# 第一种：在Linux命令行修改，会提示两个警告！
# [警告]：在命令行界面上使用密码可能不安全。
# [警告]：由于密码将以明文形式发送到服务器，请使用ssl连接以确保密码安全。
[root@localhost ~]# mysqladmin -uroot -p'Aba12345@' password 'Aba123456@'
mysqladmin: [Warning] Using a password on the command line interface can be insecure.
Warning: Since password will be sent to server in plain text, use ssl connection to ensure password safety.


# 第二种：alter user 修改密码
mysql&gt;  ALTER USER 'root'@'localhost' IDENTIFIED BY 'Aba123456@';
Query OK, 0 rows affected (0.00 sec)


# 第三种：update user set 修改密码  注意：一定要 use 数据库 才能使用命令
# MySQL5.7 版本之前使用这个修改密码
update user set password=password("填入新密码") where user='root';
update user set password="填入新密码" where user='root';

mysql&gt; update user set password=password('Aba12345@') where user='root';
ERROR 1054 (42S22): Unknown column 'password' in 'field list'

# MySQL5.7 版本之后使用这个修改密码
update user set authentication_string=password('填入新密码') where user='root';
update user set authentication_string='填入新密码' where user='root';

mysql&gt; update user set authentication_string=password('Aba12345@') where user='root';
Query OK, 1 row affected, 1 warning (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 1


# 第四种： set password 修改密码
# 在root登录下，可以修改其他用户密码
mysql&gt; set password for root@localhost = password('Aba123456@');
Query OK, 0 rows affected, 1 warning (0.00 sec)

# 在某个用户登录下，只能修改自己密码
mysql&gt; set password=password("Aba12345@");
Query OK, 0 rows affected, 1 warning (0.00 sec)


```

##### 6.12 修改密码策略

```
# 必须修改密码，才能查看 mysql 初始的密码策略：
mysql&gt; show variables like 'validate_password%';
+--------------------------------------+--------+
| Variable_name                        | Value  |
+--------------------------------------+--------+
| validate_password_check_user_name    | OFF    |
| validate_password_dictionary_file    |        |
| validate_password_length             | 8      |
| validate_password_mixed_case_count   | 1      |
| validate_password_number_count       | 1      |
| validate_password_policy             | MEDIUM |
| validate_password_special_char_count | 1      |
+--------------------------------------+--------+
7 rows in set (0.01 sec)
#关于 mysql 密码策略相关参数；
1）、validate_password_length 固定密码的总长度；
2）、validate_password_dictionary_file 指定密码验证的文件路径；
3）、validate_password_mixed_case_count 整个密码中至少要包含大/小写字母的总个数；
4）、validate_password_number_count 整个密码中至少要包含阿拉伯数字的个数；
5）、validate_password_policy 指定密码的强度验证等级，默认为 MEDIUM；
关于 validate_password_policy 的取值：
off or 关闭； 0 or LOW；  1 or MEDIUM；  2 or STRONG
    0/LOW：   只验证长度；
    1/MEDIUM：验证长度、数字、大小写、特殊字符；
    2/STRONG：验证长度、数字、大小写、特殊字符、字典文件；

6）、validate_password_special_char_count 整个密码中至少要包含特殊字符的个数；


# 2. 设置密码的验证强度等级，设置 validate_password_policy 的全局参数为 LOW 即可
set global validate_password_policy=LOW;
# 3. 当前密码长度默认为 8 ，设置为4位的密码，设置validate_password_length 的全局参数为 4 即可
set global validate_password_length=4;

```

##### 6.13 授权其他的IP可以远程登录

```
# 授权给其他的远程登录使用
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;

# 创建新用户
CREATE USER 'username'@'host' IDENTIFIED BY 'password';


```

```
# 如果返回如下内容，说明已经安装MariaDB
[root@localhost ~]# rpm -qa|grep mariadb

mariadb-libs-5.5.64-1.el7.x86_64

mariadb-5.5.64-1.el7.x86_64

mariadb-server-5.5.64-1.el7.x86_64

# 如果没有安装，执行下面命令安装和配置，按照提示输入root用户新密码
[root@localhost ~]# yum install mariadb-server -y

[root@localhost ~]# systemctl start mariadb

[root@localhost ~]# systemctl enable mariadb

[root@localhost ~]# systemctl status mariadb

[root@localhost ~]# mysql_secure_installation

```

#### 7. 修改PHP配置文件设置时区

```
# 搜索timezone，把date.timezone前的注释符# 或者 ; 去掉，值设为PRC
[root@localhost ~]# vim /etc/php.ini

date.timezone = PRC

```

#### 8. 下载，解压ECShop 3.6源码

```
yum -y install lrzsz

[root@localhost ~]# wget http://zj.mycodes.net/201708/ECShop_3.6.0_UTF8_release.zip

[root@localhost ~]# unzip ECShop_3.6.0_UTF8_release.zip

[root@localhost ~]# mv ECShop_3.6.0_UTF8_release/source/* /var/www/html/

```

#### 6、设置源码目录可写

[root@localhost ~]# mv ECShop_3.6.0_UTF8_release/source/* /var/www/html/

[root@localhost ~]# cd /var/www/html

[root@localhost ~]# ls

appserver ecshop

[root@localhost ~]# chmod 777 -R appserver ecshop

#### 7、关闭selinux

```
# 修改selinux的配置文件，把SELINUX的值改为disabled

[root@localhost conf]# vim /etc/selinux/config

SELINUX=disabled

SELINUXTYPE=targeted

# 表示临时关闭selinux防火墙

[root@localhost conf]# setenforce 0

setenforce: SELinux is disabled

```

#### 8、启动Apache服务，查询服务状态并设置开机启动服务

```
# 开启Apache HTTP Server
[root@localhost ~]# systemctl start httpd

# 开机自启动Apache HTTP Server
[root@localhost ~]# systemctl enable httpd

# 查看Apache HTTP Server 状态
[root@localhost ~]# systemctl status httpd

# 重启Apache HTTP Server 有更改内容才使用
[root@localhost ~]# systemctl status httpd

```

#### 9、防火墙允许Apache服务的80端口

```
[root@localhost conf]# firewall-cmd --add-port=80/tcp --zone=public --permanent

success

[root@localhost conf]# firewall-cmd --reload

success

```

#### 10、浏览器安装ECShop

假设服务器的IP地址是192.168.8.128，浏览器地址栏输入 http://192.168.85.128/ecshop/install/index.php

重启Apache HTTP Server 有更改内容才使用 [root@localhost ~]# systemctl status httpd

```



### 9、防火墙允许Apache服务的80端口

```shell
[root@localhost conf]# firewall-cmd --add-port=80/tcp --zone=public --permanent

success

[root@localhost conf]# firewall-cmd --reload

success

```

#### 10、浏览器安装ECShop

假设服务器的IP地址是192.168.8.128，浏览器地址栏输入 http://192.168.85.128/ecshop/install/index.php

总是报forbidden，手动把www和html,ecshop下所有目录权限全部手动改成可编辑模式才可以。。。
