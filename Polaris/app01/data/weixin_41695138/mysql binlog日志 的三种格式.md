
--- 
title:  mysql binlog日志 的三种格式 
tags: []
categories: [] 

---
转载的文章： mysql binlog日志 的三种格式 ： statement row mixed
1. binlog=statement格式：当binlog=statement时，binlog记录的是SQL本身的语句1. binlog=row格式： 如果我们把binlog设置为row格式的时候，binlog记录的不是sql原语句，而是替换成了两个event：Table_map和Delete_rows1. binlog=mixed格式：如果MySQL认为会引起主备不一致，它就会使用row格式记录到binlog；如果MySQL认为不会引起主备不一致，它就会使用statement格式记录到binlog。