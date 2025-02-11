
--- 
title:  第09课：基于 Etcd 的分布式锁实现原理及方案 
tags: []
categories: [] 

---
Etcd 最新版本已经提供了支持分布式锁的基础接口（可见），但本文并不局限于此。

本文将介绍两条实现分布式锁的技术路线：

 1. 从分布式锁的原理出发，结合 Etcd 的特性，洞见分布式锁的实现细节；
 1. 基于 Etcd 提供的分布式锁基础接口进行封装，实现分布式锁。

两条路线差距甚远，建议读者先看路线 1，以便了解 Etcd 实现分布式锁的细节。

#### 1. 为什么选择 Etcd

据官网介绍，Etcd 是一个分布式，可靠的 Key-Value 存储系统，主要用于存储分布式系统中的关键数据。初见之下，Etcd 与 NoSQL 数据库系统有几分相似，但作为数据库绝非 Etcd 所长，其读写性能远不如 MongoDB、Redis 等 Key-Value 存储系统。“让专业的人做专业的事！” Ectd 作为一个高可用的键值存储系统，有很多典型的应用场景，本文将介绍 Etcd 的优秀实践之一：分布式锁。

##### 1.1 Etcd 优点

目前，可实现分布式锁的开源软件有很多，其中应用最广泛、大家最熟悉的应该就是 ZooKeeper，此外还有数据库、Redis、Chubby 等。但若从读写性能、可靠性、可用性、安全性和复杂度等方面综合考量，作为后起之秀的 Etcd 无疑是其中的 “佼佼者” 。它完全媲美业界“名宿”ZooKeeper，在有些方面，Etcd 甚至超越了 ZooKeeper，如 Etcd 采用的 Raft 协议就要比 ZooKeeper 采用的 Zab 协议简单、易理解。

Etcd 作为 
