
--- 
title:  送你情人节(劫)专属Python全套代码 
tags: []
categories: [] 

---
今天是情人节，送你一套专属Python代码，好像发的有点晚了 ... 不过也没关系，可以留着下次用<img src="https://img-blog.csdnimg.cn/img_convert/47d92df46fe3f3dd5ce252b7d8585aa4.png" alt="47d92df46fe3f3dd5ce252b7d8585aa4.png">

### 玫瑰

部分代码实现如下：

```
# 花瓣1
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)
# 花瓣2
turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)
# 叶子1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()
turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)
```

效果：

### 爱心树

部分代码实现如下：

```
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
```

效果：

### 丘比特

部分代码实现如下：

```
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

### 多彩气球

部分代码实现如下：

```
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

全部代码已经打包整理好了，有需要的小伙伴可以在公众号**Python小二**后台回复**20220214**获取~

**<strong>往期回顾：**</strong>
- - - - - - - - 