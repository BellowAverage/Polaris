
--- 
title:  Python 中 4 个高效的技巧（建议收藏） 
tags: []
categories: [] 

---
今天我想和大家分享 4 个省时的 Python 技巧，可以节省 10~20% 的 Python 执行时间。

### 反转列表

Python 中通常有两种反转列表的方法：切片或 `reverse()` 函数调用。这两种方法都可以反转列表，但需要注意的是内置函数 `reverse()` 会更改原始列表，而切片方法会创建一个新列表。

但是他们的表现呢？哪种方式更有效？让我们看一下下面的例子：

**使用切片：**

```
$ python -m timeit -n 1000000 -s 'import numpy as np' 'mylist=list(np.arange(0, 200))' 'mylist[::-1]'
1000000 loops, best of 5: 15.6 usec per loop

```

**使用 reverse()：**

```
$ python -m timeit -n 1000000 -s 'import numpy as np' 'mylist=list(np.arange(0, 200))' 'mylist.reverse()'
1000000 loops, best of 5: 10.7 usec per loop

```

这两种方法都可以反转列表，但需要注意的是内置函数 `reverse()` 会更改原始列表，而切片方法会创建一个新列表。

显然，内置函数 `reverse()` 比列表切片方法更快！

### 交换两个值

用一行代码交换两个变量值是一种更具有 Python 风格的方法。

与其他编程语言不同，Python 不需要使用临时变量来交换两个数字或值。举个简单的例子：

```
variable_1 = 100 
variable_2 = 500

```

要交换 `variable_1` 和 `variable_2` 的值，只需要一行代码。

```
variable_1, variable_2 = variable_2, variable_1

```

您也可以对字典使用相同的技巧：

```
md[key_2], md[key_1] = md[key_1], md[key_2]

```

该技巧可以避免多次迭代和复杂的数据转换，从而减少执行时间。

### 在函数内部循环

我们都喜欢创建自定义函数来执行我们自己的特定任务。然后使用 `for` 循环遍历这些函数，多次重复该任务。

但是，在 `for` 循环中使用函数需要更长的执行时间，因为每次迭代都会调用该函数。

相反，如果在函数内部实现了 `for` 循环，则该函数只会被调用一次。

为了更清楚地解释，让我们举个例子！另外，搜索公众号Linux就该这样学后台回复“git书籍”，获取一份惊喜礼包。

首先创建一个简单的字符串列表：

```
list_of_strings = ['apple','orange','banana','pineapple','grape']

```

创建两个函数，函数内部和外部都有 `for` 循环，从简单的开始。

```
def only_function(x):
    new_string = x.capitalize()
    out_putstring = x + " " + new_string
    print(output_string)

```

和一个带有循环的 `for` 函数：

```
def for_in_function(listofstrings):
    for x in list_of_strings:
        new_string = x.capitalize()
        output_string = x + " " + new_string
        print(output_string)

```

显然，这两个函数的输出是一样的。

然后，让我们比较一下，哪个更快？

<img src="https://img-blog.csdnimg.cn/img_convert/d5302d5cccface93d0ee27e00f4bd16d.png" alt="">

如您所见，在函数内使用 `for` 循环会稍微快一些。

### 减少函数调用次数

判断对象的类型时，使用 `isinstance()` 最好，其次是对象类型标识 `id()`，对象值 `type()` 最后。

```
# Check if num an int type
type(num) == type(0) # Three function calls
type(num) is type(0) # Two function calls
isinstance(num,(int)) # One function call

```

不要将重复操作的内容作为参数放在循环条件中，避免重复操作。

```
# Each loop the len(a) will be called
while i &lt; len(a):
    statement
# Only execute len(a) once
m = len(a)
while i &lt; m:
    statement

```

要在模块 X 中使用函数或对象 Y，请直接使用 `from X import Y` 而不是 `import X; then X.Y`。这减少了使用 Y 时的一次查找（解释器不必先查找 X 模块，然后在 X 模块的字典中查找 Y）。

总而言之，你可以大量使用 Python 的内置函数。提高 Python 程序的速度，同时保持代码简洁易懂。

如果想进一步了解 Python 的内置函数，可以参考下表，或查看以下网站（https://docs.python.org/3/library/functions.html）：

<img src="https://img-blog.csdnimg.cn/img_convert/6bff6cf813df94a8b6ce1de1cc0d96b0.png" alt="">

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
