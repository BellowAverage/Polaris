
--- 
title:  0基础学习PyFlink——使用datagen生成流式数据 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- <ul><li>- - - - - - - <ul><li>- - - - 


在研究Flink的水位线（WaterMark）技术之前，我们可能需要Flink接收到流式数据，比如接入Kafka等。这就要求引入其他组件，增加了学习的难度。而Flink自身提供了datagen连接器，它可以用于生成流式数据，让问题内聚在Flink代码内部，从而降低学习探索的难度。 本节我们就介绍如何使用datagen生成数据。

## 可控参数

我们可以使用option方法控制生成的一些规则，主要分为“字段级规则”和“表级规则”。

### 字段级规则

顾名思义，字段级规则是指该规则作用于具体哪个字段，这就需要指明字段的名称——fields.**col_name**。

#### 生成方式

字段的生成方式由下面的字符串形式来控制（#表示字段的名称，下同）

>  
 fields.#.kind 


可选值有：
- random：随机方式，比如5,2,1,4,6……。- sequence：顺序方式，比如1,2,3,4,5,6……。
#### 数值控制

如果kind是sequence，则数值控制使用：
- fields.#.start：区间的起始值。- fields.#.end：区间的结束值。
如果配置了这个两个参数，则会生成有限个数的数据。

如果kind是random，则数值控制使用：
- fields.#.min：随机算法会选取的最小值。- fields.#.max：随机算法会选取的最大值。
#### 时间戳控制

fields.#.max-past仅仅可以用于TIMESTAMP和TIMESTAMP_LTZ类型的数据。它表示离现在时间戳最大的时间差，这个默认值是0。TIMESTAMP和TIMESTAMP_LTZ只支持random模式生成，这就需要控制随机值的区间。如果区间太小，我们生成的时间可能非常集中。后面我们会做相关测试。

### 表级规则

#### 生成速度

rows-per-second表示每秒可以生成几条数据。

#### 生成总量

number-of-rows表示一共可以生成多少条数据。如果这个参数不设置，则表示可以生成无界流。

## 结构

### 生成环境

我们需要流式环境，而datagen是Table API的连接器，于是使用流式执行环境创建一个流式表环境。

```
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)

```

### 定义行结构

```
    schame = Schema.new_builder().column('seed', DataTypes.INT()).build()

```

这个结构以及支持的生成模式是：

|Type|Supported Generators
|------
|BOOLEAN|random
|CHAR|random / sequence
|VARCHAR|random / sequence
|BINARY|random / sequence
|VARBINARY|random / sequence
|STRING|random / sequence
|DECIMAL|random / sequence
|TINYINT|random / sequence
|SMALLINT|random / sequence
|INT|random / sequence
|BIGINT|random / sequence
|FLOAT|random / sequence
|DOUBLE|random / sequence
|DATE|random
|TIME|random
|TIMESTAMP|random
|TIMESTAMP_LTZ|random
|INTERVAL YEAR TO MONTH|random
|INTERVAL DAY TO MONTH|random
|ROW|random
|ARRAY|random
|MAP|random
|MULTISET|random

#### 定义表信息

下面这个例子就是给seed字段按随机模式，生成seed_min和seed_max之间的数值，并且每秒生成rows_per_second行。

```
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('fields.seed.min', str(seed_min)) \
                        .option('fields.seed.max', str(seed_max)) \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()

```

## 案例

### 随机Int型

每秒生成5行数据，每行数据中seed字段值随机在最小值0和最大值100之间。由于没有指定number-of-rows，生成的是无界流。

```
def gen_random_int():
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    seed_min = 0
    seed_max = 100
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.INT()).build()
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('fields.seed.min', str(seed_min)) \
                        .option('fields.seed.max', str(seed_max)) \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
                            
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()

```

```
+----+-------------+
| op |        seed |
+----+-------------+
| +I |          25 |
| +I |          28 |
| +I |          73 |
| +I |          68 |
| +I |          40 |
| +I |          55 |
| +I |           6 |
| +I |          41 |
| +I |          16 |
| +I |          19 |
……

```

### 顺序Int型

每秒生成5行数据，每行数据中seed字段值从1开始递增，一直自增到10。由于设置了最大和最小值，生成的是有界流。

```
def gen_sequence_int():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    seed_min = 1
    seed_max = 10
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.INT()).build()
    table_descriptor = TableDescriptor.for_connector('datagen') \
                            .schema(schame) \
                            .option('fields.seed.kind', 'sequence') \
                            .option('fields.seed.start', str(seed_min)) \
                            .option('fields.seed.end', str(seed_max)) \
                            .option('rows-per-second', str(rows_per_second)) \
                            .build()
                            
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()

```

```
+----+-------------+
| op |        seed |
+----+-------------+
| +I |           1 |
| +I |           2 |
| +I |           3 |
| +I |           4 |
| +I |           5 |
| +I |           6 |
| +I |           7 |
| +I |           8 |
| +I |           9 |
| +I |          10 |
+----+-------------+
10 rows in set

```

### 随机型Int数组

每秒生成5行数据，每行数据中seed字段是一个Int型数组，数组里面的每个元素也是随机的。

```
def gen_random_int_array():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.ARRAY(DataTypes.INT())) \
                                .build()
                                
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
    
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()

```

```
+----+--------------------------------+
| op |                           seed |
+----+--------------------------------+
| +I | [625785630, -933999461, -48... |
| +I | [2087310154, 1602723641, 19... |
| +I | [1299442620, -613376781, -8... |
| +I | [2051511574, 246258035, -16... |
| +I | [2029482070, -1496468635, -... |
| +I | [1230213175, -1506525784, 7... |
| +I | [501476712, 1901967363, -56... |
……

```

### 带时间戳的多列数据

每秒生成5行数据，每行数据中seed字段值随机在最小值0和最大值100之间；timestamp字段随机在当前时间戳和“当前时间戳+max-past”之间。

```
def gen_random_int_and_timestamp():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    seed_min = 0
    seed_max = 100
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.INT()) \
                                .column('timestamp', DataTypes.TIMESTAMP()) \
                                .build()
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('fields.seed.min', str(seed_min)) \
                        .option('fields.seed.max', str(seed_max)) \
                        .option('fields.timestamp.kind', 'random') \
                        .option('fields.timestamp.max-past', '0') \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
    
          
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()

```

由于max-past值为0，所以我们看到上例中每秒生成的timestamp 都极接近。

```
+----+-------------+----------------------------+
| op |        seed |                  timestamp |
+----+-------------+----------------------------+
| +I |          66 | 2023-11-02 13:53:29.082000 |
| +I |           9 | 2023-11-02 13:53:29.146000 |
| +I |          12 | 2023-11-02 13:53:29.146000 |
| +I |          52 | 2023-11-02 13:53:29.146000 |
| +I |          29 | 2023-11-02 13:53:29.146000 |
| +I |          63 | 2023-11-02 13:53:30.066000 |
| +I |          25 | 2023-11-02 13:53:30.066000 |
| +I |          21 | 2023-11-02 13:53:30.066000 |
| +I |          24 | 2023-11-02 13:53:30.066000 |
| +I |           6 | 2023-11-02 13:53:30.066000 |
| +I |          62 | 2023-11-02 13:53:31.067000 |
| +I |          57 | 2023-11-02 13:53:31.067000 |
| +I |          44 | 2023-11-02 13:53:31.067000 |
| +I |           6 | 2023-11-02 13:53:31.067000 |
| +I |          16 | 2023-11-02 13:53:31.067000 |
……

```

如果我们把max-past放大到比较大的数值，timestamp也将大幅度变化。

```
.option('fields.timestamp.max-past', '10000')

```

```
+----+-------------+----------------------------+
| op |        seed |                  timestamp |
+----+-------------+----------------------------+
| +I |          89 | 2023-11-02 13:57:17.342000 |
| +I |          35 | 2023-11-02 13:57:10.915000 |
| +I |          32 | 2023-11-02 13:57:11.045000 |
| +I |          74 | 2023-11-02 13:57:18.407000 |
| +I |          24 | 2023-11-02 13:57:13.603000 |
| +I |          82 | 2023-11-02 13:57:12.139000 |
| +I |          41 | 2023-11-02 13:57:16.129000 |
| +I |          95 | 2023-11-02 13:57:16.592000 |
| +I |          80 | 2023-11-02 13:57:14.364000 |
| +I |          60 | 2023-11-02 13:57:18.994000 |
| +I |          56 | 2023-11-02 13:57:19.330000 |
| +I |          10 | 2023-11-02 13:57:18.876000 |
| +I |          43 | 2023-11-02 13:57:12.449000 |
| +I |          73 | 2023-11-02 13:57:13.183000 |
| +I |          17 | 2023-11-02 13:57:18.736000 |
| +I |          46 | 2023-11-02 13:57:21.368000 |
……

```

## 完整代码

```

from pyflink.datastream import StreamExecutionEnvironment,RuntimeExecutionMode
from pyflink.table import StreamTableEnvironment, TableDescriptor, Schema, DataTypes

def gen_random_int():
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    seed_min = 0
    seed_max = 100
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.INT()).build()
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('fields.seed.min', str(seed_min)) \
                        .option('fields.seed.max', str(seed_max)) \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
                            
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()
    
def gen_sequence_int():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    seed_min = 1
    seed_max = 10
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.INT()).build()
    table_descriptor = TableDescriptor.for_connector('datagen') \
                            .schema(schame) \
                            .option('fields.seed.kind', 'sequence') \
                            .option('fields.seed.start', str(seed_min)) \
                            .option('fields.seed.end', str(seed_max)) \
                            .option('rows-per-second', str(rows_per_second)) \
                            .build()
                            
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()
    
def gen_sequence_string():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    seed_min = 0
    seed_max = 100
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.STRING()).build()
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'sequence') \
                        .option('fields.seed.start', str(seed_min)) \
                        .option('fields.seed.end', str(seed_max)) \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
                            
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()

def gen_random_char():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.CHAR(4)).build()
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
                            
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()
    
def gen_random_int_and_timestamp():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    seed_min = 0
    seed_max = 100
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.INT()) \
                                .column('timestamp', DataTypes.TIMESTAMP()) \
                                .build()
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('fields.seed.min', str(seed_min)) \
                        .option('fields.seed.max', str(seed_max)) \
                        .option('fields.timestamp.kind', 'random') \
                        .option('fields.timestamp.max-past', '10000') \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
    
          
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()
    
def gen_random_int_array():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.ARRAY(DataTypes.INT())) \
                                .build()
                                
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
    
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()
    
def gen_random_map():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.MAP(DataTypes.STRING(), DataTypes.INT())) \
                                .build()
                                
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
    
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()
    
def gen_random_multiset():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.MULTISET(DataTypes.STRING())) \
                                .build()
                                
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
    
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()
    
def gen_random_row():
    
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    
    rows_per_second = 5
    schame = Schema.new_builder().column('seed', DataTypes.ROW([DataTypes.FIELD("id", DataTypes.BIGINT()), DataTypes.FIELD("data", DataTypes.STRING())])) \
                                .build()
                                
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.seed.kind', 'random') \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
    
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    table.execute().print()
    
    
if __name__ == '__main__':
    gen_random_int_and_timestamp()

```

## 参考资料
- 