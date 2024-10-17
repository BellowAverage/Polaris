
--- 
title:  520专属Python代码(Python遇到520) 
tags: []
categories: [] 

---
快到 520 了，分享几段 520 专属 Python 代码，不多说了，下面直接上货。



520专属Python代码



### No.1

效果： <img src="https://img-blog.csdnimg.cn/img_convert/97bf94730439444d352da838ddc2e376.png" alt=""> 主要代码：

```
import turtle

turtle.speed(0)
turtle.delay(10)
turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(10, 180)
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
# 花瓣
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)
# 文字
turtle.color('red')
turtle.pu()
turtle.goto(-210,80)
turtle.pd()
turtle.write('520 Happy', move=False, align='center',font=("Times", 18, "bold"))
turtle.pu()
turtle.goto(210,80)
turtle.pd()
turtle.write('I LOVE YOU', move=False, align='center',font=("Times", 18, "bold"))
turtle.pu()
turtle.pu()
turtle.hideturtle()
turtle.done()

```

### No.2

效果： <img src="https://img-blog.csdnimg.cn/img_convert/2b62a945ac619186567d45670c962764.png" alt=""> 主要代码：

```
import turtle as t

t.speed(0)
t.delay(10)
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
# 箭头
t.begin_fill()
t.left(-30)
t.fd(-15)
t.right(-40)
t.fd(-50)
t.right(-165)
t.fd(-50)
t.end_fill()
# 文字
t.color('red')
t.pu()
t.goto(-150,30)
t.pd()
t.write('I LOVE YOU',
move=False, align='center',
font=("Times", 18, "bold"))
t.hideturtle()
t.done()

```

### No.3

效果： <img src="https://img-blog.csdnimg.cn/img_convert/02d4e7dedd163eb389daa4aad55e0445.png" alt=""> 主要代码：

```
import turtle
import random

# 画爱心
def love(x, y):
    lv = turtle.Turtle()
    lv.hideturtle()
    lv.up()
    # 定位
    lv.goto(x, y)
    # 画圆弧
    def curvemove():
        for i in range(20):
            lv.right(10)
            lv.forward(2)

    lv.color('red', 'pink')
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
    # 画完复位
    lv.left(140)
    lv.end_fill()
myWin = turtle.Screen()
myWin.setup(width=700, height=700)
t = turtle.Turtle()
t.speed(0)
turtle.delay(0)
t.hideturtle()
t.left(90)
t.up()
t.backward(200)
t.down()
t.color("brown")
t.pensize(32)
t.forward(60)
tree(100, t)
myWin.exitonclick()    

```

源码在下方公号后台回复**py520**获取~
