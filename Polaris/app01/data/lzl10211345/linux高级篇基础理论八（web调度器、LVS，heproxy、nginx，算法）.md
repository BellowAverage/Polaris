
--- 
title:  linux高级篇基础理论八（web调度器、LVS，heproxy、nginx，算法） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


**目录**

































### **群集概念**

##### 1、群集的类型

负载均衡群集：LB 高可用群集：HA 高性能运算群集：HPC

##### 2、负载均衡的结构

第一层：负载调度器 第二层：服务器池 第三层：共享存储

##### 3、负载均衡的工作模式

地址转换（NAT）模式 IP隧道（TUN）模式 直接路由（DR）模式

#####  4、LVS的负载调度算法：

轮询：rr 加权轮询：wrr 最少连接：lc 加权最少连接：wlc

### 5、NFS:

网络文件系统，用于linux之间共享文件。 服务：nfs,rpcbind 共享配置文件：/etc/exports

##### 6、lvs的DR需要解决的三个问题：

需要一个公共的群集ip地址 关闭web服务器的部分arp应答 关闭lvs的ICMP重定向

### 调度器

##### lvs调度器

些许调度器中lvs调度器性能为上等调度器，但是配置复杂

##### heproxy调度器

##### 1、Haproxy

是目前笔记流行的调度器，相对nginx还是比较好的，配置简单

#####  2、HTTP请求方式：

GET方式 POST方式

##### 3、返回状态码

正常的状态码为2xx,3xx 异常的状态码为4xx,5xx

##### 4、负载均衡常用调度算法

RR：轮询调度

>  
 RR算法是最简单最常用的一种算法，即轮询调度。例如，有三个节点A、B、C,第一个用户访问会被指派到节点A,第二个用户访问会被指派到节点B,第三个用户访问会 被指派到节点C,第四个用户访问继续指派到节点A,轮询分配访问请求实现负载均衡效果。此算法还有一种加权轮询，即根据每个节点的权重轮询分配访问请求 


 LC：最小连接数

>  
 LC算法即最小连接数算法，根据后端的节点连接数大小动态分配前端请求。例如，有三个节点A、B、C,各节点的连接数分别为A:4、B:5、C:6,此时如果有第个用户连接请求，会被指派到A上，连接数变为A:5、B:5、C:6:第二个用户请求会继续分配到A上，连接数变为A:6B:5、C:6,再有新的请求会分配给B,每次将新的请求指派给连接数最小的客户端。由于实际情况下A、B、C的连接数会动态释放，很难会出现一样连接数的情况，因此此算法相比较“算法有很大改进，是目前用到比较多的一种算法 


 SH：（基于来源问调度)

>  
 SH即基于来源访问调度算法，此算法用于一些有Session会话记录在 服务器端的场景，可以基于来源的P、Cookie等做群集调度。例如，使用基于源P的群集调度算法有三个节点A、B、C,第一个用户第一次访问被指派到了A,第二个用户第一次访问被指派到了B当第一个用户第二次访问时会被继续指派到A,第二个用户第二次访问时依旧会被指派到B,只要负载均衡调度器不重启，第一个用户访问都会被指派到A,，第二个用户访问都会被指派到B,实现群集的调度。此调度算法好处是实现会话保持，但某些P访问量非常大时会引起负载不均衡，部分节点古司昌卫大吴影向山久由田 


##### nginx反向代理调度器

Nginx的upstream模块支持群集功能，但是对群集节点健康检查功能不强，性能没有Haproxy好


