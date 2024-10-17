
--- 
title:  第04课：基于 Redis 的分布式缓存实现及加固策略 
tags: []
categories: [] 

---
本文将从 Redis-Cluster 搭建切入，详解集群的创建原理和加固策略。之后，分析集群所存在的几种可靠性问题并给出解决方案，最后，介绍一个集群运维软件的实现方案。

#### 1. Redis-Cluster 搭建

本节将介绍基于 Redis 和 Lettuce 搭建一个分布式缓存集群的方法。为了生动地呈现集群创建过程，我没有采用 Redis 集群管理工具 redis-trib，而是基于 Lettuce 编写 Java 代码实现集群的创建，相信，这将有利于读者更加深刻地理解 Redis 集群模式。

##### 1.1 方案简述

Redis 集群模式至少需要三个主节点，作为举例，本文搭建一个3主3备的精简集群，麻雀虽小，五脏俱全。主备关系如下图所示，其中 M 代表 Master 节点，S 代表 Slave 节点，A-M 和 A-S 为一对主备节点。

<img src="https://images.gitbook.cn/a43e6950-966f-11e8-9f67-05ec09da262a" alt="enter image description here">

按照上图所示的拓扑结构，如果节点 1 故障下线，那么节点 2 上的 A-S 将升主为 A-M，Redis 3 节点集群仍可用，如下图所示：

<img src="https://images.gitbook.cn/b04af9c0-966f-11e8-bee3-b1dbef72ca56" alt="enter image description here">

特别说明：事实上，Redis 集群节点间是两两互通的，如下图所示，上面作为示意图，进行了适当简化。


