
--- 
title:  常见SQL错误用法案例和总结 
tags: []
categories: [] 

---
#### 1. LIMIT 语句

分页查询是最常用的场景之一，但也通常也是最容易出问题的地方。比如对于下面简单的语句，一般DBA想到的办法是在type, name, create_time字段上加组合索引。这样条件排序都能有效的利用到索引，性能迅速提升。

```
SELECT * 
FROM   operation 
WHERE  type = 'SQLStats' 
       AND name = 'SlowLog' 
ORDER  BY create_time 
LIMIT  1000, 10; 

```

好吧，可能90%以上的DBA解决该问题就到此为止。但当 LIMIT 子句变成 “`LIMIT 1000000,10`” 时，程序员仍然会抱怨：我只取10条记录为什么还是慢？

要知道数据库也并不知道第1000000条记录从什么地方开始，即使有索引也需要从头计算一次。出现这种性能问题，多数情形下是程序员偷懒了。在前端数据浏览翻页，或者大数据分批导出等场景下，是可以将上一页的最大值当成参数作为查询条件的。SQL重新设计如下：

```
SELECT   * 
FROM     operation 
WHERE    type = 'SQLStats' 
AND      name = 'SlowLog' 
AND      create_time &gt; '2017-03-16 14:00:00' 
ORDER BY create_time limit 10;

```

在新设计下查询时间基本固定，不会随着数据量的增长而发生变化。

#### 2. 隐式转换

SQL语句中查询变量和字段定义类型不匹配是另一个常见的错误。比如下面的语句：

```
mysql&gt; explain extended SELECT * 
     &gt; FROM   my_balance b 
     &gt; WHERE  b.bpn = 14000000123 
     &gt;       AND b.isverified IS NULL ;
mysql&gt; show warnings;
| Warning | 1739 | Cannot use ref access on index 'bpn' due to type or collation conversion on field 'bpn'

```

其中字段bpn的定义为varchar(20)，MySQL的策略是将字符串转换为数字之后再比较。函数作用于表字段，索引失效。

上述情况可能是应用程序框架自动填入的参数，而不是程序员的原意。现在应用框架很多很繁杂，使用方便的同时也小心它可能给自己挖坑。

#### 3. 关联更新、删除

虽然MySQL5.6引入了物化特性，但需要特别注意它目前仅仅针对查询语句的优化。对于更新或删除需要手工重写成JOIN。

比如下面UPDATE语句，MySQL实际执行的是循环/嵌套子查询（DEPENDENT SUBQUERY)，其执行时间可想而知。

```
UPDATE operation o 
SET    status = 'applying' 
WHERE  o.id IN (SELECT id 
                FROM   (SELECT o.id, 
                               o.status 
                        FROM   operation o 
                        WHERE  o.group = 123 
                               AND o.status NOT IN ( 'done' ) 
                        ORDER  BY o.parent, 
                                  o.id 
                        LIMIT  1) t); 

```

执行计划：

```
+----+--------------------+-------+-------+---------------+---------+---------+-------+------+-----------------------------------------------------+
| id | select_type        | table | type  | possible_keys | key     | key_len | ref   | rows | Extra                                               |
+----+--------------------+-------+-------+---------------+---------+---------+-------+------+-----------------------------------------------------+
| 1  | PRIMARY            | o     | index |               | PRIMARY | 8       |       | 24   | Using where; Using temporary                        |
| 2  | DEPENDENT SUBQUERY |       |       |               |         |         |       |      | Impossible WHERE noticed after reading const tables |
| 3  | DERIVED            | o     | ref   | idx_2,idx_5   | idx_5   | 8       | const | 1    | Using where; Using filesort                         |
+----+--------------------+-------+-------+---------------+---------+---------+-------+------+-----------------------------------------------------+

```

重写为JOIN之后，子查询的选择模式从DEPENDENT SUBQUERY变成DERIVED,执行速度大大加快，从7秒降低到2毫秒。

```
UPDATE operation o 
       JOIN  (SELECT o.id, 
                            o.status 
                     FROM   operation o 
                     WHERE  o.group = 123 
                            AND o.status NOT IN ( 'done' ) 
                     ORDER  BY o.parent, 
      
```
