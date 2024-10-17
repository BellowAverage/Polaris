
--- 
title:  Python3.11正式版来了 
tags: []
categories: [] 

---
>  
  原文：https://realpython.com/python311-new-features 
 

终于，Python 3.11 正式版发布了！

<img src="https://img-blog.csdnimg.cn/img_convert/20cd6a34369f2f7c5017480660a738dd.jpeg" alt="20cd6a34369f2f7c5017480660a738dd.jpeg">

2020 年 1 月 1 日，Python 官方结束了对 Python 2 的维护，这意味着 Python 2 已完全退休，进入了 Python 3 时代。打从进入 3 版本以来，Python 官方已经发布了众多修改分支，现在来到了最新的版本 Python 3.11。

其实研究界有个不公开的秘密，那就是 Python 运行速度并不快但容易上手，因此使用人数超级多，在众多最受欢迎语言榜单中 Python 多次位列第一。很多开发者都期待这门语言的性能有所提升，还有人畅想 Python 4 会不会在某个不经意的时刻到来，有这种想法的人可以放一放了，Python 之父 Van Rossum 都说了，Python 4.0 可能不会来了。

Van Rossum 曾表示：「我和 Python 核心开发团队的成员对 Python 4.0 没什么想法，提不起兴趣，估计至少会一直编号到 3.33。Python 的加速是渐进式的，3.11 版本会有新的速度提升，预计会比 3.10 快得多。」

正如 Van Rossum 所说，根据官方资料显示最新发布的 Python 3.11 比 Python 3.10 快 10-60%，对用户更友好。这一版本历经 17 个月的开发，现在公开可用。

Python 3.11 的具体改进主要表现在：更详实的 Error Tracebacks、更快的代码执行、更好的异步任务语法、改进类型变量、支持 TOML 配置解析以及一些其他非常酷的功能（包括快速启动、Zero-Cost 异常处理、异常组等）。

<img src="https://img-blog.csdnimg.cn/img_convert/f54845cdf14bb1b850ede8cd872dc536.jpeg" alt="f54845cdf14bb1b850ede8cd872dc536.jpeg">

Python 指导委员会成员和核心开发者、Python3.10/3.11 发布管理者 Pablo Galindo Salgado 表示，为了使 3.11 成为最好的 Python 版本，我们付出了很多努力。

<img src="https://img-blog.csdnimg.cn/img_convert/aa97ce8ab339ae5d01e8464623c0fb0f.jpeg" alt="aa97ce8ab339ae5d01e8464623c0fb0f.jpeg">

**Python 3.11 新特性**

**Error Tracebacks**

Python 这门编程语言对初学者非常友好，它具有易于理解的语法和强大的数据结构。但对于刚刚接触 Python 的人来说却存在一个难题，即如何解释当 Python 遇到错误时显示的 traceback。

Python 3.11 将 Decorative annotation 添加到 tracebacks 中，以帮助用户更快地解释错误消息。想要获得这种功能，可以将以下代码添加到 inverse.py 文件中。

<img src="https://img-blog.csdnimg.cn/img_convert/6603310a346dc8f00aee718669f51fd2.png" alt="6603310a346dc8f00aee718669f51fd2.png">

举例来说，你可以使用 inverse() 来计算一个数的倒数。因为 0 没有倒数，所以在运行下列代码时会抛出一个错误。

<img src="https://img-blog.csdnimg.cn/img_convert/4e990ed14e4a67e5d92e45e9400abce0.png" alt="4e990ed14e4a67e5d92e45e9400abce0.png">

注意嵌入在 traceback 中的 ^ 和~ 符号，它们指向导致错误的代码。与此前的 tracebacks 一样，你应该从底层开始，然后逐步向上。这种操作对发现错误非常有用，但如果代码过于复杂，带注释的 tracebacks 会更好。

**更快的代码执行**

Python 以速度慢著称，例如在 Python 中，常规循环比 C 中的类似循环慢几个数量级。

Python 官方正在着手改进这一缺陷。2020 年秋，Mark Shannon 提出了关于 Python 的几个性能改进。这个提议被称为香农计划 (Shannon Plan)，他们希望通过几个版本的更新将 Python 的速度提高 5 倍。不久之后微软正式加入该计划，该公司正在支持包括 Mark Shannon、Guido van Rossum 在内的开发人员，致力于「Faster CPython」项目的研究。

「Faster CPython」项目中的一个重要提案是 PEP 659，在此基础上，Python 3.11 有了许多改进。

PEP 659 描述了一种「specializing adaptive interpreter」。主要思想是通过优化经常执行的操作来加快代码运行速度， 这类似于 JIT（just-in-time）编译。只是它不影响编译，相反，Python 的字节码是动态调整或可更改的。

<img src="https://img-blog.csdnimg.cn/img_convert/84e5ec91ce7af0e2d49f1ce4631f6541.png" alt="84e5ec91ce7af0e2d49f1ce4631f6541.png">

研究人员在字节码生成中添加了一个名为「quickening」的新步骤，从而可以在运行时优化指令，并将它们替换为 adaptive 指令。

一旦函数被调用了一定次数，quickening 指令就会启动。在 CPython 3.11 中，八次调用之后就会启动 quickening。你可以通过调用 dis() 并设置 adaptive 参数来观察解释器如何适应字节码。

在基准测试中，CPython 3.11 比 CPython 3.10 平均快 25%。Faster CPython 项目是一个正在进行的项目，已经有几个优化计划在 2023 年 10 月与 Python 3.12 一起发布。你可以在 GitHub 上关注该项目。

项目地址：https://github.com/faster-cpython/ideas

**更好的异步任务语法**

Python 中对异步编程的支持已经发展了很长时间。Python 2 时代添加了生成器，asyncio 库最初是在 Python 3.4 中添加的，而 async 和 await 关键字是在 Python 3.5 中添加的。在 Python 3.11 中，你可以使用任务组（task groups），它为运行和监视异步任务提供了更简洁的语法。

**改进的类型变量**

Python 是一种动态类型语言，但它通过可选的类型提示支持静态类型。Python 静态类型系统的基础在 2015 年的 PEP 484 中定义。自 Python 3.5 以来，每个 Python 版本都引入了几个与类型相关的新提案。

Python 3.11 发布了 5 个与类型相关的 PEP，创下新高：
- PEP 646: 可变泛型- PEP 655: 根据需要或可能丢失的情况标记单个 TypedDict 项- PEP 673: Self 类型- PEP 675: 任意文字字符串类型- PEP 681: 数据类转换
**支持 TOML 配置解析**

TOML 是 Tom's Obvious Minimal Language 的缩写。这是一种在过去十年中流行起来的配置文件格式。在为包和项目指定元数据时，Python 社区已将 TOML 作为首选格式。

虽然 TOML 已被使用多年，但 Python 并没有内置的 TOML 支持。当 tomllib 添加到标准库时，Python 3.11 中的情况发生了变化。这个新模块建立在 toml 第三方库之上，允许解析 TOML 文件。

以下是名为 units.toml 的 TOML 文件示例：

<img src="https://img-blog.csdnimg.cn/img_convert/479a1d939200152e3946fe2b5209f8ee.png" alt="479a1d939200152e3946fe2b5209f8ee.png">

**其他功能**

除了以上主要更新和改进之外，Python 3.11 还有更多值得探索的功能，比如更快的程序启动速度、对异常的更多改变以及对字符串格式的小幅改进。

**更快的程序启动速度**

Faster CPython 项目的一大成果是实现了更快的启动时间。当你运行 Python 脚本时，解释器初始化需要一些操作。这就导致即便是最简单的程序也需要几毫秒才能运行。

<img src="https://img-blog.csdnimg.cn/img_convert/5fd08445dd0521b0ef06dc2f480012e9.png" alt="5fd08445dd0521b0ef06dc2f480012e9.png">

在很多情况下，与运行代码所需时间相比，启动程序需要的时间可以忽略不计。但是在运行时间较短的脚本中，如典型的命令行应用程序，启动时间可能会显著影响程序性能。比如考虑如下脚本，它受到了经典 cowsay 程序的启发。

<img src="https://img-blog.csdnimg.cn/img_convert/b3c0879437b552851b0a5a0e3985f914.png" alt="b3c0879437b552851b0a5a0e3985f914.png">

在 snakesay.py 中，你从命令行读取一条消息，然后将这条消息打印在带有一条可爱蛇的对话气泡中。你可以让蛇说任何话。这是命令行应用程序的基本示例，它运行得很快，但仍需要几毫秒。这一开销的很大部分发生在 Python 导入模块时。

<img src="https://img-blog.csdnimg.cn/img_convert/85c2cb4a5b3ca4e7139e959f56668ea3.png" alt="85c2cb4a5b3ca4e7139e959f56668ea3.png">

你可以使用 - X importtime 选项来显示导入模块所用的时间。表中的数字为微秒为单位，最后一列是模块名称的格式。

<img src="https://img-blog.csdnimg.cn/img_convert/5eb5dc0537b9f324ce6256b4d5f4f579.png" alt="5eb5dc0537b9f324ce6256b4d5f4f579.png">

该示例分别运行在 Python 3.11 和 3.10 上，结果如下图所示，Python 3.11 的导入速度更快，有助于 Python 程序更快地启动。

<img src="https://img-blog.csdnimg.cn/img_convert/6ed4d0d6b8636bf7f831ede3a2b59530.png" alt="6ed4d0d6b8636bf7f831ede3a2b59530.png">

**零成本异常**

异常的内部表示在 Python 3.11 中有所不同。异常对象更轻量级，并且异常处理发生了变化。因此只要不触发 except 字句，try … except 块中的开销就越小。

所谓的零成本异常受到了 C++ 和 Java 等其他语言的启发。当你的源代码被编译为字节码时，编译器创建跳转表，由此来实现零成本异常。如果引发异常，查询这些跳转表。如果没有异常，则 try 块中的代码没有运行时开销。

**异常组**

此前，你了解到了任务组以及它们如何同时处理多个错误。这都要归功于一个被称为异常组的新功能。

我们可以这样考虑异常组，它们是包装了其他几种常规异常的常规异常。虽然异常组在很多方面表现得像常规异常，但它们也支持特殊语法，帮助你有效地处理每个包装异常。如下所示，你可以通过给出一个描述并列出包装的异常来创建一个异常组。

<img src="https://img-blog.csdnimg.cn/img_convert/c37072d4915c2d7f4ee6b614389e8c24.png" alt="c37072d4915c2d7f4ee6b614389e8c24.png">

**异常 Notes**

常规异常具有添加任意 notes 的扩展能力。你可以使用. add_note() 向任何异常添加一个 note，并通过检查.__notes__属性来查看现有 notes。

<img src="https://img-blog.csdnimg.cn/img_convert/ca6c01ced2d26e348188239b5f52b27a.png" alt="ca6c01ced2d26e348188239b5f52b27a.png">

**负零格式化**

使用浮点数进行计算时可能会遇到一个奇怪概念——负零。你可以观察到负零和 regular zero 在 REPL 中呈现不同，如下所示。

<img src="https://img-blog.csdnimg.cn/img_convert/af07295fd0ced82c46d707db58f0f12e.png" alt="af07295fd0ced82c46d707db58f0f12e.png">

更多关于 Python 3.11 的更新细节请参阅原文档。

**往期推荐**
- - - 