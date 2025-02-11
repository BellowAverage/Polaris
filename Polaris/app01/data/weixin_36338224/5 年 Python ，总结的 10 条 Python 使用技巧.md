
--- 
title:  5 年 Python ，总结的 10 条 Python 使用技巧 
tags: []
categories: [] 

---
今天给大家分享 10 个我平时整理非常实用的 Python 开发小技巧，内容目录如下：

<img src="https://img-blog.csdnimg.cn/20201028195239947.png" alt="">

值得一提的是，这 10 个技巧全部收录在我自己写的 《Python黑魔法指南》里。

<img src="https://img-blog.csdnimg.cn/20201028195241698.png" alt="">

### 1. 如何在运行状态查看源代码？

查看函数的源代码，我们通常会使用 IDE 来完成。

比如在 PyCharm 中，你可以 Ctrl + 鼠标点击 进入函数的源代码。

那如果没有 IDE 呢？

当我们想使用一个函数时，如何知道这个函数需要接收哪些参数呢？

当我们在使用函数时出现问题的时候，如何通过阅读源代码来排查问题所在呢？

这时候，我们可以使用 inspect 来代替 IDE 帮助你完成这些事

```
# demo.py
import inspect


def add(x, y):
    return x + y

print("===================")
print(inspect.getsource(add))
```

运行结果如下

```
$ python demo.py
===================
def add(x, y):
    return x + y
```

### 2. 如何关闭异常自动关联上下文？

当你在处理异常时，由于处理不当或者其他问题，再次抛出另一个异常时，往外抛出的异常也会携带原始的异常信息。

就像这样子。

```
try:
    print(1 / 0)
except Exception as exc:
    raise RuntimeError("Something bad happened")
```

从输出可以看到两个异常信息

```
Traceback (most recent call last):
  File "demo.py", line 2, in &lt;module&gt;
    print(1 / 0)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "demo.py", line 4, in &lt;module&gt;
    raise RuntimeError("Something bad happened")
RuntimeError: Something bad happened
```

如果在异常处理程序或 finally 块中引发异常，默认情况下，异常机制会隐式工作会将先前的异常附加为新异常的 `__context__`属性。这就是 Python 默认开启的自动关联异常上下文。

如果你想自己控制这个上下文，可以加个 from 关键字（`from` 语法会有个限制，就是第二个表达式必须是另一个异常类或实例。），来表明你的新异常是直接由哪个异常引起的。

```
try:
    print(1 / 0)
except Exception as exc:
    raise RuntimeError("Something bad happened") from exc
```

输出如下

```
Traceback (most recent call last):
  File "demo.py", line 2, in &lt;module&gt;
    print(1 / 0)
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "demo.py", line 4, in &lt;module&gt;
    raise RuntimeError("Something bad happened") from exc
RuntimeError: Something bad happened
```

当然，你也可以通过`with_traceback()`方法为异常设置上下文`__context__`属性，这也能在`traceback`更好的显示异常信息。

```
try:
    print(1 / 0)
except Exception as exc:
    raise RuntimeError("bad thing").with_traceback(exc)
```

最后，如果我想彻底关闭这个自动关联异常上下文的机制？有什么办法呢？

可以使用 `raise...from None`，从下面的例子上看，已经没有了原始异常

```
$ cat demo.py
try:
    print(1 / 0)
except Exception as exc:
    raise RuntimeError("Something bad happened") from None
$
$ python demo.py
Traceback (most recent call last):
  File "demo.py", line 4, in &lt;module&gt;
    raise RuntimeError("Something bad happened") from None
RuntimeError: Something bad happened
(PythonCodingTime)
```

### 3. 最快查看包搜索路径的方式

当你使用 import 导入一个包或模块时，Python 会去一些目录下查找，而这些目录是有优先级顺序的，正常人会使用 sys.path 查看。

```
&gt;&gt;&gt; import sys
&gt;&gt;&gt; from pprint import pprint   
&gt;&gt;&gt; pprint(sys.path)
['',
 '/usr/local/Python3.7/lib/python37.zip',
 '/usr/local/Python3.7/lib/python3.7',
 '/usr/local/Python3.7/lib/python3.7/lib-dynload',
 '/home/wangbm/.local/lib/python3.7/site-packages',
 '/usr/local/Python3.7/lib/python3.7/site-packages']
&gt;&gt;&gt; 
```

那有没有更快的方式呢？

我这有一种连 console 模式都不用进入的方法呢？

你可能会想到这种，但这本质上与上面并无区别

```
[wangbm@localhost ~]$ python -c "print('\n'.join(__import__('sys').path))"

/usr/lib/python2.7/site-packages/pip-18.1-py2.7.egg
/usr/lib/python2.7/site-packages/redis-3.0.1-py2.7.egg
/usr/lib64/python27.zip
/usr/lib64/python2.7
/usr/lib64/python2.7/plat-linux2
/usr/lib64/python2.7/lib-tk
/usr/lib64/python2.7/lib-old
/usr/lib64/python2.7/lib-dynload
/home/wangbm/.local/lib/python2.7/site-packages
/usr/lib64/python2.7/site-packages
/usr/lib64/python2.7/site-packages/gtk-2.0
/usr/lib/python2.7/site-packages
```

这里我要介绍的是比上面两种都方便的多的方法，一行命令即可解决

```
[wangbm@localhost ~]$ python3 -m site
sys.path = [
    '/home/wangbm',
    '/usr/local/Python3.7/lib/python37.zip',
    '/usr/local/Python3.7/lib/python3.7',
    '/usr/local/Python3.7/lib/python3.7/lib-dynload',
    '/home/wangbm/.local/lib/python3.7/site-packages',
    '/usr/local/Python3.7/lib/python3.7/site-packages',
]
USER_BASE: '/home/wangbm/.local' (exists)
USER_SITE: '/home/wangbm/.local/lib/python3.7/site-packages' (exists)
ENABLE_USER_SITE: True
```

从输出你可以发现，这个列的路径会比 sys.path 更全，它包含了用户环境的目录。

### 4. 将嵌套 for 循环写成单行

我们经常会如下这种嵌套的 for 循环代码

```
list1 = range(1,3)
list2 = range(4,6)
list3 = range(7,9)
for item1 in list1:
    for item2 in list2:
          for item3 in list3:
              print(item1+item2+item3)
```

这里仅仅是三个 for 循环，在实际编码中，有可能会有更层。

这样的代码，可读性非常的差，很多人不想这么写，可又没有更好的写法。

这里介绍一种我常用的写法，使用 itertools 这个库来实现更优雅易读的代码。

```
from itertools import product
list1 = range(1,3)
list2 = range(4,6)
list3 = range(7,9)
for item1,item2,item3 in product(list1, list2, list3):
    print(item1+item2+item3)
```

输出如下

```
$ python demo.py
12
13
13
14
13
14
14
15
```

### 5. 如何使用 print 输出日志

初学者喜欢使用 print 来调试代码，并记录程序运行过程。

但是 print 只会将内容输出到终端上，不能持久化到日志文件中，并不利于问题的排查。

如果你热衷于使用 print 来调试代码（虽然这并不是最佳做法），记录程序运行过程，那么下面介绍的这个 print 用法，可能会对你有用。

Python 3 中的 print 作为一个函数，由于可以接收更多的参数，所以功能变为更加强大，指定一些参数可以将 print 的内容输出到日志文件中

代码如下：

```
&gt;&gt;&gt; with open('test.log', mode='w') as f:
...     print('hello, python', file=f, flush=True)
&gt;&gt;&gt; exit()

$ cat test.log
hello, python
```

### 6. 如何快速计算函数运行时间

计算一个函数的运行时间，你可能会这样子做

```
import time

start = time.time()

# run the function

end = time.time()
print(end-start)
```

你看看你为了计算函数运行时间，写了几行代码了。

有没有一种方法可以更方便的计算这个运行时间呢？

有。

有一个内置模块叫 timeit

使用它，只用一行代码即可

```
import time
import timeit

def run_sleep(second):
    print(second)
    time.sleep(second)

# 只用这一行
print(timeit.timeit(lambda :run_sleep(2), number=5))
```

运行结果如下

```
2
2
2
2
2
10.020059824
```

### 7. 利用自带的缓存机制提高效率

缓存是一种将定量数据加以保存，以备迎合后续获取需求的处理方式，旨在加快数据获取的速度。

数据的生成过程可能需要经过计算，规整，远程获取等操作，如果是同一份数据需要多次使用，每次都重新生成会大大浪费时间。所以，如果将计算或者远程请求等操作获得的数据缓存下来，会加快后续的数据获取需求。

为了实现这个需求，Python 3.2 + 中给我们提供了一个机制，可以很方便的实现，而不需要你去写这样的逻辑代码。

这个机制实现于 functool 模块中的 lru_cache 装饰器。

```
@functools.lru_cache(maxsize=None, typed=False)
```

参数解读：
- maxsize：最多可以缓存多少个此函数的调用结果，如果为None，则无限制，设置为 2 的幂时，性能最佳- typed：若为 True，则不同参数类型的调用将分别缓存。
举个例子

```
from functools import lru_cache

@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y

print(add(1, 2))
print(add(1, 2))
print(add(2, 3))
```

输出如下，可以看到第二次调用并没有真正的执行函数体，而是直接返回缓存里的结果

```
calculating: 1 + 2
3
3
calculating: 2 + 3
5
```

下面这个是经典的斐波那契数列，当你指定的 n 较大时，会存在大量的重复计算

```
def fib(n):
    if n &lt; 2:
        return n
    return fib(n - 2) + fib(n - 1)
```

第六点介绍的 timeit，现在可以用它来测试一下到底可以提高多少的效率。

不使用 lru_cache 的情况下，运行时间 31 秒

```
import timeit

def fib(n):
    if n &lt; 2:
        return n
    return fib(n - 2) + fib(n - 1)



print(timeit.timeit(lambda :fib(40), number=1))
# output: 31.2725698948
```

由于使用了 lru_cache 后，运行速度实在太快了，所以我将 n 值由 30 调到 500，可即使是这样，运行时间也才 0.0004 秒。提高速度非常显著。

```
import timeit
from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n &lt; 2:
        return n
    return fib(n - 2) + fib(n - 1)

print(timeit.timeit(lambda :fib(500), number=1))
# output: 0.0004921059880871326
```

### 8. 在程序退出前执行代码的技巧

使用 atexit 这个内置模块，可以很方便的注册退出函数。

不管你在哪个地方导致程序崩溃，都会执行那些你注册过的函数。

示例如下

<img src="https://img-blog.csdnimg.cn/20201028195242749.png" alt="">

如果`clean()`函数有参数，那么你可以不用装饰器，而是直接调用`atexit.register(clean_1, 参数1, 参数2, 参数3='xxx')`。

可能你有其他方法可以处理这种需求，但肯定比上不使用 atexit 来得优雅，来得方便，并且它很容易扩展。

但是使用 atexit 仍然有一些局限性，比如：
- 如果程序是被你没有处理过的系统信号杀死的，那么注册的函数无法正常执行。- 如果发生了严重的 Python 内部错误，你注册的函数无法正常执行。- 如果你手动调用了`os._exit()`，你注册的函数无法正常执行。
### 9. 实现类似 defer 的延迟调用

在 Golang 中有一种延迟调用的机制，关键字是 defer，例如下面的示例

```
import "fmt"

func myfunc() {
    fmt.Println("B")
}

func main() {
    defer myfunc()
    fmt.Println("A")
}
```

输出如下，myfunc 的调用会在函数返回前一步完成，即使你将 myfunc 的调用写在函数的第一行，这就是延迟调用。

```
A
B
```

那么在 Python 中否有这种机制呢？

当然也有，只不过并没有 Golang 这种简便。

在 Python 可以使用 **上下文管理器** 达到这种效果

```
import contextlib

def callback():
    print('B')

with contextlib.ExitStack() as stack:
    stack.callback(callback)
    print('A')
```

输出如下

```
A
B
```

### 10. 如何流式读取数G超大文件

使用 with...open... 可以从一个文件中读取数据，这是所有 Python 开发者都非常熟悉的操作。

但是如果你使用不当，也会带来很大的麻烦。

比如当你使用了 read 函数，其实 Python 会将文件的内容一次性的全部载入内存中，如果文件有 10 个G甚至更多，那么你的电脑就要消耗的内存非常巨大。

```
# 一次性读取
with open("big_file.txt", "r") as fp:
    content = fp.read()
```

对于这个问题，你也许会想到使用 readline 去做一个生成器来逐行返回。

```
def read_from_file(filename):
    with open(filename, "r") as fp:
        yield fp.readline()
```

可如果这个文件内容就一行呢，一行就 10个G，其实你还是会一次性读取全部内容。

最优雅的解决方法是，在使用 read 方法时，指定每次只读取固定大小的内容，比如下面的代码中，每次只读取 8kb 返回。

```
def read_from_file(filename, block_size = 1024 * 8):
    with open(filename, "r") as fp:
        while True:
            chunk = fp.read(block_size)
            if not chunk:
                break

            yield chunk
```

上面的代码，功能上已经没有问题了，但是代码看起来代码还是有些臃肿。

 借助偏函数 和 iter 函数可以优化一下代码

```
from functools import partial

def read_from_file(filename, block_size = 1024 * 8):
    with open(filename, "r") as fp:
        for chunk in iter(partial(fp.read, block_size), ""):
            yield chunk
```
