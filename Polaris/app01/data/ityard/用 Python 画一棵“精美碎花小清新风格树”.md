
--- 
title:  用 Python 画一棵“精美碎花小清新风格树” 
tags: []
categories: [] 

---
>  
  作者：1_bit 
  链接：https://urlify.cn/EvMnyi 
 

Turtle库手册可以查询查询python图形绘制库turtle中文开发文档及示例大全（https://urlify.cn/uE7bIb），手册中现有示例，不需要自己动手就可以查看演示。

使用Turtle画树，看了一下网上的代码，基本上核心的方法是使用递归；其次通过递归传参更笔的粗细从而改变绘制时的线段，更改树的躯干大小，在遍历到最后一个节点时，更改笔的颜色及粗细，绘制出树尖的花瓣或绿叶。

本篇博文使用的是网上的代码修改而成的，基本上写来写出简单编写也是使用递归，我也就拿过来用了。本来想顺便把环境也绘制一遍，但是明天上班了，今天还有别的事，就只能作罢，有时间再写一篇把环境都弄好的案例吧；下面是最终代码运行后的结果（代码没优化，效率可能不是很好）：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZzaDM2REJCTWRJcEcxeVNRTjJBMnFBOWNBUGliWmljWU1HS3AwR2xuTVNFNXJTZHFQYlRpY3NpYjZBLzY0MA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVYwSzRianZZbDg4cm9DTW1WUGFLTEhUdnZINzFpY2xTUGxZTnl0bkFQalMxaGN6ZnA3d2hpY0pIdy82NDA?x-oss-process=image/format,png">

感觉有点小清新，哈哈哈，故意配的色，碎花系！

好了，现在开始看看怎么写吧，最终代码在最下面，上面是一步步讲解其中遇见的一些问题。

首先我们使用最简单的方式绘制树的一条躯干，代码如下：

```
from turtle import *


left(80)
fd(100)
right(30)
fd(30)
right(30)
fd(40)
input()

```

结果如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZ3V1ZXb2sxSzlRY1hpYVZ0RTQ5ZkNNQ2d6VDY3T044RUlGNjFYNFQyWHd1azE5QThWOVI5bFVnLzY0MA?x-oss-process=image/format,png">

以上代码首先使用`t.left(80)`让turtle转到几乎垂直于水平线位置，随后使用`t.fd(100)`往剪头所指的方向绘制100个单位的线段，随后`t.right(30)`向右转向30度，再`t.fd(30)`往前绘制30个单位的线段；这个时候线段之间有了一个节点，这个节点就是通过right转动角度后产生的，模拟树的躯干；最后`t.right(30)`再向右转向30度，`t.fd(40)`往前绘制40个单位长度线段，使最后的躯干得到延伸。

不过以上的线段并不适合形容树这个植物，不过别急，我们先更改一下绘制的线段粗细，和颜色，让绘制的图片看起来更像树。

### **color|pensize()**

通过`t.pensize()`、`t.color()`更改笔的粗细与颜色，代码如下：

```
from turtle import *


color('#5E5E5E')
pensize(10)
left(80)
fd(100)
right(30)
fd(30)
right(30)
fd(40)
input()

```

更改好笔的粗细后，绘制的结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVYwcm1Xbmhnd3FuQ3BxVjN4N1BoZWtvR3J3QVFGaWNMalpkaFhNRWxJV3FnSkk5WG90R2diT0dRLzY0MA?x-oss-process=image/format,png">可能结果更像是一根草，不过没关系，我们慢慢更改代码；现在我们加长一下树的枝干和缩小一下笔的粗细：

```
from turtle import *


color('#5E5E5E')
pensize(6)
left(80)
fd(150)
right(30)
fd(50)
right(30)
fd(60)
input()

```

结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZGRTdXNGdibXZsVngwTkVVUTF4WXY4a1hFTGZsRjVxVEpGMElDNXU2cFhpY1g3VmhuN3lFdzZ3LzY0MA?x-oss-process=image/format,png">看起来好了很多，整个树干部分可以分为主要的躯干以及散开的枝条，我们通过可以分为几个部分编写；首先绘制树的主干，随后使用函数绘制树的枝条：

```
from turtle import *


def drawTree(length):
    right(20)
    fd(length)


color('#5E5E5E')
pensize(5)


up()
goto(0,-300)#跳到绘制起始点
down()


left(80)
fd(140)
drawTree(60)
input()

```

运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZsbFVtUnJnc0FxRWljNHZzOGljVzc3OE5lcXBmM0tzQ09oaWJOVTNtRFR3UnJSOEpjdjNnR0w0bEEvNjQw?x-oss-process=image/format,png">

此时代码从最绘制区域最下方开始往上绘制，使用 `color('#5E5E5E')` 设置了绘制颜色；`pensize(5)`设置了绘制的线段粗细；`goto(0,-300)`跳转到了绘制区域的下半部分做为起笔点；随后向左转动80度，画一根线段作为树的主干；之后调用函数 `drawTree(120)` 传入长度进行枝条的绘制，在`drawTree` 函数中，`right(20)`向右侧转动了20度，`fd(length)`画一条线段作为枝条。

既然写了函数，那我们就可以使用递归开始进行枝条的绘制了：

```
from turtle import *


def drawTree(length):
    if length&gt;1:
        right(20)
        fd(length)
        drawTree(length - 10)


color('#5E5E5E')
pensize(5)


up()
goto(0,-300)#跳到绘制起始点
down()


left(80)
fd(140)
drawTree(60)
input()

```

运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZYRnN0QUs3aWF5bXdXRnVyamIyNEhwOTU1MnpqRVNKTjBwZVlka1V6Qm44Zzk3V0xsQTlaUHhBLzY0MA?x-oss-process=image/format,png">从代码上看，只修改了 drawTree 函数部分的代码内容；在函数中使用了递归，递归后传入的值为当前长度减10个长度，并且函数中判断，长度大于1的时候才执行，这样就防止了递归中没有跳出条件而产生的死循环。

现在的长度都是有有固定差值的，使用随机数使绘制的枝条长度随机，更加贴近真实枝条的情况（在此只贴出修改部分的代码）：

```
def drawTree(length):
    if length&gt;1:
        right(20)
        fd(length)
        randlen=random.random()
        drawTree(length - 10*randlen)

```

运行结果：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZpYjZyV0Z5WGRDbnJpY3QzZ1o1RWcySEpIR0tDNXc5a3ExU3pKQ0doS0QwbktjRnBReVNHTWljRXcvNjQw?x-oss-process=image/format,png">代码使用了随机数，随机值与固定差值10进行相减，得到值后参与减法运算。

那么在这里，旋转角度也是固定的，我们再把旋转角度给随机一下：

```
def drawTree(length):
    if length&gt;1:
        randangle=random.random()
        randlen=random.random()
        right(20*randangle)
        fd(length)


        drawTree(length - 10*randlen)

```

运行结果：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZwZ0JGeHhyU2QzRVJPTnFLb21ZQUswamVpY002cDJ2VTkwVm1VbGg0S2lhYnBSSkFBaWM5a0RmZVEvNjQw?x-oss-process=image/format,png">

### **正式开始**

我们的枝条现在只有一个方向，那就是往右，我们现在添加向左的枝条绘制：

```
from turtle import *
import random


def drawTree(length):
    if length&gt;1:
        randangle=random.random()
        randlen=random.random()
        right(20*randangle)
        fd(length)


        drawTree(length - 10*randlen)
        left(40 * randangle)
        fd(length)




color('#5E5E5E')
pensize(5)


up()
goto(0,-300)#跳到绘制起始点
down()


left(80)
fd(140)
drawTree(60)
input()

```

然而出错了：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZhNmNHMkRLNXNIOVR4NVNOdFJFODMwaGtiVWlicDJrSTF0Q2J0SHVndUw1THhTZW1KeXNLcGliQS82NDA?x-oss-process=image/format,png">

### **为什么会这样？**

那是因为我们需要跳转到上一个绘制的位置，使用 backward 函数就可以了，改动 drawTree 函数如下：

```
def drawTree(length):
    if length&gt;1:
        randangle=random.random()
        randlen=random.random()
        right(20*randangle)
        fd(length)
        up()
        backward(length)
        down()
        left(40 * randangle)
        fd(length)
        drawTree(length - 10*randlen)

```

结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZ2YXhVa1UzaWFqSXphdHE0OWJnV3Z0anhaZDNWNThqeElOR2ZBOUkzWUpNR1ZXM2NFSjFaWkRnLzY0MA?x-oss-process=image/format,png">其实这个效果还是不错，不过并不是我们想要的，这个效果可能画狗尾巴草不错；更改一下代码：

```
from turtle import *
import random


def drawTree(length):
    if length&gt;1:
        #随机角度与长度
        randangle=random.random()
        randlen=random.random()


        #每次使用函数先绘制线段，再调整角度，这里是向右的角度转动
        fd(length)
        right(20*randangle)
        drawTree(length - 10*randlen)


        #这里是向左的角度转动
        left(40 * randangle)
        drawTree(length - 10*randlen)


        #为什么需要再向右转20度？那是因为我一共向左转了40度，使用backward后退，必须是相同的角度，不然退回去角度就不同了位置就不会对
        right(20 * randangle)


        up()
        backward(length)
        down()


tracer(False)
color('#5E5E5E')
pensize(5)


up()
goto(0,-300)#跳到绘制起始点
down()


left(80)
fd(140)
drawTree(60)
input()

```

结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZtaWI5ZXZ6a2liZ1lrMWliR1VienltNDJEQ0hTWnFLTVBnR3FRakY1cmdBZFRnQnZndVZPNjhpYjFBLzY0MA?x-oss-process=image/format,png">代码解释在注释里，就是个简单的递归，但是由于传入的 length 长度并不长，导致枝条绘制的线段不是很多，会导致整棵树长的不够茂盛，我们修改一下 length 传入值，改为120，绘制结果如下，注意，由于绘制过久，直接使用 tracer(False) 可以直接显示效果，就没必要绘制一次渲染一下了（这个得看你参数，直接改为False即可）；在此要更改坐标系，自定义为比现在更大的坐标系，不然屏幕显示不全的，使用代码`setworldcoordinates(-1000,-750,1000,750)`即可，整体代码如下：

```
from turtle import *
import random


def drawTree(length):
    if length&gt;1:
        #随机角度与长度
        randangle=random.random()
        randlen=random.random()


        #每次使用函数先绘制线段，再调整角度，这里是向右的角度转动
        fd(length)
        right(20*randangle)
        drawTree(length - 10*randlen)


        #这里是向左的角度转动
        left(40 * randangle)
        drawTree(length - 10*randlen)


        #为什么需要再向右转20度？那是因为我一共向左转了40度，使用backward后退，必须是相同的角度，不然退回去角度就不同了位置就不会对
        right(20 * randangle)


        up()
        backward(length)
        down()


setworldcoordinates(-1000,-750,1000,750)        
tracer(False)
color('#5E5E5E')
pensize(5)


up()
goto(0,-300)#跳到绘制起始点
down()


left(80)
fd(140)
drawTree(120)
input()

```

结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZMZUtUTklmVnVzZmUzVGlhUG4xNWtxSHI3Q3ZpYjJpYUMzWUpkWGd4c0NaajRvaWEyNmRuNDBENXdnLzY0MA?x-oss-process=image/format,png">但是由于随机数的转角和枝条长度没有限制最低的长度，可以在随机的时候给一个合适的数字相乘，并且把起笔位置再往下调，代码如下：

```
randangle=2*random.random()
randlen=2*random.random()
.
.
.
.
.
.
goto(0,-700)

```

结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVY0TTl5OEdJU3JpYll0bWljbHZBT25HVVVpYlA3dW5MSVlacU1MV2ZmaWF0dFJNTnR6eFNvNGpldHRnLzY0MA?x-oss-process=image/format,png">

### **差不多完成了**

一棵树的大致形状绘制好了，现在开始，把树的枝条的绿色和红花填上；一般来说，树的枝条越顶端，那么越小，判断长度这个值，在一定范围内是绿色，一定范围内是红色，那么就可以模拟出树开花和树绿叶的效果了，代码如下，其中的颜色代码，可以自己去调整：

```
from turtle import *
import random


def drawTree(length):
    if length&gt;1:
        if length&lt;30 and length&gt;14:#缩小一下树干
            pensize(4)
        elif length&lt;15 and length&gt;5:#长度这个范围内那么就是绿叶
            color('#04B486')#
            pensize(3)
        elif length&lt;5 and length&gt;1:#红花
            color('#FE2E9A')
            pensize(2)
        else:
            color('#5E5E5E')#其他范围就是正常的树干
            pensize(5)
        #随机角度与长度
        randangle=2*random.random()
        randlen=2*random.random()


        #每次使用函数先绘制线段，再调整角度，这里是向右的角度转动
        fd(length)
        right(20*randangle)
        drawTree(length - 10*randlen)


        #这里是向左的角度转动
        left(40 * randangle)
        drawTree(length - 10*randlen)


        #为什么需要再向右转20度？那是因为我一共向左转了40度，使用backward后退，必须是相同的角度，不然退回去角度就不同了位置就不会对
        right(20 * randangle)


        up()
        backward(length)
        down()


setworldcoordinates(-1000,-750,1000,750)        
tracer(False)
color('#5E5E5E')
pensize(5)


up()
goto(0,-700)#跳到绘制起始点
down()


left(80)
fd(140)
drawTree(120)
input()

```

运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZwT3hnanVMQmlhUlNxdnByYkpRaWJDd29nOUNlVG9iQ01VNU1zMTM5aWNqNkZUS1FaYjlOVG5QQkEvNjQw?x-oss-process=image/format,png">

### **绘制落花**

树有点长的茂盛，哈哈哈；每次随机都是不一样的树形，所以我也不懂它会一个屏幕显示不下，不过关系不大，我们现在开始绘制落叶落花效果。

落花效果的函数如下：

```
def fallingFlowers(m):
    x,y=-1000,-750


    yval=50
    for i in range(m):
        a = 100*random.random()
        b = 2*random.random()
        print(a)
        if a&gt;59:
            color('#FE2E9A')
        else:
            color('#04B486')
        circle(5)
        up()
        goto(x,y+(yval*b))
        fd(a)
        yval+=50
        down()      

```

运行如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZEcDJRNkhDcmhWUnc0MkRQRGxuV091MHNjTndyWEloaWJpY2VDYUo5UHRBRUQwU245dUtqZU9zZy82NDA?x-oss-process=image/format,png">因为我们自己定义的坐标系是 [-1000,-750]到[1000,750]，我们就从左下角的位置开始进行落花的绘制，在代码中定义了x和y坐标的值是 `x,y=-1000,-750`，随后循环里面使用一个y值进行每次的增加，每次绘制的位置从左下角往上走，所以y坐标每次循环都增加，并且赋予随机相乘，这样就会更好的进行随机了，每次都使用`goto(x,y+yval)`跳转到指定的x,y坐标位置，但是在这里要注意，x的值是不变的；并且在循环里我设置了一个a变量，这个变量a主要是用作fd(a)进行x轴上的随机，相同的值就会导致相同的排列，不是很美观，同样随机值b与yval相乘的原因也是这个。

再修改代码，在外层套个循环，使x坐标值相加，横向的铺满绘制区域：

```
from turtle import *
import random


def drawTree(length):
    if length&gt;1:
        if length&lt;30 and length&gt;14:#缩小一下树干
            pensize(4)
        elif length&lt;15 and length&gt;5:#长度这个范围内那么就是绿叶
            color('#04B486')#
            pensize(3)
        elif length&lt;5 and length&gt;1:#红花
            color('#FE2E9A')
            pensize(2)
        else:
            color('#5E5E5E')#其他范围就是正常的树干
            pensize(5)
        #随机角度与长度
        randangle=2*random.random()
        randlen=2*random.random()


        #每次使用函数先绘制线段，再调整角度，这里是向右的角度转动
        fd(length)
        right(20*randangle)
        drawTree(length - 10*randlen)


        #这里是向左的角度转动
        left(40 * randangle)
        drawTree(length - 10*randlen)


        #为什么需要再向右转20度？那是因为我一共向左转了40度，使用backward后退，必须是相同的角度，不然退回去角度就不同了位置就不会对
        right(20 * randangle)


        up()
        backward(length)
        down()
def fallingFlowers(m):
    x,y=-1000,-750
    for i in range(30):
        up()
        goto(x,y)
        x+=100
        down()
        yval=50
        for i in range(m):
            a = 100*random.random()
            b = 2*random.random()
            print(a)
            if a&gt;59:
                color('#FE2E9A')
            else:
                color('#04B486')
            circle(5)
            up()
            goto(x,y+(yval*b))
            fd(a)
            yval+=50
            down()      


setworldcoordinates(-1000,-750,1000,750)        
tracer(False)
color('#5E5E5E')
pensize(5)


# up()
# goto(0,-700)#跳到绘制起始点
# down()


# left(80)
# fd(140)
# drawTree(120)
fallingFlowers(10)
input()

```

运行结果：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVZCMVBoYXFpYlhwdFhLWWlhQ3h2M212TzVpY1JjZ2N5TWdWaWMwdVpoZGljalMzdlZzcVdtYnZpY3lZQncvNjQw?x-oss-process=image/format,png">新增的外层循环使x的值递增，最后平铺满绘制区域下半部分。

### 

### **最终结果**

最后结合树的绘制代码，打开注释，并且设置一下背景色`bgcolor("#F5F6CE")`：

```
from turtle import *
import random


def drawTree(length):
    if length&gt;1:
        if length&lt;30 and length&gt;14:#缩小一下树干
            pensize(4)
        elif length&lt;15 and length&gt;5:#长度这个范围内那么就是绿叶
            color('#04B486')#
            pensize(3)
        elif length&lt;5 and length&gt;1:#红花
            color('#FE2E9A')
            pensize(2)
        else:
            color('#5E5E5E')#其他范围就是正常的树干
            pensize(5)
        #随机角度与长度
        randangle=2*random.random()
        randlen=2*random.random()


        #每次使用函数先绘制线段，再调整角度，这里是向右的角度转动
        fd(length)
        right(20*randangle)
        drawTree(length - 10*randlen)


        #这里是向左的角度转动
        left(40 * randangle)
        drawTree(length - 10*randlen)


        #为什么需要再向右转20度？那是因为我一共向左转了40度，使用backward后退，必须是相同的角度，不然退回去角度就不同了位置就不会对
        right(20 * randangle)


        up()
        backward(length)
        down()
def fallingFlowers(m):
    x,y=-1000,-750
    for i in range(30):
        up()
        goto(x,y)
        x+=100
        down()
        yval=50
        for i in range(m):
            a = 100*random.random()
            b = 2*random.random()
            print(a)
            if a&gt;59:
                color('#FE2E9A')
            else:
                color('#04B486')
            circle(5)
            up()
            goto(x,y+(yval*b))
            fd(a)
            yval+=50
            down()      


setworldcoordinates(-1000,-750,1000,750)        
tracer(False)


fallingFlowers(10)#绘制落叶
bgcolor("#F5F6CE")
color('#5E5E5E')
pensize(5)


up()
goto(0,-700)#跳到绘制起始点
down()


left(80)
fd(140)
drawTree(120)


input()

```

结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzanhlR2E4UkRheVdzQ2ZoRDdjdlo2TVY5eFk3UEg4dXN0VGlhMGZpYTlzM0NHY2hpY2libFFpY3llblUzdlpvNndzZkJ1a2pvc1diWmc1ZklVdy82NDA?x-oss-process=image/format,png">如果觉得落叶落花不够多，可以改一下参数即可。由于代码没优化导致运行效果过慢，之后优化后再贴上来。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">
