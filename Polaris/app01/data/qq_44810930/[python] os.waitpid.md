
--- 
title:  [python] os.waitpid 
tags: []
categories: [] 

---
`os.waitpid()` 是 Python 中用于等待子进程改变状态的函数。这个函数是 `os` 模块的一部分，它提供了一个方式来收集子进程的状态信息，或者等待子进程结束。`os.waitpid()` 函数是 Unix/Linux 系统上的系统调用 `waitpid()` 的封装。

#### 使用 `os.waitpid()`

`os.waitpid()` 函数的基本用法如下：

```
pid, status = os.waitpid(pid, options)

```
- **pid**：要等待的子进程的PID。如果 pid 为 -1，表示等待任何子进程。- **options**：控制函数行为的选项。常用的选项包括 `os.WNOHANG`（如果没有子进程退出，则不阻塞）和 `os.WUNTRACED`（除了返回终止子进程的信息外，还返回因信号而停止的子进程信息）。- 返回值：`os.waitpid()` 返回一个元组 `(pid, status)`，其中 `pid` 是终止的子进程的 PID，`status` 是子进程的退出信息，可以使用 `os` 模块中的函数（如 `os.WIFEXITED(status)`，`os.WEXITSTATUS(status)` 等）进行解析。
#### 示例

下面是一个简单的示例，展示如何使用 `os.fork()` 创建子进程，并用 `os.waitpid()` 等待子进程结束：

```
import os
import time

pid = os.fork()

if pid == 0:
    # 子进程
    print("Child Process: Starting")
    time.sleep(2)  # 模拟工作，睡眠2秒
    print("Child Process: Exiting")
else:
    # 父进程
    print("Parent Process: Waiting for child to exit")
    finished_pid, status = os.waitpid(pid, 0)  # 等待子进程结束
    if os.WIFEXITED(status):
        print(f"Parent Process: Child exited with status {<!-- -->os.WEXITSTATUS(status)}")

```

在这个示例中，父进程通过调用 `os.waitpid()` 来等待子进程结束。`os.waitpid()` 将阻塞父进程，直到子进程结束。子进程通过 `time.sleep(2)` 模拟耗时操作，然后退出。父进程在子进程结束后继续执行，检查子进程的退出状态，并打印相关信息。

#### 注意事项
- `os.waitpid()` 只在 Unix/Linux 系统上可用。- 使用 `os.waitpid()` 需要注意正确处理子进程的退出状态，以避免产生僵尸进程（Zombie Process）。- 如果子进程已经结束，但父进程没有调用 `os.waitpid()` 或类似的函数来收集子进程的状态信息，子进程将变成僵尸进程，直到其状态被收集。