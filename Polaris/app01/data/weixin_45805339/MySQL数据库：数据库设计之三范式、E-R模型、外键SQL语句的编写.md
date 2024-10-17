
--- 
title:  MySQL数据库：数据库设计之三范式、E-R模型、外键SQL语句的编写 
tags: []
categories: [] 

---
## MySQL

### 数据库设计之三范式
<li> 范式: 对设计数据库提出的一些规范，目前有迹可寻的共有8种范式，一般遵守3范式即可。 
  <ul>-  第一范式（1NF）: 强调的是列的原子性，即列不能够再分成其他几列。 -  第二范式（2NF）: 满足 1NF，另外包含两部分内容，一是表必须有一个主键；二是非主键字段 必须完全依赖于主键，而不能只依赖于主键的一部分。 -  第三范式（3NF）: 满足 2NF，另外非主键列必须直接依赖于主键，不能存在传递依赖。即不能存在：非主键列 A 依赖于非主键列 B，非主键列 B 依赖于主键的情况。 
### E-R模型

#### 介绍
- E-R模型即实体-关系模型，E-R模型就是描述数据库存储数据的结构模型。- E-R模型由 实体、属性、实体之间的关系构成，主要用来描述数据库中表结构。
#### 使用场景:
- 对于大型公司开发项目，我们需要根据产品经理的设计，我们先使用建模工具, 如:power designer，db desinger等这些软件来画出实体-关系模型(E-R模型)- 开发流程是先画出E-R模型，然后根据三范式设计数据库中的表结构
### 外键SQL语句的编写

#### 1. 外键约束作用
- 外键约束:对外键字段的值进行更新和插入时会和引用表中字段的数据进行验证，数据如果不合法则更新和插入会失败，保证数据的有效性
#### 2. 对于已经存在的字段添加外键约束
<li>– 为cls_id字段添加外键约束 
  <ul>- alter table students add foreign key(cls_id) references classes(id);
#### 3. 在创建数据表时设置外键约束
<li>– 创建学校表 
  <ul>- create table school( id int not null primary key auto_increment, name varchar(10));- create table teacher(id int not null primary key auto_increment, name varchar(10), s_id int not null, foreign key(s_id) references school(id));
#### 4. 删除外键约束
<li>– 需要先获取外键约束名称,该名称系统会自动生成,可以通过查看表创建语句来获取名称 
  <ul>- show create table teacher;- alter table teacher drop foreign key 外键名;