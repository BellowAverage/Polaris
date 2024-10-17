
--- 
title:  [spark] dataframe的数据导入Mysql5.6 
tags: []
categories: [] 

---
在 Spark 项目中使用 Scala 连接 **MySQL 5.6** 并将 DataFrame 中的数据保存到 MySQL 中的步骤如下：
<li> **添加 MySQL 连接驱动依赖：** 在 Spark 项目中，你需要在项目的构建工具中添加 MySQL 连接驱动的依赖。 如果使用 Maven，可以在 `pom.xml` 文件中添加以下行： <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;mysql&lt;/groupId&gt;
    &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
    &lt;version&gt;5.1.48&lt;/version&gt;
&lt;/dependency&gt;
</code></pre> 然后，确保重新构建项目以获取新的依赖。 </li><li> **连接 MySQL 并读取数据到 DataFrame：** 使用 SparkSession 来连接 MySQL 并读取数据到 DataFrame。以下是一个简单的示例： <pre><code class="prism language-scala">import org.apache.spark.sql.{<!-- -->SparkSession, SaveMode}

val spark = SparkSession.builder
  .appName("Spark MySQL Example")
  .master("local")
  .getOrCreate()

// MySQL 连接信息
val jdbcUrl = "jdbc:mysql://your_mysql_host:3306/your_database"
val connectionProperties = new java.util.Properties()
connectionProperties.put("user", "your_username")
connectionProperties.put("password", "your_password")
connectionProperties.put("driver", "com.mysql.jdbc.Driver")
connectionProperties.put("characterEncoding", "UTF-8")


// 读取 MySQL 数据到 DataFrame
val df = spark.read.jdbc(jdbcUrl, "your_table_name", connectionProperties)

// 显示 DataFrame 数据
df.show()

// 关闭 SparkSession
spark.stop()
</code></pre> 请替换以下内容： 
  1. `your_mysql_host`：MySQL 主机地址1. `your_database`：数据库名称1. `your_username`：MySQL 用户名1. `your_password`：MySQL 密码1. `your_table_name`：要读取的表名 </li><li> **将 DataFrame 中的数据保存到 MySQL：** 使用 `write.jdbc` 将 DataFrame 中的数据保存到 MySQL。以下是一个示例： <pre><code class="prism language-scala">// 将 DataFrame 写入 MySQL（Overwrite 模式，可以根据需求选择其他模式）
df.write
  .mode(SaveMode.Overwrite)
  .jdbc(jdbcUrl, "your_table_name", connectionProperties)
</code></pre> 请根据你的需求调整保存模式和表名。 </li>
这样，你就可以在 Spark 项目中使用 Scala 连接 MySQL 5.6 并进行数据的读取和写入。
