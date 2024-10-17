
--- 
title:  不要再写 Python for 循环了！ 
tags: []
categories: [] 

---
为什么要挑战自己在代码里不写 for loop？因为这样可以迫使你去学习使用比较高级、比较地道的语法或 library。文中以 python 为例子，讲了不少大家其实在别人的代码里都见过、但自己很少用的语法。

通常如下使用场景中会用到 for 循环：
-  在一个序列来提取一些信息。 -  从一个序列生成另一个序列。 -  写 for 已成习惯。 
幸运的是，Python 已经有很多工具可以帮助你完成这些工作，你只需要转移你的思路，并以不同的角度来思考它。

通过避免编写 for 循环，你可以获得什么好处：
-  较少的代码量 -  更好的代码可读性 -  更少的缩进（对 Python 还是很有意义的） 
我们来看一下下面的代码结构：

```
# 1  
with ...:  
    for ...:  
        if ...:  
            try:  
            except:  
        else:  

```

在这个例子中，我们正在处理多层嵌套的代码，这很难阅读。这个例子使用了多层嵌套的代码。我在这段代码中发现它无差别使用缩进把管理逻辑（with, try-except）和业务逻辑（for, if）混在一起。如果你遵守只对管理逻辑使用缩进的规范，那么核心业务逻辑应该立刻脱离出来。

“扁平结构比嵌套结构更好” - The Zen of Python

可以使用的已有的工具来替换 for 循环

### 1、列表推导式

(List Comprehension / Generator 表达式)

我们来看一个简单的例子。如果你想将一个数组转换为另一个数组：

```
result = []  
for item in item_list:  
    new_item = do_something_with(item)  
    result.append(item)  

```

如果你喜欢 MapReduce，你也可以使用 map，或者 Python 中的**列表推导式**：

```
result = [do_something_with(item) for item in item_list]  

```

同样，如果您只想迭代数组中的元素，也可以使用一样的代码 Generator Expression。result = (do_something_with(item) for item in item_list)

### 2、函数

如果您想要将一个数组映射成另外数组，只需调用 map 函数，就可以用一个更高级、更实用的编程方式解决这个问题。

```
doubled_list = map(lambda x: x * 2, old_list)  

```

如果要将序列减少为单个，请使用 reduce

```
from functools import reduce  
summation = reduce(lambda x, y: x + y, numbers)  

```

另外，许多 Python 内置函数都会使用 iterables：

<img src="https://img-blog.csdnimg.cn/img_convert/d8973547da84fb7be717df585b613f57.png" alt="">

### 3、Extract Functions

(Extract Functions or Generators)

上述两种方法是很好的处理更简单的逻辑。更复杂的逻辑怎么样？作为程序员，我们编写函数来抽离出复杂的业务。相同的想法适用于此。如果你是这样写的：

```
results = []  
for item in item_list:  
    # setups  
    # condition  
    # processing  
    # calculation  
    results.append(result)  

```

显然你对一个代码块添加了太多的责任。相反，我建议你做：

```
def process_item(item):  
    # setups  
    # condition  
    # processing  
    # calculation  
    return result  
  
results = [process_item(item) for item in item_list]  

```

如果换成嵌套函数会如何

```
results = []  
for i in range(10):  
    for j in range(i):  
        results.append((i, j))  

```

换成 List Comprehension 来实现是这样的：

```
results = [(i, j)  
           for i in range(10)  
           for j in range(i)]  

```

如果你的代码块需要记录一些内部状态

```
# finding the max prior to the current item  
a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]  
results = []  
current_max = 0  
for i in a:  
    current_max = max(i, current_max)  
    results.append(current_max)  
  
# results = [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]  

```

我们使用 generator 来实现这一点：

```
def max_generator(numbers):  
    current_max = 0  
    for i in numbers:  
        current_max = max(i, current_max)  
        yield current_max  
  
a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]  
results = list(max_generator(a))  

```

读者可能要问 “等等！你在 generator 中用到 for 循环，作弊啊！别急，再看看下面的代码。

不需要自己写

itertools 会帮你实现了

这个模块很简单。我相信这个模块在大多数场景中可以替换你原先的 for 循环。例如，最后一个例子可以重写为：

```
from itertools import accumulate  
a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]  
resutls = list(accumulate(a, max))  

```

另外，如果要迭代组合序列，则需要使用`product()`， `permutations()`， `combinations()`。

### 结论
-  在大多数情况下，您都不需要编写 for 循环。 -  你应该避免编写 for 循环，这样会有更好的代码可读性。 
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
