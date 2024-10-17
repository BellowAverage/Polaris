
--- 
title:  Shell编程基础（1） - Shell简介 
tags: []
categories: [] 

---
## Shell编程基础（1） - Shell简介

#### Shell Scripting Essentials – Brief Introduction of Shell

>  
 一个Shell 脚本，就是写在文件里的一系列命令；它由运行的计算机程序中的 Unix Shell（命令行解释器）运行。 


Shell 脚本通常具有描述步骤的注释。Shell 脚本执行的不同操作是程序执行、文件操作和文本打印。包装器也是一种 shell 脚本，用于创建程序环境、运行程序等。

#### 1. Shell的种类

Unix 中有两种主要类型的 Shell。这些是：

##### 1) Bourne Shell

这是版本 7 Unix 的默认 shell。字符 $ 是 bourne shell 的默认提示。这个 shell 中的不同子类别是 Korn shell、Bourne Again shell、POSIX shell 等。

##### 2) C Shell

这是一个 Unix shell 和一个在文本窗口中运行的命令处理器。字符 % 是 C shell 的默认提示符。文件命令也可以通过 C shell（称为脚本）轻松读取。

#### 2. Shell 脚本的功能

Shell脚本的代表功能有以下几种：

##### 1) 批处理作业

在命令行界面中手动输入的几个命令可以使用 shell 脚本自动执行。这可以在用户不需要单独触发每个独立命令的情况下完成。

##### 2) 编程

现代 shell 脚本中有许多功能只有在复杂的编程语言中才能找到，例如数组、变量、注释等。许多复杂的应用程序都可以使用这些功能在 shell 脚本中编写。但是有一个问题，即 shell 脚本语言不支持类、线程等。

##### 3) 泛化

在Shell脚本中比使用循环、变量等用于多个任务要灵活得多。这方面的一个例子是称为 bash 的 Unix shell 脚本，它将 jpg 图像转换为 png 图像。

##### 4) 快捷方式

Shell 脚本为系统命令提供了一个快捷方式，其中应用了命令选项、环境设置或后处理应用。这仍然允许快捷脚本充当 Unix 命令。

#### 3. Shell 脚本的优点

Shell脚本的一些优点是： Shell 脚本的命令和语法与在命令行中输入的命令和语法相同。因此，无需切换到完全不同的语法。 用 shell 脚本编写代码比用其他编程语言编写代码要快得多。这也意味着程序更容易创建，并且可以轻松选择所需的文件。

Shell 脚本还可用于为现有程序提供链接。

非专家用户可以使用 Shell 脚本来根据他们的要求修改和定制其程序的行为。

#### 4.Shell脚本的缺点

Shell脚本的一些缺点是:
1. Shell 脚本中可能存在错误，这些错误被证明可能代价颇大；1. Shell 脚本中的程序在执行时非常慢，由于执行的每个 Shell 命令都需要一个新进程;1. Shell 脚本中的不同平台也可能存在兼容性问题。
#### 5. Shell脚本头

Shell脚本也用 shebang 标识。Shebang 是 bash # 和 bang 的组合！

遵循 Bash shell 路径。这是脚本的第一行。

Shebang 告诉 shell 通过 Bash Shell 来执行它。Shebang 只是通往 bash 解释器的绝对路径。下面是 shebang 语句的示例。

```
#！/bin/bash

```

Bash 程序的路径可能会有所不同。我们稍后将看到如何识别它。

##### 7. Shell 脚本示例

为此示例创建了一个脚本 app.sh。脚本和命令如下：

```
#！/bin/bash
gzip 
.zip
find
echo

```

gzip 是用于创建、提取或查看 .gz 文件的命令， zip 是用于创建或提取 zip 文件的命令， find 是一个有助于搜索文件的命令， echo 是一个显示一行文本的命令

本文简要小结了Bash Shell的特点（包含优点、缺点），脚本结果及示例。后续还有其它Shell编程的技术文档，敬请关注。

喜欢就点赞哈。😃
