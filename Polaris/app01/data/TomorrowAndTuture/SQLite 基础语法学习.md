
--- 
title:  SQLite 基础语法学习 
tags: []
categories: [] 

---
SQLite 是一个进程内的库，实现了自给自足的、无服务器的、零配置的、事务性的 SQL 数据库引擎。它是一个零配置的数据库，这意味着与其他数据库不一样，您不需要在系统中配置。

就像其他数据库，SQLite 引擎不是一个独立的进程，可以按应用程序需求进行静态或动态连接。SQLite 直接访问其存储文件。据说 SQLite 的语法和 MySQL 的大部分是一样的，而且从 Lite 的后缀可以看出，这应该像是一个 Mini 版本的 MySQL。虽说如此，我们还是来看看它和 MySQL 有哪些区别吧。

### 进入数据库命令行

```
[root@master ~]# sqlite3
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite&gt; 

```

### 语句语法

所有的 SQLite 语句可以以任何关键字开始，如 SELECT、INSERT、UPDATE、DELETE、ALTER、DROP 等，所有的语句以分号 ; 结束。

### 数据库备份和恢复

```
备份数据库：sqlite3 test.db ".dump" &gt; test.sql
恢复数据库：sqlite3 test.db &lt; test.sql

备份数据库：sqlite3 test.db ".dump" | sqlite3 test_bak.db
恢复数据库：sqlite3 test_bak.db ".dump" | sqlite3 test.db
```

将当前数据库备份成数据库文件 

```
sqlite&gt; .backup test.db
```

 从数据库文件进行恢复

```
sqlite&gt; .restore test.db
```

### 压缩数据库

SQLite 采用变长记录存储，当你从 Sqlite 删除数据后，未使用的磁盘空间被添加到一个内在的 “空闲列表” 中用于存储你下次插入的数据，用于提高效率，磁盘空间并没有丢失，但也不向操作系统返回磁盘空间，这就导致删除数据乃至清空数据库后，数据库文件大小还是没有任何变化，可以使用 vacuum 命令对数据库文件重新进行空间压缩整理。

```
sqlite&gt; vacuum;
```

### 创建数据库

```
[root@master ~]# sqlite3
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite&gt; .databases
main: 
sqlite&gt; .open test.db
sqlite&gt; .databases
main: /root/test.db
sqlite&gt; .quit

```

### 附加数据库

有点类似于 MySQL 的 use database; 命令

```
[root@master SQLite]# sqlite3
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite&gt; .open test.db
sqlite&gt; .open testDB.db
sqlite&gt; .database
main: /root/SQLite/testDB.db
sqlite&gt; ATTACH DATABASE 'testDB.db' as 'TEST';
sqlite&gt; .database
main: /root/SQLite/testDB.db
TEST: /root/SQLite/testDB.db

```

### 分离数据库

```
sqlite&gt; .database
main: /root/SQLite/testDB.db
TEST: /root/SQLite/testDB.db
sqlite&gt; detach database TEST;
sqlite&gt; .database
main: /root/SQLite/testDB.db

```

### 创建数据表

```
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL    
);
CREATE TABLE DEPARTMENT(
   ID INT PRIMARY KEY      NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      NOT NULL
);
------------------------------------------------------------

sqlite&gt; CREATE TABLE COMPANY(
   ...&gt;    ID INT PRIMARY KEY     NOT NULL,
   ...&gt;    NAME           TEXT    NOT NULL,
   ...&gt;    AGE            INT     NOT NULL,
   ...&gt;    ADDRESS        CHAR(50),
   ...&gt;    SALARY         REAL
   ...&gt; );
sqlite&gt; CREATE TABLE DEPARTMENT(
   ...&gt;    ID INT PRIMARY KEY      NOT NULL,
   ...&gt;    DEPT           CHAR(50) NOT NULL,
   ...&gt;    EMP_ID         INT      NOT NULL
   ...&gt; );
sqlite&gt; .tables
COMPANY     DEPARTMENT
sqlite&gt; .schema company
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);

```

### 删除数据表

```
sqlite&gt; .tables
COMPANY     DEPARTMENT
sqlite&gt; drop table company;
sqlite&gt; .tables
DEPARTMENT

```

### 插入数据

```
sqlite&gt; INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
   ...&gt; VALUES (1, 'Paul', 32, 'California', 20000.00 );

sqlite&gt; INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
   ...&gt; VALUES (2, 'Allen', 25, 'Texas', 15000.00 );

sqlite&gt; INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
   ...&gt; VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );

sqlite&gt; INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
   ...&gt; VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );

sqlite&gt; INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
   ...&gt; VALUES (5, 'David', 27, 'Texas', 85000.00 );

sqlite&gt; INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
   ...&gt; VALUES (6, 'Kim', 22, 'South-Hall', 45000.00 );

sqlite&gt; INSERT INTO COMPANY VALUES (7, 'James', 24, 'Houston', 10000.00 );

```

### 查询数据表

```
sqlite&gt; 
sqlite&gt; .header on
sqlite&gt; .mode column
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          South-Hall  45000.0   
7           James       24          Houston     10000.0 

sqlite&gt; select id, name, salary from company;
ID          NAME        SALARY    
----------  ----------  ----------
1           Paul        20000.0   
2           Allen       15000.0   
3           Teddy       20000.0   
4           Mark        65000.0   
5           David       85000.0   
6           Kim         45000.0   
7           James       10000.0 

# 可自己设置列宽
sqlite&gt; .width 10, 20, 10
sqlite&gt; select id, name, salary from company;
ID          NAME                  SALARY    
----------  --------------------  ----------
1           Paul                  20000.0   
2           Allen                 15000.0   
3           Teddy                 20000.0   
4           Mark                  65000.0   
5           David                 85000.0   
6           Kim                   45000.0   
7           James                 10000.0  

sqlite&gt; .width 10, 20, 10
sqlite&gt; SELECT sql FROM sqlite_master WHERE type = 'table' AND tbl_name = 'COMPANY';
sql       
----------
CREATE TAB
sqlite&gt; .width on
sqlite&gt; SELECT sql FROM sqlite_master WHERE type = 'table' AND tbl_name = 'COMPANY';
sql                                                                                                                                                                                       
------------------------------------------------------------------------------------                                                                   
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL    
)
```

### 运算符



不用 .mode line 的时候，好像和 MySQL 的输出差不多，不过好像行模式确实很不错。

```
sqlite&gt; select 10 + 20;
10 + 20   
----------
30        
sqlite&gt; .mode line
sqlite&gt; select 10 + 20;
10 + 20 = 30

sqlite&gt; select * from company;
     ID = 1
   NAME = Paul
    AGE = 32
ADDRESS = California
 SALARY = 20000.0

     ID = 2
   NAME = Allen
    AGE = 25
ADDRESS = Texas
 SALARY = 15000.0

...

```

```
sqlite&gt; .mode column
sqlite&gt; select * from company;
ID          NAME                  AGE         ADDRESS     SALARY    
----------  --------------------  ----------  ----------  ----------
1           Paul                  32          California  20000.0   
2           Allen                 25          Texas       15000.0   
3           Teddy                 23          Norway      20000.0   
4           Mark                  25          Rich-Mond   65000.0   
5           David                 27          Texas       85000.0   
6           Kim                   22          South-Hall  45000.0   
7           James                 24          Houston     10000.0   
sqlite&gt; select * from company where salary=20000;
ID          NAME                  AGE         ADDRESS     SALARY    
----------  --------------------  ----------  ----------  ----------
1           Paul                  32          California  20000.0   
3           Teddy                 23          Norway      20000.0   
sqlite&gt; select * from company where salary&gt;50000;
ID          NAME                  AGE         ADDRESS     SALARY    
----------  --------------------  ----------  ----------  ----------
4           Mark                  25          Rich-Mond   65000.0   
5           David                 27          Texas       85000.0  
```

### 更新数据表

```
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          South-Hall  45000.0   
7           James       24          Houston     10000.0   
sqlite&gt; UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          Texas       45000.0   
7           James       24          Houston     10000.0 
```

### 删除数据

```
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          Texas       45000.0   
7           James       24          Houston     10000.0   
sqlite&gt; delete from company where id=7;
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          Texas       45000.0  
```

### like 子句

这个典型的和 MySQL 的 like 用法是一样的，就不哆嗦了。
|WHERE SALARY LIKE '200%'|查找以 200 开头的任意值
|WHERE SALARY LIKE '%200%'|查找任意位置包含 200 的任意值
|WHERE SALARY LIKE '_00%'|查找第二位和第三位为 00 的任意值
|WHERE SALARY LIKE '2_%_%'|查找以 2 开头，且长度至少为 3 个字符的任意值
|WHERE SALARY LIKE '%2'|查找以 2 结尾的任意值
|WHERE SALARY LIKE '_2%3'|查找第二位为 2，且以 3 结尾的任意值
|WHERE SALARY LIKE '2___3'|查找长度为 5 位数，且以 2 开头以 3 结尾的任意值

### glob 子句

我一般见到的 glob 竟然是在 ruby 的语法里边（不过话说回来，用法其实还真是差不多）：

```
返回一个数组，包含与指定的通配符模式 pat 匹配的文件名：

* - 匹配包含 null 字符串的任意字符串
** - 递归地匹配任意字符串
? - 匹配任意单个字符
[...] - 匹配封闭字符中的任意一个
{a,b...} - 匹配字符串中的任意一个
Dir["foo.*"] # 匹配 "foo.c"、 "foo.rb" 等等
Dir["foo.?"] # 匹配 "foo.c"、 "foo.h" 等等
```
|语句|描述
|WHERE SALARY GLOB '200*'|查找以 200 开头的任意值
|WHERE SALARY GLOB '*200*'|查找任意位置包含 200 的任意值
|WHERE SALARY GLOB '?00*'|查找第二位和第三位为 00 的任意值
|WHERE SALARY GLOB '2??'|查找以 2 开头，且长度至少为 3 个字符的任意值
|WHERE SALARY GLOB '*2'|查找以 2 结尾的任意值
|WHERE SALARY GLOB '?2*3'|查找第二位为 2，且以 3 结尾的任意值
|WHERE SALARY GLOB '2???3'|查找长度为 5 位数，且以 2 开头以 3 结尾的任意值

### limit 子句

```
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          Texas       45000.0   

sqlite&gt; select * from company limit 3;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   

sqlite&gt; select * from company limit 3 offset 2;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0 
```

### order by

```
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          Texas       45000.0   
sqlite&gt; select * from company order by salary;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
2           Allen       25          Texas       15000.0   
1           Paul        32          California  20000.0   
3           Teddy       23          Norway      20000.0   
6           Kim         22          Texas       45000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0 
```

### group by

```
INSERT INTO COMPANY VALUES (8, 'Paul', 24, 'Houston', 20000.00 );
INSERT INTO COMPANY VALUES (9, 'James', 44, 'Norway', 5000.00 );
INSERT INTO COMPANY VALUES (10, 'James', 45, 'Texas', 5000.00 );

sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          Texas       45000.0   
8           Paul        24          Houston     20000.0   
9           James       44          Norway      5000.0    
10          James       45          Texas       5000.0    
sqlite&gt; SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME;
NAME        SUM(SALARY)
----------  -----------
Allen       15000.0    
David       85000.0    
James       10000.0    
Kim         45000.0    
Mark        65000.0    
Paul        40000.0    
Teddy       20000.0  
```

### having 子句

在一个查询中，HAVING 子句必须放在 GROUP BY 子句之后，必须放在 ORDER BY 子句之前。

```
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          Texas       45000.0   
8           Paul        24          Houston     20000.0   
9           James       44          Norway      5000.0    
10          James       45          Texas       5000.0  
sqlite&gt; SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME;
NAME        SUM(SALARY)
----------  -----------
Allen       15000.0    
David       85000.0    
James       10000.0    
Kim         45000.0    
Mark        65000.0    
Paul        40000.0    
Teddy       20000.0    
sqlite&gt; SELECT NAME, SUM(SALARY) as TOTAL FROM COMPANY GROUP BY NAME having TOTAL &gt; 40000;
NAME        TOTAL     
----------  ----------
David       85000.0   
Kim         45000.0   
Mark        65000.0   
sqlite&gt; SELECT NAME, SUM(SALARY) as TOTAL FROM COMPANY GROUP BY NAME HAVING TOTAL &gt; 40000 ORDER BY TOTAL ASC;
NAME        TOTAL     
----------  ----------
Kim         45000.0   
Mark        65000.0   
David       85000.0 
```

### distinct

```
sqlite&gt; select name from company;
NAME      
----------
Paul      
Allen     
Teddy     
Mark      
David     
Kim       
Paul      
James     
James     
sqlite&gt; select distinct name from company;
NAME      
----------
Paul      
Allen     
Teddy     
Mark      
David     
Kim       
James 
```

### 字段约束

约束是在表的数据列上强制执行的规则。这些是用来限制可以插入到表中的数据类型。这确保了数据库中数据的准确性和可靠性。约束可以是列级或表级。列级约束仅适用于列，表级约束被应用到整个表。

以下是在 SQLite 中常用的约束。
-  **NOT NULL 约束**：确保某列不能有 NULL 值。 -  **DEFAULT 约束**：当某列没有指定值时，为该列提供默认值。 -  **UNIQUE 约束**：确保某列中的所有值是不同的。 -  **PRIMARY Key 约束**：唯一标识数据库表中的各行/记录。 -  **CHECK 约束**：CHECK 约束确保某列中的所有值满足一定条件。 
#### NOT NULL 约束

默认情况下，列可以保存 NULL 值。如果您不想某列有 NULL 值，那么需要在该列上定义此约束，指定在该列上不允许 NULL 值。NULL 与没有数据是不一样的，它代表着未知的数据。

```
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```



#### DEFAULT 约束 

DEFAULT 约束在 INSERT INTO 语句没有提供一个特定的值时，为列提供一个默认值。

```
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL    DEFAULT 50000.00
);
```

#### UNIQUE 约束

UNIQUE 约束防止在一个特定的列存在两个记录具有相同的值。在 COMPANY 表中，例如，您可能要防止两个或两个以上的人具有相同的年龄。

```
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL UNIQUE,
   ADDRESS        CHAR(50),
   SALARY         REAL    DEFAULT 50000.00
);
```

#### PRIMARY KEY 约束

```
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```

#### CHECK 约束

CHECK 约束启用输入一条记录要检查值的条件。如果条件值为 false，则记录违反了约束，且不能输入到表。

```
CREATE TABLE COMPANY3(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL    CHECK(SALARY &gt; 0)
);
```

#### 删除约束

SQLite 支持 ALTER TABLE 的有限子集。在 SQLite 中，ALTER TABLE 命令允许用户重命名表，或向现有表添加一个新的列。重命名列，删除一列，或从一个表中添加或删除约束都是不可能的。

### 触发器

```
sqlite&gt; CREATE TABLE AUDIT(
   ...&gt;     EMP_ID INT NOT NULL,
   ...&gt;     ENTRY_DATE TEXT NOT NULL
   ...&gt; );
sqlite&gt; CREATE TRIGGER audit_log AFTER INSERT 
   ...&gt; ON COMPANY
   ...&gt; BEGIN
   ...&gt;    INSERT INTO AUDIT(EMP_ID, ENTRY_DATE) VALUES (new.ID, datetime('now'));
   ...&gt; END;

sqlite&gt; select * from audit;
sqlite&gt; INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
   ...&gt; VALUES (11, 'Paul', 32, 'California', 20000.00 );
sqlite&gt; select * from audit;
11          2021-01-22 06:35:27
sqlite&gt; SELECT name FROM sqlite_master
   ...&gt; WHERE type = 'trigger' AND tbl_name = 'COMPANY';
audit_log
sqlite&gt; DROP TRIGGER audit_log;

```

### 索引

#### 创建索引

```
CREATE INDEX index_name ON table_name;
```

#### 单列索引

单列索引是一个只基于表的一个列上创建的索引。

```
CREATE INDEX index_name ON table_name (column_name);
```

#### 唯一索引

使用唯一索引不仅是为了性能，同时也为了数据的完整性。唯一索引不允许任何重复的值插入到表中。

```
CREATE UNIQUE INDEX index_name ON table_name (column_name);
```

#### 组合索引

组合索引是基于一个表的两个或多个列上创建的索引。

```
CREATE INDEX index_name ON table_name (column1, column2);
```

#### 隐式索引

隐式索引是在创建对象时，由数据库服务器自动创建的索引。索引自动创建为主键约束和唯一约束。

#### 删除索引

一个索引可以使用 SQLite 的 **DROP** 命令删除。当删除索引时应特别注意，因为性能可能会下降或提高。

```
DROP INDEX index_name;
```

#### 什么情况下要避免使用索引？

虽然索引的目的在于提高数据库的性能，但这里有几个情况需要避免使用索引。使用索引时，应重新考虑下列准则：
-  索引不应该使用在较小的表上。 -  索引不应该使用在有频繁的大批量的更新或插入操作的表上。 -  索引不应该使用在含有大量的 NULL 值的列上。 -  索引不应该使用在频繁操作的列上。 
### 视图

#### 创建视图

视图（View）只不过是通过相关的名称存储在数据库中的一个 SQLite 语句。所以当原始表发生变化时，视图的结果也会根据相应的结果发生变化。

```
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          Texas       45000.0   
8           Paul        24          Houston     20000.0   
9           James       44          Norway      5000.0    
10          James       45          Texas       5000.0    
11          Paul        32          California  20000.0   
sqlite&gt; create view company_view as select id, name, age from company;
sqlite&gt; select * from company_view;
ID          NAME        AGE       
----------  ----------  ----------
1           Paul        32        
2           Allen       25        
3           Teddy       23        
4           Mark        25        
5           David       27        
6           Kim         22        
8           Paul        24        
9           James       44        
10          James       45        
11          Paul        32        
sqlite&gt; delete from company where id=11;
sqlite&gt; select * from company_view;
ID          NAME        AGE       
----------  ----------  ----------
1           Paul        32        
2           Allen       25        
3           Teddy       23        
4           Mark        25        
5           David       27        
6           Kim         22        
8           Paul        24        
9           James       44        
10          James       45  
```

#### 删除视图

要删除视图，只需使用带有 **view_name** 的 DROP VIEW 语句（和删除数据表的语法类似）。

```
sqlite&gt; DROP VIEW view_name;
```

### 子查询

子查询或称为内部查询、嵌套查询，指的是在 SQLite 查询中的 WHERE 子句中嵌入查询语句。一个 SELECT 语句的查询结果能够作为另一个语句的输入值。

子查询可以与 SELECT、INSERT、UPDATE 和 DELETE 语句一起使用，可伴随着使用运算符如 =、&lt;、&gt;、&gt;=、&lt;=、IN、BETWEEN 等。

以下是子查询必须遵循的几个规则：
-  子查询必须用括号括起来。 -  子查询在 SELECT 子句中只能有一个列，除非在主查询中有多列，与子查询的所选列进行比较。 -  ORDER BY 不能用在子查询中，虽然主查询可以使用 ORDER BY。可以在子查询中使用 GROUP BY，功能与 ORDER BY 相同。 -  子查询返回多于一行，只能与多值运算符一起使用，如 IN 运算符。 -  BETWEEN 运算符不能与子查询一起使用，但是，BETWEEN 可在子查询内使用。 
```
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          Texas       45000.0   
8           Paul        24          Houston     20000.0   
9           James       44          Norway      5000.0    
10          James       45          Texas       5000.0    

sqlite&gt; select * from company where id in (select id from company where salary &gt; 45000);
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   

sqlite&gt; select * from company where salary &gt; 45000;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0 
```

```
sqlite&gt; CREATE TABLE COMPANY_BKP(
   ...&gt;    ID INT PRIMARY KEY     NOT NULL,
   ...&gt;    NAME           TEXT    NOT NULL,
   ...&gt;    AGE            INT     NOT NULL,
   ...&gt;    ADDRESS        CHAR(50),
   ...&gt;    SALARY         REAL    
   ...&gt; );
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       85000.0   
6           Kim         22          Texas       45000.0   
8           Paul        24          Houston     20000.0   
9           James       44          Norway      5000.0    
10          James       45          Texas       5000.0    
sqlite&gt; INSERT INTO COMPANY_BKP SELECT * FROM COMPANY WHERE ID IN (SELECT ID FROM COMPANY) ;
sqlite&gt; UPDATE COMPANY SET SALARY = SALARY * 0.50 WHERE AGE IN (SELECT AGE FROM COMPANY_BKP WHERE AGE &gt;= 27 );
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  10000.0   
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       42500.0   
6           Kim         22          Texas       45000.0   
8           Paul        24          Houston     20000.0   
9           James       44          Norway      2500.0    
10          James       45          Texas       2500.0 

```

```
sqlite&gt; DELETE FROM COMPANY WHERE AGE IN (SELECT AGE FROM COMPANY_BKP WHERE AGE &gt; 27 );
sqlite&gt; select * from company;
ID          NAME        AGE         ADDRESS     SALARY    
----------  ----------  ----------  ----------  ----------
2           Allen       25          Texas       15000.0   
3           Teddy       23          Norway      20000.0   
4           Mark        25          Rich-Mond   65000.0   
5           David       27          Texas       42500.0   
6           Kim         22          Texas       45000.0   
8           Paul        24          Houston     20000.0 
```

### 聚合函数
|序号|函数 &amp; 描述
|1|**COUNT 函数** COUNT 聚集函数是用来计算一个数据库表中的行数。
|2|**MAX 函数** MAX 聚合函数允许我们选择某列的最大值。
|3|**MIN 函数** MIN 聚合函数允许我们选择某列的最小值。
|4|**AVG 函数** AVG 聚合函数计算某列的平均值。
|5|**SUM 函数** SUM 聚合函数允许为一个数值列计算总和。
|6|**RANDOM 函数** RANDOM 函数返回一个介于 -9223372036854775808 和 +9223372036854775807 之间的伪随机整数。
|7|**ABS 函数** ABS 函数返回数值参数的绝对值。
|8|**UPPER 函数** UPPER 函数把字符串转换为大写字母。
|9|**LOWER 函数** LOWER 函数把字符串转换为小写字母。
|10|**LENGTH 函数** LENGTH 函数返回字符串的长度。
|11|**sqlite_version 函数** sqlite_version 函数返回 SQLite 库的版本。
