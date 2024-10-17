
--- 
title:  使用 Python 标准库，也可以做的 3 件很酷的事情！ 
tags: []
categories: [] 

---
第三方库在使 Python 成为数据科学首选时起着至关重要的作用。从清理原始数据到构建高级机器学习管道，你可以找到用于简化任务并促进开发过程的 Python 库。

在这丰富的库选择中，我们有时会忽视 Python 的内置功能，也就是 Python 标准库。

Python的内置函数和方法对于与数据相关的任务非常有效。实际上，我们经常使用其中一些，比如 len、range 和 sorted。在本文中，我们将提及一些内置函数，并学习如何利用它们做三件有趣的事情。

### 1. 字符串模块用于数据清洗

字符串模块有几个函数可用于执行常见的字符串操作。我主要用它们来进行数据清洗。

文本数据有时可能非常杂乱，需要进行大量的清洗和处理才能用于下游处理过程。

考虑一个需要从文本中删除标点符号的情况。有不同的方法可以做到这一点，但使用 maketrans 方法非常简单。它返回一个翻译表，可以传递给 translate 函数来执行这个翻译。此外，string.punctuation 可以避免我们编写所有的标点符号。

这是我们在代码中如何做的：

```
import string

sentence = "Hello!!!! Are you planning? to come to the WEDDING?!"

trans = str.maketrans("", "", string.punctuation)

sentence.translate(trans)
# 输出
'Hello Are you planning to come to the WEDDING'

```

变量 trans 是一个翻译表，将 string.punctuation 中的每个字符映射到一个空字符串，这意味着将它们删除。

为了使其更标准化，我们可以将字母转换为小写。

```
sentence.translate(trans).lower()
# 输出
'hello are you planning to come to the wedding'

```

### 2. dict 构造函数

dict 构造函数创建了一个字典，这是Python的内置数据结构之一。字典由键值对组成。

字典在各种任务中非常有用。使用字典的一个优点是，字典操作的时间复杂度通常是常数时间 (即 O(1))，因为它们使用哈希表作为底层数据结构。

dict 构造函数之所以如此有用，是因为它对输入的灵活性。它能够将不同类型的数据格式转换为键值映射。让我们看一些例子。

```
# 两个列表
names = ["John", "Jane", "Dan"]
grades = [90, 87, 92]

dict(zip(names, grades))
# 输出
{<!-- -->'John': 90, 'Jane': 87, 'Dan': 92}

```

```
# Pandas Series
import pandas as pd

text = "It takes consistency and dedication to learn data science as it is still an evolving field"

ser = pd.Series(text.lower().split(" ")).value_counts()

dict(ser)
# 输出
{<!-- -->'it': 2,
 'takes': 1,
 'consistency': 1,
 'and': 1,
 'dedication': 1,
 'to': 1,
 'learn': 1,
 'data': 1,
 'science': 1,
 'as': 1,
 'is': 1,
 'still': 1,
 'an': 1,
 'evolving': 1,
 'field': 1}

```

```
# 元组列表
grades = [("John", 85), ("Emily", 90), ("Max", 78)]

dict(grades)
# 输出
{<!-- -->'John': 85, 'Emily': 90, 'Max': 78}

```

### 3. F-strings

在字符串中写入变量是一种常见的做法，用于调试和记录日志。这被称为字符串插值，它通过编写占位符来在字符串中保存变量值。

Python 中有不同的字符串插值方法。最新的方法是格式化字符串字面值 (即 f-strings)。它们是在 Python 3.6 中引入的。

F-strings 比其他字符串插值方法更易读，也更灵活。我们将介绍一些示例，演示了 f-strings 的灵活性以及如何更高效地使用它们。

```
# 使大数字易于阅读
number = 3450045402359

print(f"Number of rows in raw data: {<!-- -->number:,d}")
# 输出
Number of rows in raw data: 3,450,045,402,359

```

```
# 解析日期
from datetime import datetime
today = datetime.today().date()

print(f"The date is {<!-- -->today}.")
print(f"The year is {<!-- -->today:%Y}.")
print(f"The month is {<!-- -->today:%B}.")

# 输出
The date is 2023-12-20.
The year is 2023.
The month is December.

```

```
# 更多示例
from datetime import timedelta, datetime

today = datetime.today().date()

print(f"Due date is {<!-- -->today + timedelta(days=35)}") # 添加35天
# 输出
Due date is 2024-01-24

```

```
# 成员 ID
member_ids = [1010, 1011, 1023, 1030, 1039, 1045]

print(f"There are {<!-- -->len(member_ids)} members.")
# 输出
There are 6 members.

```

F-strings 还允许写入表达式，使得它们更加灵活。我们可以在 f-strings 中进行计算，因此如果仅需要用于调试，则无需创建新变量。

以上是一些示例，演示了如何使用 f-strings 进行更多操作，比如将数字转换为二进制格式和填充。

### 最后

Python 标准库提供了大量函数来处理各种操作。我们通常使用第三方库，这些库旨在解决特定任务，比如 Pandas 用于数据清洗和分析，NumPy 用于科学计算。这并不意味着我们不应该使用Python标准库。使用其他库并不是一个阻碍。相反，标准库只是增强了其他库的功能。

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
