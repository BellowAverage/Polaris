
--- 
title:  【python语法实例】-1 
tags: []
categories: [] 

---
IF语句

```
#任意输入三个数字，按从小到大顺序输出。
x = input('x=')
y = input('y=')
z = input('z=')
if x &gt; y:
    x, y = y, x
if x &gt; z:
    x, z = z, x
if y &gt; z:
    y, z = z, y
print(x, y, z)

```
