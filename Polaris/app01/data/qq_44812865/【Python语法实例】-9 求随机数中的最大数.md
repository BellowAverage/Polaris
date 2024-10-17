
--- 
title:  【Python语法实例】-9 求随机数中的最大数 
tags: []
categories: [] 

---
```
import random
x=random.randrange(100,201)     	#产生一个[100, 200]之间的随机数x
maxn = x                      	#设定最大数
print(x,end=" ")
for i  in range(2, 11):
    x=random. randrange(100,201)    #再产生一个[100, 200]之间的随机数x
    print(x,end=" ")
    if x &gt; maxn :
        maxn = x;            	 #若新产生的随机数大于最大数，则进行替换
print ("最大数：",maxn)

```
