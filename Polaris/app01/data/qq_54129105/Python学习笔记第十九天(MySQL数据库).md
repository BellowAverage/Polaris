
--- 
title:  Python学习笔记第十九天(MySQL数据库) 
tags: []
categories: [] 

---


#### Python学习笔记第十九天
- - <ul><li>- - - <ul><li>


## 操作 MySQL 数据库

Python 标准数据库接口为 Python DB-API，Python DB-API为开发人员提供了数据库应用编程接口。

Python 数据库接口支持非常多的数据库，你可以选择适合你项目的数据库：
- GadFly- mSQL- MySQL- PostgreSQL- Microsoft SQL Server 2000- Informix- Interbase- Oracle- Sybase
你可以访问查看详细的支持数据库列表。

不同的数据库你需要下载不同的DB API模块，例如你需要访问Oracle数据库和Mysql数据，你需要下载Oracle和MySQL数据库模块。

DB-API 是一个规范. 它定义了一系列必须的对象和数据库存取方式, 以便为各种各样的底层数据库系统和多种多样的数据库接口程序提供一致的访问接口 。

Python的DB-API，为大多数的数据库实现了接口，使用它连接各数据库后，就可以用相同的方式操作各数据库。

Python DB-API使用流程：
- 引入 API 模块。- 获取与数据库的连接。- 执行SQL语句和存储过程。- 关闭数据库连接。
### 什么是MySQLdb?

MySQLdb 是用于Python链接Mysql数据库的接口，它实现了 Python 数据库 API 规范 V2.0，基于 MySQL C API 上建立的。

### 如何安装MySQLdb?

为了用DB-API编写MySQL脚本，必须确保已经安装了MySQL。复制以下代码，并执行：

```
import MySQLdb

```

如果执行后的输出结果如下所示，意味着你没有安装 MySQLdb 模块：

```
Traceback (most recent call last):
  File "test.py", line 3, in &lt;module&gt;
    import MySQLdb
ImportError: No module named MySQLdb

```

安装MySQLdb，请访问  ，(Linux平台可以访问：)从这里可选择适合您的平台的安装包，分为预编译的二进制文件和源代码安装包。

如果您选择二进制文件发行版本的话，安装过程基本安装提示即可完成。如果从源代码进行安装的话，则需要切换到MySQLdb发行版本的顶级目录，并键入下列命令:

```
$ gunzip MySQL-python-1.2.2.tar.gz
$ tar -xvf MySQL-python-1.2.2.tar
$ cd MySQL-python-1.2.2
$ python setup.py build
$ python setup.py install

```

**注意：** 请确保您有root权限来安装上述模块。

### 数据库连接

连接数据库前，请先确认以下事项：
- 您已经创建了数据库 TESTDB.- 在TESTDB数据库中您已经创建了表 EMPLOYEE- EMPLOYEE表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。- 连接数据库TESTDB使用的用户名为 “testuser” ，密码为 “test123”,你可以可以自己设定或者直接使用root用户名及其密码，Mysql数据库用户授权请使用Grant命令。- 在你的机子上已经安装了 Python MySQLdb 模块。- 如果您对sql语句不熟悉，可以访问我们的**SQL基础教程**
#### 数据库连接操作

链接Mysql的TESTDB数据库： MySQLdb.connect(本地ip,数据库用户,数据库密码,数据库库名，数据编码格式)

```
# 实例 1
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
db.close()

```

### 创建数据库表

如果数据库连接存在我们可以使用execute()方法来为数据库创建表，如下所示创建表EMPLOYEE：

```
# 实例 2

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )

cursor.execute(sql)

# 关闭数据库连接
db.close()

```

### 数据库插入操作

以下实例使用执行 SQL INSERT 语句向表 EMPLOYEE 插入记录：

```
# 实例 3

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()

```

以上例子也可以写成如下形式：

```
# 实例 4

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES (%s, %s, %s, %s, %s )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()

```

## 结束语

今天学习的是PythonMysql数据库学会了吗。 今天学习内容总结一下：
1. 什么是MySQLdb?1. 如何安装MySQLdb?1. 数据库连接1. 创建数据库表1. 数据库插入操作