
--- 
title:  八、Mysql - 事务的概念 - 隔离级别 - ACID特性 - 锁 
tags: []
categories: [] 

---
**目录**























































### 知识点1：什么是事务 transaction？

>  
 **一个数据库事务由一条或者多条sql语句构成，它们形成一个逻辑的工作单元，这些sql语句要么全部执行，要么全部失败** 
 **事务是保证数据的****完整性****和****一致性****的重要手段** 


**示例：**

>  
 **        例如 inert，delect，alter，select 构成一个事务，这些sql语句要么全部都执行，要么 全部执行失败，当然，一条sql语句inser语句也可以构成一条事务** 


#### 事务类型

>  
 **        DML事务：有一条或者多条DML语句构成** 
 **        DDL事务：总是由一条DDL语句构成** 
 **        DCL事务：总是由一条DCL语句构成** 


###  知识点2：事务的开始和结束

>  
 **在Mysql中，系统变量@@autocommit 默认是打开的，这意味着任何一条SQL语句都会开始一个事务，语句执行完后事务自动结束，实际使用中，应该使用SET语句来关闭自动提交，否则一个事务不可能由多条SQL语句构成。（意思是如果没有使用显性开始事务的话，默认一个事务只能由一条sql语句组成）** 


```
wangsh@ucar_cloud 20:53  mysql&gt;show variables like "%autocommit%";
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| autocommit    | ON    |
+---------------+-------+
1 row in set (0.00 sec)

```

>  
 **commit其实就是将内存里的数据落盘到硬盘里面。** 
 **rollback  回滚  --》删除在内存里的数据修改** 


<img alt="" height="462" src="https://img-blog.csdnimg.cn/f64d08c88d7941f6a6a461598b44abdb.png" width="867">

>  
 ** 对于DDL（create、alter、drop等开头的语句）和DCL（grant、revoke语句）事务，在执行每条语句之前和之后，MySQL会自动执行一条COMMIT语句，因此事务是自动开始和结束的。自动提交打开或者关闭对这些事务没有影响** 


>  
 ** 对于DML事务，在自动提交关闭的情况下，事务的开始分为隐式开始和显式开始： 隐式开始：程序的第一条DML语句执行时或者在COMMIT或ROLLBACK语句之后执行第一条DML语句时，自动开始一个新的事务 显式开始：发出STRAT TRANSACTION语句。该语句会自动关闭自动提交，当事务结束后，autocommit变量恢复到原来的值** 


####  示例：显性开始：即只有输入commit以后事务才结束

```
wangsh@ucar_cloud 20:53  mysql&gt;start transaction;
Query OK, 0 rows affected (0.00 sec)

wangsh@ucar_cloud 21:34  mysql&gt;select user,host from mysql.user;
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
8 rows in set (0.00 sec)

wangsh@ucar_cloud 21:35  mysql&gt;commit
    -&gt; ;
Query OK, 0 rows affected (0.00 sec)

```

**新建一个表**

```
wangsh@wangsh 21:42  mysql&gt;create table tran_demo(id int, name varchar(20)); 
Query OK, 0 rows affected (0.01 sec)

wangsh@wangsh 21:42  mysql&gt;show tables;
+------------------+
| Tables_in_wangsh |
+------------------+
| shirts           |
| tran_demo        |
+------------------+

```

#### **示例：使用ROLLBACK回滚结束事务**

```
wangsh@wangsh 21:42  mysql&gt;start transaction;
Query OK, 0 rows affected (0.00 sec)

wangsh@wangsh 21:42  mysql&gt;insert into tran_demo(id,name)values(1,'ls');
Query OK, 1 row affected (0.00 sec)

wangsh@wangsh 21:43  mysql&gt;insert into tran_demo(id,name)values(2,'ls');
Query OK, 1 row affected (0.00 sec)

wangsh@wangsh 21:43  mysql&gt;insert into tran_demo(id,name)values(3,'ls');
Query OK, 1 row affected (0.00 sec)
# 设置a保存点
wangsh@wangsh 21:43  mysql&gt;savepoint a;
Query OK, 0 rows affected (0.00 sec)
wangsh@wangsh 21:44  mysql&gt;update tran_demo  set name='ww' where id=1;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

# 设置b保存点
wangsh@wangsh 21:45  mysql&gt;savepoint b;
Query OK, 0 rows affected (0.00 sec)

wangsh@wangsh 21:45  mysql&gt;delete from tran_demo where id=2;
Query OK, 1 row affected (0.00 sec)

wangsh@wangsh 21:46  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | ww   |
|    3 | ls   |
+------+------+
2 rows in set (0.00 sec)

wangsh@wangsh 21:46  mysql&gt;rollback to b;
Query OK, 0 rows affected (0.00 sec)

wangsh@wangsh 21:46  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | ww   |
|    2 | ls   |
|    3 | ls   |
+------+------+
3 rows in set (0.00 sec)

wangsh@wangsh 21:46  mysql&gt;rollback to a;
Query OK, 0 rows affected (0.00 sec)

wangsh@wangsh 21:47  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | ls   |
|    2 | ls   |
|    3 | ls   |
+------+------+
3 rows in set (0.00 sec)

# 失败回滚，回滚到保存点
wangsh@wangsh 21:47  mysql&gt;rollback;
Query OK, 0 rows affected (0.00 sec)

wangsh@wangsh 21:47  mysql&gt;select * from tran_demo;
Empty set (0.00 sec)

```

### 知识点2：COMMIT或者ROLLBACK之前数据的状态

>  
 **数据的修改都是在内存中进行的** 
 **通过查询表，当前用户（事务）能够查看DML操作的结果** 
 **其他用户（事务）不能查看当前用户（事务）所做的DML操作的结果，这叫做不允许脏读（dirty read）** 
 **脏读：一个事务读到了另外一个事务未提交的数据，已经修改但是回未提交的数据叫做脏数据。** 
 **表中在受影响的行被锁定，其他用户（事务）不能再受影响的行上面修改数据。** 


####  示例：不允许脏读

```
以用户newroot分别打开两个会话
第一个会话中执行：
START  TRANSACTION;
INSERT INTO trans_demo(id,NAME) VALUES(1, '张三');
SELECT * FROM trans_demo;
事务未结束
再在第二个会话中执行：
SELECT * FROM trans_demo;
看不到张三
第一个会话中再执行：
COMMIT;
再在第二个会话中执行：看到了张三
SELECT * FROM trans_demo;

```

>  
 ** root用户开启事务，但是还没有commit提交事务，wangsh用户是看不到root用户修改了但是未提交的数据的。** 


```
root@wangsh 22:04  mysql&gt;start transaction;
Query OK, 0 rows affected (0.00 sec)

root@wangsh 22:04  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | 一   |
+------+------+
1 row in set (0.00 sec)

root@wangsh 22:05  mysql&gt;insert into tran_demo(id,name) values(2,'二');
Query OK, 1 row affected (0.01 sec)

root@wangsh 22:05  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | 一   |
|    2 | 二   |
+------+------+
2 rows in set (0.00 sec)

```



```
wangsh@wangsh 22:05  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | 一   |
+------+------+
1 row in set (0.00 sec)

wangsh@wangsh 22:06  mysql&gt;

```

>  
 ** 只有root用户commit提交数据到磁盘wangsh用户才能查询到数据。这就是不允许脏读。** 


```
root@wangsh 22:05  mysql&gt;commit;
Query OK, 0 rows affected (0.00 sec)

```



```
wangsh@wangsh 22:06  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | 一   |
|    2 | 二   |
+------+------+
2 rows in set (0.00 sec)

wangsh@wangsh 22:08  mysql&gt;

```

#### 示例：两个事务不允许同时修改表中的同一行。

```
第一个会话中执行：
START  TRANSACTION;
UPDATE trans_demo SET NAME='李四' WHERE id=1;
SELECT * FROM trans_demo;
事务未结束
再在第二个会话中执行：
UPDATE trans_demo SET NAME='李四' WHERE id=1;
可以看到会话被阻塞，因为它得不到要修改的行上面的锁，锁被第一个会话持有
第一个会话中再执行：
COMMIT;
这时，第二个会话退出阻塞，成功进行修改

```

####  示例：两个事务不允许同时修改表中的同一行。

```
wangsh@wangsh 22:10  mysql&gt;start transaction;
Query OK, 0 rows affected (0.00 sec)

wangsh@wangsh 22:10  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | 一   |
|    2 | 二   |
+------+------+
2 rows in set (0.00 sec)

wangsh@wangsh 22:10  mysql&gt;update tran_demo set name='王' where name='二' ;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

wangsh@wangsh 22:11  mysql&gt;

```

```
root@wangsh 22:12  mysql&gt;update tran_demo set name='刘' where name='二';
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
root@wangsh 22:13  mysql&gt;

```

>  
 **当wangsh用户在修改tran_demo表的第二行数据的时候，root用户就不能同时修改，因为会话被阻塞了，它得不到要修改的行上面的锁，锁被第一个wangsh用户，也就是第一个会话持有，****只有在wangsh用户commit提交数据以后，root用户才能进行修改。** 


```
wangsh@wangsh 22:10  mysql&gt;update tran_demo set name='王' where name='二' ;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

wangsh@wangsh 22:11  mysql&gt;commit
    -&gt; ;
Query OK, 0 rows affected (0.00 sec)

wangsh@wangsh 22:17  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | 一   |
|    2 | 王   |
+------+------+
2 rows in set (0.00 sec)

```

```
root@wangsh 22:17  mysql&gt;update tran_demo set name='刘' where name='王';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

root@wangsh 22:17  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | 一   |
|    2 | 刘   |
+------+------+
2 rows in set (0.00 sec)


```

### 知识点3：并发事务的4个问题：

#### 1、脏读（dirty read）

>  
 **一个事务读到了另一个事务未提交的数据** 


####  2、不可重复读（nonrepeatable  read）

>  
 ** 在同一个事务中，同样的条件，你读取过的数据再次读取出来时发现值不一样了。** 
 **示例：在事务1中，Mary 读取了自己的工资为1000，事务没结束 select salary from employee empId =‘Mary’; ** 
 **           在事务2中，财务人员修改了Mary的工资为2000，并提交了事务 update employee set salary = 2000; commit; ** 
 **           在事务1中，Mary 再次读取自己的工资时，工资变为了2000   select salary from employee empId =‘Mary’;  ** 


####  3、幻读（phantom  read）

>  
 **在同一个事务中，同样的条件，第1次和第2次读出来的记录数不一样。** 
 **示例： 在事务1中，读取所有工资为1000的员工（10人） Select * from employee where salary =1000; ** 
 **           在事务2中，向employee表插入了一条员工记录，工资也为1000  ，并提交 Insert into employee(empId,salary) values(‘zs’,1000); commit; 事务1再次读取所有工资为1000的员工（11人） Select * from employee where salary =1000;** 


####  不可重复读和幻读的区别

>  
 **两者都表现为两次读取的结果不一致。区别是：不可重复读的重点是修改，幻读的重点在于新增或者删除** 


####  4、丢失更新

>  
 **一个事务的修改覆盖了另一个事务所做的修改 ** 
 **示例：以下操作按顺序执行 ** 
 **        事务1读取4号球员的罚款额，为50 事务2读取4号球员的罚款额，也为50 事务1把罚款额增加25，并提交 Update penalties set amount=amount + 25; Commit; ** 
 **        事务2把罚款额增加30，并提交 Update penalties set amount=amount + 30; Commit; ** 
 **        此时，事务1认为最新的罚款额为75，但是实际上是80，事务1所做的更新操作被事务2覆盖掉了。事务1的更新丢失了** 


### 知识点4：事务的隔离级别

>  
 ** 以上所有的4个问题都可以通过不允许两个用户同时运行一个事务来很容易的解决掉：用户1的事务没有结束，用户2的事务就不能开始，这样就不会出错了。但是这样的话，数据库的并发性能极差，不能接受** 


>  
  **每个事务都有一个隔离级别（isolation level），它规定了并发运行的两个事务之间是否允许发生上面的问题。** 
 **MySQL有4种事务隔离级别：** 
 **        REPEATABLE  READ ：可重复读。默认级别 ** 
 **        READ  COMMITTED：读已提交 ** 
 **        READ  UNCOMMITTED：读未提交 ** 
 **        SERIALIZABLE：串行化** 


<img alt="" height="465" src="https://img-blog.csdnimg.cn/c2fba93a761d499083e0425d4eb2395a.png" width="1038">

####  查看数据库及当前会话的事务隔离级别

```
root@wangsh 22:18  mysql&gt;select @@GLOBAL.tx_isolation,@@tx_isolation;
+-----------------------+-----------------+
| @@GLOBAL.tx_isolation | @@tx_isolation  |
+-----------------------+-----------------+
| REPEATABLE-READ       | REPEATABLE-READ |
+-----------------------+-----------------+
1 row in set, 2 warnings (0.00 sec)

root@wangsh 22:51  mysql&gt;

```

####  分别设置数据库及当前会话的事务隔离级别

```
SET GLOBAL tx_isolation='REPEATABLE-READ'; 
SET SESSION tx_isolation='SERIALIZABLE';

```

####  或者使用SET  TRANSACTION语句来设置隔离级别

>  
 **SET  [GLOBAL | SESSION]  TRANSACTION    ISOLATION LEVEL  level ** 
 **其中，level: REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED | SERIALIZABLE ** 
 **该语句对正在运行的事务没有影响，从下一个事务开始起作用** 


####  在配置文件中指定数据库的事务隔离级别

```
[mysqld] 
transaction-isolation = REPEATABLE-READ

```

### 知识点5：事务的ACID特性

>  
 **事务应该具有四个属性：原子性，一致性，隔离性，持久性** 
 **        原子性：一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做** 
 **        一致性：事务必须是使数据库从一个一致性状态变到另一个一致性状态，一致性和原子性是密切相关的。** 
 **        隔离性：一个事务的执行不能被其他事务干扰，即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行各个事务之间不能相互干扰** 
 **        持久性：持久性也称为永久性，是指一个事务一旦提交，他对数据库中数据的修改就应该是永久性的，接下来的其他操作或故障不应该对其有任何影响** 


### 知识点6：表锁 LOCK TABLES

>  
 **MySQL允许客户端会话显式地获得一个表锁，以防止其它会话修改表** 


>  
 ** MySQL允许客户端会话显式地获得一个表锁，以防止其它会话修改表 ** 
 **语法：** 
 **         LOCK  TABLES  tbl_name  [[AS] alias] lock_type [, tbl_name  [[AS] alias]  lock_type] ... ** 
 **        其中，锁类型lock_type: READ [LOCAL] | [LOW_PRIORITY] WRITE ** 
 **        对于innodb引擎， READ [LOCAL] = READ ， LOW_PRIORITY被废弃 ** 
 **        READ：当前会话和其它会话都可以读表，但是不能修改表 ** 
 **        WRITE：当前会话可以读写表，但是其它会话既不能读也不能写 UNLOCK TABLES 释放当前会话持有的所有表锁** 


#### 示例：读锁：

```
wangsh@wangsh 23:48  mysql&gt;lock tables tran_demo read;
Query OK, 0 rows affected (0.00 sec)

wangsh@wangsh 23:49  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | 一   |
|    2 | 刘   |
+------+------+
2 rows in set (0.00 sec)

wangsh@wangsh 23:49  mysql&gt;


wangsh@wangsh 22:17  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | 一   |
|    2 | 刘   |
+------+------+
2 rows in set (0.00 sec)

wangsh@wangsh 23:49  mysql&gt;insert into tran_demo(id,name) values(1,'li');


```

>  
 **释放所有的锁后，另一个会话才能进行修改操作。** 


```
wangsh@wangsh 23:52  mysql&gt;unlock tables;
Query OK, 0 rows affected (0.00 sec)

wangsh@wangsh 23:49  mysql&gt;insert into tran_demo(id,name) values(1,'li');
Query OK, 1 row affected (2 min 9.96 sec)

wangsh@wangsh 23:52  mysql&gt;select * from tran_demo;
+------+------+
| id   | name |
+------+------+
|    1 | 一   |
|    2 | 刘   |
|    1 | li   |
+------+------+
3 rows in set (0.00 sec)


```

### 知识点:7：共享锁

```
SELECT…LOCK IN SHARE MODE

```

>  
 **对查询得到行加共享锁。其它会话可以查询这些行，但是不能修改它们，除非你结束事务释放所加的锁。如果你要加锁的行正被其它事务修改，查询就被阻塞直到其它事务提交 该语句主要用在需要数据依赖关系时来确认某行记录是否存在，并确保没有人对这个记录进行UPDATE或者DELETE操作。例如：你想向子表child中插入一行，首先要确保子行所依赖的父行在父表parent中存在。先使用该语句查询出父行** 


```
SELECT * FROM parent 
  WHERE NAME = 'Jones'  LOCK IN SHARE MODE;

```

>  
 **如果查询返回了‘Jones’ ，你就可以放心的插入子行并提交事务。如果在查询时不带LOCK IN SHARE MODE子句，那么在插入子行之前父行很可能就被其它事务删除了** 


>  
 ** 注意：如果当前事务也需要对锁定的记录进行更新操作，则很有可能造成死锁。例如** 


```
会话1执行：
select  actor_id,first_name,last_name from actor where actor_id = 178 lock in share mode;
会话2执行：
select  actor_id,first_name,last_name from actor where actor_id = 178 lock in share mode;
会话1执行：被阻塞
update actor set last_name = 'MONROE T' where actor_id = 178;
会话2执行，导致死锁退出
update actor set last_name = 'MONROE T' where actor_id = 178;
ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction

```

### 知识点8:应用程序锁

>  
 **MySQ支持一种应用层级别的锁，称为应用程序锁或命名锁（named lock）。该锁和表及表中的行无关。通过这个锁，访问MySQL的应用程序可以实现互斥功能。这个锁通过一组MySQL 内置函数来实现** 


```
GET_LOCK(str,timeout)：

```

>  
 ** Str：锁的名字 Timeout：超时时间 创建一个名为str的应用程序锁。如果创建成功则返回1；如果名为str的锁已经存在，等待timeout秒的时间后还得不到锁则返回0；如果发生错误则返回null** 


####  应用程序锁释放锁

>  
 **一个应用程序获取到锁后，可以通过RELEASE_LOCK(str)、执行新的GET_LOCK(str,timeout)、或者断开mysql连接（不管是正常释放还是异常断开）这三种方式释放锁** 


>  
 ** RELEASE_LOCK(str) ： 释放名为str的锁。如果锁被成功释放，返回1；如果这个进程没有占有该锁，则返回0；如果这个名为str的锁不存在，则返回NULL ** 
 **IS_USED_LOCK(str) 检查名为str的锁是否在使用，如果被使用，则返回拥有该锁的连接标识符，否则返回NULL ** 
 **IS_FREE_LOCK(str) 检查名为str的锁是否可用，如果可用则返回1；如果在使用则返回0；如果有错误则返回NUL** 

