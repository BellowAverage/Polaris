
--- 
title:  MySQL数据库基本使用命令 
tags: []
categories: [] 

---
## MySQL基本使用

### 数据库操作

#### 0.查看时间
- select now();
#### 1.查看所有数据库
- show databases;
#### 2.创建一个新数据库并指定字符集
- create database 数据库名 charset=utf8;
#### 3.产看数据库创建信息
- show create database 数据库名;
#### 4.修改信息
- alter database 数据库 charset=utf8;
#### 5.使用数据库
- use 数据库名;
#### 6.查看当前使用的数据库
- select database();
#### 7.删除数据库
- drop database 数据库名;
### 数据库表操作

#### 0.先切换要操作的数据库
- use 数据库名;
#### 1.创建数据表
- create table 表名(字段名 类型 约束,…)- create table person(id int primary key, name char(10) not null default ‘匿名’);
#### 2.查看表的创建信息
- show create table 表名;
#### 3.查看表结构
- desc 表名;
#### 4.添加字段
- alter table 表名 add 字段名 类型 约束;
#### 5.修改字的类型或者约束
- alter table 表名 modify 字段名 新类型 新约束,…;- 注意:modify: 只能修改字段类型或者约束，不能修改字段名
#### 6.修改字段名或类型或约束
- alter table 表名 change 旧字段名 新字段名 新类型 新约束,…;
#### 6.删除字段
- alter table 表名 drop 字段名;
#### 7.删除表
- drop table 表名;
#### 8.修改表的存储引擎使用:
- alter table 表名 engine = 引擎类型;<li> 
  <ul>- 比如: alter table students engine = ‘MyISAM’;
### 表数据操作的SQL语句

#### 1.查询数据

##### 01.查询所有列
- select * from 表名;- select * from t_student;
##### 02.查询指定列
- select 列1,列2,… from 表名;- select c_id, c_name from t_student;
#### 2.添加数据:
<li> <h5>01.全列插入:</h5> 
  <ul>- insert into 表名 values (…);- insert into students values(0, ‘xx’, default, default, ‘男’);
##### 02.部分列插入：值的顺序与给出的列顺序对应
- insert into 表名 (列1,…) values(值1,…)- insert into students(name, age) values(‘王二小’, 15);
##### 03.全列多行插入
- insert into 表名 values(…),(…)…;- insert into students values(0, ‘张飞’, 55, 1.75, ‘男’),(0, ‘关羽’, 58, 1.85, ‘男’);
##### 04.部分列多行插入
- insert into 表名(列1,列2…) values(值1,…),(值1,…)…;- insert into students(name, height) values(‘刘备’, 1.75),(‘曹操’, 1.6);
###### 说明:
- 01.主键列是自动增长，但是在全列插入时需要占位，通常使用空值(0或者null或者default)- 02.在全列插入时，如果字段列有默认值可以使用 default 来占位，插入后的数据就是之前设置的默认值
#### 3.修改数据
- update 表名 set 列1=值1,列2=值2… where 条件;- update students set age = 18, gender = ‘女’ where id = 6;
#### 4.删除数据
- delete from 表名 where 条件;- delete from students where id=5;
#### 1. 问题:
- 上面的操作称之为物理删除，一旦删除就不容易恢复，我们可以使用逻辑删除的方式来解决这个问题。<li>– 添加删除表示字段，0表示未删除 1表示删除 
  <ul>- alter table students add isdelete bit default 0;- update students set isdelete = 1 where id = 8;<li> 
    <ul>- 逻辑删除，本质就是修改操作
### as和distinct关键字

#### as关键字
<li> 
  - 使用 as 给字段起别名 
  <ul>- select id as 序号, name as 名字, gender as 性别 from students;1. 可以通过 as 给表起别名<li>– 如果是单表查询 可以省略表名 
    <ul>- select id, name, gender from students;- select students.id,students.name,students.gender from students;- select s.id,s.name,s.gender from students as s;
#### distinct关键字
<li>distinct可以去除重复数据行。 
  <ul>- select distinct 列1,… from 表名;- select name, gender from students;- select distinct name, gender from students;
### where条件查询

#### where语句支持的运算符:
<li>比较运算符 
  <ul>- 等于: =- 大于: &gt;- 大于等于: &gt;=- 小于: &lt;- 小于等于: &lt;=- 不等于: != 或 &lt;&gt;- and- or- not- like是模糊查询关键字- %表示任意多个任意字符- _表示一个任意字符- between … and … 表示在一个连续的范围内查询- in 表示在一个非连续的范围内查询- 判断为空使用: is null- 判断非空使用: is not null
### 排序

#### 排序查询语法：
- select * from 表名 order by 列1 asc|desc [,列2 asc|desc,…]- 先按照列1进行排序，如果列1的值相同时，则按照 列2 排序，以此类推- asc从小到大排列，即升序- desc从大到小排序，即降序- 默认按照列值从小到大排序（即asc关键字）
### 分页查询

#### 语法
- select * from 表名 limit start,count- limit是分页查询关键字- start表示开始行索引，默认是0- count表示查询条数
#### 分页查询案例
- 查询学生表，获取第n页数据的SQL语句:- select * from students limit (n-1)*m,m