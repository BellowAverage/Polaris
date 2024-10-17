
--- 
title:  Python 数据分析（三）：初识 Pandas 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- - - <ul><li>- - 


### 1. 简介

Pandas 基于  开发，它提供了快速、灵活、明确的数据结构，旨在简单、直观地处理数据。

Pandas 适用于处理以下类型的数据：
-  有序和无序的时间序列数据 -  带行列标签的矩阵数据，包括同构或异构型数据 -  与 SQL 或 Excel 表类似的，含异构列的表格数据 -  任意其它形式的观测、统计数据集，数据转入 Pandas 数据结构时不必事先标记 
Pandas 主要数据结构是 Series（一维数据）与 DataFrame（二维数据），这两种数据结构足以处理金融、统计等领域里的大多数典型用例。

### 2. Series

Series 可以自定义标签（索引），然后通过索引来访问数组中数据，下面通过示例来了解一下。

```
from pandas import Series

'''
创建 Series 对象
如果不指定索引，则使用默认索引，范围是：[0,...,len(数据)-1]
'''
s1 = Series([1, 2, 3, 4, 5])
s2 = Series([1, 2, 3, 4, 5], index=['6', '7', '8', '9', '10'])
print(s1)
# 获取索引
print(s1.index)
# 获取值
print(s1.values)
# 获取索引和值
print(s1.iteritems)
# 取指定值
print(s2[0])
print(s2['6'])
# 连续取值
print(s2[1:3])
print(s2['7':'8'])
# 取不连续取值
print(s2[[1,4]])
print(s2[['7','10']])
# 基本运算
print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
print(s1 / s1)

```

### 3. DataFrame

DataFrame 是一种二维数据结构，类似于 Excel 、SQL 表或 Series 对象构成的字典，DataFrame 是最常用的 Pandas 对象，与 Series 一样，DataFrame 支持多种类型的输入数据，下面通过示例来做进一步了解。

#### 3.1 创建

我们先来看一下如何创建 DataFrame。

```
from pandas import DataFrame
import numpy as np

# 直接创建
df1 = DataFrame(np.random.randn(5,5), index=list('abcde'), columns=list('abcde'))
print(df1)
# 使用字典创建
dic = {<!-- -->'name':['张三', '李四', '王五', '赵六', '朱七'], 'age':[20, 18, 30, 40, 50]}
df2 = DataFrame(dic)
print(df2)
df3 = DataFrame.from_dict(dic)
print(df3)
# 转为字典
d = df3.to_dict()
print(d)

```

#### 3.2 基本操作

我们通过示例来看一下 DataFrame 的常用基本操作。

```
from pandas import DataFrame

dic = {<!-- -->'name':['张三', '李四', '王五', '赵六', '朱七'], 'age':[20, 18, 30, 40, 50], 'gender':['男', '女', '男', '女', '男']}
df = DataFrame(dic)
# 数据类型
print(df.dtypes)
# 维度
print(df.ndim)
# 概览
print(df.info())
# 行、列数
print(df.shape)
# 行索引
print(df.index.tolist())
# 列索引
print(df.columns.tolist())
# 数据（二维数组形式）
print(df.values)
# 前几行
print(df.head(2))
# 后几行
print(df.tail(2))
# 获取一列
print(df['name'])
# 类型为 Series
print(type(df['name']))
# 获取多列
print(df[['name', 'age']])
# 类型为 DataFrame
print(type(df[['name', 'age']]))
# 获取一行
print(df[1:2])
# 获取多行
print(df[1:4])
# 多行的某一列数据
print(df[1:4][['name']])
# 某一行某一列数据
print(df.loc[1, 'name'])
# 某一行指定列数据
print(df.loc[1, ['name', 'age']])
# 某一行所有列数据
print(df.loc[1, :])
# 连续多行和间隔的多列
print(df.loc[0:2, ['name', 'gender']])
# 间隔多行和间隔的多列
print(df.loc[[0, 2], ['name', 'gender']])
# 取一行
print(df.iloc[1])
# 取连续多行
print(df.iloc[0:3])
# 取间断的多行
print(df.iloc[[1, 3]])
# 取某一列
print(df.iloc[:, 0])
# 取某一个值
print(df.iloc[0, 1])

```

#### 3.3 添加删除

我们通过示例来看一下如何向 DataFrame 中添加数据以及如何从其中删除数据。

```
from pandas import DataFrame
import pandas as pd
import numpy as np

df1 = DataFrame([['张三', '22'], ['李四', '33'], ['王五', '11']], columns=['name', 'age'])
df2 = DataFrame([['张三', '22'], ['李四', '33'], ['王五', '11']], columns=['name', 'age'])
# 在某位置插入一列
# 方式 1
col = df1.columns.tolist()
col.insert(1, 'gender')
df1.reindex(columns=col)
df1['gender'] = ['男', '女', '保密']
print(df1)
# 方式 2
df1.insert(0, 'id', ['001', '002', '003'])
print(df1)
# 在某位置插入一行
row = ['004', '赵六', '66', '男']
df1.iloc[2] = row
print(df1)
df3 = DataFrame({<!-- -->'name':'赵六', 'age':'55'}, index=[0])
df2 = df2.append(df3, ignore_index=True)
print(df2)
# 合并
df4 = DataFrame(np.arange(6).reshape(3, 2), columns=['a', 'b'])
df5 = DataFrame(np.arange(6).reshape(2, 3), columns=['c', 'd', 'e'])
# 按行
pd6 = pd.concat([df4, df5], axis=1)
print(pd6)
# 按列
pd7 = pd.concat([df4, df5], axis=0, ignore_index=True)
print(pd7)
'''
删除
参数1：要删除的标签
参数2：0 表示行，1 表示列
参数3：是否在当前 df 中执行该操作
'''
df5.drop(['c'], axis=1, inplace=True)
print(df5)
df5.drop([1], axis=0, inplace=True)
print(df5)

```

<img src="https://img-blog.csdnimg.cn/2020032122185939.PNG?#pic_center" alt="" width="500">
