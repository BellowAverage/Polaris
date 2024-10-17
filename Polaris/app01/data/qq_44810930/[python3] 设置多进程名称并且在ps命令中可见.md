
--- 
title:  [python3] 设置多进程名称并且在ps命令中可见 
tags: []
categories: [] 

---
>  
 Centos7 系统 


`setproctitle` 是一个 Python 模块，用于设置进程标题（process title）。进程标题是在系统中用来标识进程的名字，通常会显示在系统级的进程管理工具（如 `ps` 命令）中。通过设置进程标题，可以让进程在系统级的进程管理工具中展示自定义的名称，方便用户查看和管理进程。

```
pip install setproctitle

```

安装完成后，你就可以在 Python 代码中使用 `setproctitle` 模块来设置进程标题，使进程在系统级的进程管理工具中展示自定义的名称。

要在 CentOS 7 系统上使用 Python 3 开启多进程并设置进程名称

```
import multiprocessing
import os
import setproctitle

# 定义一个函数，用于在子进程中执行的任务
def task(num):
    # 设置进程名称
    setproctitle.setproctitle(f"MyProcess-{<!-- -->num}")
    print(f"Process {<!-- -->num} (PID: {<!-- -->os.getpid()}) is running")

if __name__ == '__main__':
    # 创建多个子进程
    processes = []
    for i in range(5):
        process = multiprocessing.Process(target=task, args=(i,))
        processes.append(process)
        process.start()

    # 等待所有子进程结束
    for process in processes:
        process.join()

    print("All processes have finished")

```

<img src="https://img-blog.csdnimg.cn/direct/05b30bf10f674022a8cfe34405923802.png" alt="在这里插入图片描述">
