
--- 
title:  mysql常用函数 
tags: []
categories: [] 

---1. substr(): 截取字符串 SUBSTR (str, pos, len) str为列名/字符串； pos为起始位置；mysql中的起始位置pos是从1开始的；如果为正数，就表示从正数的位置往下截取字符串（起始坐标从1开始），反之如果起始位置pos为负数，那么 表示就从倒数第几个开始截取； len为截取字符个数/长度。 如： select substr(createTime, 1, 10) from orders;1. round(column, number): 四舍五入函数 column：被处理的列或者数 number：保留小数的位数 select round(sum(realTotalMoney), 2) from orders;1. in() exists() select * from A where id in(select id from B) select a.* from A a where exists(select 1 from B b where a.id=b.id) in()适合B表比A表数据小的情况: in在查询的时候，首先查询子查询的表，然后将内表和外表做一个笛卡尔积，然后按照条件进行筛选。所以相对内表比较小的时候，in的速度较快 exists()适合B表比A表数据大的情况: 指定一个子查询，检测行的存在。遍历循环外表，然后看外表中的记录有没有和内表的数据一样的。匹配上就将结果放入结果集中。 当A表数据与B表数据一样大时,in与exists效率差不多,可任选一个使用.