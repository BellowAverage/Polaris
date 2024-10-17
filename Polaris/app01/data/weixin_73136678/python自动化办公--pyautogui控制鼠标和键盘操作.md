
--- 
title:  python自动化办公--pyautogui控制鼠标和键盘操作 
tags: []
categories: [] 

---
在公司某些工作场景下，需要大量重复的工作，重复的工作完全可以通过python软件的自动化实现，省时省力。本文分享python自动化办公的利器之一--pyautogui，通过pyautogui可以轻松控制鼠标和键盘操作。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/8899086abeb67c817d3f1dffd540d362.webp?x-oss-process=image/format,png">

PyAutoGUI是一个纯Python的GUI自动化工具，其目的是可以用程序自动控制鼠标和键盘操作，多平台支持（Windows，OS X，Linux）。

**1、安装**

```
pip3 install pyautogui
复制代码
```

**2、pyautogui鼠标操作样例**

```


import pyautogui
# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()
 
# 2秒钟鼠标移动坐标为100,100位置  绝对移动
pyautogui.moveTo(x=100, y=100,duration=2, tween=pyautogui.linear)
 
#鼠标移到屏幕中央。
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
 
# 鼠标左击一次
#pyautogui.click()
# x 
# y 
# clicks 点击次数
# interval点击之间的间隔
# button 'left', 'middle', 'right' 对应鼠标 左 中 右或者取值(1, 2, or 3)
# tween 渐变函数
pyautogui.click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)
 
# 鼠标相对移动 ,向下移动
#pyautogui.moveRel(None, 10)
pyautogui.moveRel(xOffset=None, yOffset=10,duration=0.0, tween=pyautogui.linear)
 
 
# 鼠标当前位置0间隔双击
#pyautogui.doubleClick()
pyautogui.doubleClick(x=None, y=None, interval=0.0, button='left', duration=0.0, twe
```
