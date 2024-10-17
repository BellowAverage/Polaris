
--- 
title:  [spark] 将dataframe中的数据插入到mysql 
tags: []
categories: [] 

---


#### 文章目录
- - - - 


## 分区写入 `foreachPartition`

在Spark中，你可以使用`foreachPartition`或`foreach`来将DataFrame中的数据插入到MySQL数据库。以下是一个基本的Scala代码示例，假设你已经创建了一个SparkSession并加载了你的DataFrame：

```
import org.apache.spark.sql.{<!-- -->Row, SparkSession}
import java.sql.{<!-- -->Connection, DriverManager, PreparedStatement}

object SparkToMySQLExample {<!-- -->
  def main(args: Array[String]): Unit = {<!-- -->
    // 创建 SparkSession
    val spark = SparkSession.builder
      .appName("SparkToMySQLExample")
      .getOrCreate()

    // 从数据源创建 DataFrame，这里假设你已经有了一个 DataFrame，用 df 表示
    val df = // ... your DataFrame creation logic ...

    // 定义 MySQL 连接信息
    val jdbcUrl = "jdbc:mysql://your-mysql-host:3306/your-database"
    val jdbcUsername = "your-username"
    val jdbcPassword = "your-password"

    // 定义 MySQL 表名
    val tableName = "your-table"

    // 定义插入数据的 SQL 语句
    val insertQuery = s"INSERT INTO $tableName (column1, column2, ...) VALUES (?, ?, ...)"

    // 将 DataFrame 的数据插入到 MySQL
    df.foreachPartition {<!-- --> partition =&gt;
      // 在每个分区上建立一个数据库连接
      Class.forName("com.mysql.jdbc.Driver")
      val connection: Connection = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)

      // 遍历分区中的每一行数据并执行插入操作
      val preparedStatement: PreparedStatement = connection.prepareStatement(insertQuery)
      partition.foreach {<!-- --> row =&gt;
        // 根据你的 DataFrame 列的顺序设置参数
        preparedStatement.setString(1, row.getString(0))
        preparedStatement.setInt(2, row.getInt(1))
        // ... 设置其他参数 ...

        // 执行插入操作
        preparedStatement.executeUpdate()
      }

      // 关闭连接和声明
      preparedStatement.close()
      connection.close()
    }

    // 停止 SparkSession
    spark.stop()
  }
}

```

请替换示例中的`your-mysql-host`、`your-database`、`your-username`、`your-password`、`your-table`以及列名（`column1`、`column2`等）等信息为你实际使用的值。在实际应用中，请确保数据库连接信息和表结构是正确的，并根据你的数据和表结构调整插入逻辑。

此外，确保你的 Spark 应用程序能够访问 MySQL 驱动程序。你可能需要在启动 Spark 时包含 MySQL 驱动程序的 JAR 文件。

## 直接写入 `write.jdbc()`

`DataFrame.write.jdbc()` 是 Spark 提供的一种更方便的方式，用于将 DataFrame 中的数据写入关系型数据库。这个方法封装了连接数据库、创建表以及插入数据的整个过程，提供了一种更简洁和易用的接口。

与使用 `foreach` 或 `foreachPartition` 直接进行数据插入相比，使用 `write.jdbc()` 有以下优点：
1.  **简洁性和易用性：** `write.jdbc()` 方法抽象了底层的数据库连接和数据插入逻辑，使得代码更加简洁易读。你只需要提供数据库连接信息、表名和DataFrame即可，而不需要手动处理连接、预处理语句等细节。 1.  **性能优化：** Spark 内部会进行一些优化，例如分区数据、并行写入等，以提高插入性能。`write.jdbc()` 方法会在背后进行一些优化，而手动编写 `foreach` 或 `foreachPartition` 可能需要更多的手动调整以实现最佳性能。 
下面是使用 `write.jdbc()` 的简单示例：

```
import org.apache.spark.sql.{<!-- -->SparkSession, SaveMode}

object SparkToMySQLExample {<!-- -->
  def main(args: Array[String]): Unit = {<!-- -->
    val spark = SparkSession.builder
      .appName("SparkToMySQLExample")
      .getOrCreate()

    val df = // ... your DataFrame creation logic ...

    val jdbcUrl = "jdbc:mysql://your-mysql-host:3306/your-database"
    val jdbcUsername = "your-username"
    val jdbcPassword = "your-password"
    val tableName = "your-table"

    df.write
      .mode(SaveMode.Append)  // 保存模式，可以选择 Append、Overwrite、ErrorIfExists 或 Ignore
      .jdbc(jdbcUrl, tableName, new java.util.Properties() {<!-- -->
        put("user", jdbcUsername)
        put("password", jdbcPassword)
      })

    spark.stop()
  }
}

```

在这个例子中，`.mode(SaveMode.Append)` 表示将数据追加到现有表中。你可以根据需要选择不同的保存模式，例如覆盖现有表，如果表不存在则创建新表等。

总体来说，如果你的目标是将 DataFrame 中的数据写入关系型数据库，推荐使用 `write.jdbc()` 方法，因为它更容易使用且通常会有更好的性能。

## 有没有插入成功

在使用`df.write.mode(SaveMode.Append).jdbc()`方式插入数据时，你可以利用Spark的**Action**操作触发数据写入，并检查写入操作是否成功。`write` 操作属于Spark的**Transformation**，它不会立即执行，而是在遇到一个触发执行的**Action**操作时才实际执行。

在Spark中，一些典型的**Action**操作包括 `count()`、`collect()` 等，它们会触发 Spark 作业的执行。

以下是一个简单的示例，演示如何在写入数据后使用 `count()` 来验证插入是否成功：

```
import org.apache.spark.sql.{<!-- -->SparkSession, SaveMode}

object SparkToMySQLExample {<!-- -->
  def main(args: Array[String]): Unit = {<!-- -->
    val spark = SparkSession.builder
      .appName("SparkToMySQLExample")
      .getOrCreate()

    val df = // ... your DataFrame creation logic ...

    val jdbcUrl = "jdbc:mysql://your-mysql-host:3306/your-database"
    val jdbcUsername = "your-username"
    val jdbcPassword = "your-password"
    val tableName = "your-table"

    // 写入数据
    df.write
      .mode(SaveMode.Append)
      .jdbc(jdbcUrl, tableName, new java.util.Properties() {<!-- -->
        put("user", jdbcUsername)
        put("password", jdbcPassword)
      })

    // 触发写入操作后，使用 count() 来验证插入是否成功
    val rowCount = spark.read.jdbc(jdbcUrl, tableName, new java.util.Properties() {<!-- -->
      put("user", jdbcUsername)
      put("password", jdbcPassword)
    }).count()

    println(s"Number of rows in the table after insertion: $rowCount")

    spark.stop()
  }
}

```

在这个例子中，我们使用 `spark.read.jdbc` 读取插入后的表，并使用 `count()` 操作来获取表中的行数。如果插入成功，你应该能够看到插入前后的行数有所增加。

请注意，这种方法有一个缺点，即每次插入后都需要读取整个表，可能会导致性能问题。在生产环境中，可以考虑使用更高效的方法，例如通过其他手段检查数据库中的行数，或者在插入数据时记录插入的行数，并在Spark中进行验证。

## 在插入时记录行数 `累加器`

在Spark中，你可以使用`foreachPartition`或`foreach`操作，结合累加器（Accumulator）来记录插入的行数。累加器是一种分布式变量，可以在任务之间共享和累加值。以下是一个简单的示例，演示如何在Spark中记录插入的行数：

```
import org.apache.spark.sql.{<!-- -->Row, SparkSession}
import java.sql.{<!-- -->Connection, DriverManager, PreparedStatement}

object SparkInsertWithRowCounter {<!-- -->
  def main(args: Array[String]): Unit = {<!-- -->
    val spark = SparkSession.builder
      .appName("SparkInsertWithRowCounter")
      .getOrCreate()

    val df = // ... your DataFrame creation logic ...

    // 定义累加器
    val rowCounter = spark.sparkContext.longAccumulator("rowCounter")

    // 定义 MySQL 连接信息
    val jdbcUrl = "jdbc:mysql://your-mysql-host:3306/your-database"
    val jdbcUsername = "your-username"
    val jdbcPassword = "your-password"
    val tableName = "your-table"

    // 定义插入数据的 SQL 语句
    val insertQuery = s"INSERT INTO $tableName (column1, column2, ...) VALUES (?, ?, ...)"

    // 将 DataFrame 的数据插入到 MySQL，并在插入时累加行数
    df.foreachPartition {<!-- --> partition =&gt;
      // 在每个分区上建立一个数据库连接
      Class.forName("com.mysql.jdbc.Driver")
      val connection: Connection = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)

      // 遍历分区中的每一行数据并执行插入操作
      val preparedStatement: PreparedStatement = connection.prepareStatement(insertQuery)
      partition.foreach {<!-- --> row =&gt;
        // 根据你的 DataFrame 列的顺序设置参数
        preparedStatement.setString(1, row.getString(0))
        preparedStatement.setInt(2, row.getInt(1))
        // ... 设置其他参数 ...

        // 执行插入操作
        preparedStatement.executeUpdate()

        // 累加行数
        rowCounter.add(1)
      }

      // 关闭连接和声明
      preparedStatement.close()
      connection.close()
    }

    // 打印插入的总行数
    println(s"Total rows inserted: ${<!-- -->rowCounter.value}")

    // 停止 SparkSession
    spark.stop()
  }
}

```

在这个例子中，我们创建了一个名为 `rowCounter` 的累加器，并在插入数据时使用 `rowCounter.add(1)` 来累加行数。最后，通过 `rowCounter.value` 获取累加的总行数，并在Spark应用程序中进行验证。

确保替换示例中的 `your-mysql-host`、`your-database`、`your-username`、`your-password`、`your-table` 以及列名（`column1`、`column2`等）等信息为你实际使用的值。
