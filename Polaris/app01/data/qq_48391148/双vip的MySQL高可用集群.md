
--- 
title:  双vip的MySQL高可用集群 
tags: []
categories: [] 

---
<img alt="" height="580" src="https://img-blog.csdnimg.cn/a9e53192f3ce4bf2ac16a9e7cbb225dd.png" width="1200">

**目录**





































































## 一、mysql集群的搭建 

准备四台装好centos7系统的服务器

### IP地址规划：

```
master：192.168.44.170    --&gt; 主

slave1：192.168.44.160    --&gt; 从1

slave2：192.168.44.140   --&gt; 从2

backup_server:192.168.44.203  --&gt; 延迟备份服务器
```

**#################################################################################### **

### 使用ansible给从服务器安装mysql 

#### 1、使用master与所有从服务器建立SSH免密通道，然后添加到mysqld组到hosts文件里面

示例：将从服务器IP地址添加到/etc/ansible/hosts文件里面的mysqlserver组

```
[root@master ansible]# cat hosts
[mysqlserver]
192.168.44.140
192.168.44.160
192.168.44.203

```

测试ansible是否与三台从服务器建立连接

```
[root@master ansible]# ansible all -m shell -a "mkdir /root/mysql_test.txt"

192.168.44.160 | CHANGED | rc=0 &gt;&gt;

192.168.44.140 | CHANGED | rc=0 &gt;&gt;

192.168.44.203 | CHANGED | rc=0 &gt;&gt;

```

>  
 **效果：三台机器上都成功新建一个mysql_test.txt文件** 


```
[root@slave1 ~]# ls
mysql_test.txt
```

```
[root@slave2 ~]# ls
mysql_test.txt  

```

```
[root@backup_server ~]# ls
mysql_test.txt

```

**#################################################################################### ** 

#### 2、使用ansible给从服务器部署mysql（5.7.34）

使用ansible将mysql软件压缩包copy到从服务器上面，这里因为slave1上面已经安装mysql，所以没有传

```
[root@master ~]# ansible all -m copy -a "src=/root/mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz dest=/root/"
192.168.44.203 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "checksum": "c401420251b9eae3b95c21753a925675bc731df3", 
    "dest": "/root/mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz", 
    "gid": 0, 
    "group": "root", 
    "md5sum": "cdf3bec90f7dd576397b23d1ddb399c5", 
    "mode": "0644", 
    "owner": "root", 
    "secontext": "system_u:object_r:admin_home_t:s0", 
    "size": 665389778, 
    "src": "/root/.ansible/tmp/ansible-tmp-1663061649.05-19487-87578574739390/source", 
    "state": "file", 
    "uid": 0
}
192.168.44.140 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "checksum": "c401420251b9eae3b95c21753a925675bc731df3", 
    "dest": "/root/mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz", 
    "gid": 0, 
    "group": "root", 
    "md5sum": "cdf3bec90f7dd576397b23d1ddb399c5", 
    "mode": "0644", 
    "owner": "root", 
    "secontext": "system_u:object_r:admin_home_t:s0", 
    "size": 665389778, 
    "src": "/root/.ansible/tmp/ansible-tmp-1663061649.08-19486-277324168009261/source", 
    "state": "file", 
    "uid": 0
}
[root@master ~]# 

```

>  
 **使用ansible将一键二进制安装脚本copy给从服务器** 


```
[root@master ~]# ansible all -m copy -a "src=/root/onekey_install_mysql_binary_v3.sh  dest=/root/"
192.168.44.203 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "checksum": "0747136284b8c9d2d605e6a62358e4b3382d956f", 
    "dest": "/root/onekey_install_mysql_binary_v3.sh", 
    "gid": 0, 
    "group": "root", 
    "md5sum": "1d46566cecdd2bef46e6815ad978b1c8", 
    "mode": "0644", 
    "owner": "root", 
    "secontext": "system_u:object_r:admin_home_t:s0", 
    "size": 3086, 
    "src": "/root/.ansible/tmp/ansible-tmp-1663067531.62-19593-204811003943206/source", 
    "state": "file", 
    "uid": 0
}
192.168.44.140 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "checksum": "0747136284b8c9d2d605e6a62358e4b3382d956f", 
    "dest": "/root/onekey_install_mysql_binary_v3.sh", 
    "gid": 0, 
    "group": "root", 
    "md5sum": "1d46566cecdd2bef46e6815ad978b1c8", 
    "mode": "0644", 
    "owner": "root", 
    "secontext": "system_u:object_r:admin_home_t:s0", 
    "size": 3086, 
    "src": "/root/.ansible/tmp/ansible-tmp-1663067531.68-19591-45378666974808/source", 
    "state": "file", 
    "uid": 0
}

```

>  
 **使用ansible给所有从服务器执行一键安装脚本** 


```
[root@master ~]# ansible all -m shell -a "bash /root/onekey_install_mysql_binary_v3.sh"
```

**安装成功效果：**

<img alt="" height="610" src="https://img-blog.csdnimg.cn/63bd2c9096c24d1fbb5062ddede1fe9b.png" width="1200">

<img alt="" height="564" src="https://img-blog.csdnimg.cn/b1726685630847f39ac9d3fc7d451888.png" width="1200">

**#################################################################################### ** 

### 在master和slave集群配置异步复制

#### 1、先将master的数据库全备导出，然后在slave导入，达到两边数据库的基础数据一致

>  
 **使用mysqldump 将数据库全备导出** 


```
[root@master backup]# mysqldump -uroot -p'Sanchuang123#' --all-databases &gt;/backup/all_db.sql
mysqldump: [Warning] Using a password on the command line interface can be insecure.
Warning: A partial dump from a server that has GTIDs will by default include the GTIDs of all transactions, even those that changed suppressed parts of the database. If you don't want to restore GTIDs, pass --set-gtid-purged=OFF. To make a complete dump, pass --all-databases --triggers --routines --events. 
[root@master backup]# ls
all_db.sql

```

>  
 ** master和slave配置里面要开启二进制日志以及server_id ** 


master配置：

```
# binary log
log_bin
server_id = 1

```

slave1配置

```
# 二进制日志
log-bin
server_id = 2

```

slave2配置

```
# 开启二进制日志
log_bin
server_id = 3


```

backup_server配置

```
# 开启二进制日志
log_bin
server_id = 4


```

>  
 **将master导出的全备份sql文件使用ansible传到slave机器上，然后导入** 


```
[root@master backup]# ansible all -m copy -a "src=/backup/all_db.sql dest=/root/backup"
192.168.44.160 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "checksum": "10ec634ad8d698aa0a05f00f3526ee80008cac98", 
    "dest": "/root/backup/all_db.sql", 
    "gid": 0, 
    "group": "root", 
    "md5sum": "227bf971bfba9df5da84ca696b2e3a55", 
    "mode": "0644", 
    "owner": "root", 
    "size": 899886, 
    "src": "/root/.ansible/tmp/ansible-tmp-1663122288.81-19992-243949179800744/source", 
    "state": "file", 
    "uid": 0
}
192.168.44.203 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "checksum": "10ec634ad8d698aa0a05f00f3526ee80008cac98", 
    "dest": "/root/backup/all_db.sql", 
    "gid": 0, 
    "group": "root", 
    "md5sum": "227bf971bfba9df5da84ca696b2e3a55", 
    "mode": "0644", 
    "owner": "root", 
    "secontext": "system_u:object_r:admin_home_t:s0", 
    "size": 899886, 
    "src": "/root/.ansible/tmp/ansible-tmp-1663122289.14-19993-173407275816877/source", 
    "state": "file", 
    "uid": 0
}
192.168.44.140 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "checksum": "10ec634ad8d698aa0a05f00f3526ee80008cac98", 
    "dest": "/root/backup/all_db.sql", 
    "gid": 0, 
    "group": "root", 
    "md5sum": "227bf971bfba9df5da84ca696b2e3a55", 
    "mode": "0644", 
    "owner": "root", 
    "secontext": "system_u:object_r:admin_home_t:s0", 
    "size": 899886, 
    "src": "/root/.ansible/tmp/ansible-tmp-1663122289.17-19991-31806854150922/source", 
    "state": "file", 
    "uid": 0
}
[root@master backup]# 

```

>  
 **在slave和延迟备份服务器backup_server上面导入master的全备份** 


```
[root@slave1 backup]# mysql -uroot -p'Sanchuang123#' &lt; all_db.sql
mysql: [Warning] Using a password on the command line interface can be insecure.


[root@slave2 backup]# mysql -uroot -p'Sanchuang123#' &lt;all_db.sql
mysql: [Warning] Using a password on the command line interface can be insecure.


[root@backup_server backup]# mysql -uroot -p'Sanchuang123#' &lt;all_db.sql
mysql: [Warning] Using a password on the command line interface can be insecure.

```

>  
 **查看数据现在是否达到一致，可以看到每个数据库的数据已经一致** 


<img alt="" height="678" src="https://img-blog.csdnimg.cn/9357a5ba585646fe8e2ccec570c8e8c5.png" width="1200">

**#################################################################################### ** 

####  2、在master上创建一个由备份权限的授权用户，然后在slave上添加授权用户的信息

```
root@mysql 10:31  mysql&gt;create user 'chen'@'%' identified by '123456';
Query OK, 0 rows affected (1.01 sec)

root@mysql 10:40  mysql&gt;grant replication slave on *.* to 'chen'@'%';
Query OK, 0 rows affected (0.00 sec)


```

查看master相关信息

```
root@(none) 16:03  mysql&gt;show master status;
+-------------------+----------+--------------+------------------+-------------------------------------------+
| File              | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set                         |
+-------------------+----------+--------------+------------------+-------------------------------------------+
| master-bin.000002 |      194 |              |                  | 0294c53c-06a2-11ed-98a8-000c29f3aa67:1-29 |
+-------------------+----------+--------------+------------------+-------------------------------------------+
1 row in set (0.00 sec)

```

>  
 **在slave1和slave2以及backup_server 上面添加授权用户信息** 


```
root@(none) 16:07  mysql&gt;CHANGE MASTER TO MASTER_HOST='192.168.44.170' ,
    -&gt; MASTER_USER='chen',
    -&gt; MASTER_PASSWORD='123456',
    -&gt; MASTER_PORT=3306,
    -&gt; MASTER_LOG_FILE='master-bin.000002',
    -&gt; MASTER_LOG_POS=194;
Query OK, 0 rows affected, 2 warnings (0.01 sec)

```

>  
 **查看slave状态：可以看到IO线程和SQL线程并没有开启，这是因为我们还没有开启slave角色导致的** 


```
root@(none) 10:52  mysql&gt;show slave status\G;
*************************** 1. row ***************************
               Slave_IO_State: 
                  Master_Host: 192.168.44.170
                  Master_User: chen
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: master-bin.000001
          Read_Master_Log_Pos: 605
               Relay_Log_File: slave1-relay-bin.000001
                Relay_Log_Pos: 4
        Relay_Master_Log_File: master-bin.000001
             Slave_IO_Running: No
            Slave_SQL_Running: No

```

>  
 **start slave ：在slave1和slave2以及backup_server上开启slave角色，然后就可以看到IO线程和SQL线程都已经开启** 


```
root@(none) 10:53  mysql&gt;start slave;
Query OK, 0 rows affected (0.08 sec)

root@(none) 10:55  mysql&gt;show slave status\G;
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 192.168.44.170
                  Master_User: chen
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: master-bin.000001
          Read_Master_Log_Pos: 605
               Relay_Log_File: slave1-relay-bin.000002
                Relay_Log_Pos: 321
        Relay_Master_Log_File: master-bin.000001
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes

```

>  
 **所有从服务器都开启slave后，测试数据的一致性** 
 **在master上面删除zhaojunjie数据库，发现从服务上面的zhaojunjie数据库也被删除了** 


```
root@(none) 16:13  mysql&gt;drop database zhaojunjie;
Query OK, 1 row affected (0.01 sec)

```

```
root@(none) 16:12  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| flask_ht           |
| gtid_test          |
| kafka_data         |
| mysql              |
| performance_schema |
| sanchuang          |
| student            |
| sys                |
| test               |
| ucar_cloud         |
| wangsh             |
| wenlaoshi          |
| zhaojunjie         |
+--------------------+
14 rows in set (0.00 sec)

root@(none) 16:13  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| flask_ht           |
| gtid_test          |
| kafka_data         |
| mysql              |
| performance_schema |
| sanchuang          |
| student            |
| sys                |
| test               |
| ucar_cloud         |
| wangsh             |
| wenlaoshi          |
+--------------------+
13 rows in set (0.00 sec)

root@(none) 16:17  mysql&gt;

```

>  
 **此时我们的mysql集群就完成了异步复制** 


**#################################################################################### ** 

### 给mysql集群部署基于gtid的主从复制

#### 1、关闭所有从服务器上的slave服务

```
root@(none) 16:13  mysql&gt;stop slave;
Query OK, 0 rows affected (0.01 sec)

```

#### 2、编辑master和从服务器的配置文件，添加gtid功能

```
gtid-mode=on
enforce-gtid-consistency = on

```

#### 3、重启master和从服务器的mysql服务

```
[root@backup_server ~]# service mysqld restart
Shutting down MySQL.. SUCCESS! 
Starting MySQL.. SUCCESS! 

```

>  
 **重启服务后登陆mysql服务，发现IO线程和SQL线程都已经处于开启状态，至此，基于gtid的主从复制部署完成** 


**#################################################################################### **

### 给backup_server配置延迟备份

####  1、首先停止 backup_server的salve功能

```
root@(none) 16:48  mysql&gt;stop slave ;
Query OK, 0 rows affected (0.00 sec)

```

#### 2、在backup_server上设置延迟时间，然后开启slave

>  
 **为了后面测试延迟备份，设置延迟时间为10s，在生产环境应该把这个时间调大点，给灾备情况给出缓冲时间** 


```
root@(none) 16:49  mysql&gt;CHANGE MASTER TO MASTER_DELAY = 10;
Query OK, 0 rows affected (0.00 sec)

root@(none) 16:50  mysql&gt;start slave;
Query OK, 0 rows affected (0.00 sec)

```

<img alt="" height="437" src="https://img-blog.csdnimg.cn/b65bbd17c9744b5fba3f0f9f77eeba0e.png" width="1200">

####  3、测试延迟备份的效果

>  
 **在master上新建数据库delay_test，观察数据一致性情况** 
 **可以很清楚地看到，slave1和slave2上的数据很快同步，出现了delay_test数据库，但是backup_server延时备份服务器上30s后才同步，** 


```
root@(none) 16:54  mysql&gt;create database delay_test;
Query OK, 1 row affected (0.00 sec
```

```
root@(none) 16:54  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| delay_test         |
| flask_ht           |
| gtid_test          |
| kafka_data         |
| mysql              |
| performance_schema |
| sanchuang          |
| student            |
| sys                |
| test               |
| ucar_cloud         |
| wangsh             |
| wenlaoshi          |
+--------------------+
14 rows in set (0.00 sec)


```

>  
 **至此，基于gtid和延迟备份的mysql主从复制集群搭建完毕** 


 **#################################################################################### **

### 部署基于gtid的半同步复制

>  
 **在master和所有slave服务器上做相同操作，部署半同步复制** 


#### 1、首先在master上面安装插件

```
root@(none) 15:42  mysql&gt;INSTALL PLUGIN rpl_semi_sync_master SONAME 'semisync_master.so';
Query OK, 0 rows affected (0.01 sec)
```

#### 2、设置master全局变量和超时时间

```
root@(none) 15:46  mysql&gt;SET GLOBAL rpl_semi_sync_master_enabled = 1;
Query OK, 0 rows affected (0.00 sec)
 
root@(none) 15:47  mysql&gt;
```

>  
 **查看变量是否开启 ** 


```
root@(none) 15:47  mysql&gt;show variables like "%semi_sync%";
+-------------------------------------------+------------+
| Variable_name                             | Value      |
+-------------------------------------------+------------+
| rpl_semi_sync_master_enabled              | ON         |
| rpl_semi_sync_master_timeout              | 10000      |
| rpl_semi_sync_master_trace_level          | 32         |
| rpl_semi_sync_master_wait_for_slave_count | 1          |
| rpl_semi_sync_master_wait_no_slave        | ON         |
| rpl_semi_sync_master_wait_point           | AFTER_SYNC |
+-------------------------------------------+------------+
6 rows in set (0.01 sec)
 
root@(none) 15:48  mysql&gt;
```

#### 3、在slave上面安装插件，设置全局变量 

```
root@(none) 15:51  mysql&gt;INSTALL PLUGIN rpl_semi_sync_slave SONAME 'semisync_slave.so';
Query OK, 0 rows affected (0.00 sec)
 
root@(none) 15:51  mysql&gt;
```

```
root@(none) 15:52  mysql&gt;SET GLOBAL rpl_semi_sync_slave_enabled = 1;
Query OK, 0 rows affected (0.00 sec)
 
```

####  4、停止slave上面的I/O线程，然后重启I/O线程

```
root@(none) 15:53  mysql&gt;STOP SLAVE IO_THREAD;
Query OK, 0 rows affected (0.00 sec)
 
root@(none) 15:57  mysql&gt;START SLAVE IO_THREAD;
Query OK, 0 rows affected (0.00 sec)
 
root@(none) 15:58  mysql&gt;
```

>  
 **至此，gtid的半同步复制mysql集群就部署完成 ** 


  **#################################################################################### **

###  mysqlrouter读写分离部署实现

>  
 ** MySQL Router是MySQL官方提供的一个轻量级中间件，可以在应用程序与MySQL服务器之间提供透明的路由方式。主要用以解决MySQL主从库集群的高可用、、易扩展等问题。** 


#### 1、准备两台全新的linux服务器，安装好mysqlrouter软件 

>  
 **proxy-1 ：192.168.44.132** 
 **proxy-2： 192.168.44.166 ** 


**修改mysqlrouter的配置文件**

>  
 **proxy-1配置文件修改：** 


```
# 名字可以自定义
[routing:read_write]
#是mysql-router服务器的ip地址
bind_address = 192.168.44.132
bind_port = 7001
#支持可读可写
mode = read-write
#mysql-master服务器的ip地址：mysql服务的端口号
destinations = 192.168.44.170:3306
max_connections = 65535
max_connect_errors = 100
client_connect_timeout = 9

[routing:read_only]
#是mysql-router服务器的ip地址
bind_address = 192.168.44.132
bind_port = 7002
# 仅可读
mode = read-only
# mysql-slave服务器的ip地址：mysql服务的端口号
destinations = 192.168.44.170:3306,192.168.44.140:3306,192.168.44.160:3306
max_connections = 65535
max_connect_errors = 100
client_connect_timeout = 9

```

>  
 **proxy-2配置文件修改： ** 


```
# 名字可以自定义
[routing:read_write]  
#是mysql-router服务器的ip地址
bind_address = 192.168.44.166    
bind_port = 7001
#支持可读可写
mode = read-write  
#mysql-master服务器的ip地址：mysql服务的端口号
destinations = 192.168.44.170:3306 
max_connections = 65535
max_connect_errors = 100
client_connect_timeout = 9

[routing:read_only]
#是mysql-router服务器的ip地址
bind_address = 192.168.44.166 
bind_port = 7002
# 仅可读
mode = read-only 
# mysql-slave服务器的ip地址：mysql服务的端口号
destinations = 192.168.44.170:3306,192.168.44.140:3306,192.168.44.160:3306 
max_connections = 65535
max_connect_errors = 100
client_connect_timeout = 9
```

>  
 **重启mysqlrouter服务，可以看到mysqlrouter进程和7001,7002端口已经开启，说明mysqlrouter服务已经成功启动** 


```
[root@proxy-1 ~]# service mysqlrouter restart
Redirecting to /bin/systemctl restart mysqlrouter.service
[root@proxy-1 ~]# ps aux | grep mysqlrouter
mysqlro+   3455  0.3  0.9 515444  9892 ?        Ssl  22:18   0:00 /usr/bin/mysqlrouter
root       3464  0.0  0.0 112824   992 pts/0    R+   22:18   0:00 grep --color=auto mysqlrouter
[root@proxy-1 ~]# netstat -anplut |grep mysqlrouter
tcp        0      0 192.168.44.132:7001     0.0.0.0:*               LISTEN      3455/mysqlrouter    
tcp        0      0 192.168.44.132:7002     0.0.0.0:*               LISTEN      3455/mysqlrouter  
```

```
[root@proxy-2 mysqlrouter]# service mysqlrouter restart
Redirecting to /bin/systemctl restart mysqlrouter.service
[root@proxy-2 mysqlrouter]# ps aux |grep mysql
mysqlro+   2813  0.5  0.9 515444  9924 ?        Ssl  22:20   0:00 /usr/bin/mysqlrouter
root       2822  0.0  0.0 112824   988 pts/1    R+   22:20   0:00 grep --color=auto mysql
[root@proxy-2 mysqlrouter]# netstat -anplut|grep mysqlrouter
tcp        0      0 192.168.44.166:7001     0.0.0.0:*               LISTEN      2813/mysqlrouter    
tcp        0      0 192.168.44.166:7002     0.0.0.0:*               LISTEN      2813/mysqlrouter   
```

**#################################################################################### ** 

#### 2、创建授权用户验证读写分离

**在mysql集群的master机器上创建两个用户**

>  
 **read-write  ---&gt;7001 ---&gt; 192.168.44.170   写操作在master执行** 
 **read-only  --&gt;7002 --&gt; 192.168.44.170:3306,192.168.44.140:3306,192.168.44.160:3306   读操作在master和slave都可以执行** 


>  
 **创建可读可写用户：** 


```
root@(none) 11:07  mysql&gt;create user 'read-write'@'%' identified by '123456';
Query OK, 0 rows affected (0.00 sec)

root@(none) 11:10  mysql&gt;grant all on *.* to 'read-write'@'%';
Query OK, 0 rows affected (0.01 sec)

root@(none) 11:10  mysql&gt;

```

>  
 **创建仅可读用户：** 


```
root@(none) 11:10  mysql&gt;create user 'read-only'@'%' identified by '123456';
Query OK, 0 rows affected (0.00 sec)

root@(none) 11:11  mysql&gt;grant select on *.* to 'read-only'@'%';
Query OK, 0 rows affected (0.00 sec)

root@(none) 11:12  mysql&gt;

```

 **#################################################################################### ** 

#### **3、验证读写分离操作效果**

>  
 **准备一台客户机，测试访问mysqlrouter中间件所在的服务器** 


>  
 **验证效果：read-write用户可以 进行读写操作  指定端口7001** 


```
[root@client-server ~]# mysql -h 192.168.44.132 -P 7001 -u read-write -p'123456'
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
Server version: 5.7.34-log MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

read-write@(none) 11:23  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| delay_test         |
| flask_ht           |
| gtid_test          |
| kafka_data         |
| mysql              |
| performance_schema |
| sanchuang          |
| student            |
| sys                |
| test               |
| ucar_cloud         |
| wangsh             |
| wenlaoshi          |
+--------------------+
14 rows in set (0.01 sec)

read-write@(none) 11:26  mysql&gt;create database test1;
Query OK, 1 row affected (0.00 sec)

read-write@(none) 11:28  mysql&gt;select host,user from mysql.user;
+---------------+---------------+
| host          | user          |
+---------------+---------------+
| %             | chen          |
| %             | liming        |
| %             | read-only     |
| %             | read-write    |
| %             | shiyaling     |
| %             | wangsh        |
| %             | zhangj        |
| 192.168.0.124 | liuhongjie    |
| 192.168.44.%  | liu           |
| localhost     | mysql.session |
| localhost     | mysql.sys     |
| localhost     | root          |
+---------------+---------------+
12 rows in set (0.00 sec)

read-write@(none) 11:28  mysql&gt;


```

<img alt="" height="550" src="https://img-blog.csdnimg.cn/f5824c243afb46efbb51c77bd08c2ebf.png" width="1200">

 **#################################################################################### **

>  
 **验证效果：read-only用户只可以进行读操作，不能进行写操作  ，指定端口7002** 


```
[root@client-server ~]# mysql -h 192.168.44.132 -P 7002 -u read-only -p'123456'
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 5.7.34-log MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

read-only@(none) 11:35  mysql&gt;
read-only@(none) 11:35  mysql&gt;select user,host from mysql.user;
+---------------+---------------+
| user          | host          |
+---------------+---------------+
| chen          | %             |
| liming        | %             |
| read-only     | %             |
| read-write    | %             |
| shiyaling     | %             |
| wangsh        | %             |
| zhangj        | %             |
| liuhongjie    | 192.168.0.124 |
| liu           | 192.168.44.%  |
| mysql.session | localhost     |
| mysql.sys     | localhost     |
| root          | localhost     |
+---------------+---------------+
12 rows in set (0.00 sec)

read-only@(none) 11:35  mysql&gt;

```

>  
 **至此，基于gtid的半1复制的读写分离集群搭建完成** 


 **#################################################################################### **

### 搭建双vip高可用集群

>  
 **在proxy-1和proxy-2集群上部署keepalived做高可用** 
 **proxy-1和proxy-2都要安装keepalived** 


#### 1、安装部署keepalived软件 ，并修改配置文件

```
[root@proxy-1 ~]# yum install keepalived -y

```

```
[root@proxy-2 ~]# yum install keepalived -y

```

```
[root@proxy-2 ~]# keepalived -v
Keepalived v1.3.5 (03/19,2017), git commit v1.3.5-6-g6fa32f2

Copyright(C) 2001-2017 Alexandre Cassen, &lt;acassen@gmail.com&gt;

Build options:  PIPE2 LIBNL3 RTA_ENCAP RTA_EXPIRES RTA_PREF RTA_VIA FRA_OIFNAME FRA_SUPPRESS_PREFIXLEN FRA_TUN_ID RTAX_CC_ALGO RTAX_QUICKACK LIBIPTC LIBIPSET_DYNAMIC LVS LIBIPVS_NETLINK VRRP VRRP_AUTH VRRP_VMAC SOCK_NONBLOCK SOCK_CLOEXEC FIB_ROUTING INET6_ADDR_GEN_MODE SNMP_V3_FOR_V2 SNMP SNMP_KEEPALIVED SNMP_CHECKER SNMP_RFC SNMP_RFCV2 SNMP_RFCV3 SO_MARK
[root@proxy-2 ~]# 

```

>  
 **配置proxy-1：keepalived的配置文件** 
 **将proxy-1配置为master，将proxy-2作为backup** 


```
[root@proxy-1 keepalived]# cat keepalived.conf 
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
 # vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}

vrrp_instance VI_1 {
    state MASTER
    interface ens33
    virtual_router_id 61
    priority 200
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.44.180
    }
}

vrrp_instance VI_2 {
    state BACKUP
    interface ens33
    virtual_router_id 62
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.44.181
    }
}

```

>  
 **配置proxy-2 keepalived的配置文件** 


```
[root@proxy-2 keepalived]# cat keepalived.conf 
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
 # vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}

vrrp_instance VI_1 {
    state BACKUP
    interface ens33
    virtual_router_id 61
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.44.180
    }
}

vrrp_instance VI_2 {
    state MASTER
    interface ens33
    virtual_router_id 62
    priority 200
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.44.181
    }
}

```

**编辑好配置文件以后，重启keepalived服务**

```
[root@proxy-1 keepalived]# service keepalived start
Redirecting to /bin/systemctl start keepalived.service
[root@proxy-1 keepalived]# ps aux|grep keepalived
root       3892  0.0  0.1 123012  1404 ?        Ss   15:17   0:00 /usr/sbin/keepalived -D
root       3893  0.0  0.3 133980  3340 ?        S    15:17   0:00 /usr/sbin/keepalived -D
root       3894  0.0  0.2 133852  2672 ?        S    15:17   0:00 /usr/sbin/keepalived -D
root       3904  0.0  0.0 112824   992 pts/1    R+   15:17   0:00 grep --color=auto keepalived

```

```
[root@proxy-2 keepalived]# service keepalived start
Redirecting to /bin/systemctl start keepalived.service
[root@proxy-2 keepalived]# ps aux |grep keepalived
root       3369  0.0  0.1 123012  1396 ?        Ss   15:16   0:00 /usr/sbin/keepalived -D
root       3370  0.0  0.3 133984  3400 ?        S    15:16   0:00 /usr/sbin/keepalived -D
root       3371  0.0  0.2 133852  2664 ?        S    15:16   0:00 /usr/sbin/keepalived -D
root       3381  0.0  0.0 112824   988 pts/2    R+   15:16   0:00 grep --color=auto keepalived

```

>  
 **实现效果：** 


```
[root@proxy-1 keepalived]# ip add
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:92:35:e8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.44.132/24 brd 192.168.44.255 scope global noprefixroute ens33
       valid_lft forever preferred_lft forever
    inet 192.168.44.180/32 scope global ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fe92:35e8/64 scope link 
       valid_lft forever preferred_lft forever

```

```
[root@proxy-2 keepalived]# ip add
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:70:78:9f brd ff:ff:ff:ff:ff:ff
    inet 192.168.44.166/24 brd 192.168.44.255 scope global noprefixroute ens33
       valid_lft forever preferred_lft forever
    inet 192.168.44.181/32 scope global ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fe70:789f/64 scope link 
       valid_lft forever preferred_lft forever

```

 **#################################################################################### ** 

#### 2、使用客户机访问配置好的master

>  
 **注意：这个时候我们访问master是访问不了的，因为master上并没有开启7001,7002端口** 


```
[root@client-server ~]# mysql -h 192.168.44.180 -P 7001 -u read-write -p'123456'
mysql: [Warning] Using a password on the command line interface can be insecure.
ERROR 2003 (HY000): Can't connect to MySQL server on '192.168.44.180' (111)

```

>  
 **所以我们要将mysqlrouter的配置文件修改一下，将mysqlroute绑定的IP地址改为0.0.0.0，本机任意ip地址都能访问，然后重启mysqlrouter服务** 
 **注意：proxy-1和proxy-2的mysqlrouter配置文件都要修改** 


```
# 名字可以自定义
[routing:read_write]  
#是mysql-router服务器的ip地址
bind_address = 0.0.0.0    
bind_port = 7001
#支持可读可写
mode = read-write  
#mysql-master服务器的ip地址：mysql服务的端口号
destinations = 192.168.44.170:3306 
max_connections = 65535
max_connect_errors = 100
client_connect_timeout = 9

[routing:read_only]
#是mysql-router服务器的ip地址
bind_address = 0.0.0.0 
bind_port = 7002
# 仅可读
mode = read-only 
# mysql-slave服务器的ip地址：mysql服务的端口号
destinations = 192.168.44.170:3306,192.168.44.140:3306,192.168.44.160:3306 
max_connections = 65535
max_connect_errors = 100
client_connect_timeout = 9

```

```
[root@proxy-1 mysqlrouter]# service mysqlrouter restart
Redirecting to /bin/systemctl restart mysqlrouter.service
[root@proxy-1 mysqlrouter]# ps aux |egrep "mysqlrouter|keepalived"
root       3892  0.0  0.1 123012  1404 ?        Rs   15:17   0:00 /usr/sbin/keepalived -D
root       3893  0.0  0.3 133980  3340 ?        S    15:17   0:00 /usr/sbin/keepalived -D
root       3894  0.0  0.2 133852  2672 ?        S    15:17   0:00 /usr/sbin/keepalived -D
mysqlro+   3940  0.4  0.7 515444  7856 ?        Ssl  15:50   0:00 /usr/bin/mysqlrouter
root       3949  0.0  0.1 112824   996 pts/1    R+   15:50   0:00 grep -E --color=auto mysqlrouter|keepalived

```

```
[root@proxy-2 mysqlrouter]# service mysqlrouter restart
Redirecting to /bin/systemctl restart mysqlrouter.service
[root@proxy-2 mysqlrouter]# ps aux |egrep "mysqlrouter|keepalived"
root       3369  0.0  0.1 123012  1396 ?        Ss   15:16   0:00 /usr/sbin/keepalived -D
root       3370  0.0  0.3 133984  3400 ?        S    15:16   0:00 /usr/sbin/keepalived -D
root       3371  0.0  0.2 133852  2664 ?        S    15:16   0:00 /usr/sbin/keepalived -D
mysqlro+   3417  0.0  0.9 515444  9924 ?        Ssl  15:49   0:00 /usr/bin/mysqlrouter
root       3431  0.0  0.1 112824  1000 pts/2    R+   15:52   0:00 grep -E --color=auto mysqlrouter|keepalived
[root@proxy-2 mysqlrouter]# 

```

>  
 **重启服务以后，再次使用客户机访问master，可以看到，read-write和read-only都可以成功访问** 


```
[root@client-server ~]# mysql -h 192.168.44.180 -P 7001 -u read-write -p'123456'
mysql: [Warning] Using a password on the command line interface can be insecure.
ERROR 2003 (HY000): Can't connect to MySQL server on '192.168.44.180' (113)
[root@client-server ~]# mysql -h 192.168.44.180 -P 7001 -u read-write -p'123456'
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 18
Server version: 5.7.34-log MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

read-write@(none) 16:18  mysql&gt;

```

```
[root@client-server ~]# mysql -h 192.168.44.180 -P 7002 -u read-only -p'123456'
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 6
Server version: 5.7.34-log MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

read-only@(none) 16:21  mysql&gt;

```

>  
 **至此，双vip的高可用mysql集群就搭建好了** 


  **#################################################################################### **

###  prometheus监控的部署

#### 1、在监控服务器安装部署prometheus软件

>  
 **准备一台prometheus监控服务器** 
 **prometheus：192.168.44.210** 
 **下载好prometheus源码包，然后新建prometheus文件夹，将源码包上传到prometheus服务器里** 


```
[root@prometheus prometheus]# ls
prometheus-2.34.0.linux-amd64.tar.gz
[root@prometheus prometheus]# 
[root@prometheus prometheus]# tar xf prometheus-2.34.0.linux-amd64.tar.gz 
[root@prometheus prometheus]# ls
prometheus-2.34.0.linux-amd64  prometheus-2.34.0.linux-amd64.tar.gz

```

>  
 **修改PATH变量，将PATH变量写入.bashrc文件里** 


```
[root@prometheus ~]# cat .bashrc 
PATH=/root/prometheus/prometheus:$PATH

```

<img alt="" height="331" src="https://img-blog.csdnimg.cn/65e04739b3574921a7a3ac1ed6ae49c1.png" width="1061">

>  
 **将prometheus放到后台运行** 


```
[root@prometheus prometheus]# nohup prometheus &amp;
[1] 2000
[root@prometheus prometheus]# nohup: 忽略输入并把输出追加到"nohup.out"

```

<img alt="" height="567" src="https://img-blog.csdnimg.cn/3313616f05ff43919e3b5c74ae10fc2e.png" width="1200">

####  2、在要监控的服务器上安装mysqld_exporter软件

```
[root@master mysqld_exporter]# ls
mysqld_exporter-0.14.0.linux-amd64.tar.gz
[root@master mysqld_exporter]# tar xf mysqld_exporter-0.14.0.linux-amd64.tar.gz 
[root@master mysqld_exporter]# ls
mysqld_exporter-0.14.0.linux-amd64  mysqld_exporter-0.14.0.linux-amd64.tar.gz
[root@master mysqld_exporter]# mv mysqld_exporter-0.14.0.linux-amd64 mysqld_exporter
[root@master mysqld_exporter]# ls
mysqld_exporter  mysqld_exporter-0.14.0.linux-amd64.tar.gz

```

**创建授权用户，并授予权限**

```
root@(none) 21:40  mysql&gt;create user 'exporter'@'localhost' identified by '123123';
Query OK, 0 rows affected (0.00 sec)

root@(none) 21:41  mysql&gt;grant process,replication client,select on *.* to 'exporter'@'localhost';
Query OK, 0 rows affected (0.01 sec)

```

>  
 ** 创建一个配置文件my.cnf将刚才创建的用户信息添加到配置文件** 


```
[root@master mysqld_exporter]# cat my.cnf 
[client]
user=exporter
password=123123
host=localhost
port=3306

```

**测试连接，看能否监控mysql指标**

>  
 **--config.mycnf  :  指定mysqld_exporter配置文件** 
 **--web.listen-address   指定监听端口** 
 **--log.level    指定日志级别** 


```
[root@master mysqld_exporter]# nohup mysqld_exporter --config.my-cnf="/mysqld_exporter/mysqld_exporter/my.cnf" --web.listen-address='0.0.0.0':9088 --log.level=debug &amp;
[1] 22075
[root@master mysqld_exporter]# nohup: 忽略输入并把输出追加到"nohup.out"

```

<img alt="" height="281" src="https://img-blog.csdnimg.cn/6518ae74ce174b0780f4a80b0c341bf4.png" width="1200">

<img alt="" height="619" src="https://img-blog.csdnimg.cn/210108937a7d4fcd8f2fb91f7b705f43.png" width="1200">

#### 3、将mysqld_exporter接入prometheus里

>  
 ** 在prometheus配置文件prometheus.yml里面添加mysqld_exporter信息** 


```
scrape_configs:
  # The job name is added as a label `job=&lt;job_name&gt;` to any timeseries scraped from this config.
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]
  - job_name: "mysqld_exporter1"
    static_configs:
      - targets: ["192.168.44.170:9088"]

```

>  
 **修改配置文件以后重新执行prometheus程序,** 


```
[root@prometheus prometheus]# nohup prometheus --config.file=prometheus.yml &amp;
[1] 2260
[root@prometheus prometheus]# nohup: 忽略输入并把输出追加到"nohup.out"

```

<img alt="" height="841" src="https://img-blog.csdnimg.cn/9a7149bd53214e3a81bc2e00f2c28b24.png" width="1200">

<img alt="" height="859" src="https://img-blog.csdnimg.cn/5ba7cf2ddda74d5ba41d75f5942e0df8.png" width="1200">

####  4、部署grafana可视化监控指标展示工具

>  
 **下载grafana压缩包，上传至prometheus监控服务器，然后使用yum install 安装** 


```
[root@prometheus grafana]# ls
grafana-enterprise-8.4.5-1.x86_64.rpm
[root@prometheus grafana]# yum install grafana-enterprise-8.4.5-1.x86_64.rpm  -y 

```

启动grafana服务，查看端口

```
[root@prometheus grafana]# service grafana-server  start
Starting grafana-server (via systemctl):                   [  确定  ]
[root@prometheus grafana]# ss -anplut|grep grafana
tcp    LISTEN     0      128    [::]:3000               [::]:*                   users:(("grafana-server",pid=2474,fd=8))

```

访问测试grafana服务



<img alt="" height="847" src="https://img-blog.csdnimg.cn/adef229366ad4726b11222ad45e05461.png" width="1200">

添加数据源

<img alt="" height="740" src="https://img-blog.csdnimg.cn/d02cc4af6dfc403896e94ed630505c3c.png" width="1200">

>  
  ** 添加新的面板，将想要监控的指标显示出来** 


<img alt="" height="984" src="https://img-blog.csdnimg.cn/0e299b16384444cc8f072c12b20c9756.png" width="1072">

   **#################################################################################### **

 




