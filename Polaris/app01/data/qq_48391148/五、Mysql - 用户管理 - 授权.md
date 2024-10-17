
--- 
title:  五、Mysql - 用户管理 - 授权 
tags: []
categories: [] 

---
**目录**







































### 知识点1：建立用户

#### 语法形式：

```
root@sanchuang 10:32  mysql&gt;help create user
Name: 'CREATE USER'
Description:
Syntax:
CREATE USER [IF NOT EXISTS]
    user [auth_option] [, user [auth_option]] ...
    [REQUIRE {NONE | tls_option [[AND] tls_option] ...}]
    [WITH resource_option [resource_option] ...]
    [password_option | lock_option] ...

```

示例：新建一个用户liuhongjie

```
root@sanchuang 10:48  mysql&gt;create user 'liuhongjie'@'192.168.0.123' identified by 'liu123456';
Query OK, 0 rows affected (0.01 sec)

```

>  
 **'liuhongjie'   表示新建用户名** 
 **'192.168.0.123'  表示允许用户从这台主机连接过来** 
 **identified by  设置用户密码** 


 新建一个用户，他的用户名和密码会放到哪里？

```
root@sanchuang 10:52  mysql&gt;desc mysql.user;
+------------------------+-----------------------------------+------+-----+-----------------------+-------+
| Field                  | Type                              | Null | Key | Default               | Extra |
+------------------------+-----------------------------------+------+-----+-----------------------+-------+
| Host                   | char(60)                          | NO   | PRI |                       |       |
| User                   | char(32)                          | NO   | PRI |                       |       |
| Select_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Insert_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Update_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Delete_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Create_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Drop_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Reload_priv            | enum('N','Y')                     | NO   |     | N                     |       |
| Shutdown_priv          | enum('N','Y')                     | NO   |     | N                     |       |
| Process_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| File_priv              | enum('N','Y')                     | NO   |     | N                     |       |
| Grant_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| References_priv        | enum('N','Y')                     | NO   |     | N                     |       |
| Index_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Alter_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Show_db_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| Super_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Create_tmp_table_priv  | enum('N','Y')                     | NO   |     | N                     |       |
| Lock_tables_priv       | enum('N','Y')                     | NO   |     | N                     |       |
| Execute_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| Repl_slave_priv        | enum('N','Y')                     | NO   |     | N                     |       |
| Repl_client_priv       | enum('N','Y')                     | NO   |     | N                     |       |
| Create_view_priv       | enum('N','Y')                     | NO   |     | N                     |       |
| Show_view_priv         | enum('N','Y')                     | NO   |     | N                     |       |
| Create_routine_priv    | enum('N','Y')                     | NO   |     | N                     |       |
| Alter_routine_priv     | enum('N','Y')                     | NO   |     | N                     |       |
| Create_user_priv       | enum('N','Y')                     | NO   |     | N                     |       |
| Event_priv             | enum('N','Y')                     | NO   |     | N                     |       |
| Trigger_priv           | enum('N','Y')                     | NO   |     | N                     |       |
| Create_tablespace_priv | enum('N','Y')                     | NO   |     | N                     |       |
| ssl_type               | enum('','ANY','X509','SPECIFIED') | NO   |     |                       |       |
| ssl_cipher             | blob                              | NO   |     | NULL                  |       |
| x509_issuer            | blob                              | NO   |     | NULL                  |       |
| x509_subject           | blob                              | NO   |     | NULL                  |       |
| max_questions          | int(11) unsigned                  | NO   |     | 0                     |       |
| max_updates            | int(11) unsigned                  | NO   |     | 0                     |       |
| max_connections        | int(11) unsigned                  | NO   |     | 0                     |       |
| max_user_connections   | int(11) unsigned                  | NO   |     | 0                     |       |
| plugin                 | char(64)                          | NO   |     | mysql_native_password |       |
| authentication_string  | text                              | YES  |     | NULL                  |       |
| password_expired       | enum('N','Y')                     | NO   |     | N                     |       |
| password_last_changed  | timestamp                         | YES  |     | NULL                  |       |
| password_lifetime      | smallint(5) unsigned              | YES  |     | NULL                  |       |
| account_locked         | enum('N','Y')                     | NO   |     | N                     |       |
+------------------------+-----------------------------------+------+-----+-----------------------+-------+
45 rows in set (0.01 sec)

```

>  
 **当我们新建用户的时候，create语句会别转成一条insert语句插入mysql数据库的user表里面** 
 **用户名会插入 User字段里面** 
 **主机名会插入Host字段里面** 
 **密码会插入 authentication_string字段里面** 


#### 复合主键

可以看到User表里面的Host字段和User字段都是主键，也就是说名字和主机名都必须唯一，且不能为空

**示例：如果我们再创建一个同名同主机名的用户就会报错**

```
root@sanchuang 10:54  mysql&gt;create user 'liuhongjie'@'192.168.0.123' identified by '123546'
    -&gt; ;
ERROR 1396 (HY000): Operation CREATE USER failed for 'liuhongjie'@'192.168.0.123'

```

但是主机名和刚才建立的liuhongjie用户不一样就可以新建成功

```
root@sanchuang 11:02  mysql&gt;create user 'liuhongjie'@'192.168.0.124' identified by 'liu123456';
Query OK, 0 rows affected (0.00 sec)

```

查看user表里面刚才新建的字段

```
root@sanchuang 11:07  mysql&gt;select user,host,authentication_string from mysql.user;
+---------------+---------------+-------------------------------------------+
| user          | host          | authentication_string                     |
+---------------+---------------+-------------------------------------------+
| root          | localhost     | *4ABA759CFB5DDBF29AFAFBFB03026091F6F694FD |
| mysql.session | localhost     | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| mysql.sys     | localhost     | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| liming        | %             | *FFA025B9023C96F7DCB1078E0F171682708C9153 |
| liuhongjie    | 192.168.0.123 | *0BA8D66F9147D667B15E8D10BDEB997E7E15C494 |
| liuhongjie    | 192.168.0.124 | *0BA8D66F9147D667B15E8D10BDEB997E7E15C494 |
+---------------+---------------+-------------------------------------------+
6 rows in set (0.00 sec)

```

**####################################################### **

### 知识点2：修改用户密码：

#### 使用   alter user   语句来修改用户密码

语法格式：

```
Syntax:
ALTER USER [IF EXISTS]
    user [auth_option] [, user [auth_option]] ...
    [REQUIRE {NONE | tls_option [[AND] tls_option] ...}]
    [WITH resource_option [resource_option] ...]
    [password_option | lock_option] ...

ALTER USER [IF EXISTS]
    USER() IDENTIFIED BY 'auth_string'

```

```
root@sanchuang 11:07  mysql&gt;alter user 'liuhongjie'@'192.168.0.123' identified by '123';
Query OK, 0 rows affected (0.00 sec)

```

**####################################################### ** 

### 知识点3：如何查看Mysql的版本？

#### 1、可以在登陆Mysq的时候看到版本号

```
[root@localhost ~]# mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 7
Server version: 5.7.34 MySQL Community Server (GPL)

```

#### 2、使用select version()语句

```
root@sanchuang 11:13  mysql&gt;select version();
+-----------+
| version() |
+-----------+
| 5.7.34    |
+-----------+
1 row in set (0.00 sec)

```

#### 3、使用show variables like "version"语句

```
root@sanchuang 11:17  mysql&gt;show variables like "version";
+---------------+--------+
| Variable_name | Value  |
+---------------+--------+
| version       | 5.7.34 |
+---------------+--------+
1 row in set (0.01 sec)

```

**####################################################### ** 

### 知识点4：如何查看当前登陆用户？

```
root@sanchuang 11:19  mysql&gt;select user();
+----------------+
| user()         |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)

```

**####################################################### ** 

### 知识点5：如何查看当前使用的数据库？

```
root@sanchuang 11:21  mysql&gt;select database();
+------------+
| database() |
+------------+
| sanchuang  |
+------------+
1 row in set (0.00 sec)

```

### 如何查看当前有哪些用户登录到了mysql里面？

```
root@mysql 16:40  mysql&gt;show processlist;
+----+--------+-----------+-------+---------+------+----------+------------------+
| Id | User   | Host      | db    | Command | Time | State    | Info             |
+----+--------+-----------+-------+---------+------+----------+------------------+
| 14 | root   | localhost | mysql | Query   |    0 | starting | show processlist |
| 23 | wangsh | localhost | NULL  | Sleep   |   14 |          | NULL             |
+----+--------+-----------+-------+---------+------+----------+------------------+
2 rows in set (0.00 sec)

root@mysql 17:06  mysql&gt;

```

**####################################################### ** 

### 知识点6:删除用户

示例：删除用户  liuhongjie@192.168.0.123

```
root@sanchuang 11:21  mysql&gt;drop user 'liuhongjie'@'192.168.0.123';
Query OK, 0 rows affected (0.00 sec)

root@sanchuang 11:34  mysql&gt;select host,user from mysql.user;
+---------------+---------------+
| host          | user          |
+---------------+---------------+
| %             | liming        |
| 192.168.0.124 | liuhongjie    |
| localhost     | mysql.session |
| localhost     | mysql.sys     |
| localhost     | root          |
+---------------+---------------+
5 rows in set (0.00 sec)

root@sanchuang 11:34  mysql&gt;

```

**####################################################### ** 

### 知识点7：Mysql默认4个数据库

```
root@sanchuang 11:34  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |      
| sys                |    
+--------------------+

```

#### information_schema 信息库：数据字典库

>  
 **        information_schema是一个信息数据库，它保存着关于Mysql服务器所维护的所有其他数据库的信息（如数据库名，数据库表，表栏的数据类型与访问权限等）** 
 **        数据字典 --》元数据：描述其他数据的数据** 


```
# 查看字符集
root@sanchuang 11:51  mysql&gt;show character set;

```

####  performance_schema 性能架构库

>  
 **        主要用于收集数据库服务器性能参数        ** 
 **        执行某些操作会有性能相关的参数** 


####  sys：Mysql系统

>  
   **      sys库所有的数据源自performance_schema目标是把performance_schema的复杂度降低，让DBA更好的阅读这个库里面的内容，让DBA更快的了解DB的运行情况** 


#### mysql：

>  
    **     存放的是Mysql程序相关的表：登录用户表，时间相关表，db，权限表，mysql的核心数据库，类似于sql server中的master表，主要负责存储数据库的用户，权限设置，关键字等mysql自己需要使用的控制和管理信息。** 


**####################################################### ** 

###  知识点8：grant权限

语法格式：

```
Syntax:
GRANT
    priv_type [(column_list)]
      [, priv_type [(column_list)]] ...
    ON [object_type] priv_level
    TO user [auth_option] [, user [auth_option]] ...
    [REQUIRE {NONE | tls_option [[AND] tls_option] ...}]
    [WITH {GRANT OPTION | resource_option} ...]

GRANT PROXY ON user
    TO user [, user] ...
    [WITH GRANT OPTION]

```

**示例：新建一个用户wangsh % 表示可以从任何机器连接过来**

```
root@sanchuang 11:54  mysql&gt;create user 'wangsh'@'%' identified by '123456';
Query OK, 0 rows affected (0.00 sec)

```

**可以看到，普通用户只有一个默认数据库**

```
wangsh@(none) 11:56  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
+--------------------+
1 row in set (0.00 sec)


```

**使用root用户给wangsh用户授权**

```
root@sanchuang 11:59  mysql&gt;grant select,insert on student.* to 'wangsh'@'%';
Query OK, 0 rows affected (0.00 sec)

```

>  
 ** select,insert表示给用户查询和插入语句的权利** 
 **on student.* 表示在student的所有表里面** 


** 可以看到，给wangsh用户授权对student数据库的所有表有查询，插入的权限后，wangsh用户就有student这个数据库了。**

```
wangsh@(none) 11:56  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| student            |
+--------------------+
2 rows in set (0.00 sec)

wangsh@(none) 12:02  mysql&gt;

```


