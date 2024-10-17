
--- 
title:  MySQL update生命周期 
tags: []
categories: [] 

---
        本文只针对InnoDB这种存储引擎做介绍。

**目录**



















        一条 SQL 语句的执行主要是通过Server 层和存储引擎层来执行的。

### 1. Server层        <img alt="" src="https://img-blog.csdnimg.cn/d106079717f246c59bcb449393408306.jpeg">

#### 1.1 连接池

与客户端建立连接、管理连接、账号密码权限的验证。

#### 1.2 解析器

在连接池验证通过后，分析器会对SQL语句进行解析，同时判断是否语法有错误，如果有语法错误则直接抛出异常不再继续执行。

#### 1.3 优化器

将SQL语句进行优化，选择可使用的索引并生成执行计划。

#### 1.4 执行器

根据优化器生成的执行计划，调用存储引擎 API 执行 SQL。

### 2. 存储引擎层

<img alt="" src="https://img-blog.csdnimg.cn/abf947b0ecca4e65a89a7da635336bca.jpeg">

#### 2.1 事务执行过程

1. 首先会判断语句涉及的数据页是否存在于 BP(buffer pool)中，如果存在则直接从缓存池中读取数据行，如果不存在则从磁盘中读取该行记录所在的数据页并加载到BP缓冲池中。

2. 读取到对应的数据行后判断该数据行是否有加锁如果有则需要等待锁先释放，如果没有则直接对该数据行进行加锁，这里加的锁是排他锁。

3. 将修改前的记录写入undo log中，修改当前行的值并记录当前的事务编号，然后使用回滚指针指向undo log中的修改前的行，用于回滚数据和实现MVCC多版本。

4. 写redo log buffer，先判断 redo log buffer 是否够用，不够用则等待，然后将对应行记录的字段值做更新操作，并把修改操作记录到 redo log buffer 中。

5. 写 binlog cache，将修改的信息以对应 event 格式写入 binlog cache 中。

6. 写 change buffe，如果此次 update 操作涉及到二级索引的修改，则写入 change buffer page，等到下次有其他sql需要读取该二级索引的时候，再去与二级索引做合并。

#### 2.2 事务提交过程

InnpDB中的事务提交分为prepare和commit两个阶段。

1. redo log prepare，写入事务的编号，将redo log buffer刷到redo log磁盘文件中，用于异常恢复。

2. binlog write &amp; fsync，把binlog cache 里的完整事务和 redo log prepare 中的事务编号 event 写入到 binlog 中，同时执行fsync将数据刷新到磁盘中，然后清空binlog cache。

3. redo log commit，在 redo log 里标记 commit。

4. 事务执行成功后，释放排他锁。

5. 将修改后的数据刷新到数据页中。
