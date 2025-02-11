
--- 
title:  [python] os.fork 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li><ul><li>- - - - 


`os.fork()` 是 Python 中用于 Unix/Linux 系统的一个函数，它在当前进程中创建一个子进程。这个函数是 `os` 模块的一部分，直接调用了 Unix/Linux 系统的 `fork` 系统调用。`fork` 系统调用非常基础且强大，允许操作系统创建一个新的进程，这个新进程是调用它的进程（父进程）的副本。

#### 使用 `os.fork()`

当 `os.fork()` 被调用时，它会创建一个新的子进程。这个函数在父进程中返回新创建的子进程的进程ID（PID），而在子进程中则返回 0。因此，可以通过检查 `os.fork()` 的返回值来确定当前代码是在父进程中运行还是在子进程中运行。

#### 注意事项
- `os.fork()` 只在 Unix/Linux 系统上可用。如果你试图在 Windows 系统上使用它，会抛出一个 `AttributeError` 异常。- 创建进程（尤其是在循环中）时需要谨慎，以避免无意中产生大量的进程，导致所谓的 “fork 炸弹”。
#### 示例

下面是一个简单的 `os.fork()` 使用示例，演示了如何创建一个子进程，并区分父进程和子进程的执行流：

```
import os

print(os.getpid(), '1')
pid = os.fork()

print(os.getpid(), '2')


if pid &gt; 0:
    # 父进程中，os.fork() 返回子进程的 PID
    print(f"I am the parent process. My PID is {<!-- -->os.getpid()} and my child's PID is {<!-- -->pid}.")
else:
    # 子进程中，os.fork() 返回 0
    print(f"I am the child process. My PID is {<!-- -->os.getpid()}.")

# 注意：这里的代码会在父进程和子进程中都执行
print("注意：这里的代码会在父进程和子进程中都执行")


if __name__ == "__main__":
    print(os.getpid(), '3')

```

在这个示例中，`os.fork()` 创建了一个子进程。我们通过检查 `os.fork()` 的返回值来判断当前是在父进程中还是子进程中，并输出相应的信息。父进程会打印自己的 PID 和子进程的 PID，而子进程只会打印自己的 PID。

<img src="https://img-blog.csdnimg.cn/direct/03980548ee644be2ab86a045756628d9.png" alt="在这里插入图片描述">

子进程会在`os.fork()`处 **复制**一整份的**父进程的资源**,

也就是说，如果父进程在`os.fork()` 之前`import`了一些模块，或者执行了一些代码，子进程也会自动继承这些`资源`。

**然后继续向下开始执行代码。**

#### 安全使用 `os.fork()`

在使用 `os.fork()` 时，要确保对资源进行适当管理，比如关闭不需要的文件描述符，确保子进程能够正确退出以避免僵尸进程，等等。此外，也要考虑到错误处理，比如 `fork` 调用失败时的情况。

#### 底层原理

在 Python 中，`os.fork()` 是通过底层的操作系统调用来实现的。具体地说，它使用了 POSIX 标准中的 `fork()` 系统调用。

`fork()` 系统调用会创建一个新的进程，新进程是原始进程的一个副本，包括代码、数据和资源等。在调用 `os.fork()` 时，操作系统会复制当前进程的所有信息，并将这个复制的进程作为新的子进程返回给父进程。

在底层，`fork()` 调用的过程如下：
1. 操作系统为子进程创建一个新的进程控制块（Process Control Block）来存储子进程的状态信息。1. 操作系统复制父进程的代码段、数据段和堆栈等信息到子进程的地址空间。1. 子进程开始执行从 `os.fork()` 后的代码，而父进程继续执行原有的代码。1. 在子进程中，`os.fork()` 返回值为 0，使得子进程能够根据返回值判断自己是子进程。1. 在父进程中，`os.fork()` 返回值为子进程的进程ID，使得父进程能够根据返回值判断自己是父进程。
需要注意的是，`fork()` 调用会在父进程和子进程中创建一个完全相同的进程映像，包括进程的状态、文件描述符等。因此，在 `fork()` 后，父进程和子进程是相互独立的，各自有自己的内存空间和资源。
