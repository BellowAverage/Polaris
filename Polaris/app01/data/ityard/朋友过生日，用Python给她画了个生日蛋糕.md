
--- 
title:  朋友过生日，用Python给她画了个生日蛋糕 
tags: []
categories: [] 

---
每当有朋友过生日时，生日蛋糕自然是必不可少的，今天我们来看一下如何用 Python 画一个生日蛋糕。

本文我们用到的 Python 库包括：turtle、math 和 random。

实现的主要代码如下：

```
import math as m
import random as r
import turtle as t

t.speed(0)
t.delay(0)
# 设置背景颜色及窗口
t.bgcolor("#FFFFFF")
t.setup(800, 600)
t.penup()
t.goto(150, 0)
t.pendown()

t.pencolor("white")
t.begin_fill()
for i in range(360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)
t.fillcolor("#fef5f7")
t.end_fill()

t.begin_fill()
for i in range(180):
    x = drawX(150, -i)
    y = drawY(70, -i)
    t.goto(x, y)
for i in range(180, 360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)
t.fillcolor("#f2d7dd")
t.end_fill()

t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#33CCFF")
t.end_fill()

t.begin_fill()
t.pencolor("#fee48c")
for i in range(540):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.goto(-120, 0)
t.fillcolor("#99FFFF")
t.end_fill()

t.pu()
t.goto(120, 70)
t.pd()
t.pencolor("#fff0f3")
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()

t.pu()
t.goto(110, 70)
t.pd()
t.pencolor("#fff9fb")
t.begin_fill()
for i in range(360):
    x = drawX(110, i)
    y = drawY(44, i) + 70
    t.goto(x, y)
t.fillcolor("#FFCCCC")
t.end_fill()

t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
t.pencolor("#ffa79d")
for i in range(180):
    x = drawX(120, -i)
    y = drawY(48, -i) + 10
    t.goto(x, y)
t.goto(-120, 0)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#ffa79d")
t.end_fill()

for i in range(50):
    t.pu()
    x = r.randint(-500, 500)
    y = r.randint(120, 300)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(3, 5),
	color[r.randint(0, 7)])
t.penup()
t.goto(-130, 230)
t.pencolor("#FF0000")
t.write("Happy Birthday",
 font=("Curlz MT", 30))
t.hideturtle()
t.done()

```

实现效果如下：

<img src="https://img-blog.csdnimg.cn/37d7b80c41bc42018f61c608c08bd069.gif#pic_center" alt=""> 源码在下方公号后台回复**py蛋糕**获取~
