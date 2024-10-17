
--- 
title:  常用命令之mysql命令之show命令 
tags: []
categories: [] 

---
## 一、mysql show命令简介

  mysql数据库中show命令是一个非常实用的命令，SHOW命令用于显示MySQL数据库中的信息。它可以用于显示数据库、表、列、索引和用户等各种对象的信息。我们常用的有show databases，show tables，show full processlist等，实际上可以使用的还有很多，实际上包括三十多个子命令，加上可选参数可以查看的数据库信息就更多了。此博文以示例的方式介绍mysql show命令，博文的实验环境如下：
- 操作系统：centos7.6- 数据库版本：mysql5.7.26
## 二、最常用show命令使用示例

### 1、查看数据库列表

  我们用得最多的就是show databases了，可以查看数据库列表，如果是root用户可以看到所有的数据库，如果是普通用户只可以看到自己有权限的库和information_schema库。

>  
 mysql&gt; show databases; <img src="https://img-blog.csdnimg.cn/d06ca6e5b5a54e4d88c09a859f880da3.png" alt="在这里插入图片描述"> 


### 2、查看数据库连接进程

  show processlist可以查看数据库连接进程，full是可选项，区别是show显示前100个线程，show full显示所有的。这个命令root用户和普通用户都可以执行，区别就是root用户可以看到所有用户的连接信息，普通用户只能看到该用户的。连接信息中有进程ID、用户名、连接源地址和端口号、连接的数据库、命令状态、连接时间、执行状态、执行的命令明细。show processlist常用于出现锁的情况下查询进程ID，然后手动kill ID后解锁。

>  
 mysql&gt; show processlist; mysql&gt; show full processlist; <img src="https://img-blog.csdnimg.cn/9cc69b071b9c444bb09a0e91cfb4feb1.png" alt="在这里插入图片描述"> 


### 3、查看表列表

  show tables用于查看库下的表列表，需要先进入某库后才可以执行。当然我们也可以使用show tables from db_name，查看某库的数据表，前提是有权限查看。

>  
 mysql&gt; use testdb; mysql&gt; show tables; mysql&gt; show tables from mysql; <img src="https://img-blog.csdnimg.cn/2aa27e178220412da80b1138467e36a0.png" alt="在这里插入图片描述"> 


### 4、查看表结构

  使用SHOW CREATE TABLE tbl_name可以查看某表的表结构，常用于需要确认表信息，在修改表结构前常用到。

>  
 mysql&gt; show create table tb_0001; <img src="https://img-blog.csdnimg.cn/7ccd7230f196404cbd87204b3b7515a2.png" alt="在这里插入图片描述"> 


### 5、查看变量信息

  显示MySQL服务器的配置变量的值，这个命令常在排查问题的时候用到，用于查看mysql实例的参数配置，经常结合like一起使用，用于过滤指定参数。可以使用show global variables或者show session variables查看全局或者会话参数，默认是查看会话参数。

>  
 mysql&gt; show variables like ‘%time%’; <img src="https://img-blog.csdnimg.cn/8d1bff7ee45c44abb212e023df474af1.png" alt="在这里插入图片描述"> 


### 6、查看数据表的索引信息

  如果我们需要查看某表都创建了哪些索引可以使用show index from table_name的方式查看，默认有主键索引，如果还创建了其他索引通过此方式都可以看到。

>  
 mysql&gt; show index from tb_0001;<img src="https://img-blog.csdnimg.cn/b96777cfe2f14fdd8bcbf8b3902b5258.png" alt="在这里插入图片描述"> 


### 7、查看某用户的权限

  使用show grants for user@host 可以查看用户的授权，如果用户的host是任意源可以省略；也可以直接输入show grants查看当前用户的权限。

>  
 mysql&gt; show grants for bak@‘192.168.0.%’; mysql&gt; show grants; 


### 8、获取show命令帮助

>  
 mysql&gt; help show; 


## 三、需要特权执行的show命令使用示例

  如下show命令执行都需要特权，非普通用户可以执行。

### 1、查看主从状态

  如果搭建了mysql的主从模式，我们需要检查主从状态就可以使用此命令。如果配置了master或者slave角色就可以看到主从状态信息，否则为空。

>  
 mysql&gt; show master status; mysql&gt; show slave status; <img src="https://img-blog.csdnimg.cn/2a03e98bf5034c5593a9ec4103ee875d.png" alt="在这里插入图片描述"> 


### 2、查看从节点主机信息

>  
 mysql&gt; show slave hosts; ±----------±-----±-----±----------±-------------------------------------+ | Server_id | Host | Port | Master_id | Slave_UUID | ±----------±-----±-----±----------±-------------------------------------+ | 2 | | 3306 | 3306 | 4ef97f7e-cfe9-11ea-8214-3448edf3158c | ±----------±-----±-----±----------±-------------------------------------+ 1 row in set (0.00 sec) 


### 3、查看二进制日志位置

>  
 mysql&gt; show master logs; mysql&gt; show binary logs; 


### 4、查看binlog日志事件

>  
 mysql&gt; SHOW BINLOG EVENTS; <img src="https://img-blog.csdnimg.cn/13a6de295b6549448e605d3912654e78.png" alt="在这里插入图片描述"> 


## 四、其他show命令使用示例

### 1、查看可用字符集

>  
 mysql&gt; SHOW CHARACTER SET; mysql&gt; SHOW CHARACTER SET like ‘%gbk%’; 


### 2、查看显示可用的字符校对规则

>  
 mysql&gt; SHOW COLLATION; 


### 3、查看某库某表的所有列

>  
 mysql&gt; SHOW full COLUMNS FROM tb_0001 from testdb; <img src="https://img-blog.csdnimg.cn/eb559e34e566442592e2e9d62a02022c.png" alt="在这里插入图片描述"> 


### 4、查看数据库创建信息

  使用show create 可以查看创建数据库、事件、函数、存储过程、触发器、视图等的信息，需要对应的名称。

>  
 mysql&gt; show create database testdb; SHOW CREATE DATABASE db_name SHOW CREATE EVENT event_name SHOW CREATE FUNCTION func_name SHOW CREATE PROCEDURE proc_name SHOW CREATE TRIGGER trigger_name SHOW CREATE VIEW view_name 


### 5、查看最近事件

>  
 mysql&gt; show events; Empty set (0.00 sec) 


### 6、查看最近告警

>  
 mysql&gt; show warnings; Empty set (0.00 sec) 


### 7、查看最近错误

>  
 mysql&gt; show errors; Empty set (0.00 sec) 


### 8、查看引擎状态

  查看innodb引擎状态，

>  
 mysql&gt; SHOW ENGINE innodb status; 


### 9、查看已安装的插件

>  
 mysql&gt;SHOW PLUGINS 


### 10、查看数据库表状态

  查看数据库表状态，这个在进行单个表备份还原的时候还是非常有用的，通过查看表的最后更新时间，我们可以选择对应日期的备份文件进行还原，在需要对表进行业务操作的时候，也可以通过分析协助判断什么时间进行数据库操作比较合适。

>  
 mysql&gt; show table status from testdb; <img src="https://img-blog.csdnimg.cn/b5cbcf751b544886b679bed9cd564b5e.png" alt="在这里插入图片描述"> 


### 11、查看所有打开的表

>  
 mysql&gt; show open tables; 


### 12、查看数据库触发器

  我们可以通过show triggers查看所有触发器，也可以show triggers from db_name查看指定数据库的触发器。

>  
 mysql&gt; show triggers from testdb; 


### 13、查看函数或者存储过程状态

>  
 mysql&gt; SHOW FUNCTION STATUS like ‘%version_patch%’\G mysql&gt; SHOW PROCEDURE STATUS like ‘table_exists’\G 


### 14、使用profile语句分析sql性能

  我们可以使用profile语句分析需要执行的sql执行的性能情况，可以看到sql执行的各阶段的资源消耗，SHOW PROFILE语句支持选择ALL、CPU、BLOCK IO、CONTEXT SWITCH和PAGE FAULTS等来查看具体的明细信息。不过此功能即将被淘汰，在新版本中通过Performance Schema库来分析资源消耗和使用情况。

>  
 mysql&gt; set profiling=1; mysql&gt; select count(*) from testdb.tb_0001; mysql&gt; show profiles; mysql&gt; show profile for query 1; mysql&gt; show profile cpu for query 1; <img src="https://img-blog.csdnimg.cn/14862c4e36ce435bbbcf3a3012794fd2.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/439555f319d04554b5c17d3dbe332d40.png" alt="在这里插入图片描述"> 


## 五、show status常用参数说明

  使用SHOW STATUS语句能够获取MySQL服务器的一些状态信息，这些状态信息主要是MySQL数据库的性能参数。SHOW STATUS语句的语法格式如下：

>  
 SHOW [SESSION | GLOBAL] STATUS LIKE ‘status_name’; 


  其中，SESSION表示获取当前会话级别的性能参数，GLOBAL表示获取全局级别的性能参数，并且SESSION和GLOBAL可以省略，如果省略不写，默认为SESSION。status_name表示查询的参数值。熟练掌握这些参数的使用，能够更好地了解SQL语句的执行频率。常用参数说明如下：

<th align="left">参数值</th><th align="left">参数说明</th>
|------
<td align="left">Connections</td><td align="left">连接MySQL服务器的次数</td>
<td align="left">Uptime MySQL</td><td align="left">服务器启动后连续工作的时间</td>
<td align="left">Slow_queries</td><td align="left">慢查询的次数</td>
<td align="left">Com insert</td><td align="left">插入数据的次数，批量插入多条数据时，只累加1</td>
<td align="left">Com delete</td><td align="left">删除数据的次数，每次累加1</td>
<td align="left">Com update</td><td align="left">修改数据的次数，每次累加1</td>
<td align="left">Com select</td><td align="left">查询数据的次数，一次查询操作累加1</td>
<td align="left">Innodb rows read</td><td align="left">查询数据时返回的数据行数</td>
<td align="left">Innodb rows inserted</td><td align="left">插入数据时返回的记录数</td>
<td align="left">Innodb rows updated</td><td align="left">更新数据时返回的记录数</td>
<td align="left">Innodb rows deleted</td><td align="left">删除数据时返回的记录数</td>
