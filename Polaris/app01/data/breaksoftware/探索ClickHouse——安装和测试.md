
--- 
title:  探索ClickHouse——安装和测试 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- - - - - - 


## 安装

### 检测环境

```
grep -q sse4_2 /proc/cpuinfo &amp;&amp; echo "SSE 4.2 supported" || echo "SSE 4.2 not supported"

```

>  
 SSE 4.2 supported 


可以看到我们的环境支持编译版本的。如果不支持的环境可以考虑通过。

### 安装

```
sudo apt-get install -y apt-transport-https ca-certificates dirmngr
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 8919F6BD2B48D754

echo "deb https://packages.clickhouse.com/deb stable main" | sudo tee /etc/apt/sources.list.d/clickhouse.list
sudo apt-get update

sudo apt-get install -y clickhouse-server clickhouse-client

```

结束时会让输入default用户的密码。

>  
 Enter password for default user: 


>  
 **Password for default user is saved in file /etc/clickhouse-server/users.d/default-password.xml.** Setting capabilities for clickhouse binary. This is optional. chown -R clickhouse:clickhouse ‘/etc/clickhouse-server’ ClickHouse has been successfully installed. Start clickhouse-server with: sudo clickhouse start Start clickhouse-client with: clickhouse-client --password 


### 启动

```
 sudo clickhouse start

```

>  
 chown -R clickhouse: ‘/var/run/clickhouse-server/’ Will run sudo --preserve-env -u ‘clickhouse’ /usr/bin/clickhouse-server --config-file /etc/clickhouse-server/config.xml --pid-file /var/run/clickhouse-server/clickhouse-server.pid --daemon Waiting for server to start Waiting for server to start Server started 


## 测试

我们以中2021年数据为例。

### 下载

我们把数据下载下来，查看下其数据内容。

```
wget http://prod1.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2021.csv .

```

### 分析数据

```
head -10 pp-2021.csv

```

```
"{<!-- -->D22473F5-3802-7B40-E053-6C04A8C0A630}","230000","2021-06-09 00:00","CO13 0PQ","D","N","F","4","","BELLAMY CLOSE","KIRBY CROSS","FRINTON-ON-SEA","TENDRING","ESSEX","A","A"
"{<!-- -->D22473F5-3803-7B40-E053-6C04A8C0A630}","700000","2021-06-25 00:00","IG10 4BS","T","N","F","70","","SMARTS LANE","","LOUGHTON","EPPING FOREST","ESSEX","A","A"
"{<!-- -->D22473F5-3804-7B40-E053-6C04A8C0A630}","625000","2021-06-28 00:00","EN9 1LH","S","N","F","7","","THE COBBINS","","WALTHAM ABBEY","EPPING FOREST","ESSEX","A","A"
"{<!-- -->D22473F5-3805-7B40-E053-6C04A8C0A630}","360000","2021-02-17 00:00","SS9 3AU","S","N","F","117","","FLEMMING AVENUE","","LEIGH-ON-SEA","SOUTHEND-ON-SEA","SOUTHEND-ON-SEA","A","A"
"{<!-- -->D22473F5-3806-7B40-E053-6C04A8C0A630}","345000","2021-06-25 00:00","SS15 6BG","S","N","F","2","","BROADWATER GREEN","LAINDON","BASILDON","BASILDON","ESSEX","A","A"
"{<!-- -->D22473F5-3807-7B40-E053-6C04A8C0A630}","220000","2021-08-20 00:00","CO7 0HE","S","N","F","133","","CHAPEL ROAD","BRIGHTLINGSEA","COLCHESTER","TENDRING","ESSEX","A","A"
"{<!-- -->D22473F5-3808-7B40-E053-6C04A8C0A630}","362000","2021-06-29 00:00","SS15 4AX","T","N","F","32","","CROUCH STREET","","BASILDON","BASILDON","ESSEX","A","A"
"{<!-- -->D22473F5-3809-7B40-E053-6C04A8C0A630}","300000","2021-06-25 00:00","CM9 6EP","T","N","F","58","","ORCHARD ROAD","","MALDON","MALDON","ESSEX","A","A"
"{<!-- -->D22473F5-380A-7B40-E053-6C04A8C0A630}","300000","2021-06-17 00:00","SS4 3AR","T","N","F","32","","ALLERTON CLOSE","","ROCHFORD","ROCHFORD","ESSEX","A","A"
"{<!-- -->D22473F5-380B-7B40-E053-6C04A8C0A630}","535000","2021-10-22 00:00","SS9 1PZ","T","N","F","113","","LEIGHTON AVENUE","","LEIGH-ON-SEA","SOUTHEND-ON-SEA","SOUTHEND-ON-SEA","A","A"

```

这些字段具体表意可以参考，即
- uuid_string String,- price_string String,- time String,- postcode String,- a String,- b String,- c String,- addr1 String,- addr2 String,- street String,- locality String,- town String,- district String,- county String,- d String,- e String
### 放置

默认的用户文件放置位置如如下配置

```
&lt;user_files_path&gt;/var/lib/clickhouse/user_files/&lt;/user_files_path&gt;

```

切到root用户，将文件放置到上述目录

```
su root
cp pp-2021.csv /var/lib/clickhouse/user_files/
exit

```

### 查询

```
clickhouse-client

```

```
SELECT * FROM file('pp-2021.csv', 'CSV', 'uuid_string String, price_string String, time String, postcode String, a String, b String, c String, addr1 String, addr2 String, street String, locality String, town String, district String, county String, d String, e String') LIMIT 10;

```

```
SELECT *
FROM file('pp-2021.csv', 'CSV', 'uuid_string String, price_string String, time String, postcode String, a String, b String, c String, addr1 String, addr2 String, street String, locality String, town String, district String, county String, d String, e String')
LIMIT 10

Query id: c08072df-a934-4276-bfbc-68d480409ca1

┌─uuid_string────────────────────────────┬─price_string─┬─time─────────────┬─postcode─┬─a─┬─b─┬─c─┬─addr1─┬─addr2─┬─street───────────┬─locality──────┬─town───────────┬─district────────┬─county──────────┬─d─┬─e─┐
│ {<!-- -->D22473F5-3802-7B40-E053-6C04A8C0A630} │ 230000       │ 2021-06-09 00:00 │ CO13 0PQ │ D │ N │ F │ 4     │       │ BELLAMY CLOSE    │ KIRBY CROSS   │ FRINTON-ON-SEA │ TENDRING        │ ESSEX           │ A │ A │
│ {<!-- -->D22473F5-3803-7B40-E053-6C04A8C0A630} │ 700000       │ 2021-06-25 00:00 │ IG10 4BS │ T │ N │ F │ 70    │       │ SMARTS LANE      │               │ LOUGHTON       │ EPPING FOREST   │ ESSEX           │ A │ A │
│ {<!-- -->D22473F5-3804-7B40-E053-6C04A8C0A630} │ 625000       │ 2021-06-28 00:00 │ EN9 1LH  │ S │ N │ F │ 7     │       │ THE COBBINS      │               │ WALTHAM ABBEY  │ EPPING FOREST   │ ESSEX           │ A │ A │
│ {<!-- -->D22473F5-3805-7B40-E053-6C04A8C0A630} │ 360000       │ 2021-02-17 00:00 │ SS9 3AU  │ S │ N │ F │ 117   │       │ FLEMMING AVENUE  │               │ LEIGH-ON-SEA   │ SOUTHEND-ON-SEA │ SOUTHEND-ON-SEA │ A │ A │
│ {<!-- -->D22473F5-3806-7B40-E053-6C04A8C0A630} │ 345000       │ 2021-06-25 00:00 │ SS15 6BG │ S │ N │ F │ 2     │       │ BROADWATER GREEN │ LAINDON       │ BASILDON       │ BASILDON        │ ESSEX           │ A │ A │
│ {<!-- -->D22473F5-3807-7B40-E053-6C04A8C0A630} │ 220000       │ 2021-08-20 00:00 │ CO7 0HE  │ S │ N │ F │ 133   │       │ CHAPEL ROAD      │ BRIGHTLINGSEA │ COLCHESTER     │ TENDRING        │ ESSEX           │ A │ A │
│ {<!-- -->D22473F5-3808-7B40-E053-6C04A8C0A630} │ 362000       │ 2021-06-29 00:00 │ SS15 4AX │ T │ N │ F │ 32    │       │ CROUCH STREET    │               │ BASILDON       │ BASILDON        │ ESSEX           │ A │ A │
│ {<!-- -->D22473F5-3809-7B40-E053-6C04A8C0A630} │ 300000       │ 2021-06-25 00:00 │ CM9 6EP  │ T │ N │ F │ 58    │       │ ORCHARD ROAD     │               │ MALDON         │ MALDON          │ ESSEX           │ A │ A │
│ {<!-- -->D22473F5-380A-7B40-E053-6C04A8C0A630} │ 300000       │ 2021-06-17 00:00 │ SS4 3AR  │ T │ N │ F │ 32    │       │ ALLERTON CLOSE   │               │ ROCHFORD       │ ROCHFORD        │ ESSEX           │ A │ A │
│ {<!-- -->D22473F5-380B-7B40-E053-6C04A8C0A630} │ 535000       │ 2021-10-22 00:00 │ SS9 1PZ  │ T │ N │ F │ 113   │       │ LEIGHTON AVENUE  │               │ LEIGH-ON-SEA   │ SOUTHEND-ON-SEA │ SOUTHEND-ON-SEA │ A │ A │
└────────────────────────────────────────┴──────────────┴──────────────────┴──────────┴───┴───┴───┴───────┴───────┴──────────────────┴───────────────┴────────────────┴─────────────────┴─────────────────┴───┴───┘

10 rows in set. Elapsed: 0.003 sec. 

```

## 参考资料
- - - - 