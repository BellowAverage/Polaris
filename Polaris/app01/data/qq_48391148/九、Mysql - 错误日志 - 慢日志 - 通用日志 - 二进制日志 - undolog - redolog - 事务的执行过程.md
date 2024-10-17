
--- 
title:  九、Mysql - 错误日志 - 慢日志 - 通用日志 - 二进制日志 - undolog - redolog - 事务的执行过程 
tags: []
categories: [] 

---
**目录**































































### 知识点1：为什么需要日志信息？

>  
 **日志用来做什么事？** 
 **        1、用来排错。** 
 **        2、用来做数据分析，提升数据库性能等** 
 **        3、了解程序的运行情况，是否健康，了解mysql性能，运行情况** 


**########################################################################## **

###  知识点2：错误日志  error

>  
 **一般错误日志的名字是  ： 主机名.err** 
 **错误日志是Mysq里面默认开启的日志。** 


#### 示例：查看mysql里面的日志变量信息。

```
root@(none) 10:28  mysql&gt;show variables like "%log%";
+--------------------------------------------+---------------------------------------+
| Variable_name                              | Value                                 |
+--------------------------------------------+---------------------------------------+
| back_log                                   | 80                                    |
| binlog_cache_size                          | 32768                                 |
| binlog_checksum                            | CRC32                                 |
| binlog_direct_non_transactional_updates    | OFF                                   |
| binlog_error_action                        | ABORT_SERVER                          |
| binlog_format                              | ROW                                   |
| binlog_group_commit_sync_delay             | 0                                     |
| binlog_group_commit_sync_no_delay_count    | 0                                     |
| binlog_gtid_simple_recovery                | ON                                    |
| binlog_max_flush_queue_time                | 0                                     |
| binlog_order_commits                       | ON                                    |
| binlog_row_image                           | FULL                                  |
| binlog_rows_query_log_events               | OFF                                   |
| binlog_stmt_cache_size                     | 32768                                 |
| binlog_transaction_dependency_history_size | 25000                                 |
| binlog_transaction_dependency_tracking     | COMMIT_ORDER                          |
| expire_logs_days                           | 0                                     |
| general_log                                | OFF                                   |
| general_log_file                           | /data/mysql/localhost.log             |
| innodb_api_enable_binlog                   | OFF                                   |
| innodb_flush_log_at_timeout                | 1                                     |
| innodb_flush_log_at_trx_commit             | 1                                     |
| innodb_locks_unsafe_for_binlog             | OFF                                   |
| innodb_log_buffer_size                     | 16777216                              |
| innodb_log_checksums                       | ON                                    |
| innodb_log_compressed_pages                | ON                                    |
| innodb_log_file_size                       | 50331648                              |
| innodb_log_files_in_group                  | 2                                     |
| innodb_log_group_home_dir                  | ./                                    |
| innodb_log_write_ahead_size                | 8192                                  |
| innodb_max_undo_log_size                   | 1073741824                            |
| innodb_online_alter_log_max_size           | 134217728                             |
| innodb_undo_log_truncate                   | OFF                                   |
| innodb_undo_logs                           | 128                                   |
| log_bin                                    | OFF                                   |
| log_bin_basename                           |                                       |
| log_bin_index                              |                                       |
| log_bin_trust_function_creators            | OFF                                   |
| log_bin_use_v1_row_events                  | OFF                                   |
| log_builtin_as_identified_by_password      | OFF                                   |
| log_error                                  | ./localhost.localdomain.err           |
| log_error_verbosity                        | 3                                     |
| log_output                                 | FILE                                  |
| log_queries_not_using_indexes              | OFF                                   |
| log_slave_updates                          | OFF                                   |
| log_slow_admin_statements                  | OFF                                   |
| log_slow_slave_statements                  | OFF                                   |
| log_statements_unsafe_for_binlog           | ON                                    |
| log_syslog                                 | OFF                                   |
| log_syslog_facility                        | daemon                                |
| log_syslog_include_pid                     | ON                                    |
| log_syslog_tag                             |                                       |
| log_throttle_queries_not_using_indexes     | 0                                     |
| log_timestamps                             | UTC                                   |
| log_warnings                               | 2                                     |
| max_binlog_cache_size                      | 18446744073709547520                  |
| max_binlog_size                            | 1073741824                            |
| max_binlog_stmt_cache_size                 | 18446744073709547520                  |
| max_relay_log_size                         | 0                                     |
| relay_log                                  |                                       |
| relay_log_basename                         | /data/mysql/localhost-relay-bin       |
| relay_log_index                            | /data/mysql/localhost-relay-bin.index |
| relay_log_info_file                        | relay-log.info                        |
| relay_log_info_repository                  | FILE                                  |
| relay_log_purge                            | ON                                    |
| relay_log_recovery                         | OFF                                   |
| relay_log_space_limit                      | 0                                     |
| slow_query_log                             | OFF                                   |
| slow_query_log_file                        | /data/mysql/localhost-slow.log        |
| sql_log_bin                                | ON                                    |
| sql_log_off                                | OFF                                   |
| sync_binlog                                | 1                                     |
| sync_relay_log                             | 10000                                 |
| sync_relay_log_info                        | 10000                                 |
+--------------------------------------------+---------------------------------------+
74 rows in set (0.00 sec)

```

#### 错误日志的位置：

>  
 **        因为我的mysql服务是二进制安装的，我们指定了数据目录，错误日志会放在数据目录里面。** 


```
[root@localhost mysql]# ls
auto.cnf         ibdata1                    mysql               sanchuang        ucar_cloud
ca-key.pem       ib_logfile0                mysql.sock          server-cert.pem  wangsh
ca.pem           ib_logfile1                mysql.sock.lock     server-key.pem
client-cert.pem  ibtmp1                     performance_schema  student
client-key.pem   localhost.localdomain.err  private_key.pem     sys
ib_buffer_pool   localhost.localdomain.pid  public_key.pem      test
[root@localhost mysql]# 

```

####  如果不知道错误日志的位置可以登录mysql服务查找错误日志变量

```
root@(none) 10:34  mysql&gt;show variables like "log_error";
+---------------+-----------------------------+
| Variable_name | Value                       |
+---------------+-----------------------------+
| log_error     | ./localhost.localdomain.err |
+---------------+-----------------------------+
1 row in set (0.01 sec)

```

####  错误日志记录了什么内容？

>  
 **    登录失败会记录到错误日志     配置文件出错也会记录     启动过程出问题也会记录** 


#### 示例：mysql登录失败会记录错误日志。

**使用tail -f 监控日志文件**

```
[root@localhost mysql]# tail -f localhost.localdomain.err 

```

** 错误输入密码：**<img alt="" height="155" src="https://img-blog.csdnimg.cn/25e934f282384ff387e9928bb3373701.png" width="1063">

** 生成错误日志：**

<img alt="" height="390" src="https://img-blog.csdnimg.cn/3fe53badf28c4172a11bd183af9fc933.png" width="1066">

** 日志文件配置错误：**

<img alt="" height="161" src="https://img-blog.csdnimg.cn/d7466c26543c44adbdd59e23bc0c933d.png" width="1062">

** 生成警告**<img alt="" height="291" src="https://img-blog.csdnimg.cn/b9dd434b5bcb491e8e6220352bc62ec5.png" width="1061">



**########################################################################## **

### 知识点3：慢日志  slow_query_log

#### 慢日志有什么作用？

>  
 **作用：记录消耗时间比较长的SQL语句，为数据库性能提升提供了线索** 
 **最近数据库压力（负载特别高），客户反应网站或者应用使用特别慢，领导要求你查明原因？ 1.SQL语句需要优化，在数据库里启用慢日志，找出执行时间比较长的SQL 2.业务量太大了，硬件已经达到极限了  ，top、glances、dstat** 


**慢日志默认是关闭的**

>  
 **如果打开慢日志会将慢日志放在我们定义的数据目录下面。名字是主机名 + slow.log** 


```
root@(none) 10:57  mysql&gt;show variables like "%slow_query%";
+---------------------+--------------------------------+
| Variable_name       | Value                          |
+---------------------+--------------------------------+
| slow_query_log      | OFF                            |
| slow_query_log_file | /data/mysql/localhost-slow.log |
+---------------------+--------------------------------+
2 rows in set (0.00 sec)

```

####  sql语句执行时间多长算慢日志？

<img alt="" height="508" src="https://img-blog.csdnimg.cn/ad168a9b126543f49f5026fd6a9af237.png" width="570">

 <img alt="" height="299" src="https://img-blog.csdnimg.cn/3f565203e0bd4727ae1d589ffa5e3c48.png" width="1200">



>  
 **默认sql语句超过10秒就是慢sql，会记录到慢日志** 


```
root@(none) 10:45  mysql&gt;show variables like "%long_query%";
+-----------------+-----------+
| Variable_name   | Value     |
+-----------------+-----------+
| long_query_time | 10.000000 |
+-----------------+-----------+
1 row in set (0.00 sec)

```

####  在配置文件里面开启慢日志

```
# slow log
slow_query_log = 1
long_query_time = 0.001 # 标准
# 在写入慢日志中包含慢管理语句。
log_slow_admin_statements = 1


```

>  
 **重启配置文件以后就会出现慢日志文件** 


<img alt="" height="187" src="https://img-blog.csdnimg.cn/b457b7a114074131828438e6878a0a6a.png" width="1059">

```
root@(none) 11:34  mysql&gt;show variables like "%slow%";
+---------------------------+--------------------------------+
| Variable_name             | Value                          |
+---------------------------+--------------------------------+
| log_slow_admin_statements | ON                             |
| log_slow_slave_statements | OFF                            |
| slow_launch_time          | 2                              |
| slow_query_log            | ON                             |
| slow_query_log_file       | /data/mysql/localhost-slow.log |
+---------------------------+--------------------------------+
5 rows in set (0.01 sec)

root@(none) 11:35  mysql&gt;

```

>  
 **我们设置了慢日志标准为0.001秒，如果有sql语句超过这个时间的话就会记录到 慢日志里面** 


```
root@(none) 11:52  mysql&gt;show variables like "%slow%";
+---------------------------+--------------------------------+
| Variable_name             | Value                          |
+---------------------------+--------------------------------+
| log_slow_admin_statements | ON                             |
| log_slow_slave_statements | OFF                            |
| slow_launch_time          | 2                              |
| slow_query_log            | ON                             |
| slow_query_log_file       | /data/mysql/localhost-slow.log |
+---------------------------+--------------------------------+
5 rows in set (0.01 sec)

root@(none) 11:52  mysql&gt;

```

<img alt="" height="510" src="https://img-blog.csdnimg.cn/a8e12f6a27e9457ab0bd6212fbffab31.png" width="1043">

**########################################################################## **

### 知识点4:通用日志 general log

>  
 **general 日志，会记录****所有的sql操作** 
 **缺点：会消耗大量的磁盘空间，消耗cpu，内存，磁盘资源** 
 **通用日志名字为 主机名 + .log** 


```
root@(none) 12:13  mysql&gt;show variables like "%general%";
+------------------+---------------------------+
| Variable_name    | Value                     |
+------------------+---------------------------+
| general_log      | OFF                       |
| general_log_file | /data/mysql/localhost.log |
+------------------+---------------------------+
2 rows in set (0.00 sec)

```

>  
 **通用日志默认是关闭的，我们可以在配置文件里面打开通用日志。** 


```
# general 日志
general_log

```

```
root@(none) 12:15  mysql&gt;show variables like "%general%"
    -&gt; ;
+------------------+---------------------------+
| Variable_name    | Value                     |
+------------------+---------------------------+
| general_log      | ON                        |
| general_log_file | /data/mysql/localhost.log |
+------------------+---------------------------+
2 rows in set (0.00 sec)

root@(none) 12:15  mysql&gt;

```

**可以看到，开启general通用日志以后，所有使用过的sql语句都会记录在 localhost.log文件里面**

```
root@(none) 14:40  mysql&gt;use wangsh;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
root@wangsh 14:40  mysql&gt;show tables;
+------------------+
| Tables_in_wangsh |
+------------------+
| shirts           |
| tran_demo        |
+------------------+
2 rows in set (0.00 sec)

root@wangsh 14:40  mysql&gt;desc tran_demo;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

root@wangsh 14:40  mysql&gt;

```

<img alt="" height="674" src="https://img-blog.csdnimg.cn/081e83f9c47e4401b005807aa4a7d8e9.png" width="1042">

**########################################################################## **

###  知识点5：二进制日志 binary log

#### 二进制日志的作用？

>  
 **        可以用来做数据恢复** 
 **        主从复制 ** 


>  
 **二进制日志默认也是没有开启的。** 


```
root@wangsh 14:51  mysql&gt;show variables like "%log_bin%";
+---------------------------------+-------+
| Variable_name                   | Value |
+---------------------------------+-------+
| log_bin                         | OFF   |
| log_bin_basename                |       |
| log_bin_index                   |       |
| log_bin_trust_function_creators | OFF   |
| log_bin_use_v1_row_events       | OFF   |
| sql_log_bin                     | ON    |
+---------------------------------+-------+
6 rows in set (0.00 sec)

```

#### 示例：在配置文件里面开启二进制日志

```
# binary log
log_bin
server_id = 1

```

```
root@(none) 14:54  mysql&gt;show variables like "%log_bin%";
+---------------------------------+---------------------------------+
| Variable_name                   | Value                           |
+---------------------------------+---------------------------------+
| log_bin                         | ON                              |
| log_bin_basename                | /data/mysql/localhost-bin       |
| log_bin_index                   | /data/mysql/localhost-bin.index |
| log_bin_trust_function_creators | OFF                             |
| log_bin_use_v1_row_events       | OFF                             |
| sql_log_bin                     | ON                              |
+---------------------------------+---------------------------------+
6 rows in set (0.00 sec)

root@(none) 14:56  mysql&gt;

```

```
[root@localhost mysql]# ls
auto.cnf         ib_logfile1                mysql               server-key.pem
ca-key.pem       ibtmp1                     mysql.sock          student
ca.pem           localhost-bin.000001       mysql.sock.lock     sys
client-cert.pem  localhost-bin.index        performance_schema  test
client-key.pem   localhost.localdomain.err  private_key.pem     ucar_cloud
ib_buffer_pool   localhost.localdomain.pid  public_key.pem      wangsh
ibdata1          localhost.log              sanchuang
ib_logfile0      localhost-slow.log         server-cert.pem
[root@localhost mysql]# 

```

#### localhost-bin.index 文件：记录了累计共有多少个二进制文件

>  
 **mysqld服务每刷新一次，二进制文件就会增加一个，index文件里面也会新加一个** 


```
[root@localhost mysql]# ls
auto.cnf         ib_logfile1                mysql               server-key.pem
ca-key.pem       ibtmp1                     mysql.sock          student
ca.pem           localhost-bin.000001       mysql.sock.lock     sys
client-cert.pem  localhost-bin.index        performance_schema  test
client-key.pem   localhost.localdomain.err  private_key.pem     ucar_cloud
ib_buffer_pool   localhost.localdomain.pid  public_key.pem      wangsh
ibdata1          localhost.log              sanchuang
ib_logfile0      localhost-slow.log         server-cert.pem
[root@localhost mysql]# cat localhost-bin.index 
./localhost-bin.000001
[root@localhost mysql]# service mysqld restart
Shutting down MySQL.... SUCCESS! 
Starting MySQL. SUCCESS! 
[root@localhost mysql]# ls
auto.cnf         ib_logfile1                localhost-slow.log  server-cert.pem
ca-key.pem       ibtmp1                     mysql               server-key.pem
ca.pem           localhost-bin.000001       mysql.sock          student
client-cert.pem  localhost-bin.000002       mysql.sock.lock     sys
client-key.pem   localhost-bin.index        performance_schema  test
ib_buffer_pool   localhost.localdomain.err  private_key.pem     ucar_cloud
ibdata1          localhost.localdomain.pid  public_key.pem      wangsh
ib_logfile0      localhost.log              sanchuang
[root@localhost mysql]# cat localhost-bin.index 
./localhost-bin.000001
./localhost-bin.000002

```

#### 查看当前使用的是哪个二进制文件  show master status

```
root@(none) 15:00  mysql&gt;show master status;
+----------------------+----------+--------------+------------------+-------------------+
| File                 | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+----------------------+----------+--------------+------------------+-------------------+
| localhost-bin.000002 |      154 |              |                  |                   |
+----------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)

root@(none) 15:00  mysql&gt;

```

####  查看所有二进制文件和大小 show binary logs

```
root@(none) 15:03  mysql&gt;show binary logs;
+----------------------+-----------+
| Log_name             | File_size |
+----------------------+-----------+
| localhost-bin.000001 |       177 |
| localhost-bin.000002 |       205 |
| localhost-bin.000003 |       154 |
+----------------------+-----------+
3 rows in set (0.00 sec)

root@(none) 15:07  mysql&gt;

```

#### 一个二进制文件是否记录了整个mysqld进程里所有的库的操作？

>  
 **是的，对所有库的操作都会记录到一个二进制文件里面，如果需要记录到不同的日志文件里面，可以采用多实例** 


>  
 ** mysq实例：** 
 **        正在运行的一个mysql进程，这个进程里面有哪些库可以操作，二进制日志就记录哪些库的操作** 
 **多实例：** 
 **        多启动几个mysqld的进程，一个mysqld的进程对应一个库** 
 **        隔离应用，避免一个库使用特别频繁，影响其他的库** 
 **        多实例任然受到整个机器整体系统资源的限制** 


**########################################################################## **

### 知识点6：哪些行为会产生新的二进制文件？

####  1、service mysqld restart

#### 2、flush logs；

```
root@(none) 15:00  mysql&gt;flush logs;
Query OK, 0 rows affected (0.00 sec)

root@(none) 15:03  mysql&gt;show master status;
+----------------------+----------+--------------+------------------+-------------------+
| File                 | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+----------------------+----------+--------------+------------------+-------------------+
| localhost-bin.000003 |      154 |              |                  |                   |
+----------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)

root@(none) 15:03  mysql&gt;

```

```
[root@localhost mysql]# ls
auto.cnf         ib_logfile1                localhost.log       sanchuang
ca-key.pem       ibtmp1                     localhost-slow.log  server-cert.pem
ca.pem           localhost-bin.000001       mysql               server-key.pem
client-cert.pem  localhost-bin.000002       mysql.sock          student
client-key.pem   localhost-bin.000003       mysql.sock.lock     sys
ib_buffer_pool   localhost-bin.index        performance_schema  test
ibdata1          localhost.localdomain.err  private_key.pem     ucar_cloud
ib_logfile0      localhost.localdomain.pid  public_key.pem      wangsh
[root@localhost mysql]# 

```

#### 3、当日志达到最大值1G的时候，也会产生新的日志

```
root@(none) 15:07  mysql&gt;show variables like "max_binlog_size";
+-----------------+------------+
| Variable_name   | Value      |
+-----------------+------------+
| max_binlog_size | 1073741824 |
+-----------------+------------+
1 row in set (0.00 sec)

root@(none) 15:15  mysql&gt;

```

```
root@(none) 15:15  mysql&gt;select 1073741824/1024/1024;
+----------------------+
| 1073741824/1024/1024 |
+----------------------+
|        1024.00000000 |
+----------------------+
1 row in set (0.00 sec)

root@(none) 15:17  mysql&gt;

```

 **########################################################################## **

###  知识点7：查看二进制文件 mysqlbinlog

>  
 **此时我们使用的二进制文件是 Localhost-bin.000003** 
 **对数据库进行操作** 


```
root@ucar_cloud 15:33  mysql&gt;use student;
Database changed
root@student 15:34  mysql&gt;shwo tables;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'shwo tables' at line 1
root@student 15:34  mysql&gt;show tables;
Empty set (0.00 sec)

root@student 15:34  mysql&gt;create table test(id int, name varchar(20));
Query OK, 0 rows affected (0.01 sec)

root@student 15:35  mysql&gt;insert into test(id,name) values(1,'wang');
Query OK, 1 row affected (0.00 sec)

```

```
[root@localhost mysql]# mysqlbinlog -v localhost-bin.000003 
# at 535
#220812 15:35:34 server id 1  end_log_pos 580 CRC32 0xdd2e8bd1 	Write_rows: table id 113 flags: STMT_END_F

BINLOG '
xgL2YhMBAAAANQAAABcCAAAAAHEAAAAAAAEAB3N0dWRlbnQABHRlc3QAAgMPAjwAA5EKdrY=
xgL2Yh4BAAAALQAAAEQCAAAAAHEAAAAAAAEAAgAC//wBAAAABHdhbmfRiy7d
'/*!*/;
### INSERT INTO `student`.`test`
### SET
###   @1=1
###   @2='wang'

```

>  
 **at 535    从535位置号开始** 
 **220812 15:35:34    时间** 
 **end_log_pos 580   到 580位置号结束** 


**########################################################################## ** 

###  知识点8：Innodb存储引擎架构

 <img alt="" height="633" src="https://img-blog.csdnimg.cn/f5ae07cc914c4a7089ff3c72122d87b0.png" width="787">

####  redo log

>  
 **redo log的作用：** 
 **        redo log的主要作用是用于数据库的崩溃恢复** 
 **        就是当数据从内存刷到磁盘的时候，突然停电，导致刷盘失败，然后Mysql服务器重启后就会首先看redolog的日志，重新再做一遍，保障数据一致性，不丢失** 


#### **redo log可以简单分为以下两个部分：**

>  
 **        一是内存中重做日志缓冲 (redo log buffer),是易失的，在内存中** 
 **        二是重做日志文件 (redo log file)，是持久的，保存在磁盘中** 


#### redo的整体流程 

<img alt="" height="357" src="https://img-blog.csdnimg.cn/0c85222c3d614469b7f78c59544b1875.png" width="768">

>  
 **redo日志是比数据页先写入磁盘的。 ** 


>  
 **第一步：先将原始数据从磁盘中读入内存中来，修改数据的内存拷贝** 
 **第二步：生成一条重做日志并写入redo log buffer，记录的是数据被修改后的值** 
 **第三步：当事务commit时，将redo log buffer中的内容刷新到 redo log file，对 redo log file采用追加写的方式** 
 **第四步：定期将内存中修改的数据刷新到磁盘中** 
  




#### undo log

>  
 **undolog的作用** 
 **        undo log主要记录的是数据的逻辑变化，为了在发生错误时回滚之前的操作，需要将之前的操作都记录下来，然后在发生错误时才可以回滚。** 
 **        服务器运行时的回滚rollback、MVCC（多版本控制）就是基于此log** 


 **########################################################################## **

### 知识点9：事务的执行过程

>  
 **示例：状态1：A：10，B：10，状态2：A：0，B：20** 


 <img alt="" height="836" src="https://img-blog.csdnimg.cn/47ed8281a22c45259a54a67492976084.png" width="1200">



过程：

>  
        ** 1、从磁盘中读取数据A到内存中** 
 **        2、记录数据到undo.log** 
 **        3、修改A的值为0** 
 **        4、记录修改后的数据到redo.log buffer 里面** 
 **        5、从磁盘中读取数据B到内存中** 
 **        6、记录数据到undo.log** 
 **        7、修改B的值为20** 
 **        8、记录修改后的数据到redo.log buffer 里面，server层标记prepare，准备提交** 
 **        9、bin_log 写入磁盘中** 
 **        10、事务提交，redo.log 在server层标记 commit，数据刷入磁盘中，提交成功，** 
 **        如果中途失败的话，会根据undo.log回滚。** 


               



 参考资料：

        

       
