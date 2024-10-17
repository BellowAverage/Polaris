
--- 
title:  ORACLE 重构ID列 
tags: []
categories: [] 

---
今天想重构一下一个业务表ID。

比如说：我们有个表的数据ID为;1000,1001,1002……2000,我想把这个ID刷到从1开始。咋弄？

昨天弄了一个小时，发现oracle有个序列。（之前mysql的，有自增主键，不太清除oracle的逻辑）

序列的构建方式： `CREATE SEQUENCE FUNC increment by 1 start with 15232 minvalue 1`

可以构造一个起点为15231的序列。 当使用的时候，可以直接调用FUNC方法（你也可以起别的名字，我只是示范）的nextval方法，就可以构造一个序列。

于是，你想要刷新ID，首先delete掉这个方法,重新构造一个一模一样但是起点为1的方法，然后updateID这个字段即可。

```
update t1 set id = func.nextval

```

即可重构索引。（不过数据量大会锁表）

dbeaver可以直接操作： <img src="https://img-blog.csdnimg.cn/445d3cbbb9374a48ae0080e38b86daed.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_16,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">有这么几个参数： <img src="https://img-blog.csdnimg.cn/618d56667a224600ae0dd8d7a470a6d9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 循环的意思是：如果到最大值，继续到最小值重新计数。 序列一旦构建不可修改，可以drop后重新create。

其他的就不清楚了。
