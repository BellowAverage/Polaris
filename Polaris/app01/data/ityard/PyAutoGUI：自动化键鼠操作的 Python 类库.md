
--- 
title:  PyAutoGUI：自动化键鼠操作的 Python 类库 
tags: []
categories: [] 

---
来源：https://www.toutiao.com/a6827183521623179788

有些朋友可能玩过按键精灵，一个用来操作键盘鼠标完成一些自动化工作的软件。其实如果你学了Python的话，完全用不着按键精灵这种东西了。因为广泛的Python类库里，就有PyAutoGUI这样可以变成控制键盘鼠标的类库，有了它，就可以用Python随心所欲的操作电脑了。而且这个类库是跨平台的，Windows、Linux、macOS都可以用，是不是很吸引人呢？

<img src="https://img-blog.csdnimg.cn/img_convert/fd0c62c020907896a8f09aaf87ac85ad.png">安装和使用

安装PyAutoGUI非常简单，从pip安装即可。

```
pip install pyautogui
```

<img src="https://img-blog.csdnimg.cn/img_convert/6dca3c10cb8216eadcd3aafe4d5aedec.png">这里顺便介绍一下PyAutoGUI的坐标系统，和一些常见的绘图坐标系统相同，左上角为原点，向右是x轴正方向，向下是y轴正方向。假如你的屏幕是1920*1080，那么右下角的坐标就是(1919, 1079)，因为坐标是从0开始的，而不是从1开始的，这一点要格外注意。

PyAutoGUI虽然有很多函数，但是函数的作用基本上就是单击/双击鼠标、敲击/按下/弹起按键这样的，函数参数也就是点击间隔、点击按键这样很简单的参数。所以我就不列例子了，总之用起来非常简单。

## 函数简介

下面来介绍一下PyAutoGUI的函数。先来看看鼠标操作函数，主要是点击、拖动、滑动滚轮这些操作。

<img src="https://img-blog.csdnimg.cn/img_convert/0628f7ca6d524f19c5f7cbb079aadc6c.png">

键盘操作函数，主要就是按键、组合键操作。

<img src="https://img-blog.csdnimg.cn/img_convert/1c311242ad05e807ccf25cf27828ff85.png">

提示框函数，可以用来显示警告、确认、提示和密码输入对话框，增强程序可操作性。显示对话框的时候，程序会暂停，直到用户处理对话框。

<img src="https://img-blog.csdnimg.cn/img_convert/a25ab6c837ab6db4d4899daddaaa6379.png">截图函数，可以从屏幕上截图，也可以根据已有图片从屏幕上定位。主要用途是事先保存一些按钮图片，然后从屏幕上识别定位来点击按钮。

<img src="https://img-blog.csdnimg.cn/img_convert/7fe2ad5a1262ef28eab71c9fc6c6cd7d.png">

## 操作实例

首先来看看官网的一个画图例子，我们需要打开一个画图程序的窗口，然后将它放到全屏。然后运行下面的代码，然后切换到画图窗口。等待3秒钟以后就可以看到PyAutoGUI开始画图了。

```
import pyautogui

distance = 100
pyautogui.moveTo(400, 300)
while distance &gt; 0:
    pyautogui.drag(distance, 0, duration=0.1)
    distance -= 5
    pyautogui.drag(0, distance, duration=0.1)
    pyautogui.drag(-distance, 0, duration=0.1)
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.1)

```

结果如下。其实这个画图的代码很简单，就是一圈一圈缩小，然后调用drag函数拖住画笔不放。

<img src="https://img-blog.csdnimg.cn/img_convert/6faf5e96a931c6664971eb2abfff619c.png">

再来看一个图片识别的例子，这个例子需要先安装OpenCV库和opencv-python包。安装之后就可以运行下面的例子了。这个例子保存了windows 10计算机的几个按钮截图，然后通过图形识别的方式找到并点击按钮执行操作。注意下面用到了confidence参数，即使图片没有完全匹配也可以识别到。

```
import pyautogui
import time

time.sleep(3)

# Windows计算器的按钮截图
five = '5.png'
eight = '8.png'
multiply = 'multiply.png'
equals = 'equals.png'

# 图片识别和点击的函数


def find_and_click(image):
    x, y = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    pyautogui.click(x, y)


# 执行5*8=
find_and_click(five)
find_and_click(multiply)
find_and_click(eight)
find_and_click(equals)

```

代码以及图片的完整例子可以查看我的github，地址如下。

```
https://github.com/techstay/python-study/tree/master/pyautogui-sample
```

通过PyAutoGUI，你可以轻松的对图形界面进行自动化编程，按照屏幕位置或者图片识别来定位控件的位置，然后通过编程来控制鼠标和键盘输入。这和按键精灵的道理是一样的。但是Python可以利用广泛的第三方包来实现更多的功能，这一点是按键精灵无法相比的。

<img src="https://img-blog.csdnimg.cn/img_convert/bb5469eec5404798b50f3a9533fe34f6.gif">
