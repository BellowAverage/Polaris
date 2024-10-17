
--- 
title:  MySQL葵花宝典，打通你的任督二脉 
tags: []
categories: [] 

---
## MySQL葵花宝典，打通你的任督二脉



#### 文章目录
- - <ul><li>- <ul><li>- - - - <ul><li>- - <ul><li><ul><li>- - - - <ul><li>- - 


MySQL 数据库开源免费，能够跨平台，支持分布式，性能也不错，可以和 PHP、Java 等 Web 开发语言完美配合，非常适合中小型企业作为 Web 数据库（网站数据库）。

这篇 MySQL 教程通俗易懂，实例丰富，既有基础知识，也有进阶技能，能够帮助读者快速入门，是你学习 MySQL 的葵花宝典。

### 一、MySQL入门：

#### 1、生活中常见的数据库应用：

超时购物，图书馆，学生管理系统，网上购物等。

我们在超市购买商品时，就是在访问一个数据库。

结账时，收银员使用条形码阅读器扫描客户购买的每一件商品。这个条形码阅读器连接着一个访问商品数据库的应用程序，该程序根据条形码从商品数据库中找出商品价格，然后从库存中减去本次销售这种商品的数量，并且在屏幕上显示相应的价格。

如果存货量低于设置的临界值，数据库系统将提示进货以补充存货。如果有客户向超市打电话订购商品，售货员可以通过运行应用程序，查看数据库中此商品是否有足够的存货。

#### 2、数据管理技术的3个发展阶段：

**数据库管理系统**（DBMS）是数据库的核心软件之一，是位于用户与操作系统之间的数据管理软件，用于建立，使用和维护数据库。

```
数据管理就是对各种数据进行分类、组织、编码、查询和维护，主要经历了 3 个阶段，即人工管理阶段、文件系统阶段和数据库系统阶段。每一个阶段都是以减小数据冗余、增强数据独立性和方便操作数据为目的进行发展。

```

（1）人工管理阶段的特点如下：
- 数据不能长期保存- 不便于查询数据- 数据不能共享，冗余度大- 数据不具有独立性
（2）文件系统阶段的特点如下：
- 数据可以长期保存- 数据由文件系统来管理- 数据冗余大，共享性差- 数据独立性差- 无法应对突发事故（文件误删，磁盘故障等）
<img src="https://img-blog.csdnimg.cn/4f19b2b5f7d34dffbb7492d5880375d1.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

（3）数据库系统阶段的特点如下：
- 数据由数据库管理系统统一管理和控制- 数据共享性高，冗余度低- 数据独立性强- 数据粒度小
|数据管理的3个阶段|人工管理（20 世纪 50 年代中期）|文件系统（50 年代末至 60 年代中期）|数据库系统（60 年代后期）
|------
|应用背景|科学计算|科学计算、管理|大规模数据、分布数据的管理
|硬件背景|无直接存取存储设备|磁带、磁盘、磁鼓|大容量磁盘、可擦写光盘、按需增容磁带机等
|软件背景|无专门管理的软件|利用操作系统的文件系统|由 DBMS 支撑
|数据处理方式|批处理|联机实时处理、批处理|联机实时处理、批处理、分布处理
|数据的管理者|用户/程序管理|文件系统代理|DBMS 管理
|数据应用及其扩充|面向某一应用程序难以扩充|面向某一应用系统、不易扩充|面向多种应用系统、容易扩充
|数据的共享性|无共享、冗余度极大|共享性差、冗余度大|共享性好、冗余度小
|数据的独立性|数据的独立性差|物理独立性好、逻辑独立性差|具有高度的物理独立性、具有较好的逻辑独立性
|数据的结构化|数据无结构|记录内有结构、整体无结构|统一数据模型、整体结构化
|数据的安全性|应用程序保护|文件系统保护|由 DBMS 提供完善的安全保护

#### 3、数据库是啥？

**描述事物的符号称为数据。**数据有多种表现形式，可以是数字，也可以是文字、图形、图像、声音、语言等。

**信息**是指对数据进行加工处理后提取的对人类社会实践和生产活动产生决策影响的数据。

**数据库**（Database）指长期存储在计算机内的、有组织的、可共享的数据集合。

**数据库管理系统**（DBMS）是数据库系统的核心软件之一，是位于用户与操作系统之间的数据管理软件，用于建立，使用和维护数据库。它的主要功能包括数据定义、数据操作、数据库的运行管理、数据库的建立和维护等几个方面。

目前，较为流行的数据库管理系统有 、SQL Server、Oracle 和 DB2 等。

**数据库系统**（Database System，DBS）由硬件和软件共同构成。

数据库系统主要有以下 3 个组成部分：

（1）数据库：用于存储数据的地方。

（2）数据库管理系统：用于管理数据库的软件。

（3）数据库应用程序：为了提高数据库系统的处理能力所使用的管理数据库库的软件补充。

#### 4、数据库类型：

层次数据库，关系型数据库，面向文档数据库，列存储数据库，XML 数据库，键值存储数据库。

##### （1）关系型数据库：

关系型数据库是由多张能互相连接的表组成的数据库。

**优点**
1. 都是使用表结构，格式一致，易于维护。1. 使用通用的 SQL 语言操作，使用方便，可用于复杂查询。1. 数据存储在磁盘中，安全。
**缺点**
1. 读写性能比较差，不能满足海量数据的高效率读写。1. 不节省空间。因为建立在关系模型上，就要遵循某些规则，比如数据中某字段值即使为空仍要分配空间。1. 固定的表结构，灵活度较低。
常见的关系型数据库有 Oracle、DB2、 SQL Server 和 MySQL 等。

##### （2）非关系型数据库：

通常指数据以对象的形式存储在数据库中，而对象之间的关系通过每个对象自身的属性来决定。

**优点**
1. 非关系型数据库存储数据的格式可以是 key-value 形式、文档形式、图片形式等。使用灵活，应用场景广泛，而关系型数据库则只支持基础类型。1. 速度快，效率高。 NoSQL 可以使用硬盘或者随机存储器作为载体，而关系型数据库只能使用硬盘。1. 海量数据的维护和处理非常轻松。1. 非关系型数据库具有扩展简单、高并发、高稳定性、成本低廉的优势。1. 可以实现数据的分布式处理。
**缺点**
1. 非关系型数据库暂时不提供 SQL 支持，学习和使用成本较高。1. 非关系数据库没有事务处理，没有保证数据的完整性和安全性。适合处理海量数据，但是不一定安全。1. 功能没有关系型数据库完善。
常见的非关系型数据库有 Neo4j、、、Memcached 和  等。

#### 5、为什么使用数据库？

（1）数据库可以结构化存储大量的数据信息，方便用户进行有效的检索和访问。

（2）数据库可以有效地保持数据信息的一致性、完整性、降低数据冗余。

（3）数据库可以满足应用的共享和安全方面的要求，把数据放在数据库中在很多情况下也是出于安全的考虑。

（4）数据库技术能够方便智能化地分析，产生新的有用信息。

#### 6、常用数据库访问接口：

主要的数据库访问接口主要有 ODBC、JDBC、ADO.NET 和 PDO。

**（1）ODBC**（Open Database Connectivity，开放数据库互连）为访问不同的 SQL 数据库提供了一个共同的接口。

**（2）JDBC**（Java 数据库连接）用于 Java 应用程序连接数据库的标准方法，是一种用于执行 SQL 语句的 Java API，可以为多种关系数据库提供统一访问，它由一组用 Java 语言编写的类和接口组成。

**（3）ADO.NET** 是微软在 .NET 框架下开发设计的一组用于和数据源进行交互的面向对象类库。

**（4）PDO**（PHP Data Object）为 PHP 访问数据库定义了一个轻量级的、一致性的接口，它提供了一个数据访问抽象层，这样，无论使用什么数据库，都可以通过一致的函数执行查询和获取数据。

#### 7、MySQL的特点，优势：

（1）MySQL 是开放源代码的数据库；

（2）MySQL 的跨平台性；

（3）价格优势；

（4）功能强大且使用方便；

适用场景：Web 网站系统，日志记录系统，数据仓库系统，嵌入式系统

### 二、MySQL的安装和配置：

**这里可以参考这篇博客：**

https://blog.csdn.net/weixin_53060366/article/details/121623206?spm=1001.2014.3001.5501

这里给大家详细操作了三种方法在linux上安装MySQL；如：rpm包安装，yum源安装以及源码包编译安装。

MySQL 推荐使用 RPM 包进行 Linux 平台下的安装，因为 RPM 包的安装和卸载都很方便，通过简单的命令就可以实现。

### 三、MySQL图形化管理工具安装：

 服务器正确安装以后，可以通过命令行管理工具或者图形化的管理工具来操作 MySQL 数据库。

MySQL 图形化管理工具极大地方便了数据库的操作与管理，除了系统自带的命令行管理工具之外，常用的图形化管理工具还有 MySQL Workbench、phpMyAdmin、Navicat、MySQLDumper、SQLyog、MySQL ODBC Connector。

其中 phpMyAdmin 和 Navicat 提供中文操作界面，MySQL Workbench、MySQL ODBC Connector、MySQLDumper 为英文界面。

下面给大家安装Navicat图形管理工具。

可以参考博客：https://blog.csdn.net/weixin_53060366/article/details/121633899?spm=1001.2014.3001.5501

[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-fw4w9HX9-1638344113294)(E:\studyFile\学习文件\错题集\Navicat安装\截图\02.png)]

### 四、MySQL的基本操作：

对数据库进行查询和修改操作的语言叫做 SQL（Structured Query Language，结构化查询语言）。

SQL 是一种数据库查询和程序设计语言，用于存取数据以及查询、更新和管理关系数据库系统。

SQL 具有如下优点。
1. 一体化：SQL 集数据定义、数据操作和数据控制于一体，可以完成数据库中的全部工作。1. 使用方式灵活：SQL 具有两种使用方式，可以直接以命令方式交互使用；也可以嵌入使用，嵌入C、C++、Fortran、COBOL、Java 等语言中使用。1. 非过程化：只提操作要求，不必描述操作步骤，也不需要导航。使用时只需要告诉计算机“做什么”，而不需要告诉它“怎么做”，存储路径的选择和操作的执行由数据库管理系统自动完成。1. 语言简洁、语法简单：该语言的语句都是由描述性很强的英语单词组成，而且这些单词的数目不多。
**SQL功能分类：**

###### （1）DDL：数据定义语言
- DROP：删除数据库和表等对象- CREATE：创建数据库和表等对象- ALTER：修改数据库和表等对象的结构
###### （2）DML：数据操作语言
- SELECT：查询表中的数据- INSERT：向表中插入新数据- UPDATE：更新表中的数据- DELETE：删除表中的数据
###### （3）DQL：数据查询语言：

用来查询表中的记录，主要包含 SELECT 命令，来查询表中的数据。

###### （4）DCL：数据控制语言：
- GRANT：赋予用户操作权限- REVOKE：取消用户的操作权限- COMMIT：确认对数据库中的数据进行的变更- ROLLBACK：取消对数据库中的数据进行的变更
**SQL的基本书写规则：**

（1）SQL 语句要以分号`;`结尾；

（2）SQL 语句不区分大小写；

（3）常数的书写方式是固定的；

（4）单词需要用半角空格或者换行来分隔；

### 五、MySQL的增，删，改，查：

##### 1、对数据库操作：

```
#查询数据库：
SHOW DATABASES;
mysql&gt; show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| class              |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

#使用数据库
use class;
#查询数据库中的表
SHOW TABLES;

#创建toys数据库
CREATE DATABASE toys;

#删除数据库：
DROP DATABASE toys;

```

##### 2、表的相关操作：

```
#创建pet表
CREATE TABLE pet(
pid int,
pname VARCHAR(20),
page int,
ptype VARCHAR(30));

#查看表结构
desc pet;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| pid   | int(11)     | YES  |     | NULL    |       |
| pname | varchar(20) | YES  |     | NULL    |       |
| page  | int(11)     | YES  |     | NULL    |       |
| ptype | varchar(30) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
4 rows in set (0.00 sec)

#添加字段
ALTER TABLE student add iphon INT(11);

#修改一个表的字段类型
ALTER TABLE student MODIFY sname VARCHAR(50);
DESC student;

#修改表名
RENAME TABLE students to student;

#修改表的字符集
ALTER TABLE student CHARACTER SET utf8;

#修改字段的字符集
ALTER TABLE student CHANGE sname sname VARCHAR(50) CHARACTER set utf8;

#修改字段名
ALTER TABLE student CHANGE iphon siphon INT(11);

#查看表的创建细节
SHOW CREATE TABLE student;
CREATE TABLE `student` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(50) DEFAULT NULL,
  `sage` int(11) DEFAULT NULL,
  `sgender` char(2) DEFAULT NULL,
  `sadd` varchar(50) DEFAULT NULL,
  `siphon` int(11) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8


```

```
#删除一个字段
ALTER TABLE student drop siphon;

#删除表
DROP TABLE student;

#查询表中内容
SELECT * FROM student;
#根据条件查找
SELECT * FROM student WHERE sid=2;
#查找年龄大于21且是性别为男的学生
SELECT * FROM student WHERE sage&gt;21 and sgender="男";

#插入数据
INSERT INTO student (sid,sname,sage) VALUES(11,'迪丽热巴',26);
#若不指定字段，则需添加全部字段
INSERT INTO student 
VALUES(12,'王一博',23,'男','深圳'),(13,'杨洋',29,'男','南昌');

#更新表中的字段,若不指定where条件，则全部更新
UPDATE student set sname='张一山' WHERE sid=10;
#更新多个字段
UPDATE student set sname='王源',sage=22 WHERE sid=9;

#删除某一条记录，若没指定条件，将删除表中所有数据
DELETE FROM student WHERE sid=7;

```

删除时，delete和truncate的区别：

delete删除表的数据，表结构还在；

truncate删除时是把表直接drop掉，然后再建一个同样的新表，执行速度比delete快。

##### 3、DQL 查询数据：

条件查询运算符及关键字：

（1）=，&gt;，&gt;=，!=，&lt;，&lt;=

（2）between…and…

（3）in(set)；固定的范围值

（4）is null；（为空），is not null；（不为空）

（5）and，与；or，或；not，非

```
#查询学号为2或3或4,的学生信息
SELECT * FROM student WHERE sid=2 or sid=3 or sid=4;
#或者输入这个
SELECT * FROM student WHERE sid in (2,3,4);

#查询地址为空的记录
SELECT * FROM student WHERE sadd is NULL;

#查询地址不为空的记录
SELECT * FROM student WHERE sadd is not NULL;
#查询性别不为男的学生信息
SELECT * FROM student WHERE sgender!='男';
#查询年龄在20-35之间的学生记录
SELECT * FROM student WHERE sage BETWEEN 20 AND 35;

```

**模糊查询：**

（1）根据指定的关键字进行查询；

（2）使用 like 关键字后跟通配符：

通配符：_：任意一个字符（不一定是字符，其他字符也行）

%：任意0-n个字符；

```
#查询名字为4个字的学生
SELECT * FROM student WHERE sname LIKE '____';
#查询名字中包含杨字的学生信息
SELECT * FROM student WHERE sname LIKE '%杨%';

```

**字段控制查询：**

```
#去除字段重复记录
SELECT DISTINCT sage FROM student;
#两个数值型字段相加，得到一个新的字段
#表中有许多记录为null，这时需要把null转化为0，再相加
SELECT *,IFNULL(shuxue,0)+IFNULL(yuwen,0) FROM score;

#查询时排序操作
#默认是升序排序，降序要加 desc
#对学生表中数据按照年龄升序排序
SELECT * FROM student ORDER BY sage;
#当出现年龄一致时，外加字段sid，按照sid降序排序；
SELECT * FROM student ORDER BY sage,sid DESC;

```

**常见聚合函数查询：**

```
#聚合函数
#1、count统计记录行数，空行不统计
SELECT COUNT(*) FROM student;
SELECT COUNT(sage) FROM student;

#查询年龄大于22岁的学生人数
SELECT COUNT(*) FROM student WHERE sage&gt;21;
SELECT COUNT(sname),COUNT(sage) FROM student;

#条件判断进行查询
SELECT sname '姓名',sage '年龄',
CASE 
WHEN sage &lt; 20 THEN '小鲜肉'
WHEN sage &gt;= 20 AND sage &lt; 50 THEN '成年人'
ELSE '老人'
END '状态' FROM student;

#查询学生英语成绩和
SELECT SUM(yingyu) from xxcj;
#查询学生高数和体育成绩
SELECT SUM(gaoshu),SUM(tiyu) FROM xxcj;
#查询学生英语和高数成绩和,并起个别名：英高
SELECT SUM(IFNULL(yingyu,0)+IFNULL(gaoshu,0)) '英高' FROM xxcj;
#查询学生平均年龄
SELECT AVG(sage) FROM student;
#查询年龄最大和最小的学生
SELECT MAX(sage),MIN(sage) FROM student;

#查询有几门学科，分组查询
SELECT cname FROM course GROUP BY cname;
#查询分组后，每组中的成员
SELECT ptype,GROUP_CONCAT(pname) FROM pet GROUP BY ptype;
#查询每个狗狗的类型名称及每个类型中年龄大于1年的人数
SELECT ptype,GROUP_CONCAT(page),COUNT(*) 
FROM pet 
WHERE page&gt;1 GROUP BY ptype;

#指定条件查询，在group by中还可以用having
SELECT ptype,GROUP_CONCAT(page),COUNT(*) 
FROM pet GROUP BY ptype
HAVING SUM(page)&gt;4;

```

**having和where的区别：**

having是在分组后对数据进行过滤，可以使用分组函数，聚合函数；

where是在分组前对数据进行过滤，不可以使用函数。如果某记录不满足where条件，则不参与分组。

注意：having和where可以同时出现。

```
#limit 参数1，参数2
#参数1：从哪一行开始查，下角标从0开始；参数2：一共要查几行
#从第三条记录开始，向下查询4条记录
SELECT * FROM student LIMIT 2,4;

```

<img src="https://img-blog.csdnimg.cn/0d6b11a9ad734457a511c324073ef13d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

**数据查询时的书写顺序：**

**select–from–where–group by–having-- order by-- limit**
