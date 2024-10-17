
--- 
title:  大数据培训课程：Hive配置总结 
tags: []
categories: [] 

---
# ------------------配置相关--------------------------

0. 配置存储

在$HOME目录下的.hiverc文件中

1. 在提示符中显示数据库名

set hive.cli.print.current.db=true;

 

2. 优先使用本地模式执行

set hive.exec.mode.loacl.auto=true;

 

3. 打印列名

set hive.cli.print.header=true;

 

4. （非）严格模式

set hive.mapred.mode=strict;

set hive.mapred.mode=nonstrict;

 

5. 开启动态分区

set hive.exec.dynamic.partition=true;

 

# --------------动态分区调整--------------------

6.-- 设置动态分区模式

set hive.exec.dynamic.partition.mode=strict

 

7.-- 设置总的动态分区个数

set hive.exec.max.dynamic.partitions=300000

 

8.-- 设置每个节点上动态分区个数

set hive.exec.max.dynamic.partitions.pernode=10000

 

9. 设置全局可以产生文件的个数

set hive.exec.max.created.files=100000;

 

10.开启map site join

set hive.auto.convert.join=true;

 

11.设置小表大小（字节）

set hive.mapjoin.smalltable.filesize=25000000

 

12.强制将数据按照桶结构定义来插入数据

set hive.enforce.bucketing=true

 

13.limit优化

-- 启用limit优化

set hive.limit.optimize.enable=true;

-- 限制从最大多少条数据中进行limit

set hive.limit.row.max.size=10000;

-- 限制最多遍历的文件个数

set hive.limit.optimize.limit.file=10;

 

14. 压缩

--开启中间压缩（即map到reduce之间的数据压缩）

set hive.exec.compress.intermediate=true;

-- 开启hadoop中间压缩（即map到reduce之间的数据压缩）

set mapred.compress.map.output=true;

-- 开启hive最终压缩（即reduce输出的数据压缩）

set hive.exec.compress.output=true;

 

4. 数据仓库的存储地址

      hive-default.xml中，不一般不同

      &lt;property&gt;

             &lt;name&gt;hive.metastore.warehouse.dir&lt;/name&gt;

             &lt;value&gt;/user/hive/warehouse&lt;/value&gt;

             &lt;description&gt;location of default database for the warehouse&lt;/description&gt;

      &lt;/property&gt;
