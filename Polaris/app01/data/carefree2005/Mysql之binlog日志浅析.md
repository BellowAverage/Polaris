
--- 
title:  Mysql之binlog日志浅析 
tags: []
categories: [] 

---
## 一、binlog日志简介

  Binlog是MySQL数据库中的二进制日志，用于记录数据库中所有修改操作，包括增删改等操作。binlog以二进制格式保存，可以通过解析binlog文件来查看数据库的操作历史记录。binlog日志可以用于数据恢复、数据备份、数据同步等场景。在MySQL数据库中，binlog有两种模式：statement模式和row模式。statement模式记录的是SQL语句，row模式记录的是每一行数据的变化。binlog日志的开启和关闭可以通过设置MySQL的配置文件实现。   Binlog是MySQL数据库中非常重要的组件之一，Binlog的全称是Binary Log，它是一种二进制日志文件，记录了MySQL数据库中所有的修改操作，包括增、删、改等。这些修改操作可以通过Binlog进行恢复和备份，从而保证数据的安全性和完整性。   Binlog的作用非常重要，它可以用来进行数据恢复和备份，也可以用来进行数据同步和复制。在进行数据恢复时，可以使用Binlog来恢复数据到某个时间点或某个操作之前的状态，从而保证数据的完整性。在进行数据备份时，可以将Binlog文件备份到另一台服务器上，以便在主服务器出现问题时，可以快速地将备份服务器恢复到与主服务器相同的状态。   除了数据恢复和备份外，Binlog还可以用来进行数据同步和复制。在进行数据同步时，可以将Binlog文件传输到其他服务器上，从而将数据同步到其他服务器中。在进行数据复制时，可以将Binlog文件传输到备份服务器上，从而将备份服务器上的数据与主服务器上的数据保持一致。

## 二、binlog日志常用知识点

### 1、开启binlog日志

  mysql开启binlog的方式是在配置文件中配置参数log-bin = /binlogdir/binlogname，其中binlogdir是binlog日志的存储路径，binlogname是binlog日志文件名前缀，配置了该参数表示启用binlog日志，未配置参数表示禁用binlog日志。生成的binlog日志文件名通常是这样的mybinlog.000001，后面的序号随着使用递增。该参数为静态参数，修改参数后需要重启生效。

<img src="https://img-blog.csdnimg.cn/6674b415d45e42cfb8bd1dbbb23a351d.png" alt="在这里插入图片描述">

### 2、binlog日志文件大小分割

  使用max_binlog_size参数值设定binlog日志文件的大小，举个栗子，max_binlog_size = 1G，表示在binlog日志文件在大于1G的时候进行分割，即文件大小大于1073741824后新生成一个binlog日志文件，序号增1。当然binlog日志文件分割是在结束一个事务操作后的日志记录，所以binlog日志文件实际大小是大于等于1073741824的。

>  
 [bdsc@s250 logs]$ ll total 75945060 -rw-r-----. 1 bdsc bdsc 1074332741 Jun 4 18:53 mybinlog.000001 -rw-r-----. 1 bdsc bdsc 1073822182 Jun 4 20:11 mybinlog.000002 -rw-r-----. 1 bdsc bdsc 1074277669 Jun 4 21:30 mybinlog.000003 … <img src="https://img-blog.csdnimg.cn/4317fcc0e99742b69ffe905a46fc787d.png" alt="在这里插入图片描述"> 


### 3、设置binlog日志保留时间

  使用expire_logs_days参数设置binlog日志保存时间，超过日期的binlog日志将自动清除。

>  
 mysql&gt; show variables like ‘expire_logs_days’; ±-----------------±------+ | Variable_name | Value | ±-----------------±------+ | expire_logs_days | 7 | ±-----------------±------+ 1 row in set (0.01 sec) 


### 4、设置binlog格式

  使用binlog_format参数设置设置binlog日志格式，row格式最可靠，但是会产生大量的binlog日志文件。

>  
 mysql&gt; show variables like ‘binlog_format’; ±--------------±------+ | Variable_name | Value | ±--------------±------+ | binlog_format | ROW | ±--------------±------+ 1 row in set (0.00 sec) 


### 5、查看binlog日志内容

  binlog日志文件是二进制格式，直接查看是乱码，我们可以使用mysqlbinlog命令查看日志文件。日志文件里会记录日志的起始位置，以及执行的sql语句。查看的时候还可以使用参数查看指定时间段内的某数据库的日志。也可以使用命令“mysqlbinlog --start-postion=107 --stop-position=1000 -d 库名 二进制文件”查看指定位置之间的某数据库日志。

>  
 mysqlbinlog --start-datetime=‘2023-06-01 00:00:00’ --stop-datetime=‘2023-06-10 00:00:00’ -d utest mybinlog.000068 


<img src="https://img-blog.csdnimg.cn/c09ea62694394aebbb01994ccbf0ea7d.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/0f94b3ed09f74114b115eccce3b8c750.png" alt="在这里插入图片描述">

### 6、按照binlog名称清理binlog日志

  我们可以在sql脚本中使用“PURGE BINARY LOGS BEFORE DATE_SUB(NOW(), INTERVAL 7 DAY);”命令清理历史binlog日志，也可以在交互模式下按照名称清理binlog日志。

>  
 mysql&gt; purge binary logs to ‘mybinlog.000005’; Query OK, 0 rows affected (0.19 sec) 


<img src="https://img-blog.csdnimg.cn/60ebd05017344cadb1c1b8f0ab761529.png" alt="在这里插入图片描述">

### 7、按照时间清理binlog日志

  我们可以使用命令purge binary logs before time方式删除指定时间前的binlog日志。

>  
 mysql&gt; purge binary logs before ‘2023-06-5 10:12:00’; Query OK, 0 rows affected (0.55 sec) 


<img src="https://img-blog.csdnimg.cn/008448066ee5420db6fb1b437bdde2c7.png" alt="在这里插入图片描述">

### 8、导出binlog日志

  导出binlog日志文件实际上就是查看的时候通过重定向的方式将日志内容输入到指定的文件。

>  
 [bdsc@s250 logs]$ mysqlbinlog --start-datetime=‘2023-06-01 00:00:00’ --stop-datetime=‘2023-06-10 00:00:00’ mybinlog.000068 &gt; /tmp/utest.log 


<img src="https://img-blog.csdnimg.cn/3b74d93fe4b5408a9306b708b2b9c304.png" alt="在这里插入图片描述">

### 9、记录部分binlog日志

  可以使用binlog-do-db、binlog-ignore-db、binlog-do-table、binlog-ignore-table这四个参数自定义需要记录binlog日志的数据库和表。这四个参数常用于mysql搭建部分表主从模式，见博文。

## 三、binlog日志三种格式简介

  MySQL的binlog日志有三种格式，分别是Statement格式、Row格式和Mixed格式。
- Statement格式 Statement格式是最简单的binlog格式，记录的是执行的SQL语句，可以通过解析SQL语句来恢复数据。这种格式的优点是简单、易于理解和分析，缺点是可能会出现数据不一致的情况，因为同一个SQL语句在不同的环境下可能会产生不同的结果。- Row格式 Row格式是记录每一行数据的变化，包括插入、删除和更新操作。这种格式的优点是数据恢复准确、不会出现数据不一致的情况，缺点是日志量大，对于大量的数据变化会产生大量的日志。- Mixed格式 Mixed格式是Statement格式和Row格式的混合体，MySQL会自动选择使用哪种格式来记录日志。对于简单的SQL语句，使用Statement格式，对于复杂的SQL语句，使用Row格式。这种格式的优点是兼顾了简单和复杂情况下的优点，缺点是可能会出现数据不一致的情况。