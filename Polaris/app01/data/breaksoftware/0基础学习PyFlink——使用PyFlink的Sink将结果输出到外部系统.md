
--- 
title:  0基础学习PyFlink——使用PyFlink的Sink将结果输出到外部系统 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>


```
select word, count(1) as `count` from source group by word;
+--------------------------------+----------------------+
|                           word |                count |
+--------------------------------+----------------------+
|                              A |                    3 |
|                              B |                    1 |
|                              C |                    2 |
|                              D |                    2 |
|                              E |                    1 |
+--------------------------------+----------------------+

```

在生产环境，我们往往要将计算结果保存到外部系统中，比如Mysql等。这个时候我们就要使用Sink。

## Sink

Sink用于将Reduce结果输出到外部系统。它也是通过一个表（Table）来表示结构。这个和MapReduce思路中的Map很类似。

### Print

为了简单起见，我们让Sink的表连接的外部系统是print。这样我们就可以在控制台上看到数据。

```
    # define the sink
    my_sink_ddl = """
        CREATE TABLE WordsCountTableSink (
            `word` STRING,
            `count` BIGINT
        ) WITH (
            'connector' = 'print'
        );
    """
    t_env.execute_sql(my_sink_ddl).print()

```

需要强调的是，我们没有给sink的表创建主键。这个会在后面文章中作为一个对比案例进行分析。 这一步只能创建表和连接器，具体执行还要执行下一步。

## Execute

因为source和WordsCountTableSink是两张表，分别表示数据的输入和输出结构。如果要打通输入和输出，则需要将source表中的数据通过某些计算，插入到WordsCountTableSink表中。于是我们主要使用的是insert into指令。

```
    # execute insert
    my_select_ddl = """
        insert into WordsCountTableSink
        select word, count(1) as `count`
        from source
        group by word
    """
    t_env.execute_sql(my_select_ddl).wait()

```

## 完整代码

```
import argparse
import logging
import sys

from pyflink.common import Configuration
from pyflink.table import (EnvironmentSettings, TableEnvironment)

def word_count(input_path):
    config = Configuration()
    # write all the data to one file
    config.set_string('parallelism.default', '1')
    env_settings = EnvironmentSettings \
        .new_instance() \
        .in_batch_mode() \
        .with_configuration(config) \
        .build()
    
    t_env = TableEnvironment.create(env_settings)

    # define the source
    my_source_ddl = """
            create table source (
                word STRING
            ) with (
                'connector' = 'filesystem',
                'format' = 'csv',
                'path' = '{}'
            )
        """.format(input_path)
    t_env.execute_sql(my_source_ddl).print()
    tab = t_env.from_path('source')

    # define the sink
    my_sink_ddl = """
        CREATE TABLE WordsCountTableSink (
            `word` STRING,
            `count` BIGINT
        ) WITH (
            'connector' = 'print'
        );
    """
    t_env.execute_sql(my_sink_ddl).print()
    
    # execute insert
    my_select_ddl = """
        insert into WordsCountTableSink
        select word, count(1) as `count`
        from source
        group by word
    """
    t_env.execute_sql(my_select_ddl).wait()

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        required=False,
        help='Input file to process.')

    argv = sys.argv[1:]
    known_args, _ = parser.parse_known_args(argv)

    word_count(known_args.input)

```

执行命令如下

```
python sql_print.py --input input1.csv

```

输出结果如下

>  
 Using Any for unsupported type: typing.Sequence[~T] No module named google.cloud.bigquery_storage_v1. As a result, the ReadFromBigQuery transform **CANNOT** be used with `method=DIRECT_READ`. OK OK +I[A, 3] +I[B, 1] +I[C, 2] +I[D, 2] +I[E, 1] 


因为使用的是批处理模式（in_batch_mode），我们看到Flink将所有数据计算完整成，成批的执行了新增操作（+代表新增）。这块对比我们将在后续将流处理时介绍区别。 附上input1.csv内容

```
"A",
"B",
"C",
"D",
"A",
"E",
"C",
"D",
"A",

```
