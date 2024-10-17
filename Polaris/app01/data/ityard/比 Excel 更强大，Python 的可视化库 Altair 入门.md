
--- 
title:  比 Excel 更强大，Python 的可视化库 Altair 入门 
tags: []
categories: [] 

---
>  
  原作者 Parul Pandey  
  晓查 编译整理 
  量子位 出品 | 公众号 QbitAI 
 

数据转化成更直观的图片，对于理解数据背后的真相很有帮助。如果你有这方面的需求，而且还在使用Python，那么强烈推荐你试一试Altair。

**Altair**是一个专为Python编写的可视化软件包，它能让数据科学家更多地关注数据本身和其内在的联系。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTRjNvcEFuUXg3aWJuSk5KaWFVRXhGVUNhQ2NOcndWMlB0cUdVeGExc1JKZ09NVWJRNWdvUzQzY0EvNjQw?x-oss-process=image/format,png">

Altair由华盛顿大学的数据科学家Jake Vanderplas编写，目前在GitHub上已经收获超过3000星。

最近，Medium上一位小姐姐Parul Pandey分享了Altair的入门教程，希望对从事数据科学的用户有帮助。

## 使用教程

Parul以汽车数据为例，将一个汽车数据集“cars”载入到Altair中。

cars中包含汽车的生产年份、耗油量、原产国等9个方面的数据，后面将对这些内容进行可视化处理。

### 安装和导入Altair软件包

除了安装Altair和它的依赖软件外，还需要安装其他前端工具，比如Jupyter Notebook、JupyterLab、Colab等等。

Parul小姐姐推荐安装JupyterLab：

$ pip install -U altair vega_datasets jupyterlab

需要注意的是，由于Altair的教程文档中还包含vega数据集，因此也需要一并安装上。

接着在终端中输入：jupyter lab，就能在你的浏览器中自动打开它啦。

在代码开头别忘了导入Altair：

```
import altair as alt


```

完成以上准备工作，我们就可以开始绘图了

### 开始绘制图表

Altair中的基本对象是**Chart**，它将数据框作为单个参数。你可以这样定义它：

```
chart = alt.Chart(cars)


```

Chart有三个基本方法：**数据**（data）、**标记**（mark）和**编码**（encode），使用它们的格式如下：

```
alt.Chart(data).mark_point().encode(
encoding_1='column_1',
encoding_2='column_2',

# etc.)


```

数据顾名思义，直接导入cars数据集即可。标记和编码则决定着绘制图表的样式，下面着重介绍这两部分。

**标记**可以让用户在图中以不同形状来表示数据点，比如使用实心点、空心圆、方块等等。

如果我们只调用这个方法，那么所有的数据点都将重叠在一起：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTU0tBMDk5OFN3WGhabHZBb05naDRWTkM4YzV1ZnhrYm84dTl0MUkydUZVTjNYRXh3OVZONXdnLzY0MA?x-oss-process=image/format,png">

这显然是没有意义的，还需要有**编码**来指定图像的具体内容。常用的编码有：

**x**: x轴数值**y**: y轴数值**color**: 标记点颜色**opacity**: 标记点的透明度**shape**: 标记点的形状**size**: 标记点的大小**row**: 按行分列图片**column**: 按列分列图片

以汽车的耗油量为例，把所有汽车的数据绘制成一个一维散点图，指定x轴为耗油量：

```
alt.Chart(cars).mark_point().encode(
x='Miles_per_Gallon'
)


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTZlRhWXlMbkZYeHdDeTQwazBnNjgxdUwzMWliMUdUV2libk1ITWwwbFFFaWJFczRGSTZ0UkJJWXJ3LzY0MA?x-oss-process=image/format,png">

但是使用mark_point()会让所有标记点混杂在一起，为了让图像更清晰，可以替换成棒状标记点mark_tick()：

```
alt.Chart(cars).mark_tick().encode(
x='Miles_per_Gallon'
)


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTaWNESEtxOU9QV2tzUWQ3dmlhd2hZTDhoT2lhYmdXR0ZpY0hsdXhpYlJRMlJpYTM0SmxzTzlrMW10Tm1nLzY0MA?x-oss-process=image/format,png">

以耗油量为X轴、马力为Y轴，绘制所有汽车的分布，就得到一张二维图像：

```
alt.Chart(cars).mark_line().encode(
x='Miles_per_Gallon',
y='Horsepower'
)


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTSzVlUTI0aWJ1QzJQWGoxNWRPd1hHbG05SEJTZzhlUHNRY2NSWGdXN29qS0N2UDFId3lNTlpYdy82NDA?x-oss-process=image/format,png">

### 给图表上色

前面我们已经学会了绘制二维图像，如果能给不同组的数据分配不同的颜色，就相当于给数据增加了第三个维度。

```
alt.Chart(cars).mark_point().encode(
x='Miles_per_Gallon',
y='Horsepower',
color='Origin'
)


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTZk5oVzRyaWNQaWFsUzE0OGsxemliakxFeVgwUVVpYk5acUpTTUlOa2lhcVNaUEZaaWJoUFdjODk1ZFJBLzY0MA?x-oss-process=image/format,png">

上面的图中，第三个维度“原产国”是一个离散变量。

使用颜色刻度表，我们还能实现对**连续变量**的上色，比如在上图中加入“加速度”维度，颜色越深表示加速度越大：

```
alt.Chart(cars).mark_point().encode(
x='Miles_per_Gallon',
y='Horsepower',
color='Acceleration'
)


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTSGljVE5YR2liQVlDejREZmtNTWRyMzhTWVo5ZHdYUU02OVhPTWpzNnZBcE1wbm1ESWlhSWliTTJ3US82NDA?x-oss-process=image/format,png">

### 数据的分类与汇总

上面的例子中，我们使用的主要是散点图。实际上，Altair还能方便地对数据进行分类和汇总，绘制统计直方图。

相比其他绘图工具，Altair的特点在于不需要调用其他函数，而是直接在数轴上进行修改。

例如统计不同油耗区间的汽车数量，对X轴使用alt.X()，指定数据和间隔大小，对Y轴使用count()统计数量。

```
alt.Chart(cars).mark_bar().encode(
x=alt.X('Miles_per_Gallon', bin=alt.Bin(maxbins=30)),
y='count()'
)


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTM01tZWV3ZE50cGtBWjJaRlB5QllLVUlhckZjemJMbFBucVlmc0w0anpORkdlMGpjMFd0T0dnLzY0MA?x-oss-process=image/format,png">

为了分别表示出不同原产国汽车的油耗分布，前文提到的上色方法也能直方图中使用，这样就构成一幅分段的统计直方图：

```
alt.Chart(cars).mark_bar().encode(
x=alt.X('Miles_per_Gallon', bin=alt.Bin(maxbins=30)),
y='count()',
color='Origin'
)


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTVkpZaExnVUMwbUdxOGljY05jb2NSem1MMTVNYXg3Y0RwaWNTcnNxMmliY3ZsOHBTV2libkZpYm43N2cvNjQw?x-oss-process=image/format,png">

如果你觉得上图还不够直观，那么可以用column将汽车按不同原产国分列成3张直方图：

```
alt.Chart(cars).mark_bar().encode(
x=alt.X('Miles_per_Gallon', bin=alt.Bin(maxbins=30)),
y='count()',
color='Origin',
column='Origin'
)


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTcWRjTHZBMm5nTHNIOGlhbWF0WXhSN1dMOXEzOFBQaWNjS2dKVURqS3E5V090SjB3UUhKV3RBdVEvNjQw?x-oss-process=image/format,png">

### 交互

除了绘制基本图像，Altair强大之处在于用户可以与图像进行交互，包括平移、缩放、选中某一块数据等操作。

在绘制图片的代码后面，调用interactive()模块，就能实现平移、缩放：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTejJYemsyOGNVaWJhWjdaeGxpYUhWeDMwcXY4MHNvTEF4SG5PT0JsWE9qd0ljUDdFbzV0aWNxU0x3LzY0MA?x-oss-process=image/format,png">

Altair还为创建交互式图像提供了一个selection的API：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTMFg0ZDFxc3Z2aGVCbTRZWkpWRkhpYVZZYWRFcFFlWlBwMUlTNmFJc1I0Sk1xcWE5ZTFyelVkQS82NDA?x-oss-process=image/format,png">

在选择功能上，我们能做出一些更酷炫的高级功能，例如对选中的数据点进行统计，生成实时的直方图。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTVFNjMU9FcXptNEw1b3UwU1cxS3hlSG9LTWliQVljbGppYmxOb1hTaWF3TE82WUtqaWFVTk1FbmZ1dy82NDA?x-oss-process=image/format,png">

### 叠加多个图层

如果把前面的汽车耗油量按年度计算出平均值：

```
alt.Chart(cars).mark_point().encode(
x='Miles_per_Gallon',
y='Horsepower',
color='Acceleration'
)


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTQlJZMm10YUpZNG1PTU1TVTdxSWJjeXVHek4wZE9USXYydWZKN0lrVnpDWWpjc0pYdzBya3NRLzY0MA?x-oss-process=image/format,png">

在统计学上，我们还能定义平均值的置信区间，为了让图表更好看，可以分别列出三个不同产地汽车的耗油量平均值置信区间：

```
alt.Chart(cars).mark_area(opacity=0.3).encode(
x=alt.X(‘Year’, timeUnit=’year’),
y=alt.Y(‘ci0(Miles_per_Gallon)’, axis=alt.Axis(title=’Miles per Gallon’)),
y2=’ci1(Miles_per_Gallon)’,
color=’Origin’
).properties(
width=600
)


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTc3RSdmViMHdNNXNtdmlicWFvZjNNd2tBUjFpY1JIcHFPRzVwNm1FTkZyUzhhYTZucU5QTGpCS2cvNjQw?x-oss-process=image/format,png">

最后我们可以用图层API将平均值和置信区间两幅图叠加起来：

```
spread = alt.Chart(cars).mark_area(opacity=0.3).encode(
x=alt.X('Year', timeUnit='year'),
y=alt.Y('ci0(Miles_per_Gallon)', axis=alt.Axis(title='Miles per Gallon')),
y2='ci1(Miles_per_Gallon)',
color='Origin'
).properties(
width=800
)
lines = alt.Chart(cars).mark_line().encode(
x=alt.X('Year', timeUnit='year'),
y='mean(Miles_per_Gallon)',
color='Origin'
).properties(
width=800
)
spread + lines


```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdENuZEFnNmJzT2lia0hNZURsWkdMcThTak1Va3o5RkJiWFppYklHRXZPdGhjVVF0UGhqRmljVWNpYVljMDhDNjUzUlNpYmdXUXJsNFdSa2liTmcvNjQw?x-oss-process=image/format,png">

## 更多内容

本文只是介绍了Altair的一些基本使用方法，远远不能涵盖它所有的功能。如果需要了解更多，请参阅GitHub页说明：https://github.com/altair-viz/altair

教程原文：https://medium.com/analytics-vidhya/exploratory-data-visualisation-with-altair-b8d85494795c

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcmNjSFVSRTF0ZmRnOWo5em9zbzYwNGdvWmtBeGpkdGNQSHo4WmFtaWJjakZiTUhMZGxNOG1RbWhveHZxbUpIUzRpY09hN2dSVGp2M1dBLzY0MA?x-oss-process=image/format,png">
