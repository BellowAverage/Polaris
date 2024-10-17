
--- 
title:  python项目开发案例集锦 pdf,python开发案例集锦pdf 
tags: []
categories: [] 

---
大家好，给大家分享一下python项目开发案例集锦pdf百度网盘，很多人还不知道这一点。下面详细解释一下。现在让我们来看看！



<img alt="" height="1067" src="https://img-blog.csdnimg.cn/img_convert/c175706d5ef6238c52822403d085bf81.jpeg" width="800">

Source code download: 

Python是目前最流行的语言之一，它在数据科学、机器学习、web开发、脚本编写、自动化方面被许多人广泛使用。它的简单和易用性造就了它如此流行的原因。

<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/9e2f0dd90b0e327554b55a352f39bfcd.png">

在本文中，我们将会介绍 30 个简短的代码片段，你可以在 30 秒或更短的时间里理解和学习这些代码片段。

1.检查重复元素

下面的方法可以检查给定列表中是否有重复的元素。它使用了 set() 属性，该属性将会从列表中删除重复的元素。

```
def all_unique(lst):        return len(lst) == len(set(lst))        x = [1,1,2,2,3,2,3,4,5,6]    y = [1,2,3,4,5]    all_unique(x) # False    all_unique(y) # True

```

2.变位词

检测两个字符串是否互为变位词（即互相颠倒字符顺序）

```
from collections import Counter    def anagram(first, second):        return Counter(first) == Counter(second)    anagram("abcd3", "3acdb") # True

```

3.检查内存使用情况

以下代码段可用来检查对象的内存使用情况。

```
import sys    variable = 30     print(sys.getsizeof(variable)) # 24

```

4.字节大小计算

以下方法将以字节为单位返回字符串长度。

```
def byte_size(string):        return(len(string.encode( utf-8 )))        byte_size( 😀 ) # 4    byte_size( Hello World ) # 11

```

5.重复打印字符串 N 次

以下代码不需要使用循环即可打印某个字符串 n 次

```
n = 2; s ="Programming"; print(s * n); # ProgrammingProgramming

```

6.首字母大写

以下代码段使用 title() 方法将字符串内的每个词进行首字母大写。

```
s = "programming is awesome"    print(s.title()) # Programming Is Awesome

```

7.分块

以下方法使用 range() 将列表分块为指定大小的较小列表。

```
from math import ceil    def chunk(lst, size):        return list(            map(lambda x: lst[x * size:x * size + size],                list(range(0, ceil(len(lst) / size)))))    chunk([1,2,3,4,5],2) # [[1,2],[3,4],5]

```

8.压缩

以下方法使用 fliter() 删除列表中的错误值（如：False, None, 0 和“”）

```
def compact(lst):        return list(filter(bool, lst))    compact([0, 1, False, 2,   , 3,  a ,  s , 34]) # [ 1, 2, 3,  a ,  s , 34 ]

```

9.间隔数

以下代码段可以用来转换一个二维数组。

```
array = [[ a ,  b ], [ c ,  d ], [ e ,  f ]]    transposed = zip(*array)    print(transposed) # [( a ,  c ,  e ), ( b ,  d ,  f )]


```

10.链式比较

以下代码可以在一行中用各种操作符进行多次比较。

```
a = 3    print( 2 &lt; a &lt; 8) # True    print(1 == a &lt; 2) # False


```

11.逗号分隔

以下代码段可将字符串列表转换为单个字符串，列表中的每个元素用逗号分隔。

```
hobbies = ["basketball", "football", "swimming"]print("My hobbies are: " + ", ".join(hobbies)) # My hobbies are: basketball, football, swimming


```

12.计算元音字母数

以下方法可计算字符串中元音字母（‘a’, ‘e’, ‘i’, ‘o’, ‘u’）的数目。

```
import re    def count_vowels(str):        return len(len(re.findall(r [aeiou] , str, re.IGNORECASE)))    count_vowels( foobar ) # 3    count_vowels( gym ) # 0


```

13.首字母恢复小写

以下方法可用于将给定字符串的第一个字母转换为小写。

```
def decapitalize(string):        return str[:1].lower() + str[1:]    decapitalize( FooBar ) #  fooBar     decapitalize( FooBar ) #  fooBar


```

14.平面化

以下方法使用递归来展开潜在的深度列表。

```
def spread(arg):    ret = []    for i in arg:        if isinstance(i, list):            ret.extend(i)        else:            ret.append(i)    return retdef deep_flatten(lst):    result = []    result.extend(        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))    return resultdeep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]


```

15.差异

该方法只保留第一个迭代器中的值，从而发现两个迭代器之间的差异。

```
def difference(a, b):    set_a = set(a)    set_b = set(b)    comparison = set_a.difference(set_b)    return list(comparison)difference([1,2,3], [1,2,4]) # [3]


```

16.寻找差异

下面的方法在将给定的函数应用于两个列表的每个元素后，返回两个列表之间的差值。

```
def difference_by(a, b, fn):    b = set(map(fn, b))    return [item for item in a if fn(item) not in b]from math import floordifference_by([2.1, 1.2], [2.3, 3.4],floor) # [1.2]difference_by([{  x : 2 }, {  x : 1 }], [{  x : 1 }], lambda v : v[ x ]) # [ { x: 2 } ]


```

17.链式函数调用

以下方法可在一行中调用多个函数。

```
def add(a, b):    return a + bdef subtract(a, b):    return a - ba, b = 4, 5print((subtract if a &gt; b else add)(a, b)) # 9


```

18.检查重复值

以下方法使用 set() 方法仅包含唯一元素的事实来检查列表是否具有重复值。

```
def has_duplicates(lst):    return len(lst) != len(set(lst))    x = [1,2,3,4,5,5]y = [1,2,3,4,5]has_duplicates(x) # Truehas_duplicates(y) # False


```

19.合并两个词典

以下方法可用于合并两个词典。

```
def merge_two_dicts(a, b):    c = a.copy()   # make a copy of a     c.update(b)    # modify keys and values of a with the ones from b    return ca = {  x : 1,  y : 2}b = {  y : 3,  z : 4}print(merge_two_dicts(a, b)) # { y : 3,  x : 1,  z : 4}


```

在Python 3.5及更高版本中，你还可以执行以下操作：

```
def merge_dictionaries(a, b)   return {**a, **b}a = {  x : 1,  y : 2}b = {  y : 3,  z : 4}print(merge_dictionaries(a, b)) # { y : 3,  x : 1,  z : 4}


```

20.将两个列表转换成一个词典

以下方法可将两个列表转换成一个词典。

```
def to_dictionary(keys, values):    return dict(zip(keys, values))    keys = ["a", "b", "c"]    values = [2, 3, 4]print(to_dictionary(keys, values)) # { a : 2,  c : 4,  b : 3}


```

21.使用枚举

以下方法将字典作为输入，然后仅返回该字典中的键。

```
list = ["a", "b", "c", "d"]for index, element in enumerate(list):     print("Value", element, "Index ", index, )# ( Value ,  a ,  Index  , 0)# ( Value ,  b ,  Index  , 1)#( Value ,  c ,  Index  , 2)# ( Value ,  d ,  Index  , 3)


```

22.计算所需时间

以下代码段可用于计算执行特定代码所需的时间。

```
import timestart_time = time.time()a = 1b = 2c = a + bprint(c) #3end_time = time.time()total_time = end_time - start_timeprint("Time: ", total_time)# ( Time:  , 1.1205673217773438e-05)


```

23.Try else 指令

你可以将 else 子句作为 try/except 块的一部分，如果没有抛出异常，则执行该子句。

```
try:    2*3except TypeError:    print("An exception was raised")else:    print("Thank God, no exceptions were raised.")#Thank God, no exceptions were raised.


```

24.查找最常见元素

以下方法返回列表中出现的最常见元素。

```
def most_frequent(list):    return max(set(list), key = list.count)  list = [1,2,1,2,3,2,1,4,2]most_frequent(list)


```

25.回文

以下方法可检查给定的字符串是否为回文结构。该方法首先将字符串转换为小写，然后从中删除非字母数字字符。最后，它会将新的字符串与反转版本进行比较。

```
def palindrome(string):    from re import sub    s = sub( [W_] ,   , string.lower())    return s == s[::-1]palindrome( taco cat ) # True


```

26.没有 if-else 语句的简单计算器

以下代码段将展示如何编写一个不使用 if-else 条件的简单计算器。

```
import operatoraction = {    "+": operator.add,    "-": operator.sub,    "/": operator.truediv,    "*": operator.mul,    "**": pow}print(action[ - ](50, 25)) # 25


```

27.元素顺序打乱

以下算法通过实现 Fisher-Yates算法 在新列表中进行排序来将列表中的元素顺序随机打乱。

```
from copy import deepcopyfrom random import randintdef shuffle(lst):    temp_lst = deepcopy(lst)    m = len(temp_lst)    while (m):        m -= 1        i = randint(0, m)        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]    return temp_lst  foo = [1,2,3]shuffle(foo) # [2,3,1] , foo = [1,2,3]


```

28.列表扁平化

以下方法可使列表扁平化，类似于JavaScript中的[].concat(…arr)。

```
def spread(arg):    ret = []    for i in arg:        if isinstance(i, list):            ret.extend(i)        else:            ret.append(i)    return retspread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]


```

29.变量交换

以下是交换两个变量的快速方法，而且无需使用额外的变量。

```
def swap(a, b):  return b, aa, b = -1, 14swap(a, b) # (14, -1)

```

30.获取缺失键的默认值

以下代码段显示了如何在字典中没有包含要查找的键的情况下获得默认值。

```
d = { a : 1,  b : 2}print(d.get( c , 3)) # 3

```

以上是你在日常工作中可能会发现的有用方法的简短列表。它主要基于这个GitHub项目（https://github.com/30-seconds/30_seconds_of_knowledge），你可以在其中找到许多其他有用的代码片段，包括Python及其他编程语言和技术。

**-END-**

**学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后给大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！**

包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习、自动化测试带你从零基础系统性的学好Python！

>  
  👉（**安全链接，放心点击**） 
 

##### 👉Python学习大礼包👈

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9a2daf9927084238bd3861994fc5af23.png">

##### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。**（全套教程文末领取哈）**<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/direct/4add435c649a4f4d8246ca014a5baeb3.jpeg#pic_center">

#### 👉Python必备开发工具👈

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/direct/23914b3055914a04b50f2cf5f40f817d.jpeg#pic_center">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

#### 👉Python实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/direct/d87be323f61f4d618a5581d45e0f5e18.jpeg#pic_center">

#### 👉Python书籍和视频合集👈

观看零基础学习书籍和视频，看书籍和视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/direct/1664e32bdfd84e1c92be593c269d1d99.jpeg#pic_center">

#### 👉Python面试刷题👈

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center">

#### 👉Python副业兼职路线👈

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/direct/b81303b626de496eaa7c044a44f7062b.png"><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/034f3f53d2bc4a1a950e78c401439c5c.png#pic_center">**这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以点击链接免费领取**或者**保存图片到wx扫描二v码免费领取** 【`保证100%免费`】

👉（**安全链接，放心点击**）<img alt="" src="https://img-blog.csdnimg.cn/img_convert/f0e75fdd14a5f6da665cc52ca22155ae.png">
