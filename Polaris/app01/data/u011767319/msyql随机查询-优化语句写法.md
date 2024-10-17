
--- 
title:  msyql随机查询-优化语句写法 
tags: []
categories: [] 

---
### 表数据

>  
 tm_timeline 40多w数据 <img src="https://img-blog.csdnimg.cn/6e9706f334db452abdd29ab409c2d128.png" alt="在这里插入图片描述"> 


### 原始查询

```
SELECT * FROM tm_timeline
ORDER BY RAND()
LIMIT 5

```

运行sql<img src="https://img-blog.csdnimg.cn/d174c717e0a84a57a8a631d7dfdeaba6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 简单优化

```
SELECT * FROM tm_timeline t1 join  (SELECT id FROM tm_timeline ORDER BY rand() LIMIT 5) t2 on  t1.id=t2.id

```

运行sql

<img src="https://img-blog.csdnimg.cn/0bab7e2296e040059b10d0acdf60a84a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 谷歌给的方案

>  
 id 必须是连续自增了，雪花id无效 


```
SELECT * FROM tm_timeline AS t1 JOIN (SELECT ROUND(RAND() * (SELECT MAX(id) FROM tm_timeline)) AS id) AS t2
WHERE t1.id &gt;= t2.id
ORDER BY t1.id ASC LIMIT 5;

```

运行sql <img src="https://img-blog.csdnimg.cn/5790e1c9ad8c447a86a2dcb833779ff8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 另外一种写法sql

>  
 和谷歌的效率差不多 id 必须是连续自增了，雪花id无效 


```
SELECT * FROM tm_timeline AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM tm_timeline)-(SELECT MIN(id) FROM tm_timeline))+(SELECT MIN(id) FROM tm_timeline)) AS id) AS t2
WHERE t1.id &gt;= t2.id
ORDER BY t1.id LIMIT 5;

```

运行sql <img src="https://img-blog.csdnimg.cn/10db2473aa15497f8271ccd905576e92.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
