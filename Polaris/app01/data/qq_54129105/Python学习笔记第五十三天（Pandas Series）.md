
--- 
title:  Python学习笔记第五十三天（Pandas Series） 
tags: []
categories: [] 

---


#### Python学习笔记第五十三天
- - <ul><li>- - - 


## Pandas 数据结构 - Series

Pandas Series是一种类似于一维数组的对象，由一组数据（各种NumPy数据类型）以及一组与之相关的数据标签（即索引）组成。它仅由一组数据也可产生简单的Series对象。可以保存任何数据类型，注意，Series中的索引值是可以重复的。

Series 由索引（index）和列组成，函数如下：

```
pandas.Series( data, index, dtype, name, copy)

```

参数说明：
- data：一组数据(ndarray 类型)。- index：数据索引标签，如果不指定，默认从 0 开始。- dtype：数据类型，默认会自己判断。- name：设置名称。- copy：拷贝数据，默认为 False。
### 创建Series

```
# 实例 1
import pandas as pd
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)

```

这是一个简单的 Pandas Series 实例，其中 a 是一个包含三个整数的列表。通过传递给 pd.Series() 函数，这个列表被转换成了 Pandas Series 对象。输出的结果中，第一列显示的是索引值（从0开始），第二列显示的是与索引值对应的值。在这个例子中，索引值是整数，而对应的值也是整数。最后一行 dtype: int64 表示这个 Series 中的所有元素都是整数类型，且占用的字节大小为 64 位。

如果没有指定索引，Pandas Series的默认索引是从0开始的。因此，可以使用索引值来读取数据。在上面的示例中，创建了一个Pandas Series对象myvar，其中包含三个元素1、2和3。然后使用索引值1来读取myvar中的第二个元素，即输出2。

```
# 实例 2
import pandas as pd
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar[1])

```

### 指定索引值

```
# 实例 3
import pandas as pd
a = ["Google", "Facebook", "Wiki"]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

```

在这个例子中，我们指定了索引值，分别是 “x”、“y” 和 “z”。输出的结果中，第一列显示的是我们指定的索引值，第二列显示的是与索引值对应的值。

### 使用 key/value 对象来创建 Series

```
# 实例 4
import pandas as pd
sites = {<!-- -->1: "Google", 2: "Facebook", 3: "Wiki"}
myvar = pd.Series(sites)
print(myvar)

```

在这个例子中，字典的 key 变成了索引值。我们使用了一个字典 sites，其中字典的键是整数，值是字符串。然后，我们将这个字典传递给 pd.Series() 函数，创建了一个 Pandas Series 对象。输出的结果中，第一列显示的是字典的键，第二列显示的是与键对应的值。

如果我们只需要字典中的一部分数据，只需要指定需要数据的索引即可

```
# 实例 5
import pandas as pd
sites = {<!-- -->1: "Google", 2: "Facebook", 3: "Wiki"}
myvar = pd.Series(sites, index = [1, 2])
print(myvar)

```

在这个例子中，我们只指定了索引为 1 和 2 的数据，因此输出的结果中只包含索引为 1 和 2 的数据。

### 设置 Series 名称参数

```
# 实例 6
import pandas as pd
sites = {<!-- -->1: "Google", 2: "Facebook", 3: "Wiki"}
myvar = pd.Series(sites, index = [1, 2], name="Series-TEST" )
print(myvar)

```

在这个例子中，我们通过设置 name 参数为 “Series-TEST”，给 Series 对象设置了名称。输出的结果中，第一列显示的是我们设置的名称 “Series-TEST”。

## 后记

今天学习的是Python Pandas Series学会了吗。 今天学习内容总结一下：
1. Pandas 数据结构 - Series1. 创建Series1. 指定索引值1. 使用 key/value 对象来创建 Series1. 设置 Series 名称参数