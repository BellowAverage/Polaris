
--- 
title:  用 Python 画一个捂脸表情 
tags: []
categories: [] 

---
微信中的捂脸表情相信大家都不陌生，我见过以及自己使用这个表情的频率都是比较高的，可以说这个表情算是大部分人的主打表情之一了，本文我使用 Python 来画一下这个表情，我们使用到的库还是 turtle。

### 实现

因微信中的表情较小，我到网上找了一个大一点的，一起来看一下： <img src="https://img-blog.csdnimg.cn/20210321165109638.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="300"> 从图中我们可以看出这个表情由：脸框（那个大圆圈）、手、眼睛、眼泪、嘴（包括牙齿），下面我们看一下如何使用 Python 来画它。

首先，我们来画脸框，代码实现如下：

```
turtle.speed(5)
turtle.setup(500, 500)
turtle.pensize(5)
turtle.right(90)
turtle.penup()
turtle.fd(100)
turtle.left(90)
turtle.pendown()
turtle.begin_fill()
turtle.pencolor("#B8860B")
turtle.circle(150)
turtle.fillcolor("#FFFF99")
turtle.end_fill()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20210321165135767.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="300"> 接着来画嘴（包括牙齿），代码实现如下：

```
turtle.penup()
turtle.goto(77, 20)
turtle.pencolor("#B8860B")
turtle.goto(0, 50)
turtle.right(30)
turtle.fd(110)
turtle.right(90)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#925902")
turtle.circle(-97, 160)
turtle.goto(92, -3)
turtle.end_fill()
turtle.penup()
turtle.goto(77, -25)
# 牙齿
turtle.pencolor("white")
turtle.begin_fill()
turtle.fillcolor("white")
turtle.goto(77, -24)
turtle.goto(-81, 29)
turtle.goto(-70, 43)
turtle.goto(77, -8)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -100)
turtle.setheading(0)
turtle.pendown()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20210321165202187.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="300"> 再接着来画眼泪，代码实现如下：

```
# 左边眼泪
turtle.left(90)
turtle.pensize(3)
turtle.penup()
turtle.fd(150)
turtle.right(60)
turtle.fd(-150)
turtle.pendown()
turtle.left(20)
turtle.pencolor("#155F84")
turtle.fd(150)
turtle.right(180)
position1 = turtle.position()
turtle.begin_fill()
turtle.fillcolor("#B0E0E6")
turtle.fd(150)
turtle.right(20)
turtle.left(270)
turtle.circle(-150, 18)
turtle.right(52)
turtle.fd(110)
position2 = turtle.position()
turtle.goto(-33, 90)
turtle.end_fill()
# 右边眼泪
turtle.penup()
turtle.goto(0, 0)
turtle.setheading(0)
turtle.left(90)
turtle.fd(50)
turtle.right(150)
turtle.fd(150)
turtle.left(150)
turtle.fd(100)
turtle.pendown()
turtle.begin_fill()
turtle.fd(-100)
turtle.fillcolor("#B0E0E6")
turtle.right(60)
turtle.circle(150, 15)
turtle.left(45)
turtle.fd(66)
turtle.goto(77, 20)
turtle.end_fill()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20210321165217728.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="300"> 再接着画眼睛，代码实现如下：

```
turtle.pensize(5)
turtle.penup()
turtle.pencolor("black")
turtle.goto(-65, 75)
turtle.setheading(0)
turtle.left(27)
turtle.fd(30)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.left(90)
turtle.circle(30, 86)
turtle.goto(position2[0], position2[1])
turtle.goto(position1[0], position1[1])
turtle.end_fill()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20210321165310803.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="300"> 最后，我们来画手，代码实现如下：

```
turtle.pencolor("#B8860B")
turtle.fillcolor("#FFFF99")
arc(-110, 10, 110, -40, 30)
turtle.begin_fill()
turtle.circle(300, 35)
turtle.circle(13, 120)
turtle.setheading(-50)
turtle.fd(20)
turtle.setheading(130)
turtle.circle(200, 15)
turtle.circle(12, 180)
turtle.fd(40)
turtle.setheading(137)
turtle.circle(200, 16)
turtle.circle(12, 160)
turtle.setheading(-35)
turtle.fd(45)
turtle.setheading(140)
turtle.circle(200, 13)
turtle.circle(11, 160)
turtle.setheading(-35)
turtle.fd(40)
turtle.setheading(145)
turtle.circle(200, 9)
turtle.circle(10, 180)
turtle.setheading(-31)
turtle.fd(50)
turtle.setheading(-45)
turtle.pensize(7)
turtle.right(5)
turtle.circle(180, 35)
turtle.end_fill()
turtle.begin_fill()
turtle.setheading(-77)
turtle.fd(50)
turtle.left(-279)
turtle.fd(16)
turtle.circle(29, 90)
turtle.end_fill()

```

看一下最终效果： <img src="https://img-blog.csdnimg.cn/202103211653284.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="" width="300"> 是不是有内味了。

### 总结

本文我们使用 Python 画了一个捂脸表情，如果大家对实现效果不满意的话，可以自己动手将它修改成自己满意的样子。

源码在公众号 **Python小二** 后台回复 **fp** 获取。

>  
 本文非首发于个人号 

