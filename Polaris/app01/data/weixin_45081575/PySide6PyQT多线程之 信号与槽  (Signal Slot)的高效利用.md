
--- 
title:  PySide6/PyQT多线程之 信号与槽 / (Signal Slot)的高效利用 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/f7369f6cbf92407999c2c4ebb9df8df8.jpeg#pic_center#pic_center" alt="在这里插入图片描述">

## 前言

>  
 **PySide6/PyQT**信号槽是一种事件处理方式，允许程序中的对象发送和接收信号。 


在 **PySide6/PyQT** 精进的过程中，一定躲不开 **信号和槽** 这座大山，这是一个比较有意思的知识点：
- 初接触的看不懂，觉得复杂；- 看得懂的又觉得简单。
简单和难另说，将 **PySide6/PyQT** 的 **信号和槽** 讲的清楚，这个才是重点。

其实也挺简单，分三步走：
1. 定义信号**Signal**1. 定义槽**Slot**1. 将信号和槽连接：Signal().<font color="bluesky">connect</font>.Slot()
本文给你捋清楚它的具体使用，让你轻松掌握这一知识点，跨过这座大山。

## 知识点📖📖

本文用到的几个**PySide6**的知识点及链接。

|作用|链接
|------
|创建新线程|
|对象间通信的机制，允许对象发送和接收信号|
|用于响应**Signal信号**的方法|

### 基础概念

>  
 **PySide6/PyQT** 中的信号和槽是一种对象间通信机制。 


|信号（Signal）|槽（Slot）
|------
|事件的发射者|对事件的响应
|在对象中定义的方法，在特定事件发生时被触发|响应信号的函数，在信号发生时被调用

### 理解 信号和槽

用通俗易懂的话解释 **PySide6/PyQT**的信号和槽：

将**PySide6/PyQT** 的 **信号和槽** 机制简单地理解为一种 <font color="red">订阅机制</font>。
- 信号充当了 **发布者**（**publisher**）的角色，负责发布消息；- 槽扮演了 **订阅者**（**subscriber**）的角色，用于接收消息并作出响应。- 槽可以订阅一个或多个信号，当信号发生时，槽会自动被调用执行。
### 信号 Signal

>  
 在**PySide6/PyQT**中，可以使用 **Signal** 来定义信号。 


**信号** 是一种特殊函数，可以在特定的情况下被 **QObject** 对象 **发射（emit）**。
- 下面代码定义了一个名为 **my_signal** 的信号，它接受一个整形参数（可以为空，也可以更换为其它类型
```
from PySide6.QtCore import (QThread, Signal)


class MyThread(QThread):
    my_signal = Signal(int)

```

### 槽 Slot

>  
 在**PySide6/PyQT**中，可以使用 **@Slot()装饰器** 来定义 **槽**。 


**槽** 是普通的函数，它可以被信号调用。当一个信号被发射时，与之相连接的槽将被调用，并将信号的参数传递给槽。
- 下面定义了一个名为 **my_slot** 的槽，它接受一个字符串参数，并打印接收到的数据
```
from PySide6.QtCore import (QThread, Slot)


class MyThread(QThread):
    
    @Slot(int)
    def my_slot(self, data):
        print("Received data: ", data)

```

<font color="redsky">值得注意是：</font>
- 这里的 **Slot(int)** 可以不写，但是写了可以提高代码可读性和执行效率。- 首先，标明这是一个槽函数；- 其次，在运行时动态地连接信号，在一定程度上提高代码的执行效率，因为在编译期间不需要生成额外的代码来连接信号和槽。
### 连接信号和槽

在 **PySide6/PyQT** 中，可以使用 **connect()** 方法将信号和槽相连接，如下所示：
- 下面代码将**sender**对象的**my_signal信号**与**receiver**对象的**my_slot槽**相连接。- 当**sender**对象发射**my_signal信号**时，**receiver**对象的**my_slot**槽将被调用。
```
sender = MyThread()
receiver = MyThread()

sender.my_signal.connect(receiver)

```

其实就是 使用 **connect** 将两者连接起来；

### 注意事项

<font color="yellowred">重要的事情要强调三遍！</font>

信号和槽只能在 **QObject**的子类里使用！！！

信号和槽只能在 **QObject**的子类里使用！！！

信号和槽只能在 **QObject**的子类里使用！！！

然而，在**PySide6/PyQT** 中，大部分常用的类都是继承了QObject类的，所以这个问题倒无需担心，只需知道有这一概念即可。

信号和槽必须是相同的参数类型。在定义信号和槽时，必须确保它们的参数类型和个数是相同的，否则无法正确连接和触发信号和槽。

信号和槽必须是相同的参数类型。在定义信号和槽时，必须确保它们的参数类型和个数是相同的，否则无法正确连接和触发信号和槽。

信号和槽必须是相同的参数类型。在定义信号和槽时，必须确保它们的参数类型和个数是相同的，否则无法正确连接和触发信号和槽。

### 常见异常

如果在非 **QObject** 的子类中使用 **Signal** 和 **Slot**会遇到一些异常情况。这是因为在非 **QObject** 的子类中没有定义 **Signal** 和 **slot**，也没有 **QObject** 提供的信号和槽管理机制。

在非 **QObject** 的子类中使用 **Signal** 和 **Slot**，会遇到以下异常情况：
- 定义 **Signal** 时会出现 **NameError**，因为 **Signal**是在 **QObject** 中定义的；- 在 **connect()** 时会出现 **AttributeError**，因为 **connect()** 是 **QObject** 的成员函数；- 在 信号**emit()** 时会出现 **AttributeError**，即属性错误，因为该类中没有该函数。
## 信号和槽 的基本使用

>  
 说完了 基础概念，现在上代码来检验学习成果了。 


### 代码

```
# -*- coding: utf-8 -*-

import time


from PySide6.QtCore import (QThread, Signal, Slot, QSize)
from PySide6.QtWidgets import (QApplication, QPushButton, QLabel, QVBoxLayout, QWidget)


class MyThread(QThread):
    my_signal = Signal(int)
    finished_signal = Signal()

    def __init__(self, count):
        super().__init__()
        self.count: int = count

    def run(self):
        for idx in range(1, self.count + 1):
            time.sleep(1)
            # 任务进行时发出信号
            self.my_signal.emit(idx)
	    # 任务完成后发出信号
        self.finished_signal.emit()


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
        self.thread_ = MyThread(count=5)
        self.thread_.my_signal.connect(self.thread_progress)
        self.thread_.finished_signal.connect(self.thread_finished)
        self.thread_.start()

    @Slot(int)
    def thread_progress(self, item):
        self.label.setText('This is a label =&gt; ' + str(item))

    @Slot()
    def thread_finished(self):
        self.label.setText('This is a label finished.')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


```

<font color="yellowbulegreen"> **MyThread**类</font>
- 继承了 **QObject**，创建了一个名为 **MyThread**的**QThread** 类；- 包含一个名为**my_signal** 和 **finished_signal** 的信号，它们分别在 **任何进行时** 和 **任务完成后** 发射；- 注意 **my_signal** 是带参数的，而 **finished_signal** 不带参数，这个需要与 槽函数对应！！！- 循环执行 **count** 次数的操作，每次 通过 **my_signal** 发射，从而修改 应用程序中的 **lable**；- 当循环完成后，通过 **finished_signal** 发射信号，修改 应用程序中的 **label**。
<font color="yellowbulegreen"> **MainWindow**类</font>
- 继承了 **QWidget**，实现了包含一个**按钮**和一个**标签**的简单窗口;- 在**setup_thread** 函数中，实例化了**MyThread**，并将实例化后的 **my_signal 和 finished_signal** 信号连接到 **thread_progress 和 thread_finished** 函数；- **thread_progress 和 thread_finished**为槽函数，当**my_signal 和 finished_signal**发出信号时，对应**Slot**(槽函数）将被调用，并修改**label** 的显示。
### 运行效果

<img src="https://img-blog.csdnimg.cn/e234c41749564551bc08f72817e48195.gif#pic_center" alt="在这里插入图片描述">

## 后话

本次分享到此结束， see you~🐱‍🏍🐱‍🏍
