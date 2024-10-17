
--- 
title:  探索ClickHouse——使用Projection加速查询 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- - - - - - - <ul><li>- - - 


## 下载文件

```
wget wget http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv .

```

### 检查文件

```
wc -l pp-complete.csv 

```

>  
 28497127 pp-complete.csv 


```
ll pp-complete.csv

```

>  
 -rw-rw-r-- 1 fangliang fangliang 4982107267 Aug 29 05:13 pp-complete.csv 


即这个文件约有2850万行，占4个多G磁盘。

### 移动文件

```
su root
cp pp-complete.csv /var/lib/clickhouse/user_files/
exit

```

## 创建表

### 查看文件

使用下面指令查看文件内容

```
head -10 pp-complete.csv 

```

```
"{<!-- -->F887F88E-7D15-4415-804E-52EAC2F10958}","70000","1995-07-07 00:00","MK15 9HP","D","N","F","31","","ALDRICH DRIVE","WILLEN","MILTON KEYNES","MILTON KEYNES","MILTON KEYNES","A","A"
"{<!-- -->40FD4DF2-5362-407C-92BC-566E2CCE89E9}","44500","1995-02-03 00:00","SR6 0AQ","T","N","F","50","","HOWICK PARK","SUNDERLAND","SUNDERLAND","SUNDERLAND","TYNE AND WEAR","A","A"
"{<!-- -->7A99F89E-7D81-4E45-ABD5-566E49A045EA}","56500","1995-01-13 00:00","CO6 1SQ","T","N","F","19","","BRICK KILN CLOSE","COGGESHALL","COLCHESTER","BRAINTREE","ESSEX","A","A"
"{<!-- -->28225260-E61C-4E57-8B56-566E5285B1C1}","58000","1995-07-28 00:00","B90 4TG","T","N","F","37","","RAINSBROOK DRIVE","SHIRLEY","SOLIHULL","SOLIHULL","WEST MIDLANDS","A","A"
"{<!-- -->444D34D7-9BA6-43A7-B695-4F48980E0176}","51000","1995-06-28 00:00","DY5 1SA","S","N","F","59","","MERRY HILL","BRIERLEY HILL","BRIERLEY HILL","DUDLEY","WEST MIDLANDS","A","A"
"{<!-- -->AE76CAF1-F8CC-43F9-8F63-4F48A2857D41}","17000","1995-03-10 00:00","S65 1QJ","T","N","L","22","","DENMAN STREET","ROTHERHAM","ROTHERHAM","ROTHERHAM","SOUTH YORKSHIRE","A","A"
"{<!-- -->709FB471-3690-4945-A9D6-4F48CE65AAB6}","58000","1995-04-28 00:00","PE7 3AL","D","Y","F","4","","BROOK LANE","FARCET","PETERBOROUGH","PETERBOROUGH","CAMBRIDGESHIRE","A","A"
"{<!-- -->5FA8692E-537B-4278-8C67-5A060540506D}","19500","1995-01-27 00:00","SK10 2QW","T","N","L","38","","GARDEN STREET","MACCLESFIELD","MACCLESFIELD","MACCLESFIELD","CHESHIRE","A","A"
"{<!-- -->E78710AD-ED1A-4B11-AB99-5A0614D519AD}","20000","1995-01-16 00:00","SA6 5AY","D","N","F","592","","CLYDACH ROAD","YNYSTAWE","SWANSEA","SWANSEA","SWANSEA","A","A"
"{<!-- -->1DFBF83E-53A7-4813-A37C-5A06247A09A8}","137500","1995-03-31 00:00","NR2 2NQ","D","N","F","26","","LIME TREE ROAD","NORWICH","NORWICH","NORWICH","NORFOLK","A","A"

```

### 使用客户端连接服务端

```
clickhouse-client

```

### 创建表

```
CREATE TABLE uk_price_paid ( price UInt32, date Date, postcode1 LowCardinality(String), postcode2 LowCardinality(String), type Enum8('terraced' = 1, 'semi-detached' = 2, 'detached' = 3, 'flat' = 4, 'other' = 0), is_new UInt8, duration Enum8('freehold' = 1, 'leasehold' = 2, 'unknown' = 0), addr1 String, addr2 String, street LowCardinality(String), locality LowCardinality(String), town LowCardinality(String), district LowCardinality(String), county LowCardinality(String) ) ENGINE = MergeTree ORDER BY (postcode1, postcode2, addr1, addr2);

```

### 导入数据

```
INSERT INTO uk_price_paid WITH splitByChar(' ', postcode) AS p SELECT toUInt32(price_string) AS price, parseDateTimeBestEffortUS(time) AS date, p[1] AS postcode1, p[2] AS postcode2, transform(a, ['T', 'S', 'D', 'F', 'O'], ['terraced', 'semi-detached', 'detached', 'flat', 'other']) AS type, b = 'Y' AS is_new, transform(c, ['F', 'L', 'U'], ['freehold', 'leasehold', 'unknown']) AS duration, addr1, addr2, street, locality, town, district, county FROM file( 'pp-complete.csv', 'CSV', 'uuid_string String, price_string String, time String, postcode String, a String, b String, c String, addr1 String, addr2 String, street String, locality String, town String, district String, county String, d String, e String' );

```

<img src="https://img-blog.csdnimg.cn/aba00b17c3724d278978322544167699.png#pic_center" alt="在这里插入图片描述"> 整个处理速度大概是210 thousand rows/s，36.5MB/s。

>  
 INSERT INTO uk_price_paid WITH splitByChar(’ ', postcode) AS p SELECT toUInt32(price_string) AS price, parseDateTimeBestEffortUS(time) AS date, p[1] AS postcode1, p[2] AS postcode2, transform(a, [‘T’, ‘S’, ‘D’, ‘F’, ‘O’], [‘terraced’, ‘semi-detached’, ‘detached’, ‘flat’, ‘other’]) AS type, b = ‘Y’ AS is_new, transform(c, [‘F’, ‘L’, ‘U’], [‘freehold’, ‘leasehold’, ‘unknown’]) AS duration, addr1, addr2, street, locality, town, district, county FROM file(‘pp-complete.csv’, ‘CSV’, ‘uuid_string String, price_string String, time String, postcode String, a String, b String, c String, addr1 String, addr2 String, street String, locality String, town String, district String, county String, d String, e String’) Query id: 32a2a670-8417-470d-ab26-6368dd1725e5 Ok. 0 rows in set. Elapsed: 140.063 sec. Processed 28.50 million rows, 4.98 GB (203.46 thousand rows/s., 35.57 MB/s.) 


### 检查数据

#### 检查数据行数

```
SELECT count() From uk_price_paid;

```

>  
 SELECT count() FROM uk_price_paid Query id: 2d05b3f1-c683-4f2d-bcaf-e05b777eb3f8 ┌──count()───┐ │ 28497127 │ └──────────┘ 1 row in set. Elapsed: 0.005 sec. 


一共有28,497,127行数据，和文件中行数一致。

#### 检查所占磁盘

```
SELECT formatReadableSize(total_bytes) FROM system.tables WHERE name = 'uk_price_paid';

```

>  
 SELECT formatReadableSize(total_bytes) FROM system.tables WHERE name = ‘uk_price_paid’ Query id: 7cca5694-6d15-4f38-8f8d-ef8331a4caa3 ┌─formatReadableSize(total_bytes)─┐ │ 308.18 MiB │ └──────────────────────┘ 1 row in set. Elapsed: 0.007 sec. 


和之前文件4G多大小对比，减少了9/10，这个比例是相当大的。

## 查询

```
SELECT toYear(date), district, town, avg(price), sum(price), count() FROM uk_price_paid  GROUP BY toYear(date), district, town;

```

>  
 80441 rows in set. Elapsed: 2.114 sec. Processed 28.50 million rows, 284.78 MB (13.48 million rows/s., 134.71 MB/s.) 


### 新增PROJECTION

使用下面指令给toYear(date), district, town创建一个PROJECTION ，这样之后插入的数据就会被自动优化。

```
ALTER TABLE uk_price_paid ADD PROJECTION projection_by_year_district_town(SELECT toYear(date), district, town, avg(price), sum(price), count() GROUP BY toYear(date), district, town);

```

>  
 ALTER TABLE uk_price_paid ADD PROJECTION projection_by_year_district_town ( SELECT toYear(date), district, town, avg(price), sum(price), count() GROUP BY toYear(date), district, town ) Query id: 3c5ca13e-4805-412c-845a-ab18c411261c Ok. 0 rows in set. Elapsed: 0.007 sec. 


然后使用下面指令修改现有数据

```
ALTER TABLE uk_price_paid MATERIALIZE PROJECTION projection_by_year_district_town SETTINGS mutations_sync = 1;

```

>  
 ALTER TABLE uk_price_paid MATERIALIZE PROJECTION projection_by_year_district_town SETTINGS mutations_sync = 1 Query id: 7bd22c05-c74c-4972-be6d-174eaf99c498 Ok. 0 rows in set. Elapsed: 0.183 sec. 


### 优化后查询

>  
 80441 rows in set. Elapsed: 0.170 sec. Processed 92.93 thousand rows, 5.76 MB (548.06 thousand rows/s., 33.98 MB/s.) 


可以看到时间也缩短到未优化的1/10。

## 参考资料
- 