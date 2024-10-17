
--- 
title:  终于来了！！Pyston v2.0 发布，解决 Python 慢速的救星 
tags: []
categories: [] 

---
>  
 给大家推荐本书《PyCharm中文指南》，把各种 PyCharm 的高效的使用技巧用GIF动态图的形式展示出来。有兴趣的可以看它的在线文档： 


Pyston 自从 2017 年发布 0.6.1 版本后，已经淡出了人们的视线三年多了，导致现在新人都很少听过它的大名。

前两天（2020年10月28日）Pyston 在官方博客上（ v2 版本。

Pyston 是 Python 的基于 JIT 另一种实现，更快且高度兼容 CPython，和另一个被寄予厚望的 pypy 相比，Pyston 背后有 DropBox 的资金支持，发展会比 PyPy 更快。

### 速度更快

在基准测试中，Pyston v2 比 Python 3.8 快了 20%

下面是官方发布的性能测试结果：

<img src="https://img-blog.csdnimg.cn/20201102122507832.png" alt="">

### 兼容性

CPython 到现在能这么流行，从来都不是靠速度取胜。

Python 丰富的生态，大量好用的第三方库和应用，让大部分开发者允许它在速度上的不足。

有了 Pyston 后，速度和生态，二者就皆可兼得。

Pyston 和 PyPy的一个巨大区别就是它们的向后兼容性，由于Pyston是CPython的分支，因此我们认为它是当今可用的最兼容的替代Python实现之一。它支持与 CPython 相同的所有功能和C API。

### 如何看待

Pyston的发展一直都很快，实现了JIT编译的Python，而Dropbox则充分利用这一点来提高性能。根据Dropbox的标准，Pyston不仅运行速度更快，启动速度也更快。启动速度慢一直是所有动态语言JIT编译器的通病，但是Pyston通过使用内联缓存和不同的JIT技术克服了这个问题。

在这些方面PyPy也卓有成就，在最近的版本中，减少了脚本启动的时间，增加了对硬件类型和处理器的支持。多平台支持也是PyPy的一大卖点（通过Python的子集实现），让跨平台变得简单。PyPy在它的生态系统中还有很多有价值的工具：比如Python Debugger，可以向前和向后查看程序的状态。

从长期来看，Python用户有了更多的选择：PyPy注重未来的生态，Pyston则强调兼容性。

### 如何试用

从 github 仓库（ Pyston v2.0 仅提供了 适用于 Ubuntu 18.04 和 20.04 x86_64 的 deb 包。

你可以通过如下命令去下载安装

```
# 下载
$ wget https://github.com/pyston/pyston/releases/download/v2.0/pyston_2.0_amd64_18.04.deb

# 安装
$ sudo apt install ./pyston_2.0*.deb
```

然后你就可以使用 `pyston` (或者 `pyston3`) 和 `pip-pyston install`(或者 `pip-pyston3 install`) 命令来使用 pyston。

还在等什么，快去试用一下吧！！
