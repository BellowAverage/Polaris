
--- 
title:  Python学习笔记第五十四天（Pandas DataFrame） 
tags: []
categories: [] 

---


#### Python学习笔记第五十四天
- - <ul><li>- - - 


## Pandas 数据结构 - DataFrame

DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。

DataFrame 构造方法如下：

```
pandas.DataFrame( data, index, columns, dtype, copy)

```

参数说明：
- data：一组数据(ndarray、series, map, lists, dict 等类型)。- index：索引值，或者可以称为行标签。- columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。- dtype：数据类型。- copy：拷贝数据，默认为 False。- Pandas DataFrame 是一个二维的数组结构，类似二维数组。
### 使用列表创建

```
# 实例 1 
import pandas as pd
data = [['Google',10],['Facebook',12],['Wiki',13]]
df = pd.DataFrame(data,columns=['Site','Age'],dtype=float)
print(df)

```

在这个例子中，我们使用了一个包含三个列表的列表 data，每个内部列表包含两个元素。然后，我们使用 pd.DataFrame() 函数将这个列表转换为一个 DataFrame 对象，并指定列名为 ‘Site’ 和 ‘Age’，数据类型为浮点数。最后，我们打印这个 DataFrame 对象。

以下实例使用 ndarrays 创建，ndarray 的长度必须相同， 如果传递了 index，则索引的长度应等于数组的长度。如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度。

>  
 ndarrays 可以参考：NumPy Ndarray 对象 


### 使用 ndarrays 创建

```
# 实例 2
import pandas as pd
data = {<!-- -->'Site':['Google', 'Facebook', 'Wiki'], 'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print (df)

```

在这个例子中，我们使用了一个字典 data，其中键是列名，值是相应的 ndarrays。然后，我们使用 pd.DataFrame() 函数将这个字典转换为一个 DataFrame 对象。由于我们没有指定索引，因此默认情况下，索引将是 range(n)，其中 n 是数组的长度。最后，我们打印这个 DataFrame 对象。从输出结果可以知道， DataFrame 数据类型一个表格，包含 rows（行） 和 columns（列）。

>  
 还可以使用字典（key/value），其中字典的 key 为列名: 


### 使用字典创建

```
# 实例 3 
import pandas as pd
data = [{<!-- -->'a': 1, 'b': 2},{<!-- -->'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)

```

>  
 若没有对应的部分数据为 NaN。 


在这个例子中，我们使用了一个列表 data，其中包含了两个字典。然后，我们使用 pd.DataFrame() 函数将这个列表转换为一个 DataFrame 对象。由于我们没有指定索引，因此默认情况下，索引将是 range(n)，其中 n 是字典的个数。由于我们只提供了一个数据行，因此 DataFrame 对象是空的。最后，我们打印这个 DataFrame 对象。

Pandas 的 loc 方法用于选择 DataFrame 的行。在没有设置索引的情况下，索引默认从0开始，所以第一行的索引是0，第二行的索引是1，等等。

```
# 实例 4
import pandas as pd
data = {<!-- -->
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])

```

>  
 注意：返回结果其实就是一个 Pandas Series 数据。 


在返回的结果中，你可以看到每行的数据都被封装在一个 Series 中，而列的名字作为 Series 的索引。输出结果的 dtype 部分则表示该列的数据类型。

另外需要注意的是，如果 DataFrame 设置了索引，那么可以通过索引来选择行，而不仅仅是按照顺序选择。例如，如果你有一个 DataFrame，其索引是 [‘a’, ‘b’, ‘c’]，那么你可以通过 df.loc[‘a’] 选择索引为 ‘a’ 的行。

### 返回多行数

Pandas的loc方法确实可以用于选择多行。在你要选择的行索引之间用逗号隔开(使用 [[ … ]] 格式，… 为各行的索引，以逗号隔开)，就可以选择多行。例子中，df.loc[[0, 1]]将会选择索引为0和1的两行。

```
# 实例 5
import pandas as pd
data = {<!-- -->
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行和第二行
print(df.loc[[0, 1]])

```

>  
 返回结果其实就是一个 Pandas DataFrame 数据。 


在这个例子中，你可以看到选择了的数据已经按照原来的格式排列，即“行”是原来的行，“列”是原来的列。

那么我们可以指定索引值

```
# 实例 6
import pandas as pd
data = {<!-- -->
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

```

Pandas的loc方法可以用于根据索引来选择行。

```
# 实例 6
import pandas as pd
data = {<!-- -->
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# 指定索引
print(df.loc["day2"])

```

在这个例子中，df.loc[“day2”]将会选择索引为"day2"的行。你可以看到选择了的数据已经按照原来的格式排列，即“行”是原来的行，“列”是原来的列。只不过由于你这次选择的是根据索引而不是行号，所以结果中的行标签是"day2"。

## 后记

今天学习的是Python Pandas DataFrame学会了吗。 今天学习内容总结一下：
1. Pandas 数据结构 - DataFrame1. 使用列表创建1. 使用 ndarrays 创建1. 使用字典创建1. 返回多行数