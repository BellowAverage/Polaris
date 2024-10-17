
--- 
title:  第13课：深入浅出解读 Kafka 的可靠性机制 
tags: []
categories: [] 

---
#### 1. 副本机制

在分布式系统中，为了提高可靠性，最常用、最有效的策略是“副本机制”，Kafka 也不例外。Kafka 为每个 Partition 维护了一个 AR（Assigned Replicas）列表，由 ISR（In-Sync Replicas，与 Leader 数据同步的 Replica）和 OSR（Outof-Sync Replicas，与 Leader 数据不同步的 Replica）组成。初始状态下，所有的 Replica 都在 ISR 中，但在 Kafka 工作过程中，由于各种问题（网络、磁盘、内存）可能导致部分 Replica 的同步速度慢于参数 `replica.lag.time.max.ms` 指定的阈值，一旦出现这种情况，这部分 Replica 会被移出 ISR，降级至 OSR 中。 

>  
 **关于参数 replica.lag.time.max.ms** 
 数据类型为 Long，默认值为 10000，重要性为 High，官方解释如下： 
 If a follower hasn't sent any fetch requests or hasn't consumed up to the leaders log end offset for at least this time, the leader will remove the follower from ISR. 


**副本机制如何作用？**

Producer 指定 Topic 向 Broker 发送消息，经过内部处理（如负载均衡等）后写入某 Partition 
