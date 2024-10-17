
--- 
title:  织梦dedecms标签 limit=‘0,5‘的含义 
tags: []
categories: [] 

---
limit=‘0,5’ 这就是dedecms拼接sql语句的条件之一，与sql语句里的limit功能一样。 limit是含义就是 从 第1条（在计算机语zhi言中0代表第一条）开始，查询5条的数据，那下面的limit='5,10’就是从第6条开始查询10条。只会输出10条，不会输出所有的。

limit=‘0,1’

这个表示从第一篇文章开始，取1篇文章。

limit=‘2,4’

这个表示从第三篇文章开始，取4篇文章。

这个方法与row是类似的，row=‘5’，就告诉dedecms从第一条开始取5条数据，相当于limit=“0,5”。 limit还有一个写法是：limit=‘5’，相当于limit=“0,5”。
