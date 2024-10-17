
--- 
title:  Python学习笔记第五十六（Pandas JSON） 
tags: []
categories: [] 

---


#### Python学习笔记第五十六天
- - <ul><li>- - - 


## Pandas JSON

JSON（JavaScript Object Notation，JavaScript 对象表示法），是存储和交换文本信息的语法，类似 XML。

JSON 比 XML 更小、更快，更易解析，更多 JSON 内容可以参考 JSON 教程。

Pandas 可以很方便的处理 JSON 数据，本文以 sites.json 为例，内容如下：

```
[
   {<!-- -->
   "id": "A001",
   "name": "百度",
   "url": "www.baidu.com",
   "likes": 95
   },
   {<!-- -->
   "id": "A002",
   "name": "Google",
   "url": "www.google.com",
   "likes": 112
   },
   {<!-- -->
   "id": "A003",
   "name": "淘宝",
   "url": "www.taobao.com",
   "likes": 66
   }
]

```

### read_json()

```
# 实例 1
import pandas as pd
df = pd.read_json('sites.json')
print(df.to_string())

```

### to_string()

to_string() 用于返回 DataFrame 类型的数据，我们也可以直接处理 JSON 字符串。

```
# 实例 2
import pandas as pd
data =[
   {<!-- -->
   "id": "A001",
   "name": "百度",
   "url": "www.baidu.com",
   "likes": 95
   },
   {<!-- -->
   "id": "A002",
   "name": "Google",
   "url": "www.google.com",
   "likes": 112
   },
   {<!-- -->
   "id": "A003",
   "name": "淘宝",
   "url": "www.taobao.com",
   "likes": 66
   }
]
df = pd.DataFrame(data)
print(df)

```

### 字典转为 DataFrame 数据

JSON 对象与 Python 字典具有相同的格式，所以我们可以直接将 Python 字典转化为 DataFrame 数据：

```
# 实例 3
import pandas as pd
# 字典格式的 JSON                                                                                              
s = {<!-- -->
    "col1":{<!-- -->"row1":1,"row2":2,"row3":3},
    "col2":{<!-- -->"row1":"x","row2":"y","row3":"z"}
}
# 读取 JSON 转为 DataFrame                                                                                          
df = pd.DataFrame(s)
print(df)

```

## 内嵌的 JSON 数据

假设有一组内嵌的 JSON 数据文件 nested_list.json ： nested_list.json 文件内容

```
{<!-- -->
    "school_name": "ABC primary school",
    "class": "Year 1",
    "students": [
    {<!-- -->
        "id": "A001",
        "name": "Tom",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {<!-- -->
        "id": "A002",
        "name": "James",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {<!-- -->
        "id": "A003",
        "name": "Jenny",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}

```

使用以下代码格式化完整内容：

```
# 实例 4
import pandas as pd
df = pd.read_json('nested_list.json')
print(df)

```

### json_normalize()

这时我们就需要使用到 json_normalize() 方法将内嵌的数据完整的解析出来：

```
# 实例 5
import pandas as pd
import json
# 使用 Python JSON 模块载入数据
with open('nested_list.json','r') as f:
    data = json.loads(f.read())
# 展平数据
df_nested_list = pd.json_normalize(data, record_path =['students'])
print(df_nested_list)

```

`data = json.loads(f.read()) `使用 Python JSON 模块载入数据。

`json_normalize() `使用了参数 record_path 并设置为 [‘students’] 用于展开内嵌的 JSON 数据 students。

显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据：

```
# 实例 6
import pandas as pd
import json
# 使用 Python JSON 模块载入数据
with open('nested_list.json','r') as f:
    data = json.loads(f.read())
# 展平数据
df_nested_list = pd.json_normalize(
    data,
    record_path =['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)

```

接下来，让我们尝试读取更复杂的 JSON 数据，该数据嵌套了列表和字典，数据文件 nested_mix.json 如下：

nested_mix.json 文件内容

```
{<!-- -->
    "school_name": "local primary school",
    "class": "Year 1",
    "info": {<!-- -->
      "president": "John Kasich",
      "address": "ABC road, London, UK",
      "contacts": {<!-- -->
        "email": "admin@e.com",
        "tel": "123456789"
      }
    },
    "students": [
    {<!-- -->
        "id": "A001",
        "name": "Tom",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {<!-- -->
        "id": "A002",
        "name": "James",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {<!-- -->
        "id": "A003",
        "name": "Jenny",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}

```

nested_mix.json 文件转换为 DataFrame：

```
# 实例 7
import pandas as pd
import json
# 使用 Python JSON 模块载入数据
with open('nested_mix.json','r') as f:
    data = json.loads(f.read())   
df = pd.json_normalize(
    data,
    record_path =['students'],
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)
print(df)

```

读取内嵌数据中的一组数据 以下是实例文件 nested_deep.json，我们只读取内嵌中的 math 字段：

nested_deep.json 文件内容

```
{<!-- -->
    "school_name": "local primary school",
    "class": "Year 1",
    "students": [
    {<!-- -->
        "id": "A001",
        "name": "Tom",
        "grade": {<!-- -->
            "math": 60,
            "physics": 66,
            "chemistry": 61
        }
 
    },
    {<!-- -->
        "id": "A002",
        "name": "James",
        "grade": {<!-- -->
            "math": 89,
            "physics": 76,
            "chemistry": 51
        }
       
    },
    {<!-- -->
        "id": "A003",
        "name": "Jenny",
        "grade": {<!-- -->
            "math": 79,
            "physics": 90,
            "chemistry": 78
        }
    }]
}

```

这里我们需要使用到 glom 模块来处理数据套嵌，glom 模块允许我们使用 . 来访问内嵌对象的属性。

第一次使用我们需要安装 glom：

```
pip3 install glom

```

正确地使用了 glom 模块来从嵌套的 JSON 数据中提取字段

```
# 实例 8
import pandas as pd
from glom import glom
df = pd.read_json('nested_deep.json')
data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)

```

以下是对代码的详细解释：
- 首先，我们导入了 pandas 和 glom 模块。pandas 是一个用于数据操作和分析的 Python 库，而 glom 是一个用于操作和解析 JSON 数据的库。- 然后，我们使用 pandas 的 read_json 函数读取了一个名为 ‘nested_deep.json’ 的 JSON 文件。这个文件包含了一些有关学生和他们的成绩的信息。- 我们创建了一个名为 data 的变量，并使用 apply 函数和 lambda 函数来遍历 df[‘students’] 列中的每一行。对于每一行，我们使用 glom 函数来提取该行的 ‘grade’ 对象中的 ‘math’ 字段。- 最后，我们打印了 data 变量，这个变量应该包含了所有学生的数学成绩。
>  
 如果您运行这段代码，并确保您的环境已经安装了 pandas 和 glom，那么应该会看到一个包含所有学生数学成绩的列表。 


## 后记

今天学习的是Python Pandas JSON学会了吗。 今天学习内容总结一下：
1. Pandas JSON1. read_json()1. to_string()1. 字典转为 DataFrame 数据1. 内嵌的 JSON 数据1. json_normalize()