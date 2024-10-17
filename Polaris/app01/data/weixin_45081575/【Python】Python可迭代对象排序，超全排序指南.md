
--- 
title:  【Python】Python可迭代对象排序，超全排序指南 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/d7d5803268474db7b8412a5f2ca4f378.jpeg#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - - - <ul><li>- - - - <ul><li>- - 


## 前言

>  
 记录一下`Python` 的通用排序，方便自己需要用到的时候拿来即用。 


本篇文章将对`Python可迭代对象（iterable` 的排序进行详尽介绍。 值得注意的是，是可迭代对象，也就是说列表(list)，元组(tuple)，集合(set)，字典(dict)等，都是通用的！
- **列表(list)，元组(tuple)，集合(set)用法是一致的，下文中将用列表(list)做展示**- **字典(dict)，可以根据键或值做排序，这个单独展示**
## 知识点📖📖

Python内置模块：**operator** Python内置函数：**sorted()** Python关键字：**lambda**

关于它们的使用，都可以从**Python**官网进行系统的学习~

## sorted()

### sorted()内置函数

>  
 在`Python` 中，常用的排序函数是 `sorted()`，这是一个内置函数。它可以将`可迭代对象`进行排序。 


**`sorted()` 用法如下：**

```
sorted(iterable, key=None, reverse=False)

```

返回一个包含可迭代对象中所有项的新列表，按升序排列
- **iterable**：可迭代对象（**必选**参数- **key**：默认为**None**，指定带有单个参数的函数，自定义排序顺序（**可选**参数- **reverse**：默认为**False**，正向排序；如为**True**，则反向顺序排序（**可选**参数
介绍完`sorted()` 之后，下面就开始使用它来排序

### 正向排序

**列表(list)，元组(tuple)，集合(set)**

```
&gt;&gt;&gt; _list = [10, 30, 40, 20]
&gt;&gt;&gt; print(sorted(_list))
[10, 20, 30, 40]

```

**字典(dict)**
- 默认是按照 dict的key来排序的（因为**value**可能多种多样，不同类型的无法比较~
```
&gt;&gt;&gt; _dict = {<!-- -->'A': 10, 'C': 30, 'B': 20, 'D': 40}
&gt;&gt;&gt; print(sorted(_dict))
['A', 'B', 'C', 'D']

&gt;&gt;&gt; print(dict(sorted(_dict.items())))
{<!-- -->'A': 10, 'B': 20, 'C': 30, 'D': 40}

```

### 反向排序

>  
 这个操作与正向排序一样，区别在于多了 `reverse=True` 


**列表(list)，元组(tuple)，集合(set)**

```
&gt;&gt;&gt; _list = [10, 30, 40, 20]
&gt;&gt;&gt; print(sorted(_list, reverse=True))
[40, 30, 20, 10]

```

**字典(dict)**

```
&gt;&gt;&gt; _dict = {<!-- -->'A': 10, 'C': 30, 'B': 20, 'D': 40}
&gt;&gt;&gt; print(sorted(_dict, reverse=True))
['D', 'C', 'B', 'A']

&gt;&gt;&gt; print(dict(sorted(_dict.items(), reverse=True)))
{<!-- -->'D': 40, 'C': 30, 'B': 20, 'A': 10}

```

### 指定key排序

>  
 这里的思路可以发散发散，遇到的数据类型会是多种多样的，当抛砖引玉了~ 


当需要排序复杂一些的数据时候，可以借助 `lambda` 或 `operator模块` 来指定 **key**； 而在实际使用过程中，`operator模块` 的速度是要比 `lambda` 快上不少的。当然，如果你的数据量不大，那它们两个使用起来没有差别。

#### 字典(dict)排序

先来看看数据简单的排序 **字典(dict)**
- `key=lambda item:item[n]`：items是元组，根据元组索引为 **n** 排序
```
&gt;&gt;&gt; _dict = {<!-- -->'A': 10, 'C': 30, 'B': 20, 'D': 40}

# 根据字典(dict)的键排序
&gt;&gt;&gt; print(dict(sorted(_dict.items(), key=lambda item: item[0])))
{<!-- -->'A': 10, 'B': 20, 'C': 30, 'D': 40}

# 根据字典(dict)的值排序
&gt;&gt;&gt; print(dict(sorted(_dict.items(), key=lambda item: item[1])))
{<!-- -->'A': 10, 'B': 20, 'C': 30, 'D': 40}

```

#### 复杂数据排序

接下来看看复杂的数据排序~
- 下面是相对复杂的一个**列表(list)**
```
_list = [
    {<!-- -->'age': 20, 'name': 'B', 'seasonal_salary': [10000, 20000, 30000, 6000]},
    {<!-- -->'age': 50, 'name': 'C', 'seasonal_salary': [90000, 20000, 30000, 10000]},
    {<!-- -->'age': 28, 'name': 'A', 'seasonal_salary': [50000, 20000, 30000, 40000]}
]

```

**按照年龄排序**
- `operator.itemgetter('key')`：返回**callable**对象，从操作数中获取**key**- 等同于 **print(sorted(_list, key=lambda item: item[‘age’]))**
```
&gt;&gt;&gt; print(sorted(_list, key=operator.itemgetter('age'))) 
[{<!-- -->'age': 20, 'name': 'B', 'seasonal_salary': [...]}, {<!-- -->'age': 28, 'name': 'A', 'seasonal_salary': [...]}, {<!-- -->'age': 50, 'name': 'C', 'seasonal_salary': [...]}]

```

**根据姓名排序**
- 等同于 **print(sorted(_list, key=lambda item: item[‘name’]))**
```
&gt;&gt;&gt; print(sorted(_list, key=operator.itemgetter('name')))
[{<!-- -->'age': 28, 'name': 'A', 'seasonal_salary': [...]}, {<!-- -->'age': 20, 'name': 'B', 'seasonal_salary': [...]}, {<!-- -->'age': 50, 'name': 'C', 'seasonal_salary': [...]}]

```

**根据总薪资排序**
- 这里只显示总和（太长了~~- 这一步无法使用**operator**，因为`sum()` 需要的是**iterable**对象，而不是**callable**对象
```
&gt;&gt;&gt; print(sorted(_list, key=lambda item: sum(item['seasonal_salary'])))
[{<!-- -->'age': 20, 'name': 'B', 'seasonal_salary': [66000]}, {<!-- -->'age': 28, 'name': 'A', 'seasonal_salary': [140000]}, {<!-- -->'age': 50, 'name': 'C', 'seasonal_salary': [150000]}]

```

#### 指定多个key

当然，也可以指定多个key来做排序，如：

```
import operator

# operator
sorted(_list, key=operator.itemgetter('field_1', 'field_2'))
# lambda
sorted(_list, key=lambda item: (item[field_1], item[field_2]))

```

## 后话

本次分享到此结束，🐱‍🏍🐱‍🏍 see you~
