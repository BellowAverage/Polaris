
--- 
title:  【Python】实现一个鼠标连击器，每秒点击1000次 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/b3841dd12dce1ff19175097e8678eb59.png" alt="image.png">

## 前言

鼠标连击是指在很短的时间内多次点击鼠标按钮，通常是鼠标左键。当触发鼠标连击时，鼠标按钮会迅速按下和释放多次，产生连续的点击效果。

在这里鼠标连击的主要用途是：
- 帮助我们进行鼠标点击，疯狂连击；- 例如在射击游戏中连续开火，如果点击就可以攻击怪物，那就可以持续不断的高频次地攻击怪物；- 通过鼠标连击，可以快速执行多个动作，提高操作效率。
<font color="bluesky"> **问：本文使用Python可以实现多快的 `鼠标连击`呢？** </font>

<font color="bluepi"> 答：如果不在每次鼠标点击之间添加睡眠时间，那么你的电脑会宕机，完全无法响应过来~ </font>

## 注意事项✨✨

本文主要实现的是Windows系统上的 `鼠标连击` ，如果需要在其它平台如Linux、Mac系统实现`鼠标连击`，则可以使用跨平台的一些自动化模块，例如 **pyautogui**，或者是使用系统特有的模块，这里不做赘述。

本文使用的是`ctypes`库，它可以实现的`鼠标连击`速度非常快（特别是在与其它模块对比时候），原因如下：
1.  直接调用操作系统函数：`ctypes`允许你直接调用操作系统的动态链接库（DLL）中的函数。在模拟鼠标点击时，`ctypes`可以直接调用操作系统提供的原生函数，从而绕过了`pyautogui`或其它库中的一些封装层和额外的处理逻辑，使得操作更加直接和高效。 1.  无需依赖额外库和模块：`ctypes`是Python的标准库，无需安装额外的依赖库。相比之下，`pyautogui`库可能会依赖其他模块或库，这可能导致额外的加载时间和性能开销。 1.  调用系统级别的API：`ctypes`通过调用操作系统级别的API来模拟鼠标点击。这些API通常是与操作系统更底层的交互接口，因此在执行速度上可能更为高效。 
需要注意的是，使用`ctypes`库直接调用操作系统函数需要了解函数的参数和调用约定，并且代码可能会因为依赖于Windows操作系统而不具有可移植性。

总而言之，`ctypes`库在模拟鼠标点击时可能更快速是因为它直接调用了操作系统提供的原生函数，并且无需额外的依赖库和模块。

## 知识点📖📖

|库和模块|描述
|------
||用于在Python中调用动态链接库（DLL）和共享库的外部函数（这里用于鼠标点击）

据官网介绍， 是 Python 的外部函数库。它提供了与 C 兼容的数据类型，并允许调用 DLL 或共享库中的函数。可使用该模块以纯 Python 形式对这些库进行封装。

关于调用 `ctypes` 函数的步骤（具体的操作可以查阅`官方文档`）：
1. 首先，导入 `ctypes` 模块。1. 定义函数的参数类型和返回值类型，可以通过 `argtypes` 和 `restype` 属性进行设置。1. 使用 `ctypes.windll` 访问 Windows 动态链接库，并获取所需的函数。1. 调用函数并传递相应的参数。
这个模块就可以很好的实现本文的主题。

## 鼠标连击 实现

>  
 在`Python`编程中，使用`ctypes`库中的`SendInput`函数。通过多次调用`SendInput`函数发送鼠标按下和释放的事件，可以模拟鼠标连击的效果。 


需要注意的是，鼠标连击的频率和点击次数可能会受到操作系统或应用程序的限制。某些应用程序可能会有自己的点击速率限制，或者操作系统会对鼠标点击频率进行限制，以避免滥用或误操作。

### 代码

```
# encoding:utf-8

import time
import ctypes

# 定义鼠标事件常量
MOUSE_EVENT_LEFT_DOWN = 0x0002
MOUSE_EVENT_LEFT_UP = 0x0004


# 定义鼠标输入结构体
class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]


# 定义输入结构体
class Input(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("mi", MouseInput)]

    _anonymous_ = ("_input",)
    _fields_ = [("type", ctypes.c_ulong),
                ("_input", _INPUT)]


# 定义SendInput函数的参数类型
SendInput = ctypes.windll.user32.SendInput
SendInput.argtypes = (ctypes.c_uint, ctypes.POINTER(Input), ctypes.c_int)
SendInput.restype = ctypes.c_uint


# 定义鼠标点击函数
def click_mouse(count: int = 10):
    """模拟鼠标点击事件"""
    
    for i in range(count):
        # 创建一个鼠标左键按下事件
        mouse_down = Input()
        mouse_down.type = 0
        mouse_down.mi.dwFlags = MOUSE_EVENT_LEFT_DOWN

        # 创建一个鼠标左键释放事件
        mouse_up = Input()
        mouse_up.type = 0
        mouse_up.mi.dwFlags = MOUSE_EVENT_LEFT_UP

        # 将事件打包为输入结构体数组
        events = (Input * 2)()
        events[0] = mouse_down
        events[1] = mouse_up

        # 发送输入事件
        SendInput(2, events, ctypes.sizeof(Input))
        # 暂停一下
        time.sleep(0.01)


if __name__ == '__main__':
    click_mouse(count=100)


```

### 代码释义
- `MOUSE_EVENT_LEFT_DOWN` 和 `MOUSE_EVENT_LEFT_UP` 是表示鼠标左键按下和释放的常量；- `MouseInput` 是一个结构体，用于描述鼠标事件的信息，包括鼠标的坐标、鼠标数据、标志位、时间和附加信息等；- `Input` 是一个结构体，用于描述输入事件的信息，包括事件类型和事件的具体信息。这里使用了联合 `_INPUT` 来包含鼠标输入的信息；- `SendInput` 是 Windows 用户32库中的函数，用于发送输入事件。在这里，我们通过 `ctypes` 库进行函数的调用设置，指定了参数类型和返回值类型；- `click_mouse` 函数用于模拟鼠标点击事件。它接受一个可选的随机暂停时间列表作为参数，用于控制点击之间的间隔。首先创建鼠标按下和释放的事件，并将它们打包为输入结构体数组。然后使用 `SendInput` 函数发送输入事件，并通过 `time.sleep` 函数暂停一段时间。
在这个代码中，我们通过设置 `SendInput` 函数的参数类型和返回值类型，并使用 `ctypes.windll.user32.SendInput` 访问了 Windows 用户32库中的 `SendInput` 函数。然后在 `click_mouse` 函数中直接调用了 `SendInput` 函数来发送输入事件。

### 运行效果

在运行代码后，可以看到鼠标快速点击了100下。这就实现了鼠标连击器。

<img src="https://img-blog.csdnimg.cn/img_convert/422356f1a87b795f11ad2f3f746eeb22.gif" alt="鼠标点击demo.gif">

## 总结✨✨

本文介绍了 `ctypes`模块 的基本使用，并且使用 `ctypes` 实现 鼠标连击 的操作，
- 首先，介绍了`ctypes`模块的基本使用方法，它可以用来调用动态链接库中的函数；- 然后，使用`ctypes`模块调用Windows API中的鼠标事件函数，实现了模拟鼠标按下和释放的功能；
通过本文的学习，读者可以了解到如何使用`ctypes`模块实现鼠标连击，结合键盘监听就可以进行更高级的操作。这对于需要进行大量鼠标点击的自动化任务或游戏操作来说非常有用。读者可以根据自己的需求进一步扩展和优化代码，以满足实际应用场景的要求。
