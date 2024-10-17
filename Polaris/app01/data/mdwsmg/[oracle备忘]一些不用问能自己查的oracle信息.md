
--- 
title:  [oracle备忘]一些不用问能自己查的oracle信息 
tags: []
categories: [] 

---


#### oracle基础查询
- - - - - - - 


偶尔需要确认表、用户是否存在，需要查询确认数据库版本。这些东西问人不一定谁都有好脾气回你，且，确实很基础。 人麻了，我确实很菜嘛。

>  
 基本是大写，记得使用upper函数 


## 1、查询当前数据库版本

oracle查询数据库版本,下列三个语句都可以

```
select banner from sys.v_$version;

```

```
select * from v$version;

```

```
select * from product_component_version;

```

## 2、查询用户是否存在

oracle查询用户是否存在,登录任意用户可在all_users表可以查看所有用户。

```
select * from all_users;

```

oracle默认密码过期时间为180天，有时候会遇到用户密码过期现象。 可以查询dba_users表查询用户信息、用户状态。

```
select username,account_status from dba_users;

```

## 3、查询表是否存在

oracle查询表是否存在，查询当前登录用户中的所有表中是否存在该表。注意表名区分大小写，如果参数不限制，那这里就必须要加上upper函数 。

```
select * from user_tables where table_name =upper('表名');

```

all_tables表中也可以查询其他用户的表信息，owner字段指定用户名

```
select * from all_tables where owner = 'SYS';

```

## 4、查询表空间是否存在

oracle查询表空间是否存在，查询表空间详细信息。 使用以下语句查询所有表空间信息。

```
select tablespace_name from sys.dba_tablespaces;

```

## 5、查询索引是否存在

oracle查询索引是否存在，查询表空间详细信息

```
select * from user_indexes where table_name=upper('表名'); 

```

查询索引的被索引字段，user_ind_columns表更直观

```
select * from user_ind_columns where index_name=('index_name'); 

```

## 6、查询序列是否存在

oracle查询序列是否存在，使用

```
select * from user_sequences  where sequence_name = '';

```

## 7、查询存储过程是否存在

```
SELECT * FROM ALL_PROCEDURES WHERE OBJECT_NAME = upper('YOUR_PROCEDURE');

SELECT DISTINCT NAME FROM USER_SOURCE WHERE TYPE = 'PROCEDURE' and name = upper('YOUR_PROCEDURE');

```
