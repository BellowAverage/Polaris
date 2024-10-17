
--- 
title:  Python学习笔记第四十九天(NumPy 矩阵库(Matrix)) 
tags: []
categories: [] 

---


#### Python学习笔记第四十九天
- - <ul><li>- - - - - 


## NumPy 矩阵库(Matrix)

NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵，而不是 ndarray 对象。

一个 的矩阵是一个由行（row）列（column）元素排列成的矩形阵列。

矩阵里的元素可以是数字、符号或数学式。以下是一个由 6 个数字元素构成的 2 行 3 列的矩阵：

<img src="https://img-blog.csdnimg.cn/c94a83e4b66c4fa181cc3a557a5395c3.png" alt="在这里插入图片描述">

### 转置矩阵

NumPy 中除了可以使用 numpy.transpose 函数来对换数组的维度，还可以使用 T 属性。。

例如有个 m 行 n 列的矩阵，使用 t() 函数就能转换为 n 行 m 列的矩阵。 <img src="https://img-blog.csdnimg.cn/6830569243914ee0ad785608d4dc452c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f60bb459fdd54537ac12a355473dd7b4.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5e9d421e5e994ccba27d0956f91b8383.png" alt="在这里插入图片描述"> **使用 t() 函数就能转换为 n 行 m 列的矩阵的过程** <img src="https://img-blog.csdnimg.cn/6f80dcb8b3f24832b3949390422f83ea.png" alt="在这里插入图片描述">

```
# 实例 1
import numpy as np
 
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('转置数组：')
print (a.T)

```

输出结果如下：

```
原数组：
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]


转置数组：
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]

```

### matlib.empty()

matlib.empty() 函数返回一个新的矩阵，语法格式为：

numpy.matlib.empty(shape, dtype, order) 参数说明：
- shape: 定义新矩阵形状的整数或整数元组- Dtype: 可选，数据类型- order: C（行序优先） 或者 F（列序优先）
```
# 实例 2
import numpy.matlib 
import numpy as np
 
print (np.matlib.empty((2,2)))
# 填充为随机数据

```

输出结果为：

```
[[-1.49166815e-154 -1.49166815e-154]
 [ 2.17371491e-313  2.52720790e-212]]
numpy.matlib.zeros()
numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵。

```

```
# 实例 3
import numpy.matlib 
import numpy as np 
 
print (np.matlib.zeros((2,2)))

```

输出结果为：

```
[[0. 0.]
 [0. 0.]]

```

### numpy.matlib.ones()

numpy.matlib.ones()函数创建一个以 1 填充的矩阵。

```
# 实例 4
import numpy.matlib 
import numpy as np 
 
print (np.matlib.ones((2,2)))

```

输出结果为：

```
[[1. 1.]
 [1. 1.]]

```

### numpy.matlib.eye()

numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零。

numpy.matlib.eye(n, M,k, dtype) 参数说明：
- n: 返回矩阵的行数- M: 返回矩阵的列数，默认为 n- k: 对角线的索引- dtype: 数据类型
```
# 实例 5
import numpy.matlib 
import numpy as np 
 
print (np.matlib.eye(n =  3, M =  4, k =  0, dtype =  float))

```

输出结果为：

```
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]]

```

### numpy.matlib.identity()

numpy.matlib.identity() 函数返回给定大小的单位矩阵。

单位矩阵是个方阵，从左上角到右下角的对角线（称为主对角线）上的元素均为 1，除此以外全都为 0。

```
# 实例 6
import numpy.matlib 
import numpy as np 
 
# 大小为 5，类型位浮点型
print (np.matlib.identity(5, dtype =  float))

```

输出结果为：

```
[[ 1.  0.  0.  0.  0.] 
 [ 0.  1.  0.  0.  0.] 
 [ 0.  0.  1.  0.  0.] 
 [ 0.  0.  0.  1.  0.] 
 [ 0.  0.  0.  0.  1.]]

```

### numpy.matlib.rand()

numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的。

```
# 实例 7
import numpy.matlib 
import numpy as np 
 
print (np.matlib.rand(3,3))

```

输出结果为：

```
[[0.23966718 0.16147628 0.14162   ]
 [0.28379085 0.59934741 0.62985825]
 [0.99527238 0.11137883 0.41105367]]

```

矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的。

```
# 实例 8
import numpy.matlib 
import numpy as np  
 
i = np.matrix('1,2;3,4')  
print (i)

```

输出结果为：

```
[[1  2] 
 [3  4]]
 ```python
# 实例 9
import numpy.matlib 
import numpy as np  
 
j = np.asarray(i)  
print (j)

```

输出结果为：

```
[[1  2] 
 [3  4]]

```

```
# 实例 10
import numpy.matlib 
import numpy as np  
 
k = np.asmatrix (j)  
print (k)

```

输出结果为：

```
[[1  2] 
 [3  4]]

```

## 结束语

今天学习的是PythonNumPy 矩阵库(Matrix)学会了吗。 今天学习内容总结一下：
1. 转置矩阵1. matlib.empty()1. numpy.matlib.ones()1. numpy.matlib.eye()1. numpy.matlib.identity()1. numpy.matlib.rand()