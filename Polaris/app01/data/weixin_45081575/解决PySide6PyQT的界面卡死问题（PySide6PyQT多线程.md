
--- 
title:  解决PySide6/PyQT的界面卡死问题（PySide6/PyQT多线程 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/aadac4d214184d1cb0eb8f26de64c93d.jpeg#pic_center" alt="">

## 前言

>  
 问：在使用 `PySide6` 时候，会出现应用程序卡死的问题。 


>  
 答：为什么会出现这个问题呢？`PySide6` 应用程序是基于事件驱动的，主线程负责处理**GUI**事件。如果有耗时的操作任务，**GUI** 事件将被阻塞，应用程序会处于一个假死（`crash`）的状态。这个时候我们是无法同应用程序进行交互，只能等待任务完成并返回结果。 


本篇文章来尝试来解决这个问题。

## 知识点📖📖

为了避免这种情况，我们应该将长时间运行的任务移动到单独的线程中执行。 这样，既可以在后台执行任务，又能保持应用程序的响应性（不会`crash`

而在`PySide6`中，可以使用这些线程类去（**QThread、QObject、QRunnable 和 QtConcurrent**）创建线程多线程，并采用 **信号和槽机制** 来将线程中的结果回传到主线程。

本文使用**QThread**来做介绍，因为使用方法都大差不差(值得注意的是，**QThread** 继承了 **QObject**

<font size="1" color="blue">关于信号和槽机制，我会再起一篇文章来对它进行介绍。</font>

## 实现

下面实现一个简单窗口，用于模拟耗时的操作任务从而导致线程阻塞。

### 主线程阻塞

#### 代码

>  
 以下代码是一个简单的窗口，包含一个按钮和一个标签。 当点击按钮时候，会请求10次 `https://www.csdn.net/`，且每次睡眠1秒，并将请求结果和请求次数在标签上逐次打印出来。 


```
# -*- coding: utf-8 -*-


import time

import requests

from PySide6.QtCore import QSize

from PySide6.QtWidgets import (QApplication, QPushButton, QLabel, QVBoxLayout, QWidget)


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setup_ui()
        #
        self.button.clicked.connect(self.setup_thread)

    def setup_ui(self):
        self.setWindowTitle('demo')
        self.resize(QSize(250, 180))
        # 创建一个垂直布局
        layout = QVBoxLayout()
        # 创建一个标签
        self.label = QLabel('This is a label =&gt; ')
        layout.addWidget(self.label)
        # 创建一个按钮
        self.button = QPushButton('Send Request')
        layout.addWidget(self.button)
        # 将布局设置为主窗口的布局
        self.setLayout(layout)
        # 显示窗口
        self.show()

    def setup_thread(self):
        for idx in range(1, 11):
            time.sleep(1)
            res = requests.get('https://www.csdn.net/').text[:15]
            self.thread_finished((idx, res))

    def thread_finished(self, item):
        self.label.setText('This is a label =&gt; ' + str(item))


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

```

#### 效果

**窗口长这样：** <img src="https://img-blog.csdnimg.cn/2faf4427a32c4a08a20eff1fabd32698.png" alt="在这里插入图片描述"> **运行效果这样：**

理想的情况应该是打印10次请求次数和内容，但这里的标签只打印了第10次。很显然，这不是我们想要的。

因为有**time.sleep**耗时的任务，**GUI** 事件被阻塞，应用程序处于假死（`crash`）的状态。

<img src="https://img-blog.csdnimg.cn/b1c0dde4e64443c5a6ae6d43c53e76cc.gif#pic_center" alt="在这里插入图片描述">

### 使用QApplication.processEvents()

作用：用于处理当前事件队列中的所有事件，它的作用是让应用程序立即处理所有等待中的事件，并且能够让界面更加流畅，避免长时间的界面卡顿。

#### 代码

在**setup_thread**函数后面添加一行 `QApplication.processEvents()`

```
def setup_thread(self):
	for idx in range(1, 11):
	    time.sleep(1)
	    res = requests.get('https://www.csdn.net/').text[:15]
	    self.thread_finished((idx, res))
	    QApplication.processEvents()

```

#### 效果

可以看到，现在实时打印出请求的次数和内容了！ 它有用，但不是很有用！因为还有些卡顿。

<img src="https://img-blog.csdnimg.cn/233d11e5dfd743c9811a6cdbaf0cb706.gif" alt="请添加图片描述">

### 使用 <font color="bluesky" size="4">**QThread多线程** </font>

#### 代码

>  
 这一份代码与上面的代码作用一致，区别在于它用上了多线程。 


这里的 **MyThread**继承了**QThread**类，在 **PySide6** 中，**QThread** 是一个线程类，可以用来创建新线程。 这里重写了**run**方法，当线程的 **start()** 方法被调用时，就会自动执行该方法。 点击按钮会触发 **setup_thread** 方法，在该方法中会创建线程类 **MyThread** 的实例并启动该线程。

```
# -*- coding: utf-8 -*-

import time

import requests

from PySide6.QtCore import (QThread, Signal, Slot, QSize)
from PySide6.QtWidgets import (QApplication, QPushButton, QLabel, QVBoxLayout, QWidget)


class MyThread(QThread):
    signal_tuple = Signal(tuple)

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.count: int = kwargs.get('count')

    def run(self):
        for idx in range(1, self.count + 1):
            result = self.func(*self.args)
            time.sleep(1)
            # 任务完成后发出信号
            self.signal_tuple.emit((idx, result))


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setup_ui()
        #
        self.button.clicked.connect(self.setup_thread)

    def setup_ui(self):
        self.setWindowTitle('demo')
        self.resize(QSize(250, 180))
        # 创建一个垂直布局
        layout = QVBoxLayout()
        # 创建一个标签
        self.label = QLabel('This is a label =&gt; ')
        layout.addWidget(self.label)
        # 创建一个按钮
        self.button = QPushButton('Send Request')
        layout.addWidget(self.button)
        # 将布局设置为主窗口的布局
        self.setLayout(layout)
        # 显示窗口
        self.show()

    def setup_thread(self):
        self.thread_ = MyThread(self.send_request,
                                count=10)
        self.thread_.signal_tuple.connect(self.thread_finished)
        self.thread_.start()

    def send_request(self):
        return requests.get('https://www.csdn.net/').text[:15]

    @Slot(tuple)
    def thread_finished(self, item):
        self.label.setText('This is a label =&gt; ' + str(item))


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


```

#### 效果

效果很完美，应用程序没有丝毫卡顿，10次请求的也逐次在标签上打印出来。

<img src="https://img-blog.csdnimg.cn/4f391f2f18b54ba396211670a2b0cd65.gif" alt="请添加图片描述">

### <font color="red">总结</font>

多线程效果很不错！

## 后话

本次分享到此结束， see you~~🐱‍🏍🐱‍🏍
