
--- 
title:  Python学习笔记第二十九天(N维数组（ndarray）) 
tags: []
categories: [] 

---


#### Python学习笔记第二十九天
- - <ul><li>- - - - - - - - - - - 


## N维数组（ndarray）

一个ndarray是（通常为固定大小）具有相同类型和大小的项目的多维容器。尺寸和阵列中的项目的数量是由它的定义shape，它是一种tuple的Ñ指定每一维的尺寸非负整数。数组中项目的类型由单独的数据类型对象（dtype）指定，其中一个与每个ndarray相关联。

与Python中的其他容器对象一样，ndarray可以通过对数组建立索引或切片（使用N个整数）以及的方法和属性来访问和修改的内容 ndarray。

不同的ndarrays可以共享相同的数据，因此在一个中所做的更改ndarray可能在另一个中可见。也就是说，一个ndarray可以是另一个ndarray 的“视图”，并且它所引用的数据由“基本” ndarray处理。ndarrays也可以是Python strings或实现bufferor或array接口的对象所拥有的内存的视图。

例

一个大小为2 x 3的二维数组，由4个字节的整数元素组成：

```
&gt;&gt;&gt; x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
&gt;&gt;&gt; type(x)
&lt;type 'numpy.ndarray'&gt;
&gt;&gt;&gt; x.shape
(2, 3)
&gt;&gt;&gt; x.dtype
dtype('int32')

```

可以使用类似Python容器的语法对数组进行索引：

```
&gt;&gt;&gt; # The element of x in the *second* row, *third* column, namely, 6.
&gt;&gt;&gt; x[1, 2]

```

例如，切片可以产生数组的视图：

```
&gt;&gt;&gt; y = x[:,1]
&gt;&gt;&gt; y
array([2, 5])
&gt;&gt;&gt; y[0] = 9 # this also changes the corresponding element in x
&gt;&gt;&gt; y
array([9, 5])
&gt;&gt;&gt; x
array([[1, 9, 3],
       [4, 5, 6]])

```

### 构建阵列

可以使用数组创建例程中详细介绍的例程来构造新数组，也可以使用低级 ndarray构造函数来构造新数组 ：

||
|------
|ndarray（shape [，dtype，缓冲区，偏移量，…]）|数组对象表示固定大小项的多维同构数组。

### 索引阵列

可以使用扩展的Python切片语法索引数组 array[selection]。类似的语法也用于访问结构化数据类型的字段,也可以看看数组索引。

## ndarray的内部内存布局

类的实例ndarray由计算机存储器的连续一维段（由数组或某个其他对象拥有）组成，并与将N个 整数映射到块中某个项的位置的索引方案结合在一起。索引可以变化的范围由shape数组的指定。每个项目占用多少字节以及如何解释字节由与数组关联的数据类型对象定义。

内存段本质上是一维的，并且有许多不同的方案可以将N维数组的项安排在一维块中。NumPy是灵活的，ndarray 对象可以适应任何跨步索引方案。在跨步方案中，N维索引（n_0，n_1，…，n_ {N-1}） 对应于偏移量（以字节为单位）：

n _ {\ mathrm {offset}} = \ sum_ {k = 0} ^ {N-1} s_k n_k

从与数组关联的内存块的开头开始。在这里，s_k是指定strides数组的整数。的列优先顺序（使用，例如，在Fortran语言和Matlab的）和 行主顺序方案（在C中使用）都只是特定种跨距方案，并且对应于存储器可以的寻址由步幅：

s_k ^ {\ mathrm {column}} = \ mathrm {itemsize} \ prod_ {j = 0} ^ {k-1} d_j，\ quad s_k ^ {\ mathrm {row}} = \ mathrm {itemsize} \ prod_ { j = k + 1} ^ {N-1} d_j。

其中d_j = self.shape [j]。

C和Fortran顺序都是连续的，即 单段内存布局，其中可以通过索引的某种组合来访问内存块的每个部分。

尽管可以通过上述步幅来解决设置了相应标志的C风格和Fortran风格的连续数组，但实际步幅可能有所不同。在两种情况下可能会发生这种情况：

如果这样，则为任何合法索引。这意味着在偏移量公式中，因此 = self.strides [k]的值是任意的。self.shape[k] == 1index[k] == 0n_k = 0s_k n_k = 0s_k

如果数组没有元素（），则没有合法索引，并且不会使用步幅。没有元素的任何数组都可以视为C样式和Fortran样式的连续数组。self.size == 0

点1表示self和self.squeeze()始终具有相同的连续性和aligned标志值。这也意味着即使是高维数组也可以同时是C样式和Fortran样式连续的。

如果所有元素的内存偏移量和基本偏移量本身是self.itemsize的倍数，则认为数组是对齐的。了解 内存对齐方式可以在大多数硬件上提高性能。

注意

默认情况下，点（1）和（2）尚未应用。从NumPy 1.8.0开始，只有NPY_RELAXED_STRIDES_CHECKING=1在构建NumPy时定义了环境变量的情况下，才会一致地应用它们。最终，它将成为默认值。

您可以通过查看的值来检查在构建NumPy时是否启用了此选项。如果是，则您的NumPy已启用宽松的步幅检查。np.ones((10,1), order=‘C’).flags.f_contiguousTrue

警告

它不是通常认为 的C样式连续阵列或Fortran的风格连续阵列是真实的。self.strides[-1] == self.itemsizeself.strides[0] == self.itemsize

数据在新的ndarrays处于行主 （C）顺序，除非另有说明，但是，例如，基本阵列切片经常产生的观点 在不同的方案。

注意

NumPy中的几种算法适用于任意跨步数组。但是，某些算法需要单段数组。将不规则步距的数组传递给此类算法时，将自动创建一个副本。

### 阵列属性

数组属性反映了数组本身固有的信息。通常，通过数组的属性访问数组可以使您获得并且有时可以设置数组的固有属性，而无需创建新数组。公开的属性是数组的核心部分，只有其中一部分可以有意义地重置，而无需创建新的数组。每个属性的信息如下。

### 内存布局

以下属性包含有关阵列的内存布局的信息：

||
|------
|ndarray.flags|有关阵列的内存布局的信息。
|ndarray.shape|数组维度的元组。
|ndarray.strides|在遍历数组时在每个维度上步进的字节元组。
|ndarray.ndim|数组维数。
|ndarray.data|指向数组数据开头的Python缓冲区对象。
|ndarray.size|数组中元素的数量。
|ndarray.itemsize|一个数组元素的长度（以字节为单位）。
|ndarray.nbytes|数组元素消耗的总字节数。
|ndarray.base|如果内存来自其他对象，则为基础对象。

### 数据类型

也可以看看数据类型对象与数组关联的数据类型对象可以在dtype属性中找到 ：

||
|------
|ndarray.dtype|数组元素的数据类型。

### 其他属性

||
|------
|ndarray.T|转置数组。
|ndarray.real|数组的实部。
|ndarray.imag|数组的虚部。
|ndarray.flat|数组上的一维迭代器。
|ndarray.ctypes|一个用于简化数组与ctypes模块的交互的对象。

### 阵列接口

也可以看看阵列接口。

||
|------
|**array_interface**|数组接口的Python端
|**array_struct**|数组接口的C端

### ctypes外部功能接口

||
|------
|ndarray.ctypes|一个用于简化数组与ctypes模块的交互的对象。

## Array方法

一个ndarray对象具有上或与以某种方式在阵列，典型地返回一个数组结果操作的许多方法。这些方法将在下面简要说明。（每个方法的文档字符串都有更完整的描述。）

对于下面的方法，也有相应功能 numpy：all，any，argmax， argmin，argpartition，argsort，choose， clip，compress，copy，cumprod， cumsum，diagonal，imag，max， mean，min，nonzero，partition， prod，ptp，put，ravel，real， repeat，reshape，round， searchsorted，sort，squeeze，std， sum，swapaxes，take，trace， transpose，var。

### 阵列转换

||
|------
|ndarray.item（* args）|将数组的元素复制到标准Python标量并返回。
|ndarray.tolist（）|将数组作为a.ndimPython标量的-levels深度嵌套列表返回。
|ndarray.itemset（* args）|将标量插入数组中（如果可能，将标量强制转换为数组的dtype）
|ndarray.tostring（[订购]）|在数组中构造包含原始数据字节的Python字节。
|ndarray.tobytes（[订购]）|在数组中构造包含原始数据字节的Python字节。
|ndarray.tofile（fid [，sep，格式]）|将数组以文本或二进制形式写入文件（默认）。
|ndarray.dump（文件）|将数组的腌制转储到指定文件中。
|ndarray.dumps（）|以字符串形式返回数组的泡菜。
|ndarray.astype（dtype [，命令，转换，…]）|数组的副本，强制转换为指定的类型。
|ndarray.byteswap（[到位]）|交换数组元素的字节
|ndarray.copy（[订购]）|返回数组的副本。
|ndarray.view（[dtype，type]）|具有相同数据的数组的新视图。
|ndarray.getfield（dtype [，偏移量]）|以给定类型返回给定数组的字段。
|ndarray.setflags（[写，对齐，uic]）|分别设置数组标志WRITEABLE，ALIGNED（WRITEBACKIFCOPY和UPDATEIFCOPY）。
|ndarray.fill（值）|用标量值填充数组。

### 形状操作

对于整形，调整大小和转置，可以将单个元组参数替换为n将被解释为n元组的整数。

||
|------
|ndarray.reshape（形状[，顺序]）|返回包含具有新形状的相同数据的数组。
|ndarray.resize（new_shape [，refcheck]）|就地更改数组的形状和大小。
|ndarray.transpose（*轴）|返回轴已转置的数组视图。
|ndarray.swapaxes（轴1，轴2）|返回轴1和轴2互换的数组视图。
|ndarray.flatten（[订购]）|返回折叠成一维的数组副本。
|ndarray.ravel（[订购]）|返回一个展平的数组。
|ndarray.squeeze（[轴]）|从形状除去单维输入一个。

### 项目选择和操作

对于采用axis关键字的数组方法，默认为 None。如果axis为None，则将该数组视为一维数组。轴的任何其他值都表示应该进行操作的尺寸。

||
|------
|ndarray.take（索引[，轴，输出，模式]）|返回来自的元素构成的数组一个在给定的索引。
|ndarray.put（索引，值[，模式]）|为索引中的所有n设置。a.flat[n] = values[n]
|ndarray.repeat（重复[，轴]）|重复数组的元素。
|ndarray.choose（选择[，输出，模式]）|使用索引数组从一组选择中构造一个新数组。
|ndarray.sort（[轴，种类，顺序]）|就地排序数组。
|ndarray.argsort（[轴，种类，顺序]）|返回将对该数组进行排序的索引。
|ndarray.partition（kth [，轴，种类，顺序]）|重新排列数组中的元素，使第k个位置的元素的值处于排序数组中的位置。
|ndarray.argpartition（kth [，轴，种类，顺序]）|返回将对该数组进行分区的索引。
|ndarray.searchsorted（v [，侧面，分类器]）|查找应将v的元素插入到a中以保持顺序的索引。
|ndarray.nonzero（）|返回非零元素的索引。
|ndarray.compress（条件[，轴，出]]|沿给定轴返回此数组的选定切片。
|ndarray.diagonal（[偏移，轴1，轴2]）|返回指定的对角线。

### 计算

这些方法很多都采用名为axis的参数。在这种情况下

如果axis为None（默认值），则将该数组视为一维数组，并在整个数组上执行该操作。如果self是0维数组或数组标量，则此行为也是默认行为。（数组标量是类型/类float32，float64等的实例，而0维数组是仅包含一个数组标量的ndarray实例。）

如果axis是整数，则将在给定的轴上进行操作（针对可沿给定轴创建的每个1-D子数组）。

轴参数的示例

尺寸为3 x 3 x 3的3维数组，在其三个轴上各相加

```
&gt;&gt;&gt; x
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],
       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],
       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])
&gt;&gt;&gt; x.sum(axis=0)
array([[27, 30, 33],
       [36, 39, 42],
       [45, 48, 51]])
&gt;&gt;&gt; # for sum, axis is the first keyword, so we may omit it,
&gt;&gt;&gt; # specifying only its value
&gt;&gt;&gt; x.sum(0), x.sum(1), x.sum(2)
(array([[27, 30, 33],
        [36, 39, 42],
        [45, 48, 51]]),
 array([[ 9, 12, 15],
        [36, 39, 42],
        [63, 66, 69]]),
 array([[ 3, 12, 21],
        [30, 39, 48],
        [57, 66, 75]]))

```

参数dtype指定应进行归约运算（如求和）的数据类型。默认的reduce数据类型与self的数据类型相同。为避免溢出，使用较大的数据类型执行还原操作可能很有用。

对于几种方法，还可以提供可选的out参数，并将结果放入给定的输出数组中。该出 参数必须是ndarray与具有相同数目的元素。它可以具有不同的数据类型，在这种情况下将执行强制转换。

||
|------
|ndarray.max（[轴，出，keepdims，初始，…]）|沿给定轴返回最大值。
|ndarray.argmax（[轴，出]）|沿给定轴返回最大值的索引。
|ndarray.min（[轴，出，keepdims，初始，…]）|沿给定轴返回最小值。
|ndarray.argmin（[轴，出]）|返回最小值的索引沿给定轴线一个。
|ndarray.ptp（[轴，出，keepdims]）|沿给定轴的峰到峰（最大值-最小值）值。
|ndarray.clip（[最小，最大，输出]）|返回值限制为的数组。[min, max]
|ndarray.conj（）|将所有元素复数共轭。
|ndarray.round（[十进制，出]）|返回一个与舍入到小数的给定数目的每个元素。
|ndarray.trace（[偏移，轴1，轴2，dtype，输出]）|返回数组对角线的和。
|ndarray.sum（[轴，dtype，输出，keepdims，…]）|返回给定轴上数组元素的总和。
|ndarray.cumsum（[轴，dtype，输出]）|返回沿给定轴的元素的累加和。
|ndarray.mean（[轴，dtype，输出，keepdims]）|返回沿给定轴的数组元素的平均。
|ndarray.var（[轴，dtype，out，ddof，keepdims]）|返回沿给定轴的数组元素的方差。
|ndarray.std（[轴，dtype，out，ddof，keepdims]）|返回沿给定轴的数组元素的标准偏差。
|ndarray.prod（[轴，dtype，输出，keepdims，…]）|返回给定轴上数组元素的乘积
|ndarray.cumprod（[轴，dtype，输出]）|返回沿给定轴的元素的累积积。
|ndarray.all（[轴，出，keepdims]）|如果所有元素的评估结果为True，则返回True。
|ndarray.any（[轴，出，keepdims]）|如果任何元素，则返回true 一个评估为True。

## 算术，矩阵乘法和比较运算

的算术和比较运算ndarrays 被定义为按元素运算，并且通常将 ndarray对象作为结果。

每个算术运算（的+，-，*，/，//， %，divmod()，**或pow()，&lt;&lt;，&gt;&gt;，&amp;， ^，|，~）和比较（==，&lt;，&gt;， &lt;=，&gt;=，!=）等效于相应的通用功能（或ufunc的简称）中NumPy的。有关更多信息，请参见“ 通用函数 ”部分。

比较运算符：

||
|------
|ndarray.**lt**（自我，价值，/）|返回self &lt;值。
|ndarray.**le**（自我，价值，/）|返回self &lt;= value。
|ndarray.**gt**（自我，价值，/）|返回self&gt; value。
|ndarray.**ge**（自我，价值，/）|返回self&gt; = value。
|ndarray.**eq**（自我，价值，/）|返回self == value。
|ndarray.**ne**（自我，价值，/）|返回self！=值。

数组的真值（bool）：

||
|------
|ndarray.**bool**（自我，/）|自我！= 0

注意

数组的真值测试invoke ndarray.**bool**，如果数组中元素的数量大于1，则会引发错误，因为此类数组的真值不明确。使用.any()和 .all()代替在这种情况下的含义。（如果元素数为0，则数组的计算结果为False。）

一元运算：

||
|------
|ndarray.**neg**（自我，/）|-自
|ndarray.**pos**（自我，/）|+自我
|ndarray.**abs**（自）|

## 结束语

今天学习的是PythonN维数组(ndarray)学会了吗。 今天学习内容总结一下：
1. N维数组（ndarray）1. ndarray的内部内存布局1. Array方法1. 算术，矩阵乘法和比较运算