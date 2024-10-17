
--- 
title:  kafka安装使用教程快速入门 
tags: []
categories: [] 

---
####  1.kafka下载

下载地址：

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/de5bbcc61027b2a579c2816d382a5fd0.png">

以键头所指版本为例

### Kafka核心概念

在详细介绍Kafka的架构和基本组件之前，需要先了解一下Kafka的一些核心概念。 Producer：消息的生产者，负责往Kafka集群中发送消息； Consumer：消息的消费者，主动从Kafka集群中拉取消息。 Consumer Group：每个Consumer属于一个特定的Consumer Group，新建Consumer的时候需要指定对应的Consumer Group ID。 Broker：Kafka集群中的服务实例，也称之为节点，每个Kafka集群包含一个或者多个Broker（一个Broker就是一个服务器或节点）。 Message：通过Kafka集群进行传递的对象实体，存储需要传送的信息。 Topic：消息的类别，主要用于对消息进行逻辑上的区分，每条发送到Kafka集群的消息都需要有一个指定的Topic，消费者根据Topic对指定的消息进行消费。 Partition：消息的分区，Partition是一个物理上的概念，相当于一个文件夹，Kafka会为每个topic的每个分区创建一个文件夹，一个Topic的消息会存储在一个或者多个Partition中
