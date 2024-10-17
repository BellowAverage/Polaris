
--- 
title:  第11课：搭建基于 Kafka 和 ZooKeeper 的分布式消息队列 
tags: []
categories: [] 

---
“纸上得来终觉浅，绝知此事要躬行”，本文将详细介绍基于 Kafka 和 ZooKeeper 的分布式消息队列的搭建方法，并给出 Producer 和 Consumer 代码供读者测试，以便读者对分布式消息队列形成一个整体的认识。在第 12 课中，我将详细介绍基于 Kafka 和 ZooKeeper 的分布式消息队列的原理。

#### 1. ZooKeeper集群搭建

Kafka 将元数据信息保存在 ZooKeeper 中，但发送给 Topic 的数据不会发送到 ZooKeeper 上。Kafka 利用 ZooKeeper 实现动态集群扩展、Leader 选举、负载均衡等功能，因此，我们首先要搭建 ZooKeeper 集群。

##### 1.1 软件环境准备

根据 ZooKeeper 集群的原理，只要超过半数的节点正常，便可提供服务。一般，服务器为奇数台，像 1、3、5……。为什么呢？举个例子，如果服务器为 5 台，则最多可故障两台；如果为 4 台，则最多可故障一台；如果为 3 台，最多也只可故障一台。很明显，偶数台并没有什么意义，4 台服务器相较于 3 台并没有增强可用性。

 - 服务器 IP，本例中我以 3 台服务器为例，生产环境中，为了保证 ZooKeeper 的性能，服务器的内存不小于 4G，以便为 ZooKeeper 提供足够的 Java 堆内存。

```
server1：192.168.7.100
server2：192.168.7.101
server3：192.168.7.102

```

 - Java JDK 1.7及以上：ZooKeeper 基于 Java 编写，运行 Zoo
