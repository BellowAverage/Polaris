
--- 
title:  【Pandas指南】初学者必备手册 
tags: []
categories: [] 

---
>  
  本文转自AI新媒体量子位（公众号 ID: QbitAI） 
 

数据可视化本来是一个非常复杂的过程，但随着Pandas数据帧plot()函数的出现，使得创建可视化图形变得很容易。

在数据帧上进行操作的plot()函数只是**matplotlib**中plt.plot()函数的一个简单包装 ，可以帮助你在绘图过程中省去那些长长的matplotlib代码。

最近，一位来自印度的小哥以2019年世界幸福指数的数据为例，详细讲述了在Pandas中plot()函数的各种参数设置的小技巧，熟练掌握这些技巧后，你也能绘制出丰富多彩的可视化图表。

### 导入数据

在绘制图形前，我们首先需要导入csv文件：

```
import pandas as pd
df=pd.read_csv(‘./world-happiness-report-2019.csv’)
df.head(3)

```

这个csv图标的内容是各个国家按照不同维度评价的幸福指数（数据下载地址见文末）：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTElNQ3BicW1zbHh5YjdYNHExaWNaUm1ONXhNaWFDb3ZLNXJjdTNLNFVVVnd2UUM5S1I5MDJaaEJnLzY0MA?x-oss-process=image/format,png" width="1117">

数据帧中一些列的名称比较冗长，可以重命名使其更加简洁：

```
df.rename(columns={“Country (region)”: “Country”, “Log of GDP\nper capita”: “Log_GDP_per_capita”, “Healthy life\nexpectancy”:”Health_life_expect”},inplace=True)
df.column
```

### 绘制柱状图、散点图等常见图形

从最近简单的**柱状图**开始，只统计腐败程度、自由度、宽容度、社会支持等几个维度

```
%matplotlib tk
df1=df[:5]
df1.plot(‘Country’,[‘Corruption’,’Freedom’,’Generosity’,’Social support’],kind = ‘bar’
```

嫌直接写名称太麻烦？没关系，我们也可以用所在列的数字来绘制，比如上述4个列分别为7、6、8、5：

```
%matplotlib tk
df1=df[:5]
df1.plot(‘Country’,[7,6,8,5],kind = ‘bar’)
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTEh3eTlNQTd0bEhJdDJXZ3RiejBreUkxaktBRXlGQjdobTdDaWF2YTFmSGhKUmJlUVZjZUN0WncvNjQw?x-oss-process=image/format,png" width="1551">

在上面的代码中kind = ‘bar’，所以绘制的图形是柱状图，如果我们把参数改成kind = ‘line’，画出的就是**线状图**。

```
df1=df[:5]
df1.plot(‘Country’,[‘Corruption’,’Freedom’,’Generosity’,’Social support’],kind = ‘line’)
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTHlkRG9SaWJ1RDVycVkxcHpJNEpIVVNya2JYZGJlaWEydmhGN1E2WHJiMnJ4WW9pYjA0ZGUwMGNOQS82NDA?x-oss-process=image/format,png" width="715">

同样的，如果把参数改成kind = ‘line’，还能绘制出箱形图：

```
df[:5].plot(x=’Country’,kind=’box’)

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTER2QXplWHpDMmE4TXBpYm9wR2FNem5MYm83cEdqcHBwZnFYS2RYRnBRdndKelJtYUpQOWU0R0EvNjQw?x-oss-process=image/format,png" width="1533">

对于散点图，设置**kind=’scatter’**，绘制出腐败程度与自由度之间的关系，用color=’R’将点定义为红色：

```
df.plot(x=’Corruption’,y=’Freedom’,kind=’scatter’,color=’R’)

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTEJjZHVMQjRHRmtDeHlTdnNxM2MwVVM4VFRFTmJXYmJIUWpCa1RpY0VWQTBVOUFnYzJEcVdDRkEvNjQw?x-oss-process=image/format,png" width="716">

此外，Pandas中还有一个辅助函数pandas.plotting.table，它创建一个来自数据帧的表格，并将其添加到matplotlib Axes实例中。

```
from pandas.plotting import table
df1=df[:5]
df1=df.loc[:5,[‘Country (region)’,’Corruption’,’Freedom’,’Generosity’,’Social support’]]
ax=df1.plot(‘Country (region)’,[‘Corruption’,’Freedom’,’Generosity’,’Social support’], kind = ‘bar’, title =’Bar Plot’,legend=None)
table(ax, np.round(df1.describe(), 2),loc=’upper right’)
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTGJTUmIweXlnTDZRTWliNlljeElpYjlsd1N3Ym9JNm9zUjZPZXJIcFhpY2RSNzJNdGNqUXZHWFBUZy82NDA?x-oss-process=image/format,png" width="1024">

### 坐标轴的设置

#### 取值范围

使用xlim和ylim两个参数可设置x和y轴的范围。在折线图中，我们要将x轴设置为0到20，y限制为从0到100。

```
df1=df[:20]
df1[‘Freedom’].plot(kind=’line’,xlim=(0,20),ylim=(0,100))
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTEg5Y2lhc1NsUjU4NEVEUDl4ZXJrSkNQNUFRMHoxZmw2VHc1Vk80SDVsUUFwNjRpY05lS0ZlcjZBLzY0MA?x-oss-process=image/format,png" width="695">

#### x、y轴刻度

有时候坐标轴上的刻度并不理想，我们希望在上面标上我们喜欢的数值。

比如对于x轴，我们想要标上0、10、15和20几个值；对于y轴，我们想要标上0、50、70、100几个值，可以在**xticks**和**yticks**参数中悉数列出。

```
df[:20][‘Freedom’].plot(kind=’line’,xlim=(0,20),ylim=(0,100),color=’red’,xticks=([0,10,15,20]),yticks=([0,50,70,100]), title = ‘xticks’)

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTElhU1VBdGY1a2lhSUdYTzdMUmh2b25oTkpOU2tJRkI1SjBLSHRsMjlxMk0ySnVDYk5tSDNzWFEvNjQw?x-oss-process=image/format,png" width="686">

但是用列表来制定坐标刻度的方法，在数值太多的时候就比较麻烦了，因此我们还能通过指定刻度间隔的方法来绘制坐标轴，比如指定x轴间隔是1，y轴间隔是10：

```
df[:20][‘Freedom’].plot(kind=’line’,xlim=(0,20),ylim=(0,100),color=’red’,xticks=([w1 for w in range(20)]),yticks=([w10 for w in range(40)]))

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTExDbU1PTGlicDl5ODFuNXRlVzZwaWFVVzEwUXpnNGtTa2tGbWlhZ3MzazV3NTRvTEdncmRraElTUS82NDA?x-oss-process=image/format,png" width="682">

如果我们不希望在坐标轴上看到数字，而是想要设置标签。我们还可以将x轴标签更改为文本标签“低、中、高”这种样式。

```
ax=df[:20][‘Freedom’].plot(kind=’line’,xlim=(0,20),ylim=(0,100),color=’red’,xticks=([0,10,20]),yticks=([w*30 for w in range(40)]))
ax.set_xticklabels([‘Low’,’Med’,’High’])
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTG1LcjhzWGliT1JJSlJPQ212QnBTSEN0MThNMGVpY2VwWFJpY1BJSFJaZ0pNSktGZlhNNGw1dGVsQS82NDA?x-oss-process=image/format,png" width="687">

#### 对数坐标

如果数据的跨度范围非常大，横跨好几个数量级，那么用线性坐标就无法很好地展示数据。这时候我们需要用到对数坐标，设置方法是将**logx**或者**logy**的值设置为**Ture**。

如果我们只想设置x轴为对数坐标，y轴仍保持线性坐标，那么

```
df[:20][‘Freedom’].plot(kind=’line’,xlim=(0,1000),ylim=(0,100),color=’red’,logx=True)

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTGFMSWxiMGZyaWJ0NkpaNVdzVkRPSEFaUTZGdXdTbUp4WFFHWTRnbzFIYmY3WTM1Ynd4clpjeXcvNjQw?x-oss-process=image/format,png" width="674">

### 其他高阶用法

可以使用**stacked**参数来绘制带有条形图的**堆叠图**。在这里，我们绘制堆叠的水平条，stacked设置为True。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTEZ5UUJzaWJvbU03TWdjeU1sSEowUTJtM0I2cXRqWHpLNk5pYVh4RExpY1hpYlFGak5EVzlBcGh3dHcvNjQw?x-oss-process=image/format,png" width="1024">

将grid参数设置为True，可以给图表加入网格。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTDMxY1llbE12UVFlaFJwaWNFSHl4OUxZRWMxVmljcXZ0d1R4ZFBPOFJWTkFjNzRvUDQ3eWlib3BnQS82NDA?x-oss-process=image/format,png" width="719">

有了subplot参数还可以绘制子图，根据需要指定行数和列数以及绘图的数量。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZaWNVaGs1YUFHdEJKQ0tMNUQ4ekhaV2c3SkE0dGlicGlhTE5FQnBldVUwWmVpY05VMEVHVUlsT2lhNzJpYUQxSGhkaWNwS2xpYnFBbDM1eEJvRUp3RklwVzB2MXZ3LzY0MA?x-oss-process=image/format,png" width="1588">

在上面的子图中，我们没有给子图添加标题。当subplot 设置为True 时，在设置一组title的值，即可在列表上方加入标题。

>  
  原文链接：   
  https://kanoki.org/2019/09/16/dataframe-visualization-with-pandas-plot/   
  表格下载地址：  
  https://www.kaggle.com/PromptCloudHQ/world-happiness-report-2019/version/1  
  作者系网易新闻·网易号“各有态度”签约作者 
 

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">

分享或在看是对我最大的支持
