
--- 
title:  Python学习笔记第五十五天（Pandas CSV文件） 
tags: []
categories: [] 

---


#### Python学习笔记第五十五天
- - <ul><li>- - - - - <ul><li>


## Pandas CSV 文件

CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。

CSV 是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。

### read_csv()

Pandas 可以很方便的处理 CSV 文件，本文以 data.csv 为例，你可以下载 data.csv 或打开 data.csv 查看。

```
# 实例 1
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())

```

### to_string()

to_string() 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 … 代替。

```
# 实例 2
import pandas as pd
df = pd.read_csv('data.csv')
print(df)

```

### to_csv()

我们也可以使用 to_csv() 方法将 DataFrame 存储为 csv 文件：

```
# 实例 3
import pandas as pd
# 三个字段 name, site, age
nme = ["Google", "Taobao", "Wiki"]
st = ["www.google.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 80, 98]
# 字典
dict = {<!-- -->'name': nme, 'site': st, 'age': ag}    
df = pd.DataFrame(dict)
# 保存 dataframe
df.to_csv('site.csv')

```

## 数据处理

### head()

head( n ) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行。

```
# 实例 5 
import pandas as pd
df = pd.read_csv('data.csv')
# 读取前面 5 行
print(df.head())

```

>  
 注意，head()默认返回的是前5行，如果你想改变默认行数，你可以通过head()函数中的参数n进行设置。此外，你需要首先导入pandas库并读取csv文件到DataFrame对象。 


```
# 实例 6
import pandas as pd
df = pd.read_csv('data.csv')
# 读取前面 10 行
print(df.head(10))

```

### tail()

tail( n ) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN。如果指定参数n，则返回最后n行。如果n大于DataFrame的行数，则返回全部的行。

```
# 实例 7
import pandas as pd
df = pd.read_csv('data.csv')
# 读取末尾 5 行
print(df.tail())

```

>  
 注意，实例中，已经正确使用了tail()方法来读取’data.csv’文件的最后5行。如果文件有足够的行数，那么tail()方法会返回最后5行数据。如果文件不足够长，那么返回的行数将与文件的实际行数相同。 另外，对于空行，Pandas将其各个字段的值返回NaN。如果你希望将空行视为具有特定值（例如0或’'）的行，你可以使用fillna()方法来填充缺失值。 


#### fillna()

```
# 实例 8
import pandas as pd
df = pd.read_csv('data.csv')
# 将空行填充为0
print(df.tail().fillna(0))

```

读取末尾 10 行也是一样的

```
# 实例 9
import pandas as pd
df = pd.read_csv('data.csv')
# 读取末尾 10 行
print(df.tail(10).fillna(0))

```

### info()

info()方法在Pandas库中主要用于输出DataFrame的相关信息。这包括行数、列数、非空值的数量以及每列的数据类型等。

当你在一个DataFrame对象上调用info()方法时，它会输出以下信息：
1. DataFrame的索引（行标签）的详细信息，包括最小值、最大值、唯一值和步长。1. DataFrame的列标签及其一些统计信息，包括数据类型、非空值的数量等。1. DataFrame的行数和列数。
```
# 实例 10
import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())

```

当你运行上述代码时，info()方法将输出类似以下的信息（具体内容取决于你的数据）举个例子如下：

```
&lt;class 'pandas.core.frame.DataFrame'&gt;  
RangeIndex: 500 entries, 0 to 499  	 		# 行数，500 行，第一行编号为 0
Data columns (total 13 columns): 			# 列数，13列
#   Column  Non-Null Count  Dtype   		# 各列的数据类型
---  ------  --------------  -----    
0   team    500 non-null    object  		# non-null，意思为非空的数据 
1   player  483 non-null    object  
2   pos     483 non-null    object  
3   age     483 non-null    float64  
4   height   483 non-null    float64  
...  
11  mp_mp   500 non-null    float64  
12  mp40     500 non-null    float64  
13  mp40g    498 non-null    float64  
dtypes: float64(7), int64(2), object(4)  	# 类型
memory usage: 49.3 KB

```

这个输出说明了：
- DataFrame的类别（在这个例子中是一个pandas DataFrame）和索引范围。- DataFrame的列数和非空值的数量。- 每列的非空值数量和数据类型。- 每列的缺失值数量（如果有的话）。- DataFrame使用的内存量。
## 后记

今天学习的是Python Pandas DataFrame学会了吗。 今天学习内容总结一下：
1. Pandas CSV 文件1. read_csv()1. to_string()1. to_csv()1. 数据处理1. head()1. tail()1. info()