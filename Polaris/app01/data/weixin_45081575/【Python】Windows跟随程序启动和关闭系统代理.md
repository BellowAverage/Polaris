
--- 
title:  【Python】Windows跟随程序启动和关闭系统代理 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/6c9fab8202af48ccadd30ea43c60b41a.png#pic_center" alt="在这里插入图片描述">

## 前言

在日常使用计算机时，偶尔可能需要配置代理来访问特定的网络资源或进行网络调试。 当在使用**mitmproxy** 时候，
- 程序开始前，需要手动打开系统代理；- 程序结束后，需要手动关闭系统代理。
这些重复性且没有技术含量工作其实是很冗余且不友好的。 而在 **Windows** 操作系统中，使用**Python**编程是很容易去实现在程序启动和关闭时自动配置系统代理。 所以在以前也分享过一篇文章，。 在现在，发现了一个更佳的实现方式，这里做下记录，分享给各位小伙伴！

## 知识点

|模块|作用
|------
|**winproxy**|通过Python模块函数和命令行编程来实现修改系统代理
|**atexit**|程序在退出时的处理器

**atexit**官方文档：

**winproxy** 在前面的文章中有做介绍，这里不着重介绍它； 这里主要介绍的是 **Python** 内置的**atexit** 模块。

## atexit 应用场景

>  
 ps：应用场景是网上搬过来的，具体的应用应该根据日常开发中的需要来决定。 


在 Python 编程中，我们通常需要确保程序在退出时能够执行一些必要的清理操作，以释放资源或完成其他任务。这就是 `atexit` 模块发挥作用的地方。以下是 `atexit` 模块的一些常见应用场景：
-  **资源释放**：在程序中打开文件、网络连接或数据库连接等资源时，使用 `atexit` 来注册清理函数，以确保在程序退出时关闭这些资源，防止资源泄漏。 -  **日志记录**：如果程序需要进行详细的日志记录，可以使用 `atexit` 来注册一个清理函数，以在程序退出时保存或上传日志文件。 -  **临时文件清理**：如果程序生成了临时文件，可以使用 `atexit` 来注册一个清理函数，以在程序退出时删除这些临时文件，以释放磁盘空间。 -  **状态保存**：有时需要在程序退出时保存一些状态信息，以便下次程序运行时可以恢复。`atexit` 可以用于执行状态保存的操作。 -  **子进程或线程管理**：如果程序创建了子进程或线程，可以使用 `atexit` 来注册清理函数，以确保在程序退出时正确终止这些子进程或线程。 -  **网络连接管理**：对于涉及网络通信的程序，使用 `atexit` 来注册清理函数，以在程序退出时关闭网络连接，释放网络资源。 
## 使用

### 基础使用

在Python中，可以使用`atexit`模块来注册在程序退出后执行的操作。通过使用`atexit`模块，可以确保在程序退出时执行特定的操作，以释放资源或完成其他必要的清理工作。

**代码释义：** 代码定义了一个名为`cleanup`的清理函数，然后使用`atexit.register()`方法来注册它。当程序退出时，无论是正常退出还是由于异常退出，都会执行`cleanup`函数中定义的清理任务。

```
import atexit

def cleanup():
    print("Performing cleanup tasks...")

# 注册清理函数
atexit.register(cleanup)

# 主程序
print("Main program")


```

程序运行结果如下图所示： <img src="https://img-blog.csdnimg.cn/d54bbb0f7add46f28e79d977e5691bcf.png" alt="在这里插入图片描述">

### Python 编程与系统代理配置

>  
 在了解**atexit**的基础使用后，现在来结合**winproxy**使用。 


在这个示例中，使用 `winproxy` 库来操作 **Windows** 系统的代理设置。首先定义了 `set_proxy` 函数，用于设置系统代理。然后，使用 `atexit` 模块来注册 `close_proxy` 函数，以确保在程序退出时关闭代理。

部分代码参考我之前分享的一篇文章：

```
import atexit
from winproxy import ProxySetting


ps = ProxySetting()


def set_proxy():
    """设置系统代理"""
    ps.enable = True
    ps.server = '127.0.0.1:9527'
    ps.registry_write()
    print('代理已经打开!')


def close_proxy():
    """关闭系统代理"""
    ps.enable = False
    ps.registry_write()
    print('代理已经关闭!')


if __name__ == '__main__':
    # 打开代理
    set_proxy()
    # 注册清理函数
    atexit.register(close_proxy)


```

## 总结

通过结合 **Python** 编程和 `atexit` 模块，可以实现在程序启动和关闭时自动配置系统代理的功能。 这种方法确保了系统代理的正确使用，同时也展示了 `atexit` 模块在 **Python** 编程中的实际应用场景。 不得不说，`atexit`是个好东西！！！

## 后话✨✨

本次分享到此结束， see you~~🐱‍🏍🐱‍🏍
