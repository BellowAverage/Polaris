
--- 
title:  【Python语法实例】-11自定义函数 
tags: []
categories: [] 

---
```
def math(k):
    if(k==1):
        return lambda x,y : x+y
    if(k==2):
        return lambda x,y : x-y
    if(k==3):
        return lambda x,y : x*y
    if(k==4):
        return lambda x,y : x/y
#调用函数
action = math(1)				#返回加法Lambda表达式
print("10+2=", action(10,2))
action = math(2)				#返回减法Lambda表达式
print("10-2=",action(10,2))
action = math(3)				#返回乘法Lambda表达式
print("10*2=,=",action(10,2))
action = math(4)				#返回除法Lambda表达式
print("10/2=,=",action(10,2))

```
