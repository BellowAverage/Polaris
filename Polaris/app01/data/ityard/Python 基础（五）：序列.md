
--- 
title:  Python 基础（五）：序列 
tags: []
categories: [] 

---


#### 目录
- - - <ul><li>- - - - - 


## 1 简介

Python 中的序列是一块可存放多个值的连续内存空间，所有值按一定顺序排列，每个值所在位置都有一个编号，称其为索引，我们可以通过索引访问其对应值。

我们上一节说的就是序列结构，除此之外常见的序列结构还包括列表、元组等。

## 2 基本使用

### 2.1 索引

序列索引支持非负数和负数，索引为非负数，从 `0` 开始，如下所示：

<img src="https://img-blog.csdnimg.cn/20191106213703471.PNG#pic_center" alt="在这里插入图片描述" width="400"> 索引为负数由右向左计数，从 `-1` 开始，如图所示：

<img src="https://img-blog.csdnimg.cn/20191107080326981.png#pic_center" alt="" width="400"> 下面通过一个示例作进一步了解，以字符串为例，如下所示：

```
str = 'Python'
print('str[0] str[-6] =', str[0], str[-6])
print('str[5] str[-1] =', str[5], str[-1])

```

输出结果：

```
str[0] str[-6] = P P
str[5] str[-1] = n n

```

从结果来看，我们使用非负数索引与负数索引得到的结果一致。

### 2.2 切片

切片操作可以访问一定范围内的元素，语法如下所示：

`sname[start : end : step]`
- sname：表示序列的名称；- start：开始索引位置（包括该位置），默认为 0；- end：表示切片的结束索引位置（不包括该位置），默认为序列的长度；- step：步长。
以字符串为例，如下所示：

```
str = 'Python'
print(str[:3])
print(str[3:])
print(str[:])

```

输出结果：

```
Pyt
hon
Python

```

### 2.3 相加

Python 支持类型相同的序列使用 `+` 作相加操作，该操作不会去除重复的元素。以字符串为例，如下所示：

```
str1 = 'Python'
str2 = 'Python'
print('str1 + str2 --&gt; ',str1 + str2)

```

输出结果：

```
str1 + str2 --&gt;  PythonPython

```

### 2.4 相乘

Python 中，使用数字 n 乘以一个序列会生成新的序列，内容为原来序列被重复 n 次的结果。以字符串为例，如下所示：

```
str = 'Python'
print('2 * str --&gt; ',2 * str)

```

输出结果：

```
2 * str --&gt;  PythonPython

```

### 2.5 检查元素是否包含在序列中

Python 使用 `in` 关键字检查某元素是否为序列的成员，语法如下：

`val in seq`
- val：要检查的元素；- seq：指定的序列。
通过一个例子作进一步了解，以字符串为例，如下所示：

```
str = 'Python'
print('on'in str)

```

输出结果：

```
True

```

### 2.6 内置函数

<th align="left">函数</th>|描述
|------
<td align="left">len()</td>|计算序列的长度
<td align="left">max()</td>|找出序列中的最大元素
<td align="left">min()</td>|找出序列中的最小元素
<td align="left">list()</td>|将序列转换为列表
<td align="left">str()</td>|将序列转换为字符串
<td align="left">sum()</td>|计算元素的和
<td align="left">sorted()</td>|对元素进行排序
<td align="left">enumerate()</td>|将序列组合为一个索引序列，多用在 for 循环中

简单举几个例子，如下所示：

```
str = 'dbcae'
print('len --&gt;', len(str))
print('max --&gt;', max(str))
print('sorted --&gt;', sorted(str))

```

输出结果：

```
len --&gt; 5
max --&gt; e
sorted --&gt; ['a', 'b', 'c', 'd', 'e']

```

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="335">
