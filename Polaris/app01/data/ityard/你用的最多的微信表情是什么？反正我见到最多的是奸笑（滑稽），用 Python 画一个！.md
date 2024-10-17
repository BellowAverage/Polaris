
--- 
title:  你用的最多的微信表情是什么？反正我见到最多的是奸笑（滑稽），用 Python 画一个！ 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/2020051819505369.PNG?#pic_center" alt=""> 微信自带的表情大家应该都用过，其中奸笑（其他的平台也有叫滑稽的）的表情使用率算是比较高的，对于这个表情，有的人喜欢，也有的人不喜欢，这个都是正常的，我们不讨论这个。

大家应该都知道 Python 的 turtle 库可以画画，本文我们就使用这个库画一个奸笑表情。

由于微信上的表情尺寸较小，看起来不方便，我从网上找了一个大一点的，如下所示： <img src="https://img-blog.csdnimg.cn/20200518192640889.jpg#pic_" alt="" width="300"> 我们可以看出这个表情的组成部分包括：脸框（就是那个大圆圈）、眼眉、眼眶、眼珠、红腮、嘴，下面我们开始画这几部分。

首先我们画脸框，代码实现如下所示：

```
penup()  
goto(\-210,0)  
seth(\-90)  
pendown()  
pencolor('#FFCC33')  
pensize(4)  
begin\_fill()  
circle(210,360)  
fillcolor('#FFFF99')  
end\_fill()  
pencolor('#330033')

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200518192911528.PNG#pic_" alt="" width="300"> 接着眉毛，代码实现如下：

```
penup()  
pensize(4)  
goto(\-180,140)  
pencolor('#585858')  
pendown()  
seth(70)  
circle(\-60,140)  

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200518192943741.PNG#pic_" alt="" width="300"> 再接着画眼眶和眼珠，代码实现如下：

```
# 眼眶  
penup()  
pensize(4)  
goto(\-180,90)  
pencolor('#909090')  
pendown()  
seth(40)  
begin\_fill()  
circle(\-120,80)  
penup()  
goto(\-180,90)  
seth(\-130)  
pendown()  
circle(15,110)  
seth(40)  
circle(\-106,83)  
seth(30)  
circle(18,105)  
fillcolor('white')  
end\_fill()  
# 眼珠  
pensize(2)  
penup()  
goto(30,83)  
pendown()  
begin\_fill()  
circle(8,360)  
fillcolor('black')  
end\_fill()  
penup()  
goto(\-170,83)  
pendown()  
begin\_fill()  
circle(8,360)  
fillcolor('black')  
end\_fill()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200518193010343.PNG?#pic_" alt="" width="300"> 再接着画红腮，代码实现如下：

```
pensize(1)  
pencolor('LightSalmon')  
begin\_fill()  
penup()  
goto(\-160,50)  
pendown()  
seth(\-90)  
for i in range(2):  
for j in range(10):  
forward(j)  
left(9)  
for j in range(10,0,\-1):  
forward(j)  
left(9)  
fillcolor('LightSalmon')  
end\_fill()  
pensize(1)  
pencolor('LightSalmon')  
begin\_fill()  
penup()  
goto(40,50)  
pendown()  
seth(\-90)  
for i in range(2):  
for j in range(10):  
forward(j)  
left(9)  
for j in range(10,0,\-1):  
forward(j)  
left(9)  
fillcolor('LightSalmon')  
end\_fill()  
hideturtle()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200518193032147.PNG#pic_" alt="" width="300"> 最后我们画嘴，代码实现如下：

```
pensize(5)  
penup()  
goto(\-150,\-30)  
pencolor('#585858')  
pendown()  
seth(\-90)  
circle(150,180)

```

看一下最终效果： <img src="https://img-blog.csdnimg.cn/20200518193050485.PNG#pic_" alt="" width="300"> 是不是有内味了。 <img src="https://img-blog.csdnimg.cn/20200518193316804.jpg#pic_" alt="" width="300">

>  
 作者：程序员野客 公号：Python小二 声明：本文首发于公号 

