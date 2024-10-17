
--- 
title:  [sparkSQL] Shuffle 
tags: []
categories: [] 

---
在Spark SQL中，Shuffle 是指将数据重新分布到不同的节点上以进行处理的操作。在 Spark SQL 中，以下是一些可能触发 Shuffle 的操作或代码：
<li> **`group by` 和 `aggregations`：** 
  1. 当使用 `GROUP BY` 或聚合函数（如 `SUM`、`AVG`）时，Spark 通常需要将数据重新分发到不同的节点上，以便执行合并操作。 <pre><code class="prism language-sql">SELECT department, AVG(salary) FROM employees GROUP BY department
</code></pre> </li><li> **`join` 操作：** 
  1. `JOIN` 操作可能需要将两个数据集的相应分区重新分发到相同的节点上，以便执行连接操作。 <pre><code class="prism language-sql">SELECT * FROM employees JOIN departments ON employees.department_id = departments.department_id
</code></pre> </li><li> **窗口函数（Window Functions）：** 
  1. 使用窗口函数时，Spark 可能需要重新组织数据以进行窗口聚合。 <pre><code class="prism language-sql">SELECT department, salary, AVG(salary) OVER (PARTITION BY department ORDER BY salary) as avg_salary FROM employees
</code></pre> </li><li> **`distinct` 操作：** 
  1. 当使用 `DISTINCT` 时，Spark 可能需要将数据重新分区以识别并删除重复的值。 <pre><code class="prism language-sql">SELECT DISTINCT department FROM employees
</code></pre> </li><li> **`repartition` 和 `coalesce`：** 
  1. 手动调整分区数量的操作，例如使用 `repartition` 或 `coalesce`，也可能触发 Shuffle。 <pre><code class="prism language-scala">val repartitionedDF = df.repartition(10, col("department"))
</code></pre> </li>- `JOIN` 操作可能需要将两个数据集的相应分区重新分发到相同的节点上，以便执行连接操作。- 当使用 `DISTINCT` 时，Spark 可能需要将数据重新分区以识别并删除重复的值。
请注意，Shuffle 操作是开销较大的操作，因为它涉及数据的物理移动和网络通信。在 Spark 中，尽量减少 Shuffle 操作可以提高性能。可以通过合理设计数据分区、使用广播变量、使用合适的数据结构等方式来减少 Shuffle 的发生。
