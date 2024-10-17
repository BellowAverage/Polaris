
--- 
title:  系统性的学会 Pandas 看这一篇就够了 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/f4d3a23d274b0e1cf54b9120103ae948.png">

>  
  作者：Ma Sizhou  
  https://blog.csdn.net/weixin_45901519/article/details/112980822 
 

## 1、Pandas数据结构
- 2008年WesMcKinney开发出的库- 专门用于数据挖掘的开源python库- 以Numpy为基础，借力Numpy模块在计算方面性能高的优势- 基于matplotlib，能够简便的画图- 独特的数据结构
### 1.1 为什么使用Pandas

Numpy已经能够帮助我们处理数据，能够结合matplotlib解决部分数据展示等问题，那么pandas学习的目的在什么地方呢？
- （1）增强图表可读性- <ul><li>在numpy当中创建学生成绩表样式：- 返回结果：
```
array([[92, 55, 78, 50, 50],
       [71, 76, 50, 48, 96],
       [45, 84, 78, 51, 68],
       [81, 91, 56, 54, 76],
       [86, 66, 77, 67, 95],
       [46, 86, 56, 61, 99],
       [46, 95, 44, 46, 56],
       [80, 50, 45, 65, 57],
       [41, 93, 90, 41, 97],
       [65, 83, 57, 57, 40]])

```

如果数据展示为这样，可读性就会更友好：<img src="https://img-blog.csdnimg.cn/img_convert/3259d21e6ad15a78543a941862b3c386.png">
- （2）便捷的数据处理能力<img src="https://img-blog.csdnimg.cn/img_convert/15b9842d39b56f7fb61f28bdc5b39078.png">- （3）读取文件方便- （4）封装了Matplotlib、Numpy的画图和计算
### 1.2 Pandas数据结构

Pandas中一共有三种数据结构，分别为：Series、DataFrame和MultiIndex（老版本中叫Panel ）。

其中Series是一维数据结构，DataFrame是二维的表格型数据结构，MultiIndex是三维的数据结构。

#### 1.2.1 Series

Series是一个类似于一维数组的数据结构，它能够保存任何类型的数据，比如整数、字符串、浮点数等，主要由一组数据和与之相关的索引两部分构成。<img src="https://img-blog.csdnimg.cn/img_convert/e5dd844c8bfcad567901db2cb8dc861f.png">

##### （1）Series的创建

```
# 导入pandas
import pandas as pd

pd.Series(data=None, index=None, dtype=None)

```
- 参数：- <ul><li>data：传入的数据，可以是ndarray、list等- index：索引，必须是唯一的，且与数据的长度相等。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。- dtype：数据的类型
**通过已有数据创建:**
- （1）指定内容，默认索引：
```
pd.Series(np.arange(10))

```

```
# 运行结果
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
9    9
dtype: int64

```
- （2）指定索引：
```
pd.Series([6.7,5.6,3,10,2], index=[1,2,3,4,5])

```

```
# 运行结果
1     6.7
2     5.6
3     3.0
4    10.0
5     2.0
dtype: float64

```
- （3）通过字典数据创建
```
color_count = pd.Series({'red':100, 'blue':200, 'green': 500, 'yellow':1000})
color_count

```

```
# 运行结果
blue       200
green      500
red        100
yellow    1000
dtype: int64

```

##### （2）Series的属性

为了更方便地操作Series对象中的索引和数据，Series中提供了两个属性index和values：
- index：
```
color_count = pd.Series({'red':100, 'blue':200, 'green': 500, 'yellow':1000})

color_count.index

# 结果
Index(['blue', 'green', 'red', 'yellow'], dtype='object')

```
- values：
```
color_count.values

# 结果
array([ 200,  500,  100, 1000])

```

也可以使用索引来获取数据：

```
color_count[2]

# 结果
100

```

#### 1.2.2 DataFrame

DataFrame是一个类似于二维数组或表格(如excel)的对象，既有行索引，又有列索引：
- 行索引，表明不同行，横向索引，叫index，0轴，axis=0- 列索引，表名不同列，纵向索引，叫columns，1轴，axis=1<img src="https://img-blog.csdnimg.cn/img_convert/c2ba8339c5275f1210d8aa2f75ffbb01.png">
##### （1）DataFrame的创建

```
# 导入pandas
import pandas as pd

pd.DataFrame(data=None, index=None, columns=None)

```
- 参数：- <ul><li>index：行标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。- columns：列标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
通过已有数据创建

**举例一：**

```
pd.DataFrame(np.random.randn(2,3))

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/867484bb195441de330fe54dd123e119.png">**举例二：创建学生成绩表**

使用np创建的数组显示方式，比较两者的区别。

```
# 生成10名同学，5门功课的数据
score = np.random.randint(40, 100, (10, 5))#均匀分布

# 结果
array([[92, 55, 78, 50, 50],
       [71, 76, 50, 48, 96],
       [45, 84, 78, 51, 68],
       [81, 91, 56, 54, 76],
       [86, 66, 77, 67, 95],
       [46, 86, 56, 61, 99],
       [46, 95, 44, 46, 56],
       [80, 50, 45, 65, 57],
       [41, 93, 90, 41, 97],
       [65, 83, 57, 57, 40]])

```

**但是这样的数据形式很难看到存储的是什么的样的数据，可读性比较差！！**

**问题：如何让数据更有意义的显示？**

```
# 使用Pandas中的数据结构
score_df = pd.DataFrame(score)

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/9471ad3f75a89f27b8875e265c2be802.png">给分数数据增加行列索引,显示效果更佳：
- 增加行、列索引：
```
# 构造行索引序列
subjects = ["语文", "数学", "英语", "政治", "体育"]

# 构造列索引序列
stu = ['同学' + str(i) for i in range(score_df.shape[0])]

# 添加行索引
data = pd.DataFrame(score, columns=subjects, index=stu)

```

结果：

##### （2）DataFrame的属性
- （1）shape
```
data.shape

# 结果
(10, 5)

```
- （2）index
DataFrame的行索引列表

```
data.index

# 结果
Index(['同学0', '同学1', '同学2', '同学3', '同学4', '同学5', '同学6', '同学7', '同学8', '同学9'], dtype='object')

```
- （3）columns
DataFrame的列索引列表

```
data.columns

# 结果
Index(['语文', '数学', '英语', '政治', '体育'], dtype='object')

```
- （4）values
直接获取其中array的值

```
array([[54, 82, 62, 81, 47],
       [50, 58, 73, 72, 48],
       [88, 89, 49, 99, 83],
       [79, 81, 69, 45, 87],
       [87, 64, 62, 74, 85],
       [68, 56, 58, 77, 53],
       [77, 49, 82, 48, 82],
       [96, 49, 67, 94, 71],
       [98, 77, 44, 99, 41],
       [71, 52, 74, 90, 44]])

```
- （5）T
转置

```
data.T

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/06c87ed248f1c7700b81530edd46ed6a.png">
- （6）head(5)：显示前5行内容
如果不补充参数，默认5行。填入参数N则显示前N行

```
data.head(5)

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/905ca25413cb30ed87fa4193ebaaface.png">
- （7）tail(5):显示后5行内容
如果不补充参数，默认5行。填入参数N则显示后N行

```
data.tail(5)

```

结果：

##### （3）DatatFrame索引的设置

现在要将下图的行索引改变，变成下下图所示样子，怎么做呢？<img src="https://img-blog.csdnimg.cn/img_convert/43265632555687331a023ceb4307f3bc.png">
- (1)修改行列索引值
```
stu = ["学同学_" + str(i) for i in range(score_df.shape[0])]

# 必须整体全部修改
data.index = stu

```

注意：以下修改方式是错误的，说明不能单独修改

```
# 错误修改方式，不能单个修改
data.index[3] = '学生_3'

```
- （2）重设索引- <ul><li>设置新的下标索引- drop:默认为False，不删除原来索引，如果为True,删除原来的索引值- reset_index(drop=False)
```
# 重置索引,drop=False
data.reset_index()

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/99f060778d5c0aede842e8d9c32a5e97.png">

```
# 重置索引,drop=True
data.reset_index()

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/b41949ad3fbc9b99a123fbc6d18fd9bd.png">
- （3）以某列值设置为新的索引- set_index(keys, drop=True)- <ul><li>keys : 列索引名成或者列索引名称的列表- drop : boolean, default True.当做新的索引，删除原来的列
设置新索引案例：

1、创建

```
df = pd.DataFrame({'month': [1, 4, 7, 10],
                    'year': [2012, 2014, 2013, 2014],
                    'sale':[55, 40, 84, 31]})

   month  sale  year
0  1      55    2012
1  4      40    2014
2  7      84    2013
3  10     31    2014

```

2、以月份设置新的索引

```
df.set_index('month')
       sale  year
month
1      55    2012
4      40    2014
7      84    2013
10     31    2014

```

3、设置多个索引，以年和月份

```
df = df.set_index(['year', 'month'])
df
            sale
year  month
2012  1     55
2014  4     40
2013  7     84
2014  10    31

```

>  
  注：通过刚才的设置，这样DataFrame就变成了一个具有MultiIndex的DataFrame。 
 

#### 1.2.3 MultiIndex与Panel

##### （1）MultiIndex

MultiIndex是三维的数据结构;

多级索引（也称层次化索引）是pandas的重要功能，可以在Series、DataFrame对象上拥有2个以及2个以上的索引。
- （1）multiIndex的特性
打印刚才的df的行索引结果

```
df
            sale
year  month
2012  1     55
2014  4     40
2013  7     84
2014  10    31

df.index

MultiIndex(levels=[[2012, 2013, 2014], [1, 4, 7, 10]],
           labels=[[0, 2, 1, 2], [0, 1, 2, 3]],
           names=['year', 'month'])

```

多级或分层索引对象。
- index属性- <ul><li>names:levels的名称- levels：每个level的元组值
```
df.index.names
# FrozenList(['year', 'month'])

df.index.levels
# FrozenList([[2012, 2013, 2014], [1, 4, 7, 10]])

```
- （2）multiIndex的创建
```
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))

# 结果
MultiIndex(levels=[[1, 2], ['blue', 'red']],
           codes=[[0, 0, 1, 1], [1, 0, 1, 0]],
           names=['number', 'color'])

```

##### （2）Panel
- （1）panel的创建- <ul><li>作用：存储3维数组的Panel结构- 参数：- data : ndarray或者dataframe- items : 索引或类似数组的对象，axis=0- major_axis : 索引或类似数组的对象，axis=1- minor_axis : 索引或类似数组的对象，axis=2- class pandas.Panel(data=None, items=None, major_axis=None, minor_axis=None)
```
p = pd.Panel(data=np.arange(24).reshape(4,3,2),
                 items=list('ABCD'),
                 major_axis=pd.date_range('20130101', periods=3),
                 minor_axis=['first', 'second'])

# 结果
&lt;class 'pandas.core.panel.Panel'&gt;
Dimensions: 4 (items) x 3 (major_axis) x 2 (minor_axis)
Items axis: A to D
Major_axis axis: 2013-01-01 00:00:00 to 2013-01-03 00:00:00
Minor_axis axis: first to second

```
- （2）查看panel数据
```
p[:,:,"first"]
p["B",:,:]

```

>  
  注：Pandas从版本0.20.0开始弃用：推荐的用于表示3D数据的方法是通过DataFrame上的MultiIndex方法。 
 

## 2、基本数据操作

为了更好的理解这些基本操作，我们将读取一个真实的股票数据。关于文件操作，后面在介绍，这里只先用一下API。

```
# 读取文件
data = pd.read_csv("./data/stock_day.csv")

# 删除一些列，让数据更简单些，再去做后面的操作
data = data.drop(["ma5","ma10","ma20","v_ma5","v_ma10","v_ma20"], axis=1)

```

### 2.1 索引操作

Numpy当中我们已经讲过使用索引选取序列和切片选择，pandas也支持类似的操作，也可以直接使用列名、行名称，甚至组合使用。

#### 2.2.1 直接使用行列索引(先列后行)

获取’2018-02-27’这天的’open’的结果：

```
# 直接使用行列索引名字的方式（先列后行）
data['open']['2018-02-27']
23.53

# 不支持的操作
# 错误
data['2018-02-27']['open']
# 错误
data[:1, :2]

```

#### 2.2.2 结合loc或者iloc使用索引

获取从’2018-02-27’到’2018-02-22’，'open’的结果：

```
# 使用loc:只能指定行列索引的名字
data.loc['2018-02-27':'2018-02-22', 'open']

2018-02-27    23.53
2018-02-26    22.80
2018-02-23    22.88
Name: open, dtype: float64

# 使用iloc可以通过索引的下标去获取
# 获取前3天数据,前5列的结果
data.iloc[:3, :5]

            open    high    close    low
2018-02-27    23.53    25.88    24.16    23.53
2018-02-26    22.80    23.78    23.53    22.80
2018-02-23    22.88    23.37    22.82    22.71

```

#### 2.2.3 使用ix组合索引（混合索引:下标和名称）

获取行第1天到第4天，[‘open’, ‘close’, ‘high’, ‘low’]这个四个指标的结果：

```
# 使用ix进行下表和名称组合做引
data.ix[0:4, ['open', 'close', 'high', 'low']]

# 推荐使用loc和iloc来获取的方式
data.loc[data.index[0:4], ['open', 'close', 'high', 'low']]
data.iloc[0:4, data.columns.get_indexer(['open', 'close', 'high', 'low'])]

            open    close    high    low
2018-02-27    23.53    24.16    25.88    23.53
2018-02-26    22.80    23.53    23.78    22.80
2018-02-23    22.88    22.82    23.37    22.71
2018-02-22    22.25    22.28    22.76    22.02

```

### 2.2 赋值操作

对DataFrame当中的close列进行重新赋值为1。

```
# 直接修改原来的值
data['close'] = 1 # 这一列都变成1
# 或者
data.close = 1

```

### 2.3 排序

排序有两种形式，一种对于索引进行排序，一种对于内容进行排序:

#### 2.3.1 DataFrame排序
- （1）使用`df.sort_values(by=, ascending=)`- <ul><li>by：指定排序参考的键- ascending:默认升序- ascending=False:降序- ascending=True:升序- 单个键或者多个键进行排序,- 参数：
如下：

例一：

```
# 按照开盘价大小进行排序 , 使用ascending指定按照大小排序
data.sort_values(by="open", ascending=True).head()

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/4d70a43c025ff566429caab164698b55.png">例二：

```
# 按照多个键进行排序
data.sort_values(by=['open', 'high'])

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/38449951575fa343860ac396b7abd586.png">
- （2）使用`df.sort_index(ascending=)`给索引进行排序
这个股票的日期索引原来是从大到小，现在重新排序，从小到大:

```
# 对索引进行排序
data.sort_index()

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/8d72d8ca070f4c9382c6feb903ea5ea6.png">

#### 2.3.2 Series排序
- （1）使用`series.sort_values(ascending=True)`进行排序
series排序时，只有一列，不需要参数

```
data['p_change'].sort_values(ascending=True).head()

2015-09-01   -10.03
2015-09-14   -10.02
2016-01-11   -10.02
2015-07-15   -10.02
2015-08-26   -10.01
Name: p_change, dtype: float64

```
- （2）使用`series.sort_index()`进行排序
与df一致

```
# 对索引进行排序
data['p_change'].sort_index().head()

2015-03-02    2.62
2015-03-03    1.44
2015-03-04    1.57
2015-03-05    2.02
2015-03-06    8.51
Name: p_change, dtype: float64

```

### 2.4 总结

## 3、DataFrame运算

### 3.1 算术运算
- （1）`add(other)`
比如进行数学运算加上具体的一个数字

```
data['open'].head().add(1)

2018-02-27    24.53
2018-02-26    23.80
2018-02-23    23.88
2018-02-22    23.25
2018-02-14    22.49
Name: open, dtype: float64

```
- （2）`sub(other)`
整个列减一个数

```
data.open.head().sub(2)

2018-02-27    21.53
2018-02-26    20.80
2018-02-23    20.88
2018-02-22    20.25
2018-02-14    19.49
Name: open, dtype: float64

```

### 3.2 逻辑运算

#### 3.2.1 逻辑运算符号
- 例如筛选data[“open”] &gt; 23的日期数据- <ul><li>data[“open”] &gt; 23返回逻辑结果
```
data["open"] &gt; 23

2018-02-27     True
2018-02-26    False
2018-02-23    False
2018-02-22    False
2018-02-14    False

```

```
# 逻辑判断的结果可以作为筛选的依据
data[data["open"] &gt; 23].head()

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/dd8d47b8b15752795079d7ba8495c1a2.png">
- 完成多个逻辑判断：
```
data[(data["open"] &gt; 23) &amp; (data["open"] &lt; 24)].head()

```

#### 3.2.2 逻辑运算函数
- （1）`query(expr)`- <ul><li>expr:查询字符串
通过query使得刚才的过程更加方便简单，下面是使用的例子：

```
data.query("open&lt;24 &amp; open&gt;23").head()

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/9f6d6627eb0348681ed9639e797e1ba3.png">
- （2）`isin(values)`
例如判断’open’是否为23.53和23.85：

```
# 可以指定值进行一个判断，从而进行筛选操作
data[data["open"].isin([23.53, 23.85])]

```

#### 3.2.3 统计运算

##### （1）describe

综合分析: 能够直接得出很多统计结果,count, mean, std, min, max 等

```
# 计算平均值、标准差、最大值、最小值
data.describe()

```

##### （2）统计函数

看一下`min(最小值)`, `max(最大值)`, `mean(平均值)`, `median(中位数)`, `var(方差)`, `std(标准差)`,`mode(众数)`是怎么操作的:

<img src="https://img-blog.csdnimg.cn/img_convert/e202af579149533b21e6116a8bb08cd9.png">

对于单个函数去进行统计的时候，坐标轴还是按照默认列“columns” (axis=0, default)，如果要对行“index” 需要指定(axis=1)。
- （1）`max()、min()`
```
# 使用统计函数：0 代表列求结果， 1 代表行求统计结果
data.max(axis=0) # 最大值

open                   34.99
high                   36.35
close                  35.21
low                    34.01
volume             501915.41
price_change            3.03
p_change               10.03
turnover               12.56
my_price_change         3.41
dtype: float64

```
- （2）`std()、var()`
```
# 方差
data.var(axis=0)

open               1.545255e+01
high               1.662665e+01
close              1.554572e+01
low                1.437902e+01
volume             5.458124e+09
price_change       8.072595e-01
p_change           1.664394e+01
turnover           4.323800e+00
my_price_change    6.409037e-01
dtype: float64

# 标准差
data.std(axis=0)

open                   3.930973
high                   4.077578
close                  3.942806
low                    3.791968
volume             73879.119354
price_change           0.898476
p_change               4.079698
turnover               2.079375
my_price_change        0.800565
dtype: float64

```
- （3）`median()`：中位数
中位数为将数据从小到大排列，在最中间的那个数为中位数。如果没有中间数，取中间两个数的平均值。

```
data.median(axis=0)

open               21.44
high               21.97
close              10.00
low                20.98
volume          83175.93
price_change        0.05
p_change            0.26
turnover            2.50
dtype: float64

```
- （4）`idxmax()、idxmin()`
```
# 求出最大值的位置
data.idxmax(axis=0)

open               2015-06-15
high               2015-06-10
close              2015-06-12
low                2015-06-12
volume             2017-10-26
price_change       2015-06-09
p_change           2015-08-28
turnover           2017-10-26
my_price_change    2015-07-10
dtype: object


# 求出最小值的位置
data.idxmin(axis=0)

open               2015-03-02
high               2015-03-02
close              2015-09-02
low                2015-03-02
volume             2016-07-06
price_change       2015-06-15
p_change           2015-09-01
turnover           2016-07-06
my_price_change    2015-06-15
dtype: object

```

##### （3）累计统计函数

<img src="https://img-blog.csdnimg.cn/img_convert/850b93f71cec81dc9afeaff4b8a2b1aa.png">

那么这些累计统计函数怎么用？<img src="https://img-blog.csdnimg.cn/img_convert/40a06dbf9c40d6a520077892e3e34f3d.png">以上这些函数可以对series和dataframe操作，这里我们按照时间的从前往后来进行累计
- 排序
```
# 排序之后，进行累计求和
data = data.sort_index()

```
- 对p_change进行求和
```
stock_rise = data['p_change']

stock_rise.cumsum()

2015-03-02      2.62
2015-03-03      4.06
2015-03-04      5.63
2015-03-05      7.65
2015-03-06     16.16
2015-03-09     16.37
2015-03-10     18.75
2015-03-11     16.36
2015-03-12     15.03
2015-03-13     17.58
2015-03-16     20.34
2015-03-17     22.42
2015-03-18     23.28
2015-03-19     23.74
2015-03-20     23.48
2015-03-23     23.74

```

**那么如何让这个连续求和的结果更好的显示呢？**

如果要使用plot函数，需要导入matplotlib.下面是绘图代码：

```
import matplotlib.pyplot as plt
# plot显示图形, plot方法集成了直方图、条形图、饼图、折线图
stock_rise.cumsum().plot()
# 需要调用show，才能显示出结果
plt.show()

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/55d46027a37e25b56efde5111c15597e.png">

>  
  关于plot，稍后会介绍API的选择。 
 

##### （4）自定义运算
- `apply(func, axis=0)`- <ul><li>func:自定义函数- axis=0:默认是列，axis=1为行进行运算
定义一个对列，最大值-最小值的函数

下面看个例子：

```
data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0)

open     22.74
close    22.85
dtype: float64

```

>  
  特定需求需要用这个。 
 

## 4、Pandas画图

### 4.1 pandas.DataFrame.plot
- <h3>`DataFrame.plot(kind='line')`</h3>- <ul><li>‘line’ : 折线图- ‘bar’ : 条形图- ‘barh’ : 横放的条形图- ‘hist’ : 直方图- ‘pie’ : 饼图- ‘scatter’ : 散点图- kind : str，需要绘制图形的种类
关于“barh”的解释：http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.barh.html

更多细节：https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html?highlight=plot#pandas.DataFrame.plot

看个例子：

```
import matplotlib.pyplot as plt
# plot显示图形, plot方法集成了直方图、条形图、饼图、折线图
stock_rise.cumsum().plot(kind="line")
# 需要调用show，才能显示出结果
plt.show()

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/436b41336eb2bcaa7eed405202e434a2.png">

### 4.2 pandas.Series.plot

更多细节：https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.plot.html?highlight=plot#pandas.Series.plot

>  
  注：使用的时候查看。 
 

## 5、文件读取与存储

我们的数据大部分存在于文件当中，所以pandas会支持复杂的IO操作，pandas的API支持众多的文件格式，如CSV、SQL、XLS、JSON、HDF5。

>  
  注：最常用的HDF5和CSV文件 
 

<img src="https://img-blog.csdnimg.cn/img_convert/aa661c3e4564119c28252d9d713cc642.png">接下来重点看一下，应用CSV方式、HDF方式和json方式实现文件的读取和存储。

### 5.1 CSV

#### 5.1.1 read_csv
- `pandas.read_csv(filepath_or_buffer, sep =',', usecols )`- <ul><li>filepath_or_buffer:文件路径- sep :分隔符，默认用","隔开- usecols:指定读取的列名，列表形式
举例：读取之前的股票的数据：

```
# 读取文件,并且指定只获取'open', 'close'指标
data = pd.read_csv("./data/stock_day.csv", usecols=['open', 'close'])

            open    close
2018-02-27    23.53    24.16
2018-02-26    22.80    23.53
2018-02-23    22.88    22.82
2018-02-22    22.25    22.28
2018-02-14    21.49    21.92

```

#### 5.1.2 to_csv
- `DataFrame.to_csv(path_or_buf=None, sep=', ’, columns=None, header=True, index=True, mode='w', encoding=None)`- <ul><li>path_or_buf :文件路径- sep :分隔符，默认用","隔开- columns :选择需要的列索引- header :boolean or list of string, default True,是否写进列索引值- index:是否写进行索引- mode:‘w’：重写, ‘a’ 追加
>  
  举例：保存读取出来的股票数据保存’open’列的数据，然后读取查看结果： 
 

```
# 选取10行数据保存,便于观察数据
data[:10].to_csv("./data/test.csv", columns=['open'])

# 读取，查看结果
pd.read_csv("./data/test.csv")

     Unnamed: 0    open
0    2018-02-27    23.53
1    2018-02-26    22.80
2    2018-02-23    22.88
3    2018-02-22    22.25
4    2018-02-14    21.49
5    2018-02-13    21.40
6    2018-02-12    20.70
7    2018-02-09    21.20
8    2018-02-08    21.79
9    2018-02-07    22.69

```

会发现将索引存入到文件当中，变成单独的一列数据。如果需要删除，可以指定index参数,删除原来的文件，重新保存一次。

下面例子把index指定为False，那么保存的时候就不会保存行索引了：

```
# index:存储不会将索引值变成一列数据
data[:10].to_csv("./data/test.csv", columns=['open'], index=False)

```

当然我们也可以这么做，就是把索引保存到文件中，读取的时候变成了一列，那么可以把这个列再变成索引，如下：

```
# 把Unnamed: 0这一列，变成行索引
open.set_index(["Unnamed: 0"])

# 把索引名字变成index
open.index.name = "index"

```

### 5.2 HDF5

#### 5.2.1 read_hdf与to_hdf

**HDF5文件的读取和存储需要指定一个键，值为要存储的DataFrame**
- （1）`pandas.read_hdf(path_or_buf，key =None，** kwargs)`- <ul><li>path_or_buffer:文件路径- key:读取的键- return:Theselected object
（2）`DataFrame.to_hdf(path_or_buf, key, **kwargs)`

#### 5.2.2 案例
- 读取文件
```
day_close = pd.read_hdf("./data/day_close.h5")

```

如果读取的时候出现以下错误<img src="https://img-blog.csdnimg.cn/img_convert/cef491a143052b5301eb62502d3dbd50.png">需要安装安装tables模块避免不能读取HDF5文件

```
pip install tables

```
- 存储文件
```
day_close.to_hdf("./data/test.h5", key="day_close")

```

再次读取的时候, 需要指定键的名字

```
new_close = pd.read_hdf("./data/test.h5", key="day_close")

```

注意：优先选择使用HDF5文件存储
- HDF5在存储的时候支持压缩，使用的方式是blosc，这个是速度最快的也是pandas默认支持的- 使用压缩可以提磁盘利用率，节省空间- HDF5还是跨平台的，可以轻松迁移到hadoop 上面
### 5.3 JSON

JSON是我们常用的一种数据交换格式，在前后端的交互经常用到，也会在存储的时候选择这种格式。所以我们需要知道Pandas如何进行读取和存储JSON格式。

#### 5.3.1 read_json
- `pandas.read_json(path_or_buf=None, orient=None, typ='frame', lines=False)`- <ul><li>按照每行读取json对象- （1）‘split’ : dict like {index -&gt; [index], columns -&gt; [columns], data -&gt; [values]}- （2）‘records’ : list like [{column -&gt; value}, … , {column -&gt; value}]- （3）‘index’ : dict like {index -&gt; {column -&gt; value}}- （4）‘columns’ : dict like {column -&gt; {index -&gt; value}},默认该格式- （5）‘values’ : just the values array- split 将索引总结到索引，列名到列名，数据到数据。将三部分都分开了- records 以columns：values的形式输出- index 以index：{columns：values}…的形式输出- colums 以columns:{index:values}的形式输出- values 直接输出值- `path_or_buf` : 路径- `orient` : string,以什么样的格式显示.下面是5种格式：- `lines` : boolean, default False- `typ` : default ‘frame’， 指定转换成的对象类型series或者dataframe
**案例：**
- 数据介绍：
这里使用一个新闻标题讽刺数据集，格式为json。is_sarcastic：1讽刺的，否则为0；headline：新闻报道的标题；article_link：链接到原始新闻文章。存储格式为：

```
{"article_link": "https://www.huffingtonpost.com/entry/versace-black-code_us_5861fbefe4b0de3a08f600d5", "headline": "former versace store clerk sues over secret 'black code' for minority shoppers", "is_sarcastic": 0}
{"article_link": "https://www.huffingtonpost.com/entry/roseanne-revival-review_us_5ab3a497e4b054d118e04365", "headline": "the 'roseanne' revival catches up to our thorny political mood, for better and worse", "is_sarcastic": 0}

```
- 读取
orient指定存储的json格式，lines指定按照行去变成一个样本：

```
json_read = pd.read_json("./data/Sarcasm_Headlines_Dataset.json", orient="records", lines=True)

```

结果为：<img src="https://img-blog.csdnimg.cn/img_convert/dd498843d94f2de0934be4d1e8849314.png">

#### 5.3.2 to_json
- `DataFrame.to_json(path_or_buf=None, orient=None, lines=False)`- <ul><li>将Pandas 对象存储为json格式- path_or_buf=None：文件地址- orient:存储的json形式，{‘split’,’records’,’index’,’columns’,’values’}- lines:一个对象存储为一行
**案例：**
- 存储文件
```
# 不指定lines=Treu，则保存成一行
json_read.to_json("./data/test.json", orient='records')

```

结果：

```
[{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/versace-black-code_us_5861fbefe4b0de3a08f600d5","headline":"former versace store clerk sues over secret 'black code' for minority shoppers","is_sarcastic":0},{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/roseanne-revival-review_us_5ab3a497e4b054d118e04365","headline":"the 'roseanne' revival catches up to our thorny political mood, for better and worse","is_sarcastic":0},{"article_link":"https:\/\/local.theonion.com\/mom-starting-to-fear-son-s-web-series-closest-thing-she-1819576697","headline":"mom starting to fear son's web series closest thing she will have to grandchild","is_sarcastic":1},{"article_link":"https:\/\/politics.theonion.com\/boehner-just-wants-wife-to-listen-not-come-up-with-alt-1819574302","headline":"boehner just wants wife to listen, not come up with alternative debt-reduction ideas","is_sarcastic":1},{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/jk-rowling-wishes-snape-happy-birthday_us_569117c4e4b0cad15e64fdcb","headline":"j.k. rowling wishes snape happy birthday in the most magical way","is_sarcastic":0},{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/advancing-the-worlds-women_b_6810038.html","headline":"advancing the world's women","is_sarcastic":0},....]

```
- 修改`lines`参数为True
```
# 指定lines=True，则多行存储
json_read.to_json("./data/test.json", orient='records', lines=True)

```

结果：

```
{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/versace-black-code_us_5861fbefe4b0de3a08f600d5","headline":"former versace store clerk sues over secret 'black code' for minority shoppers","is_sarcastic":0}
{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/roseanne-revival-review_us_5ab3a497e4b054d118e04365","headline":"the 'roseanne' revival catches up to our thorny political mood, for better and worse","is_sarcastic":0}
{"article_link":"https:\/\/local.theonion.com\/mom-starting-to-fear-son-s-web-series-closest-thing-she-1819576697","headline":"mom starting to fear son's web series closest thing she will have to grandchild","is_sarcastic":1}
{"article_link":"https:\/\/politics.theonion.com\/boehner-just-wants-wife-to-listen-not-come-up-with-alt-1819574302","headline":"boehner just wants wife to listen, not come up with alternative debt-reduction ideas","is_sarcastic":1}
{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/jk-rowling-wishes-snape-happy-birthday_us_569117c4e4b0cad15e64fdcb","headline":"j.k. rowling wishes snape happy birthday in the most magical way","is_sarcastic":0}...

```

## 6、高级处理-缺失值处理

在pandas中，缺失值使用NaN来标记，如下图所示：<img src="https://img-blog.csdnimg.cn/img_convert/0236a2cf761c39dd2042f1ca5320a806.png">

### 6.1 如何处理nan

按如下步骤进行：
- （1）获取缺失值的标记方式(NaN或者其他标记方式)- （2）如果缺失值的标记方式是NaN- <ul><li>1、删除存在缺失值的:`dropna(axis='rows')`注：不会修改原数据，需要接受返回值- 2、替换缺失值:`fillna(value, inplace=True)`- value:替换成的值- inplace:True:会修改原数据，False:不替换修改原数据，生成新的对象- `pd.isnull(df),`- `pd.notnull(df)`- 判断数据中是否包含NaN：- 存在缺失值nan:
（3）如果缺失值没有使用NaN标记，比如使用"？"
- 先替换‘?’为np.nan，然后继续处理
>  
  步骤就是上面的这样，下面通过例子来看看怎么使用pandas处理的： 
 

### 6.2 电影数据的缺失值处理
- 电影数据文件获取
```
# 读取电影数据
movie = pd.read_csv("./data/IMDB-Movie-Data.csv")

```

#### 6.2.1 判断缺失值是否存在
- <h3>（1）`pd.notnull()`</h3>
```
# 判断是否是缺失值，是则返回False
pd.notnull(movie)

# 结果：
Rank    Title    Genre    Description    Director    Actors    Year    Runtime (Minutes)    Rating    Votes    Revenue (Millions)    Metascore
0    True    True    True    True    True    True    True    True    True    True    True    True
1    True    True    True    True    True    True    True    True    True    True    True    True
2    True    True    True    True    True    True    True    True    True    True    True    True
3    True    True    True    True    True    True    True    True    True    True    True    True
4    True    True    True    True    True    True    True    True    True    True    True    True
5    True    True    True    True    True    True    True    True    True    True    True    True
6    True    True    True    True    True    True    True    True    True    True    True    True
7    True    True    True    True    True    True    True    True    True    True    False    True

```

但是上面这样显然不好观察，我们可以借助`np.all()`来返回是否有缺失值。`np.all()`只要有一个就返回False，下面看例子：

```
np.all(pd.notnull(movie))

# 返回
False

```
- <h3>（2）`pd.isnull()`</h3>这个和上面的正好相反，判断是否是缺失值，是则返回True。
```
# 判断是否是缺失值，是则返回True
pd.isnull(movie).head()

# 结果：
 Rank Title Genre Description Director Actors Year Runtime (Minutes) Rating Votes Revenue (Millions) Metascore
0 False False False False False False False False False False False False
1 False False False False False False False False False False False False
2 False False False False False False False False False False False False
3 False False False False False False False False False False False False
4 False False False False False False False False False False False False

```

这个也不好观察，我们利用`np.any()` 来判断是否有缺失值，若有则返回True，下面看例子：

```
np.any(pd.isnull(movie))
# 返回
True

```

#### 6.2.2 存在缺失值nan,并且是np.nan
- 1、删除
pandas删除缺失值，使用dropna的前提是，缺失值的类型必须是np.nan

```
# 不修改原数据
movie.dropna()

# 可以定义新的变量接受或者用原来的变量名
data = movie.dropna()

```
- 2、替换缺失值
```
# 替换存在缺失值的样本的两列
# 替换填充平均值，中位数
movie['Revenue (Millions)'].fillna(movie['Revenue (Millions)'].mean(), inplace=True)

```

替换所有缺失值：

```
# 这个循环，每次取出一列数据，然后用均值来填充
for i in movie.columns:
    if np.all(pd.notnull(movie[i])) == False:
        print(i)
        movie[i].fillna(movie[i].mean(), inplace=True)

```

#### 6.2.3 不是缺失值nan，有默认标记的

直接看例子：

数据是这样的：<img src="https://img-blog.csdnimg.cn/img_convert/04a7658aea77b7f08e42604f3216420e.png">

```
# 读入数据
wis = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data")

```

以上数据在读取时，可能会报如下错误：

```
URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)&gt;

```

解决办法：

```
# 全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

```

处理思路分析：
- 1、先替换‘?’为np.nan- <ul><li>to_replace:替换前的值- value:替换后的值- `df.replace(to_replace=, value=)`
```
# 把一些其它值标记的缺失值，替换成np.nan
wis = wis.replace(to_replace='?', value=np.nan)

```
- 2、再进行缺失值的处理
```
# 删除
wis = wis.dropna()

```
- 3、验证：
```
np.all(pd.notnull(wis))
# 返回True，说明没有了缺失值

# 或者

np.any(pd.isnull(wis))
# 返回False，说明没有了缺失值

```

## 7、高级处理-数据离散化

### 7.1 为什么要离散化

连续属性离散化的目的是为了简化数据结构，数据离散化技术可以用来减少给定连续属性值的个数。离散化方法经常作为数据挖掘的工具。

### 7.2 什么是数据的离散化

**连续属性的离散化就是在连续属性的值域上，将值域划分为若干个离散的区间，最后用不同的符号或整数 值代表落在每个子区间中的属性值。**

离散化有很多种方法，这里使用一种最简单的方式去操作：
- 原始人的身高数据：165，174，160，180，159，163，192，184- 假设按照身高分几个区间段：150~165, 165~180,180~195
这样我们将数据分到了三个区间段，对应的标记为矮、中、高三个类别，最终要处理成一个"哑变量"矩阵。

>  
  下面通过股票数据的例子来看看，具体是怎么操作的。 
 

### 7.3 股票的涨跌幅离散化

我们对股票每日的"p_change"这一列进行离散化，下图便是离散化后的结果，当前数据存在哪个区间，则这个区间标记为1，否则为0。

<img src="https://img-blog.csdnimg.cn/img_convert/b688eb327fa3727ab7fa3a444e09a3ff.png">那具体怎么做的呢？接着看：

#### 7.3.1 读取股票的数据

先读取股票的数据，筛选出p_change数据。

```
data = pd.read_csv("./data/stock_day.csv")
p_change= data['p_change']

```

#### 7.3.2 将股票涨跌幅数据进行分组

下面是所在区间的个数。<img src="https://img-blog.csdnimg.cn/img_convert/42845a2197d648003018a7cf740c8fd9.png">

使用的工具：
- `pd.qcut(data, q)`：- <ul><li>对数据进行分组，将数据分成q组，一般会与`value_counts`搭配使用，统计每组的个数
`series.value_counts()`：统计每个分组中有多少数据。

```
# 自行分组
qcut = pd.qcut(p_change, 10)
# 计算分到每个组数据个数
qcut.value_counts()

# 运行结果：
(5.27, 10.03]                    65
(0.26, 0.94]                     65
(-0.462, 0.26]                   65
(-10.030999999999999, -4.836]    65
(2.938, 5.27]                    64
(1.738, 2.938]                   64
(-1.352, -0.462]                 64
(-2.444, -1.352]                 64
(-4.836, -2.444]                 64
(0.94, 1.738]                    63
Name: p_change, dtype: int64

```

自定义区间分组：
- `pd.cut(data, bins)`
```
# 自己指定分组区间
bins = [-100, -7, -5, -3, 0, 3, 5, 7, 100]
p_counts = pd.cut(p_change, bins)
p_counts.value_counts()

# 运行结果：
(0, 3]        215
(-3, 0]       188
(3, 5]         57
(-5, -3]       51
(7, 100]       35
(5, 7]         35
(-100, -7]     34
(-7, -5]       28
Name: p_change, dtype: int64

```

#### 7.3.3 股票涨跌幅分组数据变成one-hot编码
- 什么是one-hot编码把每个类别生成一个布尔列，这些列中只有一列可以为这个样本取值为1.其又被称为热编码。
把下图中左边的表格转化为使用右边形式进行表示：

<img src="https://img-blog.csdnimg.cn/img_convert/b532197eeef619c7cde230360bbf1197.png">下面看看pandas中是怎么实现的：
- `pandas.get_dummies(data, prefix=None)`- <ul><li>data:array-like, Series, or DataFrame- prefix:分组名字
下面是例子：

```
# 得出one-hot编码矩阵
dummies = pd.get_dummies(p_counts, prefix="rise")

```

运行结果：<img src="https://img-blog.csdnimg.cn/img_convert/43b88cb73a981762f5456e9bebc4eff5.png">

## 8、高级处理-合并

如果你的数据由多张表组成，那么有时候需要将不同的内容合并在一起分析

### 8.1 pd.concat实现数据合并
- `pd.concat([data1, data2], axis=1)`- <ul><li>按照行或列进行合并,axis=0为列索引，axis=1为行索引
比如我们将刚才处理好的one-hot编码与原数据合并:

```
# 按照行索引进行
pd.concat([data, dummies], axis=1)

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/b29672dd0e90ac7988e212b38bb7f8ca.png">

### 8.2 pd.merge
- `pd.merge(left, right, how='inner', on=None)`- <ul><li>可以指定按照两组数据的共同键值对合并或者左右各自- `left`: DataFrame- `right`: 另一个DataFrame- `on`: 指定的共同键- `how`:按照什么方式连接，下面的表格是说明
<img src="https://img-blog.csdnimg.cn/img_convert/27452a9a51f4ba578772e81a4aaa01f4.png">

例子：

```
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                        'key2': ['K0', 'K0', 'K0', 'K0'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

```
- **内连接：健相同的取上，不同的删掉**
```
# 默认内连接
result = pd.merge(left, right, on=['key1', 'key2'])

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/b04a357b5cb70b036e35ded9a561779b.png">
- **左连接：按左边的数据进行合并**
```
result = pd.merge(left, right, how='left', on=['key1', 'key2'])

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/b768be26c672c7c403ca5c446a5e99ef.png">
- **右连接：按右边的数据进行合并**
```
result = pd.merge(left, right, how='right', on=['key1', 'key2'])

```
- 外**链接：无论健是否相同都取上，对应不上的使用NaN填充。**
```
result = pd.merge(left, right, how='outer', on=['key1', 'key2'])

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/5be7aa2724ff33438d47d0bfd56b4e6e.png">

## 9、高级处理-交叉表与透视表

### 9.1 交叉表与透视表什么作用

探究股票的涨跌与星期几有关？

以下图当中表示，week代表星期几，1,0代表这一天股票的涨跌幅是好还是坏，里面的数据代表比例

可以理解为所有时间为星期一等等的数据当中涨跌幅好坏的比例<img src="https://img-blog.csdnimg.cn/img_convert/b5a865b0ff3c0ca3efb3a71a93ef806f.png"><img src="https://img-blog.csdnimg.cn/img_convert/ea49bc8980394237d8a69259278756a6.png">
- 交叉表：**交叉表用于计算一列数据对于另外一列数据的分组个数(用于统计分组频率的特殊透视表)**- <ul><li>`pd.crosstab(value1, value2)`
透视表：**透视表是将原有的DataFrame的列分别作为行索引和列索引，然后对指定的列应用聚集函数**
- `data.pivot_table(）`- `DataFrame.pivot_table([], index=[])`
### 9.2 案例分析

#### 9.2.1 数据准备
- 准备两列数据，星期数据以及涨跌幅是好是坏数据- 进行交叉表计算
```
# 寻找星期几跟股票张得的关系
# 1、先把对应的日期找到星期几
date = pd.to_datetime(data.index).weekday
data['week'] = date  # 增加一列

# 2、假如把p_change按照大小去分个类0为界限
data['posi_neg'] = np.where(data['p_change'] &gt; 0, 1, 0)

# 通过交叉表找寻两列数据的关系
count = pd.crosstab(data['week'], data['posi_neg'])

```

结果：

但是我们看到count只是每个星期日子的好坏天数，并没有得到比例，该怎么去做？
- 对于每个星期一等的总天数求和，运用除法运算求出比例
```
# 算数运算，先求和
sum = count.sum(axis=1).astype(np.float32)

# 进行相除操作，得出比例
pro = count.div(sum, axis=0)

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/32ec2e6268fe86f49341753d4edc7f58.png">

#### 9.2.2 查看效果

使用plot画出这个比例，使用stacked的柱状图

```
pro.plot(kind='bar', stacked=True)
plt.show()

```

#### 9.2.3 使用pivot_table(透视表)实现

使用透视表，刚才的过程更加简单

```
# 通过透视表，将整个过程变成更简单一些
data.pivot_table(['posi_neg'], index='week')

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/e7d59758940b3f35da0b8ddb94df1d4e.png">

## 10、高级处理-分组与聚合

**分组与聚合通常是分析数据的一种方式，通常与一些统计函数一起使用，查看数据的分组情况**

### 10.1 什么分组与聚合

下图展示了分组与聚合的概念：<img src="https://img-blog.csdnimg.cn/img_convert/59f4045c3311d59991d1a01c9d46b3b2.png">

### 10.2 分组API
- `DataFrame.groupby(key, as_index=False)`- <ul><li>key:分组的列数据，可以多个
案例:不同颜色的不同笔的价格数据

```
col =pd.DataFrame({'color': ['white','red','green','red','green'], 'object': ['pen','pencil','pencil','ashtray','pen'],'price1':[5.56,4.20,1.30,0.56,2.75],'price2':[4.75,4.12,1.60,0.75,3.15]})

# 结果：
color    object    price1    price2
0    white    pen    5.56    4.75
1    red    pencil    4.20    4.12
2    green    pencil    1.30    1.60
3    red    ashtray    0.56    0.75
4    green    pen    2.75    3.15

```
- 进行分组，对颜色分组，price进行聚合：
```
# 按color分组，再取出price1列求平均值
col.groupby(['color'])['price1'].mean()
# 和上述一个功能
col['price1'].groupby(col['color']).mean()
# 结果：
color
green    2.025
red      2.380
white    5.560
Name: price1, dtype: float64

# 分组，数据的结构不变
col.groupby(['color'], as_index=False)['price1'].mean()
# 结果：
color    price1
0    green    2.025
1    red    2.380
2    white    5.560

```

### 10.3 星巴克零售店铺数据

现在我们有一组关于全球星巴克店铺的统计数据，如果我想知道美国的星巴克数量和中国的哪个多，或者我想知道中国每个省份星巴克的数量的情况，那么应该怎么办？

数据来源：https://www.kaggle.com/starbucks/store-locations/data

#### 10.3.1 数据获取

从文件中读取星巴克店铺数据

```
# 导入星巴克店的数据
starbucks = pd.read_csv("./data/starbucks/directory.csv")

```

#### 10.3.2 进行分组聚合

```
# 按照国家分组，求出每个国家的星巴克零售店数量
count = starbucks.groupby(['Country']).count()

```

画图显示结果:

```
count['Brand'].plot(kind='bar', figsize=(20, 8))
plt.show()

```

<img src="https://img-blog.csdnimg.cn/img_convert/b8e99a5bb4014cae0692afd90368f556.png">假设我们加入省市一起进行分组:

```
# 设置多个索引，set_index()
starbucks.groupby(['Country', 'State/Province']).count()

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/0d83b9289e56fa8e773444723c097da5.png">

## 11、电影案例分析

### 11.1 需求

现在我们有一组从2006年到2016年1000部最流行的电影数据

数据来源：https://www.kaggle.com/damianpanek/sunday-eda/data
- 问题1：我们想知道这些电影数据中评分的平均分，导演的人数等信息，我们应该怎么获取？- 问题2：对于这一组电影数据，如果我们想rating，runtime的分布情况，应该如何呈现数据？- 问题3：对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？
### 11.2 实现

首先获取导入包，获取数据:

```
%matplotlib inline
import pandas  as pd 
import numpy as np
from matplotlib import pyplot as plt

```

```
#文件的路径
path = "./data/IMDB-Movie-Data.csv"
#读取文件
df = pd.read_csv(path)

```

#### 11.2.1 问题一：

**我们想知道这些电影数据中评分的平均分，导演的人数等信息，我们应该怎么获取？**
- 得出评分的平均分
使用mean函数

```
df["Rating"].mean()

# 结果：
6.723200000000003

```
- 得出导演人数信息
求出唯一值，然后进行形状获取

```
## 导演的人数
# df["Director"].unique().shape[0] # 方法一
np.unique(df["Director"]).shape[0] # 方法二

644

```

#### 11.2.2 问题二：

**对于这一组电影数据，如果我们想Rating的分布情况，应该如何呈现数据？**
- 直接呈现，以直方图的形式
选择分数列数据，进行plot

```
df["Rating"].plot(kind='hist',figsize=(20,8))
plt.show()

```

效果：<img src="https://img-blog.csdnimg.cn/img_convert/1d7a9ea03586c29933e1a7f887be887d.png">

>  
  发现直接通过pandas的plot画图，显示的下标不合适，这个时候我们需要借助matplotlib来改变。 
 
- Rating进行分布展示
进行绘制直方图

```
# 1.添加画布
plt.figure(figsize=(20,8),dpi=100)

# 2.画图
plt.hist(df["Rating"].values,bins=20)
# 2.1 添加刻度线
max_ = df["Rating"].max()
min_ = df["Rating"].min()
x_ticks = np.linspace(min_, max_, num=21)
plt.xticks(x_ticks)
# 2.2添加网格线
plt.grid()

# 3.显示
plt.show()

```

>  
  数据分析：从上图中就可以发现，评分主要分布在5~8分之间 
 

#### 11.2.3 问题三：

**对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？**
- 思路分析- <ul><li>1、创建一个全为0的dataframe，列索引置为电影的分类，temp_df- 2、遍历每一部电影，temp_df中把分类出现的列的值置为1- 3、求和- 思路
下面接着看：
- 1、创建一个全为0的dataframe，列索引置为电影的分类，temp_df
```
# 进行字符串分割
temp_list = [i.split(",") for i in df["Genre"]]
# 获取电影的分类
genre_list = np.unique([i for j in temp_list for i in j]) 

# 增加新的列，创建全为0的dataframe
temp_df = pd.DataFrame(np.zeros([df.shape[0],genre_list.shape[0]]),columns=genre_list)

```
- 2、遍历每一部电影，temp_df中把分类出现的列的值置为1
```
for i in range(1000):
    #temp_list[i] 就是['Action','Adventure','Animation']等
    temp_df.ix[i,temp_list[i]]=1
    
print(temp_df.sum().sort_values()) # 求合并排序，ascending=False为倒序

```
- 3、求和,绘图
```
temp_df.sum().sort_values(ascending=False).plot(kind="bar",figsize=(20,8),fontsize=20,colormap="cool")
plt.show()

```

结果：<img src="https://img-blog.csdnimg.cn/img_convert/faf6c51a3fc3d44102b9771c8d2d7b44.png">

若有用，欢迎点赞，若有错，请指正，谢谢！
