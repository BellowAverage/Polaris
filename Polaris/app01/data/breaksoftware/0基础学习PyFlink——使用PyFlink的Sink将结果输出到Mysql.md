
--- 
title:  0基础学习PyFlink——使用PyFlink的Sink将结果输出到Mysql 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- 


## Mysql配置

假定本机已安装好Mysql Server和Client。

### 配置用户和密码

通过下面的配置，我们可以让Flink通过该用户名和密码访问Mysql数据库。

```
sudo mysql -u root
use mysql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'pwd123';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
quit

```

### 创建数据库和表

这个表只有两个字段，一个是用于表示字符的word，一个是其个数count。 需要注意的是，我们并没有设置主键。

```
create database words_count_db;
use words_count_db;
CREATE TABLE WordsCountTable (
  word varchar(255) NOT NULL,
  count BIGINT
);

```

## PyFlink配置

因为我们要使用JDBC连接Mysql，于是需要引入相关的包

```
cd /home/fangliang/pyflink-test/.env/lib/python3.10/site-packages/pyflink/lib

```

下载jdbc和mysql-connector包

```
wget https://repo1.maven.org/maven2/org/apache/flink/flink-connector-jdbc_2.12/1.14.6/flink-connector-jdbc_2.12-1.14.6.jar .
wget https://repo.maven.apache.org/maven2/mysql/mysql-connector-java/8.0.9-rc/mysql-connector-java-8.0.9-rc.jar .

```

<img src="https://img-blog.csdnimg.cn/aaf8d148a72049ae9c06c6c506c9a7e1.png" alt="在这里插入图片描述">

## Sink

相较于中输出到终端的Sink，我们只需要修改器with字段的连接器即可。

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

words_count_db是之前在Mysql中创建的数据库名；WordsCountTable是Mysql中表名；其他字段比较好理解，就不解释了。

## 完整代码

```
# sql.py
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
            'connector' = 'jdbc',
            'url' = 'jdbc:mysql://127.0.0.1:3306/words_count_db?useSSL=false',
            'table-name' = 'WordsCountTable',
            'driver'='com.mysql.jdbc.Driver',
            'username'='admin',
            'password'='pwd123'
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

执行命令是

```
python sql.py --input input1.csv

```

>  
 Using Any for unsupported type: typing.Sequence[~T] No module named google.cloud.bigquery_storage_v1. As a result, the ReadFromBigQuery transform **CANNOT** be used with `method=DIRECT_READ`. OK OK 


我们在Mysql Client端查询结果数据如下

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
+------+-------+
5 rows in set (0.00 sec)

```

附上input1.csv

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
