
--- 
title:  还在为 520 发愁吗？教你用 Python 写个表白神器！ 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20200519223912861.PNG" alt=""> 520 了，还在为表白发愁吗？教你用 Python 写个表白神器，给心仪的她（他）一个优雅的告白，本文实现用到的库是 turtle。

### 丘比特之箭

首先，我们来画一个丘比特之箭，要实现的最终效果如下： <img src="https://img-blog.csdnimg.cn/20200519224452311.PNG#pic_center" alt="" width="400"> 我们来简单看一下实现思路，从上图中可以看出丘比特之箭组成包括：心连心、箭和文字三部分，下面我们分别看一下具体实现。

我们先来看心连心的实现，我们要实现的心连心是两个心形叠加，再在心中添加填充色，实现代码如下：

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

实现效果： <img src="https://img-blog.csdnimg.cn/20200520063953755.PNG#pic_center" alt="" width="400"> 我们接着看箭的实现，箭包括头部和尾部两部分，实现代码如下：

```
# 箭尾
t.color('yellow')
t.width(5)
t.left(70)
t.fd(50)
t.fd(-50)
t.left(70)
t.fd(50)
t.fd(-50)
t.left(145)
t.fd(20)
t.left(145)
t.fd(50)
t.fd(-50)
t.left(70)
t.fd(50)
t.fd(-50)
t.left(145)
t.fd(20)
t.left(145)
t.fd(50)
t.fd(-50)
t.left(70)
t.fd(50)
t.fd(-50)
t.left(145)
t.width(3)
t.fd(220)
t.right(90)
t.pu()
t.fd(10)
t.pd()
# 箭头
t.begin_fill()
t.left(-30)
t.fd(-15)
t.right(-40)
t.fd(-50)
t.right(-165)
t.fd(-50)
t.end_fill()

```

实现效果： <img src="https://img-blog.csdnimg.cn/20200520064101742.PNG#pic_center" alt="" width="400"> 最后，我们看一下如何添加文字，代码实现如下：

```
t.color('red')
t.write('I LOVE YOU', move=False, align='center',font=("Times", 18, "bold"))

```

### 红玫瑰

接着，我们再来画一个红玫瑰，要实现的最终效果如下： <img src="https://img-blog.csdnimg.cn/20200519224633194.PNG#pic_center" alt="" width="400">

我们来简单看一下实现思路，从上图中可以看红玫瑰组成包括：玫瑰花和文字两部分，下面我们分别看一下具体实现。

我们先来看红玫瑰的实现，红玫瑰包括花和叶子，实现代码如下：

```
turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)
turtle.fillcolor('red')
# 花瓣1
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)
# 花瓣2
turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)
# 叶子1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()
turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)
# 叶子2
turtle.right(90)
turtle.right(45)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(80, 90)
turtle.left(90)
turtle.circle(80, 90)
turtle.end_fill()
turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200, 60)

```

实现效果： <img src="https://img-blog.csdnimg.cn/20200520064150604.PNG#pic_center" alt="" width="300"> 我们再来看如何添加文字，实现代码如下：

```
turtle.color('red')
turtle.write('520 Happy', move=False, align='center',font=("Times", 18, "bold"))
turtle.write('I LOVE YOU', move=False, align='center',font=("Times", 18, "bold"))

```

>  
 作者：程序员野客 公号：Python小二 链接： 

