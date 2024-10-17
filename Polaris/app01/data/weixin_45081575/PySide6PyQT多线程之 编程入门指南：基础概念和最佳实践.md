
--- 
title:  PySide6/PyQT多线程之 编程入门指南：基础概念和最佳实践 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/f7369f6cbf92407999c2c4ebb9df8df8.jpeg#pic_center" alt="在这里插入图片描述">

## 前言

>  
 本篇文章介绍 **PySide6/PyQT**多线程编程的基本概念，用到的知识点，以及**PySide6/PyQT**多线程的基本使用。 


看多线程介绍，就看 <font color="bluegreen"> **知识点📖📖**</font> ；

看多线程代码，就看 <font color="bluegreen"> **实现**</font> 。

## 知识点📖📖

本文用到的几个**PySide6**的知识点及链接。

|作用|链接
|------
|创建新线程|
|对象间通信的机制，允许对象发送和接收信号|
|用于响应**Signal信号**的方法|
|互斥锁，用于保护对象|
|与 **QMutex**一起使用|
||

### 多线程模块

值得注意的是在 **PySide6/PyQT** 中实现多线程，可以选择的有很多，有 <font color="bluesky"> QObject、QThread、QRunnable、QThreadPool</font> 等；
- 其中**QThread**是继承了**QObject** 的类，它可以作为基类来创建自定义的线程类；- **QThreadPool** 是一个线程池类，它管理着一组线程，可以方便地调度和管理线程的执行；- **QRunnable** 是一个任务接口，用于将任务封装为一个可在后台线程中执行的对象。可以通过继承 **QRunnable** 类来实现自定义的任务，并在 **QThreadPool** 中执行。
### 多线程通信和同步

>  
 在多线程的编程中，线程之间的**通信和同步**是绕不开的话题。 


<font color="bluegreenyellow"> **通信：**</font>
- **PySide6/PyQT** 提供了**信号槽（Signal and Slot）** 机制，它们用于在线程之间传递消息和触发事件。通过在不同的线程中发送信号和连接槽函数，可以实现线程间的通信。
<font color="bluegreenyellow"> **同步：**</font>
- 在共享对象被多个线程同时访问时候容易出现意料之外的问题，需要保护好资源争夺；- 互斥锁（**QMutex**）和条件变量（**QWaitCondition**）等同步机制可以用于控制线程的并发访问，确保线程安全和避免线程竞争。
### 多线程异常

这个较为通俗易懂，一般来说 使用 **try-except** 去捕获线程内部可能发生的异常，并在 **except** 语句块中处理异常即可。

异常处理：
- 在捕获到异常后，可以选择重新尝试操作、回退到安全状态、释放资源、打印错误信息等。
当然，也可以在异常时候 使用**signal**信号发送异常的消息。（示例代码如下

```
from PySide6.QtCore import QThread, Signal

class MyThread(QThread):
    # 定义一个线程崩溃的信号
    thread_crashed = Signal(Exception)

    def run(self):
        try:
            # 线程的执行逻辑
            pass
        except Exception as e:
            # 发送线程崩溃的信号
            self.thread_crashed.emit(e)

```

### 多线程生命周期

>  
 线程的生命周期包括：线程的创建、启动、运行、暂停、恢复和终止等阶段。 


在使用多线程时候，需要注意多线程的生命周期。因为合理管理线程的生命周期可以避免线程资源的浪费和泄漏。
-  如果是使用**QThread**，则需要手动处理这些操作，否则可能会导致资源泄漏或线程的未正常退出。 -  如果是使用 **QRunnbale + QThreadPool**，主线程则会根据线程池的设置自动创建和销毁线程，从而减少了手动管理线程的复杂性。 
所以我推荐使用 **QRunnbale + QThreadPool**，因为省事~~

### 多线程优先级

>  
 线程优先级决定了线程在竞争CPU资源时的执行顺序，优先级越高的线程在竞争CPU时会被更早地执行。 


当然，这个线程优先级并不一定保证绝对的执行顺序，只是优先级越高的在竞争CPU时候，会有更高的概率更早执行；因为线程优先级的具体表现会受到系统的调度算法和资源情况的影响。

### 多线程应用场景

>  
 如果你看了这篇文章，那么大概你已经有了 多线程的应用场景了。 


<font color="greenyellow"> **大致搜罗了下，应用场景如下：**</font>
1. 后台下载文件、图像处理，数据处理等 避免阻塞主线程，提升处理的性能和用户体验。1. 网络请求网络通信等；1. 多任务并发执行；1. 反正一句话！就是避免阻塞主线程并提高效率！！！
## 实现

### <font color="skyblue">QThread</font> 多线程

#### 使用注意事项

在使用 **PySide6** 的 **QThread** 时，注意事项包括且不局限于以下几点：
- 不要使用**Python原生**的线程库来实现；- 消息或任务结果 通过**Signal信号**来传递；- 不要在**QThread**调用主线程的**GUI控件**，**应用程序**会进入卡死状态；<li>**QThread对象**必须在主线程中创建，否则程序可能会奔溃； 
  <ul>- 因为**PySide6**是基于**事件循环**的框架，**GUI线程**和**子线程**都运行在同一个事件循环中。如果在**子线程**中创建和启动**QThread对象**，它会尝试创建一个**新的事件循环**，这会导致两个**事件循环**并行运行，产生无法预估的结果。
#### 代码

>  
 代码用上一篇文章中的，看这里 — 


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

#### 代码释义

<font color="bluesky" size="5">**MyTherad类** </font>
- 继承了**QThread**；- 创建了一个 **signal_tuple**信号；- 类接收一个**func**函数以及不定长的传参（这里主要传**func** 和**count**；- 重写 **run**方法，线程的 **start()** 方法被调用时，就会自动执行**run**方法；- 执行 **count** 次数的**func**，每次睡眠1秒，使用**signal_tuple** 将执行结果和执行次数发送出去。
<font color="bluesky" size="5">**MainWindow类** </font>
- 继承了 **QWidget**，实现了包含一个**按钮**和一个**标签**的简单窗口;- 在**setup_thread** 函数中，实例化了**MyThread**，并将实例化后的**signal_tuple**信号连接到 **thread_finished**函数；- **thread_finished**为槽函数，当**signal_tuple**发出信号时，这**Slot**(槽函数）将被调用，并修改**label** 的显示。
在实例代码 以及 代码释义中可以清晰的看到，示例代码完美符合了本文中我指出来的 **QThread 多线程**的几个注意事项：
- 使用**Signal**信号传递运行结果；- 在主线程中创新子线程；- 不在子线程中修改主线程的控件。
以上便是 **QThread 多线程**在 **PySide6/PyQT** 中的简单使用。

## 后话

本次分享到此结束， see you~~🐱‍🏍🐱‍🏍
