
--- 
title:  Python编程技巧 – format格式化文本 
tags: []
categories: [] 

---
## Python编程技巧 – format格式化文本

### Python Programming Essentials - Using format() to format texts

By Jackson@ML

本文简要介绍Python语言的format()方法（也即函数）相关实例和技巧，希望对读者有所帮助。

#### 1. format定义和方法

format()方法能够格式化指定的值，并且将它们插入到字符串的占位符中。

##### 1) 示例代码一

了解占位符，让我们先看一个例子。代码如下：

```
a = 10
print("a =", a)

```

通常，为了表达一个公式，或者完整的语义字符串，会将双引号放置到format()方法中。

此外，还有一种情况非常常见，就是利用变量时，需要在双引号中添加占位符(一对大括号{ })。例如下面的代码示例：

```
a = 10
print("a = {}".format(a))

```

这段代码会得出与前述代码同样的结果：

```
a = 10

```

但是，第二段代码明显有着不同的风格，不但更加灵活，也使变量运用游刃有余。由此，占位符{ }在其中起着举足轻重的作用。 这都是因为：format()会返回格式化的字符串。

##### 2) 示例代码一

让我们看另一个例子。假如需要进行数学运算，需要两个值相加，类似得到 **2+3=5** 的结果，而不仅仅是这两个数相加，那么就需要声明两个变量a和b来完成加法。

```
a = 2; b= 3
sum = a + b
print("a + b = ", sum)

```

运行结果如下：

```
a + b = 5

```

但若有很多数值相加或者相乘、相除等，这个打印结果就不会很好看，对变量使用也显得刻板无味。

如果我们使用format()方法来格式化文本，会得到更好的结果：

```
a = 2; b= 3
print("a + b = {}".format(a + b))

```

代码简化后，结构清晰，格式占位符{ } 对应a + b的结果。仍然输出同样结果：

```
a + b = 5

```

#### 2. 全局函数format

在Python编程语言中，用format函数可以更好地控制输出格式。

##### 1） 输出字段的格式

Format()可以控制输出字段格式，例如：需要输出10的 10次幂，由于数值太长，需要用逗号分隔开。 因此，可以写出如下代码：

```
pw = 10 ** 10
result = format(pw, ',')
print("The result is {}".format(result))

```

运行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/7b2e756a840e4f2bbc70ac32cae3962f.png" alt="在这里插入图片描述">

##### 2） 浮点数输出

当涉及到浮点数输出时，通常需要指定小数点位数，那么使用Format函数就十分方便，看以下代码：

```
pi = 3.14159265
result = format(pi, '6.2f')
print('Pi equals{}'.format(result))

```

圆周率pi变量的值有很多位小数，但是，我只想保留整数位6位和小数位2位，则可用’6.2f’来限制浮点数格式，得出结果后再打印输出。

运行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/5d84631176154596a926ba8cb743f776.png" alt="在这里插入图片描述">

##### 3） 字符串切割输出

除了浮点数外，长字符串也会面临同样问题。如果需要截断字符串，可以用format函数控制输出位数。看以下代码：

```
msg = 'Taylor Swift is a world-famous country music songwriter and singer.'
result = format(msg, '50.12')
print("Welcome! {}.".format(result))

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/9647bffe952446fdaeff8654f55b4251.png" alt="在这里插入图片描述"> 利用format函数成功截取了长度12个字符的结果Taylor Swift。

后续如果有空，我将会分享更多有趣的格式化字符串的案例。

#### 相关阅读：
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 