
--- 
title:  Python数据分析三剑客之Pandas 
tags: []
categories: [] 

---
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/35f2f68353bb18ea4f5768f11fb47458.webp?x-oss-process=image/format,png">

>  
 写在前面的话： 开始之前请确保已经配置好python环境，并安装好第三方库pandas和numpy。 


### 1. pandas库介绍

什么是pandas？pandas是提供高性能易用数据类型和数据分析工具的**第三方库**。简单讲，pandas主要作用有两个：提供了简易高效的数据类型、提供了数据分析的工具。pandas基于numpy，常和numpy、matplotlib一起使用。 关于数据类型，python中自带的数据类型远远不能满足于数据分析。可以说在数据分析中numpy中的数据类型是基础数据类型，关注的是数据的结构表达，体现在数据间的关系（维度）；pandas中的数据类型是基于numpy的扩展数据类型，关注的是数据的应用表达，体现在数据与索引之间的关系上。我们再学习pandas时最重要的是**理解如何去操作索引**，从某种程度上来说，操作索引就是操作数据。

### 2. pandas库的series类型

pandas主要有两种数据类型，一维度的`Series`数据类型，二维及高维的`DataFrame`类型。我们先来看一下第一种，series类型。

2.1 什么是series类型？

series类型由一组数据及与之相关的数据索引组成。我们来看几行代码：

```
     import pandas as pd
    
     a = pd.Series([7,8,9,10])
     print(a)
复制代码
```

输出如下：

```
     0     7
     1     8
     2     9
     3    10
     dtype: int64
复制代码
```

观察输出代码，我们可以发现Series对象一共由3部分组成：左侧**自动索引部分**，右侧**数据部分**，底部**数据类型**（numpy中的数据类型）部分。

除了自动添加索引外，我们还可以对其索引进行自定义：

```
     import pandas as pd
     
     a =pd.Series([7,8,9,10],index=["a","b","c","d"])  # index指定索引
     print(a)
复制代码
```

输出如下：

```
     a     7
     b     8
     c     9
     d    10
     dtype: int64
复制代码
```

可见，索引部分变为了我们自定义的`abcd`。

2.2 如何创建series类型？

创建Series类型的方法有很多种，主要以 以下几种为主：

 1. 从**标量**创建
 1. 从**字典**创建
 1. 从**ndarray**类型创建
 1. 从**列表**创建

**下面进行具体讲解：**

（1）从标量值创建

即指定一个标量生成一个series类型，如下：

```
     import pandas as pd
     
     a = pd.Series(5,index=["a","b","c","d","e","f"])
     print(a)
复制代码
```

输出如下：

```
 a    5
 b    5
 c    5
 d    5
 e    5
 f    5
 dtype: int64
复制代码
```

需要注意的是，此时的index参数不能省略（因为需要index来指定生成元素的个数和索引）。 （2）从字典类型创建 传入一个参数字典，字典的键为series类型的索引，字典的值为series类型的值：

```
 import pandas as pd
 ​
 my_dir={
     "a":1,
     "b":2,
     "c":3
 }
 b = pd.Series(my_dir)
 print(b)
复制代码
```

输出如下：

```
 a    1
 b    2
 c    3
 dtype: int64
复制代码
```

此外，利用字典构造series类型时，我们同样可以使用index来指定其索引或改变其结构，这个索引会覆盖字典中的“键索引”。

（3）从ndarray类型创建 ndarray类型是numpy中的数据类型，我们可以直接传入ndarray类型进行创建：

```
     import pandas as pd
     import numpy as np
     
     c = np.arange(4)
     d = pd.Series(c)
     print(d)
复制代码
```

输出如下：

```
     0    0
     1    1
     2    2
     3    3
     dtype: int32
复制代码
```

同样，也可以使用index参数自定义索引。

（4）也可以从python列表创建，见2.1中的小例。

2.3 series类型的基本使用

Series对象包括index和values两部分，所以主要是这两部分操作。我们先看一下下面的案例：

 - a.index:获取索引
 - a.values: 获取数据
 - a['a']: 获取索引为a的元素
 - a[0]：获取索引为0的元素，注意！自动索引和自定义索引并存但不能混合使用

因为series是基于ndarray类型的，所以对Series的操作类似于ndarray类型的操作：

 - numpy中运算和操作可用于series类型
 - 可以通过自动索引或自定义索引对其进行切片

```
     import pandas as pd
      
     a = pd.Series([1,2,3,4,5,6],index=["a","b","c","d","e","f"])
     
     print("a的值：",a.values)
     print("a的索引：",a.index)
     print("a[0]：",a[0])
     print("a['a']:",a["a"])
     print("a切片：\n",a[::-1])
复制代码
```

输出如下：

```
     a的值： [1 2 3 4 5 6]
     a的索引： Index(['a', 'b', 'c', 'd', 'e', 'f'], dtype='object')
     a[0]： 1
     a['a']: 1
     a切片：
      f    6
     e    5
     d    4
     c    3
     b    2
     a    1
     dtype: int64
复制代码
```

此外，series类型具备**对齐**操作。如下：

```
     import pandas as pd
     
     
     a = pd.Series([1,2,3],index=["c","d","e"])
     b = pd.Series([4,5,6,7,8],index=["a","b","e","f","g"])
     c = a+b
     print(c)
复制代码
```

输出如下：

```
     a    NaN
     b     NaN
     c    NaN
     d     NaN
     e     9.0
     f     NaN
     g     NaN
     dtype: float64
复制代码
```

我们让两个series类型相加。观察输出结果可以发现，只有当a、b两者中有相同索引（包括位置）时，他们才会相加，而其余值则不会相加。这就对是series的对齐操作。这也同时验证了pandas是基于索引的运算。

Series类型还有一个name属性，即series对象和索引都可以被赋予一个名称。我们可以使用.name来获取或定义其名称。

```
 import pandas  as pd
 ​
  a = pd.Series([1,2,3],index=["c","d","e"])
  
 print(a.name)   # 初始是没有名称的
 a.name = "mySeries"
 print(a.name)
   
 print(a.index.name)
 a.index.name = "索引列"
 print(a.index.name)
 print("*"*20)
 print(a)
复制代码
```

输出如下：

```
  None
 mySeries
 None
 索引列
 ********************
 索引列
 c    1
 d    2
 e    3
 Name: mySeries, dtype: int64
复制代码
```

### 3. pandas库的Da
