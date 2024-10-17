
--- 
title:  2PC和3PC Seata 的at模式 
tags: []
categories: [] 

---
### 2PC和3PC Seata 的at模式

参考 

### 2PC

准备提交阶段-提交阶段

### 3PC

准备提交阶段-预提交阶段-提交阶段，3pc相对于2pc,多加入预提交阶段，和超时

### Seata 的at模式

Seata AT分为两阶段，主要逻辑全部在第一阶段，第二阶段主要做回滚或日志清理的工作。 会在每个数据库中维护undo_log表，@GlobalTransactional 注解表示开启分布式事务 at模式是增强版的2pc，第一阶段业务数据和回滚日志记录在同一个本地事务中提交,提交之后就会释放资源
