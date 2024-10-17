
--- 
title:  探索ClickHouse——使用MaterializedView存储kafka传递的数据 
tags: []
categories: [] 

---


#### 大纲
- - - 


## 创建表

该表结构直接借用了中的表结构。

```
CREATE TABLE materialized_uk_price_paid_from_kafka ( price UInt32, date Date, postcode1 LowCardinality(String), postcode2 LowCardinality(String), type Enum8('terraced' = 1, 'semi-detached' = 2, 'detached' = 3, 'flat' = 4, 'other' = 0), is_new UInt8, duration Enum8('freehold' = 1, 'leasehold' = 2, 'unknown' = 0), addr1 String, addr2 String, street LowCardinality(String), locality LowCardinality(String), town LowCardinality(String), district LowCardinality(String), county LowCardinality(String) ) ENGINE = MergeTree ORDER BY (postcode1, postcode2, addr1, addr2);

```

>  
 CREATE TABLE materialized_uk_price_paid_from_kafka ( `price` UInt32, `date` Date, `postcode1` LowCardinality(String), `postcode2` LowCardinality(String), `type` Enum8(‘terraced’ = 1, ‘semi-detached’ = 2, ‘detached’ = 3, ‘flat’ = 4, ‘other’ = 0), `is_new` UInt8, `duration` Enum8(‘freehold’ = 1, ‘leasehold’ = 2, ‘unknown’ = 0), `addr1` String, `addr2` String, `street` LowCardinality(String), `locality` LowCardinality(String), `town` LowCardinality(String), `district` LowCardinality(String), `county` LowCardinality(String) ) ENGINE = MergeTree ORDER BY (postcode1, postcode2, addr1, addr2) Query id: 55b16049-a865-4d54-9333-d661c6280a09 Ok. 0 rows in set. Elapsed: 0.005 sec. 


## 创建MaterializedView

```
CREATE MATERIALIZED VIEW uk_price_paid_from_kafka_consumer_view TO materialized_uk_price_paid_from_kafka AS SELECT splitByChar(' ', postcode) AS p, toUInt32(price_string) AS price, parseDateTimeBestEffortUS(time) AS date, p[1] AS postcode1, p[2] AS postcode2, transform(a, ['T', 'S', 'D', 'F', 'O'], ['terraced', 'semi-detached', 'detached', 'flat', 'other']) AS type, b = 'Y' AS is_new, transform(c, ['F', 'L', 'U'], ['freehold', 'leasehold', 'unknown']) AS duration, addr1, addr2, street, locality, town, district, county FROM uk_price_paid_from_kafka;

```

这样kafka topic中的数据被清洗到materialized_uk_price_paid_from_kafka表中。

## 查询

```
select * from materialized_uk_price_paid_from_kafka;

```

<img src="https://img-blog.csdnimg.cn/729dbc7e8b5648699fa8d59dc9eb6833.png" alt="在这里插入图片描述"> 我们在给topic发送下面的内容

>  
 “{5FA8692E-537B-4278-8C67-5A060540506D}”,“19500”,“1995-01-27 00:00”,“SK10 2QW”,“T”,“N”,“L”,“38”,“”,“GARDEN STREET”,“MACCLESFIELD”,“MACCLESFIELD”,“MACCLESFIELD”,“CHESHIRE”,“A”,“A” 


再查询表

```
select * from materialized_uk_price_paid_from_kafka;

```

<img src="https://img-blog.csdnimg.cn/3325133df6d64ff29843cd31572326f4.png" alt="在这里插入图片描述">
