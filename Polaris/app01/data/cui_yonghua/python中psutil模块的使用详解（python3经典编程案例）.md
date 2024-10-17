
--- 
title:  python中psutil模块的使用详解（python3经典编程案例） 
tags: []
categories: [] 

---
#### 一. psutil模块的介绍

**`psutil（process and system utilities）`** 是一个跨平台的库，用于在Python中检索有关运行进程和系统利用率（CPU、内存、磁盘、网络、传感器）的信息。

它主要用于系统监控、分析和限制流程资源以及管理正在运行的流程。

它实现了经典UNIX命令行工具提供的许多功能，如ps、top、iotop、lsof、netstat、ifconfig、free等。

psutil模块可以跨平台使用，支持Linux／UNIX／OSX／Windows等，它主要用来做系统监控，性能分析，进程管理等。

在python中，可以使用psutil这个第三方模块去获取信息的信息。

github地址：

官方文档：

安装：`pip3 install psutil`

#### 二. psutil模块的使用

##### 2.1 获取cpu信息

```
import psutil

# 1. 获取CPU的完整信息
print(psutil.cpu_times())

# 2. 获取CPU的逻辑个数
print(psutil.cpu_count())

# 3. 获取CPU的物理个数
print(psutil.cpu_count(logical=False))


# 4. psutil获取系统CPU使用率的方法是cpu_percent(),其有两个参数，分别是interval和percpu
# interval指定的是计算cpu使用率的时间间隔，percpu则指定是选择总的使用率还是每个cpu的使用率
for x in range(10):
    print(psutil.cpu_percent(interval=1))
    
    print(psutil.cpu_percent(interval=1,percpu=True))

```

##### 2.2 获取内存信息

```
import psutil
# 1. 获取系统内存的使用情况
print(psutil.virtual_memory())

# 2. 获取系统交换内存的统计信息
print(psutil.swap_memory())

```

##### 2.3 获取磁盘信息

```
# 1. 获取磁盘分区的信息
print(psutil.disk_partitions())
# 2. 获取磁盘的使用情况
print(psutil.disk_usage('/'))
# 3. 获取磁盘的IO统计信息（读写速度等）
print(psutil.disk_io_counters())

```

##### 2.4 获取网络信息

```
# 1. 获取总的网络IO信息
print(psutil.net_io_counters())
# 2. 获取网卡的IO信息
print(psutil.net_io_counters(pernic=True))
# 3. 获取网络接口信息
print(psutil.net_if_addrs())
# 4. 获取网络接口状态信息
print(psutil.net_if_stats())

```

##### 2.5 获取其他系统信息

```
# 获取系统的开机时间，并转化为自然的格式
print(psutil.boot_time())
# 获取连接系统的用户列表
print(psutil.users())
# 获取系统全部的进程信息
print(psutil.pids())
# 获取单个进程的信息, 获取指定进程ID=780
print(psutil.Process(780))

```

##### 2.6 模拟出ps命令的效果

```
print(psutil.test())

```

##### 2.7 以json的形式返回进程的pid和名称

```
for proc in psutil.process_iter(['pid', 'name']):
    print(proc.info)

# 运行结果入下：
{<!-- -->'pid': 35907, 'name': 'Google Chrome Helper (Renderer)'}
{<!-- -->'pid': 36575, 'name': 'com.apple.Safari.SafeBrowsing.Service'}
{<!-- -->'pid': 36729, 'name': 'com.apple.AppleU'}

```

❤️ 如果觉得有用，可以关注或者收藏一下哦 ！！！❤️
