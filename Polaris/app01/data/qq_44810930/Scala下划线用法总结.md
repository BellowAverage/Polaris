
--- 
title:  Scala下划线用法总结 
tags: []
categories: [] 

---
Scala是一门以java虚拟机（JVM）为运行环境并将面向对象和函数式编程的最佳特性结合在一起的静态类型编程语言。scala 单作为一门语言来看， 非常的简洁高效，在Scala中存在很多让代码更加简洁的语法，下划线“_”便是其中一个。下划线的普遍用法总结如下：
1. 用于变量初始化
在Java中，可以声明变量而不必给出初始值，在Scala中，变量在声明时必须显示指定，可以使用下划线对变量进行初始化。而且该语法只适用于成员变量，不适用于局部变量。例：

<img src="https://img-blog.csdnimg.cn/direct/61290dde8f27461fa86075b085425ef6.png" alt="在这里插入图片描述">
1. 用于导包引入
导包引入时使用_导入该包下所有内容，类比Java中的*。例如： <img src="https://img-blog.csdnimg.cn/direct/a7608a8aaafc4548a77ed6b2a142349d.png" alt="在这里插入图片描述"> 3.用于将方法转变为函数

在Scala中方法不是值，而函数是。所以一个方法不能赋值给一个val变量，而函数可以。方法可以转换为函数赋值给变量，例： <img src="https://img-blog.csdnimg.cn/direct/574da829a90f4251bfc71b4f9a79058e.png" alt="在这里插入图片描述">
1. 用于模式匹配
模式匹配中可以用下划线来作为Java中default的类比使用，也可以在匹配集合类型时，用于代表集合中元素，例：

<img src="https://img-blog.csdnimg.cn/direct/8f69b77b8f194ba5aee92a6f1b5a5ea9.png" alt="在这里插入图片描述"> 5. 用于访问tuple元素

例： <img src="https://img-blog.csdnimg.cn/direct/b52eab3499194d63ae5f829b7a2be646.png" alt="在这里插入图片描述"> 6. 用于简写函数

如果函数的参数在函数体只出现一次，则可以用下划线代替。

<img src="https://img-blog.csdnimg.cn/direct/b6005f71318e4b5bbe216f9c1b8f4fc4.png" alt="在这里插入图片描述">
1. 定义偏函数
对某个多参数函数进行部分函数调用，没有传入的参数使用_代替，返回结果即为偏函数。例：

<img src="https://img-blog.csdnimg.cn/direct/0ebe41110f0a4f839580db1e8807fd10.png" alt="在这里插入图片描述">
