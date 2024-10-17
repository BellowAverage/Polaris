
--- 
title:  arangodb的使用-个人笔记 
tags: []
categories: [] 

---
### 参考文档

**了解数据模型对象**

参考，熟悉数据库、集合、文档及图

**函数**

参考，熟悉函数的功能

**学习AQL查询语言**

参考，了解AQL的语法



**图Graphs**

参考，学习图的知识

A、

B、

C、

**Spring集成ArangoDB**

参考

### ArangoSearch数据搜索学习笔记

1、视图View



2、分析器 Analyzers



3、搜索函数 ArangoSearch Functions



4、

### ArangoSearch的模糊搜索实现

在arangodb 3.7版本之后，增加了几个模糊搜索相关的函数，具体参考以下文章：



模糊搜索函数的文档介绍：  

其中较常用的函数是：

NGRAM_MATCH()

函数定义：

NGRAM_MATCH(path, target, threshold, analyzer)
- path 要匹配的“数据”，可以为某文档里的字段或者一串字符串- target 用于搜索的字符，只能为字符串数据- threshold : 精确度，值范围为 0.0 - 1.0. 如果不设置则为默认值 0.7- analyzer (string): 分词器的名称， 分词器要求为ngram类型的分词器，且采用bigram定义
```
"bigram" (min: 2, max: 2, preserveOriginal: false, streamType: "utf8", features:["position", "frequency", "norm"] )

```

关于bigram分词器的定义说明，也可以

查询例子:

```

FOR doc IN viewName
  SEARCH NGRAM_MATCH(doc.text, "quick fox", "bigram")
  RETURN doc.text

```

### 实战

**根据日期计算年龄**

```
for ui in UserInfo
for us in UserStatus
filter ui._key == us._key
sort rand()
limit 1
let age = FLOOR(DATE_DIFF(ui.birthday,DATE_NOW(),"d")/365.2425)
return {<!-- --> age:age,key:ui._key,birthday:ui.birthday,nickName:ui.nickName }

FLOOR(DATE_DIFF(ui.birthday,DATE_NOW(),"d")/365.2425)

```

>  
 执行效果 


<img src="https://img-blog.csdnimg.cn/20210623180641731.png" alt="在这里插入图片描述">
