
--- 
title:  [spark] 存储到hdfs时指定分区 
tags: []
categories: [] 

---
在 SparkSQL 中指定多个分区字段进行数据存储：

>  
 类似hive 分区存储 




#### 文章目录
- - 


## 代码

```
import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder()
  .appName("MultiPartitionedWriteExample")
  .getOrCreate()

// 假设你有一个 DataFrame 叫做 data，包含了需要存储的数据
val data = spark.read.json("hdfs://path_to_your_data/data.json")

// 使用 partitionBy() 方法将数据按照多个字段的不同值进行分区存储
data.write
  .partitionBy("partition_column1", "partition_column2")
  .format("parquet")  // 指定数据格式，比如 Parquet
  .save("hdfs://path_to_save_data/")

```

在上述代码中，`partitionBy("partition_column1", "partition_column2")` 指定了要根据多个字段进行分区存储。 这样，数据就会根据字段 `partition_column1` 和 `partition_column2` 的不同值被存储到不同的目录中。

## 示例

假设你有如下一个数据表 `employees`：

|id|name|department|salary
|------
|1|Alice|HR|50000
|2|Bob|IT|60000
|3|Charlie|IT|55000
|4|David|Marketing|45000
|5|Eve|Marketing|70000

现在，假设你想要按照 `department` 和 `salary` 两个字段进行分区存储到 HDFS 上，那么你可以使用以下代码：

```
import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder()
  .appName("MultiPartitionedWriteExample")
  .getOrCreate()

val employees = Seq(
  (1, "Alice", "HR", 50000),
  (2, "Bob", "IT", 60000),
  (3, "Charlie", "IT", 55000),
  (4, "David", "Marketing", 45000),
  (5, "Eve", "Marketing", 70000)
).toDF("id", "name", "department", "salary")

employees.write
  .partitionBy("department", "salary")
  .format("parquet")
  .save("hdfs://path_to_save_data/employees")

```

通过上述代码，数据将被按照 `department` 和 `salary` 进行分区，最终存储在 HDFS 中的目录结构如下：

```
hdfs://path_to_save_data/employees/
├── department=HR
│   ├── salary=50000
│   │   └── part-00000-x.snappy.parquet
│   └── _SUCCESS
├── department=IT
│   ├── salary=55000
│   │   └── part-00000-x.snappy.parquet
│   ├── salary=60000
│   │   └── part-00000-x.snappy.parquet
│   └── _SUCCESS
├── department=Marketing
│   ├── salary=45000
│   │   └── part-00000-x.snappy.parquet
│   ├── salary=70000
│   │   └── part-00000-x.snappy.parquet
│   └── _SUCCESS
└── _SUCCESS

```

在上述目录结构中，每个分区字段的值都会对应一个目录，其中包含了该分区值对应的数据文件。

例如，第一个分区字段是 `department`，那么数据将按照不同的部门名称存储到对应的目录下，每个部门目录下又会根据第二个分区字段 `salary` 的不同值再进行子目录的划分。

需要注意的是，对于大量的数据和分区字段，需要谨慎地选择分区字段，以免导致过多的小文件。
