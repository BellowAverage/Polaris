
--- 
title:  第03课：分布式一致性协议 Gossip 和 Redis 集群原理解析 
tags: []
categories: [] 

---
Redis 是一个开源的、高性能的 Key-Value 数据库。基于 Redis 的分布式缓存已经有很多成功的商业应用，其中就包括阿里 ApsaraDB，阿里 Tair 中的 RDB 引擎，美团 MOS 以及腾讯云 CRS。本文我将着重介绍 Redis Cluster 原理、类 Codis 分布式方案以及分布式信息一致性协议 Gossip，以帮助大家深入理解 Redis。

#### 1. Redis 单机模式

顾名思义，单机模式指 Redis 主节点以单个节点的形式存在，这个主节点可读可写，上面存储数据全集。在3.0版本之前，Redis 只能支持单机模式，出于可靠性考量，通常单机模式为“1主 N 备”的结构，如下所示：

<img alt="" height="380" src="https://img-blog.csdnimg.cn/07bb3d7b0d064e268dd2a13fd752e85d.png" width="600">

需要说明的是，即便有很多个 Redis 主节点，只要这些主节点以单机模式存在，本质上仍为单机模式。单机模式比较简单，足以支撑一般应用场景，但单机模式具有固有的局限性：不支持自动故障转移，扩容能力极为有限（只能 Scale Up，垂直扩容），存在高并发瓶颈。

##### 1.1 不支持自动故障转移

Redis 单机模式下，即便是“1主 N 备”结构，当主节点故障时，备节点也无法自动升主，即无法自动故障转移（Failover）。故障转移需要“哨兵”Sentinel 辅助，Sentinel 是 Redis 高可用的解决方案，由一个或者多个 Sentinel 实例组成的系统可
