
--- 
title:  11 个 Python 教程来炫耀你的高级技能 
tags: []
categories: [] 

---
如果你可以以 Python 式的方式使用 Python，那么 Python 是一种优雅的语言。

但不管你有多资深，真正用 Python 写代码都需要一些时间。

本文将向你分享 11 个 Pythonic 技巧，让你的 Python 技能提升到一个新水平。

现在，我们就一起来看这些代码。

### 1、Python中的解构赋值

给变量赋值是编程的基本操作，Python 有一些语法糖来使过程更加优雅。 让我们看一个简单的例子：

```
a, *mid, b = [1, 2, 3, 4, 5, 6]
print(a, mid, b)
# 1 [2, 3, 4, 5] 6

```

如上所示，在一个星号的帮助下，mid 变量将中间的项目作为列表接收。

### 2、使用 Zip 函数聚合项目

Python 有一个惊人的内置函数，叫做 zip。顾名思义，zip 函数聚合来自不同迭代的项目，例如列表、元组或集合，并返回一个迭代器。

```
id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
sex = ['male', 'male', 'male', 'male']
record = zip(id, leaders, sex)

print(list(record))
# [(1, 'Elon Mask', 'male'), (2, 'Tim Cook', 'male'), (3, 'Bill Gates', 'male'), (4, 'Yang Zhou', 'male')]

```

### 3、在 Python 中正确使用 Lambda 函数

如果你喜欢单线，Lambda 函数是你的朋友，让我们在这里看一个经典的问题：

给你一个清单如下，你能把里面所有的奇数都打印出来吗？

很简单的，你只需要一行代码：

```
print(list(filter(lambda x: x % 2 == 1, numbers)))
# [1, 37, 43, 51, 83, 43]

```

### 4、使用下划线忽略变量

有时，一个变量是无用的，你不必费心给它起名字，你可以用下划线忽略它。

```
&gt;&gt;&gt; L = [1,3,5,7]
&gt;&gt;&gt; a, _, b, _ = L
&gt;&gt;&gt; print(a, b)
1 5

```

### 5、利用列表理解的力量

同样，如果你是 Python 单行代码的粉丝，列表理解是你必须知道的，它具有将多个操作转换为一行代码的能力：

```
Genius = ["Jerry", "Jack", "tom", "yang"]
L1 = [name if name.startswith('y') else 'Not Genius' for name in Genius]
print(L1)
# ['Not Genius', 'Not Genius', 'Not Genius', 'yang']

```

### 6、放置一个占位符

有时，你需要定义一个函数但尚未弄清楚如何实现它，你可以在其中放置一个占位符：

```
def my_func():
    pass

```

或者更可爱的方式：🙂

```
def my_func():
    ...

```

### 7、通过正则表达式处理文本

正则表达式 (regex) 是处理字符/字符串的强大工具，Python 内置的 re 模块提供了正则表达式的所有功能：

```
import re
txt = "Yang is so handsome!!!"
x = re.search("Elon", txt)
print(x)
#None

```

### 8、Python 中的 Map 和 Reduce

Python中有两个著名的高阶函数：map()和reduce()。

map()函数接收两个参数，一个是函数，另一个是Iterable，它依次将初始化函数应用于序列的每个元素，并将结果作为新的迭代器返回。

```
names = ['yAnG', 'MASk', 'thoMas', 'LISA']
names = map(str.capitalize, names)
print(list(names))
# ['Yang', 'Mask', 'Thomas', 'Lisa']

```

reduce()方法也有两个参数，一个是函数，另一个是Iterable，它将函数应用于序列，该函数必须接收两个参数，reduce 继续结果并与序列的下一个元素执行累积计算。最后，它返回累积计算的结果。

```
from functools import reduce

city = ['L', 'o', 'n', 'd', 'o', 'n', 2, 0, 2, 0]
city_to_str = reduce(lambda x, y: str(x) + str(y), city)
print(city_to_str)
# London2020

```

### 9、优雅地删除字符串中不必要的空格

这个字符串处理技巧结合了 splits() 和 join() 的强大功能：

```
quote = "   Yang   is a full   stack hacker."
new_quote = ' '.join(quote.split())
print(new_quote)
# Yang is a full stack hacker.

```

### 10、浅拷贝列表的最简单方法

在 Python 中浅拷贝列表的最简单方法是利用列表切片的特性：

```
&gt;&gt;&gt; a = [1, 2, 3, 4, 5, 6]
&gt;&gt;&gt; b = a[:]
&gt;&gt;&gt; b[0]=100
&gt;&gt;&gt; b
[100, 2, 3, 4, 5, 6]
&gt;&gt;&gt; a
[1, 2, 3, 4, 5, 6]

```

### 11. 在解释器中检查最后一个表达式的值

这是 Python Interpreter 的一个有趣的小技巧，我们可以使用一个下划线来简单地获取最后一个表达式的值。

```
&gt;&gt;&gt; 5+6
11
&gt;&gt;&gt; _
11

```

### 关于Python技术储备

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以找到适合自己的学习方案 


包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习等习教程。带你从零基础系统性的学好Python！

## 零基础Python学习资源介绍

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。**（全套教程文末领取哈）** <img src="https://img-blog.csdnimg.cn/img_convert/673b13641cf2ddf5e18b5c58afd50200.png#pic_center" alt="">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">
