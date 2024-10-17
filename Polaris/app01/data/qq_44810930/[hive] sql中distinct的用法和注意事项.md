
--- 
title:  [hive] sql中distinct的用法和注意事项 
tags: []
categories: [] 

---
在 Hive SQL 中，`DISTINCT` 用于去重查询结果中的行。它返回唯一的行，消除结果集中的重复项。以下是 `DISTINCT` 的基本用法和一些注意事项：

#### 基本用法：

```
-- 获取列1和列2的唯一组合
SELECT DISTINCT column1, column2 FROM your_table;

-- 获取整个表的唯一行
SELECT DISTINCT * FROM your_table;

```

#### 注意事项：
<li> **DISTINCT 和 NULL：** `DISTINCT` 关键字会将包含 NULL 值的行视为相等，因此在去重时会将其中的一行过滤掉。如果你想要包含 NULL 值，需要使用 `IS NULL` 或 `IS NOT NULL` 条件。 <pre><code class="prism language-sql">-- 包含 NULL 值的情况
SELECT DISTINCT column1 FROM your_table WHERE column2 IS NULL;
</code></pre> </li><li> **多列的去重：** `DISTINCT` 可以同时应用于多列，返回唯一的组合。 <pre><code class="prism language-sql">SELECT DISTINCT column1, column2 FROM your_table;
</code></pre> </li><li> **排序和去重：** `DISTINCT` 不会对结果进行排序。如果需要排序，可以在查询中使用 `ORDER BY` 子句。 <pre><code class="prism language-sql">-- 获取按照 column1 排序的唯一行
SELECT DISTINCT * FROM your_table ORDER BY column1;
</code></pre> </li><li> **性能注意事项：** 在大型数据集上使用 `DISTINCT` 可能涉及到数据的全局排序和去重，可能会导致性能开销较大。在某些情况下，你可能需要考虑其他方式来达到相似的效果，例如使用 `GROUP BY`。 <pre><code class="prism language-sql">-- 使用 GROUP BY 达到去重效果
SELECT column1, MAX(column2) AS column2 FROM your_table GROUP BY column1;
</code></pre> </li>
总体而言，`DISTINCT` 是在 Hive SQL 中用于去重的常见关键字，但在处理大数据集时，你可能需要考虑性能方面的影响，并根据实际需求选择合适的方法。
