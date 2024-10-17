
--- 
title:  python创意编程大赛作品,python创意编程作品集_python编程大赛作品 
tags: []
categories: [] 

---


#### 目录
- - <ul><li><ul><li><ul><li>- - - - - - - - - - - - 


## 前言

本篇文章给大家谈谈python创意小作品100行代码左右，以及python创意编程大赛作品，希望对各位有所帮助，不要忘了收藏本站喔。

<img src="https://img-blog.csdnimg.cn/img_convert/9ea68a0e8ffd2aeda619a6a3ce5ce645.jpeg#pic_center" alt="">

路漫漫其修远兮，吾将上下而求索

今天自己写了七个小代码，我本着开放的原则向大家全部开放（虽然这个代码没啥技术含量，哈哈），大家可以看看，有没有需要提高的地方，最后谢谢您的观看，希望对您有所帮助。

话不多说，直接上小代码

##### 一 求阶乘

```
#求阶乘
while True: 
  try:
    a=int(input("请输入数字："))
    num=1
    for i in range(a,1,-1):
        num=num*i
    print('%d的阶乘是%d[python和java哪个更值得学](http://17whz.com/54.html "python和java哪个更值得学")。'%(a,num));break
  except:
      print("抱歉，您输入错误,请从新输入：");continue

```

##### 二 彩色螺旋形

```
#螺旋线
import turtle as t 
t.bgcolor("black")
n = 6
colors = ["red","yellow","blue","orange","green","purple"]
for x in range(260):
    t.pencolor(colors[x%6])
    t.forward(x*3/n+x)
    t.left(360/n+1)
    t.width(x*n/200)
t.done()

```

##### 三 计算俩数之间整数的和

```
print("计算俩数之间整数的和")
while True: 
    num=0
    try:
        a=int(input("请输入第一个数："))
        b=int(input("请输入第二个数："))
        if b&gt;=a:
            for i in range(a,b+1):
                print(i);num+=i
            print("%d到%d之间整数的总和是：%d"%(a,b,num));break
        else:
            print("抱歉，第二个数比第一个数小，请从新输入！")
    except:
        print("您输入有误，请从新输入！！");continue

```

##### 四 实现求圆的面积、周长方法（构造方法）

```
#实现求圆的面积周长方法
import math
class Y(object):
    def __init__(self,r):
        self.r=r
    def mianji(self):
     return math.pi*math.pow(self.r,2)
    def zc(self):
     return  2*math.pi*self.r
if __name__ == '__main__':
    a=int(input("请输入你想算的圆的半径："));c=Y(a)
    print("圆的面积是:{:.2f}".format(c.mianji()))
    print("圆的周长是{:.2f}".format(c.zc()))

```

##### 五 计算行列式的代码

```
# 计算行列式
import numpy as aa
a = aa.array([
    [-2,-1,1,0],
    [3,1,-1,1],
    [1,2,-1,1],
    [4,1,3,-1]
])
b = (aa.linalg.det(a))
print(round(b))#round对数字四舍五入

```

##### 六 计算球的体积

```
#计算球的体积
import math
r = int(input("输入球的半径"))
def t(r=r):
    return  (4 * math.pi * r ** 3) / 3
print("球的体积是：",t())

```

##### 七 计算到今天出生多少天

```
#计算出生多少天
import datetime
print("输入的格式 年-月-日 （2002-3-12）")
a = input("输入出生日期：", )
b = datetime.datetime.strptime(a, "%Y-%m-%d")
now = datetime.datetime.now()
r = now - b
print(r)

```

**-END-**

<mark>**读者福利：如果大家对Python感兴趣，这套python学习资料一定对你有用**</mark>

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以根据这些资料规划好学习计划和方向。 


<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习、Python量化交易等习教程。带你从零基础系统性的学好Python！</mark>

## 零基础Python学习资源介绍

① Python所有方向的<mark>学习路线图</mark>，清楚各个方向要学什么东西

② 600多节<mark>Python课程视频</mark>，涵盖必备基础、爬虫和数据分析

③ 100多个<mark>Python实战案例</mark>，含50个超大型项目详解，学习不再是只会理论

④ 20款主流手游迫解 <mark>爬虫手游逆行迫解教程包</mark>

⑤ <mark>爬虫与反爬虫攻防</mark>教程包，含15个大型网站迫解

⑥ <mark>爬虫APP逆向实战</mark>教程包，含45项绝密技术详解

⑦ 超<mark>300本Python电子好书</mark>，从入门到高阶应有尽有

⑧ 华为出品独家<mark>Python漫画教程</mark>，手机也能学习

⑨ 历年互联网企业<mark>Python面试真题</mark>,复习时非常方便

<img src="https://img-blog.csdnimg.cn/7c1055f9bb6e41af9262556bdf20e084.png#pic_center" alt="在这里插入图片描述">

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取哈）**</mark> <img src="https://img-blog.csdnimg.cn/9f969354b48f4e3ab0253e89203deca2.png#pic_center" alt="在这里插入图片描述">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/6cf364e7eeb64b0da07021bce5a59ec6.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

## 资料领取

<mark>这份完整版的Python全套学习资料已为大家备好，朋友们如果需要可以微信扫描下方二维码添加，输入"领取资料" 可免费领取全套资料</mark>【<font color="#CC0033" size="3" face="微软雅黑">有什么需要协作的还可以随时联系我</font>】<mark>朋友圈也会不定时的更新最前言python知识。↓↓↓</mark><font color="red" size="3"> **或者**</font> 【】领取
