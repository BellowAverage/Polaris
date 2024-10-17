
--- 
title:  python判断一个字段是否是mongo ObjectId类型 
tags: []
categories: [] 

---
MongoDB中有一个自动生成的字段：”_id”，类型为ObjectId。

在某些业务中，需要提前判断这个某个字段是否是合法的ObjectId。

此处可以直接使用bson包中的校验方法。详细使用方法可以直接查看该方法的源码。

```
from bson import objectid

# 合法的
a = '5349b4ddd2781d08c09890f4'

# 有问题的
b = "6274da523946a702a7f3b523d"

# 返回值为True
print(objectid.ObjectId.is_valid(a))

# 返回值为False
print(objectid.ObjectId.is_valid(b))
```


