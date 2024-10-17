
--- 
title:  我用 Python 画了一盘粽子送给大家 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/cca41b155e625ef6406606f0e9439c32.png">

今天是端午节，首先祝大家端午安康，说到端午节，粽子则是必不可少的，现在粽子的种类也是五花八门，但我还是喜欢传统的白棕子，你喜欢哪种粽子呢？在大家吃着美味粽子的同时，本文我们画一盘粽子送给大家。

### 先睹为快

我们先来欣赏一下最终的效果图：

<img src="https://img-blog.csdnimg.cn/img_convert/63539f163659e14670f3ebd60ba71444.png">

从图中我们可以看出整体分三部分组成：盘子、粽子、文字，下面我们展开来说一下相应实现。

### 盘子实现

首先，我们来画一个盘子，盘子的组成比较简单，就是一个椭圆再加上填充色，代码实现如下：

```
# 画盘子
def plate(a, b, angle, steps, rotateAngle):
    minAngle = (2 * math.pi / 360) * angle / steps
    rotateAngle = rotateAngle / 360 * 2 * math.pi
    penup() # 起笔
    setpos(b * math.sin(rotateAngle), -b * math.cos(rotateAngle))
    pendown() # 落笔
    for i in range(steps):
        nextPoint = [a * math.sin((i + 1) * minAngle), -b * math.cos((i + 1) * minAngle)]
        nextPoint = [nextPoint[0] * math.cos(rotateAngle) - nextPoint[1] * math.sin(rotateAngle),
                     nextPoint[0] * math.sin(rotateAngle) + nextPoint[1] * math.cos(rotateAngle)]
        setpos(nextPoint)

```

效果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/a3f41bb3cfa8e1408149f52d4598bbed.png">

### 粽子实现

接着，我们看一下本文最核心的部分-粽子的实现，实现代码如下：

```
# 画粽子
def rice_dumpling():
    pensize(2) # 画笔宽度
    pencolor(2, 51, 12) # 画笔颜色
    fillcolor(4, 77, 19) # 填充色
    begin_fill()
    fd(200) # 向前
    circle(15, 120) #画圆弧
    fd(200)
    circle(15, 120)
    fd(200)
    circle(15, 120)
    fd(200)
    circle(15, 60)
    fd(100)
    circle(15, 90)
    fd(173)
    circle(1, 90)
    end_fill()
    penup()
    fd(100)
    right(60)
    back(105)
    a = pos()
    pendown()
    color(60, 67, 0)
    fillcolor(85, 97, 9)
    begin_fill()
    fd(120)
    goto(a)
    penup()
    back(15)
    left(90)
    fd(20)
    right(90)
    pendown()
    fd(150)
    right(120)
    fd(24)
    right(60)
    fd(120)
    right(60)
    fd(24)
    end_fill()
    begin_fill()
    left(110)
    fd(65)
    left(100)
    fd(24)
    left(80)
    fd(50)
    end_fill()

```

效果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/e033fdf1849e0e6d116b363d9d99a6a6.png">

### 文字实现

我们再接着看一下如何添加文字，比如我要添加的文字是：祝大家端午安康，添加文字实现很容易，只需一行代码即可，代码实现如下：

```
write("祝大家端午安康", move=False, align="center", font=("Comic Sans", 18, "bold"))

```

文中全部代码已经为大家整理好了，有需要的在公众号**Python小二**后台回复**端午**即可获取。

如果大家觉得本文有一点帮助的话，记得随手点个赞支持一下~
