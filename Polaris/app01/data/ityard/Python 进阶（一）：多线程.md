
--- 
title:  Python 进阶（一）：多线程 
tags: []
categories: [] 

---


#### 目录
- - <ul><li>- - - - - - - 


## 1. 相关概念

### 1.1 解释器

Python 解释器的主要作用是将我们在 `.py` 文件中写好的代码交给机器去执行，比较常见的解释器包括如下几种：
-  **CPython**：官方解释器，我们从下载安装后获得的就是这个解释器，它使用 C 语言开发，是使用范围最广泛的 Python 解释器。 -  **Jython**：由 Java 编写，它可以将 Python 代码编译成 Java 字节码，再由 JVM 执行对应的字节码。 -  **IronPython**：与 Jython 类似，它由 C# 编写，是运行在 .Net 平台上的解释器。 -  **IPython**：基于 CPython 的一个交互式解释器，它主要增强了 CPython 的交互方式。 -  **PyPy**：采用了 JIT 技术，它是一个关注执行速度的 Python 解释器，该解释器可以明显提升 Python 代码的执行速度。 
### 1.2 GIL

GIL 全称 global interpreter lock，中文译为全局解释器锁，CPython 解释器就是通过 GIL 机制来确保同一时刻只有一个线程执行 Python 代码的，这样做十分方便的帮助 CPython 解决了并发访问的线程安全问题，但却牺牲了在多处理器上的并行性，所以 CPython 解释器下的多线程并不是真正意义上的多线程。

我们可能会有一个疑问：既然 CPython 解释器使用 GIL 机制牺牲了多线程的并行性，那么把 GIL 去掉换用其他方式实现不行吗？在说这个问题之前，我们先简单了解一下基本情况：最初因 GIL 可以简单、快捷的解决多线程并发访问的安全问题选择了这种机制，随后又有大量的代码库开发者开始依赖这种特性，随之时间的推移，人们开始意识到了并行性的问题，但这时已经到了尾大不掉的程度了，所以现实情况是：尽管可以去掉 GIL，但工程量太大了。

## 2. threading

Python（CPython） 提供了 `_thread` 和 `threading` 两个线程模块，`_thread` 是低级模块，`threading` 对 `_thread` 进行了封装，提高了 `_thread` 原有功能的易用性以及扩展了新功能，通常我们只需要使用 `threading` 模块就可以了，这里我们也只对 `threading` 模块进行详细介绍。

### 2.1 方法属性

首先，我们来看一下 `threading` 模块的直接方法和属性。

**threading.enumerate()** 以列表形式返回当前所有存活的 threading.Thread 对象。

**threading.active_count()** 返回当前存活的 threading.Thread 对象，等于 len(threading.enumerate())。

**threading.current_thread()** 返回当前对应调用者控制的 threading.Thread 对象，如果调用者的控制线程不是利用 threading 创建，则会返回一个功能受限的虚拟线程对象。

**threading.get_ident()** 返回当前线程的线程标识符，它是一个非零的整数，其值没有直接含义，它可能会在线程退出，新线程创建时被复用。

**threading.main_thread()** 返回主线程对象，一般情况下，主线程是 Python 解释器开始时创建的线程。

**threading.stack_size([size])** 返回创建线程时用的堆栈大小，可选参数 size 指定之后新建线程的堆栈大小，size 值需要为 0 或者最小是 32768（32KiB）的一个正整数，如不指定 size，则默认为 0。

**threading.get_native_id()** 返回内核分配给当前线程的原生集成线程 ID，其值是一个非负整数。

**threading.TIMEOUT_MAX** 指定阻塞函数（如：Lock.acquire()， Condition.wait() …）中形参 timeout 允许的最大值，传入超过这个值的 timeout 会抛出 OverflowError 异常。

### 2.2 线程对象

先了解一下 Python 守护线程基本概念。
-  **守护线程**：当一个线程被标记为守护线程时，Python 程序会在剩下的线程都是守护线程时退出，即等待所有非守护线程运行完毕；守护线程在程序关闭时会突然关闭，可能会导致资源不能被正确释放的的问题，如：已经打开的文档等。 -  **非守护线程**：通常我们创建的线程默认就是非守护线程，Python 程序退出时，如果还有非守护线程在运行，程序会等待所有非守护线程运行完毕才会退出。 
**threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)** 创建线程对象，参数说明如下所示。
- group：通常默认即可，作为日后扩展 ThreadGroup 类实现而保留。- target：用于 run() 方法调用的可调用对象，默认为 None。- name：线程名称，默认是 Thread-N 格式构成的唯一名称，其中 N 是十进制数。- args：用于调用目标函数的参数元组，默认为 ()。- kwargs：用于调用目标函数的关键字参数字典，默认为 {}。- daemon：设置线程是否为守护模式，默认为 None。
看一下线程对象 threading.Thread 的方法和属性。
- **start()**：启动线程。- **run()**：线程执行具体功能的方法。- **join(timeout=None)**：当 timeout 为 None 时，会等待至线程结束；当 timeout 不为 None 时，会等待至 timeout 时间结束，单位为秒。- **is_alive()**：判断线程是否存活。- **getName()**：返回线程名。- **setName()**：设置线程名。- **isDaemon()**：判断线程是否为守护线程。- **setDaemon()**：设置线程是否为守护线程。- **name**：线程名。- **ident**：线程标识符。- **daemon**：线程是否为守护线程。
我们可以通过实例化 threading.Thread 来创建线程，也可以使用继承 threading.Thread 的子类来创建。

**实例化 threading.Thread**

```
import threading
import time

def target(sleep):
    time.sleep(sleep)
    print('当前线程为:', threading.current_thread().name,' ', 'sleep:', sleep)

if __name__ == '__main__':
    t1 = threading.Thread(name='t1', target=target, args=(1,))
    t2 = threading.Thread(name='t2', target=target, args=(2,))
    t1.start()
    t2.start()
    print('主线程结束')

```

**继承 threading.Thread**

```
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, sleep, name):
        super().__init__()
        self.sleep = sleep
        self.name = name
    def run(self):
        time.sleep(self.sleep)
        print('name：' + self.name)

if __name__ == '__main__':
    t1 = MyThread(1, 't1')
    t2 = MyThread(1, 't2')
    t1.start()
    t2.start()

```

### 2.3 锁对象

同一变量在多线之间是共享的，任何一个变量都可以被所有线程修改，当多个线程一起修改同一变量时，很可能互相冲突得不到正确的结果，造成线程安全问题。通过示例看一下：

```
import threading

a = 5
def oper(b):
    global a
    a = a - b
    a = a + b

def target(b):
    for i in range(100000):
        oper(b)

if __name__ == '__main__':
    m = 10
    while m &gt; 0:
        t1 = threading.Thread(target=target, args=(1,))
        t2 = threading.Thread(target=target, args=(2,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(a)
        m = m - 1

```

执行结果：

```
5
5
5
6
6

```

正常情况下，oper(b) 操作会使 a 的值保持不变，但从多线程的执行结果来看，我们发现出现了错误的结果，并且每次执行的结果可能不同，通常这种问题我们可以使用加锁的方式解决。

**threading.Lock** 实现原始锁对象的类，一旦一个线程获得一个锁，会阻塞随后尝试获得锁的线程，直到它被释放，通常称其为互斥锁，它是由 _thread 模块直接扩展实现的。它具有如下方法：
-  acquire(blocking=True, timeout=-1)：可以阻塞或非阻塞地获得锁，参数 blocking 用来设置是否阻塞，timeout 用来设置阻塞时间，当 blocking 为 False 时 timeout 将被忽略。 -  release()：释放锁。 -  locked()：判断是否获得了锁，如果获得了锁则返回 True。 
**threading.RLock** 可重入锁（也称递归锁）类，一旦线程获得了重入锁，同一个线程再次获取它将不阻塞，重入锁必须由获取它的线程释放。它具有如下方法：
-  acquire(blocking=True, timeout=-1)：解释同上。 -  release()：解释同上。 
我们对上述代码进行加锁操作，如下所示：

```
import threading

# 创建锁
lock = threading.Lock()

a = 5
def oper(b):
    # 获取锁
    lock.acquire()
    global a
    a = a - b
    a = a + b
    # 释放锁
    lock.release()

def target(b):
    for i in range(100000):
        oper(b)

if __name__ == '__main__':
    m = 5
    while m &gt; 0:
        t1 = threading.Thread(target=target, args=(1,))
        t2 = threading.Thread(target=target, args=(2,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(a)
        m = m - 1

```

执行结果：

```
5
5
5
5
5

```

我们可以尝试多次执行，现在每次都可以获得正确的结果了。

### 2.4 条件对象

条件对象总是与某种类型的锁对象相关联，锁对象可以通过传入获得，或者在缺省的情况下自动创建。

**threading.Condition(lock=None)** 实现条件对象的类。它具有如下方法：
-  acquire(*args)：请求底层锁。 -  release()：释放底层锁。 -  wait(timeout=None)：等待直到被通知或发生超时。 -  wait_for(predicate, timeout=None)：等待直到条件计算为 True，predicate 是一个可调用对象且它的返回值可被解释为一个布尔值。 -  notify(n=1)：默认唤醒一个等待该条件的线程。 -  notify_all()：唤醒所有正在等待该条件的线程。 
使用条件对象的典型场景是将锁用于同步某些共享状态的权限，那些关注某些特定状态改变的线程重复调用 wait() 方法，直到所期望的改变发生；对于修改状态的线程，它们将当前状态改变为可能是等待者所期待的新状态后，调用 notify() 方法或者 notify_all() 方法。

```
import time
import threading

# 创建条件对象
c = threading.Condition()
privilege = 0

def getPri():
    global privilege
    c.acquire()
    c.wait()
    print(privilege)
    c.release()

def updPri():
    time.sleep(5)
    c.acquire()
    global privilege
    privilege = 1
    c.notify()
    c.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=getPri)
    t2 = threading.Thread(target=updPri)
    t1.start()
    t2.start()

```

### 2.5 信号量对象

和锁机制一样，信号量机制也是一种实现线程同步的机制，不过它比锁多了一个计数器，这个计数器主要用来计算当前剩余的锁的数量。

**threading.Semaphore(value=1)** 信号量实现类，可选参数 value 赋予内部计数器初始值，默认值为 1 。它具有如下方法：
-  acquire(blocking=True, timeout=None)：获取一个信号量，参数 blocking 用来设置是否阻塞，timeout 用来设置阻塞时间。 -  release()：释放一个信号量，将内部计数器的值增加1。 
```
import threading

# 创建信号量对象
s = threading.Semaphore(10)

a = 5
def oper(b):
    # 获取信号量
    s.acquire()
    global a
    a = a - b
    a = a + b
    # 释放信号量
    s.release()

def target(b):
    for i in range(100000):
        oper(b)

if __name__ == '__main__':
    m = 5
    while m &gt; 0:
        t1 = threading.Thread(target=target, args=(1,))
        t2 = threading.Thread(target=target, args=(2,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(a)
        m = m - 1

```

### 2.6 事件对象

一个线程发出事件信号，其他线程等待该信号，这是最简单的线程之间通信机制之一。

**threading.Event** 实现事件对象的类。它有如下方法：
-  is_set()：当内部标志为 True 时返回 True。 -  set()：将内部标志设置为 True。 -  clear()：将内部标志设置为 False。 -  wait(timeout=None)：阻塞线程直到内部变量为 True。 
```
import time
import threading

# 创建事件对象
event = threading.Event()

def dis_class():
    time.sleep(5)
    event.wait()
    print('同学们下课了')


def bell():
    time.sleep(3)
    print('下课铃声响了')
    event.set()

if __name__ == '__main__':
    t1 = threading.Thread(target=bell)
    t2 = threading.Thread(target=dis_class)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

```

参考： https://docs.python.org/3.8/library/threading.html#barrier-objects

<img src="https://img-blog.csdnimg.cn/20200127132036938.png#pic_center" alt="" width="600">
