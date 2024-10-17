
--- 
title:  关于TypeError: write() argument must be str, not bytes报错的解决办法 
tags: []
categories: [] 

---
在学习《python计算机视觉》中，书中有段源代码为

```
from numpy import *
from numpy.random import randn
import pickle

# 创建二维样本数据
n = 200

# 两个正态分布数据集
class_1 = 0.6 * randn(n, 2)
class_2 = 1.2 * randn(n, 2) + array([5, 1])
labels = hstack((ones(n), -ones(n)))

# 用pickle模块保存
with open('points_normal.pkl', 'w') as f:
    pickle.dump(class_1, f)
    pickle.dump(class_2, f)
    pickle.dump(labels, f)
```

运行后会出现TypeError: write() argument must be str, not bytes报错。只需将

>  
 **with open('points_normal.pkl', 'w') as f:** 


**改为：**

>  
 **with open('points_normal.pkl', 'wb') as f:** 


错因：本人使用的的python3.9的版本，在python3中，用pickle模块保存创建的数据时，要以二进制（b）模式写入。

-----今天不学习，明天变废物。-----


