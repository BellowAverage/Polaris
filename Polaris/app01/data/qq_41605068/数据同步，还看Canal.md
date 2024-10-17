
--- 
title:  数据同步，还看Canal 
tags: []
categories: [] 

---
一个系统最重要的是数据，有时对于一个业务场景，不单单是把数据保存在数据库中，还需要同步保存在ES，Redis等等中。这时阿里开源组件Canal由此而生，它可以同步数据库中的增量数据保存到其它存储应用中。

## 一、介绍

<img alt="" height="627" src="https://img-blog.csdnimg.cn/bdd0d2208a2e4ed0b0db622e5e43adb9.png" width="1200">

 canal的工作原理就是把自己伪装成MySQL slave，模拟MySQL slave的交互协议向MySQL Mater发送 dump协议，MySQL mater收到canal发送过来的dump请求，开始推送binary log给canal，然后canal解析binary log，再发送到存储目的地，比如MySQL，Kafka，Elastic Search等等。

通过上面官网的描述可知，Canal的数据同步不是全量的，而是增量的。是基于binary log增量订阅和消费，因此，Canal可做：（参考：）
- 数据库镜像- 数据库实时备份- 索引构建和实施维护- 业务cache（缓存）刷新- 增量数据处理
## 二、搭建Canal

>  
  canal 支持源端 MySQL 版本包括 5.1.x , 5.5.x , 5.6.x , 5.7.x , 8.0.x 


### 2.1设置MySQL服务器

```
-- 使用命令登录：mysql -u root -p
-- 创建用户 用户名：canal 密码：Canal@123456
create user 'canal'@'%' identified by 'Canal@123456';
-- 授权 库名.*
GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT ON template.* TO 'canal'@'%';
```

报错：

<img alt="" height="68" src="https://img-blog.csdnimg.cn/02d77b36741647d4a8407ee7cbea022d.png" width="1056">

 解决方法：

>  
 因为replication slave 的级别是global，所以不能只作用于某一数据库，而是全局。所以还是要通过 *.* 执行，并在/etc/my.cnf中添加binlog-do-db=template来限制主从复制的数据库为template 


```
GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'canal'@'%';
FLUSH PRIVILEGES;
```

对已有账户进行查询：

>  
 show grants for 'canal' 


<img alt="" height="166" src="https://img-blog.csdnimg.cn/a51988bffac3465bbc858c136d87e5dc.png" width="882">

###  2.2修改**/etc/my.cnf文件**

```
# 配置MySQL replaction需要定义，不要和canal的slaveId重复
server_id= 1
# 开启MySQL的binlog
log-bin=mysql-bin
# 选择ROW(行)模式
binlog_format=row
#监控的数据库  不写则开启全部数据库的监听
binlog-do-db=gmallXXXXX

```

#### 2.2.1MySQL的binlog介绍

MySQL的二进制日志记录了所有的DDL和DML( 除了数据查询语句 )语句，以事件形式记录，还包含语句所执行的消耗的时间，MySQL的二进制日志是事务安全型的。

一般来说开启二进制日志大概会有1%的性能损耗。二进制有两个最重要的使用场景:
- MySQL Replication在Master端开启binlog，Mster把它的二进制日志传递给slaves来达到master-slave数据一致的目的。- 通过使用mysqlbinlog工具来使恢复数据。
二进制日志包括两类文件：二进制日志索引文件（文件名后缀为.index）用于记录所有的二进制文件，二进制日志文件（文件名后缀为.00000*）记录数据库所有的DDL和DML(除了数据查询语句)语句事件。

binlog日志的前缀是mysql-bin ，以后生成的日志文件就是 mysql-bin.123456 的文件后面的数字按顺序生成。 每次mysql重启或者到达单个文件大小的阈值时，新生一个文件，按顺序编号。

#### 2.2.2binlog的分类设置
-  statement 【语句集】 
binlog会记录每次一执行写操作的语句。 相对row模式节省空间，但是可能产生不一致性，例如：update table_name set create_date=now();如果用binlog日志进行恢复，由于执行时间不同可能产生的数据就不同 ( master落库数据时create_date为2021-08-08 11:10:30 ，但binlog从库落库执行语句时create_date的时间可能就变为2021-08-08 11:11:23 ，主要是语句执行时间为异步)

**优点**： 节省空间

**缺点**： 有可能造成数据不一致
-  row 【行级】 
binlog会记录每次操作后每行记录的变化。

**优点**：保持数据的绝对一致性。因为不管sql是什么，引用了什么函数，他只记录执行后的效果。

​**缺点**：占用较大空间。
-  mixed 【综合语句集和行级】 
 statement的升级版，一定程度上解决了因一些情况而造成的statement模式不一致问题，在某些情况下譬如：
1. 当函数中包含 UUID() 时；1. 包含 AUTO_INCREMENT 字段的表被更新时；1. 执行 INSERT DELAYED 语句时；1. 用 UDF 时；
会按照 ROW的方式进行处理

**优点**：节省空间，同时兼顾了一定的一致性。

**缺点**：还有些极个别情况依旧会造成不一致，另外statement和mixed对于需要对binlog的监控的情况都不方便。

### 2.3重启MySQL

```
service mysqld restart

```

>  
 使用命令查看是否打开binlog模式：show variables like 'log_bin'; 


<img alt="" height="167" src="https://img-blog.csdnimg.cn/3800b60e95a74acb8d62a35d697769ca.png" width="523">

>  
 查看binlog日志文件列表：show binary logs; 


<img alt="" height="173" src="https://img-blog.csdnimg.cn/d19749d6aac3422a8c38c9be44f80ce5.png" width="822">

>  
  查看当前正在写入的binlog文件：show master status; 


<img alt="" height="172" src="https://img-blog.csdnimg.cn/3a378be1bd0f4e2faefc17b7c4c297c2.png" width="1145">

## 三、安装Canal

下载地址：

<img alt="" height="284" src="https://img-blog.csdnimg.cn/cfe9ff9cc38946ba89373f3dbeae6c6f.png" width="858">

###  3.1版本区别

#### 3.1.1canal-deploy（canal-server）

可以直接监听MySQL的binlog，把自己伪装成MySQL的从库，只负责接收数据，并不做处理。接收到MySQL的binlog数据后可以通过配置canal.serverMode：tcp, kafka, rocketMQ, rabbitMQ连接方式发送到对应的下游。其中tcp方式可以自定义canal客户端进行接受数据，较为灵活。

#### 3.1.2canal-adapter（官网提供的canal-client）

相当于canal的客户端，会从canal-server中获取数据(需要配置为tcp方式)，然后对数据进行同步，可以同步到MySQL、Elasticsearch和HBase等存储中去。

相较于canal-server自带的canal.serverMode，canal-adapter提供的下游数据接受更为广泛。

#### 3.1.3canal-admin

为canal提供整体配置管理、节点运维等面向运维的功能，提供相对友好的WebUI操作界面，方便更多用户快速和安全的操作。

### 3.2安装

>  
 wget  https://github.com/alibaba/canal/releases/download/canal-1.1.6/canal.deployer-1.1.6.tar.gz 


git太慢了，也可以使用docker

>  
 docker pull canal/canal-server 
 docker run --name canal -d canal/canal-server 
  
 #配置文件 
 docker cp canal:/home/admin/canal-server/conf/canal.properties /usr/tchuhu/canal/conf 
 docker cp canal:/home/admin/canal-server/conf/example/instance.properties /usr/tchuhu/canal/conf 


### 3.3修改配置文件

```
#########################canal.properties###########################
# 默认端口 11111
# 默认输出model为tcp, 这里根据使用的mq类型进行修改
# tcp, kafka, RocketMQ
canal.serverMode = tcp

#################################################
######### destinations ############# 
#################################################
# canal可以有多个instance,每个实例有独立的配置文件，默认只 有一个example实例。
# 如果需要处理多个mysql数据的话，可以复制出多个example,对其重新命名，
# 命令和配置文件中指定的名称一致。然后修改canal.properties 中的 canal.destinations
# canal.destinations=实例 1，实例 2，实例 3
canal.destinations = example

```

```
########instance.properties###############
# 不能和mysql重复
canal.instance.mysql.slaveId=2
# 使用mysql的虚拟ip（这里因为创建用户时写的%，所以不要写127.0.0.1）和端口
canal.instance.master.address=IP:3306
# 使用已创建的canal用户
canal.instance.dbUsername=canal
canal.instance.dbPassword=canal
canal.instance.connectionCharset = UTF-8
# canal.instance.defaultDatabaseName =test

# 问题：（原本这样的，值同步test库，此处没能解决，单据指定数据库同步配置）
# canal.instance.filter.regex=.*\\..*
# canal.instance.defaultDatabaseName =test

# 注掉上面，然后添加，同步所有的库。
# .\*\\\\..\*:  表示匹配所有的库所有的表
canal.instance.filter.regex =.\*\\\\..\*

# 目的地，可以认识一个消息队列，不需要更改。
canal.mq.topic=example

# 如果是

```

>  
 docker run --name canal -p 11111:11111 -v /usr/tchuhu/canal/conf/instance.properties:/home/admin/canal-server/conf/example/instance.properties -v /usr/tchuhu/canal/conf/canal.properties:/home/admin/canal-server/conf/canal.properties 
 -v /usr/tchuhu/canal/logs:/home/admin/canal-server/logs 
 -d canal/canal-server 
  
 注:内存不足时canal会自动退出 
 <img alt="" height="108" src="https://img-blog.csdnimg.cn/658558bf7cf7429ea90e067d151971f7.png" width="1200"> 
 查看内存：free -m 
 释放内存：sync; echo 3 &gt; /proc/sys/vm/drop_caches 
 **如果还不行的话，增加虚拟内存：** 
 **关闭原本的swap**：sudo swapoff -a  【此时swap已经变成0】 
 <h4>设置新的swap大小：</h4> 
 <pre>dd if=/dev/zero of=/swapfile bs=1M count=31906</pre> 
 - of是指 在指定的路径创建swapfile文件- bs指的是Block Size，就是每一块的大小。这里的例子是1M，意思就是count的数字，是以1M为单位的。- count是告诉程序，新的swapfile要多少个block。这里是31906，就是说，新的swap文件是31906M大小,也就是将近32G。- 注意：可能需要点时间完成此步，耐心等待完成。- 注意：swap大小原则，设置为物理内存的1-2倍大小。因为最开始分析就是物理内存或swap内存不足导致，因此这里讲swap内存设置为物理内存的2倍大小。 
 完成： 
 <img alt="" src="https://img-blog.csdnimg.cn/img_convert/1d625407271e2a3ba253b739a5a7e937.png"> 
 **把新增加的swapfile文件设置为swap文件 ：**sudo mkswap /swapfile 
 **修改/etc/fstab文件，让swap在启动时自动生效**：vi /etc/fstab 
 在文件最后一行添加   
 <pre>/swapfile swap  swap  defaults  0   0</pre> 
 **重启服务器**：reboot 
 **挂载swapfile文件：**swapon /swapfile 
 查看结果： 
 <img alt="" src="https://img-blog.csdnimg.cn/img_convert/878276a24da9e5fb9d341010019dfd7e.png"> 
  


```
        &lt;dependency&gt;
            &lt;groupId&gt;top.javatool&lt;/groupId&gt;
            &lt;artifactId&gt;canal-spring-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;1.2.1-RELEASE&lt;/version&gt;
        &lt;/dependency&gt;
```

>  
 <pre>canal.server=IP:11111
canal.destination=example</pre> 


```
@Component
@Slf4j
@CanalTable("metabolome")
public class MetHandler implements EntryHandler&lt;Metabolome&gt; {
    @Override
    public void insert(Metabolome metabolome) {
        //新增
        System.out.println("新增："+metabolome.toString());
    }

    @Override
    public void update(Metabolome before, Metabolome after) {
        //修改
        System.out.println("修改前："+before.toString());
        System.out.println("修改后："+after.toString());
    }

    @Override
    public void delete(Metabolome metabolome) {
        System.out.println("删除："+metabolome);
    }
}
```

修改一条记录，运行结果：

<img alt="" height="672" src="https://img-blog.csdnimg.cn/043c4646a52d426ba07386a54b5cfdbb.png" width="1200">

** canal消息格式：**

```
Entry  
    Header  
        logfileName [binlog文件名]  
        logfileOffset [binlog position]  
        executeTime [binlog里记录变更发生的时间戳,精确到秒]  
        schemaName   
        tableName  
        eventType [insert/update/delete类型]  
    entryType   [事务头BEGIN/事务尾END/数据ROWDATA]  
    storeValue  [byte数据,可展开，对应的类型为RowChange]  
RowChange
    isDdl       [是否是ddl变更操作，比如create table/drop table]
    sql         [具体的ddl sql]
rowDatas    [具体insert/update/delete的变更数据，可为多条，1个binlog event事件可对应多条变更，比如批处理]
    beforeColumns [Column类型的数组，变更前的数据字段]
    afterColumns [Column类型的数组，变更后的数据字段]
    Column
    index
    sqlType     [jdbc type]
    name        [column name]
    isKey       [是否为主键]
    updated     [是否发生过变更]
    isNull      [值是否为null]
    value       [具体的内容，注意为string文本]

```

## 五、总结

canal的tcp模式，需要自己解析数据，一条插入语句同时插入多条记录，会产生多条消息。而kafka模式，同时插入多条记录会只会产生一条消息（通过json数组的方式）
