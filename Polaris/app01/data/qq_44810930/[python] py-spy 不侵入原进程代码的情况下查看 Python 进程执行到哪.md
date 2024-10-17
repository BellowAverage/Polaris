
--- 
title:  [python] py-spy 不侵入原进程代码的情况下查看 Python 进程执行到哪 
tags: []
categories: [] 

---
如果你不想修改原来的代码，也可以考虑使用第三方工具来实现在不侵入原进程代码的情况下查看 Python 进程执行到哪一行代码了。一个常用的工具是 `py-spy`，它可以在不需要修改源代码的情况下对 Python 进程进行采样和调试。

你可以按照以下步骤来使用 `py-spy` 工具：
1. 首先，安装 `py-spy` 工具。可以通过 pip 来进行安装：
```
pip install py-spy -i https://pypi.tuna.tsinghua.edu.cn/simple

```

## 监控正在执行的python程序
1. 然后，在终端中运行以下命令，使用 `py-spy` 来监视正在运行的 Python 进程：
```
py-spy top --pid &lt;your_python_process_id&gt;

```

请将 `&lt;your_python_process_id&gt;` 替换为你要监视的 Python 进程的进程 ID。
1.  `py-spy` 将会显示 Python 进程的运行信息，包括当前执行的函数和源文件位置。 1.  `py-spy` 中的快捷键 
```
按键      动作
     1      按 %Own 排序（当前在函数中花费的时间的百分比）
     2      按 %Total 排序（当前在函数及其子函数中花费的时间的百分比）
     3      按 OwnTime 排序（在函数中总共花费的时间）
     4      按 TotalTime 排序（在函数及其子函数中总共花费的时间）
    L,l     在行号或函数之间切换聚合方式
    R,r     重置统计信息
    X,x     退出帮助界面

```

## 生成火焰图

`py-spy record --pid &lt;PID&gt; --output profile.svg `
