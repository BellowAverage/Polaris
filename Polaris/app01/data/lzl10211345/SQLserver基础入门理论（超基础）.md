
--- 
title:  SQLserver基础入门理论（超基础） 
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













































### SQL  server 是什么

>  
 SQL Server 是 公司推出的。具有使用方便好与相关程度高等优点，可跨越从运行Microsoft  的膝上型电脑到运行 2012 的大型的服务器等多种平台使用。 
 Microsoft SQL Server 是一个全面的数据库平台，使用集成的 (BI)工具提供了企业级的。Microsoft SQL Server 为关系型数据和提供了更安全可靠的存储功能，使您可以构建和管理用于业务的高可用和高性能的数据。 


## 一.入门概念

### 1. 基本概念

数据库系统（DBS） 数据库管理系统 （DBMS） SQL server     mysql 数据库管理员 （DBA）

### 2. 经典数据模型

网状模型   多对多 层次模型   一对多 关系模型   一对一

### 3.主流数据库：

（1）SQL Server （微软公司产品）               面向Windows操 作系统               简单 ，易用 （2）Oracle （甲骨文公司产品）        面向所用主流平台              安全，完善，操作复杂 （3）DB2（IBM公司产品）               面向所有主流平台               大型，安全，完善 （4）MySQL  （甲骨文公司收购）             开源，体积小，速度快，稳定

### 4.主键的特点：

由一个或多个字段组成，保证实体的唯一性 一个主键值对应一行数据 不允许取空值（NULL） 一个表只能有一个主键

### 5.数据完整性规则：

实体完整性 域完整性 用户定义完整性 引用完整性

### 6.SQL server2016的版本

企业版：用于实际的生产环境中 开发版：用于个人学习和交流

### 7.启动和停止数据库服务的方法：

方法一：使用服务管理器启动或停止数据库服务 方法二：使用SQL server配置管理器启动或停止数据库服务 (常用） 方法三：使用SSMS启动或停止数据库服务

### 8.数据库的分类：

（1）系统数据库 Master：记录系统级别信息，如登录用户，其他数据库文件的位置等 Model：数据模板，创建数据库时使用 Msdb：用于SQL server 代理计划警报和作业 Tempdb：保存临时对象或中间结果集 (2)用户数据库：用户自己创建的

### 9.身份验证模式：

Windows身份验证 混合身份验证（sql身份验证和window身份验证）

### 二，文件操作基础

### 1.文件类型

 （1）数据文件 主数据文件（.mdf）：有且只有一个 次要数据文件（.ndf）：可有可无，有可以多个 （2）事务日志文件（.ldf）：至少有一个 记录所有事务的SQL语句 用于恢复数据库

### 2.扩展数据库的方法

方法一：扩建现有文件的自动增长设置。 方法二：添加新文件（次要数据文件）

### 3.收缩数据库的方法：

方法一：手动收缩（针对数据库和文件） 方法二：自动收缩（针对数据库） 作用：释放数据库中未使用的空间

### 4.数据库的操作

创建库，扩展库，收缩库，分离和附加库，删除库

### 5.常用数据类型

int：整数类型 money：货币类型 字符类型：char,varchar,nchar,nvarchar datetime：时间日期

### 6.标识列（自增列）的要求：

类型：必须为数字类型 种子：开始的数字 递增量：数字之间的等差

### 7.约束：

成绩大于等于0并且小于等于100 成绩 &gt;= 0  and  成绩 &lt;= 100

### 8.创建表的语法格式

create   table   表名 （           列名1    数据类型  （），        列明2    数据类型  （），     ...  ）

### 9.删除表的语法格式

 drop   table    表名

>  
 ♥️关注，就是我创作的动力 
 ♥️点赞，就是对我最大的认可 
 ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 

