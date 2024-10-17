
--- 
title:  kafka启动闪退（ ERROR Fatal error during KafkaServer startup. Prepare to shutdown (kafka.server.KafkaSer） 
tags: []
categories: [] 

---
执行： nohup bin/kafka-server-start.sh config/server.properties &amp;

进入日志： cd /export/servers/kafka_2.12-2.4.1/logs cat server.log 查看报错信息：

```
[2021-11-24 14:19:31,577] INFO [ZooKeeperClient Kafka server] Connected. (kafka.zookeeper.ZooKeeperClient)
[2021-11-24 14:19:31,850] INFO Cluster ID = F5_E0Y5hRaaG9s_xgm5qpg (kafka.server.KafkaServer)
[2021-11-24 14:19:31,874] ERROR Fatal error during KafkaServer startup. Prepare to shutdown (kafka.server.KafkaServer)
kafka.common.InconsistentClusterIdException: The Cluster ID F5_E0Y5hRaaG9s_xgm5qpg doesn't match stored clusterId Some(i6qZt03xSSy1SyP0jGCYDw) in meta.properties. The broker is trying to join the wrong cluster. Configured zookeeper.connect may be wrong.
        at kafka.server.KafkaServer.startup(KafkaServer.scala:220)
        at kafka.server.KafkaServerStartable.startup(KafkaServerStartable.scala:44)
        at kafka.Kafka$.main(Kafka.scala:84)
        at kafka.Kafka.main(Kafka.scala)
[2021-11-24 14:19:31,876] INFO shutting down (kafka.server.KafkaServer)
[2021-11-24 14:19:31,879] INFO [ZooKeeperClient Kafka server] Closing. (kafka.zookeeper.ZooKeeperClient)
[2021-11-24 14:19:31,985] INFO Session: 0x10000024a760003 closed (org.apache.zookeeper.ZooKeeper)
[2021-11-24 14:19:31,985] INFO EventThread shut down for session: 0x10000024a760003 (org.apache.zookeeper.ClientCnxn)
[2021-11-24 14:19:31,987] INFO [ZooKeeperClient Kafka server] Closed. (kafka.zookeeper.ZooKeeperClient)
[2021-11-24 14:19:31,990] INFO shut down completed (kafka.server.KafkaServer)
[2021-11-24 14:19:31,990] ERROR Exiting Kafka. (kafka.server.KafkaServerStartable)
[2021-11-24 14:19:31,994] INFO shutting down (kafka.server.KafkaServer)

```

发现是clusterId 不匹配

### 解决办法1：
1. 进入 config
```
cd /export/servers/kafka_2.12-2.4.1/config

```
1. cat server.properties 找到 log.dirs的配置项，小编的是 log.dirs=/export/servers/kafka_2.12-2.4.1/data1. 进入 data,修改 meta.properties 文件
把 cluster.id= 改成 Cluster ID的值，小编的是： F5_E0Y5hRaaG9s_xgm5qpg

### 解决方法2：

根据 log.dirs=/export/servers/kafka_2.12-2.4.1/data 这个配置项，进入data文件夹下 cd /export/servers/kafka_2.12-2.4.1/data 删除所有的文件和文件夹，并重新执行： nohup bin/kafka-server-start.sh config/server.properties &amp;
