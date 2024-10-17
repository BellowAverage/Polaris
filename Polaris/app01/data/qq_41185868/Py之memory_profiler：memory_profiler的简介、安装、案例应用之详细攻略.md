
--- 
title:  Py之memory_profiler：memory_profiler的简介、安装、案例应用之详细攻略 
tags: []
categories: [] 

---
Py之memory_profiler：memory_profiler的简介、安装、案例应用之详细攻略





**目录**



















## **memory_profiler的简介**

memory_profiler 是一个用于 Python 的内存分析工具，它可以帮助你监测和分析 Python 程序的内存使用情况，帮助你发现内存泄漏或者优化内存使用。







## **memory_profiler的安装**

```
pip install -i https://mirrors.aliyun.com/pypi/simple memory_profiler
```

<img alt="" height="191" src="https://img-blog.csdnimg.cn/direct/6f1993dfec404b05bdff6d8f459dacd0.png" width="1200">





## **memory_profiler的案例应用**

### **<strong><strong>1、使用 memory_profiler 来分析函数的内存使用情况**</strong></strong>

```
# example.py

from memory_profiler import profile

@profile
def my_func():
    a = [1] * (10 ** 6)  # 创建一个包含百万个元素的列表
    b = [2] * (2 * 10 ** 7)  # 创建一个包含两千万个元素的列表
    del b  # 删除变量 b，释放内存
    return a

if __name__ == "__main__":
    my_func()

```

为了运行内存分析，你可以在终端中执行以下命令

```
python -m memory_profiler example.py
```

执行命令后，memory_profiler 将会逐行分析 my_func() 函数的内存使用情况，并将结果打印出来，帮助你了解函数在执行过程中的内存占用情况，以便发现潜在的内存问题。








