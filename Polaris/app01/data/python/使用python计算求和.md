
--- 
title:  使用python计算求和 
tags: []
categories: [] 

---
1、利用一般循环

```
i = 1
result = 0
while i&lt;=500:

    result += i
    i += 1
"""
 for i in range(501):
 #利用迭代器对象range生成1到500
    if i &lt;=500:
       result += i
"""
print(result)
```

2、高斯求和

公式：（首项+末项）* 项数 / 2

```
n = 500
sum = (1+n)*n/2
print(sum)
```

3、用函数实现

```
def add(i):
    result = 0
    for i in range(1,i+1):
    # 利用可迭代对象range生成 从1到i+1结束，不包括i+1
        result += i
    return result
sum = add(500)
print(sum)
```

4、用python内置函数实现

```
result = sum([i for i in range(501)])
print(result)
```


