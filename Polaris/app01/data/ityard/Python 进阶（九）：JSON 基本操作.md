
--- 
title:  Python 进阶（九）：JSON 基本操作 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- - <ul><li>- - - 


### 1. 概述

JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，它具有简洁、清晰的层次结构，易于阅读和编写，还可以有效的提升网络传输效率。Python 标准库的 json 模块可以用来处理 JSON 格式数据的基本操作。

### 2. 使用

json 模块主要提供了 dump、dumps、load、loads 方法对 JSON 数据进行编解码。

#### 2.1 dumps

json 模块的 dumps 方法可以将 Python 对象转为 JSON 格式字符串，以字典格式为例，看个示例：

```
import json

d = {<!-- -->'id':'001', 'name':'张三', 'age':'20'}
j = json.dumps(d, ensure_ascii=False)
print(j)

```

执行结果：

```
{<!-- -->"id": "001", "name": "张三", "age": "20"}

```

我们发现上面的输出结果并不是格式化的 JSON，dumps 方法还可以对数据进行格式化，如下所示：

```
import json

d = {<!-- -->'id':'001', 'name':'张三', 'age':'20'}
j = json.dumps(d, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
print(j)

```

执行结果：

```
{<!-- -->
    "age": "20",
    "id": "001",
    "name": "张三"
}

```

当然，除了字典类型外，其他一些 Python 类型也可转成 JSON 格式的字符串，它们之间有对应关系如下所示：

<th align="left">Python</th><th align="left">JSON</th>
|------
<td align="left">dict</td><td align="left">object</td>
<td align="left">list, tuple</td><td align="left">array</td>
<td align="left">str</td><td align="left">string</td>
<td align="left">iint, float, int 和 float 派生的枚举</td><td align="left">number</td>
<td align="left">True</td><td align="left">true</td>
<td align="left">False</td><td align="left">false</td>
<td align="left">None</td><td align="left">null</td>

再来看一下如何将 JSON 数据写入文件：

```
import json

d = {<!-- -->'id':'001', 'name':'张三', 'age':'20'}
j = json.dumps(d, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
with open('test.json', 'w', encoding='utf-8') as f:
    f.write(j)

```

#### 2.2 dump

json 模块的 dump 方法可以将 Python 对象序列化为 JSON 格式化流形式的文件类对象。

如果我们需要将数据写到文件里的时候，dump 方法会比 dumps 方法方便一点，看一下示例：

```
import json

d = {<!-- -->'id':'001', 'name':'张三', 'age':'20'}
with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=4, ensure_ascii=False)

```

如果我们需要的数据格式为 JSON 格式字符串时，比如：将数据存入数据库，这时则需要用 dumps 方法。

#### 2.3 loads

json 模块的 loads 方法可以将 JSON 格式数据转为 Python 对象，看个示例：

```
import json

j = '{"id":"001", "name":"张三", "age":"20"}'
d = json.loads(j)
print(d)

```

执行结果：

```
{<!-- -->'id': '001', 'name': '张三', 'age': '20'}

```

两者之间转换的对应关系如下所示：

<th align="left">JSON</th><th align="left">Python</th>
|------
<td align="left">object</td><td align="left">dict</td>
<td align="left">array</td><td align="left">list</td>
<td align="left">string</td><td align="left">str</td>
<td align="left">number (int)</td><td align="left">int</td>
<td align="left">number (real)</td><td align="left">float</td>
<td align="left">true</td><td align="left">True</td>
<td align="left">false</td><td align="left">False</td>
<td align="left">null</td><td align="left">None</td>

我们再来读取一下之前生成的 test.json 中数据并将其转为 Python 对象，如下所示：

```
import json

with open('test.json', encoding='utf-8') as f:
    data = f.read()
    print(json.loads(data))

```

执行结果：

```
{<!-- -->'id': '001', 'name': '张三', 'age': '20'}

```

#### 2.4 load

json 模块的 load 方法将文件类对象转为 Python 对象，看个示例：

```
import json

with open('test.json', encoding='utf-8') as f:
    print(json.load(f))

```

执行结果：

```
{<!-- -->'id': '001', 'name': '张三', 'age': '20'}

```

我们可以看出 load 方法传的参数是文件对象，而 loads 方法参数传的是字符串。

<img src="https://img-blog.csdnimg.cn/20200215093746977.png#pic_center" alt="" width="500">
