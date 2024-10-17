
--- 
title:  使用pypy来提升你的python项目性能 
tags: []
categories: [] 

---
## 一、PyPy介绍

PyPy是用Python实现的Python解释器的动态编译器，是Armin Rigo开发的产品，能够提升我们python项目的运行速度。PyPy 是利用即时编译的 Python 的替代实现。背后的原理是 PyPy 开始时就像一个解释器，直接从源文件运行我们的 Python 代码。但是，PyPy 不是逐行运行代码，而是在执行它们之前将部分代码编译为机器代码。

根据的介绍可以看到，平均下来PyPy比CPython（也就是我们主流使用的python）快4.5倍：

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9571ca0c1bc379f4cbb293e17094047d.webp?x-oss-process=image/format,png">

**PyPy除了速度快外，还有下面一些特点:**

 1. 内存使用情况比cpython少
 1. gc策略更优化
 1. Stackless 协程模式默认支持，支持高并发
 1. 兼容性好，高度兼容cpython实现，基本可以无缝切换
 1. PyPy为许多平台和操作系统提供预编译的二进制文件：


