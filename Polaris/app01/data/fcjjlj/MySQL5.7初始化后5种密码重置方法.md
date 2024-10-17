
--- 
title:  MySQL5.7初始化后5种密码重置方法 
tags: []
categories: [] 

---
前言：由于好几次安装MySQL5.7后一直被重置密码所困扰,因此特意整理重置的方法 安装MySQL5.7

```
[ubuntu@VM-0-12-ubuntu]# ll  以下的rpm安装包可以随处下载
total 402356
-rw-r--r-- 1 root root      24744 Nov 25  2015 libaio-0.3.109-13.el7.x86_64.rpm
-rw-r--r-- 1 7155 31415  25106088 Mar  5 10:24 mysql-community-client-5.7.22-1.el7.x86_64.rpm
-rw-r--r-- 1 7155 31415   3781636 Mar  5 10:24 mysql-community-devel-5.7.22-1.el7.x86_64.rpm
-rw-r--r-- 1 7155 31415   2239868 Mar  5 10:24 mysql-community-libs-5.7.22-1.el7.x86_64.rpm
-rw-r--r-- 1 7155 31415 172992596 Mar  5 10:25 mysql-community-server-5.7.22-1.el7.x86_64.rpm
[ubuntu@VM-0-12-ubuntu]# 
[ubuntu@VM-0-12-ubuntu]# rpm -ivh *.rpm --nodeps --force
warning: mysql-community-client-5.7.22-1.el7.x86_64.rpm: Header V3 DSA/SHA1 Signature, key ID 5072e1f5: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:mysql-community-libs-5.7.22-1.el7################################# [ 20%]
   2:mysql-community-client-5.7.22-1.e################################# [ 40%]
   3:libaio-0.3.109-13.el7            ################################# [ 60%]
   4:mysql-community-server-5.7.22-1.e################################# [ 80%]
   5:mysql-community-devel-5.7.22-1.el################################# [100%]
 
启动mysql
[ubuntu@VM-0-12-ubuntu]# systemctl start mysqld
 
从日志中获取随机生成的密码
[ubuntu@VM-0-12-ubuntu]# grep password /var/log/mysqld.log 
2018-07-15T09:01:09.735836Z 1 [Note] A temporary password is generated for root@localhost: ViFg8pWf+,lU
[ubuntu@VM-0-12-ubuntu]# mysql -uroot -pViFg8pWf+,lU
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.22
Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.
Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
 
登录后并不能任何操作
mysql&gt; show databases;
ERROR 1820 (HY000): Unknown error 1820
mysql&gt; select * from mysql;
ERROR 1046 (3D000): 

```

##### 方法1：使用alter修改

```
mysql&gt; ALTER USER USER() IDENTIFIED BY 'Reid790!@#$';
Query OK, 0 rows affected (0.00 sec)
 
mysql&gt; ALTER USER 'root'@'localhost' IDENTIFIED BY 'Tom579#$%^&amp;';  #针对localhost
Query OK, 0 rows affected (0.00 sec)
 
或者先关闭其密码策略修改
mysql&gt; select @@validate_password_length;
ERROR 1820 (HY000): Unknown error 1820
mysql&gt;  ALTER USER USER() IDENTIFIED BY '12345678';
Query OK, 0 rows affected (0.00 sec)
 
validate_password_policy有以下取值：
Policy  Tests Performed
0 or LOW    Length
1 or MEDIUM Length; numeric, lowercase/uppercase, and special characters
2 or STRONG Length; numeric, lowercase/uppercase, and special characters; dictionary file
默认是1，即MEDIUM，所以刚开始设置的密码必须符合长度，且必须含有数字，小写或大写字母，特殊字符。

```

##### 方法2：使用set password

```
mysql&gt; SET PASSWORD FOR 'root'@'localhost' = PASSWORD('Gerk087@&amp;#@');  #第一次也要符合密友复杂度
Query OK, 0 rows affected, 1 warning (0.00 sec)
 
mysql&gt; flush privileges;
Query OK, 0 rows affected (0.00 sec)

```

##### 方法3：使用update

```
mysql&gt; UPDATE mysql.user SET authentication_string = PASSWORD('Marry583@&amp;%!'), password_expired = 'N' WHERE User = 'root' AND Host = 'localhost';
Query OK, 1 row affected, 1 warning (0.00 sec)
 
mysql&gt; flush privileges;
Query OK, 0 rows affected (0.00 sec)

```

##### 方法4：使用mysql_secure_installation

```
[ubuntu@VM-0-12-ubuntu]# mysql_secure_installation 
 
Securing the MySQL server deployment.
 
Enter password for user root: Marry583@&amp;%!
The 'validate_password' plugin is installed on the server.
The subsequent steps will run with the existing configuration
of the plugin.
Using existing password for root.
 
Estimated strength of the password: 100 
Change the password for root ? ((Press y|Y for Yes, any other key for No) : y
 
New password: Tom579#$%^&amp;
 
Re-enter new password: Tom579#$%^&amp;
 
Estimated strength of the password: 100 
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.
为了安全应该yes
Remove anonymous users? (Press y|Y for Yes, any other key for No) : No 
 
 ... skipping.
 
 
Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.
为了安全应该yes
Disallow root login remotely? (Press y|Y for Yes, any other key for No) : No 
 
 ... skipping.
By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.
 
为了安全应该yes
Remove test database and access to it? (Press y|Y for Yes, any other key for No) : No  
 
 ... skipping.
Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.
 
Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
Success.
 
All done! 

```

##### 方法5：跳过授权列表skip-grant-tables

```
[ubuntu@VM-0-12-ubuntu]# mysql
ERROR 1045 (28000): Unknown error 1045
[ubuntu@VM-0-12-ubuntu]# vim /etc/my.cnf  #使用完后去掉
[mysqld]
skip-grant-tables=1
 
重启mysql,再修改
[ubuntu@VM-0-12-ubuntu]# systemctl restart mysqld
[ubuntu@VM-0-12-ubuntu]# mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.22 MySQL Community Server (GPL)
 
Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.
 
Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.
 
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
 
mysql&gt; set password = PASSWORD('Reid4909@%&amp;');
ERROR 1290 (HY000): Unknown error 1290
mysql&gt; ALTER USER 'root'@'localhost' IDENTIFIED BY 'Tom579#$%^&amp;';
ERROR 1290 (HY000): Unknown error 1290
mysql&gt; flush privileges;
Query OK, 0 rows affected (0.00 sec)
 
mysql&gt; set password = PASSWORD('Reid4909@%&amp;');
ERROR 1133 (42000): 
mysql&gt; ALTER USER 'root'@'localhost' IDENTIFIED BY 'Tom579#$%^&amp;';
Query OK, 0 rows affected (0.01 sec)
 
mysql&gt; set password for root@localhost = password('123456');
Query OK, 0 rows affected, 1 warning (0.00 sec)

```

##### 总结Summary

a. mysql5.7安装好后会在/var/log/mysql.log中产随机密码,而且不修改密码不能执行任何操作 b. mysql5.7的user表中的password字串修改为authentication_string c. 修改密码的Policy转变是1(中级),因此设置时要符合规则 d. 跳过授权列时,同时也不受密码policy影响
