
--- 
title:  《Turtle绘图》Python用Turtle库绘制多啦爱梦、小猪佩奇、皮卡丘等卡通人物 
tags: []
categories: [] 

---
https://blog.csdn.net/meenr/article/details/107245170 

#### 目录
- - <ul><li>- <ul><li>- - - - - - - - - - 


## 利用Turtle库绘制卡通人物形象

Turtle库：Turtle(海龟)绘图很适合用来引导孩子学习编程。 最初来自于 Wally Feurzeig, Seymour Papert 和 Cynthia Solomon 于 1967 年所创造的 Logo 编程语言。使用Turtle绘图可以编写重复执行简单动作的程序画出精细复杂的形状。

本文的主要内容是综合整理了网络上几种使用Python的Turtle库来绘制一些卡通人物，如多啦爱梦、小猪佩奇和皮卡丘等的资源。亲测了运行效果并略作改进，下面将依次展示效果图与参考代码。（部分内容文末已标明出处）

```
                                                                           ——2贰进制

```

### 多啦爱梦的绘制

#### exe可执行文件

该部分已经封装成.exe可执行文件，下载后直接解压即可在无python环境的Windows系统PC端直接运行，表白、送小朋友神器。 **演示视频：**  https://www.bilibili.com/video/BV1fb4y1z7Z4/  https://mp.weixin.qq.com/s/VgxdRL2tPV-SGf2HNV3H1g **资源下载地址：** https://download.csdn.net/download/meenr/12598183 ****

```
                                                               ——2贰进制

```

#### 运行效果图

话不多说看效果，上代码 <img src="https://img-blog.csdnimg.cn/20200710144906150.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="380" height="500">

#### 源代码

下面是用turtle绘制多啦爱梦的全部参考代码。

```
# -*- coding: utf-8 -*-
'''=============================
#@Project : TurtleEg
#@File    : 多啦爱梦
#@Software: pyIDLE3.6
#@Author  : Violet
#@Date    : 2020/6/27 
#@Desc    : turtle绘制多啦爱梦
================================'''
from turtle import *

# 无轨迹跳跃
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()

# 眼睛
def eyes():
    fillcolor("#ffffff")
    begin_fill()

    if 0 &lt;= i &lt; 30 or 60 &lt;= i &lt; 90:
        a -= 0.05
        lt(3)
        fd(a)
    else:
        a += 0.05
        lt(3)
        fd(a)
    tracer(True)
    end_fill()


# 胡须
def beard():
    my_goto(-32, 135)
    my_goto(-32, 115)
    seth(193)
    fd(60)

    my_goto(37, 135)
    seth(15)
    fd(60)

    my_goto(37, 125)
    seth(0)
    fd(60)

    my_goto(37, 115)
    seth(-13)
    fd(60)

# 嘴巴
def mouth():
    my_goto(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)

# 围巾
def scarf():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()

# 鼻子
def nose():
    my_goto(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()

# 黑眼睛
def black_eyes():
    seth(0)
    my_goto(-20, 195)
    circle(13)
    end_fill()

    pensize(6)
    my_goto(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    my_goto(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    my_goto(0, 0)

# 脸
def face():
    fd(183)
    lt(45)
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    my_goto(63.56,218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)

# 头型
def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()

# 画哆啦A梦
def Doraemon():
    # 头部
    head()
    # 围脖
    scarf()
    # 脸
    face()
    # 红鼻子
    nose()
    # 嘴巴
    mouth()
    # 胡须
    beard()
    # 身体
    my_goto(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)

    fillcolor('#00a0de')
    begin_fill()

    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    # print(pos())

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)
    seth(100)
    circle(-1000, 9)
    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)
    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()

    # 左手
    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()

    # 脚
    my_goto(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()

    my_goto(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()

    # 右手
    my_goto(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()

    # 口袋
    my_goto(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    my_goto(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)

    #铃铛
    my_goto(-103.42, 15.09)
    fd(90)
    seth(70)
    fillcolor('#ffd200')
    # print(pos())
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180-10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    my_goto(0, -150)

    # 画眼睛
    black_eyes()

if __name__ == '__main__':
    screensize(800,600, "#f0f0f0")
    pensize(3)  # 画笔宽度
    speed(9)    # 画笔速度
    Doraemon()
    my_goto(100, -300)
    write('by Violet', font=("Bradley Hand ITC", 30, "bold"))
    mainloop()


```

### 皮卡丘的绘制（头像和全身像）

#### 皮卡丘头像运行效果图

<img src="https://img-blog.csdnimg.cn/20200710145105957.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="350" height="350">

#### 皮卡丘头像代码

下面展示一些用turtle绘制皮卡丘头像的参考代码

```
# -*- coding: utf-8 -*-
'''=============================
#@Project : TurtleEg
#@File    : 皮卡丘
#@Software: pyIDLE3.6
#@Author  : Violet
#@Date    : 2020/6/27 
#@Desc    : turtle绘制皮卡丘
================================'''
from turtle import *
'''
绘制皮卡丘头部
'''
def face(x,y):
     """画脸"""
     begin_fill()
     penup()
     # 将海龟移动到指定的坐标
     goto(x, y)
     pendown()
     # 设置海龟的方向
     setheading(40)
     
     circle(-150, 69)
     fillcolor("#FBD624")
     # 将海龟移动到指定的坐标
      
     penup()
     goto(53.14, 113.29)
     pendown()
      
     setheading(300)
     circle(-150, 30)
     setheading(295)
     circle(-140, 20)

     forward(5)
     setheading(260)
     circle(-80, 70)
   
     penup()
     goto(-74.43,-79.09)
     pendown()
     
     penup()
     # 将海龟移动到指定的坐标
     goto(-144,103)
     pendown()
     setheading(242)
     circle(110, 35)
     right(10)
     forward(10)
     setheading(250)
     circle(80, 115)
    
     penup()
     goto(-74.43,-79.09)
     pendown()
     setheading(10)
     penup()
     goto(-144, 103)
     
     pendown()
     penup()
     goto(x, y)
     pendown()
     
     end_fill()
     
     # 下巴
     penup()
     goto(-50, -82.09)
     pendown()
     pencolor("#DDA120")
     fillcolor("#DDA120")
     begin_fill()
     setheading(-12)
     circle(120, 25)
     setheading(-145)
     forward(30)
     setheading(180)
     circle(-20, 20)
     setheading(143)
     forward(30)
     end_fill()
    
 
def eye():
     """画眼睛"""
     # 左眼
     color("black","black")
     penup()
     goto(-110, 27)
     pendown()
     begin_fill()
     setheading(0)
     circle(24)
     end_fill()
     # 左眼仁
     color("white", "white")
     penup()
     goto(-105, 51)
     pendown()
     begin_fill()
     setheading(0)
     circle(10)
     end_fill()
     # 右眼
     color("black", "black")
     penup()
     goto(25, 40)
     pendown()
     begin_fill()
     setheading(0)
     circle(24)
     end_fill()
     # 右眼仁
     color("white", "white")
     penup()
     goto(17, 62)
     pendown()
     begin_fill()
     setheading(0)
     circle(10)
     end_fill()
     
def cheek():
     """画脸颊"""
     # 右边
     color("#9E4406", "#FE2C21")
     penup()
     goto(-130, -50)
     pendown()
     begin_fill()
     setheading(0)
     circle(27)
     end_fill()
     
     # 左边
     color("#9E4406", "#FE2C21")
     penup()
     goto(53, -20)
     pendown()
     begin_fill()
     setheading(0)
     circle(27)
     end_fill()
     

```

#### 皮卡丘全身运行效果图

<img src="https://img-blog.csdnimg.cn/20200710145134215.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="450" height="450">

#### 皮卡丘全身像代码

下面展示一些用turtle绘制皮卡丘全身像的参考代码

```

# -*- coding: utf-8 -*-
'''=============================
#@Project : TurtleEg
#@File    : 皮卡丘全身像
#@Software: PyCharm
#@Author  : Violet
#@Date    : 2020/6/27 
#@Desc    : turtle绘制帽子皮卡丘
================================'''
import turtle

def getPosition(x, y):
        turtle.setx(x)
        turtle.sety(y)
        print(x, y)

class Pikachu:
    def __init__(self):
        self.t = turtle.Turtle()
        t = self.t
        t.pensize(3)
        t.speed(9)
        t.ondrag(getPosition)
        
    def noTrace_goto(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def leftEye(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.noTrace_goto(x, y+10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.noTrace_goto(x+6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def rightEye(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.noTrace_goto(x, y+10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.noTrace_goto(x-6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def mouth(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t

        t.fillcolor('#88141D')
        t.begin_fill()
        # 下嘴唇
        l1 = []
        l2 = []
        t.seth(190)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.right(3)
            t.fd(a)
            l1.append(t.position())
        
        self.noTrace_goto(x, y)
        
        t.seth(10)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.left(3)
            t.fd(a)
            l2.append(t.position())
        
        # 上嘴唇
        
        t.seth(10)
        t.circle(50, 15)
        t.left(180)
        t.circle(-50, 15)
        
        t.circle(-50, 40)
        t.seth(233)
        t.circle(-50, 55)
        t.left(180)
        t.circle(50, 12.1)
        t.end_fill()

        # 舌头
        self.noTrace_goto(17, 54)
        t.fillcolor('#DD716F')
        t.begin_fill()
        t.seth(145)
        t.circle(40, 86)
        t.penup()
        for pos in reversed(l1[:20]):
            t.goto(pos[0], pos[1]+1.5)
        for pos in l2[:20]:
            t.goto(pos[0], pos[1]+1.5)
        t.pendown()
        t.end_fill()

        # 鼻子
        self.noTrace_goto(-17, 94)
        t.seth(8)
        t.fd(4)
        t.back(8)
        
    # 红脸颊
    def leftCheek(self, x, y):
        turtle.tracer(False)
        t = self.t
        self.noTrace_goto(x, y)
        t.seth(300)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 &lt;= i &lt; 30 or 60 &lt;= i &lt; 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def rightCheek(self, x, y):
        t = self.t
        turtle.tracer(False)
        self.noTrace_goto(x, y)
        t.seth(60)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
      

   

```

### 直接获取.py源文件

因为源代码太多，篇幅的原因，读者如需要全部参考代码可通过下面两种途径获取

#### 一

第一步：扫描下方二维码，或打开微信搜索并关注“**2贰进制**”公主号； 第二步：回复:“ **turtle卡通人物** ”即可获取。 <img src="https://img-blog.csdnimg.cn/2020070300554991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="二维码" width="250" height="250">

#### 二

也可扫描下方二维码，加入学习交流QQ群“ **480558240** ”，联系管理员获取包括但不限于本篇内容的更多学习资料。 <img src="https://img-blog.csdnimg.cn/2020071217121655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="300" height="300"> **2贰进制–Echo 2020年6月** 如果您觉得本文还不错，请点赞＋评论＋收藏或关注！ 如果本文对你有所帮助，解决了您的困扰，可以通过赞赏来给予我更大支持： <img src="https://img-blog.csdnimg.cn/20210424133535613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="400" height="200"> 此致 感谢您的阅读、点赞、评论、收藏与打赏。

### 小猪佩奇的绘制

#### 小猪佩奇运行效果图

<img src="https://img-blog.csdnimg.cn/20200710145235856.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="350" height="450">

#### 小猪佩奇代码

下面展示一些用turtle绘制小猪佩奇的参考代码

```
# -*- coding: utf-8 -*-
'''=============================
#@Project : TurtleEg
#@File    : 小猪佩奇
#@Software: PyCharm
#@Author  : Violet
#@Date    : 2020/6/27 
#@Desc    :turtle绘制小猪佩奇
================================'''

import turtle as t

t.pensize(4)
t.hideturtle()
t.colormode(255)
t.color((255,155,192),"pink")
t.setup(840,500)
t.speed(10)

#鼻子
t.pu()
t.goto(-100,100)
t.pd()
t.seth(-30)
t.begin_fill()
a=0.4
for i in range(120):
    if 0&lt;=i&lt;30 or 60&lt;=i&lt;90:
        a=a+0.08
        t.lt(3) #向左转3度
        t.fd(a) #向前走a的步长
    else:
        a=a-0.08
        t.lt(3)
        t.fd(a)
t.end_fill()

t.pu()
t.seth(90)
t.fd(25)
t.seth(0)
t.fd(10)
t.pd()
t.pencolor(255,155,192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160,82,45)
t.end_fill()

t.pu()
t.seth(0)
t.fd(20)
t.pd()
t.pencolor(255,155,192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160,82,45)
t.end_fill()

#头
t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(41)
t.seth(0)
t.fd(0)
t.pd()
t.begin_fill()
t.seth(180)
t.circle(300,-30)
t.circle(100,-60)
t.circle(80,-100)
t.circle(150,-20)
t.circle(60,-95)
t.seth(161)
t.circle(-300,15)
t.pu()
t.goto(-100,100)
t.pd()
t.seth(-30)
a=0.4
for i in range(60):
    if 0&lt;=i&lt;30 or 60&lt;=i&lt;90:
        a=a+0.08
        t.lt(3) #向左转3度
        t.fd(a) #向前走a的步长
    else:
        a=a-0.08
        t.lt(3)
        t.fd(a)
t.end_fill()

#耳朵
t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(-7)
t.seth(0)
t.fd(70)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50,50)
t.circle(-10,120)
t.circle(-50,54)
t.end_fill()

t.pu()
t.seth(90)
t.fd(-12)
t.seth(0)
t.fd(30)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50,50)
t.circle(-10,120)
t.circle(-50,56)
t.end_fill()

#眼睛
t.color((255,155,192),"white")
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-95)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()

t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()

t.color((255,155,192),"white")
t.pu()
t.seth(90)
t.fd(-25)
t.seth(0)
t.fd(40)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()

t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()

#腮
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(-95)
t.seth(0)
t.fd(65)
t.pd()
t.begin_fill()
t.circle(30)
t.end_fill()

#嘴
t.color(239,69,19)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(-100)
t.pd()
t.seth(-80)
t.circle(30,40)
t.circle(40,80)



```
