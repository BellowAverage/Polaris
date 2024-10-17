
--- 
title:  【Python语法实例】-3最大公约数 
tags: []
categories: [] 

---
```
num1 = int(input("输入第一个数字: "))# 用户输入两个数字
num2 = int(input("输入第二个数字: "))
m = num1
n = num2
if m &lt; n: 						#m,n交换值
    t = m
    m = n
    n = t 
r = m % n;
while  r!=0:
    m = n;
    n = r
    r = m % n
print( num1,"和", num2,"的最大公约数为", n)


```
