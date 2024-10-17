
--- 
title:  MySQL删除全局唯一索引unique 
tags: []
categories: [] 

---
删除索引（通用）
- alter table 表名 drop index 索引名；- drop index 索引名 on 表名
查看索引
- show keys from 表名- show index from 表名;- desc 表名；
详细步骤： 1、看一下群描述，哪些字段加了唯一索引：

```
desc table_name;

```

2、查看一下索引名：

```
show index from table_name;

```

3、删除指定索引名：

```
alter table table_name drop index ix_table_name_colume_name;

```

4、再查看表描述，发现字段名已删除：

```
desc table_name;

```
