
--- 
title:  [python] dict类型变量写在文件中 
tags: []
categories: [] 

---
在Python中，如果你想要将一个字典变量以具有可读性的格式写入文件，并且指定缩进为2个空格，你可以使用`json`模块来实现。`json`模块提供了一种很方便的方法来进行序列化和反序列化Python对象。下面是一个具体的示例：

## 字典变量以具有可读性的格式写入文件

```
import json

# 假设这是你想要写入文件的字典
data = {<!-- -->
  'name': '张三',
  'age': 30,
  'is_student': False,
  'courses': ['计算机科学', '数据分析']
}

# 指定要写入的文件名
filename = 'data.json'

# 写入文件
with open(filename, 'w', encoding='utf-8') as f:
    # 使用json.dump()函数将字典写入文件，指定缩进为2个空格
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'字典已成功写入到文件 {<!-- -->filename}')

```

这段代码首先导入了`json`模块，然后定义了一个字典`data`，该字典包含了一些键值对。使用`open()`函数以写入模式(`'w'`)打开一个文件，并通过`json.dump()`函数将字典写入该文件。

在`json.dump()`函数中，`ensure_ascii=False`参数确保了非ASCII字符（如中文）能够正确地写入文件，而`indent=2`参数则指定了输出的格式应该有2个空格的缩进，使得最终写入文件的内容具有较好的可读性。

执行上述代码后，你会在当前目录下创建一个名为`data.json`的文件，文件内容将是格式化后的JSON，类似于：

```
{<!-- -->
  "name": "张三",
  "age": 30,
  "is_student": false,
  "courses": [
    "计算机科学",
    "数据分析"
  ]
}

```

这样，你就成功地将一个Python字典以可读的格式并且缩进为2个空格写入到了一个文件中。

## TypeError: Object of type set is not JSON serializable


