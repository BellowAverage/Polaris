
--- 
title:  如何使用PyQuery库？ 
tags: []
categories: [] 

---
PyQuery是一个类似于jQuery的Python库，它提供了一种可用于解析和操作HTML文档的强大工具。如何使用PyQuery库呢，下面是使用PyQuery库的详细说明：

### 安装PyQuery

PyQuery库可以通过pip安装。在终端中运行以下命令即可安装：

```
pip install pyquery

```

### 导入PyQuery

要使用PyQuery，需要导入该库。可以使用以下代码导入PyQuery：

```
from pyquery import PyQuery as pq

```

### <img alt="" height="387" src="https://img-blog.csdnimg.cn/6b6404be4a934d46afee4f9512dca201.png" width="576">

 

### 获取HTML文档

使用`pq()`函数初始化HTML文档，可以从以下几种不同的来源获取HTML文档：

 - URL
 - 文件
 - 字符串

以下是示例：

#### 从URL获取HTML文档

```
doc = pq(url='http://www.baidu.com')
print(doc('title'))

```

#### 从文件获取HTML文档

```
doc = pq(filename='example.html')
print(doc('title'))

```

#### 从字符串获取HTML文档

```
doc = pq('&lt;html&gt;&lt;head&gt;&lt;
```
