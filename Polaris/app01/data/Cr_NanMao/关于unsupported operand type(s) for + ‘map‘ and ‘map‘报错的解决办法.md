
--- 
title:  关于unsupported operand type(s) for +: ‘map‘ and ‘map‘报错的解决办法 
tags: []
categories: [] 

---
在学习《python计算机视觉》书中的8.3.1 中，有一段源代码是

```
class_1 = map(list, class_1)
class_2 = map(list, class_2)
labels = list(labels)
samples = class_1 + class_2  # concatenate the two lists
```

在运行程序后会弹出：unsupported operand type(s) for +: 'map' and 'map'的报错，出错指向在：samples = class_1 + class_2 这行代码中。经过研究，发现是python版本问题，我用的是python3，书里用的是python2。而在python2中，返回的是一个`list`类型数据，在python3中该语句返回的是一个`map`类型的数据。需要将

>  
 **class_1 = map(list, class_1) class_2 = map(list, class_2)** 


转换成list类型，即：



>  
 <pre><em>class_1 = list(map(list, class_1))
class_2 = list(map(list, class_2))</em>
</pre> 


运行之后问题就解决了。

----今天不学习，明天变废物。----
