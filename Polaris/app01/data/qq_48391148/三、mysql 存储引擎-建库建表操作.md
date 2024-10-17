
--- 
title:  三、mysql 存储引擎-建库建表操作 
tags: []
categories: [] 

---
**目录**































































### 知识点1：mysql里面的数据库和表都以文件形式存储在linux系统里面

linux里面一切皆文件，我们在数据库里面创建的数据库和表都是以文件的形式存储于机器里面

```
root@(none) 15:41  mysql&gt;create database sanchuang;
Query OK, 1 row affected (0.01 sec)

root@(none) 15:41  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sanchuang          |
| student            |
| sys                |
+--------------------+
6 rows in set (0.01 sec)

root@(none) 15:41  mysql&gt;use sanchuang;
Database changed
root@sanchuang 15:41  mysql&gt;show tables;
Empty set (0.00 sec)

root@sanchuang 15:41  mysql&gt;create table student(id int,name varchar(20));
Query OK, 0 rows affected (0.01 sec)

```

**###################################################** 

### 我们在mysql里面创建数据库和表以后，也会生成对应的目录和文件

```
[root@localhost etc]# cd /data/mysql/
[root@localhost mysql]# ls
auto.cnf         ib_buffer_pool  localhost.localdomain.err  performance_schema  server-key.pem
ca-key.pem       ibdata1         localhost.localdomain.pid  private_key.pem     student
ca.pem           ib_logfile0     mysql                      public_key.pem      sys
client-cert.pem  ib_logfile1     mysql.sock                 sanchuang
client-key.pem   ibtmp1          mysql.sock.lock            server-cert.pem
[root@localhost mysql]# cd sanchuang/
[root@localhost sanchuang]# ls
db.opt
[root@localhost sanchuang]# ls
db.opt  student.frm  student.ibd
[root@localhost sanchuang]# pwd
/data/mysql/sanchuang
[root@localhost sanchuang]# 

```

**###################################################** 

### 知识点2： 存储引擎是什么？

数据库存储引擎是数据库底层软件组件，数据库管理系统使用数据引擎进行创建、查询、更新和删除数据操作。不同的存储引擎提供不同的存储机制、索引技巧、锁定水平等功能，使用不同的存储引擎还可以获得特定的功能，许多数据库管理系统都支持多种不同的存储引擎。MySQL 的核心就是存储引擎。

#### ** innodb 是MYSQL 的存储引擎（默认的存储引擎）**



#### **还有哪些存储引擎？**

 InnoDB、MyISAM、Memory

myisam

**student.frm文件  ---》存储表结构的  frame**

**student.ibd文件   ---》 innodb data 和index**

**###################################################**

### **示例：查看数据库里有哪些表：**

```
root@sanchuang 15:50  mysql&gt;show tables;
+---------------------+
| Tables_in_sanchuang |
+---------------------+
| student             |
+---------------------+
1 row in set (0.00 sec)

```

### **示例:查看student表的结构：**

```
root@sanchuang 16:00  mysql&gt;desc student;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)


```

 当我们不知道某个命令的具体语法时候可以使用**help**来查看语法规则

**###################################################** 

### **示例：查看insert帮助文档**

**[]里面的代表可接可不接**

**{}里面的表示可以选择一个**

```
root@sanchuang 16:00  mysql&gt;help insert
Name: 'INSERT'
Description:
Syntax:
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {VALUES | VALUE} (value_list) [, (value_list)] ...
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    SET assignment_list
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    SELECT ...
    [ON DUPLICATE KEY UPDATE assignment_list]

value:
    {expr | DEFAULT}

value_list:
    value [, value] ...

assignment:
    col_name = value

assignment_list:
    assignment [, assignment] ...


```

**###################################################** 

### **示例：向刚创建的表里面插入数据**

```
root@sanchuang 16:05  mysql&gt;insert into student(id,name) value(1,"cali");
Query OK, 1 row affected (0.00 sec)

root@sanchuang 16:10  mysql&gt;select * from student;
+------+------+
| id   | name |
+------+------+
|    1 | cali |
+------+------+
1 row in set (0.00 sec)

```

**###################################################** 

### **知识点3：新建数据库操作**

#### 新建一个数据库

```
root@(none) 09:17  mysql&gt;create database wangsh;
Query OK, 1 row affected (0.00 sec)

root@(none) 09:21  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sanchuang          |
| student            |
| sys                |
| wangsh             |
+--------------------+
7 rows in set (0.00 sec)

```

**###################################################** 

#### 查看刚才创建的数据库的字符集结构

#### 方法1：直接输入语句 ** show create database wangsh;**

```
root@(none) 09:22  mysql&gt;show create database wangsh;
+----------+-----------------------------------------------------------------+
| Database | Create Database                                                 |
+----------+-----------------------------------------------------------------+
| wangsh   | CREATE DATABASE `wangsh` /*!40100 DEFAULT CHARACTER SET utf8 */ |
+----------+-----------------------------------------------------------------+
1 row in set (0.00 sec)

```

**###################################################** 

#### 方法2：进入新建库对应的文件夹里面查看db.opt文件的内容也可以查看数据库的字符集内容

```
[root@localhost /]# cd /data/mysql/
[root@localhost mysql]# ls
auto.cnf         ib_buffer_pool  localhost.localdomain.err  performance_schema  server-key.pem
ca-key.pem       ibdata1         localhost.localdomain.pid  private_key.pem     student
ca.pem           ib_logfile0     mysql                      public_key.pem      sys
client-cert.pem  ib_logfile1     mysql.sock                 sanchuang           wangsh
client-key.pem   ibtmp1          mysql.sock.lock            server-cert.pem
[root@localhost mysql]# cd wangsh/
[root@localhost wangsh]# ls
db.opt
[root@localhost wangsh]# cat db.opt 
default-character-set=utf8
default-collation=utf8_general_ci

```

**###################################################** 

#### show variables;**会将所有的变量都显示出来**

```
root@(none) 09:29  mysql&gt;show variables;

```

```
root@(none) 09:30  mysql&gt;show variables like "%character%";
+--------------------------+----------------------------------+
| Variable_name            | Value                            |
+--------------------------+----------------------------------+
| character_set_client     | utf8                             |
| character_set_connection | utf8                             |
| character_set_database   | utf8                             |
| character_set_filesystem | binary                           |
| character_set_results    | utf8                             |
| character_set_server     | utf8                             |
| character_set_system     | utf8                             |
| character_sets_dir       | /usr/local/mysql/share/charsets/ |
+--------------------------+----------------------------------+
8 rows in set (0.01 sec)

```

system  --&gt;mysql系统

server  --&gt; linux系统

character_set_database  --&gt;数据里的字符集

server  --&gt;system  --》database

**###################################################** 

#### **示例：删除数据库 drop database**

```
root@(none) 21:59  mysql&gt;drop database wangsh;
Query OK, 0 rows affected (0.01 sec)

root@(none) 21:59  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sanchuang          |
| student            |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

```

#### 将数据库删除以后，linux系统里面对应数据库的那个目录也会删除

```
[root@localhost mysql]# cd /data/mysql/
[root@localhost mysql]# ls | grep wangsh
[root@localhost mysql]# 

```

**###################################################** 

#### 库和表的关系

        库里有表，库里面包含表

        库：文件夹

        表：文件



**###################################################** 

### 新建表操作

```
root@wangsh 22:08  mysql&gt;use sanchuang;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
root@sanchuang 22:08  mysql&gt;create table wangsh.table1(id int,name varchar(20));
Query OK, 0 rows affected (0.01 sec)

root@sanchuang 22:09  mysql&gt;show tables in wangsh;
+------------------+
| Tables_in_wangsh |
+------------------+
| table1           |
+------------------+
1 row in set (0.00 sec)

```

**###################################################** 

#### 当一个表存在时，我们再次新建这个表名会报错

```
root@sanchuang 22:09  mysql&gt;create table wangsh.table1(id int,name varchar(20));
ERROR 1050 (42S01): Table 'table1' already exists

```

#### **但是我们可以加 if not exists 来解决这个问题**

**如果表已经存在，那么不报错，不存在则新建**

**有一条警告，可以用show warnings；来查看**

```
root@sanchuang 22:12  mysql&gt;create table if not exists wangsh.table1(id int,name varchar(20));
Query OK, 0 rows affected, 1 warning (0.00 sec)

root@sanchuang 22:12  mysql&gt;show warnings;
+-------+------+-------------------------------+
| Level | Code | Message                       |
+-------+------+-------------------------------+
| Note  | 1050 | Table 'table1' already exists |
+-------+------+-------------------------------+
1 row in set (0.00 sec)

```

**###################################################** 

#### **主键：表里面的一列或多列不能重复**

```
root@sanchuang 22:41  mysql&gt;create table t2(id int(4) not null primary key, name varchar(10) not null);
Query OK, 0 rows affected (0.01 sec)

root@sanchuang 22:41  mysql&gt;desc t2
    -&gt; ;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(4)      | NO   | PRI | NULL    |       |
| name  | varchar(10) | NO   |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.01 sec)

```

**###################################################** 

#### 查看表结构：

#### 方法1： **show create table t2;**

```
root@sanchuang 22:44  mysql&gt;show create table t2;
+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                         |
+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| t2    | CREATE TABLE `t2` (
  `id` int(4) NOT NULL,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+-------+--------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

```

#### 方法2： **desc t2;**

```
root@sanchuang 22:46  mysql&gt;desc t2;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(4)      | NO   | PRI | NULL    |       |
| name  | varchar(10) | NO   |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

```

**###################################################** 

### ** 存储引擎和字符集的捆绑问题**

字符集可以和库捆绑，也可以和表捆绑，但是存储引擎和表捆绑的，不是和库捆绑，因为库是一个文件夹，而表示文件，是存放在磁盘上面的

**###################################################** 

### **字符集的继承问题：**

**                                                          库  --  表   -- 字段 **

        如果不给字段，表指定字符集的话，它会自动继承，字段继承表，表继承库，如果指定则使用指定的字符集。

**###################################################** 

### **关系型数据库**

        Mysql，oracle， MSSQL，postgresql

### **非关系型数据库**

        redis，mongDB，TIDB，timeseriesDB

        非关系型数据库一般是 KEY：VALUE 键值对来存储，例如redis

**###################################################** 

### **结构化数据和非结构化数据**

        结构化数据一般是指关系型数据库表示和存储，可以用二维表来逻辑表达实现的数据

        非结构化数据顾名思义，就是没有固定结构的数据，包括所有格式的办公文档，文本，图片，XML，HTML，各类报表，等都属于非结构化数据，对于这类数据，我们一般直接整体进行存储，而且一般存储为二进制的数据格式。


