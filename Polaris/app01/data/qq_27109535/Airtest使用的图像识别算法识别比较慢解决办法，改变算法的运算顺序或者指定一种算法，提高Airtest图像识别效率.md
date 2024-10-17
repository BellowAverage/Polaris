
--- 
title:  Airtest使用的图像识别算法识别比较慢解决办法，改变算法的运算顺序或者指定一种算法，提高Airtest图像识别效率 
tags: []
categories: [] 

---
## Airtest使用的图像识别算法识别比较慢解决办法，改变算法的运算顺序或者指定一种算法，提高Airtest图像识别效率

## 调整Airtest图像识别算法的使用顺序

```
from airtest.core.settings import Settings as ST

# 调整Airtest图像识别算法的使用顺序
ST.CVSTRATEGY = ["mstpl","tpl", "sift","brisk"]




```

## 指定一种算法（mstpl算法）

```

from airtest.core.settings import Settings as ST

# 指定仅使用mstpl算法
ST.CVSTRATEGY = ["mstpl"]

```
