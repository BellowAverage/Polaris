
--- 
title:  [hive] 在hive sql中定义变量 
tags: []
categories: [] 

---
在Hive SQL中，可以使用`SET`命令来定义变量。

变量可以用于存储和引用常量或表达式的值，以便在查询中重复使用。

下面是定义和使用变量的示例：

```
-- 定义一个变量
SET my_var = 'Hello, World!';

-- 在查询中使用变量
SELECT * FROM my_table WHERE column = ${my_var};

```
- 使用`SET`命令定义了一个名为`my_var`的变量，- 在查询中使用`${my_var}`引用变量。这样，变量的值将被替换为实际的字符串，从而执行相应的查询操作。
```
-- 列出当前会话中定义的所有变量
SET;

-- 查看特定变量的值
SET my_var;

```

Hive中的变量是会话级别的，即它们在会话结束后会被重置。
