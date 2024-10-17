
--- 
title:  [spark] SaveMode 
tags: []
categories: [] 

---
https://spark.apache.org/docs/latest/api/java/index.html?org/apache/spark/sql/SaveMode.html

<img src="https://img-blog.csdnimg.cn/direct/7a32c9b982964a99a9669845ca211a2a.png" alt="在这里插入图片描述">

**Overwrite** 覆盖模式是指将DataFrame保存到数据源时，如果数据/表已经存在，则现有数据将被DataFrame的内容覆盖。

注意: Overwrite 模式会覆盖已存在的表并删除表中的数据，然后写入新的数据。如果昨天存入的数据也在同一表中，它们将被新的数据替代，整个表的内容将被更新。

如果您希望在不删除原有数据的情况下追加新的数据，可以选择使用 Append 模式。这样，新的数据将会在表的末尾追加，而不会影响已有的数据。

### 是否会自动创建Mysql表
-  默认为SaveMode.ErrorIfExists模式，该模式下，如果数据库中已经存在该表，则会直接报异常 -  SaveMode.Append 如果表已经存在，则追加在该表中；若该表不存在，则会先创建表，再插入数据； -  SaveMode.Overwrite 重写模式，若表不存在，则创建表, 其实质是先将已有的表及其数据全都删除，再重新创建该表，最后插入新的数据； -  SaveMode.Ignore 若表不存在，则创建表，并存入数据；在表存在的情况下，直接跳过数据的存储，不会报错。 