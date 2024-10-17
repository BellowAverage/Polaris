
--- 
title:  Python模块psutil：系统进程管理与Selenium效率提升的完美结合 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/66e3517fa2b74bbd99b152d8f5445cbc.png" alt="在这里插入图片描述">

## 前言

在前面编写一个`Selenium`的自动化程序时候，发现一个问题。

因笔记本配置较为差，所以每次初始化`Selenium`的`WebDriver`都会非常慢，整个等待过程是不友好的。

所以我就想到：
<li> 
  <blockquote> 
   在程序中初始化一个全局的`WebDriver`对象，在程序结束之后不退出`Selenium`打开的浏览器。 
   这样就只需要启动一次`Selenium`打开的浏览器，后面都使用这个浏览器。 
  </blockquote> </li>
这样的确是个好主意，但随之而来的问题是：
<li> 
  <blockquote> 
   ？万一`Selenium`打开的浏览器被系统回收或者出现异常了，那么程序运行就会出错！ 
  </blockquote> </li>
所以在最终，整个问题解决的思路如下：
1. 程序运行前先检测指定的 `Selenium浏览器`（系统进程）是否存在；1. 如果存在则往后运行程序；1. 如果不存在则先打开`Selenium`浏览器，再往后运行程序。
文章的标题虽然为 **Python psutil：系统进程管理与Selenium效率提升的完美结合**，但是应用场景却是很广的，譬如系统监控、系统监控、性能分析、限制系统资源、管理进程。

本文主要借助于 `Python` 的 `psutil`模块来实现，所以下面更多的是介绍 `psutil`模块的使用。

当然，重要的并不是使用什么工具，而是怎么使用工具，以及工具能帮助我们解决哪些问题。

## 知识点

|模块|解释
|------
||用于在 Python 中检索有关运行进程和系统利用率（CPU、内存、磁盘、网络、传感器）的信息。

具体的介绍看下图：

>  
 psutil（python system and process utilities）是一个跨平台库，用于访问操作系统的进程和系统利用率（CPU、内存、磁盘、网络等）。它主要用于系统监控，分析和限制系统资源，以及管理运行的进程。它实现了Unix命令行工具提供的许多功能，如ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等。 


<img src="https://img-blog.csdnimg.cn/5d8ab7851afd4e72bb4e6969b8eddd30.png" alt="在这里插入图片描述">

## 应用场景

在使用selenium进行自动化测试时，每次开启和销毁浏览器窗口都会消耗系统资源。使用psutil来监控selenium的浏览器窗口。如果检测到窗口已经存在，就可以复用这个窗口，而不是每次都创建新的窗口。这样可以节省消耗系统资源。

**psutil**还可以用于多种场景，包括系统监控、性能分析、限制系统资源、管理进程等。

## psutil的基础使用

这部分操作，在官方文档中都可以找到。

### 获取CPU 信息

```
import psutil

# 获取CPU的数量
cpu_count = psutil.cpu_count()
print(f'Number of CPUs: {<!-- -->cpu_count}')

# 获取CPU的使用率
cpu_percent = psutil.cpu_percent()
print(f'CPU usage: {<!-- -->cpu_percent}%')

# 获取CPU的详细信息
cpu_times = psutil.cpu_times()
print(f'CPU times: {<!-- -->cpu_times}')

```

### 获取 内存 信息

```
# 获取系统的内存使用情况
mem_info = psutil.virtual_memory()
print(f'Memory info: {<!-- -->mem_info}')

# 获取系统的交换内存（swap）使用情况
swap_info = psutil.swap_memory()
print(f'Swap info: {<!-- -->swap_info}')

```

### 获取 磁盘 信息

```
# 获取磁盘分区信息
disk_partitions = psutil.disk_partitions()
print(f'Disk partitions: {<!-- -->disk_partitions}')

# 获取根目录的磁盘使用情况
disk_usage = psutil.disk_usage('/')
print(f'Disk usage: {<!-- -->disk_usage}')

# 获取磁盘IO信息
disk_io = psutil.disk_io_counters()
print(f'Disk IO: {<!-- -->disk_io}')

```

### 获取 网络 信息

```
# 获取网络IO信息
net_io = psutil.net_io_counters()
print(f'Network IO: {<!-- -->net_io}')

# 获取当前的网络连接信息
net_connections = psutil.net_connections()
print(f'Network connections: {<!-- -->net_connections}')

# 获取网络接口信息
net_if_addrs = psutil.net_if_addrs()
print(f'Network interface addresses: {<!-- -->net_if_addrs}')

# 获取网络接口状态
net_if_stats = psutil.net_if_stats()
print(f'Network interface stats: {<!-- -->net_if_stats}')

```

### 获取 进程 信息

```
# 获取当前运行的所有进程ID
pids = psutil.pids()
print(f'Process IDs: {<!-- -->pids}')

# 获取所有进程实例
for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.info)

# 获取指定PID的进程实例
pid = 1
if psutil.pid_exists(pid):
    proc = psutil.Process(pid)
    print(f'Process info: {<!-- -->proc.info()}')

```

## 监控系统进程代码

### 指定chrome版

这里用到我之前的一篇`Selenium`文章，

文章中提到，在命令行使用以下命令去驱动`Selenium浏览器`

```
chrome.exe --remote-debugging-port=9527 --user-data-dir=“F:\selenium”

```

因为使用了命令行去执行，所以在代码中需要检索：是否包含指定命令函参数

在我的`Selenium`项目中，检测该`Selenium`浏览器受否存在的代码如下所示：
- 看不懂就看注释啪🥧~
<img src="https://img-blog.csdnimg.cn/b07c6618b9c6484183dac95b13de08a3.png" alt="在这里插入图片描述">

**代码释义：**

这份代码的主要用途是检查是否有包含特定命令行参数的Chrome浏览器进程正在运行。它遍历所有正在运行的进程，如果进程的名称包含"chrome"，并且命令行参数中包含`--remote-debugging-port=port`，那么就返回True，否则返回False。这对于自动化测试非常有用，可以避免重复创建和销毁浏览器窗口，从而节省系统资源。

### 通用版

下面函数可以用于监控特定的进程是否在运行。例如，你可能有一个重要的服务或应用，你希望确保它始终在运行。你可以定期运行这个函数来检查这个服务或应用是否在运行，如果不在运行，可以采取相应的操作，如重新启动服务或应用。

```
import os
import subprocess

import psutil


def check_if_specific_process_running(process_name, cmdline=None) -&gt; bool:
    """
    检查是否有包含指定名称的进程正在运行。
    
    Args:
        process_name(str): 要检查的进程名
        cmdline(str): 要检查的命令行参数。默认为None。

    Returns:
        bool: 如果找到匹配的进程则返回True，否则返回False。
    """
    # 遍历所有正在运行的进程
    for proc in psutil.process_iter():
        try:
            # 检查进程名是否包含给定的名称字符串
            if process_name.lower() in proc.name().lower():
                # 获取进程详细信息列表
                p_info = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
                # 如果提供了cmdline，检查它是否在进程的cmdline中
                if cmdline:
                    if any(cmdline in cmd for cmd in p_info['cmdline']):
                        return True
                # 如果没有提供cmdline，返回True，因为进程名匹配
                else:
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def exec_cmd_command():
    """
    切换到指定路径，若有。然后打开浏览器

    Returns:
        True
    """
    os.chdir(path=config.CHROME_PATH)
    subprocess.Popen(
        r'chrome.exe --remote-debugging-port=9527 --user-data-dir="F:\selenium"',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return True


if __name__ == '__main__':
    if not check_if_specific_chrome_running():
        # 打开浏览器
        exec_cmd_command()

```

## 总结

psutil是一个强大的库，可以用于获取系统和进程的信息，以及管理进程。它在系统监控、性能分析、资源管理等方面都有广泛的应用。本文中代码是一个很好的例子，展示了如何使用psutil来检查特定的浏览器进程是否正在运行，从而避免重复创建和销毁窗口，节省系统资源。

## 后话

本次分享到此结束，

see you🎉🎉
