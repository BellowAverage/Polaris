
--- 
title:  Python中insert用法详解！ 
tags: []
categories: [] 

---
　　Python中insert用法是什么?这篇文章为大家详细的讲解一下Python中insert用法，并附带实战案例，希望能够给你们带来帮助。

　　描述：

　　insert()函数用于将指定对象插入列表的指定位置。

　　语法：

　　inser()方法语法：

　　list.insert(index, obj)

　　参数：

　　index -- 对象obj需要插入的索引位置。

　　obj -- 要插入列表中的对象。

　　返回值：

　　该方法没有返回值，但会在列表指定位置插入对象。

　　实例

　　以下实例展示了insert()函数的使用方法：

　　#!/usr/bin/python

　　aList = [123, 'xyz', 'zara', 'abc']

　　aList.insert(3, 2009)

　　print "Final List : ", aList

　　以上实例输出结果如下：

　　Final List : [123, 'xyz', 'zara', 2009, 'abc']
