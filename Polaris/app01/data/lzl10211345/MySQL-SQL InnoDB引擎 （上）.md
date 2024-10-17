
--- 
title:  MySQL-SQL InnoDB引擎 （上） 
tags: []
categories: [] 

---
>  
  ♥️**作者：小刘在C站** 
  ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
  ♥️**努力不一定有回报，但一定会有收获加油！一起努力，共赴美好人生！** 
  ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
  **♥️小刘私信可以随便问，只要会绝不吝啬，感谢CSDN让你我相遇！** 
 

**目录**

































































### **1 ****逻辑存储结构**

###  1). 表空间

### 2). 段

### 3). 区 



### 4). 页



### 5). 行

行，InnoDB 存储引擎数据是按行进行存放的。

### **2 ****架构 **

## **2.1 ****概述 **





<img alt="" height="552" src="https://img-blog.csdnimg.cn/40803221c8ae4f328f2a7188f354e8ec.png" width="754">

## **6.2.2 ****内存结构**



<img alt="" height="570" src="https://img-blog.csdnimg.cn/8b0ef96d924d438aaad0d5b7fd28d575.png" width="293">

 

## 

## 1). Buffer Pool 

## 









##  2). Change Buffer 

 先来看一幅图，这个是二级索引的结构图：

<img alt="" height="352" src="https://img-blog.csdnimg.cn/c84789f59aac48c7935cd76ed7d57d51.png" width="830">

 

## 3). Adaptive Hash Index 

## 4). Log Buffer

## 

1: 日志在每次事务提交时写入并刷新到磁盘，默认值。 

0: 每秒将日志写入并刷新到磁盘一次。

2: 日志在每次事务提交后写入，并每秒刷新到磁盘一次。

<img alt="" height="104" src="https://img-blog.csdnimg.cn/53121973f41a493497a49e105a1fb45d.png" width="760">

##  **2.3 ****磁盘结构**



<img alt="" height="564" src="https://img-blog.csdnimg.cn/12f84a025ff54d0b88164605b1759726.png" width="468">

## 1). System Tablespace  

 系统表空间，默认的文件名叫 ibdata1。 

## 2). File-Per-Table Tablespaces

 

##  3). General Tablespaces

## A. 创建表空间

```
CREATE TABLESPACE ts_name ADD DATAFILE 'file_name' ENGINE = engine_name; 
```

<img alt="" height="43" src="https://img-blog.csdnimg.cn/b23b928b31274c649559d3701825433d.png" width="749">

##  B. 创建表时指定表空间

```
CREATE TABLE xxx ... TABLESPACE ts_name;
```

<img alt="" height="49" src="https://img-blog.csdnimg.cn/89d76d49d277468397f12b0a8624e799.png" width="760">

##  4). Undo Tablespaces 

## 5). Temporary Tablespaces

## 6). Doublewrite Buffer Files 

##  7). Redo Log

 以循环方式写入重做日志文件，涉及两个文件：

 

 

<img alt="" height="530" src="https://img-blog.csdnimg.cn/2d8c42a69a3242faaa921a6aebe1f943.png" width="741">

## **2.4 ****后台线程**



<img alt="" height="525" src="https://img-blog.csdnimg.cn/f2931394a2ce4e69bd7dfe6cc9c1c1c1.png" width="676">

 

### 1). Master Thread 

### 2). IO Thread 

 我们可以通过以下的这条指令，查看到InnoDB的状态信息，其中就包含IO Thread信息。

```
show engine innodb status \G;
```

<img alt="" height="446" src="https://img-blog.csdnimg.cn/23adfe6bb51145a89cd26e03faefcf63.png" width="755">

###  3). Purge Thread 

### 4). Page Cleaner Thread

>  
  ♥️关注，就是我创作的动力 
  ♥️点赞，就是对我最大的认可 
  ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 
 
