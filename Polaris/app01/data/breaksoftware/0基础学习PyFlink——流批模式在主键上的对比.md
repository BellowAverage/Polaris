
--- 
title:  0基础学习PyFlink——流批模式在主键上的对比 
tags: []
categories: [] 

---


#### 大纲
- - - - <ul><li>- <ul><li>- - - - <ul><li>- - - 


## 批处理

```
    env_settings = EnvironmentSettings \
        .new_instance() \
        .in_batch_mode() \
        .with_configuration(config) \
        .build()

```

```
# 批处理
+I[A, 3]
+I[B, 1]
+I[C, 2]
+I[D, 2]
+I[E, 1]

```

## 流处理

```
    env_settings = EnvironmentSettings \
        .new_instance() \
        .in_streaming_mode() \
        .with_configuration(config) \
        .build()

```

```
# 流处理
+I[A, 1]
+I[B, 1]
+I[C, 1]
+I[D, 1]
-U[A, 1]
+U[A, 2]
+I[E, 1]
-U[C, 1]
+U[C, 2]
-U[D, 1]
+U[D, 2]
-U[A, 2]
+U[A, 3]

```

我们看到批处理是一次性的达成了最终计算——只插入了5条数据，且每条数据都是最终结果。 而流处理则是进行了13次操作，其中插入操作5次，删除4次，更新4次。

## 只有插入操作

### Mysql表无主键

```
CREATE TABLE WordsCountTable (
  word varchar(255) NOT NULL,
  count BIGINT
);

```

#### Sink表无主键

```
    my_sink_ddl = """
        CREATE TABLE WordsCountTableSink (
            `word` STRING,
            `count` BIGINT
        ) WITH (
            'connector' = 'jdbc',
            'url' = 'jdbc:mysql://127.0.0.1:3306/words_count_db?useSSL=false',
            'table-name' = 'WordsCountTable',
            'driver'='com.mysql.jdbc.Driver',
            'username'='admin',
            'password'='pwd123'
        );
    """

```

#### Sink表有主键

```
    my_sink_ddl = """
        CREATE TABLE WordsCountTableSink (
            `word` STRING,
            `count` BIGINT,
            PRIMARY KEY (`word`) NOT ENFORCED
        ) WITH (
            'connector' = 'jdbc',
            'url' = 'jdbc:mysql://127.0.0.1:3306/words_count_db?useSSL=false',
            'table-name' = 'WordsCountTable',
            'driver'='com.mysql.jdbc.Driver',
            'username'='admin',
            'password'='pwd123'
        );
    """

```

则对于只有插入操作的Batch模式，不管Sink表有没有主键，每次程序执行时都会插入新数据。比如我们执行两次批处理模式代码，则可以看到5的2倍=10条数据。

```
select * from WordsCountTable;

```

```
+------+-------+
| word | count |
+------+-------+
| A    |     3 |
| B    |     1 |
| C    |     2 |
| D    |     2 |
| E    |     1 |
| A    |     3 |
| B    |     1 |
| C    |     2 |
| D    |     2 |
| E    |     1 |
+------+-------+
10 rows in set (0.00 sec)

```

这个很好理解。

### Mysql表有主键

```
CREATE TABLE WordsCountTable (
  word varchar(255) NOT NULL,
  count BIGINT,
  PRIMARY KEY (word)
);

```

#### Sink表无主键

因为word成为主键，不可以重复。第一次执行插入操作时成功了

```
+------+-------+
| word | count |
+------+-------+
| A    |     3 |
| B    |     1 |
| C    |     2 |
| D    |     2 |
| E    |     1 |
+------+-------+
5 rows in set (0.00 sec)

```

但是第二次执行时，会因为主键冲突报错：

>  
 Caused by: java.sql.SQLIntegrityConstraintViolationException: Duplicate entry ‘E’ for key ‘WordsCountTable.PRIMARY’ 


### Sink表有主键

因为Mysql和Sink表里主键一致，不管执行多少次程序，都不会产生多余的数据。

```
+------+-------+
| word | count |
+------+-------+
| A    |     3 |
| B    |     1 |
| C    |     2 |
| D    |     2 |
| E    |     1 |
+------+-------+
5 rows in set (0.00 sec)

```

## 有删除和更新操作

在流模式中我们看到，流处理处理有插入操作外，还有其他操作。我们再对比下它们的表现。

### Sink表无主键

#### Mysql表无主键

#### Mysql有无主键

因为流模式删除和更新操作需要通过主键来寻找对象，所以会报如下错误

>  
 java.lang.IllegalStateException: please declare primary key for sink table when query contains update/delete record. 


### Sink表有主键

由于Sink表设置了主键，于是流模式产生的更新和删除操作可以通过其找到对应项，就不会报错。

#### Mysql表无主键

由于Mysql表没有主键，导致每次执行都会插入一批数据。比如下面是我们执行两次的结果

```
+------+-------+
| word | count |
+------+-------+
| E    |     1 |
| A    |     3 |
| D    |     2 |
| C    |     2 |
| B    |     1 |
| A    |     3 |
| D    |     2 |
| B    |     1 |
| C    |     2 |
| E    |     1 |
+------+-------+
10 rows in set (0.00 sec)

```

这从另外一个方面说明：**流模式产生的一系列操作，在Execute环节，最终会对这些操作进行合并，将合并的操作同步给外部系统。**比如之前的流操作实际产生了13个行为，而最终落到数据库里只有5条数据，且第二次操作也是插入了5条新的、最终的数据，这就说明中间的操作在同步给数据库之前已经做了合并处理。

#### Mysql表有主键

因为Mysql表有主键，Sink过来的操作执行的是“**有则更新，无则写入**”的模式。 比如我们第一次执行程序时，得到

```
+------+-------+
| word | count |
+------+-------+
| A    |     3 |
| B    |     1 |
| C    |     2 |
| D    |     2 |
| E    |     1 |
+------+-------+
5 rows in set (0.00 sec)

```

然后我们将数据源中的E改成了A，则这次将出现4个A，但是不会出现E。执行后的结果是

```
+------+-------+
| word | count |
+------+-------+
| A    |     4 |
| B    |     1 |
| C    |     2 |
| D    |     2 |
| E    |     1 |
+------+-------+
5 rows in set (0.00 sec)

```

这个实验就证明了，当Sink和Mysql表的主键一致时，执行的是insert on duplicate key update操作。
