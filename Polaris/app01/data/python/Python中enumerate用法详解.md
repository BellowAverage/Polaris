
--- 
title:  Python中enumerate用法详解 
tags: []
categories: [] 

---
enumerate()是python的内置函数、适用于python2.x和python3.x enumerate在字典上是枚举、列举的意思 enumerate参数为可遍历/可迭代的对象(如列表、字符串) enumerate多用于在for循环中得到计数，利用它可以同时获得索引和值，即需要index和value值的时候可以使用enumerate enumerate()返回的是一个enumerate对象  

>  
 s = [1, 2, 3, 4, 5] e = enumerate(s) print(e)   输出结果： &lt;enumerate object at 0x000001631F79A828&gt; 


 enumerate的使用： 例如：已知s = [1,2,3,4,5,6]，要求输出: 0,1 1,2 2,3 3,4 4,5 5,6

>  
 s = [1, 2, 3, 4, 5] e = enumerate(s) for index, value in e:     print('%s, %s' % (index, value))   输出结果： 0, 1 1, 2 2, 3 3, 4 4, 5 


>  
  s = [1, 2, 3, 4, 5] # 从指定索引1开始 for index, value in enumerate(s, 1):     print('%s, %s' % (index, value))   输出结果： 1, 1 2, 2 3, 3 4, 4 5, 5 


>  
  s = [1, 2, 3, 4, 5] # 从指定索引3开始 for index, value in enumerate(s, 3):     print('%s, %s' % (index, value))   输出结果： 3, 1 4, 2 5, 3 6, 4 7, 5 


 补充： 如果要统计文件的行数，可以这样写：

>  
 count = len(open(filepath, 'r').readlines()) 


这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。

可以利用enumerate()：

>  
 count = 0 for index, line in enumerate(open(filepath,'r'))：     count += 1 

