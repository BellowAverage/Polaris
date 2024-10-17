
--- 
title:  python多层json结构学习指导 
tags: []
categories: [] 

---
python多层json结构学习指导。网上关于生成多层json结构的比较少，基本都是关于添加元素，解析，怎么转化为json之类的

下面就以文章信息的json为基础来构建多层json。

### 生成最基本的一个json：

```
import json

article_info = {<!-- -->}
data = json.loads(json.dumps(article_info))

data['article1'] = 'NONE'

article = json.dumps(data, ensure_ascii=False)
print(article)


```

<img src="https://img-blog.csdnimg.cn/e2d6eeb7757f4d8692b1fbb9e31cc92b.png" alt="在这里插入图片描述">

### 将一个json嵌套进去：

```
import json

article_info = {<!-- -->}
data = json.loads(json.dumps(article_info))

data['article1'] = 'NONE'

article2 = {<!-- -->'title': 'python基础', 'publish_time': '2019-4-1', 'writer': {<!-- -->}}
data['article2'] = article2

article = json.dumps(data, ensure_ascii=False)
print(article)

```

<img src="https://img-blog.csdnimg.cn/be9f0607b0a64442b206aa7feba60f33.png" alt="在这里插入图片描述">

### 下面将writer的信息(json)插入其中：

```
import json

article_info = {<!-- -->}
data = json.loads(json.dumps(article_info))

data['article1'] = 'NONE'

article2 = {<!-- -->'title': 'python基础', 'publish_time': '2019-4-1', 'writer': {<!-- -->}}
data['article2'] = article2

writer = {<!-- -->'name': '李先生', 'sex': '男', 'email': 'xxx@gmail.com'}
data['article2']['writer'] = writer

article = json.dumps(data, ensure_ascii=False)
print(article)


```

<img src="https://img-blog.csdnimg.cn/dcae5916d4c346f7b2bc66ff03435b5d.png" alt="在这里插入图片描述">
