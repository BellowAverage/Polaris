
--- 
title:  Kafka + Canal + MySQL 集群部署 
tags: []
categories: [] 

---
**目录**











































### 1、什么是Canal？

<img alt="" height="430" src="https://img-blog.csdnimg.cn/1785a10fec864c659eb40ea3e366882b.png" width="819">

####  **canal产生的背景：**

>  
 **早期，阿里巴巴B2B公司因为存在杭州和美国双机房部署，存在跨机房同步的业务需求。不过早期的数据库同步业务，主要是基于trigger的方式获取增量变更，不过从2010年开始，阿里系公司开始逐步的尝试基于数据库的日志解析，获取增量变更进行同步，由此衍生出了增量订阅&amp;消费的业务，从此开启了一段新纪元。** 


>  
 ** canal 翻译为水道，管道，沟渠，是由java语言开发的，它的定位就是基于数据库增量日志解析，提供增量数据订阅&amp;消费，目前主要支持mysql/mariadb 当前的 canal 支持源端 MySQL 版本包括 5.1.x , 5.5.x , 5.6.x , 5.7.x , 8.0.x** 


####  **canal工作原理主要是利用了mysql的主从复制原理：**

>  
 **主从复制简单过程：当有数据改变发生的时候，master会将改变记录到二进制日志（binary log）中，这些记录叫二进制日志事件，可以通过show binlog events 进行查看。slave将master上的binary log拷贝到它的中继日志(relay log);最后slave将中继日志里面的events进行重现，将数据改变反映成自己的数据。** 


####  **canal工作原理：**

>  
 **1、canal模拟mysql slave的交互协议，伪装自己为mysql slave，向mysql master发送dump协议** 
 **2、mysql master收到dump请求，开始推送binary log给slave(也就是canal)。** 
 **3、canal解析binary log对象（原始为byte流）** 


#### 实验环境： 

>  
 ** 本次实验的目的是使用canal将mysql的数据解析到kafka，因此实验环境为 ****Mysql5.7.34**** + ****Canal 1.1.5**** + ****Kafka2.12** 
 **部署集群之前先部署ZooKeeper集群。 ** 


#### 实验目的：

>  
 **kafka通过canal实时消费到mysql的数据。即mysql只要由数据库的库，表，结构和内容发生改变，canal就将数据吐到kafka，让kafka的消费者可以实时消费到mysql的数据** 


**################################################### **

### 2、mysql的安装部署

>  
 **mysql部署版本：5.7.34 mysql部署机器：node1** 
 **本次mysql部署采用二进制安装，使用安装部署脚本前先将防火墙，selinux规则都关闭。 ** 


####  mysql下载路径：

<img alt="" height="390" src="https://img-blog.csdnimg.cn/1771f47ead594f35b33d2ec36925461b.png" width="1200">





**mysql安装部署脚本：**

```
[root@node1 lianxi]# cat install_mysql.sh 
#!/bin/bash
 
#解决软件的依赖关系
yum  install cmake ncurses-devel gcc  gcc-c++  vim  lsof bzip2 openssl-devel ncurses-compat-libs -y

#下载安装包
wget https://downloads.mysql.com/archives/get/p/23/file/mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz
 
#解压mysql二进制安装包
tar  xf  mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz
 
#移动mysql解压后的文件到/usr/local下改名叫mysql
mv mysql-5.7.34-linux-glibc2.12-x86_64 /usr/local/mysql
 
#新建组和用户 mysql
groupadd mysql
#mysql这个用户的shell 是/bin/false 属于mysql组 
useradd -r -g mysql -s /bin/false mysql
 
 
#新建存放数据的目录
mkdir  /data/mysql -p
#修改/data/mysql目录的权限归mysql用户和mysql组所有，这样mysql用户可以对这个文件夹进行读写了
chown mysql:mysql /data/mysql/
#只是允许mysql这个用户和mysql组可以访问，其他人都不能访问
chmod 750 /data/mysql/
 
#进入/usr/local/mysql/bin目录
cd /usr/local/mysql/bin/
 
#初始化mysql
./mysqld  --initialize --user=mysql --basedir=/usr/local/mysql/  --datadir=/data/mysql  &amp;&gt;passwd.txt
 
#让mysql支持ssl方式登录的设置
./mysql_ssl_rsa_setup --datadir=/data/mysql/
 
#获得临时密码
tem_passwd=$(cat passwd.txt |grep "temporary"|awk '{print $NF}')
  #$NF表示最后一个字段
  # abc=$(命令)  优先执行命令，然后将结果赋值给abc 
 
# 修改PATH变量，加入mysql bin目录的路径
#临时修改PATH变量的值
export PATH=/usr/local/mysql/bin/:$PATH
#重新启动linux系统后也生效，永久修改
echo  'PATH=/usr/local/mysql/bin:$PATH' &gt;&gt;/root/.bashrc
 
#复制support-files里的mysql.server文件到/etc/init.d/目录下叫mysqld
cp  ../support-files/mysql.server   /etc/init.d/mysqld
 
#修改/etc/init.d/mysqld脚本文件里的datadir目录的值
sed  -i '70c  datadir=/data/mysql'  /etc/init.d/mysqld
 
#生成/etc/my.cnf配置文件
cat  &gt;/etc/my.cnf  &lt;&lt;EOF
[mysqld_safe]
[client]
socket=/data/mysql/mysql.sock
[mysqld]
socket=/data/mysql/mysql.sock
port = 3306
open_files_limit = 8192
innodb_buffer_pool_size = 512M
character-set-server=utf8
[mysql]
auto-rehash
prompt=\\u@\\d \\R:\\m  mysql&gt;
EOF
 
#修改内核的open file的数量
ulimit -n 1000000
#设置开机启动的时候也配置生效
echo "ulimit -n 1000000" &gt;&gt;/etc/rc.local
chmod +x /etc/rc.d/rc.local
 
 
#启动mysqld进程
service mysqld start
 
#将mysqld添加到linux系统里服务管理名单里
/sbin/chkconfig --add mysqld
#设置mysqld服务开机启动
/sbin/chkconfig mysqld on
 
#初次修改密码需要使用--connect-expired-password 选项
#-e 后面接的表示是在mysql里需要执行命令  execute 执行
#set password='123456';  修改root用户的密码为123456
mysql -uroot -p$tem_passwd --connect-expired-password   -e  "set password='123456';"
 
 
#检验上一步修改密码是否成功，如果有输出能看到mysql里的数据库，说明成功。
mysql -uroot -p'123456'  -e "show databases;"
```

#### 开启二进制日志

```
vim /etc/my.cnf

# 开启二进制日志
log_bin
server_id=1
```

#### 配置mysql slave的权限

>  
 **canal的原理是模拟自己为mysql slave，所以要创建一个用户，配置mysql slave相关权限，授权canal连接mysql具有作为mysql slave的权限** 


```
root@(none) 11:37  mysql&gt;create user canal identified by 'canal';
Query OK, 0 rows affected (0.00 sec)

root@(none) 11:38  mysql&gt;grant select,replication slave,replication client on *.* to 'canal'@'%';
Query OK, 0 rows affected (0.00 sec)

root@(none) 11:42  mysql&gt;flush privileges;
Query OK, 0 rows affected (0.00 sec)

root@(none) 11:42  mysql&gt;show grants for 'canal';
+---------------------------------------------------------------------------+
| Grants for canal@%                                                        |
+---------------------------------------------------------------------------+
| GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'canal'@'%' |
+---------------------------------------------------------------------------+
1 row in set (0.00 sec)
```

**################################################### ** 

### 3、kafka的安装部署

#### kafka下载路径：

<img alt="" height="504" src="https://img-blog.csdnimg.cn/a0f260d794ea492b98e4a05c21761dd7.png" width="1200">



>  
 **部署节点：node1，node2，node3** 
 **上传kafka_2.12安装包到/usr/local目录下面，然后解压缩，更改权限，制作软链接** 


```
[root@node031 local]# tar -xvf kafka_2.12-2.1.1.tgz
[root@node031 local]# ln -s kafka_2.12-2.1.1 kafka
[root@node031 local]# chown -R hadoop:hadoop kafka
[root@node031 local]# chown -R hadoop:hadoop kafka_2.12-2.1.1
```

#### kafka配置：

>  
 **分别在node1，node2，node3上操作，注意broker.id要不一致** 


```
[hadoop@node1 config]$ vim server.properties

broker.id=1
zookeeper.connect=node1:2181,node2:2181,node3:2181
```

#### **启动kafka集群，将三台服务器的kafka都启动**

```
[hadoop@node1 kafka]$ bin/kafka-server-start.sh -daemon config/server.properties 

[hadoop@node1 kafka]$ ps -ef |grep kafka
hadoop    50006      1  1 17:11 pts/1    00:00:07 /usr/local/jdk/bin/java -Xmx1G -Xms1G -server -XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:+ExplicitGCInvokesConcurrent -XX:MaxInlineLevel=15 -Djava.awt.headless=true -Xloggc:/usr/local/kafka/bin/../logs/kafkaServer-gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dkafka.logs.dir=/usr/local/kafka/bin/../logs -Dlog4j.configuration=file:bin/../config/log4j.properties -cp /usr/local/kafka/bin/../libs/activation-1.1.1.jar:/usr/local/kafka/bin/../libs/aopalliance-repackaged-2.6.1.jar:/usr/local/kafka/bin/../libs/argparse4j-0.7.0.jar:/usr/local/kafka/bin/../libs/audience-annotations-0.5.0.jar:/usr/local/kafk
```

#### 创建topic测试

创建topic test 和 example

```
[root@node1 bin]# ./kafka-topics.sh --create --zookeeper node1:2181 --replication-factor 1 --partitions 1 --topic test
Created topic "test".
[root@node1 bin]# ./kafka-topics.sh --create --zookeeper node1:2181 --replication-factor 1 --partitions 1 --topic example
Created topic "example".
```

#### 进入ZooKeeper客户端查看新建的topic

```
[root@node1 bin]# ./zkCli.sh 
[zk: localhost:2181(CONNECTED) 0] ls /
[admin, brokers, cluster, config, consumers, controller, controller_epoch, feature, hbase, isr_change_notification, latest_producer_id_block, log_dir_event_notification, zookeeper]
[zk: localhost:2181(CONNECTED) 0] ls /brokers/topics
[example, test]
```

#### 生产者消费者测试

```
# 创建一个生产者
[root@node1 bin]# ./kafka-console-producer.sh --broker-list 192.168.20.11:9092 --topic test
# 创建一个消费者
[root@node1 bin]# ./kafka-console-consumer.sh --bootstrap-server 192.168.20.11:9092 --topic test
# 在生产者里面产生数据看消费者能否消费到数据。
[root@node1 bin]# ./kafka-console-producer.sh --broker-list 192.168.20.11:9092 --topic test
&gt;hello world
&gt;this is kafka test
&gt;fef
&gt;fef
# 消费数据正常
[root@node1 bin]# ./kafka-console-consumer.sh --bootstrap-server 192.168.20.11:9092 --topic test
hello world
this is kafka test
fef
fef

```

**################################################### **

### 4、Canal的安装部署

#### canal下载路径：

#### 



>  
 **Canal部署节点：node1** 


>  
 **上传canal1.1.5的二进制包到/usr/local下，然后解压** 


```
[root@node1 local]# tar -xvf canal.deployer-1.1.5.tar.gz
```

>  
 **制作软链接** 


```
[root@node1 local]# ln -s canal-1.1.5 canal
```

>  
 **更改权限** 


```
[root@node1 local]# chown -R hadoop:hadoop canal
[root@node1 local]# chown -R hadoop:hadoop canal-1.1.5
```

**更改canal配置:**

>  
 **canal只要是两个配置文件要修改，canal.properties修改canal服务模式为kafka，设置kafka地址** 


```
[root@node1 conf]# vim canal.properties
canal.serverMode = kafka
kafka.bootstrap.servers = node1:9092,node2:9092,node3:9092
```

>  
 **example/instance.properties配置mysql的用户，密码，kafka的topic等 ** 


```
cd /usr/local/canal/conf/example
vim instance.properties

# 数据库地址
canal.instance.master.address=192.168.20.11:3306
# 数据库用户
canal.instance.dbUsername=canal
# 数据库密码
canal.instance.dbPassword=canal
# 数据库名.要监控的表名
canal.instance.filter.regex=test\..*
# topic name  canal从mysql获取的数据会存入这个主题
canal.mq.topic=canal_test
```

**启动canal**

```
[root@node1 bin]# ./startup.sh
[root@node1 bin]# jps
42848 ResourceManager
67395 Kafka
68775 ConsoleConsumer
66167 QuorumPeerMain
69110 CanalLauncher
40824 DataNode
69135 Jps
```

**################################################### ** 

### 5、kafka实时消费mysql数据测试

>  
 **创建一个主题 canal_test** 


```
./kafka-topics.sh --create --zookeeper node1:2181,node2:2181,node3:2181 --replication-factor 1 --partitions 1 --topic canal_test
```

>  
 **创建一个kafka消费者来消费canal_test主题。** 


```
[root@node1 bin]# ./kafka-console-consumer.sh --bootstrap-server node1:9092 --topic canal_test --from-beginning
```

>  
 **登录mysql，对test数据库进行操作，等待canal将数据从mysql吐到kafka里。** 


```
root@(none) 17:15  mysql&gt;use test;
Database changed
root@test 17:15  mysql&gt;create table company(id int);
Query OK, 0 rows affected (0.01 sec)

root@test 17:15  mysql&gt;insert into company(id) values(1);
Query OK, 1 row affected (0.01 sec)

root@test 17:16  mysql&gt;select * from company;
+------+
| id   |
+------+
|    1 |
+------+
1 row in set (0.01 sec)
root@test 17:16  mysql&gt;insert into company(id) values(2);
Query OK, 1 row affected (0.00 sec)
```

>  
 **成功消费到数据。** 


```
[root@node1 bin]# ./kafka-console-consumer.sh --bootstrap-server node1:9092 --topic canal_test --from-beginning
{"data":null,"database":"test","es":1680599305000,"id":1,"isDdl":true,"mysqlType":null,"old":null,"pkNames":null,"sql":"DROP TABLE `grands` /* generated by server */","sqlType":null,"table":"grands","ts":1680599658035,"type":"ERASE"}
{"data":null,"database":"test","es":1680599735000,"id":2,"isDdl":true,"mysqlType":null,"old":null,"pkNames":null,"sql":"create table company(id int)","sqlType":null,"table":"company","ts":1680599735417,"type":"CREATE"}
{"data":[{"id":"1"}],"database":"test","es":1680599764000,"id":3,"isDdl":false,"mysqlType":{"id":"int"},"old":null,"pkNames":null,"sql":"","sqlType":{"id":4},"table":"company","ts":1680599764271,"type":"INSERT"}
```

<img alt="" height="199" src="https://img-blog.csdnimg.cn/c1a618a330f44238abe76ecbe96d3f10.png" width="787">


