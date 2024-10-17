
--- 
title:  【hive sql】ROW_NUMBER() 
tags: []
categories: [] 

---
有一张表t1，表中有字段day和num，要取出每天num排名前10的所有数据

```

SELECT day, num
FROM (
  SELECT day, num,
         ROW_NUMBER() OVER (PARTITION BY day ORDER BY num DESC) as rank
  FROM t1
) t
WHERE rank &lt;= 10;


```

这个查询首先使用窗口函数 ROW_NUMBER() 对每天的数据进行排序，

并为每一行分配一个排名。

然后，在外部查询中，我们选择排名不超过 10 的记录。
