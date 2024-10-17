
--- 
title:  mysql查表里面的字段 
tags: []
categories: [] 

---
mysql查表里面的字段的方法：使用“SHOW FROM”语句配合FULL关键字来查询，语法“SHOW FULL COLUMNS FROM table_name”，可以显示指定数据表的所有字段信息。

mysql查表里面的字段的方法第一种: 表中所有字段信息

select COLUMN_NAME,COLUMN_COMMENT from information_schema.columns where  table_name='表名' mysql查表里面的字段的方法第二种: 查询指定字段信息

select COLUMN_NAME,COLUMN_COMMENT from information_schema.columns WHERE column_name='字段名' and table_name = '表名' mysql查表里面的字段的方法第三种: 查询表信息与字段信息

SELECT * FROM information_schema.columns WHERE COLUMN_NAME='字段' and table_name = '表名'; SELECT * FROM information_schema.columns WHERE table_name = '表名';

<img alt="" height="617" src="https://img-blog.csdnimg.cn/1b807ccd4c67421fa9c7d6883230b164.png" width="1000">

 
