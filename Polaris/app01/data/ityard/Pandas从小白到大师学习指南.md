
--- 
title:  Pandas从小白到大师学习指南 
tags: []
categories: [] 

---
>  
  作者：Rudolf Höhn 
  机器之心编译 
 

在本文中，作者从 Pandas 的简介开始，一步一步讲解了 Pandas 的发展现状、内存优化等问题。这是一篇最佳实践教程，既适合用过 Pandas 的读者，也适合没用过但想要上手的小白。

通过本文，你将有望发现一到多种用 pandas 编码的新方法。

本文包括以下内容：
- Pandas 发展现状- 内存优化- 索引- 方法链- 随机提示
在阅读本文时，我建议你阅读每个你不了解的函数的文档字符串（docstrings）。简单的 Google 搜索和几秒钟 Pandas 文档的阅读，都会使你的阅读体验更加愉快。

**Pandas 的定义和现状**

**什么是 Pandas？**

Pandas 是一个「开源的、有 BSD 开源协议的库，它为 Python 编程语言提供了高性能、易于使用的数据架构以及数据分析工具」。总之，它提供了被称为 DataFrame 和 Series（对那些使用 Panel 的人来说，它们已经被弃用了）的数据抽象，通过管理索引来快速访问数据、执行分析和转换运算，甚至可以绘图（用 matplotlib 后端）。

Pandas 的当前最新版本是 v0.25.0 

(https://github.com/pandas-dev/pandas/releases/tag/v0.25.0)

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOVpUVVVuNFFWWDk1R3NRSEkxemNjRHJSU1VmMVFaT3d0RHVqYnd4UFc4TFpSVHR0U3JqSldNZDJsY2NDUUZ0ZFZzRW9Yc3pybGxpYWcvNjQw?x-oss-process=image/format,png">

Pandas 正在逐步升级到 1.0 版，而为了达到这一目的，它改变了很多人们习以为常的细节。Pandas 的核心开发者之一 Marc Garcia 发表了一段非常有趣的演讲——「走向 Pandas 1.0」。

演讲链接：https://www.youtube.com/watch?v=hK6o_TDXXN8

用一句话来总结，Pandas v1.0 主要改善了稳定性（如时间序列）并删除了未使用的代码库（如 SparseDataFrame）。

**数据**

让我们开始吧！选择「1985 到 2016 年间每个国家的自杀率」作为玩具数据集。这个数据集足够简单，但也足以让你上手 Pandas。

数据集链接：https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016

在深入研究代码之前，如果你想重现结果，要先执行下面的代码准备数据，确保列名和类型是正确的。

```
import pandas as pd
import numpy as np
import os
# to download https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016


data_path = 'path/to/folder/'
df = (pd.read_csv(filepath_or_buffer=os.path.join(data_path, 'master.csv')) 
.rename(columns={'suicides/100k pop' : 'suicides_per_100k', ' gdp_for_year ($) ' : 'gdp_year',  'gdp_per_capita ($)' : 'gdp_capita', 'country-year' : 'country_year'}) 
.assign(gdp_year=lambda _df: _df['gdp_year'].str
.replace(',','').astype(np.int64)) )

```

提示：如果你读取了一个大文件，在 

read_csv（https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html）中参数设定为 chunksize=N，这会返回一个可以输出 DataFrame 对象的迭代器。

这里有一些关于这个数据集的描述：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOVpUVVVuNFFWWDk1R3NRSEkxemNjRFk4eDNOSmhESTYxZDA0TEVNMmdScmZPTjZtU3I4Vzc1WkFiVWs2UXZ4TG9iZzhsbjBjREdtdy82NDA?x-oss-process=image/format,png">

```
&gt;&gt;&gt; df.columnsIndex(['country', 'year', 'sex', 'age', 'suicides_no', 'population', 'suicides_per_100k', 'country_year', 'HDI for year', 'gdp_year', 'gdp_capita', 'generation'], dtype='object')

```

这里有 101 个国家、年份从 1985 到 2016、两种性别、六个年代以及六个年龄组。有一些获得这些信息的方法：

可以用 unique() 和 nunique() 获取列内唯一的值（或唯一值的数量）；

```
&gt;&gt;&gt; df['generation'].unique()
array(['Generation X', 'Silent', 'G.I. Generation', 'Boomers', 'Millenials', 'Generation Z'], dtype=object)
&gt;&gt;&gt; df['country'].nunique()
101

```

可以用 describe() 输出每一列不同的统计数据（例如最小值、最大值、平均值、总数等），如果指定 include='all'，会针对每一列目标输出唯一元素的数量和出现最多元素的数量；

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOVpUVVVuNFFWWDk1R3NRSEkxemNjRHFzeHZQYWFPd2Q2T0JvMVNFeUtNR0RCelpzZ1hYV2Nud2FKU0w2a2FpY2FjM1A3emprZW53UVEvNjQw?x-oss-process=image/format,png">

可以用 head() 和 tail() 来可视化数据框的一小部分。

通过这些方法，你可以迅速了解正在分析的表格文件。

**内存优化**

在处理数据之前，了解数据并为数据框的每一列选择合适的类型是很重要的一步。

在内部，Pandas 将数据框存储为不同类型的 numpy 数组（比如一个 float64 矩阵，一个 int32 矩阵）。

有两种可以大幅降低内存消耗的方法。

```
import pandas as pd


def mem_usage(df: pd.DataFrame) -&gt; str: 
"""This method styles the memory usage of a DataFrame to be readable as MB. Parameters ---------- df: pd.DataFrame Data frame to measure. Returns ------- str Complete memory usage as a string formatted for MB. """ 
    return f'{df.memory_usage(deep=True).sum() / 1024 ** 2 : 3.2f} MB'


def convert_df(df: pd.DataFrame, deep_copy: bool = True) -&gt; pd.DataFrame: 
"""Automatically converts columns that are worth stored as ``categorical`` dtype. Parameters ---------- df: pd.DataFrame Data frame to convert. deep_copy: bool Whether or not to perform a deep copy of the original data frame. Returns ------- pd.DataFrame Optimized copy of the input data frame. """ 
    return df.copy(deep=deep_copy).astype({ col: 'category' for col in df.columns if df[col].nunique() / df[col].shape[0] &lt; 0.5})

```

Pandas 提出了一种叫做 memory_usage() 的方法，这种方法可以分析数据框的内存消耗。在代码中，指定 deep=True 来确保考虑到了实际的系统使用情况。

memory_usage()：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.memory_usage.html

了解列的类型

https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics-dtypes

很重要。它可以通过两种简单的方法节省高达 90% 的内存使用：
- 了解数据框使用的类型；- 了解数据框可以使用哪种类型来减少内存的使用（例如，price 这一列值在 0 到 59 之间，只带有一位小数，使用 float64 类型可能会产生不必要的内存开销）
除了降低数值类型的大小（用 int32 而不是 int64）外，Pandas 还提出了分类类型：https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html

>  
  如果你是用 R 语言的开发人员，你可能觉得它和 factor 类型是一样的。 
 

这种分类类型允许用索引替换重复值，还可以把实际值存在其他位置。教科书中的例子是国家。和多次存储相同的字符串「瑞士」或「波兰」比起来，为什么不简单地用 0 和 1 替换它们，并存储在字典中呢？

```
categorical_dict = {0: 'Switzerland', 1: 'Poland'}

```

Pandas 做了几乎相同的工作，同时添加了所有的方法，可以实际使用这种类型，并且仍然能够显示国家的名称。

回到 convert_df() 方法，如果这一列中的唯一值小于 50%，它会自动将列类型转换成 category。这个数是任意的，但是因为数据框中类型的转换意味着在 numpy 数组间移动数据，因此我们得到的必须比失去的多。

接下来看看数据中会发生什么。

```
&gt;&gt;&gt; mem_usage(df)
10.28 MB
&gt;&gt;&gt; mem_usage(df.set_index(['country', 'year', 'sex', 'age']))
5.00 MB
&gt;&gt;&gt; mem_usage(convert_df(df))
1.40 MB
&gt;&gt;&gt; mem_usage(convert_df(df.set_index(['country', 'year', 'sex', 'age'])))
1.40 MB



```

通过使用「智能」转换器，数据框使用的内存几乎减少了 10 倍（准确地说是 7.34 倍）。

**索引**

Pandas 是强大的，但也需要付出一些代价。当你加载 DataFrame 时，它会创建索引并将数据存储在 numpy 数组中。这是什么意思？一旦加载了数据框，只要正确管理索引，就可以快速地访问数据。

访问数据的方法主要有两种，分别是通过索引和查询访问。根据具体情况，你只能选择其中一种。但在大多数情况中，索引（和多索引）都是最好的选择。我们来看下面的例子：

```
&gt;&gt;&gt; %%time
&gt;&gt;&gt; df.query('country == "Albania" and year == 1987 and sex == "male" and age == "25-34 years"')
CPU times: user 7.27 ms, sys: 751 µs, total: 8.02 ms
# ==================
&gt;&gt;&gt; %%time
&gt;&gt;&gt; mi_df.loc['Albania', 1987, 'male', '25-34 years']
CPU times: user 459 µs, sys: 1 µs, total: 460 µs

```

什么？加速 20 倍？

你要问自己了，创建这个多索引要多长时间？

```
%%time
mi_df = df.set_index(['country', 'year', 'sex', 'age'])
CPU times: user 10.8 ms, sys: 2.2 ms, total: 13 ms

```

通过查询访问数据的时间是 1.5 倍。如果你只想检索一次数据（这种情况很少发生），查询是正确的方法。否则，你一定要坚持用索引，CPU 会为此感激你的。

.set_index(drop=False) 允许不删除用作新索引的列。

.loc[]/.iloc[] 方法可以很好地读取数据框，但无法修改数据框。如果需要手动构建（比如使用循环），那就要考虑其他的数据结构了（比如字典、列表等），在准备好所有数据后，创建 DataFrame。否则，对于 DataFrame 中的每一个新行，Pandas 都会更新索引，这可不是简单的哈希映射。

```
&gt;&gt;&gt; (pd.DataFrame({'a':range(2), 'b': range(2)}, index=['a', 'a']) .loc['a']) 
  a b
a 0 0
a 1 1

```

因此，未排序的索引可以降低性能。为了检查索引是否已经排序并对它排序，主要有两种方法：

```
%%time
&gt;&gt;&gt; mi_df.sort_index()
CPU times: user 34.8 ms, sys: 1.63 ms, total: 36.5 ms
&gt;&gt;&gt; mi_df.index.is_monotonicTrue

```

更多详情请参阅：
- Pandas 高级索引用户指南：https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html；- Pandas 库中的索引代码：https://github.com/pandas-dev/pandas/blob/master/pandas/core/indexing.py。
**方法链**

使用 DataFrame 的方法链是链接多个返回 DataFrame 方法的行为，因此它们都是来自 DataFrame 类的方法。在现在的 Pandas 版本中，使用方法链是为了不存储中间变量并避免出现如下情况：

```
import numpy as np
import pandas as pd
df = pd.DataFrame({'a_column': [1, -999, -999], 'powerless_column': [2, 3, 4], 'int_column': [1, 1, -1]}) 
df['a_column'] = df['a_column'].replace(-999, np.nan) 
df['power_column'] = df['powerless_column'] ** 2 
df['real_column'] = df['int_column'].astype(np.float64) 
df = df.apply(lambda _df: _df.replace(4, np.nan)) 
df = df.dropna(how='all')

```

用下面的链替换：

```
df = (pd.DataFrame({'a_column': [1, -999, -999], 
'powerless_column': [2, 3, 4], 
'int_column': [1, 1, -1]}) 
.assign(a_column=lambda _df: _df['a_column'].replace(-999, np.nan)) 
.assign(power_column=lambda _df: _df['powerless_column'] ** 2) 
.assign(real_column=lambda _df: _df['int_column'].astype(np.float64)) 
.apply(lambda _df: _df.replace(4, np.nan)) 
.dropna(how='all') )

```

说实话，第二段代码更漂亮也更简洁。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOVpUVVVuNFFWWDk1R3NRSEkxemNjRFlGcTFjVXdraWJDRWlieDVIUTJta1loUjFpY25oVzE2cktQaWJISFNTUjJ0Sk1oMzNYaWI4VFZnenR3LzY0MA?x-oss-process=image/format,png">

方法链的工具箱是由不同的方法（比如 apply、assign、loc、query、pipe、groupby 以及 agg）组成的，这些方法的输出都是 DataFrame 对象或 Series 对象（或 DataFrameGroupBy）。

了解它们最好的方法就是实际使用。举个简单的例子：

```
(df 
.groupby('age') 
.agg({'generation':'unique'}) 
.rename(columns={'generation':'unique_generation'})
# Recommended from v0.25
# .agg(unique_generation=('generation', 'unique')))

```

**获得每个年龄范围中所有唯一年代标签的简单链**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOVpUVVVuNFFWWDk1R3NRSEkxemNjRFBGT0xyRnpVZlJ0WGRiVHZMUHh3aWFmN1R5YllTa1NrdWFCOUI2aWNBakh1ODBwbWlhVGw2a2RpY1EvNjQw?x-oss-process=image/format,png">

**在得到的数据框中，「年龄」列是索引。**

除了了解到「X 代」覆盖了三个年龄组外，分解这条链。第一步是对年龄组分组。这一方法返回了一个 DataFrameGroupBy 对象，在这个对象中，通过选择组的唯一年代标签聚合了每一组。

在这种情况下，聚合方法是「unique」方法，但它也可以接受任何（匿名）函数。

在 0.25 版本中，Pandas 引入了使用 agg 的新方法：

https://dev.pandas.io/whatsnew/v0.25.0.html#groupby-aggregation-with-relabeling。

```
(df 
.groupby(['country', 'year']) 
.agg({'suicides_per_100k': 'sum'}) 
.rename(columns={'suicides_per_100k':'suicides_sum'})
# Recommended from v0.25
# .agg(suicides_sum=('suicides_per_100k', 'sum')) .sort_values('suicides_sum', ascending=False) .head(10))

```

**用排序值（sort_values）和 head 得到自杀率排前十的国家和年份**

```
(df 
.groupby(['country', 'year']) 
.agg({'suicides_per_100k': 'sum'}) 
.rename(columns={'suicides_per_100k':'suicides_sum'})
# Recommended from v0.25
# .agg(suicides_sum=('suicides_per_100k', 'sum')) 
.nlargest(10, columns='suicides_sum'))

```

**用排序值 nlargest 得到自杀率排前十的国家和年份**

在这些例子中，输出都是一样的：有两个指标（国家和年份）的 MultiIndex 的 DataFrame，还有包含排序后的 10 个最大值的新列 suicides_sum。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOVpUVVVuNFFWWDk1R3NRSEkxemNjREF3emJlcGFKbkthWHdKaWEycGpFcXRuQWpUUjZybWFkVENXQ2ljYnZoeUwxVzJwNkpTT2xENk9BLzY0MA?x-oss-process=image/format,png">

**「国家」和「年份」列是索引。**

nlargest(10) 比 sort_values(ascending=False).head(10) 更有效。

另一个有趣的方法是 unstack：

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html，这种方法允许转动索引水平。

```
(mi_df 
.loc[('Switzerland', 2000)] 
.unstack('sex') [['suicides_no', 'population']])

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOVpUVVVuNFFWWDk1R3NRSEkxemNjRHZLZkV5aWJEUkd6V09XM3BhRnBRNzFmREN4WGljVWlhRWVHeXZUT28yRk5ZMjZVRTlac0xxQXJYdy82NDA?x-oss-process=image/format,png">

**「age」是索引，列「suicides_no」和「population」都有第二个水平列「sex」。**

下一个方法 pipe 是最通用的方法之一。这种方法允许管道运算（就像在 shell 脚本中）执行比链更多的运算。

管道的一个简单但强大的用法是记录不同的信息。

```
def log_head(df, head_count=10): 
    print(df.head(head_count)) 
    return df


def log_columns(df): 
    print(df.columns) 
    return df


def log_shape(df): 
    print(f'shape = {df.shape}') 
    return df

```

**和 pipe 一起使用的不同记录函数。**

举个例子，我们想验证和 year 列相比，country_year 是否正确：

```
(df 
.assign(valid_cy=lambda _serie: _serie.apply( 
lambda _row: re.split(r'(?=\d{4})', 
_row['country_year'])[1] == str(_row['year']), axis=1)) 
.query('valid_cy == False') 
.pipe(log_shape))

```

**用来验证「country_year」列中年份的管道。**

管道的输出是 DataFrame，但它也可以在标准输出（console/REPL）中打印。

```
shape = (0, 13)

```

你也可以在一条链中用不同的 pipe。

```
(df .pipe(log_shape) 
.query('sex == "female"') 
.groupby(['year', 'country']) 
.agg({'suicides_per_100k':'sum'}) 
.pipe(log_shape) 
.rename(columns={'suicides_per_100k':'sum_suicides_per_100k_female'})
# Recommended from v0.25
# .agg(sum_suicides_per_100k_female=('suicides_per_100k', 'sum')) 
.nlargest(n=10, columns=['sum_suicides_per_100k_female']))

```

**女性自杀数量最高的国家和年份。**

生成的 DataFrame 如下所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOVpUVVVuNFFWWDk1R3NRSEkxemNjRDBuNExmdWFwaWFWamF0aEtiMWFQZWdpY2VVMGFBaHlUcUJhb2JTTkhJZFBNQWgzQ0VlMlVhZlhRLzY0MA?x-oss-process=image/format,png">

**索引是「年份」和「国家」。**

标准输出的打印如下所示：

```
shape = (27820, 12)
shape = (2321, 1)

```

除了记录到控制台外，pipe 还可以直接在数据框的列上应用函数。

```
from sklearn.preprocessing import MinMaxScaler


def norm_df(df, columns): 
    return df.assign(**{col: MinMaxScaler().fit_transform(df[[col]].values.astype(float))  
    for col in columns})  


for sex in ['male', 'female']: 
    print(sex) 
    print( df .query(f'sex == "{sex}"') 
    .groupby(['country']) 
    .agg({'suicides_per_100k': 'sum', 'gdp_year': 'mean'}) 
    .rename(columns={'suicides_per_100k':'suicides_per_100k_sum',  'gdp_year': 'gdp_year_mean'})
    # Recommended in v0.25
    # .agg(suicides_per_100k=('suicides_per_100k_sum', 'sum'), 
    # gdp_year=('gdp_year_mean', 'mean')) 
    .pipe(norm_df, columns=['suicides_per_100k_sum', 'gdp_year_mean']) 
    .corr(method='spearman') ) 
    print('\n')

```

**自杀数量是否和 GDP 的下降相关？****是否和性别相关？**

上面的代码在控制台中的打印如下所示：

```
male
                    suicides_per_100k_sum gdp_year_mean
suicides_per_100k_sum       1.000000         0.421218
gdp_year_mean               0.421218         1.000000



```

```
female
                     suicides_per_100k_sum gdp_year_mean
suicides_per_100k_sum        1.000000         0.452343
gdp_year_mean                0.452343         1.000000



```

深入研究代码。norm_df() 将一个 DataFrame 和用 MinMaxScaling 扩展列的列表当做输入。使用字典理解，创建一个字典 {column_name: method, …}，然后将其解压为 assign() 函数的参数 (colunmn_name=method, …)。

在这种特殊情况下，min-max 缩放不会改变对应的输出：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html，它仅用于参数。

在（遥远的？）未来，缓式评估（lazy evaluation）可能出现在方法链中，所以在链上做一些投资可能是一个好想法。

**最后（随机）的技巧**

下面的提示很有用，但不适用于前面的任何部分：

itertuples() 可以更高效地遍历数据框的行；

```
&gt;&gt;&gt; %%time
&gt;&gt;&gt; for row in df.iterrows(): continue
CPU times: user 1.97 s, sys: 17.3 ms, total: 1.99 s
&gt;&gt;&gt; for tup in df.itertuples(): continue
CPU times: user 55.9 ms, sys: 2.85 ms, total: 58.8 ms

```

注意：tup 是一个 namedtuple

join() 用了 merge()；

在 Jupyter 笔记本中，在代码块的开头写上 %%time，可以有效地测量时间；

UInt8 类：https://pandas.pydata.org/pandas-docs/stable/user_guide/gotchas.html#support-for-integer-na支持带有整数的 NaN 值；

记住，任何密集的 I/O（例如展开大型 CSV 存储）用低级方法都会执行得更好（尽可能多地用 Python 的核心函数）。

还有一些本文没有涉及到的有用的方法和数据结构，这些方法和数据结构都很值得花时间去理解：

数据透视表：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html?source=post_page

时间序列/日期功能：https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html?source=post_page

绘图：https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html?source=post_page

**总结**

希望你可以因为这篇简短的文章，更好地理解 Pandas 背后的工作原理，以及 Pandas 库的发展现状。本文还展示了不同的用于优化数据框内存以及快速分析数据的工具。希望对现在的你来说，索引和查找的概念能更加清晰。最后，你还可以试着用方法链写更长的链。

这里还有一些笔记：https://github.com/unit8co/medium-pandas-wan?source=post_page

除了文中的所有代码外，还包括简单数据索引数据框（df）和多索引数据框（mi_df）性能的定时指标。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOVpUVVVuNFFWWDk1R3NRSEkxemNjRHZvT3hRVlkxU3cwNkZBa3ZIMDNVc0ZVam9mNzNLak54WTdPczN2bnlzRlBpY2E4N3BOZWZ3VGcvNjQw?x-oss-process=image/format,png">

熟能生巧，所以继续修炼技能，并帮助我们建立一个更好的世界吧。

PS：有时候纯用 Numpy 会更快。

**原文链接：https://medium.com/unit8-machine-learning-publication/from-pandas-wan-to-pandas-master-4860cf0ce442**

PS：如果觉得分享内容有一些帮助，欢迎大家随手分享、点赞、在看。

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">
