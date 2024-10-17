
--- 
title:  浅谈Python当中Lambda函数的用法 
tags: []
categories: [] 

---
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/ea3fb2ec33bcb761ba940f5a456339dc.jpeg">

今天来给大家推荐一个Python当中超级好用的内置函数，那便是lambda方法，本篇教程大致和大家分享：

 - 什么是lambda函数
 - lambda函数过滤列表元素
 - lambda函数和map()方法的联用
 - lambda函数和apply()方法的联用
 - 什么时候不适合使用lambda方法

什么是Lambda函数

在Python当中，我们经常使用lambda关键字来声明一个匿名函数，所谓地匿名函数，通俗地来讲就是没有名字的函数，具体的语法格式如下所示：

其中它可以接受任意数量的参数，但是只允许包含一个表达式，而该表达式的运算结果就是函数的返回值，我们可以简单地来写一个例子：

output：

过滤列表中的元素

那么我们如何来过滤列表当中的元素呢？这里就需要将lambda函数和filter()方法联合起来使用了，而filter()方法的语法格式：

 - function -- 判断函数
 - iterable -- 可迭代对象，列表或者是字典

其中我们有这么一个列表：
