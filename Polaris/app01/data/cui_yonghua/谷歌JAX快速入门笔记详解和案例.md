
--- 
title:  谷歌JAX快速入门笔记详解和案例 
tags: []
categories: [] 

---
附：推荐一本新书：，写的比较好，这里是微信公众号链接：

### 一. 什么是JAX?

JAX最初由谷歌大脑团队的 Matt Johnson、Roy Frostig、Dougal Maclaurin 和 Chris Leary 等人发起，借助 Autograd 的更新版本，并且结合了 XLA，可对 Python 程序与 NumPy 运算执行自动微分，支持循环、分支、递归、闭包函数求导，也可以求三阶导数；依赖于 XLA，JAX 可以在 GPU 和 TPU 上编译和运行 NumPy 程序；通过 grad，可以支持自动模式反向传播和正向传播，且二者可以任意组合成任何顺序。

JAX并非是一个深度学习的框架或者库，它的设计目标也并非是作为一个新的深度学习框架。

简单来说，JAX是一个包含可组合函数变换的数值计算库，只不过深度学习恰好是JAX能做的一项工作。

JAX处于函数变换（function transformations）和科学计算的交界处，所以也有能力训练神经网络模型，但不止于训练。

目前JAX在Github上已经斩获了超2万多颗star： <img src="https://img-blog.csdnimg.cn/2ba4c477701f46cebc75ba084c715e89.png" alt="在这里插入图片描述">

github地址：（截至目前，star数：20.3k）

官方文档：

JAX 是一个非常有前途的项目，并且用户一直在稳步增长。JAX 已经在深度学习、机器人 / 控制系统、贝叶斯方法和科学模拟等诸多领域得到了广泛应用。

### 二. 为什么应该使用JAX

JAX目前已经达到深度学习的最高水平。在当前开源的框架中，没有哪一个框架能在`简洁、易用、速度`这3个方面有两个能同时超过JAX。

 - `简洁`：JAX的设计追求最少的封装，尽量避免重复造轮子。设计遵循`tensor→variable(autograd)→module` 3个由低到高的层次，分别代表高维数组（张量），自动求导（变量）和神经网络（层/模块），而且这3个抽象直接连接紧密，可以同时进行修改和操作。而tensorflow充斥着graph、operation、tensor、layer等全新的概念。**JAX源码只有 tensorflow 的十分之一左右**，更少的抽象、更直观的设
