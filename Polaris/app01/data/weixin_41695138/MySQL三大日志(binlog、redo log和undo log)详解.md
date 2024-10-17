
--- 
title:  MySQL三大日志(binlog、redo log和undo log)详解 
tags: []
categories: [] 

---
在此记录一下，方便后期的复习查看 参考： 

binlog（归档日志） redo log（重做日志）事务日志 undo log（回滚日志） MySQL InnoDB 引擎使用 redo log(重做日志) 保证事务的持久性，使用 undo log(回滚日志) 来保证事务的原子性。 MySQL数据库的数据备份、主备、主主、主从都离不开binlog，需要依靠binlog来同步数据，保证数据一致性
