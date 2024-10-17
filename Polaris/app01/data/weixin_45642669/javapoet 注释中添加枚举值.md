
--- 
title:  javapoet 注释中添加枚举值 
tags: []
categories: [] 

---
## 问题描述

使用javapoet生成源代码

为了实现这么一个目的<img src="https://img-blog.csdnimg.cn/56121a0874d649de8c17a606f90b4555.png" alt="在这里插入图片描述">

## 解决

翻了一下源代码，他的实现如下： <img src="https://img-blog.csdnimg.cn/7e64c8995a4849dc9c05d777b5e65e10.png" alt="在这里插入图片描述"> 这个方法是私有的，暂时不确定如何调用

照着这个方法，即可实现大多数类型的基本调用

<img src="https://img-blog.csdnimg.cn/228de39693dd40c6ad934803bc17f6d6.png" alt="在这里插入图片描述"> 即可实现上图需要的效果
