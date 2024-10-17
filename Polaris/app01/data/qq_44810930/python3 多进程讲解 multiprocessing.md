
--- 
title:  python3 多进程讲解 multiprocessing 
tags: []
categories: [] 

---
在Python中，`multiprocessing`模块提供了一个强大的基于进程的并行性。这意味着它允许你利用多个处理器上的多个核心，从而可以显著提高某些类型任务的执行速度。这对于CPU密集型任务特别有用，比如大规模数学计算、图像处理等。

#### 基本概念
- **进程**：进程是操作系统分配资源和调度的基本单位。每个进程都有自己独立的内存空间，因此进程间通信需要特定的机制（如管道、队列等）。- **线程**：线程是进程内的执行单元，同一进程内的线程共享该进程的内存空间。
与线程相比，进程之间的隔离级别更高，这使得进程更稳定，但创建和管理进程的开销也更大。

#### `multiprocessing`模块的核心组件
1. **Process**：用于表示一个进程对象。1. **Pool**：提供了一种方便的方法来并行地执行函数调用。1. **Queue**、**Pipe**：进程间通信（IPC）的机制。1. **Lock**、**Semaphore**等：用于进程间的同步。
#### 使用`Process`创建进程

下面是一个简单的例子，展示如何使用`multiprocessing.Process`来创建和启动一个进程：

```
from multiprocessing import Process

def my_function(name):
    print(f'Hello {<!-- -->name}')

if __name__ == '__main__':
    # 创建进程对象
    p = Process(target=my_function, args=('World',))
    # 启动进程
    p.start()
    # 等待进程结束
    p.join()

```

#### 使用`Pool`进行并行计算

如果你有大量的任务需要执行，并且这些任务是独立的，那么使用`Pool`类可以非常方便地将任务分发到多个进程中去执行。

```
from multiprocessing import Pool

def square(number):
    return number * number

if __name__ == '__main__':
    # 创建一个包含4个进程的池
    with Pool(4) as p:
        # map方法类似于内置的map函数，但在多个进程中并行执行
        results = p.map(square, range(10))
        print(results)

```

#### 进程间通信

进程间通信（IPC）可以使用`Queue`或`Pipe`完成。`Queue`是多生产者、多消费者队列，非常适合跨进程通信。

```
from multiprocessing import Process, Queue

def worker(q):
    q.put('Hello')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())  # 打印 "Hello"
    p.join()

```

#### 注意事项
- 在Windows系统上，如果你使用`multiprocessing`模块，确保将进程的启动代码放在`if __name__ == '__main__':`块中，以避免无限递归创建进程。- 进程间通信比线程间通信有更大的开销，因为它们不共享内存空间。- 对全局变量的修改在进程间不会互相影响，因为每个进程都有自己的地址空间。
`multiprocessing`模块提供了丰富的功能，可以帮助你有效地利用多核CPU来加速你的程序。正确地使用它，可以显著提高程序的性能。

## 在父进程中join了子进程, 但还是意外结束

当你在父进程中使用`join()`等待子进程结束时，通常期望的行为是父进程会一直阻塞，直到子进程完成其任务。然而，如果你观察到父进程和子进程都在子进程未正常结束时就被终止了，可能是由于以下几个原因导致的：
1.  **未捕获的异常**：如果子进程执行的代码中有异常抛出，并且这些异常没有被捕获处理，那么子进程可能会因为这个异常而提前终止。父进程在调用`join()`后，会发现子进程已经结束，因此继续执行或者也结束。确保子进程中的代码有良好的异常处理机制。 1.  **信号处理**：在Unix/Linux系统中，进程可以通过信号进行通信。某些信号（如SIGINT、SIGTERM）默认行为是终止进程。如果父进程或子进程收到这样的信号，它们可能会提前终止。如果你的程序需要处理中断（如用户按Ctrl+C），你可能需要在父进程和子进程中安装信号处理器来优雅地处理这些信号。 1.  **主动终止子进程**：如果代码中其他部分（可能是另一个线程）调用了子进程的`terminate()`方法，那么子进程会被立即终止。检查代码以确保没有不恰当的`terminate()`调用。 1.  **资源限制或系统策略**：在极少数情况下，操作系统可能因为资源限制（如内存不足）或特定的系统策略（如对进程数量的限制）而终止进程。检查系统日志（如`/var/log/syslog`或`/var/log/messages`）可能提供一些线索。 1.  **父进程先于子进程结束**：虽然你提到使用了`join()`，但如果有代码路径导致`join()`被跳过或未正确执行，父进程可能会先于子进程结束。确保所有路径都正确调用了`join()`。 
为了诊断问题，可以尝试以下方法：
- **增加日志记录**：在子进程的开始、各个关键点、以及正常结束处增加日志输出，可以帮助你确定子进程是否正常执行以及在何处终止。- **异常捕获**：确保子进程中的代码包含顶级异常捕获，以便于记录未捕获异常的信息。- **信号处理**：如果怀疑是信号导致的提前终止，可以在父进程和子进程中添加信号处理器，记录信号接收情况或尝试优雅地处理它们。
示例代码，展示如何在子进程中捕获异常：

```
from multiprocessing import Process
import traceback

def worker():
    try:
        # 模拟工作负载
        raise ValueError("An error occurred")
    except Exception as e:
        print(f"Caught exception in child process: {<!-- -->e}")
        traceback.print_exc()

if __name__ == "__main__":
    p = Process(target=worker)
    p.start()
    p.join()

```
