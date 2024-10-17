
--- 
title:  几个可以整蛊你朋友的 Python 程序 
tags: []
categories: [] 

---
来源：https://dream.blog.csdn.net

Python 能做很多无聊，但有意思的事情，例如接下来的一些案例。

以下程序，不要发代码，要不实现不了你整蛊的目的。

要打包成一个 `exe` 程序，发给朋友才有意思。

使用 `pip install pyinstaller`。

打包命令如下：

```
pyinstaller -F 文件名.py


```

过程中如果出现 BUG（一般是编码错误），文末有解决方案

### 无聊程序之一 

```
while True:
    n = input("猜猜我在想啥？")
    print("猜错喽")


```

你的朋友将永远无法知道你在想什么。

当然我安装 360 之后，程序没了。有兴趣研究免杀的，可以在给本文点个赞，点赞过 100，我出套 Python 免杀教程。

### 无聊程序之二 

死命弹窗

```
import tkinter.messagebox

while True:
     tkinter.messagebox.showerror('Windows 错误','你的电脑正在被攻击！')


```

运行之后，很就刺激了，如果对方不会杀进程，更刺激。

### 无聊程序之三 

调用默认浏览器，无限打开 CSDN ，让他爱上学习。

```
import webbrowser
while True:
     webbrowser.open('www.csdn.net')


```

额，使用之后，我自己的电脑死机了。

瞬间 CPU…

### 无聊程序之四 

这个程序就动感多了，会随机出现弹窗。

```
import tkinter as tk
import random
import threading
import time


def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('你是一个傻狍子')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='你是一个傻狍子', bg='green',
             font=('宋体', 17), width=20, height=4).pack()
    window.mainloop()


threads = []
for i in range(100):
    t = threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()


```

运行效果如下图所示，非常带劲，可以任意修改。

### 无聊程序之五 

该程序在我看来能排到第一，甚至可以和当下最火的枪茅台案例结合一下。

```
import os
import time
a = """

     oooo oooooooooo.            .oooooo..o                     oooo         o8o  oooo  oooo
     `888 `888'   `Y8b          d8P'    `Y8                     `888         `"'  `888  `888
     888  888      888         Y88bo.       .ooooo.   .ooooo.   888  oooo  oooo   888   888
     888  888      888          `"Y8888o.  d88' `88b d88' `"Y8  888 .8P'   `888   888   888
     888  888      888 8888888      `"Y88b 888ooo888 888        888888.     888   888   888
     888  888     d88'         oo     .d8P 888    .o 888   .o8  888 `88b.   888   888   888
.o. 88P o888bood8P'           8""88888P'  `Y8bod8P' `Y8bod8P' o888o o888o o888o o888o o888o
`Y888P

功能列表：
1.预约商品
2.秒杀抢购商品
"""
print(a)

key = input("请选择:")

if key == "1":
    time.sleep(1.5)
    print('没有预约到\n')
    time.sleep(3)
    print('没事的，来抱一哈\n')

else:
    print("既然如此...")
    time.sleep(3)
    print("那你想得美~~~~~")
    os.system('shutdown -r -t 10')
time.sleep(10)


```

别运行，运行之后别怪我。
