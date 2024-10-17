
--- 
title:  [spark] RDD, DataFrame和DataSet是什么?如何相互转化 
tags: []
categories: [] 

---


#### 文章目录
- - 


## 是什么

在 Apache Spark 中，RDD（Resilient Distributed Dataset）、DataFrame 和 Dataset 是三个不同的数据抽象层，各自有不同的特点和用途。
<li> **RDD（Resilient Distributed Dataset）：** 
  1. RDD 是 Spark 最基本的抽象，表示分布在集群节点上的不可变、可弹性恢复的数据集。1. RDD 提供了一系列转换操作（transformation）和行动操作（action）来处理数据。转换操作会创建一个新的 RDD，而行动操作会返回结果或将数据写入外部存储。1. RDD 编程风格是面向函数的，并且对类型的要求较弱，适用于较低层次的数据处理和计算。 </li><li> **DataFrame：** 
  1. DataFrame 是在 Spark 1.3 引入的更高层次的抽象，构建在 RDD 之上，提供了更丰富的结构化数据处理能力。1. DataFrame 是以类似关系型数据库表的形式组织的分布式数据集合，每列都有名称和数据类型。1. Spark 提供了一系列的 DataFrame 操作，包括 SQL 查询、过滤、聚合等，而且可以利用 Catalyst 引擎进行优化执行计划。1. DataFrame 通常比 RDD 更易于使用，特别是在执行结构化查询时。 </li><li> **Dataset：** 
  1. Dataset 是 Spark 1.6 引入的抽象，它是 DataFrame 的扩展，提供了类型安全的编程接口。1. Dataset 支持强类型的编程语言（如 Scala 和 Java），并在编译时进行类型检查，提供更好的性能和更好的错误检测。1. Dataset 同时提供了 DataFrame 的结构化查询能力，可以通过编程接口或者 SQL 查询进行操作。 </li>- DataFrame 是在 Spark 1.3 引入的更高层次的抽象，构建在 RDD 之上，提供了更丰富的结构化数据处理能力。- DataFrame 是以类似关系型数据库表的形式组织的分布式数据集合，每列都有名称和数据类型。- Spark 提供了一系列的 DataFrame 操作，包括 SQL 查询、过滤、聚合等，而且可以利用 Catalyst 引擎进行优化执行计划。- DataFrame 通常比 RDD 更易于使用，特别是在执行结构化查询时。
简而言之，RDD 是最基本的抽象，DataFrame 是对结构化数据的更高层次抽象，而 Dataset 是在 DataFrame 基础上提供了类型安全性的扩展。在实际使用中，通常优先选择使用 DataFrame 或 Dataset，因为它们更适合进行结构化数据处理和利用 Spark 的优化能力。

## 如何转化

在 Apache Spark 中，可以通过一些方法进行 RDD、DataFrame 和 Dataset 之间的转化。以下是一些示例 Scala 代码，演示了如何进行这些转化：
1. **RDD 转 DataFrame：**
```
import org.apache.spark.sql.{<!-- -->SparkSession, Row}
import org.apache.spark.sql.types.{<!-- -->StructType, StructField, StringType, IntegerType}

val spark = SparkSession.builder
  .appName("RDD to DataFrame")
  .master("local")
  .getOrCreate()

// 创建一个示例 RDD
val rdd = spark.sparkContext.parallelize(Seq(
  Row("John", 25),
  Row("Alice", 30),
  Row("Bob", 28)
))

// 定义结构信息
val schema = StructType(Seq(
  StructField("name", StringType, nullable = true),
  StructField("age", IntegerType, nullable = true)
))

// 创建 DataFrame
val df = spark.createDataFrame(rdd, schema)

// 打印 DataFrame
df.show()

// 关闭 SparkSession
spark.stop()

```
1. **DataFrame 转 RDD：**
```
import org.apache.spark.sql.{<!-- -->SparkSession, Row}

val spark = SparkSession.builder
  .appName("DataFrame to RDD")
  .master("local")
  .getOrCreate()

// 创建一个示例 DataFrame
val df = spark.createDataFrame(Seq(
  ("John", 25),
  ("Alice", 30),
  ("Bob", 28)
)).toDF("name", "age")

// 转换为 RDD
val rdd = df.rdd

// 打印 RDD
rdd.foreach(println)

// 关闭 SparkSession
spark.stop()

```
1. **DataFrame 转 Dataset：**
```
import org.apache.spark.sql.{<!-- -->SparkSession, Encoder}
import org.apache.spark.sql.expressions.Encoder

case class Person(name: String, age: Int)

val spark = SparkSession.builder
  .appName("DataFrame to Dataset")
  .master("local")
  .getOrCreate()

// 创建一个示例 DataFrame
val df = spark.createDataFrame(Seq(
  ("John", 25),
  ("Alice", 30),
  ("Bob", 28)
)).toDF("name", "age")

// 转换为 Dataset
val ds = df.as[Person]

// 打印 Dataset
ds.show()

// 关闭 SparkSession
spark.stop()

```
1. **Dataset 转 DataFrame：**
```
import org.apache.spark.sql.{<!-- -->SparkSession, Encoder}
import org.apache.spark.sql.expressions.Encoder

case class Person(name: String, age: Int)

val spark = SparkSession.builder
  .appName("Dataset to DataFrame")
  .master("local")
  .getOrCreate()

// 创建一个示例 Dataset
val ds = Seq(
  Person("John", 25),
  Person("Alice", 30),
  Person("Bob", 28)
).toDS()

// 转换为 DataFrame
val df = ds.toDF()

// 打印 DataFrame
df.show()

// 关闭 SparkSession
spark.stop()

```

这些示例代码演示了在 Spark 中如何进行 RDD、DataFrame 和 Dataset 之间的基本转化。根据实际需求和数据处理场景，选择适当的数据抽象进行操作。
