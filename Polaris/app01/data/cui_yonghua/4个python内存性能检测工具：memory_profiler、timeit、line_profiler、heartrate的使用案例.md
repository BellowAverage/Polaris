
--- 
title:  4个python内存性能检测工具：memory_profiler、timeit、line_profiler、heartrate的使用案例 
tags: []
categories: [] 

---
这里总结了4个比较好的python性能检测工具，包括内存使用、运行时间、执行次数等方面。

#### 1、memory_profiler查看内存的使用情况

memory_profiler可以用来测量python进程的内存使用情况。可以按行查看内存的使用情况。

memory_profiler 是一个监控进程内存消耗的模块，可以逐行分析 Python 程序的内存消耗。它是一个依赖 psutil 模块的纯 Python 模块。

只需要在目标函数上加个装饰器 @profile，就可以实现对此函数内存使用的统计。

安装：`pip install -U memory_profiler`

官方文档：

**案例1**，脚本如下：

```
from memory_profiler import profile

@profile
def base_func1():
    for n in range(10000):
        print(f'当前n的值是：{
     <!-- -->n}')


base_func1()

# 从返回的数据结果来看，执行当前函数使用了45.3 MiB的内存。返回结果如下：
# Line #    Mem usage    Increment  Occurrences   Line Contents
# ================================&amp;#
```
