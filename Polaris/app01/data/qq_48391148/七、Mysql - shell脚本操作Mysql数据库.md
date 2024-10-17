
--- 
title:  七、Mysql - shell脚本操作Mysql数据库 
tags: []
categories: [] 

---
**目录**



















### **知识点1：在linux系统里面使用shell来操作数据库**

```
[root@localhost ~]# mysql -u wangsh -p'123456' -e "show databases"
mysql: [Warning] Using a password on the command line interface can be insecure.
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sanchuang          |
| student            |
| sys                |
| t1                 |
| wangsh             |
+--------------------+
[root@localhost ~]# mysql -u wangsh -p'123456' -e "select host,user from mysql.user"
mysql: [Warning] Using a password on the command line interface can be insecure.
+---------------+---------------+
| host          | user          |
+---------------+---------------+
| %             | liming        |
| %             | shiyaling     |
| %             | wangsh        |
| %             | zhangj        |
| 192.168.0.124 | liuhongjie    |
| localhost     | mysql.session |
| localhost     | mysql.sys     |
| localhost     | root          |
+---------------+---------------+
[root@localhost ~]# 

```

#### 一次多条语句查询

```
[root@localhost ~]# mysql -u wangsh -p'123456' -e "show databases;select user,host from mysql.user"
mysql: [Warning] Using a password on the command line interface can be insecure.
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sanchuang          |
| student            |
| sys                |
| t1                 |
| wangsh             |
+--------------------+
+---------------+---------------+
| user          | host          |
+---------------+---------------+
| liming        | %             |
| shiyaling     | %             |
| wangsh        | %             |
| zhangj        | %             |
| liuhongjie    | 192.168.0.124 |
| mysql.session | localhost     |
| mysql.sys     | localhost     |
| root          | localhost     |
+---------------+---------------+

```

 **############################################**

### 知识点2：使用EOF方式操作数据库

一次进行多条sql语句的操作

```
[root@localhost ~]# mysql -u wangsh -p'123456' &lt;&lt;EOF
&gt; show databases;
&gt; select host,user from mysql.user;
&gt; use mysql;
&gt; show tables;
&gt; EOF
mysql: [Warning] Using a password on the command line interface can be insecure.
Database
information_schema
mysql
performance_schema
sanchuang
student
sys
t1
wangsh
host	user
%	liming
%	shiyaling
%	wangsh
%	zhangj
192.168.0.124	liuhongjie
localhost	mysql.session
localhost	mysql.sys
localhost	root
Tables_in_mysql
columns_priv
db
engine_cost
event
func
general_log
gtid_executed
help_category
help_keyword
help_relation
help_topic
innodb_index_stats
innodb_table_stats
ndb_binlog_index
plugin
proc
procs_priv
proxies_priv
server_cost
servers
slave_master_info
slave_relay_log_info
slave_worker_info
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user

```

**############################################** 

### 知识点3：在mysql里面使用Linux命令

>  
 **在linux命令前面加上system** 


```
wangsh@(none) 17:10  mysql&gt;system ls;
anaconda-ks.cfg  mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz  onekey_install_mysql_binary_v3.sh
wangsh@(none) 17:10  mysql&gt;system pwd;
/root
wangsh@(none) 17:11  mysql&gt;

```

**############################################** 

### 知识点4：mysql里面删除语句的区别

#### delete 语句 和 truncate语句的区别

>  
 **truncate适合删除大的表，速度非常快，可以理解为直接去清除表空间（表文件），但是不会产生日志二进制文件，不能通过日志去恢复，只能通过原来的备份去恢复** 
 **delete语句删除数据非常慢，但是会产生二进制日志文件，可以恢复** 


**############################################**

### 面试题：将除了题目要求的三张表外的所有表的数据清空，编写一个shell脚本

<img alt="" height="193" src="https://img-blog.csdnimg.cn/a49699b437854422a571ce5996c32b79.png" width="925">

####  **示例：建立测试环境：**

```
wangsh@(none) 17:22  mysql&gt;create database test;
Query OK, 1 row affected (0.00 sec)

wangsh@(none) 17:22  mysql&gt;use test;
Database changed
wangsh@test 17:22  mysql&gt;create table tbllog_fan(id int);
Query OK, 0 rows affected (0.01 sec)

wangsh@test 17:23  mysql&gt;create table tbllog_liu(id int);
Query OK, 0 rows affected (0.00 sec)

wangsh@test 17:23  mysql&gt;create table tbllog_zhang(id int);
Query OK, 0 rows affected (0.01 sec)

wangsh@test 17:23  mysql&gt;create table tbllog_wang(id int);
Query OK, 0 rows affected (0.00 sec)

wangsh@test 17:23  mysql&gt;create table tbllog_pay(id int);
Query OK, 0 rows affected (0.01 sec)

wangsh@test 17:24  mysql&gt;create table tbllog_role(id int);
Query OK, 0 rows affected (0.01 sec)

wangsh@test 17:24  mysql&gt;create table tbllog_online(id int);
Query OK, 0 rows affected (0.01 sec)

wangsh@test 17:24  mysql&gt;show tables ;
+----------------+
| Tables_in_test |
+----------------+
| tbllog_fan     |
| tbllog_liu     |
| tbllog_online  |
| tbllog_pay     |
| tbllog_role    |
| tbllog_wang    |
| tbllog_zhang   |
+----------------+
7 rows in set (0.00 sec)

wangsh@test 17:24  mysql&gt;insert into tbllog_fan(id) values(1),(2),(3);
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

wangsh@test 17:25  mysql&gt;insert into tbllog_liu(id) values(1),(2),(3);
Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0

wangsh@test 17:25  mysql&gt;insert into tbllog_online(id) values(1),(2),(3);
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

wangsh@test 17:25  mysql&gt;insert into tbllog_pay(id) values(1),(2),(3);
Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0

wangsh@test 17:25  mysql&gt;insert into tbllog_role(id) values(1),(2),(3);
Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0

wangsh@test 17:26  mysql&gt;insert into tbllog_wang(id) values(1),(2),(3);
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

wangsh@test 17:26  mysql&gt;insert into tbllog_zhang(id) values(1),(2),(3);
Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0

```

查看建立的环境：

```
root@test 17:43  mysql&gt;show tables;
+----------------+
| Tables_in_test |
+----------------+
| tbllog_fan     |
| tbllog_liu     |
| tbllog_online  |
| tbllog_pay     |
| tbllog_role    |
| tbllog_wang    |
| tbllog_zhang   |
+----------------+
7 rows in set (0.00 sec)

root@test 17:43  mysql&gt;select * from tbllog_fan;
+------+
| id   |
+------+
|    1 |
|    2 |
|    3 |
+------+
3 rows in set (0.00 sec)

```

####  编写shell脚本

```
[root@localhost lianxi]# cat truncate_tables.sh 
#! /bin/bash

for i in $(mysql -uwangsh -p'123456' -e "use test;show tables" 2&gt; /dev/null|tail -n +2|egrep -v  "^tbllog_pay|^tbllog_online|^tbllog_role")
do
	mysql -u wangsh -p'123456' -e "truncate table test.$i"
	echo "成功删除$i表"
done


```

执行结果

```
[root@localhost lianxi]# bash truncate_tables.sh 
mysql: [Warning] Using a password on the command line interface can be insecure.
成功删除tbllog_fan表
mysql: [Warning] Using a password on the command line interface can be insecure.
成功删除tbllog_liu表
mysql: [Warning] Using a password on the command line interface can be insecure.
成功删除tbllog_wang表
mysql: [Warning] Using a password on the command line interface can be insecure.
成功删除tbllog_zhang表

```

>  
 **可以看到，除了规定的三张表，其他表的内容都被清空了。 ** 


```
root@test 17:43  mysql&gt;select * from tbllog_fan;
Empty set (0.00 sec)

root@test 17:45  mysql&gt;select * from tbllog_liu;
Empty set (0.00 sec)

root@test 17:45  mysql&gt;select * from tbllog_role;
+------+
| id   |
+------+
|    1 |
|    2 |
|    3 |
+------+
3 rows in set (0.00 sec)

```


