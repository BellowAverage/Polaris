
--- 
title:  在CentOS 7中使用Python 3执行系统命令 
tags: []
categories: [] 

---
#### 1. 使用`os.system()`

这个方法简单直接，但它不返回命令的输出，只返回命令的退出状态。如果你只需要知道命令是否成功执行，这个方法就足够了。

```
import os

cmd = "ls -l"
status = os.system(cmd)

if status == 0:
    print("Command executed successfully")
else:
    print("Command execution failed")

```

#### 2. 使用`subprocess.run()`

这是从Python 3.5开始推荐的方式，它提供了更多的功能和灵活性。特别是，它允许你捕获命令的输出。

```
import subprocess

try:
    result = subprocess.run(["ls", "-l"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("stdout:", result.stdout)
except subprocess.CalledProcessError as e:
    print("Error executing command:", e)

```

#### 3. 使用`subprocess.Popen()`

当你需要更细粒度的控制，比如非阻塞读取输出或写入输入到进程，`subprocess.Popen()`是一个更复杂但更强大的选择。

```
import subprocess

process = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()

print("stdout:", stdout)
if process.returncode != 0:
    print("stderr:", stderr)

```

#### 注意事项
- 在CentOS 7上，默认可能不会安装Python 3。你可能需要手动安装Python 3及其pip包管理器。- 当执行需要特定权限的命令时（例如，操作系统级别的任务），确保你的Python脚本以合适的用户权限运行。- 对于一些复杂的命令，特别是那些涉及管道（`|`）、重定向（`&gt;`、`&lt;`）等Shell特性的命令，可能需要通过`shell=True`参数传递给`subprocess.run()`或`subprocess.Popen()`，或者将命令作为一个字符串而不是列表传递。但要小心使用`shell=True`，因为它可能会引入安全风险，特别是当命令字符串来自不可信的输入时。
在使用这些方法时，请确保你的Python脚本考虑到了CentOS 7环境的特点，包括任何潜在的路径和权限问题。
