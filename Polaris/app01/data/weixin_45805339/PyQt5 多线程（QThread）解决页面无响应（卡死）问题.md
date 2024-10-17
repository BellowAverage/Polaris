
--- 
title:  PyQt5 多线程（QThread）解决页面无响应（卡死）问题 
tags: []
categories: [] 

---
很多时候我们可能需要用多任务去处理相应业务，如果我们都在页面主线程处理，页面会出现无响应状态。切换模块或页面出现崩溃现象。这样我们需要用多线程的方式来处理：

### 1.创建多进程类

```
from PyQt5.QtCore import QThread, pyqtSignal


class MyThread(QThread):
    my_str = pyqtSignal(str) # 创建任务信号

    def run(self):
    	"""
    	多线程功能函数
        :return:
        """
        print("此处省略1万行代码") # 你的需要单独开启线程的逻辑代码
        self.my_str.emit("ok") # 发出任务完成信号
        

```

### 2.创建曹函数

在页面主窗口类下添加槽函数

```
    def get_sin_out(self, out_str):
        """
        :param out_str:
        :return:
        """
        if out_str == "ok":
        	print("处理完成")

```

### 3.信号与槽函数的连接

```
# 放在__init__(self):下，主窗口类实例，初始化时加载
self.my_thread = MyThread()
self.my_thread.my_str.connect(self.get_sin_out)

```

### 4.启动多线程

```
    def start_thread(self):
        """
        启动多线程
        :return:
        """
        try:
        	print("此处省略1万代码")
            self.my_thread.start()
        except Exception as e:
        	print(e)
            

```

### 5.按钮出发事件

```
# 放在__init__(self):下，主窗口类实例，初始化时加载
self.myBn.clicked.connect(lambda: self.start_thread())

```
