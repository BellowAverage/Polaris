
--- 
title:  python从写循环定时器学习Timer 
tags: []
categories: [] 

---
python 如何写一个定时器，循环定时做某一操作呢？

### Timer 对象

```
from threading import Timer
def hello(): 
    print "hello, world" 
   
t = Timer(10.0, hello) 
t.start()
复制代码
```

10秒后输出：

```
hello, world
复制代码
```

重点研究 `t = Timer(10.0, hello)` 这句代码，python 提供了一个，它会在指定的时间后执行某一操作；它的完整形式：

```
class threading.Timer(interval, function, args=[], kwargs={})
复制代码
```

`interval` 是时间间隔，`function` 是可调用的对象，`args` 和 `kwargs` 会作为 `function` 的参数。

**注意：这里只会执行一次 function，而不会一直定时执行，且 Timer 在执行操作的时候会创建一个新的线程。**

`Timer` 在 python2 和 python3 有点区别：

```
# p
```
