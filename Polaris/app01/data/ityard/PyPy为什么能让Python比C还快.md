
--- 
title:  PyPy为什么能让Python比C还快 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/3d7739909874772a0d3fad55d5821fac.png">

转自：机器之心，编辑：杜伟、陈萍

Python 之父 Guido van Rossum曾经说过：**如果想让代码运行得更快，应该使用 PyPy。**

对于研究人员来说，迅速把想法代码化并查看其是否行得通至关重要。Python 是能够实现这一目标的出色语言，它能够让人们专注于想法本身，而不必过度为代码格式等无聊的事情困扰。

但是，Python 有一个致命的缺点：**速度比 C、C ++ 等语言慢很多。**那么，构建一个 Python 原型测试想法之后，如何将其转变为快速且高性能的工具？通常来说，人们还要再进行一步工作：将 Python 代码手动转换为 C 语言的代码。但如果 Python 原型本身就可以运行得很快，那么转换代码的时间就可以做一些更有意义的事情。

而 PyPy，恰好可以解决这一问题。它能够让 Python 代码运行得比 C 还快。

```

import timefrom termcolor import colored
start = time.time()number = 0for i in range(100000000):    number += i    print(colored("FINISHED", "green"))print(f"Ellapsed time: {time.time() - start} s")

```

为了证明 PyPy 的速度，使用默认的 Python 解释器和 PyPy 运行上述代码，执行一个从整数 0 加到 100,000,000 的循环, 然后打印出运行时间。运行结果如下：

<img src="https://img-blog.csdnimg.cn/img_convert/6e730b49bc6dd8338447baaba4677d58.gif">

运行时间 Python vs PyPy

这不是学术意义上的评估，但该结果是令人惊叹的。与大约需要 10 秒钟的默认 Python 解释器相比，PyPy 仅用 0.22 秒就完成了执行。而且无需进行任何更改就可以直接将 Python 代码放到 PyPy 上。而同一台计算机上，等效的 C 语言实现需要 0.32 秒，PyPy 甚至击败了最快的 C 语言。

**为什么 PyPy 这么快？**

尽管代码完全相同，但代码的执行方式却大不相同。PyPy 提升速度的秘诀是「**即时编译（ just-in-time compilation）**」，即** JIT 编译**。

提前编译 

C、C ++、Swift、Haskell、Rust 等编程语言通常是提前编译（AOT 编译）的。这意味着用这些语言编写代码之后，编译器会将源代码转换成特定计算机架构可读的机器码。也就是说在执行程序时，执行的并不是原始源代码，而是机器码。

<img src="https://img-blog.csdnimg.cn/img_convert/5bedcdbe382cf3477161c8ff13e19541.png">

提前编译把源代码转化为机器代码

解释语言 

与 C 语言等上述语言不同，Python、JavaScript、PHP 等语言采用另一种方法——解释语言。与将源代码转换为机器码相比，解释的过程中源代码是保持不变的。每次运行程序时，解释器都会逐行查看代码并运行。例如，每个 Web 浏览器都内置了 JavaScript 解释器。

<img src="https://img-blog.csdnimg.cn/img_convert/e6782e2a8b5c271b629b57b05b5eaf4f.png">

解释器逐行运行程序

即时编译

PyPy 是利用即时编译来执行 Python 代码的。即 PyPy 不同于解释器，它并不会逐行运行代码，而是在执行程序前先将部分代码编译成机器码。

<img src="https://img-blog.csdnimg.cn/img_convert/18522e12c2c5188a4c9b5e04a2837214.png">

JIT 编译综合了提前编译和解释

如上图所示，而 **PyPy 使用的 JIT 编译是解释和提前编译的结合，可以利用提前编译来提高性能，并提高解释型语言的灵活性和跨平台可用性。**

这也就是为什么PyPy可以让Python有这么快的执行速度了。目前，大部分的使用者还保持使用着默认的Python编译器，如果对速度有要求不妨可以试试PyPy编译器<img src="https://img-blog.csdnimg.cn/img_convert/abb2b7eea9cba9e627f9c6720301f88a.png">

原文链接：https://towardsdatascience.com/run-your-python-code-as-fast-as-c-4ae49935a826

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/f8a72199276b6dbdce3e7f371c3aba21.gif">

微信扫码关注，了解更多内容
