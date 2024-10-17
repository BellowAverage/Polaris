
--- 
title:  用 Python 画个生日蛋糕为朋友庆生 
tags: []
categories: [] 

---
>  
  来源：http://suo.im/5CtiXr 
 

### 前言

蛋糕的由来：某天在b站上看到某up主，用ipad手绘了一个蛋糕，当时觉得还不错，于是就想自己也画一个蛋糕出来。但奈何画画技术不行，于是就想到利用刚学完的python来实现。

下面我来展示我的代码：

```
import turtle as t
import math as m
import random as r




def drawX(a, i):
    angle = m.radians(i)
    return a * m.cos(angle)




def drawY(b, i):
    angle = m.radians(i)
    return b * m.sin(angle)




# 设置背景颜色，窗口位置以及大小
t.bgcolor("#d3dae8")
t.setup(1000, 800)
t.penup()
t.goto(150, 0)
t.pendown()
# 1
t.pencolor("white")
t.begin_fill()
for i in range(360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)
t.fillcolor("#fef5f7")
t.end_fill()
# 2
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
# 3
t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#cbd9f9")
t.end_fill()
# 4
t.begin_fill()
t.pencolor("#fee48c")
for i in range(540):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.goto(-120, 0)
t.fillcolor("#cbd9f9")
t.end_fill()
# 5
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
# 6
t.pu()
t.goto(110, 70)
t.pd()
t.pencolor("#fff9fb")
t.begin_fill()
for i in range(360):
    x = drawX(110, i)
    y = drawY(44, i) + 70
    t.goto(x, y)
t.fillcolor("#fff9fb")
t.end_fill()
# 7
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
# 8
t.pu()
t.goto(120, 70)
t.pd()
t.begin_fill()
t.pensize(4)
t.pencolor("#fff0f3")
for i in range(1800):
    x = drawX(120, 0.1 * i)
    y = drawY(-18, i) + 10
    t.goto(x, y)
t.goto(-120, 70)
t.pensize(1)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()
# 9
t.pu()
t.goto(80, 70)
t.pd()
t.begin_fill()
t.pencolor("#6f3732")
t.goto(80, 120)
for i in range(180):
    x = drawX(80, i)
    y = drawY(32, i) + 120
    t.goto(x, y)
t.goto(-80, 70)
for i in range(180, 360):
    x = drawX(80, i)
    y = drawY(32, i) + 70
    t.goto(x, y)
t.fillcolor("#6f3732")
t.end_fill()
# 10
t.pu()
t.goto(80, 120)
t.pd()
t.pencolor("#ffaaa0")
t.begin_fill()
for i in range(360):
    x = drawX(80, i)
    y = drawY(32, i) + 120
    t.goto(x, y)
t.fillcolor("#ffaaa0")
t.end_fill()
# 11
t.pu()
t.goto(70, 120)
t.pd()
t.pencolor("#ffc3be")
t.begin_fill()
for i in range(360):
    x = drawX(70, i)
    y = drawY(28, i) + 120
    t.goto(x, y)
t.fillcolor("#ffc3be")
t.end_fill()
# 12
t.pu()
t.goto(80, 120)
t.pd()
t.begin_fill()
t.pensize(3)
t.pencolor("#ffaaa0")
for i in range(1800):
    x = drawX(80, 0.1 * i)
    y = drawY(-12, i) + 80
    t.goto(x, y)
t.goto(-80, 120)
t.pensize(1)
for i in range(180, 360):
    x = drawX(80, i)
    y = drawY(32, i) + 120
    t.goto(x, y)
t.fillcolor("#ffaaa0")
t.end_fill()
# 13
t.pu()
t.goto(64, 120)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 60
    y = drawY(1, i) + 120
    t.goto(x, y)
t.goto(64, 170)
for i in range(540):
    x = drawX(4, i) + 60
    y = drawY(1, i) + 170
    t.goto(x, y)
t.goto(56, 120)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(64, 120 + 10 * i)
    t.pu()
    t.goto(56, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(60, 170)
t.pd()
t.goto(60, 180)
t.pensize(1)
#
t.pu()
t.goto(64, 190)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 60
    y = drawY(10, i) + 190
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()


# 14
t.pu()
t.goto(-56, 120)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 120
    t.goto(x, y)
t.goto(-56, 170)
for i in range(540):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 170
    t.goto(x, y)
t.goto(-64, 120)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-56, 120 + 10 * i)
    t.pu()
    t.goto(-64, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(-60, 170)
t.pd()
t.goto(-60, 180)
t.pensize(1)
#
t.pu()
t.goto(-56, 190)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(10, i) + 190
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 15
t.pu()
t.goto(0, 130)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i)
    y = drawY(1, i) + 130
    t.goto(x, y)
t.goto(4, 180)
for i in range(540):
    x = drawX(4, i)
    y = drawY(1, i) + 180
    t.goto(x, y)
t.goto(-4, 130)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(4, 130 + 10 * i)
    t.pu()
    t.goto(-4, 130 + 10 * i)
    t.pd()
t.pu()
t.goto(0, 180)
t.pd()
t.goto(0, 190)
t.pensize(1)
#
t.pu()
t.goto(4, 200)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i)
    y = drawY(10, i) + 200
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 16
t.pu()
t.goto(30, 110)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 30
    y = drawY(1, i) + 110
    t.goto(x, y)
t.goto(34, 160)
for i in range(540):
    x = drawX(4, i) + 30
    y = drawY(1, i) + 160
    t.goto(x, y)
t.goto(26, 110)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(34, 110 + 10 * i)
    t.pu()
    t.goto(26, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(30, 160)
t.pd()
t.goto(30, 170)
t.pensize(1)
#
t.pu()
t.goto(34, 180)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 30
    y = drawY(10, i) + 180
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 17
t.pu()
t.goto(-30, 110)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 30
    y = drawY(1, i) + 110
    t.goto(x, y)
t.goto(-26, 160)
for i in range(540):
    x = drawX(4, i) - 30
    y = drawY(1, i) + 160
    t.goto(x, y)
t.goto(-34, 110)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-26, 110 + 10 * i)
    t.pu()
    t.goto(-34, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(-30, 160)
t.pd()
t.goto(-30, 170)
t.pensize(1)
#
t.pu()
t.goto(-26, 180)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 30
    y = drawY(10, i) + 180
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
###随机
color = ["#e28cb9", "#805a8c", "#eaa989", "#6e90b7", "#b8b68f", "#e174b5", "#cf737c", "#7c8782"]
for i in range(80):
    t.pu()
    x = r.randint(-120, 120)
    y = r.randint(-25, 30)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(40):
    t.pu()
    x = r.randint(-90, 90)
    y = r.randint(-35, 10)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])


for i in range(40):
    t.pu()
    x = r.randint(-80, 80)
    y = r.randint(60, 90)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(30):
    t.pu()
    x = r.randint(-50, 50)
    y = r.randint(45, 70)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(50):
    t.pu()
    x = r.randint(-500, 500)
    y = r.randint(120, 300)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(3, 5), color[r.randint(0, 7)])
t.seth(90)
t.pu()
t.goto(0, 0)
t.fd(210)
t.left(90)
t.fd(170)
t.pd()
t.write("Happy Birthday", font=("Curlz MT", 50))
t.done()

```

### 

### 效果图

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV2pTek1ycFNtRGliN091RXNCdzZ2YXJpYlZQdVRKb2VlbUpFWnp2UTMwYWx4c0Q0a1Jwcmw3ZjVBLzY0MA?x-oss-process=image/format,png">

总结
- 其实这里需要注意的是这份代码写的比较low，有许多重复的代码，没有用函数封装起来，一点都不优雅。希望大家可以在以后写代码的时候可以注意一下这一点。- 这里比较难的点，就是任意曲线的绘制。对于这个问题，我一开始也想了很多办法，也去网上查了很多资料，但是关于这方面的资料好像比较少。当时我在知乎等一些文章上发现一些大佬用本轮法进行图像的绘制，好像是轮子的个数越多，画出来的图像就越精准，其原理就是利用了高等数学下册的傅里叶变换。那时看了许多这种类型的文章，但是由于我们还没有学习傅里叶变换，也就看了一个寂寞。- 后来我在看turtle库时，发现了一个goto函数，也就是在画板上以正中心为原点，右边为x轴的正方向，上边为y轴的正方向。于是我就想到了用我们高中学过的参数方程来实现任意曲线的绘制。大家可以尝试着用一下参数方程来绘制自己想要的图形
<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanlWcFZ6VXNndmR4cVpiN2NhTjR4V2pVTXVTaHRKTlhPZUNZaWJUSzR5M0RCQWNKdFJwRnFpYmw4VVBNVEd3OHV0RGZEaDcyVzV1cWVMZy82NDA?x-oss-process=image/format,png">

最后我想说的是，数学真的很重要！！！

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcmNjSFVSRTF0ZmRnOWo5em9zbzYwNGdvWmtBeGpkdGNQSHo4WmFtaWJjakZiTUhMZGxNOG1RbWhveHZxbUpIUzRpY09hN2dSVGp2M1dBLzY0MA?x-oss-process=image/format,png">
