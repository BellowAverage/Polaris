
--- 
title:  历时五年，Cython3.0终于来了 
tags: []
categories: [] 

---
（点击上方快速关注并设置为星标，一起学Python）

>  
  转自：OSC开源社区（ID：oschina2013) 
 

经过近五年的漫长岁月，Cython 3.0 宣布正式发布。

公告称，“Cython 3.0 在各个方面都优于之前的任何其他 Cython 版本。它更加 Python 化，与 C 和 C++ 集成得更好，支持更多 Python 实现和配置，提供了许多很棒的新语言特性。更快、更安全、更易用。It's simply better。”

<img src="https://img-blog.csdnimg.cn/img_convert/c7e73a5bb482dae280bb738c9f74d571.png" alt="c7e73a5bb482dae280bb738c9f74d571.png">

新的语言特性包括：
- Python 3 默认语法和语义- 纯 Python 代码中的 Cython 类型注释- 自动 NumPy ufunc 生成- 快速 @dataclass 和 @total_ordering 扩展类型- 默认情况下 C 函数中的安全异常传播- Cython 代码中的 Unicode 标识符
Cython 3 在许多方面对 Cython 进行了清理和现代化。它放弃了对早已过时的 Python 2 的支持，增加了对较新的 Python 功能（最高可达 Python 3.12）的支持，并扩展了纯 Python 模式（pure python）的使用。“简而言之，这允许将更广泛的 Python 代码编译为优化的 C 代码。”

根据介绍，纯 Python 模式允许 Python 开发人员在 Cython 上使用现有的 Python linting 和代码分析工具。一直以来，Cython 都在使用自己独特的语法，即 Python 语法和 C 类型声明语法的混合体，这使得 Cython 很难使用 Python 工具进行故障排除。随着时间的推移，Cython 开始提供一种与传统 Python 语法完全兼容的替代语法，称为纯 Python 模式。绝大多数 Cython 函数现在都以纯 Python 模式显示，包括调用外部 C 库的函数。

另一个主要改进是 NumPy 支持。Cython 3 增加了直接在 Cython 中编写 NumPy ufuncs 的功能，以便可以快速轻松地将用 Cython 编写的简单数值函数应用于 NumPy 数据结构的全部内容。

Cython 的内部结构也进行了重新设计，以更好地配合 Python 内部结构的不断变化。例如，Python 的新 "limited API" 公开了 Python API 的一个有保证的稳定子集，专门用于 Cython 经常 hook Python 解释器的工作类型。Cython 3 已初步支持 limited API，且这种支持还在不断增加。InfoWorld 指出，从长远来看，这意味着为某一版本 Python 构建的 Cython 扩展模块可以在未来版本的 Python 中运行，而无需重新编译。

更多详情可查看官方公告：https://cython.readthedocs.io/en/latest/src/changes.html
- - - - - 