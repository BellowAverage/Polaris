
--- 
title:  Java知识体系最强总结，看完这篇就足够了 
tags: []
categories: [] 

---
**本人从事Java开发已多年，平时有记录问题解决方案和总结知识点的习惯，整理了一些有关Java的知识体系，这不是最终版，会不定期的更新**。也算是记录自己在从事编程工作的成长足迹，通过博客可以促进博主与阅读者的共同进步，结交更多志同道合的朋友。**特此分享给大家，本人见识有限，写的博客难免有错误或者疏忽的地方，还望各位大佬指点，在此表示感激不尽**。

整理的Java知识体系主要包括**基础知识，工具，并发编程，数据结构与算法，数据库，JVM，架构设计，应用框架，中间件，微服务架构，分布式架构，程序员的一些思考，团队与项目管理，运维，权限，推荐书籍，云计算，区块链**等，包含了作为一个Java工程师在开发工作学习中需要用到或者可能用到的绝大部分知识。**千里之行始于足下**，希望大家根据自己的薄弱点，查缺补漏，根据自己感兴趣的方面多学习，学的精通一点，从现在开始行动起来。**路漫漫其修远兮，吾将上下而求索，不管编程开发的路有多么难走，多么艰辛，我们都将百折不挠，不遗余力地去追求和探索**。

<img src="https://img-blog.csdnimg.cn/2019121810082198.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly90aGlua3dvbi5ibG9nLmNzZG4ubmV0,size_16,color_FFFFFF,t_70" alt="">

#### Java面试总结

Java面试总结汇总，整理了包括Java基础知识，集合容器，并发编程，JVM，常用开源框架Spring，MyBatis，数据库，中间件等，包含了作为一个Java工程师在面试中需要用到或者可能用到的绝大部分知识。欢迎大家阅读，本人见识有限，写的博客难免有错误或者疏忽的地方，还望各位大佬指点，在此表示感激不尽。文章持续更新中…

|序号|内容|链接地址
|------
|1|Java基础知识面试题（2020最新版）|
|2|Java集合容器面试题（2020最新版）|
|3|Java异常面试题（2020最新版）|
|4|并发编程面试题（2020最新版）|
|5|JVM面试题（2020最新版）|
|6|Spring面试题（2020最新版）|
|7|Spring MVC面试题（2020最新版）|
|8|Spring Boot面试题（2020最新版）|
|9|Spring Cloud面试题（2020最新版）|
|10|MyBatis面试题（2020最新版）|
|11|Redis面试题（2020最新版）|
|12|MySQL数据库面试题（2020最新版）|
|13|消息中间件MQ与RabbitMQ面试题（2020最新版）|
|14|Dubbo面试题（2020最新版）|
|15|Linux面试题（2020最新版）|
|16|Tomcat面试题（2020最新版）|
|17|ZooKeeper面试题（2020最新版）|
|18|Netty面试题（2020最新版）|
|19|架构设计&amp;分布式&amp;数据结构与算法面试题（2020最新版）|

#### 基础知识

##### Java概述

|序号|内容|链接地址
|------
|1|Java简介|
|2|Java发展历程|
|3|Java语言特点|
|4|JDK安装与环境变量配置|
|5|JVM、JRE和JDK的关系|
|6|Java是编译型还是解释型语言|
|||

##### 基础语法

大部分已完成

待整理：

Java开发必会的反编译知识（附支持对Lambda进行反编译的工具）

一文读懂什么是Java中的自动拆装箱

Java的枚举类型用法介绍

类、枚举、接口、数组、可变参数

泛型、序列化

|序号|内容|链接地址
|------
|1|Java标识符|
|2|Java关键字(Java 8版本)|
|3|Java注释|
|4|Java访问修饰符|
|5|Java分隔符|
|6|Java转义字符|
|7|Java进制|
|8|Java流程控制语句|
|9|Java流程控制语句-顺序结构|
|10|Java流程控制语句-分支结构|
|11|Java流程控制语句-循环结构|
|12|Java表达式|
|13|Java运算符|
|14|Java变量|
|15|Java常量|
|16|Java数据类型|
|17|Java反射|
|18|Java语法糖|
|19|Java注解|
|20|JSON简介|
|21|Properties类简介|
|22|XML简介|
|23|YML简介|
|24|Java8新特性-Lambda表达式|
|25|Java基础语法|

##### 面向对象

待整理：

抽象

继承、封装、多态

接口、抽象类、内部类

|序号|内容|链接地址
|------
|1|什么是面向对象|

##### 集合框架

迭代器、增强for、泛型

|序号|内容|链接地址
|------
|1|Java集合框架总结|
|2|ArrayList(JDK1.8)源码解析|
|3|HashMap(JDK1.8)源码解析|
|4|LinkedHashMap(JDK1.8)源码解析|
|5|LinkedList(JDK1.8)源码解析|
|6|TreeMap(JDK1.8)源码解析|

##### IO流

待整理：

File、递归

字节流、字节缓冲流

编码表、编码方式、转换流、序列化、序列化流、打印流、commons-io

##### 网络编程

网络概述、网络模型

Socket原理机制

UDP

TCP/IP

协议、OSI 七层协议、HTTP、HTTP2.0、HTTPS

网络安全

​ XSS、CSRF、SQL注入、Hash Dos、脚本注入、漏洞扫描工具、验证码

​ DDoS防范、用户隐私信息保护、序列化漏洞

​ 加密解密、对称加密、哈希算法、非对称加密

​ 服务安全、数据安全、数据备份

​ 网络隔离、登录跳板机、非外网分离

​ 认证、授权

##### 常用API

String、StringBuffer、StringBuilder、正则表达式

Number、Radom、Math、System、包装类

Arrays、Collections

###### 日期时间API

|序号|内容|链接地址
|------
|1|Java7日期时间API|
|2|史上最全Java7日期时间工具类|
|3|Java8日期时间API|
|4|史上最全Java8日期时间工具类|

##### 常用工具类库

待整理：OkHttp、commons-lang3

|序号|内容|链接地址
|------
|1|HttpClient工具类|
|2|WGS84地球坐标系，GCJ02火星坐标系，BD09百度坐标系简介与转换|
|3|Lombok简介、使用、工作原理、优缺点|
|4|Java几种常用JSON库性能比较|

##### 单元测试

JUnit

##### 异常

|序号|内容|链接地址
|------
|1|Java异常总结|
|2|Java异常架构与异常关键字|
|3|Java异常处理流程|
|4|如何选择异常类型|
|5|Java异常常见面试题|
|6|Java异常处理最佳实践|

##### 日志

|序号|内容|链接地址
|------
|1|常用日志框架Log4j，Logback，Log4j2性能比较与日志门面SLF4J简介|
|2|日志作用|
|3|Apache Log4j2详解|
|4|Log4j2同步日志，混合日志和异步日志配置详解|
|5|Log4j2配置文件详解|
|6|Log4j2的Appenders配置详解|
|7|Log4j2的Filters配置详解|
|8|Log4j2的Policy触发策略与Strategy滚动策略配置详解|
|9|Log4j2的Loggers配置详解|

##### Java8新特性

|序号|内容|链接地址
|------
|1|Java8新特性-Lambda表达式|
|2|Java8新特性-Optional|
|3|Java8新特性-Stream|
|4|Java8新特性-Base64|
|5|Java8新特性-日期时间API|

#### 工具

##### IDEA

|序号|内容|链接地址
|------
|1|IDEA常用配置和常用插件|
|2|IDEA中Maven依赖下载失败解决方案|
|3|在IDEA中使用Linux命令|

##### Eclipse &amp; STS

|序号|内容|链接地址
|------
|1|Eclipse &amp; Spring Tool Suite常用配置|

##### Maven

|序号|内容|链接地址
|------
|1|Maven简介|
|2|Maven安装与配置|
|3|Maven依赖冲突|
|4|手动安装Maven依赖|
|5|Maven部署jar包到远程仓库|
|6|Maven私服Nexus安装与使用|

##### Docker

|序号|内容|链接地址
|------
|1|使用Docker安装GitLab|
|2|虚拟机和容器有什么不同|
|3|Docker 从入门到实践系列一 - 什么是Docker|
|4|Docker 从入门到实践系列二 - Docker 安装|
|5|Docker 从入门到实践系列三 - Docker 常用命令|
|6|Docker 从入门到实践系列四 - Docker 容器编排利器 Docker Compose|

##### Git

|序号|内容|链接地址
|------
|1|Git简介|
|2|版本控制|
|3|Git忽略文件.gitignore详解|
|4|Git与SVN的区别|
|5|常用Git命令|
|6|Git，GitHub与GitLab的区别|

##### GitLab

##### GitKraken

##### Navicat

#### 并发编程

##### 基础知识

|序号|内容|链接地址
|------
|1|并发编程的优缺点|
|2|线程的状态和基本操作|
|3|进程和线程的区别(超详细)|
|4|创建线程的四种方式|

##### 并发理论

|序号|内容|链接地址
|------
|1|Java内存模型|
|2|重排序与数据依赖性|
|3|as-if-serial规则和happens-before规则的区别|
|4|Java并发理论总结|

##### 并发关键字

|序号|内容|链接地址
|------
|1|Java并发关键字-synchronized|
|2|Java并发关键字-volatile|
|3|Java并发关键字-final|

##### Lock体系

待整理：

公平锁 &amp; 非公平锁

乐观锁 &amp; 悲观锁

可重入锁 &amp; 不可重入锁

互斥锁 &amp; 共享锁

死锁

|序号|内容|链接地址
|------
|1|Lock简介与初识AQS|
|2|AQS(AbstractQueuedSynchronizer)详解与源码分析|
|3|ReentrantLock(重入锁)实现原理与公平锁非公平锁区别|
|4|读写锁ReentrantReadWriteLock源码分析|
|5|Condition源码分析与等待通知机制|
|6|LockSupport详解|

##### 并发容器

|序号|内容|链接地址
|------
|1|并发容器之ConcurrentHashMap详解(JDK1.8版本)与源码分析|
|2|并发容器之ConcurrentLinkedQueue详解与源码分析|
|3|并发容器之CopyOnWriteArrayList详解|
|4|并发容器之ThreadLocal详解|
|5|ThreadLocal内存泄漏分析与解决方案|
|6|并发容器之BlockingQueue详解|
|7|并发容器之ArrayBlockingQueue与LinkedBlockingQueue详解|

##### 线程池

|序号|内容|链接地址
|------
|1|线程池ThreadPoolExecutor详解|
|2|Executors类创建四种常见线程池|
|3|线程池之ScheduledThreadPoolExecutor详解|
|4|FutureTask详解|

##### 原子操作类

|序号|内容|链接地址
|------
|1|原子操作类总结|

##### 并发工具

|序号|内容|链接地址
|------
|1|并发工具之CountDownLatch与CyclicBarrier|
|2|并发工具之Semaphore与Exchanger|

##### 并发实践

|序号|内容|链接地址
|------
|1|实现生产者消费者的三种方式|

#### 数据结构与算法

##### 数据结构

|序号|内容|链接地址
|------
|1|红黑树详细分析(图文详解)，看了都说好|

```
1、数组
2、栈
3、队列
4、链表
5、树
	二叉树
    完全二叉树
    平衡二叉树
    二叉查找树（BST）
    红黑树
    B，B+，B*树
    LSM 树

字段是不是数据结构


```

##### 算法

语言只是编程工具，算法才是编程之魂！

```
1、排序算法：快速排序、归并排序、计数排序
2、搜索算法：回溯、递归、剪枝
3、图论：最短路径、最小生成树、网络流建模
4、动态规划：背包问题、最长子序列、计数问题
5、基础技巧：分治、倍增、二分法、贪心算法

宽度优先搜索
深度优先搜索
广度优先
双指针
扫描线

朴素贝叶斯
推荐算法


```

###### 排序算法

|序号|内容|链接地址
|------
|1|史上最全经典排序算法总结(Java实现)|
|2|冒泡排序（Bubble Sort）|
|3|选择排序（Selection Sort）|
|4|插入排序（Insertion Sort）|
|5|希尔排序（Shell Sort）|
|6|归并排序（Merge Sort）|
|7|快速排序（Quick Sort）|
|8|堆排序（Heap Sort）|
|9|计数排序（Counting Sort）|
|10|桶排序（Bucket Sort）|
|11|基数排序（Radix Sort）|

##### LeetCode

|序号|内容|链接地址
|------
|1|LeetCode第1题 两数之和(Two Sum)|
|2|LeetCode第3题 无重复字符的最长子串(Longest Substring Without Repeating Characters)|
|3|LeetCode第7题 整数反转(Reverse Integer)|
|4|LeetCode第9题 回文数(Palindrome Number)|
|5|LeetCode第13题 罗马数字转整数(Roman to Integer)|
|6|LeetCode第14题 最长公共前缀(Longest Common Prefix)|
|7|LeetCode第20题 有效的括号(Valid Parentheses)|
|8|LeetCode第26题 删除排序数组中的重复项(Remove Duplicates from Sorted Array)|

#### 数据库

##### Oracle

##### MySQL

###### 数据库基础知识

|序号|内容|链接地址
|------
|1|MySQL语句分类|
|2|MySQL插入语句insert into,insert ignore into,insert into … on duplicate key update,replace into-解决唯一键约束|
|3|MySQL复制表的三种方式|
|4|MySQL删除表的三种方式|
|5|MySQL中count(字段) ，count(主键 id) ，count(1)和count(*)的区别|

###### 数据类型

###### 引擎

###### 索引

###### 三大范式

###### 常用SQL语句

###### 存储过程与函数

###### 视图

###### MySQL优化

###### 事务

###### 数据备份与还原

##### Redis

|序号|内容|链接地址
|------
|1|Redis总结|
|2|Redis使用场景|
|3|Redis数据类型|
|4|Redis持久化|
|5|Redis过期键的删除策略|
|6|Redis数据淘汰策略|
|7|Redis与Memcached的区别|
|8|Redis常见面试题(精简版)|
|9|Redis中缓存雪崩、缓存穿透等问题的解决方案|
|10|阿里云Redis开发规范学习总结|
|11|Redis开发常用规范|
|12|这可能是最中肯的Redis规范了|

#### Java虚拟机

##### 深入理解Java虚拟机

|序号|内容|链接地址
|------
|1|深入理解Java虚拟机-走近Java|
|2|深入理解Java虚拟机-Java内存区域与内存溢出异常|
|3|深入理解Java虚拟机-垃圾回收器与内存分配策略|
|4|深入理解Java虚拟机-虚拟机执行子系统|
|5|深入理解Java虚拟机-程序编译与代码优化|
|6|深入理解Java虚拟机-高效并发|

#### 架构设计

高可用架构

高并发架构

可伸缩架构

集群

##### 设计模式

常用设计模式

创建型： 单例模式、工厂模式、抽象工厂模式

结构型： 适配器模式、外观模式、代理模式、装饰器模式

行为型： 观察者模式、策略模式、模板模式

|序号|内容|链接地址
|------
|1|设计模式|

###### 创建型模式

|序号|内容|链接地址
|------
|1|抽象工厂模式|
|2|单例模式|
|3|工厂模式|
|4|建造者模式|
|5|原型模式|

###### 结构型模式

|序号|内容|链接地址
|------
|1|代理模式|
|2|过滤器模式|
|3|桥接模式|
|4|适配器模式|
|5|外观模式|
|6|享元模式|
|7|装饰器模式|
|8|组合模式|

###### 行为型模式

|序号|内容|链接地址
|------
|1|备忘录模式|
|2|策略模式|
|3|迭代器模式|
|4|访问者模式|
|5|观察者模式|
|6|解释器模式|
|7|空对象模式|
|8|命令模式|
|9|模板模式|
|10|责任链模式|
|11|中介者模式|
|12|状态模式|

###### J2EE模式

|序号|内容|链接地址
|------
|1|MVC模式|
|2|传输对象模式|
|3|服务定位器模式|
|4|拦截过滤器模式|
|5|前端控制器模式|
|6|数据访问对象模式|
|7|业务代表模式|
|8|组合实体模式|

###### 实践应用

|序号|内容|链接地址
|------
|1|业务复杂=if else？刚来的大神竟然用策略+工厂彻底干掉了他们！|

#### 应用框架

如何学习一个框架或者技术
-  是什么，简介，概述 -  有什么用，用途，使用场景 -  怎么用，在实际开发中的应用，注意事项 -  优缺点 -  框架原理，工作流程，工作原理 -  常见面试题 -  源码分析，核心类，核心方法，设计模式 -  发布博客，在开发和实践中，博客反馈中持续改进 -  与同事朋友交流，技术论坛，技术分享中持续丰富知识 
常用框架
-  集成开发工具（IDE）：Eclipse、MyEclipse、Spring Tool Suite（STS）、Intellij IDEA、NetBeans、JBuilder、JCreator -  JAVA服务器：tomcat、jboss、websphere、weblogic、resin、jetty、apusic、apache -  负载均衡：nginx、lvs -  web层框架：Spring MVC、Struts2、Struts1、Google Web Toolkit（GWT）、JQWEB -  服务层框架：Spring、EJB -  持久层框架：Hibernate、MyBatis、JPA、TopLink -  数据库：Oracle、MySql、MSSQL、Redis -  项目构建：maven、ant -  持续集成：Jenkins -  版本控制：SVN、CVS、VSS、GIT -  私服：Nexus -  消息组件：IBM MQ、RabbitMQ、ActiveMQ、RocketMq -  日志框架：Commons Logging、log4j 、slf4j、IOC -  缓存框架：memcache、redis、ehcache、jboss cache -  RPC框架：Hessian、Dubbo -  规则引擎：Drools -  工作流：Activiti -  批处理：Spring Batch -  通用查询框架：Query DSL -  JAVA安全框架：shiro、Spring Security -  代码静态检查工具：FindBugs、PMD -  Linux操作系统：CentOS、Ubuntu、SUSE Linux、 -  常用工具：PLSQL Developer（Oracle）、Navicat（MySql）、FileZilla（FTP）、Xshell（SSH）、putty（SSH）、SecureCRT（SSH）、jd-gui（反编译） 
##### Spring

|序号|内容|链接地址
|------
|1|Spring简介、设计理念、优缺点、应用场景|
|2|Spring模块组成(框架组成、整体架构、体系架构、体系结构)|
|3|Spring容器中bean的生命周期|
|4|控制反转(IoC)与依赖注入(DI)详解|

###### 《Spring实战》读书笔记

|序号|内容|链接地址
|------
|1|《Spring实战》读书笔记-第1章 Spring之旅|
|2|《Spring实战》读书笔记-第2章 装配Bean|
|3|《Spring实战》读书笔记-第3章 高级装配|
|4|《Spring实战》读书笔记-第4章 面向切面的Spring|
|5|《Spring实战》读书笔记-第5章 构建Spring Web应用程序|
|6|《Spring实战》读书笔记-第6章 渲染Web视图|
|7|《Spring实战》读书笔记-第7章 Spring MVC的高级技术|

##### Spring MVC

##### MyBatis

|序号|内容|链接地址
|------
|1|MyBatis官方文档|
|2|MyBatis官方文档-简介|
|3|MyBatis官方文档-入门|
|4|MyBatis官方文档-XML 配置|
|5|MyBatis官方文档-XML 映射文件|
|6|MyBatis官方文档-动态 SQL|
|7|MyBatis官方文档-Java API|
|8|MyBatis官方文档-SQL 语句构建器类|
|9|MyBatis官方文档-日志|
|10|MyBatis功能架构|
|11|MyBatis工作原理|
|12|MyBatis核心类|
|13|MyBatis面试宝典|
|14|MyBatis实现一对一，一对多关联查询|
|15|MyBatis缓存|

###### MyBatis 源码分析

|序号|内容|链接地址
|------
|1|MyBatis 源码分析 - MyBatis入门|
|2|MyBatis 源码分析 - 配置文件解析过程|
|3|MyBatis 源码分析 - 映射文件解析过程|
|4|MyBatis 源码分析 - SQL 的执行过程|
|5|MyBatis 源码分析 - 内置数据源|
|6|MyBatis 源码分析 - 缓存原理|
|7|MyBatis 源码分析 - 插件机制|

##### Quartz

<th align="left">序号</th>|内容|链接地址
|------
<td align="left">1</td>|Quartz简介|
<td align="left"></td>||

##### Hibernate

##### Shiro

##### Spring Security

##### Netty

##### 搜索引擎

###### Lucene/Solr

###### Elasticsearch

###### ELK

#### 中间件

##### 消息中间件

###### RabbitMQ

###### RocketMQ

###### ActiveMQ

###### Kafka

##### 远程过程调用中间件

###### Dubbo

##### 数据访问中间件

Sharding JDBC

MyCat

##### Web应用服务器

###### Tomcat

待整理：Tomcat各组件作用 Tomcat集群 Tomcat面试题

|序号|内容|链接地址
|------
|1|Win10安装Tomcat服务器与配置环境变量|
|2|Linux(CentOS7)安装Tomcat与设置Tomcat为开机启动项|
|3|Tomcat与JDK版本对应关系，Tomcat各版本特性|
|4|Tomcat目录结构|
|5|Tomcat乱码与端口占用的解决方案|
|6|Tomcat系统架构与请求处理流程|
|7|史上最强Tomcat8性能优化|

###### Nginx

##### 缓存

本地缓存

客户端缓存

服务端缓存

​ web缓存，Redis，Memcached，Ehcache

##### 其他

###### Zookeeper

#### 微服务与分布式

##### Spring Boot

|序号|内容|链接地址
|------
|1|application.yml与bootstrap.yml的区别|
|2|一分钟了解约定优于配置|

##### Spring Cloud

|序号|内容|链接地址
|------
|1|Spring Cloud入门-十分钟了解Spring Cloud|
|2|Spring Cloud入门-Eureka服务注册与发现(Hoxton版本)|
|3|Spring Cloud入门-Ribbon服务消费者(Hoxton版本)|
|4|Spring Cloud入门-Hystrix断路器(Hoxton版本)|
|5|Spring Cloud入门-Hystrix Dashboard与Turbine断路器监控(Hoxton版本)|
|6|Spring Cloud入门-OpenFeign服务消费者(Hoxton版本)|
|7|Spring Cloud入门-Zuul服务网关(Hoxton版本)|
|8|Spring Cloud入门-Config分布式配置中心(Hoxton版本)|
|9|Spring Cloud入门-Bus消息总线(Hoxton版本)|
|10|Spring Cloud入门-Sleuth服务链路跟踪(Hoxton版本)|
|11|Spring Cloud入门-Consul服务注册发现与配置中心(Hoxton版本)|
|12|Spring Cloud入门-Gateway服务网关(Hoxton版本)|
|13|Spring Cloud入门-Admin服务监控中心(Hoxton版本)|
|14|Spring Cloud入门-Oauth2授权的使用(Hoxton版本)|
|15|Spring Cloud入门-Oauth2授权之JWT集成(Hoxton版本)|
|16|Spring Cloud入门-Oauth2授权之基于JWT完成单点登录(Hoxton版本)|
|17|Spring Cloud入门-Nacos实现注册和配置中心(Hoxton版本)|
|18|Spring Cloud入门-Sentinel实现服务限流、熔断与降级(Hoxton版本)|
|19|Spring Cloud入门-Seata处理分布式事务问题(Hoxton版本)|
|20|Spring Cloud入门-汇总篇(Hoxton版本)|

##### 服务注册发现

##### 服务配置

##### 负载均衡

##### 服务调用

##### 服务限流

##### 熔断降级

##### 网关路由

##### 服务权限

##### 链路追踪

##### 分布式事务

##### 分布式缓存

##### 分布式会话

##### 日志收集

##### 服务监控

##### 消息驱动

##### 数据处理流

##### 自动化测试与部署

##### 第三方支持

##### 分布式协调服务Zookeeper

#### 程序员的一些思考

|序号|内容|链接地址
|------
|1|程序员写个人技术博客的价值与意义|
|2|Java知识体系最强总结(2020版)|
|3|博客之星，有你的鼓励更精彩|

#### 团队与项目管理

##### 需求调研

##### 项目管理

|序号|内容|链接地址
|------
|1|Worktile、Teambition与Tower项目管理软件对比|

##### 代码管理

##### 文档管理

|序号|内容|链接地址
|------
|1|几款常见接口管理平台对比|
|2|Swagger2常用注解说明|

##### 测试

#### Python

|序号|内容|链接地址
|------
|1|Win10安装Python3.9|
|2|Anaconda安装|
|3|PyCharm2020.3.2安装|
|4|PyCharm常用配置和常用插件|

#### 运维

常规监控

APM

持续集成(CI/CD)：Jenkins，环境分离

自动化运维：Ansible，puppet，chef

测试：TDD 理论，单元测试，压力测试，全链路压测，A/B 、灰度、蓝绿测试

虚拟化：KVM，Xen，OpenVZ

容器技术：Docker

云技术：OpenStack

DevOps

#### 操作系统

计算机操作系统

计算机原理

Linux

CPU

进程，线程，协程

##### CentOS8

|序号|内容|链接地址
|------
|1|VMware Workstation Pro 16搭建CentOS8虚拟机集群|
|2|CentOS8安装Docker|
|3|CentOS8搭建Nacos1.4.0集群|
|4|CentOS8安装GitLab13.7.2|
|5|CentOS8安装MySQL8|

#### 推荐书籍

|序号|内容|链接地址
|------
|1|读书清单-计算机|
|||

#### 读书笔记

|序号|内容|链接地址
|------
|1|高效休息法-读书笔记|
|2|斯坦福高效睡眠法-读书笔记|
|3|高效能人士的七个习惯-读书笔记|
|4|富爸爸穷爸爸-读书笔记|
|5|如何阅读一本书-读书笔记|
|6|人性的弱点-读书笔记|
|7|麦肯锡极简工作法-读书笔记|
|||
|||

#### 云计算

IaaS、SaaS、PaaS、虚拟化技术、openstack、Serverlsess

#### 搜索引擎

Solr、Lucene、Nutch、Elasticsearch

#### 权限管理

Shiro、Spring Security

#### 区块链

哈希算法、Merkle树、公钥密码算法、共识算法、Raft协议、Paxos 算法与 Raft 算法、拜占庭问题与算法、消息认证码与数字签名

有幸看到一篇这样一组数据。

<img src="https://img-blog.csdnimg.cn/c3114b9c3bf947adb177b7aaf91e1be5.png" alt="">

根据这些我不得总结，it行业确实人才紧缺，

##### **网络安全行业特点**

1、就业薪资非常高，涨薪快 2021年猎聘网发布网络安全行业就业薪资行业最高人均33.77万！ <img src="https://img-blog.csdnimg.cn/img_convert/d5f06d6b9945fd6e8a5f92a0198e5446.png" alt="">

2、人才缺口大，就业机会多

2019年9月18日《中华人民共和国中央人民政府》官方网站发表：我国网络空间安全人才 需求140万人，而全国各大学校每年培养的人员不到1.5W人。猎聘网《2021年上半年网络安全报告》预测2027年网安人才需求300W，现在从事网络安全行业的从业人员只有10W人。 <img src="https://img-blog.csdnimg.cn/img_convert/9cf857398f52a97ff49d437ac5fe690a.png" alt="">

##### 行业发展空间大，岗位非常多

网络安全行业产业以来，随即新增加了几十个网络安全行业岗位︰网络安全专家、网络安全分析师、安全咨询师、网络安全工程师、安全架构师、安全运维工程师、渗透工程师、信息安全管理员、数据安全工程师、网络安全运营工程师、网络安全应急响应工程师、数据鉴定师、网络安全产品经理、网络安全服务工程师、网络安全培训师、网络安全审计员、威胁情报分析工程师、灾难恢复专业人员、实战攻防专业人员…

##### 职业增值潜力大

网络安全专业具有很强的技术特性，尤其是掌握工作中的核心网络架构、安全技术，在职业发展上具有不可替代的竞争优势。

随着个人能力的不断提升，所从事工作的职业价值也会随着自身经验的丰富以及项目运作的成熟，升值空间一路看涨，这也是为什么受大家欢迎的主要原因。

从某种程度来讲，在网络安全领域，跟医生职业一样，越老越吃香，因为技术愈加成熟，自然工作会受到重视，升职加薪则是水到渠成之事。

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

## 学习资料分享

如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**
