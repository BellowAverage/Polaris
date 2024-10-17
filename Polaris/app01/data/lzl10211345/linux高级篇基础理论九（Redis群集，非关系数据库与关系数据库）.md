
--- 
title:  linux高级篇基础理论九（Redis群集，非关系数据库与关系数据库） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


**上一章**

后续会发布Redis真实部署操作

**目录**























### Redis

Redis是一个开源的、使用C语言编写、支持网络、可基于内存亦可持久化的日志型、key-value (键值对)数据库，是目前分布式架构中不可或缺的一环。 Redis服务器程序是单进程模型，也就是在一台服务器上可以同时启动多个Redis进程，而Redis 的实际处理速度则完全依靠于主进程的执行效率。若在服务器上只运行一个Rdis进程，当多个客户端同时访问时，服务器的处理能力会有一定程度的下降；若在同一台服务器上开启多个Rdis进程 Rdis在提高并发处理能力的同时会给服务器的CU造成很大压力。也就是说，在实际生产环境中 需要根据实际的需求来决定开启多少个Rdis进程。若对高并发要求更高一些，可能会考虑在同一台 服务器上开启多个进程：若CU资源比较紧张，采用单进程即可



### 区别

关系数据库基于关系模型上，存储数据结构统一，SQL语句用于执行对关系型数据库中数据的检索和操作。

非关系数据库有这不同的存储方式，使用真实开发环境也完全不同，分布式，开源横向扩展。

### 理论

##### 1、数据库的类型：

（1）关系型数据库：oracle，MySQL，SQLserver，DB2 （2）非关系型数据库：Redis、MongoDB、Hbase,CouhDB

##### 2、Redis的优点

具有极高的数据读写速度 支持丰富的数据类型 支持数据的持久化 原子性 支持数据备份

##### 3、Redis的命令工具

Redis-cli命令行工具 Redis-benchmark测试工具

##### 4,、Redis服务说明

主配置文件：  /etc/redis/6379.conf 端口：tcp   6379 重启服务：/etc/init.d/redis_6379  restart

##### 5、redis的相关命令：

set:存放数据 get：获取数据 keys *  :查询所有的键 exists   ： 判断键值是否存在 del   :  删除指定的键 type ： 获取键对应的数据类型 rename ：重命名键，如果有重名，会覆盖。 renamenx : 重命名键，不会覆盖。 dbsize  : 查看键的数目 select： 切换数据库（共16个库，分别是0-15） move ：  数据库之间移动数据 flushdb:删除当前库的数据（慎用） flushall :删除所有库的数据（慎用）

##### 6、Redis群集的角色

master：master之间分配slots（存取数据） slave：slave向它指定的master同步数据（备份数据）

##### 7、群集节点使用的tcp端口：

6379端口用于客户端的连接 16379端口用于群集总线

>  
 人生要尽全力度过每一关,不管遇到什么困难不可轻言放弃！！！ 

