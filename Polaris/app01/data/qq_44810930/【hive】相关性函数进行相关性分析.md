
--- 
title:  【hive】相关性函数进行相关性分析 
tags: []
categories: [] 

---


#### 文章目录
- - - - - 


在Hive SQL中，使用类似的相关性函数进行相关性分析。常见的相关性函数包括CORR、COVAR_POP、COVAR_SAMP、STDDEV_POP、STDDEV_SAMP等。

## CORR

举个例子，假设有一个表格sales，其中包含两列数据`sales_amt`和`advertising_amt`，我们可以使用CORR函数来计算这两列数据的相关性：

```
SELECT CORR(sales_amt, advertising_amt) as correlation
FROM sales;

```

这将返回一个值，表示sales_amt和advertising_amt之间的相关性，值范围从-1到1。
- 如果结果为正，则表示两列数据之间呈正相关关系；- 如果结果为负，则表示两列数据之间呈负相关关系；- 如果结果接近于0，则表示两列数据之间几乎没有相关性。
## COVAR_POP

COVAR_POP函数是用于计算总体协方差的Hive SQL函数。它用于衡量两个变量之间的线性关系强度及方向。

COVAR_POP函数的语法如下：

```
COVAR_POP(expression1, expression2)

```

其中，expression1和expression2是需要计算协方差的两个数值表达式或列名。COVAR_POP函数返回的是这两个变量的总体协方差。

总体协方差（Population Covariance）是基于整个总体的样本数据计算得出的协方差。它衡量了两个变量在总体层面上的线性关系。协方差的结果可以为正、负或零，正值表示正相关，负值表示负相关，零表示无相关性。

需要注意的是，COVAR_POP函数的结果不具有标准化，无法直接进行比较。如果需要进行比较，可以使用相关性函数（如CORR）来衡量两个变量之间的相关性强度。

## COVAR_SAMP

COVAR_SAMP函数是用于计算样本协方差的Hive SQL函数。它用于衡量两个变量之间的线性关系强度及方向。

COVAR_SAMP函数的语法如下：

```
COVAR_SAMP(expression1, expression2)

```

其中，expression1和expression2是需要计算协方差的两个数值表达式或列名。COVAR_SAMP函数返回的是这两个变量的样本协方差。

样本协方差（Sample Covariance）是基于样本数据计算得出的协方差，它用于估计总体协方差。与总体协方差类似，样本协方差的结果可以为正、负或零，表示两个变量之间的线性关系情况。

需要注意的是，样本协方差是样本统计量，对总体协方差进行估计。在实际应用中，通常使用样本协方差来估计总体协方差，并结合其他统计指标进行综合分析。

## STDDEV_POP

STDDEV_POP函数是用于计算总体标准差的Hive SQL函数。它用于衡量一组数据的离散程度或变异程度。

STDDEV_POP函数的语法如下：

```
STDDEV_POP(expression)

```

其中，expression是需要计算标准差的数值表达式或列名。STDDEV_POP函数返回的是这组数据的总体标准差。

总体标准差（Population Standard Deviation）是基于整个总体的样本数据计算得出的标准差。它衡量了数据点相对于均值的离散程度。标准差越大，表示数据点越分散；标准差越小，表示数据点越集中在均值附近。

总体标准差的计算公式为：[ \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2} ]

其中，N表示总体样本容量，(x_i) 表示每个样本数据点，(\mu) 表示总体均值。

在实际应用中，总体标准差常用于描述整个总体数据的离散程度，帮助分析数据的分布情况。

## STDDEV_SAMP

STDDEV_SAMP函数是用于计算样本标准差的Hive SQL函数。它用于衡量一组样本数据的离散程度或变异程度。

STDDEV_SAMP函数的语法如下：

```
STDDEV_SAMP(expression)

```

其中，expression是需要计算标准差的数值表达式或列名。STDDEV_SAMP函数返回的是这组样本数据的样本标准差。

样本标准差（Sample Standard Deviation）是基于样本数据计算得出的标准差，用于估计总体标准差。它衡量了样本数据点相对于样本均值的离散程度。与总体标准差类似，样本标准差越大表示样本数据点越分散，越小表示样本数据点越集中在均值附近。

样本标准差的计算公式为：[ \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2} ]

其中，n表示样本容量，(x_i) 表示每个样本数据点，(\bar{x}) 表示样本均值。

在实际应用中，样本标准差常用于描述样本数据的离散程度，帮助分析样本数据的分布情况，并通过样本标准差来估计总体标准差。需要注意的是，样本标准差通常用于对样本数据的统计推断，而总体标准差用于对整个总体的统计推断。
