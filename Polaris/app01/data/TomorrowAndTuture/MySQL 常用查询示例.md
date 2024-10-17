
--- 
title:  MySQL 常用查询示例 
tags: []
categories: [] 

---
本文主要以《数据库系统概论》教材里的例子为例（教材里的 SQL 比较广泛，不只是针对 MySQL，但大部分概念都是适用的），正好来一波满满的回忆杀！

为什么选择学生表、课程表和选课表作为例子呢？原因也简单，主要是因为这三张表能将大部分的查询示例都覆盖掉，而且理解方面也容易。

## 数据表创建

### 学生表

```
CREATE TABLE `student` (
  `Sno` char(9) NOT NULL,
  `Sname` char(20) DEFAULT NULL,
  `Ssex` char(2) DEFAULT NULL,
  `Sage` smallint(6) DEFAULT NULL,
  `Sdept` char(20) DEFAULT NULL,
  PRIMARY KEY (`Sno`),
  UNIQUE KEY `Sname` (`Sname`)
);
```

### 课程表

```
CREATE TABLE `course` (
  `Cno` char(4) NOT NULL,
  `Cname` char(40) NOT NULL,
  `Cpno` char(4) DEFAULT NULL,
  `Ccredit` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`Cno`),
  KEY `Cpno` (`Cpno`),
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`Cpno`) REFERENCES `course` (`cno`)
);
```

### 选课表 

```
CREATE TABLE `sc` (
  `Sno` char(9) NOT NULL,
  `Cno` char(4) NOT NULL,
  `Grade` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`Sno`,`Cno`),
  KEY `Cno` (`Cno`),
  CONSTRAINT `sc_ibfk_1` FOREIGN KEY (`Sno`) REFERENCES `student` (`sno`),
  CONSTRAINT `sc_ibfk_2` FOREIGN KEY (`Cno`) REFERENCES `course` (`cno`)
);
```

## 数据插入

### 学生表

```
INSERT INTO `student` VALUES ('201215121', '李勇', '男', 20, 'CS');
INSERT INTO `student` VALUES ('201215122', '刘晨', '女', 19, 'CS');
INSERT INTO `student` VALUES ('201215123', '王敏', '女', 18, 'MA');
INSERT INTO `student` VALUES ('201215125', '张立', '男', 19, 'IS');
```

### 课程表

**注意：**课程表数据插入时可能会受外键约束影响导致无法插入数据，可先将 Cpno 字段设为空，记录插入后再使用 update 进行修改。

```
INSERT INTO `course` VALUES ('1', '数据库', '5', 4);
INSERT INTO `course` VALUES ('2', '数学', NULL, 2);
INSERT INTO `course` VALUES ('3', '信息系统', '1', 4);
INSERT INTO `course` VALUES ('4', '操作系统', '6', 3);
INSERT INTO `course` VALUES ('5', '数据结构', '7', 4);
INSERT INTO `course` VALUES ('6', '数据处理', NULL, 2);
INSERT INTO `course` VALUES ('7', 'PASCAL语言', '6', 4);
```

### 选课表

**注意：**选课表的外键约束，与上同理，因此需要先插入好 学生表 和 课程表 的数据。

```
INSERT INTO `sc` VALUES ('201215121', '1', 92);
INSERT INTO `sc` VALUES ('201215121', '2', 85);
INSERT INTO `sc` VALUES ('201215121', '3', 88);
INSERT INTO `sc` VALUES ('201215122', '2', 90);
INSERT INTO `sc` VALUES ('201215122', '3', 80);
```

## 数据查询

### 常用查询条件

<img alt="" height="462" src="https://img-blog.csdnimg.cn/28845d3efa8f4a799fc95ef4d5d6c225.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATG9vb29raW5n,size_20,color_FFFFFF,t_70,g_se,x_16" width="1190">

### 单表查询

#### 普通查询

```
select Sno, Sname from Student;
```

```
mysql&gt; select Sno, Sname from Student;
+-----------+--------+
| Sno       | Sname  |
+-----------+--------+
| 201215122 | 刘晨   |
| 201215125 | 张立   |
| 201215121 | 李勇   |
| 201215123 | 王敏   |
+-----------+--------+
4 rows in set (0.00 sec)
```

#### 查询计算后的值 

```
select Sname, 2021 - Sage from student;
```

```
mysql&gt; select Sname, 2021 - Sage from student;
+--------+-------------+
| Sname  | 2021 - Sage |
+--------+-------------+
| 李勇   |        2001 |
| 刘晨   |        2002 |
| 王敏   |        2003 |
| 张立   |        2002 |
+--------+-------------+
4 rows in set (0.00 sec)
```

#### 字段设置别名

```
select Sname, 2021 - Sage as birth from student;
```

```
mysql&gt; select Sname, 2021 - Sage as birth from student;
+--------+-------+
| Sname  | birth |
+--------+-------+
| 李勇   |  2001 |
| 刘晨   |  2002 |
| 王敏   |  2003 |
| 张立   |  2002 |
+--------+-------+
4 rows in set (0.00 sec)
```

#### 查询结果去重 

```
select distinct Sno from SC;
```

```
mysql&gt; select distinct Sno from SC;
+-----------+
| Sno       |
+-----------+
| 201215121 |
| 201215122 |
+-----------+
2 rows in set (0.00 sec)
```

#### where条件查询 

```
select Sname from Student where Sdept='CS';
```

```
mysql&gt; select Sname from Student where Sdept='CS';
+--------+
| Sname  |
+--------+
| 李勇   |
| 刘晨   |
+--------+
2 rows in set (0.00 sec)
```



```
select Sname, Sage from Student where Sage&lt;20;
```

```
mysql&gt; select Sname, Sage from Student where Sage&lt;20;
+--------+------+
| Sname  | Sage |
+--------+------+
| 刘晨   |   19 |
| 王敏   |   18 |
| 张立   |   19 |
+--------+------+
3 rows in set (0.00 sec)
```



```
select distinct Sno from SC where Grade&gt;60;
```

```
mysql&gt; select distinct Sno from SC where Grade&gt;60;
+-----------+
| Sno       |
+-----------+
| 201215121 |
| 201215122 |
+-----------+
2 rows in set (0.00 sec)
```

#### between ... and 

```
select Sname, Sdept, Sage from Student where Sage between 20 and 23;
```

```
mysql&gt; select Sname, Sdept, Sage from Student where Sage between 20 and 23;
+--------+-------+------+
| Sname  | Sdept | Sage |
+--------+-------+------+
| 李勇   | CS    |   20 |
+--------+-------+------+
1 row in set (0.00 sec)
```

#### in

```
select Sname, Ssex from Student where Sdept in ('CS', 'MA', 'IS');
```

```
mysql&gt; select Sname, Ssex from Student where Sdept in ('CS', 'MA', 'IS');
+--------+------+
| Sname  | Ssex |
+--------+------+
| 李勇   | 男   |
| 刘晨   | 女   |
| 王敏   | 女   |
| 张立   | 男   |
+--------+------+
4 rows in set (0.00 sec)
```

#### not in

```
select Sname, Ssex from Student where Sdept not in ('CS', 'MA', 'IS');
```

```
mysql&gt; select Sname, Ssex from Student where Sdept not in ('CS', 'MA', 'IS');
Empty set (0.00 sec)
```

#### like

```
select Sname, Sno, Ssex from Student where Sname like '刘%';
```

```
mysql&gt; select Sname, Sno, Ssex from Student where Sname like '刘%';
+--------+-----------+------+
| Sname  | Sno       | Ssex |
+--------+-----------+------+
| 刘晨   | 201215122 | 女   |
+--------+-----------+------+
1 row in set (0.00 sec)
```



```
select Sname, Sno, Ssex from Student where Sname like '欧阳_';
```

```
mysql&gt; select Sname, Sno, Ssex from Student where Sname like '欧阳_';
Empty set (0.00 sec)
```

#### null

```
select Sno, Cno from SC where Grade is not null;
```

#### or 

```
select Sname from Student where Sdept='CS' or Sdept='MA' or Sdept='IS';
```

```
mysql&gt; select Sname from Student where Sdept='CS' or Sdept='MA' or Sdept='IS';
+--------+
| Sname  |
+--------+
| 李勇   |
| 刘晨   |
| 王敏   |
| 张立   |
+--------+
4 rows in set (0.00 sec)
```

#### order by

```
select Sno, Grade from SC where Cno='3' order by Grade desc;
```

```
mysql&gt; select Sno, Grade from SC where Cno='3' order by Grade desc;
+-----------+-------+
| Sno       | Grade |
+-----------+-------+
| 201215121 |    88 |
| 201215122 |    80 |
+-----------+-------+
2 rows in set (0.00 sec)
```

#### order by 多重排序

```
select * from Student order by Sdept, Sage desc;
```

```
mysql&gt; select * from Student order by Sdept, Sage desc;
+-----------+--------+------+------+-------+
| Sno       | Sname  | Ssex | Sage | Sdept |
+-----------+--------+------+------+-------+
| 201215121 | 李勇   | 男   |   20 | CS    |
| 201215122 | 刘晨   | 女   |   19 | CS    |
| 201215125 | 张立   | 男   |   19 | IS    |
| 201215123 | 王敏   | 女   |   18 | MA    |
+-----------+--------+------+------+-------+
4 rows in set (0.00 sec)
```

### 聚合查询

#### 常用聚合函数

<img alt="" height="282" src="https://img-blog.csdnimg.cn/c5b14234031e4991969834215a90cbb8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATG9vb29raW5n,size_20,color_FFFFFF,t_70,g_se,x_16" width="1146">

#### count

```
select count(*) from Student;
```

```
mysql&gt; select count(*) from Student;
+----------+
| count(*) |
+----------+
|        4 |
+----------+
1 row in set (0.00 sec)
```



```
select count(distinct Sno) from SC;
```

```
mysql&gt; select count(distinct Sno) from SC;
+---------------------+
| count(distinct Sno) |
+---------------------+
|                   2 |
+---------------------+
1 row in set (0.00 sec)
```

#### avg

```
select avg(Grade) from SC where Cno='1';
```

```
mysql&gt; select avg(Grade) from SC where Cno='1';
+------------+
| avg(Grade) |
+------------+
|    92.0000 |
+------------+
1 row in set (0.00 sec)
```

#### max

```
select max(Grade) from SC where Cno='1';
```

```
mysql&gt; select max(Grade) from SC where Cno='1';
+------------+
| max(Grade) |
+------------+
|         92 |
+------------+
1 row in set (0.00 sec)
```

#### sum

```
select sum(Ccredit) from SC, Course where Sno='201215122' and SC.Cno=Course.Cno;
```

```
mysql&gt; select sum(Ccredit) from SC, Course where Sno='201215122' and SC.Cno=Course.Cno;
+--------------+
| sum(Ccredit) |
+--------------+
|            6 |
+--------------+
1 row in set (0.00 sec)
```

### GROUP BY

group by 子句将查询结果按某一列或多列的值分组，值相等的为一组。

```
select Cno, Count(Sno) from SC group by Cno;
```

```
mysql&gt; select Cno, Count(Sno) from SC group by Cno;
+-----+------------+
| Cno | Count(Sno) |
+-----+------------+
| 1   |          1 |
| 2   |          2 |
| 3   |          2 |
+-----+------------+
3 rows in set (0.00 sec)
```

 分组后，可使用 having 指定筛选条件（比如查询每个选课学生选课的平均成绩）。

```
select Sname, avg(Grade) from Student, SC where SC.Sno=Student.Sno group by SC.Sno;
```

```
mysql&gt; select Sname, avg(Grade) from Student, SC where SC.Sno=Student.Sno group by SC.Sno;
+--------+------------+
| Sname  | avg(Grade) |
+--------+------------+
| 李勇   |    88.3333 |
| 刘晨   |    85.0000 |
+--------+------------+
2 rows in set (0.00 sec)
```

查询平均成绩大于 85 的学生。

```
select Sno, avg(Grade) from SC group by Sno having avg(Grade)&gt;85;
```

```
mysql&gt; select Sno, avg(Grade) from SC group by Sno having avg(Grade)&gt;85;
+-----------+------------+
| Sno       | avg(Grade) |
+-----------+------------+
| 201215121 |    88.3333 |
+-----------+------------+
1 row in set (0.00 sec)
```

### 连接查询

既然叫连接查询，那么也就是属于多表查询的范畴了。

```
select Student.*, SC.* from Student, SC where Student.Sno=SC.Sno;
```

```
mysql&gt; select Student.*, SC.* from Student, SC where Student.Sno=SC.Sno;
+-----------+--------+------+------+-------+-----------+-----+-------+
| Sno       | Sname  | Ssex | Sage | Sdept | Sno       | Cno | Grade |
+-----------+--------+------+------+-------+-----------+-----+-------+
| 201215121 | 李勇   | 男   |   20 | CS    | 201215121 | 1   |    92 |
| 201215121 | 李勇   | 男   |   20 | CS    | 201215121 | 2   |    85 |
| 201215121 | 李勇   | 男   |   20 | CS    | 201215121 | 3   |    88 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 201215122 | 2   |    90 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 201215122 | 3   |    80 |
+-----------+--------+------+------+-------+-----------+-----+-------+
5 rows in set (0.00 sec)
```

#### 交叉连接

如果不添加限制条件的话，本质上就是两个表的笛卡尔积，产生的表比较大，慎用。 

```
select Student.*, SC.* from Student, SC;
```

```
mysql&gt; select Student.*, SC.* from Student, SC;
+-----------+--------+------+------+-------+-----------+-----+-------+
| Sno       | Sname  | Ssex | Sage | Sdept | Sno       | Cno | Grade |
+-----------+--------+------+------+-------+-----------+-----+-------+
| 201215121 | 李勇   | 男   |   20 | CS    | 201215121 | 1   |    92 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 201215121 | 1   |    92 |
| 201215123 | 王敏   | 女   |   18 | MA    | 201215121 | 1   |    92 |
| 201215125 | 张立   | 男   |   19 | IS    | 201215121 | 1   |    92 |
| 201215121 | 李勇   | 男   |   20 | CS    | 201215121 | 2   |    85 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 201215121 | 2   |    85 |
| 201215123 | 王敏   | 女   |   18 | MA    | 201215121 | 2   |    85 |
| 201215125 | 张立   | 男   |   19 | IS    | 201215121 | 2   |    85 |
| 201215121 | 李勇   | 男   |   20 | CS    | 201215121 | 3   |    88 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 201215121 | 3   |    88 |
| 201215123 | 王敏   | 女   |   18 | MA    | 201215121 | 3   |    88 |
| 201215125 | 张立   | 男   |   19 | IS    | 201215121 | 3   |    88 |
| 201215121 | 李勇   | 男   |   20 | CS    | 201215122 | 2   |    90 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 201215122 | 2   |    90 |
| 201215123 | 王敏   | 女   |   18 | MA    | 201215122 | 2   |    90 |
| 201215125 | 张立   | 男   |   19 | IS    | 201215122 | 2   |    90 |
| 201215121 | 李勇   | 男   |   20 | CS    | 201215122 | 3   |    80 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 201215122 | 3   |    80 |
| 201215123 | 王敏   | 女   |   18 | MA    | 201215122 | 3   |    80 |
| 201215125 | 张立   | 男   |   19 | IS    | 201215122 | 3   |    80 |
+-----------+--------+------+------+-------+-----------+-----+-------+
20 rows in set (0.00 sec)
```

#### 等值连接

```
select Student.Sno, Sname, Ssex, Sage, Sdept, Cno, Grade from Student, SC where Student.Sno=SC.Sno;
```

```
mysql&gt; select Student.Sno, Sname, Ssex, Sage, Sdept, Cno, Grade from Student, SC where Student.Sno=SC.Sno;
+-----------+--------+------+------+-------+-----+-------+
| Sno       | Sname  | Ssex | Sage | Sdept | Cno | Grade |
+-----------+--------+------+------+-------+-----+-------+
| 201215121 | 李勇   | 男   |   20 | CS    | 1   |    92 |
| 201215121 | 李勇   | 男   |   20 | CS    | 2   |    85 |
| 201215121 | 李勇   | 男   |   20 | CS    | 3   |    88 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 2   |    90 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 3   |    80 |
+-----------+--------+------+------+-------+-----+-------+
5 rows in set (0.00 sec)
```

#### 内连接

内连接（INNER JOIN）根据连接谓词结合两个表（table1 和 table2）的列值来创建一个新的结果表。查询会把 table1 中的每一行与 table2 中的每一行进行比较，找到所有满足连接谓词的行的匹配对。

上面的例子用 using 关键字也是可以的哟，usring(Sno) 表示使用两个表的相同字段 Sno 作为连接条件。

```
select * from admin inner join user on admin.name = user.name
类似于：
select * from admin inner join user on using(name)
```

```
select Student.Sno, Sname, Ssex, Sage, Sdept, Cno, Grade from Student inner join SC using(Sno);

```

```
mysql&gt; select Student.Sno, Sname, Ssex, Sage, Sdept, Cno, Grade from Student inner join SC using(Sno);
+-----------+--------+------+------+-------+-----+-------+
| Sno       | Sname  | Ssex | Sage | Sdept | Cno | Grade |
+-----------+--------+------+------+-------+-----+-------+
| 201215121 | 李勇   | 男   |   20 | CS    | 1   |    92 |
| 201215121 | 李勇   | 男   |   20 | CS    | 2   |    85 |
| 201215121 | 李勇   | 男   |   20 | CS    | 3   |    88 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 2   |    90 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 3   |    80 |
+-----------+--------+------+------+-------+-----+-------+
5 rows in set (0.00 sec)
```

#### 自然连接

我们可以看到，上面的连接有重复的列。若等值连接把目标列中重复的属性列去掉则为自然连接。

**内连接 **与自然连接比较像，只不过自然连接只考虑同名属性，内连接则不要求必须为同名属性列，用 on 关键字选择共同属性（如等值连接）。

```
select Student.*, SC.* from Student natural join SC;
```

```
mysql&gt; select Student.*, SC.* from Student natural join SC;
+-----------+--------+------+------+-------+-----+-------+
| Sno       | Sname  | Ssex | Sage | Sdept | Cno | Grade |
+-----------+--------+------+------+-------+-----+-------+
| 201215121 | 李勇   | 男   |   20 | CS    | 1   |    92 |
| 201215121 | 李勇   | 男   |   20 | CS    | 2   |    85 |
| 201215121 | 李勇   | 男   |   20 | CS    | 3   |    88 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 2   |    90 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 3   |    80 |
+-----------+--------+------+------+-------+-----+-------+
5 rows in set (0.00 sec)
```

查询选修 2 号课程且成绩  85 分以上的学生的学号和姓名。 

```
select Student.Sno, Sname from Student, SC where Student.Sno=SC.Sno and SC.Cno='2' and SC.Grade&gt;85;
```

```
mysql&gt; select Student.Sno, Sname from Student, SC where Student.Sno=SC.Sno and SC.Cno='2' and SC.Grade&gt;85;
+-----------+--------+
| Sno       | Sname  |
+-----------+--------+
| 201215122 | 刘晨   |
+-----------+--------+
1 row in set (0.00 sec)
```

#### 自身连接

查询先行课的先行课。

```
select first.Cno, second.Cpno from Course first, Course second where first.Cpno=second.Cno;
```

```
mysql&gt; select first.Cno, second.Cpno from Course first, Course second where first.Cpno=second.Cno;
+-----+------+
| Cno | Cpno |
+-----+------+
| 3   | 5    |
| 1   | 7    |
| 4   | NULL |
| 7   | NULL |
| 5   | 6    |
+-----+------+
5 rows in set (0.00 sec)
```

#### 外连接

和普通连接相比，都好变成了 left outer join （当然也有 right outer join），where 变成了 on。

**左外连接**：列出左边关系中所有的元组；**右外连接**：列出右边关系中所有的元组。

```
select Student.Sno, Sname, Ssex, Sage, Sdept, Cno, Grade from Student left outer join SC on Student.Sno=SC.Sno;
```

```
mysql&gt; select Student.Sno, Sname, Ssex, Sage, Sdept, Cno, Grade from Student left outer join SC on Student.Sno=SC.Sno;
+-----------+--------+------+------+-------+------+-------+
| Sno       | Sname  | Ssex | Sage | Sdept | Cno  | Grade |
+-----------+--------+------+------+-------+------+-------+
| 201215121 | 李勇   | 男   |   20 | CS    | 1    |    92 |
| 201215121 | 李勇   | 男   |   20 | CS    | 2    |    85 |
| 201215121 | 李勇   | 男   |   20 | CS    | 3    |    88 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 2    |    90 |
| 201215122 | 刘晨   | 女   |   19 | CS    | 3    |    80 |
| 201215123 | 王敏   | 女   |   18 | MA    | NULL |  NULL |
| 201215125 | 张立   | 男   |   19 | IS    | NULL |  NULL |
+-----------+--------+------+------+-------+------+-------+
7 rows in set (0.00 sec)
```

#### 多表连接

查询每个学生的学号，姓名，选修课程和成绩。where 第一个条件判断学生选修了哪些课程，第二个条件则是在第一个条件的基础上，查询选修课程的名称。

```
select Student.Sno, Sname, Cname, Grade from Student, SC, Course where Student.Sno=SC.Sno and SC.Cno=Course.Cno;
```

```
mysql&gt; select Student.Sno, Sname, Cname, Grade from Student, SC, Course where Student.Sno=SC.Sno and SC.Cno=Course.Cno;
+-----------+--------+--------------+-------+
| Sno       | Sname  | Cname        | Grade |
+-----------+--------+--------------+-------+
| 201215121 | 李勇   | 数据库       |    92 |
| 201215121 | 李勇   | 数学         |    85 |
| 201215121 | 李勇   | 信息系统     |    88 |
| 201215122 | 刘晨   | 数学         |    90 |
| 201215122 | 刘晨   | 信息系统     |    80 |
+-----------+--------+--------------+-------+
5 rows in set (0.00 sec)
```

### 嵌套查询

查询选修 2 号课程的学生。

```
select Sname from Student where Sno in 
    (select Sno from SC where Cno='2');
```

```
mysql&gt; select Sname from Student where Sno in
    -&gt;     (select Sno from SC where Cno='2');
+--------+
| Sname  |
+--------+
| 李勇   |
| 刘晨   |
+--------+
2 rows in set (0.00 sec)
```

有些嵌套查询可以写成表连接查询的形式替代，有些则是不能替代的。

```
select Sname from Student, SC where Student.Sno=SC.Sno and SC.Cno='2';
```

```
mysql&gt; select Sname from Student, SC where Student.Sno=SC.Sno and SC.Cno='2';
+--------+
| Sname  |
+--------+
| 李勇   |
| 刘晨   |
+--------+
2 rows in set (0.00 sec)
```

#### 带有 in 的子查询

查询选修了课程名为 “信息系统” 的学生学号和姓名。

```
select Sno, Sname from Student where Sno in 
    (select Sno from SC where Cno in 
        (select Cno from Course where Cname='信息系统'));
```

```
mysql&gt; select Sno, Sname from Student where Sno in
    -&gt;     (select Sno from SC where Cno in
    -&gt;         (select Cno from Course where Cname='信息系统'));
+-----------+--------+
| Sno       | Sname  |
+-----------+--------+
| 201215121 | 李勇   |
| 201215122 | 刘晨   |
+-----------+--------+
2 rows in set (0.00 sec)
```

#### 带有比较运算的子查询

**不相关子查询**：子查询的查询条件不依赖于父查询。

```
select Sno, Sname, Sdept from Student where Sdept=
    (select Sdept from Student where Sname='刘晨');
```

```
mysql&gt; select Sno, Sname, Sdept from Student where Sdept=
    -&gt;     (select Sdept from Student where Sname='刘晨');
+-----------+--------+-------+
| Sno       | Sname  | Sdept |
+-----------+--------+-------+
| 201215121 | 李勇   | CS    |
| 201215122 | 刘晨   | CS    |
+-----------+--------+-------+
2 rows in set (0.00 sec)
```

**相关子查询**：子查询的查询条件依赖于父查询。

```
select Sno, Cno from SC x where Grade&gt;=
    (select avg(Grade) from SC y where x.Sno=y.Sno);
```

```
mysql&gt; select Sno, Cno from SC x where Grade&gt;=
    -&gt;     (select avg(Grade) from SC y where x.Sno=y.Sno);
+-----------+-----+
| Sno       | Cno |
+-----------+-----+
| 201215121 | 1   |
| 201215122 | 2   |
+-----------+-----+
2 rows in set (0.00 sec)
```

#### 带有 ANY 或 ALL 的子查询

```
select Sname, Sage from Student where Sage&lt;any(
    select Sage from Student where Sdept='CS')
    and Sdept!='CS';
```

```
mysql&gt; select Sname, Sage from Student where Sage&lt;any
    -&gt;     select Sage from Student where Sdept='CS')
    -&gt;     and Sdept!='CS';
+--------+------+
| Sname  | Sage |
+--------+------+
| 王敏   |   18 |
| 张立   |   19 |
+--------+------+
2 rows in set (0.00 sec)

```

 上面查询也可以用聚合函数实现，毕竟 &lt; any(result) 等价于 &lt; max(result)；&lt; all(result) 等价于 &lt; min(result)。更多等价转换关系请参考下表：

<img alt="" height="237" src="https://img-blog.csdnimg.cn/56a336c26a62416fb59cc505878d4efb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATG9vb29raW5n,size_20,color_FFFFFF,t_70,g_se,x_16" width="1079">

```
select Sname, Sage from Student where Sage&lt;(
    select max(Sage) from Student where Sdept='CS')
    and Sdept!='CS';
```

```
mysql&gt; select Sname, Sage from Student where Sage&lt;(
    -&gt;     select max(Sage) from Student where Sdept='CS')
    -&gt;     and Sdept!='CS';
+--------+------+
| Sname  | Sage |
+--------+------+
| 王敏   |   18 |
| 张立   |   19 |
+--------+------+
2 rows in set (0.00 sec)
```

#### 带有 EXISTS的子查询

```
select Sname from Student where exists
    (select * from SC where Sno=Student.Sno and Cno='1');
```

```
mysql&gt; select Sname from Student where exists
    -&gt;     (select * from SC where Sno=Student.Sno and Cno='1');
+--------+
| Sname  |
+--------+
| 李勇   |
+--------+
1 row in set (0.00 sec)
```

 当然，这块直接用表连接查询也是可以实现的：

```
select Sname from Student, SC where Student.Sno=SC.Sno and Cno='1';
```

```
mysql&gt; select Sname from Student, SC where Student.Sno=SC.Sno and Cno='1';
+--------+
| Sname  |
+--------+
| 李勇   |
+--------+
1 row in set (0.00 sec)
```

### 集合查询

主要是 UNION、INTERSECT 和 EXCEPT。**注意**：参加集合操作的查询结果列数必须相同，对应项的数据类型也必须相同。

#### UNION

```
select Sno from SC where Cno='1' union
select Sno from SC where Cno='2';
```

```
mysql&gt; select Sno from SC where Cno='1' union
    -&gt; select Sno from SC where Cno='2';
+-----------+
| Sno       |
+-----------+
| 201215121 |
| 201215122 |
+-----------+
2 rows in set (0.00 sec)
```

#### INTERSECT

mysql 好像不支持。

```
select * from Student where Sdept='CS' INTERSECT
select * from Student where Sage&lt;=19;
```

#### EXCEPT

mysql 好像也不支持。不过这两个基本上都可以通过表连接或者子查询来进行等价替换。

```
select * from Student where Sdept='CS' EXCEPT
select * from Student where Sage&lt;=19;
```
