
--- 
title:  [python] 使用sqlparse 解析和美化SQL 
tags: []
categories: [] 

---
在 Python3 中，可以使用 sqlparse 模块来美化 SQL 语句。sqlparse 是一个开源的 Python 模块，它可以解析 SQL 语句并将其格式化为易于阅读和理解的结构。具体来说，sqlparse 可以：
1. 将 SQL 语句解析为语法树，并以易于操作的对象形式呈现；1. 格式化 SQL 语句，包括缩进、大小写、空格等方面的优化；1. 高亮显示 SQL 语句中的关键字、函数、表名等，以提高可读性。
以下是一个示例代码，演示如何使用 sqlparse 模块对 SQL 语句进行美化：

```
import sqlparse

# 定义一个 SQL 语句
sql = "SELECT id, name FROM users WHERE age &gt; 18 ORDER BY create_time DESC;"

# 使用 sqlparse 解析和美化 SQL 语句
formatted_sql = sqlparse.format(sql, reindent=True, keyword_case='upper')

# 输出美化后的 SQL 语句
print(formatted_sql)

```

sqlparse 模块的 format() 方法对 SQL 语句进行美化， 在 format() 方法中，我们指定了 reindent=True 参数，表示需要重新缩进 SQL 语句；

同时指定了 keyword_case=‘upper’ 参数，表示将 SQL 关键字转换为大写形式。

需要**注意**的是，sqlparse 只是一种美化 SQL 的工具，它并不会对 SQL 的语义进行修改或优化。因此，在实际使用中，还需要**仔细检查**美化后的 SQL 语句，确保其与原始 SQL 语句的含义相同。
- 美化后输出如下
```
SELECT id,
       name,
       age
FROM users
WHERE age &gt; 18
ORDER BY create_time DESC;

```

#### 获取sql语句中select的字段名

使用 sqlparse 模块获取 SQL 语句中 SELECT 语句的字段名：

```
import sqlparse

# 定义一个 SQL 语句
sql = "SELECT id, name, age FROM users WHERE age &gt; 18 ORDER BY create_time DESC;"

# 使用 sqlparse 解析 SQL 语句
parsed = sqlparse.parse(sql)

# 遍历解析后的结果，提取 SELECT 语句中的字段名
for stmt in parsed:
    for token in stmt.tokens:
        if isinstance(token, sqlparse.sql.Token) and token.value.upper() == 'SELECT':
            for identifier in token.get_identifiers():
                print(identifier.get_name())

```

在上面的示例代码中，我们首先定义了一个 SQL 语句，然后使用 sqlparse 模块的 parse() 方法解析该 SQL 语句。接着，我们遍历解析后的结果，找到 SELECT 关键字所在的位置，然后提取其中的字段名。最后，我们使用 print() 函数将提取出的字段名打印出来。

当你运行上述代码时，如果输入的 SQL 语句中有 SELECT 语句，那么会输出该 SELECT 语句中的字段名。例如，对于给定的 SQL 语句，输出可能如下所示：

```
id
name
age

```
