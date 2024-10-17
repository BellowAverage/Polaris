
--- 
title:  【Python语法实例】-10for循环套用 
tags: []
categories: [] 

---
```
for x in range(0, 100):
    for y in range(0, 100):
        z = 100-x-y
        if z &gt;= 0 and 5*x+3*y+z/3 == 100 :
            print ('公鸡%d只，母鸡%d只，小鸡%d只'%(x, y, z))

```
