
--- 
title:  MySQL-SQL视图详细 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**努力不一定有回报，但一定会有收获加油！一起努力，共赴美好人生！** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 **♥️小刘私信可以随便问，只要会绝不吝啬，感谢CSDN让你我相遇！** 


**前言**

本章讲解SQL语言中视图，为上章。

**目录**



































### **1 ****视图 **

#### **1.1 ****介绍 **

### **1.2 ****语法**

#### 1). 创建

```
CREATE [OR REPLACE] VIEW 视图名称[(列名列表)] AS SELECT语句 [ WITH [
CASCADED | LOCAL ] CHECK OPTION ]
```

#### 2). 查询 

```
查看创建视图语句：SHOW CREATE VIEW 视图名称;
查看视图数据：SELECT * FROM 视图名称 ...... ;
```

#### 3). 修改 

```
方式一：CREATE [OR REPLACE] VIEW 视图名称[(列名列表)] AS SELECT语句 [ WITH
[ CASCADED | LOCAL ] CHECK OPTION ]
方式二：ALTER VIEW 视图名称[(列名列表)] AS SELECT语句 [ WITH [ CASCADED |
LOCAL ] CHECK OPTION ] 
```

#### 4). 删除

```
DROP VIEW [IF EXISTS] 视图名称 [,视图名称] ...
```

```
-- 创建视图
create or replace view stu_v_1 as select id,name from student where id &lt;= 10;


-- 查询视图

show create view stu_v_1;
select * from stu_v_1;
select * from stu_v_1 where id &lt; 3;


-- 修改视图
create or replace view stu_v_1 as select id,name,no from student where id &lt;= 10;
alter view stu_v_1 as select id,name from student where id &lt;= 10;


-- 删除视图
drop view if exists stu_v_1;
```

```
create or replace view stu_v_1 as select id,name from student where id &lt;= 10 ;

select * from stu_v_1;

insert into stu_v_1 values(6,'Tom');

insert into stu_v_1 values(17,'Tom22');
```



### **1.3 ****检查选项 **

### 1). CASCADED 

###  2). LOCAL 

###  **1.4 ****视图的更新**

```
create view stu_v_count as select count(*) from student;
```

```
insert into stu_v_count values(10);
```

<img alt="" height="40" src="https://img-blog.csdnimg.cn/49c9b58fbdae465aa63ad70f6c09534a.png" width="771">

###  **1.5 ****视图作用 **

#### 1). 简单 

#### 2). 安全

#### 3). 数据独立 

### **1.6 ****案例**

```
create view tb_user_view as select id,name,profession,age,gender,status,createtime
from tb_user;
select * from tb_user_view;
```

```
create view tb_stu_course_view as select s.name student_name , s.no student_no ,
c.name course_name from student s, student_course sc , course c where s.id =
sc.studentid and sc.courseid = c.id;
select * from tb_stu_course_view;
```

>  
                   ♥️关注，就是我创作的动力 
                   ♥️点赞，就是对我最大的认可 
                   ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 
                  
