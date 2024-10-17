
--- 
title:  Python学习笔记第二十六天(JSON) 
tags: []
categories: [] 

---


#### Python学习笔记第二十六天
- - <ul><li>- - - <ul><li>


## 使用JSON

本章节我们将为大家介绍如何使用 Python 语言来编码和解码 JSON 对象。

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。

### JSON 函数

使用 JSON 函数需要导入 json 库：**import json**。

|函数|描述
|------
|json.dumps|将 Python 对象编码成 JSON 字符串
|json.loads|将已编码的 JSON 字符串解码为 Python 对象

### json.dumps

json.dumps 用于将 Python 对象编码成 JSON 字符串。

```
# 实例 1
import json  
  
data = [ {<!-- --> 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]  
  
data2 = json.dumps(data)  
print(data2)

```

```
# 实例 2
import json  
  
data = [ {<!-- --> 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]  
  
data2 = json.dumps({<!-- -->'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))  
print(data2)

```

python 原始类型向 json 类型的转化对照表：

|Python|JSON
|------
|dict|object
|list, tuple|array
|str, unicode|string
|int, long, float|number
|True|true
|False|false
|None|null

### json.loads

json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。

```
# 实例 3
import json  
  
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';  
  
text = json.loads(jsonData)  
print(text)

```

json 类型转换到 python 的类型对照表：

|JSON|Python
|------
|object|dict
|array|list
|string|unicode
|number (int)|int, long
|number (real)|float
|true|True
|false|False
|null|None

## 使用第三方库：Demjson

Demjson 是 python 的第三方模块库，可用于编码和解码 JSON 数据，包含了 JSONLint 的格式化及校验功能。

Github 地址：

官方地址：

#### 环境配置

在使用 Demjson 编码或解码 JSON 数据前，我们需要先安装 Demjson 模块。本教程我们会下载  并安装：

```
$ tar -xvzf demjson-2.2.3.tar.gz
$ cd demjson-2.2.3
$ python setup.py install

```

更多安装介绍查看：

### JSON 函数

|函数|描述
|------
|encode|将 Python 对象编码成 JSON 字符串
|decode|将已编码的 JSON 字符串解码为 Python 对象

### encode

Python encode() 函数用于将 Python 对象编码成 JSON 字符串。

```
# 实例 4
import demjson  
  
data = [ {<!-- --> 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]  
  
json = demjson.encode(data)  
print(json)

```

### decode

Python 可以使用 demjson.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型。

```
# 实例 5
import demjson  
  
json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';  
  
text = demjson.decode(json)  
print(text)

```

## 结束语

今天学习的是Python线程学会了吗。 今天学习内容总结一下：
1. 使用JSON1. 使用第三方库：Demjson