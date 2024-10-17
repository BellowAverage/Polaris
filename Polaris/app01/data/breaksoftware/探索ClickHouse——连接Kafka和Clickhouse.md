
--- 
title:  探索ClickHouse——连接Kafka和Clickhouse 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- - - - <ul><li>- - - - - - - - - - - 


## 安装Kafka

### 新增用户

```
sudo adduser kafka
sudo adduser kafka sudo
su -l kafka

```

### 安装JDK

```
sudo apt-get install openjdk-8-jre

```

### 下载解压kafka

可以从下找到希望安装的版本。需要注意的是，不要下载路径包含src的包，否则会报“Classpath is empty”之类的错误。

```
mkdir ~/Downloads
curl "https://downloads.apache.org/kafka/3.5.1/kafka_2.13-3.5.1.tgz" -o ~/Downloads/kafka.tgz
mkdir ~/kafka &amp;&amp; cd ~/kafka
tar -xvzf ~/Downloads/kafka.tgz --strip 1

```

### 配置

#### 配置kafka

```
vim ~/kafka/config/server.properties

```

将下面这行加入文件的末尾

```
# ~/kafka/config/server.properties
delete.topic.enable=true

```

同时修改log的路径

```
# ~/kafka/config/server.properties
log.dirs=/home/kafka/logs

```

#### 创建zookeeper service

```
sudo vim /etc/systemd/system/zookeeper.service

```

将下面内容填入上述文件中

```
[Unit]
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=simple
User=kafka
ExecStart=/home/kafka/kafka/bin/zookeeper-server-start.sh /home/kafka/kafka/config/zookeeper.properties
ExecStop=/home/kafka/kafka/bin/zookeeper-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target

```

#### 创建kafka service

```
sudo vim /etc/systemd/system/kafka.service

```

将下面内容填入上述文件中

```
[Unit]
Requires=zookeeper.service
After=zookeeper.service

[Service]
Type=simple
User=kafka
ExecStart=/bin/sh -c '/home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties &gt; /home/kafka/kafka/kafka.log 2&gt;&amp;1'
ExecStop=/home/kafka/kafka/bin/kafka-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target

```

### 启动kafka#

#### 启动服务

```
sudo systemctl start kafka

```

#### 查看状态

```
sudo systemctl status kafka

```

>  
 ● kafka.service Loaded: loaded (/etc/systemd/system/kafka.service; enabled; vendor preset: enabled) Active: active (running) since Thu 2023-09-28 03:09:39 UTC; 4s ago Main PID: 3561758 (sh) Tasks: 42 (limit: 2143) Memory: 292.4M CPU: 2.768s CGroup: /system.slice/kafka.service ├─3561758 /bin/sh -c “/home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties &gt; /home/kafka/kafka/kafka.log 2&gt;&amp;1” └─3561760 java -Xmx1G -Xms1G -server -XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:+ExplicitGCInvokesConcurrent -XX:MaxInlineLevel=15 -Djava.awt.headless=true -Xloggc:/&gt; Sep 28 03:09:39 ubuntua systemd[1]: Started kafka.service. 


可以看到kafka已经处于running状态。

### 测试

#### 创建Topic

```
~/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:2181 --replication-factor 1 --partitions 1 --topic TutorialTopic

```

#### 发送消息

```
echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TutorialTopic &gt; /dev/null

```

#### 订阅Topic

新启动一个界面，执行下面命令

```
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic TutorialTopic --from-beginning

```

它会收到上面发的消息

>  
 Hello, World 


## 连接

### 创建表

使用kafka engine将kafka中的流映射到一个表中。我们以中的数据为例。

```
clickhouse-client --stream_like_engine_allow_direct_select 1

```

```
CREATE TABLE uk_price_paid_from_kafka (uuid_string String, price_string String, time String, postcode String, a String, b String, c String, addr1 String, addr2 String, street String, locality String, town String, district String, county String, d String, e String) ENGINE = Kafka SETTINGS kafka_broker_list = 'localhost:9092', kafka_topic_list='TutorialTopic', kafka_group_name='clickhouse', kafka_format='CSV', kafka_skip_broken_messages=1, kafka_num_consumers=1;

```

>  
 CREATE TABLE uk_price_paid_from_kafka ( `uuid_string` String, `price_string` String, `time` String, `postcode` String, `a` String, `b` String, `c` String, `addr1` String, `addr2` String, `street` String, `locality` String, `town` String, `district` String, `county` String, `d` String, `e` String ) ENGINE = Kafka SETTINGS kafka_broker_list = ‘localhost:9092’, kafka_topic_list = ‘TutorialTopic’, kafka_group_name = ‘clickhouse’, kafka_format = ‘CSV’, kafka_skip_broken_messages = 1, kafka_num_consumers = 1 Query id: 07a063e9-6a61-42c0-8fec-1fe2f119ee28 Ok. 0 rows in set. Elapsed: 0.008 sec. 


### 给kafka发送消息

```
~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TutorialTopic

```

进入消息输入模式，发送下面两个消息

```
"{<!-- -->F887F88E-7D15-4415-804E-52EAC2F10958}","70000","1995-07-07 00:00","MK15 9HP","D","N","F","31","","ALDRICH DRIVE","WILLEN","MILTON KEYNES","MILTON KEYNES","MILTON KEYNES","A","A"
"{<!-- -->40FD4DF2-5362-407C-92BC-566E2CCE89E9}","44500","1995-02-03 00:00","SR6 0AQ","T","N","F","50","","HOWICK PARK","SUNDERLAND","SUNDERLAND","SUNDERLAND","TYNE AND WEAR","A","A"

```

<img src="https://img-blog.csdnimg.cn/48aa99cdf8314368abc2d97ef968532a.png" alt="在这里插入图片描述">

### Clickhouse收到消息

在clickhouse-client交互终端中执行下面指令：

```
select * from uk_price_paid_from_kafka;

```

<img src="https://img-blog.csdnimg.cn/ef5fa10afb564771aa4a1dee9ce6c36a.png" alt="在这里插入图片描述"> 可以看到之前发送给kafka Topic的内容在Clickhouse中被收到了。

### 问题

后面我再在clickhouse-client交互终端中查询不到数据了。即使我们给kafka该主题发消息，也查询不到。后面我们再将中讲解使用MaterializedView清洗和固化kafka的数据。

## 参考资料
- - - - - 