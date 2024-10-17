
--- 
title:  Mysql报错1194 - Table ‘‘ is marked as crashed and should be repaired的解决办法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解：Mysql报错1194 - Table ‘’ is marked as crashed and should be repaired的解决办法。 日期：2023年8月9日 作者：任聪聪 


### 具体现象

说明：执行sql语句查询或者检索相关数据时会出现如下报错内容：

```
1194 - Table 'xxxx你的表名' is marked as crashed and should be repaired

```

### 主要原因及解决办法

造成这个报错的主要原因可能是，服务器之前有过一次强制重启，又或者是mysql突然被停止，但是用户的数据有新增，出现了表的数据结构损坏导致的。

网络上很多人说要重启mysql就好了，但实际上并不是姐姐这个报错的更本方法。

#### 解决办法

前置准备：将报错的表进行一个备份，备份完毕后执行下面的修复命令：

```
REPAIR TABLE  your_table_name

```

执行完毕后，即可解决这个报错问题。
