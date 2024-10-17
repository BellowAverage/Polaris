
--- 
title:  七夕最强Python表白代码来了 
tags: []
categories: [] 

---
点击上方**Python小二**，选择**星标**公众号

干货速达，不迷路

快到七夕了，大家都懂，这里不过多解释了，送大家几段节日专属Python代码。

>  
  玫瑰 
 

毫无疑问，玫瑰一直都是七夕、520......这类节日的专属，带文字的玫瑰花，文字可以根据节日自行更改。

参考代码：

```
import turtle

turtle.speed(0)
turtle.delay(10)
turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(10, 180)
turtle.circle(25, 110)
# 花瓣
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)
# 文字
turtle.color('red')
turtle.pu()
turtle.goto(-210,80)
turtle.pd()
turtle.write('520 Happy', move=False, align='center',font=("Times", 18, "bold"))
turtle.pu()
turtle.goto(210,80)
turtle.pd()
turtle.write('I LOVE YOU', move=False, align='center',font=("Times", 18, "bold"))
turtle.pu()
turtle.pu()
turtle.hideturtle()
turtle.done()
```

效果：

>  
  心连心 
 

丘比特爱心之箭，把你的心我的心串一串......

参考代码：

```
import turtle as t

t.color('red','pink')
t.begin_fill()
t.width(5)
t.left(135)
t.fd(100)
t.right(180)
t.circle(50,-180)
t.left(90)
t.circle(50,-180)
t.right(180)
t.fd(100)
t.pu()
t.goto(50,-30)
t.pd()
t.right(90)
t.fd(100)
t.right(180)
t.circle(50,-180)
t.left(90)
t.circle(50,-180)
t.right(180)
t.fd(100)
t.end_fill()
t.hideturtle()
t.pu()
t.goto(250,-70)
t.pd()
```

效果：

>  
  动态爱心 
 

一颗跳动的爱心，见之心动.....

参考代码：

```
import random
from tkinter import *
from math import sin, cos, pi, log

for _ in range(520):
 x, y = random.choice(point_list)
 x, y = scatter_inside(x, y, 0.17)
 self._center_diffusion_points.add((x, y))
heart_halo_point = set()
for _ in range(halo_number):
 t = random.uniform(0, 2 * pi)
 x, y = heart(t, shrink_ratio=11.6)
 x, y = shrink(x, y, halo_radius)
 if (x, y) not in heart_halo_point:
  heart_halo_point.add((x, y))
  x += random.randint(-14, 14)
  y += random.randint(-14, 14)
  size = random.choice((1, 2, 2))
  all_points.append((x, y, size))
for x, y in self._points:
 x, y = self.calc_position(x, y, ratio)
 size = random.randint(1, 3)
 all_points.append((x, y, size))
for x, y in self._edge_diffusion_points:
 x, y = self.calc_position(x, y, ratio)
 size = random.randint(1, 2)
 all_points.append((x, y, size))
self.all_points[generate_frame] = all_points
for x, y in self._center_diffusion_points:
 x, y = self.calc_position(x, y, ratio)
 size = random.randint(1, 2)
 all_points.append((x, y, size))
self.all_points[generate_frame] = all_points
```

效果：

>  
  爱心biu 
 

一个小可爱伸手发射爱心+文字，文字可根据节日自行更改。

参考代码：

```
from turtle import *

color('black')
go_to(-228, 72)
pensize(3)
left(150)
ring(350,1,0.8,'right')
left(150)
forward(70)
left(90)
forward(10)
ring(200,0.1,0.9,'right')
forward(10)
left(90)
forward(20)
ring(200,0.1,0.9,'right')
forward(10)
left(90)
ring(200,0.2,0.9,'right')
left(100)
left
forward(80)
go_to(-228, 72)
left(40)
forward(40)
ring(120,0.2,0.9,'left')
go_to(-219,52)
right(95)
forward(80)
right(85)
ring(205,0.1,0.9,'left')
forward(40)
left(90)
forward(10)
ring(200,0.1,0.9,'right')
forward(10)
left(90)
forward(40)
ring(205,0.1,0.9,'left')
right(92)
forward(90)
```

效果：

>  
  爱心树 
 

一棵长满爱心果实的爱心树，祝你们修成正果.....

参考代码：

```
import turtle, random

# 画爱心
def love(x, y):
    lv = turtle.Turtle()
    lv.hideturtle()
    lv.up()
    # 定位
    lv.goto(x, y)
    # 画圆弧
    def curvemove():
        for i in range(20):
            lv.right(10)
            lv.forward(2)

    lv.color('red', 'pink')
    lv.speed(10000000)
    lv.pensize(1)
    lv.down()
    lv.begin_fill()
    lv.left(140)
    lv.forward(22)
    curvemove()
    lv.left(120)
    curvemove()
    lv.forward(22)
    # 画完复位
    lv.left(140)
    lv.end_fill()

# 画树
def tree(branchLen, t):
    # 剩余树枝太少要结束递归
    if branchLen &gt; 5:
        # 如果树枝剩余长度较短则变绿
        if branchLen &lt; 20:
            t.color("green")
            t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
            t.down()
            t.forward(branchLen)
            love(t.xcor(), t.ycor())
            t.up()
            t.backward(branchLen)
            t.color("brown")
            return
        t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
        t.down()
        t.forward(branchLen)
        # 以下递归
        ang = random.uniform(15, 45)
        t.right(ang)
        # 随机决定减小长度
        tree(branchLen - random.uniform(12, 16), t)
        t.left(2 * ang)
        # 随机决定减小长度
        tree(branchLen - random.uniform(12, 16), t)
        t.right(ang)
        t.up()
        t.backward(branchLen)
```

效果：

>  
  告白气球 
 

五颜六色动态向上漂浮的气球，鼠标点击可击破气球。

参考代码：

```
from turtle import *
from random import randrange, choice

# 气球
balloons = []
# 颜色
color_option = ["red", "blue", "green", "purple", "pink", "yellow", "orange"]
# 气球大小
size = 50
# 气球线
def line(x, y, a, b, line_width=1, color_name="black"):
    up()
    goto(x, y)
    down()
    color(color_name)
    width(line_width)
    goto(a, b)

def distance(x, y, a, b):
    # 判断鼠标点击位置和气球坐标的距离
    return ((a - x) ** 2 + (b - y) ** 2) ** 0.5
def tap(x, y):
    for i in range(len(balloons)):
        # 判断是否点击气球队列中的其中一个
        if distance(x, y, balloons[i][0], balloons[i][1]) &lt; (size / 2):
            # 删除气球
            balloons.pop(i)
            return
```

效果：

>  
  告白墙 
 

一幅寂静优美的画面配上优美的文字，一眼万年.....

参考代码：

```
import cv2
import numpy as np
from PIL import Image
from wordcloud import WordCloud

img = cv2.imread('test.png')
mask = np.zeros(img.shape[:2], np.uint8)
size = (1, 65)
bgd = np.zeros(size, np.float64)
fgd = np.zeros(size, np.float64)
rect = (1, 1, img.shape[1], img.shape[0])
cv2.grabCut(img, mask, rect, bgd, fgd, 10, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 1, 255)
img = img.astype(np.int32)
img *= mask2[:, :, np.newaxis]
img[img&gt;255] = 255
img =img.astype(np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = Image.fromarray(img, 'RGB')
img.save('test1.jpg')
```

效果：

好了，这个七夕小二就送你这些Python表白代码了，如有帮助记得给小二点个在看随手转发一下，笔芯♥~

完整代码已经打包整理好了，点击下方卡片，在公众号**Python小二**后台回复**20230822**免费领取。










