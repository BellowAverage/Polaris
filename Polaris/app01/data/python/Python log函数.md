
--- 
title:  Python log函数 
tags: []
categories: [] 

---
`log()`有两种形式
- `log(x)`：返回 `x` 的自然对数（底数为`e`）- `log(x, base)`：返回以`base`为基的`x`的对数。`base`默认为`e`，也可以手动输入
注意：`log`不能直接使用，需要从头文件`math`中导入

```
from math import log, exp
print(log(exp(1)))
print(log(8, 2))
&gt;&gt;1.0
&gt;&gt;3.0

```
