
--- 
title:  python好看的流星雨代码,编程流星雨特效怎么弄 
tags: []
categories: [] 

---
这篇文章主要介绍了python好看的流星雨代码，具有一定借鉴价值，需要的朋友可以参考下。希望大家阅读完这篇文章后大有收获，下面让小编带着大家一起了解一下。



<img alt="" height="442" src="https://img-blog.csdnimg.cn/img_convert/9a44bb3d46fc535b12bda037c1b5f5a8.jpeg" width="573">

Source code download: 

### Python之流星雨代码实现



##### 文章目录
- 


```
import turtle as tu
import random as ra

import math

tu.setup(1.0, 1.0)
tu.screensize(1.0, 1.0)    #设置画布大小
tu.bgcolor('black')        #设置画布颜色
t = tu.Pen()
t.ht()                     #隐藏画笔
colors = ['skyblue','white','cyan','aqua']   #流星的颜色列表

class Star():    #流星类

    def __init__(self):
        self.r = ra.randint(50,100)  
        self.t = ra.randint(1,3)
        self.x = ra.randint(-2000,1000)   #流星的横坐标
        self.y = ra.randint(0,500)        #流星的纵坐标
        self.speed = ra.randint(5,10)     #流星移动速度
        self.color = ra.choice(colors)    #流星的颜色
        self.outline = 1                  #流星的大小

    def star(self):                #画流星函数
        t.pensize(self.outline)    #流星的大小
        t.penup()                  #提笔
        t.goto(self.x,self.y)      #随机位置
        t.pendown()                #落笔
        t.color(self.color)        
        t.begin_fill()
        t.fillcolor(self.color)
        t.setheading(-30)
        t.right(self.t)
        t.forward(self.r)
        t.left(self.t)
        t.circle(self.r*math.sin(math.radians(self.t)),180)
        t.left(self.t)
        t.forward(self.r)
        t.end_fill()   

    def move(self):                   #流星移动函数
        if self.y &gt;= -500:            #当流星还在画布中时
            self.y -= self.speed      #设置上下移动速度
            self.x += 2*self.speed    #设置左右移动速度
        else:                     
            self.r = ra.randint(50,100)
            self.t = ra.randint(1,3)
            self.x = ra.randint(-2000,1000)
            self.y = 500
            self.speed = ra.randint(5,10)
            self.color = ra.choice(colors)
            self.outline = 1

Stars = []            #用列表保存所有流星

for i in range(100):     
    Stars.append(Star())      

while True:           #开始绘制
    tu.tracer(0)
    t.clear()
    for i in range(100):    #80个流星
        Stars[i].move()
        Stars[i].star()
    tu.update()

tu.mainloop()

```


