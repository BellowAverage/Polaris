
--- 
title:  python3.7 中的断点调试工具 breakpoint 
tags: []
categories: [] 

---
在Python 3.7中，引入了一个新的内置函数`breakpoint()`，这是一个非常实用的特性，旨在为开发者提供一个标准化的方式来启动调试器。



#### 文章目录
- <ul><li><ul><li>- - - - 


#### 使用`breakpoint()`

在你希望暂停并开始调试的代码位置，只需添加一行`breakpoint()`。当Python执行到这一行时，程序将会暂停，并进入调试模式，允许你检查当前的程序状态、变量值、执行步骤等。

```
def my_function(x):
    for i in range(x):
        print(i)
        if i == 2:
            breakpoint()  # 程序将在这里暂停

my_function(5)

```

在上面的例子中，当循环变量`i`等于2时，程序会暂停并进入调试模式。

#### 检查和修改变量

一旦进入调试模式，你就可以使用`pdb`的命令来检查和修改变量了。这里有几个常用的命令：
- `p 表达式`：打印表达式的值。例如，`p x`将显示变量`x`的当前值。- `pp 表达式`：以更易于阅读的方式打印表达式的值（pretty print）。- `n`（next）：执行下一行代码。- `c`（continue）：继续执行，直到遇到下一个断点。- `l`（list）：显示当前正在执行的代码周围的几行。- `s`（step）：进入函数。- `r`（return）：继续执行，直到当前函数返回。- `q`（quit）：退出调试器，结束程序执行。
#### 定制化`breakpoint()`

`breakpoint()`的另一个优点是它的行为可以通过环境变量进行定制。
-  如果你将`PYTHONBREAKPOINT`设置为0，那么`breakpoint()`将完全被禁用，即使代码中有`breakpoint()`调用，程序也会忽略它，继续执行。 -  你还可以设置`PYTHONBREAKPOINT`为其他调试器入口函数的路径。例如，如果你更喜欢使用`ipdb`而不是`pdb`作为你的调试器，你可以将环境变量设置为`ipdb.set_trace`。 
#### 示例：使用环境变量禁用`breakpoint()`

假设你有一个脚本，其中包含`breakpoint()`调用，但在某些情况下，你希望脚本忽略这些调用并正常运行。你可以在运行脚本之前设置环境变量：

```
export PYTHONBREAKPOINT=0
python your_script.py

```

这将禁用所有的`breakpoint()`调用，脚本将不会进入调试模式。

#### 总结

`breakpoint()`是Python 3.7引入的一个非常有用的特性，它简化了调试过程，使得在代码中插入断点变得非常方便。通过使用环境变量，你还可以灵活地控制`breakpoint()`的行为，包括完全禁用它或者指定不同的调试器。这为Python开发者提供了一个强大且灵活的调试工具。
