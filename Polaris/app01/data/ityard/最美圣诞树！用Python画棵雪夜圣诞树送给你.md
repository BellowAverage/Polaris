
--- 
title:  最美圣诞树！用Python画棵雪夜圣诞树送给你 
tags: []
categories: [] 

---
今天是平安夜，明天就是圣诞节，这两天应该是苹果最畅销的日子 ...

<img src="https://img-blog.csdnimg.cn/img_convert/3b1187defcd33c95f2da29d3be9fc862.gif" alt="3b1187defcd33c95f2da29d3be9fc862.gif">

提到圣诞节，就不得不提圣诞树，本文我们用 Python 来画一棵圣诞树，先睹为快。

<img src="https://img-blog.csdnimg.cn/img_convert/33bba968f681eee0c10f6a082d53ab7d.gif" alt="33bba968f681eee0c10f6a082d53ab7d.gif">

下面展开来看一下主要代码实现。

#### 树

圣诞树主要代码实现如下：

```
# 画第一层
seth(-120)
for i in range(10):
    fd(12)
    right(2)
penup()
goto(0, 150)
seth(-60)
pendown()
for i in range(10):
    fd(12)
    left(2)
seth(-150)
penup()
fd(10)
pendown()
for i in range(5):
    fd(10)
    right(15)
seth(-150)
penup()
fd(8)
pendown()
for i in range(5):
    fd(10)
    right(15)
seth(-155)
penup()
fd(5)
pendown()
for i in range(5):
    fd(7)
    right(15)
# 画第二层
penup()
goto(-55, 34)
pendown()
seth(-120)
for i in range(10):
    fd(8)
    right(5)

penup()
goto(50, 35)
seth(-60)
pendown()
for i in range(10):
    fd(8)
    left(5)
seth(-120)
penup()
fd(10)
seth(-145)
pendown()
for i in range(5):
    fd(10)
    right(15)
penup()
fd(10)
seth(-145)
pendown()
for i in range(5):
    fd(12)
    right(15)
penup()
fd(8)
seth(-145)
pendown()
for i in range(5):
    fd(10)
    right(15)
penup()
seth(-155)
fd(8)
pendown()
for i in range(5):
    fd(11)
    right(15)
......
```

#### 星星

五角星主要代码实现如下：

```
pensize(2)
pencolor("yellow")
penup()
goto(x, y)
pendown()
begin_fill()
fillcolor("yellow")
for i in range(5):
    left(72)
    fd(size)
    right(144)
    fd(size)
end_fill()
```

#### 帽子

帽子主要代码实现如下：

```
penup()
goto(-30, -120)
pencolor("white")
pendown()
fillcolor("white")
begin_fill()
fd(30)
circle(4, 180)
fd(30)
circle(4, 180)
end_fill()
penup()
goto(-25, -115)
seth(75)
pendown()
fillcolor("red")
begin_fill()
for i in range(5):
    fd(6)
    right(20)
seth(-10)
for i in range(5):
    fd(8)
    right(15)
seth(145)
for i in range(5):
    fd(5)
    left(2)
seth(90)
for i in range(5):
    fd(1)
    left(2)
seth(-90)
for i in range(4):
    fd(4)
    right(6)
seth(161)
fd(30)
end_fill()
pensize(1)
pencolor("white")
```

#### 袜子

袜子主要代码实现如下：

```
penup()
goto(-20, 80)
pencolor("white")
pendown()
begin_fill()
fillcolor("white")
fd(25)
circle(4, 180)
fd(25)
circle(4, 180)
end_fill()
penup()
goto(-15, 80)
pendown()
begin_fill()
fillcolor("red")
seth(-120)
fd(20)
seth(150)
fd(5)
circle(7, 180)
fd(15)
circle(5, 90)
fd(30)
seth(160)
fd(18)
end_fill()
penup()
seth(0)
goto(70, -240)
```

#### 蝴蝶结

蝴蝶结主要代码实现如下：

```
penup()
pencolor("#f799e6")
goto(x, y)
seth(80)
pendown()
pensize(2)
circle(5)
seth(10)
fd(15)
seth(120)
fd(20)
seth(240)
fd(20)
seth(180)
fd(20)
seth(-60)
fd(20)
seth(50)
fd(20)
seth(-40)
fd(30)
seth(-130)
fd(5)
seth(135)
fd(30)
seth(-60)
fd(30)
seth(-150)
fd(6)
seth(110)
fd(30)
```

#### 雪花

雪落效果主要代码实现如下：

```
screen.delay(0)
t = Turtle(visible = False,shape='circle')
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.setheading(-90)
t.goto(r.randint(-width/2,width/2),height/2)
stars = []
for i in range(200):
    star = t.clone()
    s =r.random() / 3
    star.shapesize(s,s)
    star.speed(int(s*10))
    star.setx(r.randint(-width/2,width/2))
    star.sety(height/2 + r.randint(1,height))
    star.showturtle()
    stars.append(star)
while True:
    for star in stars:
        star.sety(star.ycor() - 8 * star.speed())
        if star.ycor()&lt;-height/2:
            star.hideturtle()
            star.setx(r.randint(-width/2,width/2))
            star.sety(height/2 + r.randint(1,height))
            star.showturtle()
```

以上就是圣诞树的主要Python代码实现部分，当然我们还可以为其添加背景音乐，这里就不细说了，感兴趣的可以参考：。

完整代码已经打包整理好了，有需要的可以在公众号Python小二后台回复圣诞树直接获取。

**<strong><img src="https://img-blog.csdnimg.cn/img_convert/2f10371a04793fe0a60340221c6a5437.png" alt="2f10371a04793fe0a60340221c6a5437.png"> **</strong>**<strong>阅读更多**</strong>
- - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/98c23b3f850954a6bec8522d760a1b3f.gif" alt="98c23b3f850954a6bec8522d760a1b3f.gif">
