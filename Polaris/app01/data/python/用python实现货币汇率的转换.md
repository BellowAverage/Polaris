
--- 
title:  用python实现货币汇率的转换 
tags: []
categories: [] 

---
github地址：

例如我们想要看一下美元与英镑之间的汇率转换，100美元可以换成多少的英镑，代码如下

```
# 导入模块
from currency_converter import CurrencyConverter
from datetime import date
# 案例一
conv = CurrencyConverter()
c = conv.convert(100, 'USD', 'GBP')
print(round(c, 2)) # 保留两位小数

```

或者我们想要看一下美元与欧元之间的汇率转换，100美元可以换成多少的欧元：

```
# 案例二
c = conv.convert(100, 'USD', 'EUR', date=date(2022, 3, 30))
print(round(c, 2)) # 44.1

```
