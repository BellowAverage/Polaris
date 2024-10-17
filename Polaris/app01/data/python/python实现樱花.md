
--- 
title:  python实现樱花 
tags: []
categories: [] 

---
****python实现樱花****

代码如下：

```
from turtle import *
from random import *
from math import *
def tree(n, l):
    pd ()  # 下笔
    # 阴影效果
    t = cos ( radians ( heading () + 45 ) ) / 8 + 0.25
    pencolor ( t, t, t )
    pensize ( n / 3 )
    forward ( l )  # 画树枝

    if n &gt; 0:
        b = random () * 15 + 10  # 右分支偏转角度
        c = random () * 15 + 10  # 左分支偏转角度
        d = l * (random () * 0.25 + 0.7)  # 下一个分支的长度
        # 右转一定角度,画右分支
        right ( b )
        tree ( n - 1, d )
        # 左转一定角度，画左分支
        left ( b + c )
        tree ( n - 1, d )
        # 转回来
        right ( c )
    else:
        # 画叶子
        right ( 90 )
        n = cos ( radians ( heading () - 45 ) ) / 4 + 0.5
        ran = random ()
        # 这里相比于原来随机添加了填充的圆圈，让樱花叶子看起来更多一点
        if (ran &gt; 0.7):
            begin_fill ()
            circle ( 3 )
            fillcolor ( 'pink' )
        # 把原来随机生成的叶子换成了统一的粉色
        pencolor ( "pink" )
        circle ( 3 )
        if (ran &gt; 0.7):
            end_fill ()
        left ( 90 )
        # 添加0.3倍的飘落叶子
        if (random () &gt; 0.7):
            pu ()
            # 飘落
            t = heading ()
            an = -40 + random () * 40
            setheading ( an )
            dis = int ( 800 * random () * 0.5 + 400 * random () * 0.3 + 200 * random () * 0.2 )
            forward ( dis )
            setheading ( t )
            # 画叶子
            pd ()
            right ( 90 )
            n = cos ( radians ( heading () - 45 ) ) / 4 + 0.5
            pencolor ( n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4 )
            circle ( 2 )
            left ( 90 )
            pu ()
            # 返回
            t = heading ()
            setheading ( an )
            backward ( dis )
            setheading ( t )
    pu ()
    backward ( l )  # 退回


bgcolor ( 0.956, 0.9255, 0.9882 )  # 设置背景色（把灰色换成淡紫色）
ht ()  # 隐藏turtle
speed ( 0 )  # 速度 1-10渐进，0 最快
tracer ( 0, 0 )
pu ()  # 抬笔
backward ( 50 )
left ( 90 )  # 左转90度
pu ()  # 抬笔
backward ( 300 )  # 后退300
tree ( 12, 100 )  # 递归7层
done ()


```

效果如下：

<img src="https://img-blog.csdnimg.cn/6c3ff1e5a2d5443a91c131e8fd3eb22c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAamVmZiBvbmU=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="请添加图片描述">
