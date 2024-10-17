
--- 
title:  Python线程池 
tags: []
categories: [] 

---
Python可以配置线程池，线程池的作用：
-  预先开启设定的线程。当一个线程结束以后可以让程序继续使用该线程。 -  设置线程的最大数目，让系统不至于因为开启多个线程而崩溃。 -  在有大量空闲时间的进程中，配置多线程可以让程序并行处理，提高处理速度。 
线程池的基类是 concurrent.futures 模块中的 Executor，Executor 提供了两个子类，即 ThreadPoolExecutor 和 ProcessPoolExecutor，其中 ThreadPoolExecutor 用于创建线程池，而 ProcessPoolExecutor 用于创建进程池。
- Python的线程是有GIL锁的，所以是单核的。- Python的进程每个都有独立的GIL锁，所以是多核的，但是每个都需要独立的分配内存空间，所以空间占用大
使用线程池来执行线程任务的步骤如下：
- 调用 ThreadPoolExecutor 类的构造器创建一个线程池。- 定义一个普通函数作为线程任务。- 调用 ThreadPoolExecutor 对象的 submit() 方法来提交线程任务。- 调用 ThreadPoolExecutor 对象的 shutdown(wait = True) 方法来关闭线程池。
```
def fun(index):
	print(index)
	time.sleep(3)
	
from concurrent.futures import ThreadPoolExecutor
theard_pool = ThreadPoolExecutor(max_workers=2)
for i in range(1000):
	thread_pool.submit(fun, i)
thread_pool.shutdown(wait= True)

```

有这么几个问题：
- 按照逻辑而言，不一定能保证严格有序- 所有的任务都扔进队列实现的，所以在处理tb级别的数据的时候会出现溢出？？？（需要确认）