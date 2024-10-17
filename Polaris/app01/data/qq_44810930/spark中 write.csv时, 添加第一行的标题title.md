
--- 
title:  spark中 write.csv时, 添加第一行的标题title 
tags: []
categories: [] 

---
在 Spark 中使用 `write.csv` 写入 CSV 文件时，默认情况下是不会在文件中添加标题行的。但是，你可以通过设置 `header` 选项来控制是否包含标题行。

下面是一个示例：

```
val data = Seq(
  (1, "John", 28),
  (2, "Alice", 22),
  (3, "Bob", 32)
)

val columns = Seq("id", "name", "age")

val df = data.toDF(columns: _*)

df.write
  .options(Map("header" -&gt; "true", "encoding" -&gt; "UTF-8"))
  .csv("/path/to/output")

```
- `"header" -&gt; "true"` 添加标题- `"encoding" -&gt; "UTF-8"` 中文
如果 `header` 选项设置为 `false` 或省略，默认情况下将不包含标题行。

请注意，`header` 选项适用于多种文件格式，不仅仅是 CSV。你可以使用相同的方法在其他格式（例如 Parquet、JSON 等）中添加或禁用标题。
