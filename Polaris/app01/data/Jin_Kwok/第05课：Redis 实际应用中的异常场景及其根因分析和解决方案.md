
--- 
title:  第05课：Redis 实际应用中的异常场景及其根因分析和解决方案 
tags: []
categories: [] 

---
上一篇较为详细地介绍了基于 Redis 的分布式缓存实现方案，解决了 “怎么用” 的问题。但是，在实际应用中，异常场景时有出现，作为一名攻城狮，仅仅“会用”是不够的，还需要能够定位、解决实际应用中出现的异常问题。

本文将介绍一组 Redis 实际应用中遇到的异常场景，如 Redis 进程无法拉起、故障倒换失败、Slot 指派失败等，并针对这些异常场景给出根因分析和可供参考的解决方案。

#### 1. `redis-server` 启动报错

我们先看第一个异常场景，即 `redis-server`启动报错: 

```
version 'GLIBC_2.14' not found 

```

接下来解析它的根因及解决方案。

##### 1.1 问题基本信息

假设有一项目，使用 Redis 集群作为分布式缓存，它只是整个项目中的一个模块。

Redis 集群部署环境为 Suse 12 Linux。

每一次迭代，项目组都会编译一个大包进行验证，在同一套部署环境中，Redis 集群部署“偶现”失败，部分节点上 `redis-server` 进程未能拉起，尝试用命令：`./redis-server ./xxx/redis.conf` 手动拉起 `redis-server` 进程，结果失败，报如下错误：

```
/lib64/libc.so.6: version `GLIBC_2.14' not found(required by /opt/…/redis-server)

```

##### 1.2 表因分析

很明显，报错信息显示安装环境 Li
