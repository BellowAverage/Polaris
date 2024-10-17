
--- 
title:  Python中的——random模块 
tags: []
categories: [] 

---
Python中的random模块用于生成。下面介绍一下random模块中最常用的几个函数。

### random.random

random.random()用于生成一个0到1的随机符点数: 0 &lt;= n &lt; 1.0

### random.uniform

random.uniform的函数原型为：random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a &gt; b，则生成的随机数n: a &lt;= n &lt;= b。如果 a &lt;b， 则 b &lt;= n &lt;= a。

print random.uniform(10, 20)   print random.uniform(20, 10)   #---- 结果（不同机器上的结果不一样）   #18.7356606526   #12.5798298022   print random.uniform(10, 20) print random.uniform(20, 10) #---- 结果（不同机器上的结果不一样） #18.7356606526 #12.5798298022

## **random.randint**

 　　random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数
