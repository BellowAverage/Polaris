
--- 
title:  PostgreSQL 学习笔记 
tags: []
categories: [] 

---
之前的话，MySQL 接触得稍微多一些，最近由于工作的原因，刚好以一个菜鸟的身份来学学 PostgreSQL。



### 常用快捷命令

其实用 \? 就可以把所有快捷命令及其解释就都显示出来了。

```
\?                      显示所有快捷命令及其注解
\l                      显示可用的数据库
\c &lt;database-name&gt;      进入具体的数据库
\d                      显示可用的数据表
\d &lt;table-name&gt;         查看表信息
\di                     查看数据库所有索引
\dv                     查看数据库所有视图
\du                     查看数据库所有角色
\h &lt;keyword&gt;            显示指定命令帮助信息
\q                      退出 psql 命令行
\x                      行/列 模式切换（类似于 sqlite 中的 .mode line 和 .mode column）
...
```

psql 命令参数

```
root@localhost ~# psql --help
psql is the PostgreSQL interactive terminal.

Usage:
  psql [OPTION]... [DBNAME [USERNAME]]

General options:
  -c, --command=COMMAND    run only single command (SQL or internal) and exit
  -d, --dbname=DBNAME      database name to connect to (default: "root")
  -f, --file=FILENAME      execute commands from file, then exit
  -l, --list               list available databases, then exit
  -v, --set=, --variable=NAME=VALUE
                           set psql variable NAME to VALUE
                           (e.g., -v ON_ERROR_STOP=1)
  -V, --version            output version information, then exit
  -X, --no-psqlrc          do not read startup file (~/.psqlrc)
  -1 ("one"), --single-transaction
                           execute as a single transaction (if non-interactive)
  -?, --help[=options]     show this help, then exit
      --help=commands      list backslash commands, then exit
      --help=variables     list special variables, then exit

Input and output options:
  -a, --echo-all           echo all input from script
  -b, --echo-errors        echo failed commands
  -e, --echo-queries       echo commands sent to server
  -E, --echo-hidden        display queries that internal commands generate
  -L, --log-file=FILENAME  send session log to file
  -n, --no-readline        disable enhanced command line editing (readline)
  -o, --output=FILENAME    send query results to file (or |pipe)
  -q, --quiet              run quietly (no messages, only query output)
  -s, --single-step        single-step mode (confirm each query)
  -S, --single-line        single-line mode (end of line terminates SQL command)

Output format options:
  -A, --no-align           unaligned table output mode
      --csv                CSV (Comma-Separated Values) table output mode
  -F, --field-separator=STRING
                           field separator for unaligned output (default: "|")
  -H, --html               HTML table output mode
  -P, --pset=VAR[=ARG]     set printing option VAR to ARG (see \pset command)
  -R, --record-separator=STRING
                           record separator for unaligned output (default: newline)
  -t, --tuples-only        print rows only
  -T, --table-attr=TEXT    set HTML table tag attributes (e.g., width, border)
  -x, --expanded           turn on expanded table output
  -z, --field-separator-zero
                           set field separator for unaligned output to zero byte
  -0, --record-separator-zero
                           set record separator for unaligned output to zero byte

Connection options:
  -h, --host=HOSTNAME      database server host or socket directory (default: "local socket")
  -p, --port=PORT          database server port (default: "5432")
  -U, --username=USERNAME  database user name (default: "root")
  -w, --no-password        never prompt for password
  -W, --password           force password prompt (should happen automatically)

```

```
psql -d public -U postgres -p 5450 -c "delete from license"
```

### 安装

我自己是 centos7.6 虚拟机，通过选择系统和版本，官方就会提供了一个 yum 安装的命令：

```
sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo yum install -y postgresql13-server
sudo /usr/pgsql-13/bin/postgresql-13-setup initdb
sudo systemctl enable postgresql-13
sudo systemctl start postgresql-13

```

执行一下就差不多了，安装完毕后，系统会创建一个数据库超级用户 postgres，密码为空。

```
root@master ~# psql --version
psql (PostgreSQL) 9.2.24

root@master ~# cat /etc/passwd | grep postgres
postgres:x:26:26:PostgreSQL Server:/var/lib/pgsql:/bin/bash

```

这时使用以下命令进入 postgres 命令行了。

```
root@master ~# sudo -i -u postgres
-bash-4.2$ pwd
/var/lib/pgsql
-bash-4.2$ psql
psql (9.2.24, server 13.7)
WARNING: psql version 9.2, server version 13.0.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(3 rows)


```

### 修改密码

修改数据库用户 postgres 的密码

```
postgres=# ALTER USER postgres WITH PASSWORD 'postgres';

```

### 配置允许远程连接

#### 进入安装目录

如果是默认安装的话，路径和下面的应该差不多，后边按照实际版本指定一下路径就好了。

```
root@master ~# cd /var/lib/pgsql/13/data
root@master /v/l/p/1/data# pwd
/var/lib/pgsql/13/data

```

#### 编辑 pg_hba.conf

添加一行

<img alt="" height="234" src="https://img-blog.csdnimg.cn/617d9adbfc8b4a5c93b469c9329056a4.png" width="625">

#### 编辑 postgresql.conf

<img alt="" height="132" src="https://img-blog.csdnimg.cn/350154a8e51a46a0bac8a635089c547b.png" width="544">

#### 防火墙开放 5432 端口

```
firewall-cmd --zone=public --add-port=5432/tcp --permanent
firewall-cmd --reload
```

#### 重启 pgsql 数据库服务

```
systemctl restart postgresql-13.service
```

#### Navicat 连接测试

<img alt="" height="800" src="https://img-blog.csdnimg.cn/cdfa4d031d0846cf86304bcf3d420250.png" width="708">

### 数据库创建（create database &lt;dbname&gt;;）

在 postgres 命令行的话，就用 create database &lt;dbname&gt;; 创建数据库（记得加分号）。

```
postgres=# CREATE DATABASE looking;
CREATE DATABASE
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 looking   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(4 rows)

```

在 linux 命令行的话，可以使用 createdb 命令创建数据库。 

```
-bash-4.2$ createdb world
-bash-4.2$ psql
psql (9.2.24, server 13.7)
WARNING: psql version 9.2, server version 13.0.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 hello     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 looking   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 world     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
(6 rows)

```

postgres 的默认端口是 5432。

```
-bash-4.2$ cat /etc/services | grep 5432
postgres        5432/tcp        postgresql      # POSTGRES
postgres        5432/udp        postgresql      # POSTGRES

```

创建数据库的时候可以使用 -p 命令指定其他端口。

```
createdb -h localhost -p 5435 -U postgres looking
```

### 选择数据库（\c &lt;dbname&gt;）

```
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 hello     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 looking   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 world     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
(6 rows)

postgres=# \c looking
psql (9.2.24, server 13.7)
WARNING: psql version 9.2, server version 13.0.
         Some psql features might not work.
You are now connected to database "looking" as user "postgres".

```

### 删除数据库（drop database &lt;dbname&gt;;）

```
postgres=# drop database world;
DROP DATABASE

```

和创建数据库一样，也可以在 linux 命令行使用 dropdb 删除数据库。

```
-bash-4.2$ dropdb hello
-bash-4.2$ psql
psql (9.2.24, server 13.7)
WARNING: psql version 9.2, server version 13.0.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 looking   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(4 rows)

```

### 创建表（create table &lt;tablename&gt;;）

数据表的创建和 mysql 的语法差不多，创建完以后可以用 \d 查看已创建的数据表信息。

```
looking=# drop table company;
DROP TABLE
looking=# \d
No relations found.
looking=# CREATE TABLE COMPANY(
looking(#    ID INT PRIMARY KEY     NOT NULL,
looking(#    NAME           TEXT    NOT NULL,
looking(#    AGE            INT     NOT NULL,
looking(#    ADDRESS        CHAR(50),
looking(#    SALARY         REAL
looking(# );
CREATE TABLE
looking=# CREATE TABLE DEPARTMENT(
looking(#    ID INT PRIMARY KEY      NOT NULL,
looking(#    DEPT           CHAR(50) NOT NULL,
looking(#    EMP_ID         INT      NOT NULL
looking(# );
CREATE TABLE
looking=# \d
           List of relations
 Schema |    Name    | Type  |  Owner   
--------+------------+-------+----------
 public | company    | table | postgres
 public | department | table | postgres
(2 rows)

```

### 删除表（drop table &lt;tablename&gt;;）

PostgreSQL 使用 DROP TABLE 语句来删除表格，包含表格数据、规则、触发器等。

```
looking=# \d
           List of relations
 Schema |    Name    | Type  |  Owner   
--------+------------+-------+----------
 public | company    | table | postgres
 public | department | table | postgres
(2 rows)

looking=# drop table company, department;
DROP TABLE
looking=# \d
No relations found.

```

### 模式

PostgreSQL 模式（SCHEMA）可以看着是一个表的集合。一个模式可以包含视图、索引、数据类型、函数和操作符等。相同的对象名称可以被用于不同的模式中而不会出现冲突，类似数据库里边的**命名空间**。

```
looking=# create schema myschema;
CREATE SCHEMA
looking=# drop schema myschema;
DROP SCHEMA

```

### 插入数据

```
looking=# CREATE TABLE COMPANY(
looking(#    ID INT PRIMARY KEY     NOT NULL,
looking(#    NAME           TEXT    NOT NULL,
looking(#    AGE            INT     NOT NULL,
looking(#    ADDRESS        CHAR(50),
looking(#    SALARY         REAL,
looking(#    JOIN_DATE      DATE
looking(# );
CREATE TABLE
looking=# \d
          List of relations
 Schema |  Name   | Type  |  Owner   
--------+---------+-------+----------
 public | company | table | postgres
(1 row)

looking=# INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY,JOIN_DATE) VALUES (1, 'Paul', 32, 'California', 20000.00,'2001-07-13');
INSERT 0 1
looking=# INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,JOIN_DATE) VALUES (2, 'Allen', 25, 'Texas', '2007-12-13');
INSERT 0 1
looking=# INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY,JOIN_DATE) VALUES (3, 'Teddy', 23, 'Norway', 20000.00, DEFAULT );
INSERT 0 1
looking=# INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY,JOIN_DATE) VALUES
 (4, 'Mark', 25, 'Rich-Mond ', 65000.00, '2007-12-13' ),
 (5, 'David', 27, 'Texas', 85000.00, '2007-12-13');
INSERT 0 2

```

### 查询数据

```
looking=# select * from company;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  2 | Allen |  25 | Texas                                              |        | 2007-12-13
  3 | Teddy |  23 | Norway                                             |  20000 | 
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
(5 rows)

```

### 运算符

PostgreSQL 运算符是一个保留关键字或字符，一般用在 WHERE 语句中，作为过滤条件。假设变量 a 为 2，变量 b 为 3，则：
|运算符|描述|实例
|+|加|a + b 结果为 5
|-|减|a - b 结果为 -1
|*|乘|a * b 结果为 6
|/|除|b / a 结果为 1
|%|模（取余）|b % a 结果为 1
|^|指数|a ^ b 结果为 8
||/|平方根||/ 25.0 结果为 5
|||/|立方根|||/ 27.0 结果为 3
|!|阶乘|5 ! 结果为 120
|!!|阶乘（前缀操作符）|!! 5 结果为 120

```
looking=# select 5!;
 ?column? 
----------
      120
(1 row)

```

### 表达式

#### 布尔表达式

```
looking=# SELECT * FROM COMPANY WHERE SALARY = 20000;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  3 | Teddy |  23 | Norway                                             |  20000 | 
(2 rows)

```

#### 数字表达式

```
looking=# SELECT (17 + 6) AS ADDITION ;
 addition 
----------
       23
(1 row)

```

```
looking=#  SELECT COUNT(*) AS "RECORDS" FROM COMPANY;
 RECORDS 
---------
       5
(1 row)

```

#### 日期表达式

```
looking=# SELECT CURRENT_TIMESTAMP;
       current_timestamp       
-------------------------------
 2022-06-07 18:19:20.020001+08
(1 row)

```

### 常规操作

我自己大概看了一下，这些常规操作和 MySQL 好像没太大区别，至少从表象上来看是这样的，所以就不多赘述了，简单列几个例子看看就好。

#### WHERE

可以在 WHERE 子句中使用比较运算符或逻辑运算符，例如 &gt;, &lt;, =, LIKE, NOT 等等。

```
looking=# SELECT * FROM COMPANY WHERE SALARY &gt; 30000;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
(2 rows)

```

#### AND / OR

```
looking=# SELECT * FROM COMPANY WHERE AGE &gt;=25 AND SALARY &gt; 65000;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
(1 row)

looking=# SELECT * FROM COMPANY WHERE AGE &gt;=25 OR SALARY &gt; 65000;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  2 | Allen |  25 | Texas                                              |        | 2007-12-13
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
(4 rows)

```

#### UPDATE

```
looking=# SELECT * FROM COMPANY;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  2 | Allen |  25 | Texas                                              |        | 2007-12-13
  3 | Teddy |  23 | Norway                                             |  20000 | 
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
(5 rows)

looking=# UPDATE COMPANY SET SALARY = 15000 WHERE ID=3;
UPDATE 1
looking=# SELECT * FROM COMPANY;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  2 | Allen |  25 | Texas                                              |        | 2007-12-13
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
  3 | Teddy |  23 | Norway                                             |  15000 | 
(5 rows)

```

#### DELETE

```
looking=# SELECT * FROM COMPANY;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  2 | Allen |  25 | Texas                                              |        | 2007-12-13
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
  3 | Teddy |  23 | Norway                                             |  15000 | 
(5 rows)

looking=# DELETE FROM COMPANY WHERE ID=2;
DELETE 1
looking=# SELECT * FROM COMPANY;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
  3 | Teddy |  23 | No
```

#### LIKE

在 PostgreSQL 中，主要有以下两种通配符：百分号 % （%通配任意个任意字符）和 下划线 _（_通配一个任意字符）。对于非文本类型的字段，记得通配字段后边要加上 ::text 将相应字段类型转换为字符串数据类型再进行匹配。

```
looking=# SELECT * FROM COMPANY WHERE AGE LIKE '3%';
ERROR:  operator does not exist: integer ~~ unknown
LINE 1: SELECT * FROM COMPANY WHERE AGE LIKE '3%';
                                        ^
HINT:  No operator matches the given name and argument types. You might need to add explicit type casts.
looking=# SELECT * FROM COMPANY WHERE AGE::text LIKE '3%';
 id | name | age |                      address                       | salary | join_date  
----+------+-----+----------------------------------------------------+--------+------------
  1 | Paul |  32 | California                                         |  20000 | 2001-07-13
(1 row)


looking=# SELECT * FROM COMPANY WHERE ADDRESS::text LIKE '_o%';
 id | name  | age |                      address                       | salary | join_date 
----+-------+-----+----------------------------------------------------+--------+-----------
  3 | Teddy |  23 | Norway                                             |  15000 | 
(1 row)

looking=# SELECT * FROM COMPANY WHERE ADDRESS::text LIKE '%o%';
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  3 | Teddy |  23 | Norway                                             |  15000 | 
(3 rows)

```

#### LIMIT

```
looking=# SELECT * FROM COMPANY;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
  3 | Teddy |  23 | Norway                                             |  15000 | 
(4 rows)

looking=# SELECT * FROM COMPANY LIMIT 2;
 id | name | age |                      address                       | salary | join_date  
----+------+-----+----------------------------------------------------+--------+------------
  1 | Paul |  32 | California                                         |  20000 | 2001-07-13
  4 | Mark |  25 | Rich-Mond                                          |  65000 | 2007-12-13
(2 rows)

```

#### ORDER BY

```
looking=# SELECT * FROM COMPANY;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
  3 | Teddy |  23 | Norway                                             |  15000 | 
(4 rows)

looking=# SELECT * FROM COMPANY ORDER BY ID;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  3 | Teddy |  23 | Norway                                             |  15000 | 
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
(4 rows)

looking=# SELECT * FROM COMPANY ORDER BY SALARY;
 id | name  | age |                      address                       | salary | join_date  
----+-------+-----+----------------------------------------------------+--------+------------
  3 | Teddy |  23 | Norway                                             |  15000 | 
  1 | Paul  |  32 | California                                         |  20000 | 2001-07-13
  4 | Mark  |  25 | Rich-Mond                                          |  65000 | 2007-12-13
  5 | David |  27 | Texas                                              |  85000 | 2007-12-13
(4 rows)

```

#### GROUP BY

```
looking=# SELECT * FROM COMPANY;
 id | name  | age |                      address                       | salary 
----+-------+-----+----------------------------------------------------+--------
  1 | Paul  |  32 | California                                         |  20000
  2 | Allen |  25 | Texas                                              |  15000
  3 | Teddy |  23 | Norway                                             |  20000
  4 | Mark  |  25 | Rich-Mond                                          |  65000
  5 | David |  27 | Texas                                              |  85000
  6 | Kim   |  22 | South-Hall                                         |  45000
  7 | James |  24 | Houston                                            |  10000
  8 | Paul  |  24 | Houston                                            |  20000
  9 | James |  44 | Norway                                             |   5000
 10 | James |  45 | Texas                                              |   5000
(10 rows)

looking=# SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME ORDER BY NAME;
 name  |  sum  
-------+-------
 Allen | 15000
 David | 85000
 James | 20000
 Kim   | 45000
 Mark  | 65000
 Paul  | 40000
 Teddy | 20000
(7 rows)
looking=# SELECT ADDRESS, SUM(SALARY) FROM COMPANY GROUP BY ADDRESS ORDER BY ADDRESS;
                      address                       |  sum   
----------------------------------------------------+--------
 California                                         |  20000
 Houston                                            |  30000
 Norway                                             |  25000
 Rich-Mond                                          |  65000
 South-Hall                                         |  45000
 Texas                                              | 105000
(6 rows)

```

#### HAVING

```
looking=# select * from company;
                                    LOOKING
 id | name  | age |                      address                       | salary 
----+-------+-----+----------------------------------------------------+--------
  1 | Paul  |  32 | California                                         |  20000
  2 | Allen |  25 | Texas                                              |  15000
  3 | Teddy |  23 | Norway                                             |  20000
  4 | Mark  |  25 | Rich-Mond                                          |  65000
  5 | David |  27 | Texas                                              |  85000
  6 | Kim   |  22 | South-Hall                                         |  45000
  7 | James |  24 | Houston                                            |  10000
  8 | Paul  |  24 | Houston                                            |  20000
  9 | James |  44 | Norway                                             |   5000
 10 | James |  45 | Texas                                              |   5000
(10 rows)

looking=# SELECT NAME FROM COMPANY GROUP BY name HAVING count(name) &gt; 2;
LOOKING
 name  
-------
 James
(1 row)

```

#### DISTINCT

```
looking=# SELECT NAME FROM COMPANY;
LOOKING
 name  
-------
 Paul
 Allen
 Teddy
 Mark
 David
 Kim
 James
 Paul
 James
 James
(10 rows)

looking=# SELECT DISTINCT NAME FROM COMPANY;
LOOKING
 name  
-------
 Teddy
 David
 Paul
 Kim
 Mark
 Allen
 James
(7 rows)

```

### 约束

#### NOT NULL

```
CREATE TABLE COMPANY1(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```

#### UNIQUE

```
CREATE TABLE COMPANY3(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL UNIQUE,
   ADDRESS        CHAR(50),
   SALARY         REAL    DEFAULT 50000.00
);
```

#### PRIMARY KEY

```
CREATE TABLE COMPANY4(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```

#### FOREIGN KEY

```
CREATE TABLE COMPANY6(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```

```
CREATE TABLE DEPARTMENT1(
   ID INT PRIMARY KEY      NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      references COMPANY6(ID)
);
```

#### CHECK

```
CREATE TABLE COMPANY5(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL    CHECK(SALARY &gt; 0)
);
```

#### EXCLUSION

EXCLUSION 约束确保如果使用指定的运算符在指定列或表达式上比较任意两行，至少其中一个运算符比较将返回 false 或 null。

```
CREATE TABLE COMPANY7(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT,
   AGE            INT  ,
   ADDRESS        CHAR(50),
   SALARY         REAL,
   EXCLUDE USING gist
   (NAME WITH =,  -- 如果满足 NAME 相同，AGE 不相同则不允许插入，否则允许插入
   AGE WITH &lt;&gt;)   -- 其比较的结果是如果整个表边式返回 true，则不允许插入，否则允许
);
```

#### 删除约束

```
ALTER TABLE table_name DROP CONSTRAINT some_name;
```

### 连接

在 PostgreSQL 中，JOIN 有五种连接类型：
- CROSS JOIN ：交叉连接- INNER JOIN：内连接- LEFT OUTER JOIN：左外连接- RIGHT OUTER JOIN：右外连接- FULL OUTER JOIN：全外连接
### UNION

UNION 操作符用于合并两个或多个 SELECT 语句的结果集。UNION 内部的每个 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每个 SELECT 语句中的列的顺序必须相同。

### NULL

NULL 值代表遗漏的未知数据。默认地，表的列可以存放 NULL 值。NOT NULL 表示强制字段始终包含值。如果不向字段添加值，就无法插入新记录或者更新记录。具有 NULL 值的字段表示在创建记录时可以留空。NULL 值在查询时可能会导致一些问题，因为一个未知的值去与其他任何值比较，结果永远是未知的。另外无法比较 NULL 和 0，因为它们是不等价的。

```
looking=# select * from company;
                                    LOOKING
 id | name  | age |                      address                       | salary 
----+-------+-----+----------------------------------------------------+--------
  1 | Paul  |  32 | California                                         |  20000
  2 | Allen |  25 | Texas                                              |  15000
  3 | Teddy |  23 | Norway                                             |  20000
  4 | Mark  |  25 | Rich-Mond                                          |  65000
  5 | David |  27 | Texas                                              |  85000
  6 | Kim   |  22 | South-Hall                                         |  45000
  7 | James |  24 | Houston                                            |  10000
  8 | Paul  |  24 | Houston                                            |  20000
  9 | James |  44 | Norway                                             |   5000
 10 | James |  45 | Texas                                              |   5000
(10 rows)

looking=# UPDATE COMPANY SET ADDRESS = NULL, SALARY = NULL where ID IN(6,7);
UPDATE 2
looking=# select * from company;
                                    LOOKING
 id | name  | age |                      address                       | salary 
----+-------+-----+----------------------------------------------------+--------
  1 | Paul  |  32 | California                                         |  20000
  2 | Allen |  25 | Texas                                              |  15000
  3 | Teddy |  23 | Norway                                             |  20000
  4 | Mark  |  25 | Rich-Mond                                          |  65000
  5 | David |  27 | Texas                                              |  85000
  8 | Paul  |  24 | Houston                                            |  20000
  9 | James |  44 | Norway                                             |   5000
 10 | James |  45 | Texas                                              |   5000
  6 | Kim   |  22 |                                                    |       
  7 | James |  24 |                                                    |       
(10 rows)

```

#### IS NULL

```
looking=# select * from company WHERE SALARY IS NULL;
               LOOKING
 id | name  | age | address | salary 
----+-------+-----+---------+--------
  6 | Kim   |  22 |         |       
  7 | James |  24 |         |       
(2 rows)

```

#### IS NOT NULL

```
looking=# select * from company WHERE SALARY IS NOT NULL;
                                    LOOKING
 id | name  | age |                      address                       | salary 
----+-------+-----+----------------------------------------------------+--------
  1 | Paul  |  32 | California                                         |  20000
  2 | Allen |  25 | Texas                                              |  15000
  3 | Teddy |  23 | Norway                                             |  20000
  4 | Mark  |  25 | Rich-Mond                                          |  65000
  5 | David |  27 | Texas                                              |  85000
  8 | Paul  |  24 | Houston                                            |  20000
  9 | James |  44 | Norway                                             |   5000
 10 | James |  45 | Texas                                              |   5000
(8 rows)

```

### 别名

我们可以用 SQL 重命名一张表或者一个字段的名称，这个名称就叫着该表或该字段的别名。创建别名是为了让表名或列名的可读性更强。SQL 中 使用 **AS** 来创建别名。

#### 表别名

```
SELECT C.ID, C.NAME, C.AGE, D.DEPT FROM COMPANY AS C, DEPARTMENT AS D WHERE  C.ID = D.EMP_ID;
```

#### 列别名 

```
SELECT C.ID AS COMPANY_ID, C.NAME AS COMPANY_NAME, C.AGE, D.DEPT  FROM COMPANY AS C, DEPARTMENT AS D WHERE  C.ID = D.EMP_ID;
```

### 触发器

触发器是数据库的回调函数，它会在指定的数据库事件发生时自动执行/调用。

#### 语法

```
CREATE TRIGGER trigger_name [BEFORE|AFTER] [INSERT|DELETE|UPDATE]
ON table_name
[
 -- 触发器逻辑....
];
```

```
CREATE TRIGGER trigger_name [BEFORE|AFTER] [INSERT|DELETE|UPDATE] OF column_name
ON table_name
[
 -- 触发器逻辑....
];
```

#### 实例

创建表

```
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);

CREATE TABLE AUDIT(
   EMP_ID INT NOT NULL,
   ENTRY_DATE TEXT NOT NULL
);
```

创建触发器 

```
looking=# CREATE OR REPLACE FUNCTION auditlogfunc() RETURNS TRIGGER AS $example_table$
looking$#    BEGIN
looking$#       INSERT INTO AUDIT(EMP_ID, ENTRY_DATE) VALUES (new.ID, current_timestamp);
looking$#       RETURN NEW;
looking$#    END;
looking$# $example_table$ LANGUAGE plpgsql;
CREATE FUNCTION

looking=# CREATE TRIGGER example_trigger AFTER INSERT ON COMPANY FOR EACH ROW EXECUTE PROCEDURE auditlogfunc();
CREATE TRIGGER

```

测试触发器 

```
looking=# INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 );
INSERT 0 1
looking=# select * from audit;
                LOOKING
 emp_id |          entry_date           
--------+-------------------------------
      1 | 2022-06-10 15:01:53.225493+08
(1 row)

```

#### 列举触发器

```
looking=# select * from pg_trigger;
                                                                                                                  LOOKING
  oid  | tgrelid | tgparentid |     tgname      | tgfoid | tgtype | tgenabled | tgisinternal | tgconstrrelid | tgconstrindid | tgconstraint | tgdeferrable | tginitdeferred | tgnargs | tgattr | tgargs | tgqual | tgoldtable | tgnewtable 
-------+---------+------------+-----------------+--------+--------+-----------+--------------+---------------+---------------+--------------+--------------+----------------+---------+--------+--------+--------+------------+------------
 16448 |   16433 |          0 | example_trigger |  16447 |      5 | O         | f            |             0 |             0 |            0 | f            | f              |       0 |        | \x     |        |            | 
(1 row)

```

```

looking=# SELECT tgname FROM pg_trigger, pg_class WHERE tgrelid=pg_class.oid AND relname='company';
     LOOKING
     tgname      
-----------------
 example_trigger
(1 row)


```

#### 删除触发器

```
looking=# DROP TRIGGER EXAMPLE_TRIGGER ON COMPANY;
DROP TRIGGER

```

### 索引

索引必须是在 WHERE 子句的过滤条件中使用非常频繁的列。

#### 语法

```
CREATE INDEX index_name ON table_name;
```

#### 单列索引

```
CREATE INDEX index_name ON table_name (column_name);
```

#### 组合索引

```
CREATE INDEX index_name ON table_name (column1_name, column2_name);
```

#### 唯一索引

局部索引 是在表的子集上构建的索引；子集由一个条件表达式上定义。索引只包含满足条件的行。

```
CREATE UNIQUE INDEX index_name ON table_name (column_name);
```

#### 局部索引

```
CREATE INDEX index_name ON table_name (conditional_expression);
```

#### 隐式索引

隐式索引 是在创建对象时，由数据库服务器自动创建的索引。索引自动创建为主键约束和唯一约束。

#### 查看索引

查看表索引

```
\d &lt;tablename&gt;
```

 查看数据库所有索引

```
\di
```

#### 删除索引

```
DROP INDEX index_name;
```

#### 使用准则

使用索引时，需要考虑下列准则：
- 索引不应该使用在较小的表上。- 索引不应该使用在有频繁的大批量的更新或插入操作的表上。- 索引不应该使用在含有大量的 NULL 值的列上。- 索引不应该使用在频繁更新操作的列上。
### ALTER TABLE

#### 语法

用 ALTER TABLE 在一张已存在的表上添加列的语法如下：

```
ALTER TABLE table_name ADD column_name datatype;
```

在一张已存在的表上 DROP COLUMN（删除列），语法如下：

```
ALTER TABLE table_name DROP COLUMN column_name;
```

修改表中某列的 DATA TYPE（数据类型），语法如下：

```
ALTER TABLE table_name ALTER COLUMN column_name TYPE datatype;
```

给表中某列添加 NOT NULL 约束，语法如下：

```
ALTER TABLE table_name ALTER column_name datatype NOT NULL;
```

给表中某列 ADD UNIQUE CONSTRAINT（ 添加 UNIQUE 约束），语法如下：

```
ALTER TABLE table_name ADD CONSTRAINT MyUniqueConstraint UNIQUE(column1, column2...);
```

给表中 ADD CHECK CONSTRAINT（添加 CHECK 约束），语法如下：

```
ALTER TABLE table_name ADD CONSTRAINT MyUniqueConstraint CHECK (CONDITION);
```

给表 ADD PRIMARY KEY（添加主键），语法如下：

```
ALTER TABLE table_name ADD CONSTRAINT MyPrimaryKey PRIMARY KEY (column1, column2...);
```

DROP CONSTRAINT （删除约束），语法如下：

```
ALTER TABLE table_name DROP CONSTRAINT MyUniqueConstraint;
```

DROP PRIMARY KEY （删除主键），语法如下：

```
ALTER TABLE table_name DROP CONSTRAINT MyPrimaryKey;
```

#### 实例

添加列：

```
looking=# select * from company;
                                    LOOKING
 id | name | age |                      address                       | salary 
----+------+-----+----------------------------------------------------+--------
  1 | Paul |  32 | California                                         |  20000
(1 row)

looking=# alter table company add gender char(1);
ALTER TABLE
looking=# select * from company;
                                        LOOKING
 id | name | age |                      address                       | salary | gender 
----+------+-----+----------------------------------------------------+--------+--------
  1 | Paul |  32 | California                                         |  20000 | 
(1 row)

```

删除列：

```
looking=# select * from company;
                                        LOOKING
 id | name | age |                      address                       | salary | gender 
----+------+-----+----------------------------------------------------+--------+--------
  1 | Paul |  32 | California                                         |  20000 | 
(1 row)

looking=# alter table company drop gender;
ALTER TABLE
looking=# select * from company;
                                    LOOKING
 id | name | age |                      address                       | salary 
----+------+-----+----------------------------------------------------+--------
  1 | Paul |  32 | California                                         |  20000
(1 row)

```

添加和删除 NOT NULL 约束 

```
looking=# alter table company alter column salary set not null;
ALTER TABLE
looking=# alter table company alter column salary drop not null;
ALTER TABLE

```

### TRUNCATE TABLE

TRUNCATE TABLE 用于删除表的数据，但不删除表结构，DELETE 也可以删除表数据，但是它会扫描表，所以速度比 TRUNCATE 慢。TRUNCATE TABLE 可以立即释放表空间，而不需要后续 VACUUM 操作（与 SQLite 的 VACUUM 操作类似），这在大型表上非常有用。也可以用 DROP TABLE 删除表，但是这个命令会连表的结构一起删除，如果想插入数据，需要重新建立这张表。

#### DELETE

```
looking=# delete from company;
DELETE 1

```

#### TRUNCATE

```
looking=# truncate table company;
TRUNCATE TABLE

```

#### DROP

```
looking=# drop table company;
DROP TABLE

```

### 视图

同 MySQL。

### 事务
- **BEGIN** 或 **BEGIN TRANSACTION **开始一个事务- **ROLLBACK** 事务回滚- **COMMIT** 或 **END TRANSACTION **事务确认
### 锁

```
looking=# begin;
BEGIN
looking=# LOCK TABLE company IN ACCESS EXCLUSIVE MODE;
LOCK TABLE
looking=# do something on company;
looking=# commit;
COMMIT

```

上面的消息指示表被锁定，直到事务结束，并且要完成事务，您必须回滚或提交事务。

### 子查询

也叫嵌套查询，同 MySQL。

#### SELECT

```
INSERT INTO COMPANY_BKP SELECT * FROM COMPANY  WHERE ID IN (SELECT ID FROM COMPANY) ;
```

#### UPDATE

```
UPDATE COMPANY SET SALARY = SALARY * 0.50 WHERE AGE IN (SELECT AGE FROM COMPANY_BKP WHERE AGE &gt;= 35 );  -- 薪资减半？
```

#### DELETE

```
DELETE FROM COMPANY WHERE AGE IN (SELECT AGE FROM COMPANY_BKP WHERE AGE &gt; 35 ); -- 裁员？
```

### AUTO INCREMENT

#### MySQL

```
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

#### PostgreSQL

```
CREATE TABLE COMPANY(
   ID  SERIAL PRIMARY KEY,
   NAME           TEXT      NOT NULL,
   AGE            INT       NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```

SMALLSERIAL、SERIAL 和 BIGSERIAL 范围：

|伪类型|存储大小|范围
|------
|`SMALLSERIAL`|2字节|1 到 32,767
|`SERIAL`|4字节|1 到 2,147,483,647
|`BIGSERIAL`|8字节|1 到 922,337,2036,854,775,807
