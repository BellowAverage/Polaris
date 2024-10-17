
--- 
title:  [hive] 本地xlsx 导入到hive 
tags: []
categories: [] 

---
要将一个 xlsx 文件中的数据导入到 Hive 表中，可以通过以下步骤来实现：
1.  首先，将 xlsx 文件中的数据导出为 CSV 格式，这样更方便后续处理。可以使用 Excel 软件将 xlsx 文件另存为 CSV 格式。 1.  在 Hive 中创建一个新表，用于存储导入的数据。假设表名为 `my_table`，包含两列 `key` 和 `type`，可以使用以下 Hive DDL 语句创建表： 
```
CREATE TABLE my_table (
    key STRING,
    type STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

```
1. 将 CSV 文件上传到 HDFS 中，假设文件路径为 `/path/to/data.csv`。
```
hdfs dfs -put -f local.csv /path/to/data.csv

```
1. 使用 Hive 命令行或其他工具连接到 Hive，并执行以下命令将 CSV 文件中的数据导入到 `my_table` 表中：
```
LOAD DATA INPATH '/path/to/data.csv' [OVERWRITE] INTO TABLE my_table;

```
- `OVERWRITE` 可选, 是否覆盖掉原来的内容
执行上述命令后，Hive 将会将 CSV 文件中的数据加载到指定的表中。你可以通过查询 `my_table` 表来验证数据是否成功导入。
