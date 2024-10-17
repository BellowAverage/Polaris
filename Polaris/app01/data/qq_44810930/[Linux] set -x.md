
--- 
title:  [Linux] set -x 
tags: []
categories: [] 

---
`set -x`是一个在Unix/Linux shell中使用的命令，用于在执行时显示所有执行的命令及其参数。这个命令通常用于调试脚本，因为它可以让用户看到脚本执行的每一步操作。

当你在shell中执行`set -x`后，之后执行的命令都会被打印到标准错误输出（stderr）。这包括命令本身和命令的扩展结果。这对于理解脚本的执行流程非常有帮助，尤其是当你试图找出脚本中的错误或不期望的行为时。

例如，如果你有一个简单的shell脚本如下：

```
#!/bin/bash

name="World"
echo "Hello, $name!"

```

在脚本中加入`set -x`：

```
#!/bin/bash

set -x
name="World"
echo "Hello, $name!"

```

执行这个脚本时，你将会看到以下输出：

```
+ name=World
+ echo 'Hello, World!'
Hello, World!

```

这显示了脚本中每个命令的执行细节，包括变量的赋值和命令的输出。

除了`set -x`之外，还有其他几个相关的选项，如`set -v`（verbose模式），它在执行前打印每一行命令，但不展开变量和命令替换。

要停止这种调试模式，可以使用`set +x`命令。这将关闭跟踪功能，直到你再次启用它。
