
--- 
title:  Python 数据分析（一）：NumPy 基础知识 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- - <ul><li>- - - - - - 


### 1. 简介

NumPy（Numerical Python）是一个开源的 Python 科学计算扩展库，主要用来处理任意维度数组与矩阵，通常对于相同的计算任务，使用 NumPy 要比直接使用 Python 基本数据结构要简单、高效的多。安装使用 `pip install numpy` 命令即可。

### 2. 使用

#### 2.1 ndarray

ndarray 即 n 维数数组类型，它是一个相同数据类型的集合，以 0 下标为开始进行集合中元素的索引。

创建数组可以使用 NumPy 的 array 方法，具体格式如下：

**array(p_object, dtype=None, copy=True, order=‘K’, subok=False, ndmin=0)**
-  p_object：数组或嵌套的数列 -  dtype：数组元素的数据类型 -  copy：是否需要复制 -  order：创建数组的样式，C 为行方向，F 为列方向，A 为任意方向（默认） -  subok：默认返回一个与基类类型一致的数组 -  ndmin：生成数组的最小维度 
当然，还可以使用 arange 方法，下面看一下具体使用示例。

**创建数组**

看一下如何创建一维数组

```
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array(range(1, 6))
arr3 = np.arange(1, 6)
print (arr1)
print (arr2)
print (arr3)

```

看一下如何创建多维数组，以二维数组为例

```
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr)

```

**常用属性**

通过示例来看一下 ndarray 对象的常用属性

```
import numpy as np

arr = np.array([1, 2, 3])
# 元素类型
print(arr.dtype)
# 形状
print(arr.shape)
# 元素个数
print(arr.size)
# 维度
print(arr.ndim)
# 每个元素大小（字节）
print(arr.itemsize)

```

**改变数组的形状**

```
import numpy as np

arr = np.arange(30)
print(arr)
# 变成二维数组
arr.shape = (5, 6)
print(arr)
# 变成三维数组
arr = arr.reshape((2, 3, 5))
print(arr)

```

#### 2.2 数据类型

通过下表来看一下 NumPy 的常用数据类型。

<th align="left">类型</th><th align="left">描述</th>
|------
<td align="left">int_</td><td align="left">默认的整数类型（类似于 C 语言中的 long，int32 或 int64）</td>
<td align="left">intc</td><td align="left">与 C 的 int 类型一样，一般是 int32 或 int 64</td>
<td align="left">intp</td><td align="left">用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64）</td>
<td align="left">int8</td><td align="left">字节（-128 to 127）</td>
<td align="left">int16</td><td align="left">整数（-32768 to 32767）</td>
<td align="left">int32</td><td align="left">整数（-2147483648 to 2147483647）</td>
<td align="left">int64</td><td align="left">整数（-9223372036854775808 to 9223372036854775807）</td>
<td align="left">uint8</td><td align="left">无符号整数（0 to 255）</td>
<td align="left">uint16</td><td align="left">无符号整数（0 to 65535）</td>
<td align="left">uint32</td><td align="left">无符号整数（0 to 4294967295）</td>
<td align="left">uint64</td><td align="left">无符号整数（0 to 18446744073709551615）</td>
<td align="left">bool_</td><td align="left">布尔型数据类型（True 或者 False）</td>
<td align="left">float_</td><td align="left">float64 类型的简写</td>
<td align="left">float16</td><td align="left">半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位</td>
<td align="left">float32</td><td align="left">单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位</td>
<td align="left">float64</td><td align="left">双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位</td>
<td align="left">complex_</td><td align="left">complex128 类型的简写，即 128 位复数</td>
<td align="left">complex64</td><td align="left">复数，表示双 32 位浮点数（实数部分和虚数部分）</td>
<td align="left">complex128</td><td align="left">复数，表示双 64 位浮点数（实数部分和虚数部分）</td>

通过示例来看一下如何修改数据类型。

```
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1.111, 2.222, 3.333])
# 当前数据类型
print(arr1.dtype)
# 修改数据类型
arr1 = arr1.astype(np.int64)
print(arr1.dtype)
# 保留一位小数
arr2 = np.round(arr2, 1)
print(arr2)

```

#### 2.3 索引与切片

NumPy 数组支持索引、切片操作，还可以进行迭代，先看一下一维数组。

```
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[3])
# 修改元素值
arr[3] = 10
print(arr[3])
print(arr[2:])
print(arr[2:4])
print(arr[4:])
for i in arr:
    print(i)

```

再看一下多维数组的这些操作。

```
import numpy as np

arr = np.arange(12).reshape(3, 4)
print(arr)
# 取某一个值
print(arr[2, 3])
# 取多个不连续的值
print(arr[[0, 2],[1, 3]])
# 取一行
print(arr[0])
# 连续取多行
print(arr[1:])
# 取不连续的多行
print(arr[[0, 2]])
# 取一列
print(arr[:, 0])
# 连续取多列
print(arr[:, 2:])
# 取不连续的多列
print(arr[:, [0, 2]])

```

#### 2.4 副本与视图

视图（浅复制）只是原有数据的一个引用，通过该引用可访问、操作原有数据，如果我们对视图进行修改，它会影响原始数据，因为浅复制共享内存。

副本（深复制）是对数据的完整拷贝，如果我们对副本进行修改，它不会影响到原始数据，因为深复制不共享内存。

调用 ndarray 的 view() 方法会产生一个视图，下面通过示例来看一下。

```
import numpy as np

a = np.arange(6).reshape(2,3)
# 创建视图
b = a.view()
print('a的id：', id(a))
print('b的id：', id(b))
# 修改 b 的形状
b.shape =  3,2
print('a的形状：')
print(a)
print('b的形状：')
print(b)
print(a is b)

```

调用 ndarray 的 copy() 方法会产生一个副本，下面通过示例来看一下。

```
import numpy as np

a = np.arange(1, 6)
# 创建副本
b = a.copy()
print(a is b)
b[1] = 10
print(a[1])
print(b[1])

```

#### 2.5 轴的概念

NumPy 中的轴简单来说就是方向的意思，使用数字 0、1、2 表示，一维数组只有 0 轴，二维数组有 0、1 轴，三维数组有 0、1、2 轴，了解轴的相应概念可以方便我们进行相应计算。

#### 2.6 基本运算

**数组与数字之间运算**

看一下数组与数字之间的加、减、乘、除运算。

```
import numpy as np

arr = np.arange(12).reshape(3, 4)
print(arr + 3)
print(arr - 1)
print(arr * 2)
print(arr / 3)

```

**数组与数组之间运算**

看一下数组与数组之间的运算。

```
import numpy as np

# 相同行数，相同列数
a = np.arange(12).reshape(3, 4)
b = np.arange(20, 32).reshape(3, 4)
print(a + b)
print(b * a)
# 相同行数
c = np.arange(12).reshape(3, 4)
d = np.arange(3).reshape(3, 1)
print(c + d)
print(c - d)
# 相同列数
e = np.arange(12).reshape(4, 3)
f = np.arange(3).reshape(1, 3)
print(e * f)
print(e - f)

```

**常用数学运算**

```
import numpy as np

arr = np.array([[33, 55], [11, 66], [22, 99]])
print(arr)
# 最大值
print(np.max(arr))
# 最小值
print(np.min(arr))
# 某一轴上的最大值
print(np.max(arr, 1))
# 某一轴上的最小值
print(np.min(arr, 1))
# 平均值
print(np.mean(arr))
# 某一行、一列的平均值
print(np.mean(arr, axis=1))
# 最大值索引
print(np.argmax(arr))
print(np.argmax(arr, axis=1))
# 最小值索引
print(np.argmin(arr))
print(np.argmin(arr, axis=1))
# 极差
print(np.ptp(arr))
print(np.ptp(arr, axis=1))
# 方差
print(np.var(arr))
# 标准差
print(np.std(arr))
# 中位数
print(np.median(arr))

```

#### 2.7 常用操作

**添加操作**

NumPy 的 append() 方法可以在数组的末尾添加值，该操作会分配至整个数组，并把原数组复制到新数组，该操作需保证输入的维度匹配，下面看一下使用示例。

```
import numpy as np

arr = np.array([[1, 3, 5], [2, 4, 6]])
# 添加元素
print(np.append(arr, [1, 1, 3]))
# 沿 0 轴添加元素
print(np.append(arr, [[1, 1, 3]], axis=0))
# 沿 1 轴添加元素
print(np.append(arr, [[1, 1, 3], [2, 1, 5]], axis=1))

```

我们还可以使用 insert() 方法进行添加操作，该方法在给定索引前沿给定轴向数组中插入值，下面看一下使用示例。

```
import numpy as np

arr = np.array([[1, 3, 5], [2, 4, 6]])
# 添加元素
print(np.insert(arr, 1, [1, 1, 3]))
# 沿 0 轴添加元素
print(np.insert(arr, 1, [1, 1, 3], axis=0))
# 沿 1 轴添加元素
print(np.insert(arr, 1, [1, 5], axis=1))

```

**删除操作**

NumPy 的 delete() 可以对数组进行删除操作，下面看一下使用示例。

```
import numpy as np

arr = np.array([[1, 3, 5], [2, 4, 6]])
# 删除元素
print(np.delete(arr, 1))
# 沿 0 轴删除元素
print(np.delete(arr, 1, axis=0))
# 沿 1 轴删除元素
print(np.delete(arr, 1, axis=1))

```

**去重操作**

NumPy 的 unique() 方法可以去除数组中的重复元素。

```
import numpy as np

arr = np.array([1, 3, 5, 2, 4, 6, 1, 5, 3])
# 去除重复元素
print(np.unique(arr))
# 去重数组的索引数组
u, indices = np.unique(arr, return_index=True)
print(indices)
# 去重元素的重复数量
u, indices = np.unique(arr, return_counts=True)
print(indices)

```

<img src="https://img-blog.csdnimg.cn/20200215093746977.png#pic_center" alt="" width="500">
