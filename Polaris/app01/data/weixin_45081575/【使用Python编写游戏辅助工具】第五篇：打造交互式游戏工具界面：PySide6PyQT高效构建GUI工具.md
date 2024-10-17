
--- 
title:  【使用Python编写游戏辅助工具】第五篇：打造交互式游戏工具界面：PySide6/PyQT高效构建GUI工具 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/49c55ff8abd8b710957ffad708bc5c5b.png" alt="image.png">

## 前言

>  
 这里是【使用Python编写游戏辅助工具】的第五篇：打造交互式游戏工具界面：PySide6/PyQT高效构建GUI工具。本文主要介绍使用`PySide6`来实现构建GUI工具。 


在前面，我们实现了两个实用的游戏辅助功能：
1. 由键盘监听事件触发的鼠标连击功能；1. 对Windows窗口的多种操作（如隐藏、显示、设置前台等
在这一篇文章中，笔者将带领读者朋友们使用 `PySide6/PyQT` 将前面实现的功能封装成一个GUI工具，这样一个简单的游戏辅助工具初具雏形了。

即使你完全没有 `PySide6/PyQT` 这方面的开发经验也没关系，学习就完事了；

即便不想学习，笔者也会提供源码，拿来用就完事了。

本文章为本系列文章最后一篇，【使用Python编写游戏辅助工具】系列文章到此结束。

## 文章脉络概述

该工具大致的组织架构如下图所示：
- 包含 `鼠标连击`、`Windows窗口操作`等功能！
在本系列文章中，我们将逐步构建一个游戏辅助工具，它将提供以下主要功能（所有功能都是借助`Python`的相关库和模块来帮助我们实现的；）：
1.  鼠标连击器：实现自动触发连续鼠标点击动作，帮助我们实现连击操作； 1.  Windows窗口操作：利用`Python`的相关库和模块，我们将探索如何操作和控制Windows窗口，包括隐藏窗口、显示窗口、置顶窗口等操作； 
## 系列文章脉络

>  
 系列文章内容大体如下，后续可能会更新新的文章。 

-  <font color="bluegreen">**点击直达：**</font> -  <font color="bluegreen">**点击直达：**</font> -  <font color="bluegreen">**点击直达：**</font> -  <font color="bluegreen">**点击直达：**</font> -  <font color="bluegreen">**点击直达：**</font> 
## 知识点📖📖

|库和模块|描述
|------
||提供了Python与Qt框架的绑定，用于创建图形用户界面（GUI）

**安装依赖**

```
pip install pyside6

```

这个模块就可以很好的实现本文的主题。

## 实现

>  
 因文章篇幅有限，抓重点来讲。 


本文的代码实在是太多了，也不知从哪说起。干脆把代码都贴上来，

### 操作示例

视频介绍：
- 下面的动图主要展示了该工具可以最小化到系统托盘，并从系统托盘恢复的操作。
<img src="https://img-blog.csdnimg.cn/img_convert/576c42d4d3cabc20007cd40f097b591a.gif" alt="展示最小化到系统托盘.gif">

### 项目组织

使用`PySide6/PyQT` 构建的GUI工具组织架构如下所示：
- 采用了MVC模型，通过MVC模式的应用，可以实现数据、用户界面和业务逻辑的解耦，提高代码的可读性、可维护性和可测试性；- 模型、视图和控制器各自担负不同的责任，使代码更具结构化，并允许团队成员分工合作，独立开发和测试各个组件。
```
GameAssistant/
├── controllers/
│   ├── __init__.py
│   └── controller_main.py
├── make/
│   └── 辅助小工具.spec
├── models/
│   ├── invoke_func/
│   │   ├── __init__.py
│   │   ├── mouse_click.py
│   │   └── window_operate.py
│   ├── __init__.py
│   └── model_main.py
├── views/
│   ├── resources/
│   │   ├── main.ui
│   │   ├── trash.png
│   │   └── utils.qrc
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_ui.py
│   │   └── utils_rc.py
│   ├── widgets/
│   │   ├── __init__.py
│   │   └── view_main.py
│   └── __init__.py
├── main.py
├── README.md
└── requirements.txt

```

### 绘制GUI界面

在`designer.exe` 软件中，绘制出下图所示的工具界面（路径在**views/resources/main.ui**
<li>使用了`QTabWidget` 控件，绘制了两个页面。 
  - 在`鼠标连击` 页面，有一个输入框；- 在`后台挂机` 页面，有一个输入框和两个按钮 </li>
这个比较简单，动手拖拽需要的控件，拼凑起来就可以了（有手就行。

如下动图所示：

<img src="https://img-blog.csdnimg.cn/img_convert/7a4d877762c5471424bb44d3da877887.gif" alt="工具展示.gif">

### model（模型）

这里使用了 **QRunnable + QThreadPool** 实现的线程池，并将所有任务都给到 线程池中运行。
- **鼠标点击** 和 **Windows操作** 的代码放置在（**models/invoke_func/** 下
```
# -*- coding: utf-8 -*-
# Name:         model_main.py
# Author:       小菜
# Date:         2023/6/14 20:00
# Description:


from collections import defaultdict
from PySide6.QtCore import (QObject, QRunnable, QThreadPool, Signal)

from models.invoke_func.mouse_click import click_mouse
from models.invoke_func.window_operate import (show_window, hide_window)

flag = True


class WorkerRunnable(QRunnable):

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.status_signal = kwargs.get('status_signal')

    def run(self):
        if not self.args:
            self.func()
        while flag:
            self.func(*self.args)

    def win_run(self):
        res = self.func(*self.args)
        self.status_signal.emit({<!-- -->'status': res})


class ModelMain(QObject):
    win_status_signal: Signal = Signal(dict)

    def __init__(self):
        super().__init__()
        self.thread_pool = QThreadPool()
        self.thread_status_map = defaultdict(bool)

    def stop_keyboard_listener(self):
        global flag
        if flag:
            flag = False
            thread_name: str = 'click'
            self.thread_status_map[thread_name] = False

    def click_operate(self, frequency: int = 10):
        global flag
        thread_name: str = 'click'
        if self.thread_status_map[thread_name]:
            return
        flag = True
        self.thread_status_map[thread_name] = True
        if frequency &lt; 10:
            frequency = 10
        print(flag, thread_name, self.thread_status_map[thread_name], frequency)
        click_frequency_map = {<!-- -->
            10: [0.09],
            20: [0.035],
            30: [0.027],
            40: [0.014],
            50: [0.013],
            60: [0.005],
            70: [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0],
            80: [0.01, 0.01, 0.01, 0],
            90: [0.01, 0.01, 0],
            100: [0.01, 0.0001, 0.0001, 0, 0],
            150: [0.001, 0.001, 0, 0, 0]
        }
        task = WorkerRunnable(
            click_mouse,
            click_frequency_map.get(frequency, 150)
        )
        self.thread_pool.start(task)

    def show_win_operate(self, title: str = None):
        task = WorkerRunnable(show_window,
                              title,
                              status_signal=self.win_status_signal)
        self.thread_pool.start(task.win_run)

    def hide_win_operate(self, title: str = None):
        task = WorkerRunnable(hide_window,
                              title,
                              status_signal=self.win_status_signal)
        self.thread_pool.start(task.win_run)


```

### view（视图）

视图代码实现了
- 添加工具到系统托盘，从系统托盘退出或恢复工具；- 按下键盘的 `Esc`就最小化到系统托盘；
```
# -*- coding: utf-8 -*-
# Name:         view_main.py
# Author:       小菜
# Date:         2023/6/14 20:00
# Description:
import os

from PySide6.QtGui import (QAction, QIcon, QShortcut, QKeySequence)
from PySide6.QtWidgets import (QMainWindow, QSystemTrayIcon, QMenu)

from views import Ui_MainWindow


class ViewMain(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -&gt; None:
        super().__init__(parent=parent)
        self.setupUi(self)

        # 创建系统托盘图标相关的变量和对象
        self._restore_action = QAction()
        self._quit_action = QAction()
        self._tray_icon_menu = QMenu()

        # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(u":/trash.png"))
        self.tray_icon.setToolTip("辅助小工具")

        # 创建系统托盘图标的菜单和动作
        self.create_actions()
        self.create_tray_icon()
        self.tray_icon.show()

        # 连接系统托盘图标的激活信号到槽函数
        self.tray_icon.activated.connect(self.tray_icon_activated)

        # 键盘监听
        self.listen_keyboard()

    def tray_icon_activated(self, reason):
        # 当系统托盘图标被激活时的操作
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.restore_from_tray()

    def restore_from_tray(self):
        # 还原窗口
        if self.isMinimized():
            self.showNormal()
        elif self.isMaximized():
            self.showMaximized()
        else:
            self.show()

    def create_actions(self):
        # 创建系统托盘图标菜单的动作
        self._restore_action = QAction("显示", self)
        self._restore_action.triggered.connect(self.restore_from_tray)  # "显示"菜单项触发还原窗口的操作

        self._quit_action = QAction("退出", self)
        self._quit_action.triggered.connect(lambda: os._exit(0))  # "退出"菜单项触发退出应用程序的操作

    def create_tray_icon(self):
        # 创建系统托盘图标的菜单
        self._tray_icon_menu = QMenu(self)
        self._tray_icon_menu.addAction(self._restore_action)
        self._tray_icon_menu.addSeparator()
        self._tray_icon_menu.addAction(self._quit_action)

        self.tray_icon.setContextMenu(self._tray_icon_menu)
        self.tray_icon.show()

    def show_notification(self, title: str = '连击信息⚠', text: str = None, icon=QSystemTrayIcon.MessageIcon.Information):
        # 显示系统通知
        self.tray_icon.showMessage(
            title,
            f"警告！！！{<!-- -->text}",
            icon,
            2000
        )

    def listen_keyboard(self):
        # 键盘监听
        shortcut = QShortcut(QKeySequence("Esc"), self)
        # 当按下 Esc 键时隐藏窗口
        shortcut.activated.connect(self.hide)


```

### controller（**控制器**）

这里做的操作是将 model与view连接起来，充当了一个中间人的活儿。

```
# -*- coding: utf-8 -*-
# Name:         controller_main.py
# Author:       小菜
# Date:         2023/6/14 20:00
# Description:

import keyboard
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QSystemTrayIcon

from views import ViewMain
from models import (ModelMain, WorkerRunnable)

round_to_nearest_10 = lambda number: min(round(number / 10) * 10, 150)


class ControllerMain:

    def __init__(self):
        self.view = ViewMain()
        self.model = ModelMain()
        # 显示窗口
        self.view.show()
        # 初始化 键盘监听
        self.init_operate()

        # 绑定按钮
        self.view.btn_show_win.clicked.connect(self.show_win_operate)
        self.view.btn_hide_win.clicked.connect(self.hide_win_operate)

        # 绑定信号到槽函数
        self.model.win_status_signal.connect(self.window_listen)

    def init_operate(self):
        task = WorkerRunnable(self.listen_keyboard)
        self.model.thread_pool.start(task)

    def listen_keyboard(self):
        keyboard.add_hotkey('Ctrl+Shift+A', self.click_operate)
        keyboard.add_hotkey('Ctrl+Shift+Q', self.model.stop_keyboard_listener)
        keyboard.wait()

    def click_operate(self):
        frequency = 10
        # 创建匿名函数
        try:
            frequency = round_to_nearest_10(int(self.view.line_edit_click.text()))
            print(frequency)
        except (ValueError, TypeError):
            ...
        finally:
            self.model.click_operate(frequency=frequency)
            self.view.show_notification(text='开始点击')

    def show_win_operate(self):
        win_title = self.view.line_edit_title.text()
        if not win_title:
            return
        self.model.show_win_operate(title=win_title)

    def hide_win_operate(self):
        win_title = self.view.line_edit_title.text()
        if not win_title:
            return
        self.model.hide_win_operate(title=win_title)

    @Slot(dict)
    def window_listen(self, item):
        if not item.get('status'):
            self.view.show_notification(
                title='警告警告⚠',
                text='找不到窗口！！！',
                icon=QSystemTrayIcon.MessageIcon.Warning
            )


```

### main函数

函数启动入口

```
# -*- coding: utf-8 -*-
# Name:         main.py
# Author:       小菜
# Date:         2023/6/14 20:00
# Description:


import sys
from ctypes import windll

from PySide6.QtWidgets import QApplication

from controllers import ControllerMain

if __name__ == '__main__':
    # 同步图标
    windll.shell32.SetCurrentProcessExplicitAppUserModelID('nothing')
    app = QApplication()
    # 关闭窗口时候不退出程序
    app.setQuitOnLastWindowClosed(False)
    controller = ControllerMain()
    # 事件循环
    sys.exit(app.exec())


```

## 总结🎈🎈

本文介绍了 `PySide6/PyQT` 打包游戏辅助工具的操作。

将前面介绍的 `鼠标连点`、`Windows窗口操作`等功能打包成一个GUI工具，从更加方便后续的使用。

总而言之，本文通过详细介绍使用 `PySide6/PyQT` 打包GUI的操作，帮助读者理解和应用Python在游戏辅助工具开发中的打包功能。
