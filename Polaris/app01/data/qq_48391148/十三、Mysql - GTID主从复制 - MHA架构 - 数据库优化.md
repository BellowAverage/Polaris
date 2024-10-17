
--- 
title:  十三、Mysql - GTID主从复制 - MHA架构 - 数据库优化 
tags: []
categories: [] 

---
**目录**













































## 全局事务标识符 (GTID)

>  
 ** 全局事务标识符 (GTID) 是****在源服务器（源）上创建并与提交的每个事务相关联的唯一标识符****。这个标识符不仅对于它起源的服务器是唯一的，而且在给定的复制拓扑中的所有服务器中都是****唯一****的。** 
 **GTID 分配区分在源上提交的客户端事务和在副本上复制的复制事务。当客户端事务在源上提交时，它会被分配一个新的 GTID，前提是该事务已写入二进制日志。保证客户端事务具有单调递增的 GTID，生成的数字之间没有间隙。如果客户端事务没有写入二进制日志（例如，因为事务被过滤掉，或者事务是只读的），则不会在源服务器上为其分配 GTID。** 


### GTID的优势

>  
 **比起 binlog + position 的传统方式，在恢复的时候，不需要指定二进制日志文件和位置号了，降低了故障切换的难度，提高了效率** 


## 主从复制实验之开启GTID功能的半同步复制

### 步骤：

#### **在master配置文件上面开启GTID功能**

```
# slow log
slow_query_log = 1
long_query_time = 0.001 # 标准
# 在写入慢日志中包含慢管理语句。
log_slow_admin_statements = 1

# general 日志
general_log

# binary log
log_bin
server_id = 1
# 只保留最近7天的二进制日志
expire_logs_days = 7
# 开启GTID功能
gtid-mode=on
enforce-gtid-consistency = on

# 开启半同步复制
rpl_semi_sync_master_enabled=1
rpl_semi_sync_master_timeout=1000 # 1 second

```

**################################################# **

#### ** 在slave上面开启gtid功能**

```
# 二进制日志
log-bin
server_id = 2

# 开启半同步
rpl_semi_sync_slave_enabled=1

log_slave_updates = on

# 开启GTID
gtid-mode=on
enforce-gtid-consistency = on

```

**################################################# ** 

#### 清除master上的二进制日志，起到一个让实验过程更加清晰的效果

```
root@(none) 21:40  mysql&gt;reset master;
Query OK, 0 rows affected (0.00 sec)

root@(none) 22:06  mysql&gt;show master status;
+----------------------+----------+--------------+------------------+-------------------+
| File                 | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+----------------------+----------+--------------+------------------+-------------------+
| localhost-bin.000001 |      154 |              |                  |                   |
+----------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)

root@(none) 22:06  mysql&gt;

```

>  
 **查看slave机器状态，发现IO线程是关闭状态。先将salve停止，然后在重新配置master信息** 


```
root@(none) 21:41  mysql&gt;show slave status\G;
*************************** 1. row ***************************
               Slave_IO_State: 
                  Master_Host: 192.168.44.170
                  Master_User: liu
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: localhost-bin.000002
          Read_Master_Log_Pos: 523
               Relay_Log_File: network-relay-bin.000008
                Relay_Log_Pos: 4
        Relay_Master_Log_File: localhost-bin.000002
             Slave_IO_Running: No
            Slave_SQL_Running: Yes
root@(none) 21:41  mysql&gt;stop slave;
Query OK, 0 rows affected (0.00 sec)

root@(none) 22:09  mysql&gt;CHANGE MASTER TO MASTER_HOST='192.168.44.170' ,
    -&gt; MASTER_USER='liu',
    -&gt; MASTER_PASSWORD='Sanchuang1234#',
    -&gt; MASTER_PORT=3306,
    -&gt; master_auto_position=1;
Query OK, 0 rows affected, 2 warnings (0.00 sec)

root@(none) 22:11  mysql&gt;start slave;
Query OK, 0 rows affected (0.01 sec)

root@(none) 22:12  mysql&gt;show slave status\G;
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 192.168.44.170
                  Master_User: liu
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: localhost-bin.000001
          Read_Master_Log_Pos: 154
               Relay_Log_File: network-relay-bin.000002
                Relay_Log_Pos: 375
        Relay_Master_Log_File: localhost-bin.000001
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes


```

**################################################# ** 

>  
 <h4 id="%E6%B5%8B%E8%AF%95master%E5%92%8Cslave%E7%9A%84%E6%95%B0%E6%8D%AE%E4%B8%80%E8%87%B4%E6%80%A7">**测试master和slave的数据一致性**</h4> 


```
root@(none) 22:06  mysql&gt;create database gtid_test;
Query OK, 1 row affected (0.00 sec)


root@(none) 22:12  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| gtid_test          |
| liuhongjie         |
| mysql              |
| performance_schema |
| sanchuang          |
| student            |
| sys                |
| test               |
| ucar_cloud         |
| wangsh             |
| zhaojunjie         |
+--------------------+
12 rows in set (0.00 sec)

root@(none) 22:14  mysql&gt;

```

**################################################# ** 

>  
 **在二进制日志里面可以看到gtid ** 


<img alt="" height="532" src="https://img-blog.csdnimg.cn/cae3a9ab5af54893b0b50a923fa95695.png" width="1048">

**################################################# ** 

## MHA架构

### 什么是MHA？

>  
 **MHA（MasterHigh Availability）是一套优秀的MySQL高可用环境下故障切换和主从复制的软件。** 
 **MHA 能够在30秒内实现故障切换，并能在故障切换中，最大可能的保证数据一致性。** 


**################################################# ** 

### MHA服务的两种角色

 MHA 服务有两种角色， MHA Manager(管理节点)和 MHA Node(数据节点)：

>  
 **MHA Manager： 　　通常单独部署在一台独立机器上管理多个 master/slave 集群(组)，每个 master/slave 集群称作一个 application，用来管理统筹整个集群。MHA node： 　　运行在每台 MySQL 服务器上(master/slave/manager)，它通过监控具备解析和清理 logs 功能的脚本来加快故障转移。 　　主要是接收管理节点所发出指令的代理，代理需要运行在每一个 mysql 节点上。简单讲 node 就是用来收集从节点服务器上所生成的 bin-log 。对比打算提升为新的主节点之上的从节点的是否拥有并完成操作，如果没有发给新主节点在本地应用后提升为主节点。** 


**################################################# ** 

### MHA工作原理

>  
 **MHA工作原理总结为以下几条： （1） 从宕机崩溃的 master 保存二进制日志事件（binlog events）； （2） 识别含有最新更新的 slave ； （3） 应用差异的中继日志(relay log) 到其他 slave ； （4） 应用从 master 保存的二进制日志事件(binlog events)； （5） 提升一个 slave 为新 master ； （6） 使用其他的 slave 连接新的 master 进行复制。 ** 


**################################################# ** 

### MHA架构图

 <img alt="" height="630" src="https://img-blog.csdnimg.cn/c2d1de6dbc7942b6b38bb571280ded47.png" width="1172">

** 参考：**

        

 **################################################# ** 

##  数据库优化

### 为什么要优化

>  
 - **系统的吞吐量瓶颈往往出现在数据库的访问速度上**- **随着应用程序的运行，数据库的中的数据会越来越多，处理时间会相应变慢**- **数据是存放在磁盘上的，读写速度无法和内存相比** 
 **优化原则：减少系统瓶颈，减少资源占用，增加系统的反应速度。** 


###  数据库优化方法：

#### 升级硬件，添加服务器 

#### 系统参数调优，内存，文件系统，内核等参数调优

#### 数据库结构优化

>  
 **一个好的数据库设计方案对于数据库的性能往往会起到事半功倍的效果。** 
 **需要考虑数据冗余、查询和更新的速度、字段的数据类型是否合理等多方面的内容。** 


#### 将字段很多的表分解成多个表

>  
 **对于字段较多的表，如果有些字段的使用频率很低，可以将这些字段分离出来形成新表。** 
 **因为当一个表的数据量很大时，会由于使用频率低的字段的存在而变慢。** 


#### 增加中间表

>  
 **对于需要经常联合查询的表，可以建立中间表以提高查询效率。** 
 **通过建立中间表，将需要通过联合查询的数据插入到中间表中，然后将原来的联合查询改为对中间表的查询。**   


#### 架构调优

>  
 ** 增加中间件，分布式集群** 


 
