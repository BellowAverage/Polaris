
--- 
title:  第06课：Redis-Cluster 故障倒换调优原理分析 
tags: []
categories: [] 

---
Redis-Cluster 是 Redis 官方推出的集群方案，其分布式一致性协议基于 Gossip 算法（第03课中已经详细介绍）。当 Redis-Cluster 出现主节点故障后，集群会经历故障检测、选举、故障倒换三大步骤，在此期间 Redis-Cluster 是不能提供服务的，鉴于此，优化这三个步骤的耗时，便是保障集群可用性、提升性能的关键点之一。

需要说明的是，优化耗时并没有普适性的方案，而是需要根据集群的规模和应用场景有针对性的优化，因此，犹如 JVM 的优化，掌握优化的原理才能“治本”，以不变应万变。

#### 1. Redis-Cluster 故障检测原理及优化分析

Redis-Cluster 中出现主节点故障后，检测故障需要经历单节点视角检测、检测信息传播、下线判决三个步骤，下文将结合源码分析。

##### 1.1 单点视角检测

在第 03 课中介绍过，集群中的每个节点都会定期通过集群内部通信总线向集群中的其它节点发送 PING 消息，用于检测对方是否在线。如果接收 PING 消息的节点没有在规定的时间内（`cluster_node_timeout`）向发送 PING 消息的节点返回 PONG 消息，那么，发送 PING 消息的节点就会将接收 PING 消息的节点标注为疑似下线状态（Probable Fail，PFAIL）。如下源码：

<img src="https://images.gitbook.cn/b77d4f90-a2ea-11e8-9b2d-01357ecc007a" alt="enter image description here">

需要注意的是，判断 PFAIL 的依据也是参数 `cluster_node_timeout&lt;`
