
--- 
title:  用Python画个生日蛋糕为朋友庆生 
tags: []
categories: [] 

---
每当有朋友过生日时，生日蛋糕自然是必不可少的，今天我们来看一下如何用 Python 画一个生日蛋糕。

本文我们用到的 Python 库包括：turtle、math 和 random。

实现的主要代码如下：

```
import math as m
import random as r
import turtle as t

t.speed(0)
t.delay(0)
# 设置背景颜色及窗口
t.bgcolor("#FFFFFF")
t.setup(800, 600)
t.penup()
t.goto(150, 0)
t.pendown()

t.pencolor("white")
t.begin_fill()
for i in range(360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)
t.fillcolor("#fef5f7")
t.end_fill()

t.begin_fill()
for i in range(180):
    x = drawX(150, -i)
    y = drawY(70, -i)
    t.goto(x, y)
for i in range(180, 360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)
t.fillcolor("#f2d7dd")
t.end_fill()

t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#33CCFF")
t.end_fill()

t.begin_fill()
t.pencolor("#fee48c")
for i in range(540):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.goto(-120, 0)
t.fillcolor("#99FFFF")
t.end_fill()

t.pu()
t.goto(120, 70)
t.pd()
t.pencolor("#fff0f3")
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()

t.pu()
t.goto(110, 70)
t.pd()
t.pencolor("#fff9fb")
t.begin_fill()
for i in range(360):
    x = drawX(110, i)
    y = drawY(44, i) + 70
    t.goto(x, y)
t.fillcolor("#FFCCCC")
t.end_fill()

t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
t.pencolor("#ffa79d")
for i in range(180):
    x = drawX(120, -i)
    y = drawY(48, -i) + 10
    t.goto(x, y)
t.goto(-120, 0)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#ffa79d")
t.end_fill()

for i in range(50):
    t.pu()
    x = r.randint(-500, 500)
    y = r.randint(120, 300)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(3, 5),
 color[r.randint(0, 7)])
t.penup()
t.goto(-130, 230)
t.pencolor("#FF0000")
t.write("Happy Birthday",
 font=("Curlz MT", 30))
t.hideturtle()
t.done()
```

实现效果（点击下方视频查看）：

**源码获取：**

①**关注**上方视频号**来去如风** + ②**点****♥** + ③**私信**“生日”，完成①②③点即可免费获取~

<img src="https://img-blog.csdnimg.cn/img_convert/0c771caa49fdf9c450e80f794523cb56.png" alt="0c771caa49fdf9c450e80f794523cb56.png"><img src="https://img-blog.csdnimg.cn/img_convert/c50692e2c1f2d615970007ecd698b200.png" alt="c50692e2c1f2d615970007ecd698b200.png">

推荐阅读  点击标题可跳转
- - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/5bb22a23122b141a244791cad8005be9.gif" alt="5bb22a23122b141a244791cad8005be9.gif">
