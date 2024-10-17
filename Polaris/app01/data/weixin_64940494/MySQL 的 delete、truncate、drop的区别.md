
--- 
title:  MySQL 的 delete、truncate、drop的区别 
tags: []
categories: [] 

---
        mysql语句中有三种删除数据的方式分别时delete、truncate、drop。这三种删除数据的方式对于mysql来说其删除时的操作不一样。

####         一、delete删除

1、delete属于数据库DML操作语言，删除时只数据行并不会删除表的结构，执行删除时会通过事务并且会触发触发器（trigger）；

2、在 InnoDB 中，delete其实并不会真的把数据删除，mysql 实际上只是给删除的数据打了个标记为已删除，因此 delete 删除表中的数据时，表文件在磁盘上所占空间不会变小，存储空间不会被释放，只是把删除的数据行设置为不可见。 虽然未释放磁盘空间，但是下次插入数据的时候，仍然可以覆盖这部分空间；

3、 执行delete时会先将删除数据缓存到回滚空间段(rollback segement)中，直到事务提交之后生效;

4、 delete from table_name 删除表的全部数据,针对于MyISAM 会立刻释放磁盘空间，InnoDB 不会释放磁盘空间；

5、对于delete from table_name where xxx 带条件的删除, 不管是InnoDB还是MyISAM都不会释放磁盘空间;

6、 delete操作以后使用 optimize table table_name 会立刻释放磁盘空间。不管是InnoDB还是MyISAM 。所以要想达到释放磁盘空间的目的，需要执行optimize table 操作；

7、delete 操作是一行一行执行删除的，并且同时将该行的的删除操作日志记录在redo和undo表空间中以便进行回滚（rollback）和重做操作，生成的大量日志也会占用磁盘空间；

#### 二、truncate (截断表)

1、truncate：属于数据库DDL定义语言，操作truncate时不走事务也不触发触发器 trigger，删除后无法找回数据；

2、 truncate table table_name 时，数据会全部删除但不会删除表的结构，不管是 InnoDB和MyISAM 都会立刻释放磁空间 ，它的操作类似于先删除表后再重新创建表；

3、truncate能够快速清空一个表，并且重置auto_increment的值；

#### 三、drop (删除表)

1、drop：属于数据库DDL定义语言；操作drop时不走事务也不触发触发器 trigger，删除后无法找回数据；

2、 drop table table_name 时不仅数据会被删除同时表结构、触发器、索引、被依赖的约束都会被删除 ，不管是 InnoDB 和 MyISAM都会立刻释放磁盘空间 ，依赖于该表的存储过程/函数将保留,但是变为 invalid 状态；

#### 总结：

从删除权限上看 delete &lt; truncate &lt; drop

从安全程度上看 delete &gt; truncate &gt; drop

从执行速度上看 delete &lt; truncate &lt; drop

truncate和drop操作需谨慎。
