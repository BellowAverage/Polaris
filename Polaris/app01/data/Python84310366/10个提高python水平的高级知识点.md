
--- 
title:  10个提高python水平的高级知识点 
tags: []
categories: [] 

---
>  
 分享一些有助于我们掌握 Python 的高级概念。如迭代器、生成器、装饰器、双端队列、排序字典等！ 


本文，我们将分享一些有助于我们掌握 Python 的高级概念。如迭代器、生成器、装饰器等！

### 1. 异常处理

`异常处理`是一个很重要的概念，它可以帮助我们更好地解决程序中的各种问题。

异常是在程序执行过程中发生并中断的情况。它可能由于多种原因而发生。比如：除法运算中分母为0的情况，会抛出：`ZeroDivisionError`；导入不存在的包时，会抛出：`ImportError`；列表越界时，会抛出：`IndexError`。python 中大约有30个内置异常。

我们使用 `try` 和 `except` 来处理 Python 中的异常。语法如下：

```
try:
    pass # 可能发生异常的代码
except ValueError:
    pass # 发生异常时执行的代码
except ZeroDivisionError:
    pass # 发生异常时执行的代码
else:
    pass # 其他情况时执行的代码
finally:
    pass # 最终执行的执行的代码

```

### 2. collections模块

`collections` 模块被称为用于存储数据的容器。例如列表、元组、集合、字典。Python 中有许多库是为了提供额外的数据结构而开发的， `collections`就是其中之一，旨在改进内置容器的功能。该模块中最常用的五种数据结构：

#### 1. Counter

>  
 对可迭代对象的计数。 


```
from collections import Counter
data = [1,1,1,2,3,4,3,3,5,6,7,7,1]
count = Counter(data)
print(count) # Counter({1: 4, 2: 1, 3: 4, 4: 1, 5: 1, 6: 1, 7: 2})

## ⚠️ Counter有几个惊艳的方法：

# 返回出现次数最多的前3个元素
print(count.most_common(3)) # [('1', 4), ('3', 4), ('2', 1)]

# 返回生成Counter对象的数据，迭代器格式。
for i in count.elements():
    print(i) # 1 1 1 2 3 4 3 3 5 6 7 7 1

```

#### 2. namedtuple

>  
 给元组元素命名，并且可以通过名字访问元素。 


```
from collections import namedtuple
User = namedtuple('User', ['name', 'sex', 'age'])
user = User(name='Runoob', sex='male', age=12)
print(user) # User(name='Runoob', sex='male', age=12)
user = User._make(['RunoX', 'Male', 13])
print(user) # User(name='RunoX', sex='Male', age=13)
print(user.name, user.sex, user.age) # RunoX Male 13
user = user._replace(age=22)
print(user) # User(name='RunoX', sex='Male', age=22)
print(user._asdict()) # {'name': 'RunoX', 'sex': 'Male', 'age': 22}

```

#### 3. OrderedDict

>  
 OrderedDict 是一种可以记住它们插入顺序的字典。当然，在最新版本的 Python 中，内置的 dict 也可以记住它。 


```
from collections import OrderedDict
dictt = OrderedDict()
dictt['a'] = 5
dictt['d'] = 2
dictt['c'] = 1
dictt['b'] = 3
print(dictt) # OrderedDict([('a', 5), ('d', 2), ('c', 1), ('b', 3)])

```

#### 4. defaultdict

>  
 `defaultdict` 将返回字典中不存在的键的默认值，而不是显示键错误。当然新版的`dict.get()`方法也可以返回默认值。 


```
# 创建一个默认值为0的字典
from collections import defaultdict
dictt = defaultdict(int)
dictt['a'] = 2
print(dictt['a']) # 2
print(dictt['b']) # 0

# 新版本的 `dict.get()` 方法
dict = {<!-- -->'a': 1, 'b': 2}
print(dict.get('a', 0)) # 1
print(dict.get('c', 0)) # 0
print(dict.get('c')) # None

```

#### 5. deque

>  
 `deque` 是一个双端队列，可以从两侧添加和删除元素。 


```
from collections import deque
queue = deque(['a', 'b', 'c'])
queue.append('d')
print(queue) # deque(['a', 'b', 'c', 'd'])
queue.appendleft('e')
print(queue) # deque(['e', 'a', 'b', 'c', 'd'])
queue.pop()
print(queue) # deque(['e', 'a', 'b', 'c'])
queue.popleft()
print(queue) # deque(['a', 'b', 'c'])

```

### 3. itertools 模块

>  
 Python `itertools` 模块提供了各种适用于组合计算的函数。 

1.  `product(iterable,iterable)`：两个iterables的笛卡尔积 1.  `permutation(iterable)`：所有可能的排序，没有重复元素 1.  `combinations(iterable,n)`：指定长度的所有可能组合，不重复。这里 n 是组合元组的大小。 1.  `combinations_with_replacement(iterable,n)`：指定长度的所有可能的组合，重复。 1.  `accumlate(iterable)` ：返回累积iterable元素的总和。 1.  `groupby(iterable,key=FUNC)` ：返回一个迭代器，其中包含来自可迭代对象的连续键和组。 
```
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
a = [1,2,3]
print(list(product(a,a))) # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
print(list(permutations(a))) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(combinations(a,2))) # [(1, 2), (1, 3), (2, 3)]
print(list(combinations_with_replacement(a,2))) # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
print(list(accumulate(a))) # [1, 3, 6]
print(list(groupby(a))) # [(1, &lt;itertools._grouper object at 0x7f8b8b8b9d10&gt;), (2, &lt;itertools._grouper object at 0x7f8b8b8b9d20&gt;), (3, &lt;itertools._grouper object at 0x7f8b8b8b9d30&gt;)]

```

### 4. lambda 函数

>  
 lambda 函数是一种匿名函数，它的语法只包含一个语句，即：`lambda [arg1 [,arg2,.....argn]]:expression`。 


```
even_or_odd = lambda a: a%2==0
numbers = [1,2,3,4,5]
even = list(map(even_or_odd,numbers))
print(even) # [False, True, False, True, False]

```

### 5. 装饰器

装饰器是 Python 的一个特性，它可以在不显式修改现有代码的情况下向现有代码添加一些新功能。

有两种类型的装饰器——函数装饰器和类装饰器。装饰器函数在函数名前有一个@。

要理解装饰器的概念，我们首先需要了解一件事——python 中的函数是类对象。与其他对象不同，它们可以在函数内部定义，在其他函数中作为参数传递，甚至作为函数返回。

```
import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        a,b = args
        print(a*b)
        result = func(*args,**kwargs)
        print(a/b)
        return result
    return wrapper

@decorator
def add(x,y):
    return x+y
result = add(5,6)
print(result) ##

```

让我们理解上面装饰器的例子:

首先，我们有一个函数名 add，它的工作是获取两个变量并返回它们的总和。现在经过一段时间的工作后，我们意识到需要为同一个函数添加乘法和除法功能。现在我们有两个选择，第一个是在同一个 add 函数中添加乘法和除法代码。或者我们可以使用装饰器来添加功能而无需显式更改函数。

为了使用装饰器，我们首先在第 2 行定义了一个装饰器函数。此函数将 func 作为输入。在第二行中，我们有另一个函数，因为我们知道我们可以在函数内部定义函数。它是一个具有 `*args`、`**kwargs` 函数参数的包装函数。有了这些，两者都定义为参数，现在我们可以在函数内部传递任意数量的参数。在包装函数的主体中，我们有乘法逻辑，然后仅使用加法逻辑调用实际的加法函数，最后我们有除法逻辑。当我们使用一些参数 `add(5,6)` 调用 add 函数时，输出将是：

```
30  
0.8333333333333334  
11  


```

因为它首先执行乘法逻辑并打印值，然后加法逻辑并保存值，然后除法逻辑并打印值，最后返回相加的值并打印值。

### 6. 迭代器

生成器是一种返回可迭代对象的函数。它至少包含一个 `yield` 语句。`yield` 是 Python 中的一个关键字，用于从函数返回值而不破坏其当前状态或对局部变量的引用。带有 yield 关键字的函数称为生成器。相对于 `return` 你可以把 `yield` 理解为不中断函数的暂停，并且返回一个值。

生成器仅在需要时生成一次项目。它们的**内存效率很高，占用的内存空间更少**。

```
def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
        yield a

for i in fibonacci(5):
    print(i) ## 1 1 2 3 5

```

### 7. 进程和线程

线程和多处理都用于同时运行多个脚本。进程是程序的一个实例，线程是进程中的一个实体。

线程化是多个线程同时运行以执行不同任务的技术，而多处理是多个进程同时运行在不同CPU上的技术。下图对进程和线程的区别进行了说明，更多的信息请参考：这儿

<img src="https://img-blog.csdnimg.cn/img_convert/29b02b1cdf40bc255e9347e516f578c2.png" alt="">

### 8. 双下划线方法

`Dunder` 是 `Double` 和 `Under` 的缩写，称为双下划线方法，是python中的一种特殊方法。

```
num =5
print(num*6) ## 30
print(num.__mul__(6)) ## 30

```

这些方法主要用于重载预定义的运算符。例如，`+`、`-`、`*`、`/` 是必须在数字对象周围使用的数字运算符，但 `+` 也用作两个字符串之间的连接运算符。所以我们可以说 `+` 运算符被重载来执行多个任务。

```
a =5
b =6
print(a+b) ## 11
print(a.__add__(b)) ## 11
c = 'hello'
d = 'world'
print(c+d) ## helloworld
print(c.__add__(d)) ## helloworld

```

### 9. 日志

日志记录是在代码执行时捕获代码流的过程。日志记录有助于轻松调试代码。它通常在文件中完成，以便我们以后可以检索它。在 python 中，我们有一个库日志记录，可以帮助我们将日志写入文件。有五个级别的日志记录：
1.  `Debug` 调试：用于诊断问题的详细信息。 1.  `Info` 信息：成功确认。 1.  `Warning` 警告：发生意外情况时。 1.  `Error` 错误：由于比警告更严重的问题。 1.  `Critical` 严重：严重错误后程序无法自行运行。 
这儿作者推荐大家一个简单的日志记录工具：`loguru`。

### 10. 上下文管理器

上下文管理器是 Python 中的一个很好的工具，可以帮助进行资源管理。它们允许您在需要时分配和释放资源。上下文管理器最常用和最受认可的例子是 with 语句。with 主要用于打开和关闭文件。

```
with open('./test.txt', 'w') as f:
    f.write('Hello World!')

```

### 小节

上面分享的10个提供python水平的高级知识点，希望在你工作或面试中有所帮助。

在编程的路上，挑战与精进同在，尝试学习使用**装饰器** 、`yield`、`itertool` 之类的高级功能，可以让你的编程生活变得更加有趣！

## 关于Python学习指南

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后给大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、自动化办公等学习教程。带你从零基础系统性的学好Python！</mark>

#### 👉Python所有方向的学习路线👈

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取）**</mark>

<img src="https://img-blog.csdnimg.cn/3c4ee87941694f3789398db3d52a2637.png#pic_center" alt="在这里插入图片描述">

#### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。

<img src="https://img-blog.csdnimg.cn/64c89bf6293d4699bf7ee8f34b9e69fd.png#pic_center" alt="在这里插入图片描述">

#### <mark>温馨提示：篇幅有限，已打包文件夹，获取方式在：文末</mark>

#### 👉Python70个实战练手案例&amp;源码👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/2017b67544f94e8898db755e2703224a.png#pic_center" alt="在这里插入图片描述">

#### 👉Python大厂面试资料👈

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自**阿里、腾讯、字节等一线互联网大厂**最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/3055c54d3224495987c589f150324d73.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b0751719fe914aec8c8d09f62f772e44.png#pic_center" alt="在这里插入图片描述">

#### 👉Python副业兼职路线&amp;方法👈

学好 Python 不论是就业还是做副业赚钱都不错，但要学会兼职接单还是要有一个学习规划。

<img src="https://img-blog.csdnimg.cn/01bcd7cbfd6d43fb85ef410766735154.png#pic_center" alt="在这里插入图片描述">

**👉** **这份完整版的Python全套学习资料已经上传，朋友们如果需要可以扫描下方CSDN官方认证二维码或者点击链接免费领取**【**`保证100%免费`**】

<font color="red">**点击免费领取《CSDN大礼包》： 安全链接免费领取**</font>
