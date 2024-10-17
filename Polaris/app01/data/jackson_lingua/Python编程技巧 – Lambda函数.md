
--- 
title:  Python编程技巧 – Lambda函数 
tags: []
categories: [] 

---
## Python编程技巧 – Lambda函数

### Python Programming Skills – Lambda Functions

By Jackson@ML 2023-11-25

>  
 在前文介绍过Python函数，一个函数用def关键字声明，不带或带有参数，并以冒号结束；函数块根据结果由解释器确定返回值动态类型。 


为了引入lambda函数，先看下面代码，编写函数add(x, y) 进行两个数的加法运算并打印输出：

```
def add(x, y):
    return x + y
print("x + y = ", add(10, 3))

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/0512943b7f924e47b3935dc85f67adbb.png" alt="在这里插入图片描述"> 经常这样写函数，会不经意地发现，很多函数都只用一次，并且重复使用的概率很低；同时，每每涉及到函数，都得这么写一遍，体现的效率不是很高。

那么，问题来了：如果仅用一次，或者不经常用，函数该怎么变得简洁呢？ Lambda函数，将为我们解决这个问题。

本文简要介绍lambda函数及其表达式如何应用在计算和相关函数领域，以提高我们的工作效率的案例，希望对开发者和学习者有所帮助。

#### 1. 一个简单的lambda函数

按照上述的传统函数预算法则，如果不需要再次调用它，那么视之为**匿名函数**，就可以使用lambda表达式来实现该函数，如下代码：

```
lmd = lambda x, y: x + y
print(lmd(10, 3))

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/2dddebfe73ff4b45b3a5efe613901a43.png" alt="在这里插入图片描述"> 可以看到，函数本身只有一行语句，其中lambda表达式简明扼要地表达了函数传递了参数x, y, 函数返回值是x + y的和（即10 + 3）。

尽管该函数没有名称，但是它把返回值赋给了变量lmd，并由lmd打印输出结果：13。

#### 2. 为什么使用lambda函数？

假如函数只需要使用一次，并且当您在另一个函数中将它们用作匿名函数时，可以更好地显示 lambda 的强大功能。 比如下方代码，你有一个函数，它接受一个参数传递，并且该参数将与一个未知数字相乘：

```
def myFunction(n):
    return lambda a : a * n
myDoubler = myFunction(2)
print(myDoubler(11))

```

myFunction函数传递了参数n,实际参数值为2（即倍数）；紧接着，myDoubler函数作为变量被赋予了myFunction(2)，并由lambda表达式计算，返回与实际参数11的乘积结果：22. 执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/03b0eda14c21494ca17892193c003c8f.png" alt="在这里插入图片描述"> 同样，如果n = 3, 执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/0b529f7b2c3048599f189c066ffe12ee.png" alt="在这里插入图片描述"> 如果我们想要通过myFunction来打造不同的函数myDoubler, myTripler,从而分别计算输出2倍、3倍于参数的结果，可以变为以下代码：

<img src="https://img-blog.csdnimg.cn/48c4800414034c748554174907dae16c.png" alt="在这里插入图片描述">

#### 3. 小结

通过本文的示例，说明了Python语言提供了高效的lambda函数及其表达式。如果需要只使用一次，或者使代码看起来简洁，那么lambda函数将是一个不错的选择。

当然，普通Python函数的强大功能仍不容忽视，而在敏捷开发过程中，lambda函数在表达匿名函数方面，的确方便可行。

技术好文陆续推出，敬请关注。

喜欢就点赞哈！ 您的认可，我的动力。😊

## 相关阅读：
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 