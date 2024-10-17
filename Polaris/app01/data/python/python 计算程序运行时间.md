
--- 
title:  python 计算程序运行时间 
tags: []
categories: [] 

---
python 计算程序运行用时，主要有两种方法：

time.time() 和 time.clock()

使用方法如下：

**1. time.time()**

```
import time
start_time = time.time()    # 程序开始时间
# function()   运行的程序
end_time = time.time()    # 程序结束时间
run_time = end_time - start_time    # 程序的运行时间，单位为秒
print(run_time)

```

**2. time.clock()**

与time.time()用法一致。

```
import time
start_time = time.clock()    # 程序开始时间
# function()   运行的程序
end_time = time.clock()    # 程序结束时间
run_time = end_time - start_time    # 程序的运行时间，单位为秒
print(run_time)

```

附：**time.sleep() **让程序暂停指定的秒数，如 time.sleep(0.5)

**二者的区别为：**

**time.time() **为wall time(墙上时钟)，是系统时钟的时间戳（1970-01-01 00:00:00 UTC 后经过的浮点秒数）。

**time.clock() **为该程序运行后CPU运行的浮点秒数。不包含**sleep**用时**。**

所以在统计程序运行用时时，应按照自身需求进行选用。
