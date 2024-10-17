
--- 
title:  Python 数据可视化之 seaborn 使用详解 
tags: []
categories: [] 

---
>  
  作者：yhlp 
  https://segmentfault.com/a/1190000017891341 
 

seaborn是python中的一个非常强大的数据可视化库，它集成了matplotlib，下图为seaborn的官网，如果遇到疑惑的地方可以到官网查看。http://seaborn.pydata.org/

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3JYY25PSzlLNENKNWVlU3U1SzUxdzRqdENwZU1QVjFUMjhoYU1NRTRIRG5TaWNRSGljUGVrOUFnLzY0MA?x-oss-process=image/format,png">

从官网的主页我们就可以看出，seaborn在数据可视化上真的非常强大。

1. 首先我们还是需要先引入库，不过这次要用到的python库比较多。

```
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

```

2. `sns.set_style()`：不传入参数用的就是seaborn默认的主题风格，里面的参数共有五种。
- darkgrid- whitegrid- dark- white- ticks
我比较习惯用whitegrid。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIVzZYa3U1aWFlSnJZZDdBSjBadmlhQkc4dEI0dXdYaWIzN2JVd0ZJNkNGV2xrMWpWSENpYWpqdnBxTHcvNjQw?x-oss-process=image/format,png">

3. 下面说一下seaborn里面的调色板，我们可以用`sns.color_palette()`获取到这些颜色，然后用`sns.palplot()`将这些色块打印出来。color_palette()函数还可以传入一些参数。

```
sns.palplot(sns.color_palette("hls",n))#显示出n个不同颜色的色块
sns.palplot(sns.color_palette("Paired",2n))#显示出2n个不同颜色的色块，且这些颜色两两之间是相近的
sns.palplot(sns.color_palette("color"))#由浅入深显示出同一颜色的色块
sns.palplot(sns.color_palette("color_r"))##由深入浅显示出同一颜色的色块
sns.palplot(sns.color_palette("cubehelix",n))#显示出n个颜色呈线性变化的色块
sns.palplot(sns.cubehelix_palette(k,start=m,rot=n))#显示出k个start(0,3)为m，rot(-1,1)为n的呈线性变化的色块
sns.palplot(sns.light_palette("color"))#将一种颜色由浅到深显示
sns.palplot(sns.dark_palette("color"))#将一种颜色由深到浅显示
sns.palplot(sns.dark_palette("color",reverse=bool))#reverse的值为False，则将一种颜色由深到浅显示；若为True，则将一种颜色由浅到深显示

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV2RMaWFTdlVKRHdzemljYnRUTlRCaWM5Y2NQSUwwMXg0d1Z2MFlhQkdRa095MktsWlFVUGgxU1hNQS82NDA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV0RESHlBVkpvWHBEYUpZSzFGelBsUW15UzdMOXRWWkpXSWpOSk1OcW5udkpXTnRuY0h1aldjZy82NDA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV0xXSTF4aWJKV0dZbWdoNUcxczNDUDJ3V0l2eFFhOW10eVNrd1FzOExHbFNvSXJIUUs3bE5TNGcvNjQw?x-oss-process=image/format,png">

4. `sns.kdeplot(x,y,cmap=pal)`：绘制核密度分布图。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV1laSW1kOXZmdklLR1dVZzJLWmQ0QUVURG5uWWVFNEMySDd5VnhadDYyOU9rTHRzaWFMcUhydHcvNjQw?x-oss-process=image/format,png">

5. `sns.distplot(x,kde=bool,bins=n)`：kde代表是否进行核密度估计，也就是是否绘制包络线，bins指定绘制的条形数目。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3pYaWFHSW9IQ3Nic1d1T1pCbVdTOXlEYW1pYnFhck04Ynp5Q2liSkJTRTFFazR6V2ViYjBCUjNLdy82NDA?x-oss-process=image/format,png">

6. 根据均值和协方差绘图：

首先我们要根据均值和协方差获取数据

```
mean,cov = [m,n],[(a,b),(c,d)]#指定均值和协方差
data = np.random.multivariate_normal(mean,cov,e)#根据均值和协方差获取e个随机数据
df = pd.DataFrame(data,columns=["x","y"])#将数据指定为DataFrame格式

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3FxbXE0ZVprTUNqMWZiQ1RvSE9COXFXS005cVdoMFpSbFlWZUJFcFJTbFBURk8zdHBtSEhvdy82NDA?x-oss-process=image/format,png">

然后绘制图像

```
sns.jointplot(x="x",y="y",data=df) #绘制散点图

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV2hVUHVsekRQUjVaY2hLdmtUb1M4M3RXNmhzUzlxWWhVMmNpYWJ4ZXprOTZCNWVldlBlWHFHWncvNjQw?x-oss-process=image/format,png">

用`sns.jointplot(x="x",y="y",data=df)`可以绘制出x和y单变量的条形图以及x与y多变量的散点图。

7. 在jointplot()函数中传入kind=“hex”，能够在数据量比较大时让我们更清晰地看到数据的分布比重。

```
x,y = np.random.multivariate_normal(mean,cov,2000).T
with sns.axes_style("white"):
    sns.jointplot(x=x,y=y,kind="hex",color="c")

```

绘制出的图像如下

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV1d0bzl5T2padDJKaWM3dFI5Z0tVY2Z6elVDWWdBczZheDZVUjNnZ3luN2ljcEdveWxLaWFjYTFhQS82NDA?x-oss-process=image/format,png">

8. `sns.pairplot(df)`：绘制出各变量之间的散点图与条形图，且对角线均为条形图。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV0ozS2pmc3NjdE1HWnR2VlptclJJVWFuVTBROG54VVdOUEhSVGpicm1OcTk5RjdlTTZ2OXVpYkEvNjQw?x-oss-process=image/format,png">

在这里我们可以先使用`df = sns.load_dataset("")`将seaborn中原本带有的数据读入或用pandas读取。

9. 绘制回归分析图：这里可以用两个函数`regplot()`和`lmplot()`，用regplot()更好一些。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3hEV2ljVzdPSTRpY25HeklJekpZNlFzYTYyYkVhQ2ZsaWJnSXBxZE13WUFpYXJBNDRMQ2xPM0ZjNHcvNjQw?x-oss-process=image/format,png">

如果两个变量不适合做回归分析，我们可以传入`x_jitter()`或`y_jitter()`让x轴或y轴的数据轻微抖动一些，得出较为准确的结果。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIVzJvV3hsQnRKNEZOaWMzazdtalFDZFU0N1Q2bkVaWkRJcVRyQWZSbHdocjZLMFVnT3ZRcThNOWcvNjQw?x-oss-process=image/format,png">

10. `sns.stripplot(x="",y="",data=df,jitter=bool)`：绘制一个特征变量中的多个变量与另一变量关系的散点图，jitter控制数据是否抖动。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV2lidHNmdjFpYU9NejFDNWliZWdhWDBmNmM3MUo3M25neHZ6cEFQRDU5OGNLZW1JNU5pYWljaWJ4azFxUS82NDA?x-oss-process=image/format,png">

11. `sns.swarmplot(x="",y="",hue="",data=df)`：绘制页状散点图，hue指定对数据的分类，由于在大量数据下，上面的散点图会影响到我们对数据的观察，这种图能够更清晰地观察到数据分布。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIVzVnTDlUazJHcEwycVlSN2sxTUFVbmlhMmo5SUdYdHQ1NjN2WHRyMnV0YWJuWFcza2liaWFiOHdXUS82NDA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIVzNEYVRjeFN3U3VTdlIzMFpDMDRxaWNMcjVNU3cyRVFHV3R5UW9HWDFTblN1V2RUa1B3MFF4ZmcvNjQw?x-oss-process=image/format,png">

12. `sns.boxplot(x="",y="",hue="",data=df，orient="h")`：绘制盒形图，hue同样指定对数据的分类。在统计学中有四分位数的概念，第一个四分位记做Q1，第二个四分位数记做Q2，第三个四分位数记做Q3，Q3-Q1得到的结果Q叫做四分位距，如果一个数n,n的范围是n&lt;Q1-1.5Q或n&gt;Q3+1.5Q，则称n为离群点，也就是不符合数据规范的点，利用盒形图可以很清晰地观察到离群点。如果传入orient则画出的盒形图是横向的。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV2ZDQU1HaWF0UWFncGJIbGFQUXFoTXJvQ2ZKdHRvMlRkOGljT3l4TzBrQ3dYZGliN2NnaWFKNmN0dkEvNjQw?x-oss-process=image/format,png">

13. `sns.violinplot(x="",y="",data=df,hue="",split=bool)`：绘制小提琴图，split表示是否将两类数据分开绘制，如果为True，则不分开绘制，默认为False。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV0doYTJLOGpjbmVKalBscGliUFoxaWJYRktBQTFmUGgxVGpwaWJMaklWRkZQbFpOaWJnMzJtU2VoQVEvNjQw?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3ZFVG9wUWM0Z2lhdklKN0dDYzNOTEhpYWlhZzU0RncxY0taWFI0cE40REdBQXVMSTkxQXIwckdXUS82NDA?x-oss-process=image/format,png">

14. 还可以将页状散点图和小提琴图在一起绘制，只需将两个绘图命令

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3dVU2J2RWdJajZaTmlhWDVaNjd4SE9ESnBnVmFYbVhrS0hUNTRuZW5aUDhEd0NuYXI5V3BSd2cvNjQw?x-oss-process=image/format,png">

inner="None"表示去除小提琴图内部的形状。

15. `sns.barplot(x="",y="",hue="",data=df)`：按hue的数据分类绘制条形图。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3NmdjJaZTQ0NW44dk5VbmNROW1pY2thWGFHYjVweUk4NFZ3OXc2cXBxa3hXbEN0aWFpYzRmUjE4US82NDA?x-oss-process=image/format,png">

16. `sns.pointplot(x="",y="",hue="",data=df)`：绘制点图，点图可以更好的描述数据的变化差异。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV2phc1pyVHZNTXJ1TmliM1F1YlA1OFVxS0toSmxVMnREOTBiOVdyV0o0OWZJb21VaWJpY2NhTWpBQS82NDA?x-oss-process=image/format,png">

17. 我们还可以传入其他参数：

```
sns.pointplot(x="class",y="survived",hue="sex",data=titanic,
             palette={"male":"#02ff96","female":"#0980e6"},#指定曲线的颜色
             markers=["s","d"],linestyles=["-","-."])#指定曲线的点型和线型

```

绘制出的图像如下

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV29GUDJZTUpNV2xzRnc5Smljekg4MGNNaGhDNG9nMmRpY1VHUDcxdDdFUzZkOVRrV3UxbzhHcGtRLzY0MA?x-oss-process=image/format,png">

18. `sns.factorplot(x="", y="", hue="", data=df)`：绘制多层面板分类图。

```
sns.factorplot(x="day",y="total_bill",hue="smoker",data=tips)

```

绘制出的图像如下

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV1hyWFgyazN3SGliUjVuMkdOZWtzOEVITk9wUU00Q0g3VUhaRXVFaWNIRWFrYVRRaWNLMk01YUszUS82NDA?x-oss-process=image/format,png">

19. `sns.factorplot(x="",y="",hue="",data=df,kind="")`：kind中指定要画图的类型。

```
sns.factorplot(x="day",y="total_bill",hue="smoker",data=tips,kind="bar")

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3lmdXprdmxVMU9CVGVKajNBbnJHbTFqdFhEVk5vaWM1Ynd4RWZnbVhuRjR4OTdpY0tlOXFsbFlnLzY0MA?x-oss-process=image/format,png">

```
sns.factorplot(x="day",y="total_bill",hue="smoker",col="time",data=tips,kind="swarm")

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV1BHY2liSjVYYXV2aWNZcUtVcXF0T0lkQVN5M0p5SnQ4Y2liNmpwdkw1aWNkUEhwM0tXRjRyRG5SY0EvNjQw?x-oss-process=image/format,png">

```
sns.factorplot(x="time",y="total_bill",hue="smoker",col="day",data=tips,kind="box",size=5,aspect=0.8) #aspect指定横纵比

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV1VPRmh5V2o1cnUwUW8yZ0pqaWJUb3hpY0kxQndwYzFXQ2pYVFJ5UWhJZWxnam4wV1RvdEFVMmd3LzY0MA?x-oss-process=image/format,png">

20. `sns.factorplot()`的参数：
- x,y,hue 数据集变量 变量名。- date 数据集 数据集名。- row,col 更多分类变量进行平铺显示 变量名。- col_wrap 每行的最高平铺数 整数。- estimator 在每个分类中进行矢量到标量的映射 矢量。- ci 置信区间 浮点数或None。- n_boot 计算置信区间时使用的引导迭代次数 整数。- units 采样单元的标识符，用于执行多级引导和重复测量设计 数据变量或向量数据。- order, hue_order 对应排序列表 字符串列表。- row_order, col_order 对应排序列表 字符串列表。- kind : 可选：point 默认, bar 柱形图, count 频次, box 箱体, violin 提琴, strip 散点，swarm 分散点 size 每个面的高度（英寸） 标量 aspect 纵横比 标量 orient 方向 "v"/"h" color 颜色 matplotlib颜色 palette 调色板 seaborn颜色色板或字典 legend hue的信息面板 True/False legend_out 是否扩展图形，并将信息框绘制在中心右边 True/False share{x,y} 共享轴线 True/False。
21. `sns.FacetGrid()`：这是一个很重要的绘图函数。

```
g = sns.FacetGrid(tips,col="time")
g.map(plt.hist,"tip")

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV2lidDJCWmw4OHNaSXZsNTE4RDlGZ25uZGRGN1N3YXU0VFM4bjZvZWliMGhFcGg0MFZ3czBqSlFnLzY0MA?x-oss-process=image/format,png">

```
g = sns.FacetGrid(tips,col="sex",hue="smoker",size=5,aspect=1)
g.map(plt.scatter,"total_bill","tip",alpha=0.3,s=100)#alpha指定点的透明度，s指定点的大小
g.add_legend()#添加图例

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV1Q2UmNSeWs2OGs3dHVTZUF3b1FoZnpRUUh5cExDWlAzSElUODdYMU9lSUVpY1RUVzZseFpDUEEvNjQw?x-oss-process=image/format,png">

```
g = sns.FacetGrid(tips,col="day",size=4,aspect=0.8)
g.map(sns.barplot,"sex","total_bill")

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIVzVSSzNmMk9lRUk1TDhCMTNvUGNtNTVzUUE2emxkaWJ1VjFuNTZBa0xBaWFDdEtpYzh2SWlhUDRxMXcvNjQw?x-oss-process=image/format,png">

22. `sns.PairGrid()`：将各变量间的关系成对绘制。

```
iris = sns.load_dataset("iris")
g = sns.PairGrid(iris)
g.map(plt.scatter)

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV2dkSHROZldJTG1POFNaaWJlckx3ck9PdUFlazRMd2hFOGtQanNnN2ZnbDkyaWEzOUFpYU1JcjQ1US82NDA?x-oss-process=image/format,png">

23. `g.map_diag()`和`g.map_offdiag()`：绘制对角线和非对角线的图形

                

```
g = sns.PairGrid(iris)
g.map_diag(plt.hist)    #指定对角线绘图类型
g.map_offdiag(plt.scatter)    #指定非对角线绘图类型

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV2JCek5mYUJLa2d2NXZGaGZDaWFxbWZYMUFRQTlTVnY0aWFIdDY0aWFxSElwcjZvNXlPTWljTlNOdEEvNjQw?x-oss-process=image/format,png">

```
g = sns.PairGrid(iris, hue="species")
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
g.add_legend()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3g5bWlhQkVBZmpZMGpuV0JSN3NRcDN1Y2ljVHhiNVZMOGljbTV4NTZhNTFHQ0JpYkFZdnFmeFlmbkEvNjQw?x-oss-process=image/format,png">

```
g = sns.PairGrid(iris, vars=["sepal_length", "sepal_width"], hue="species",size=3)
g.map(plt.scatter)

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV0JpYTFMamV4ZTNjd2VObVRGVnRsRTdFOE9XZFVJZVlhNjlGNVJvb3lJSWN0Nk1jMlhaQVJhaFEvNjQw?x-oss-process=image/format,png">

```
g = sns.PairGrid(tips, hue="size", palette="GnBu_d")
g.map(plt.scatter, s=50, edgecolor="white")
g.add_legend()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV1lPaWNwMnZacDQ1Qmc0S0JtTGV5TUp0UGxlNTBDTmo3aHBQNHBuSDQxaWJlelBQRXl5M3hhSXBBLzY0MA?x-oss-process=image/format,png">

24. `sns.heatmap()`：绘制热度图，热度图可以很清楚看到数据的变化情况以及变化过程中的最大值和最小值。

                

```
uniform_data = np.random.rand(3, 3)
print (uniform_data)
heatmap = sns.heatmap(uniform_data)

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV0dKUEp3ZzEwajFtTmVBMk9oUldKZ2t0S2FxUkZ3TmdxdnRQUkZZZ0tTSkxISVdCM1hXZTFSdy82NDA?x-oss-process=image/format,png">

25. 向heatmap()中传入参数`vmin=`和`vmax=`。

                

```
ax = sns.heatmap(uniform_data,vmin=0.2,vmax=0.5)  #超过最大值都是最大值的颜色，小于最小值都是最小值的颜色

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3QyTWJqcDd4QlpROUNQRFRvaHVjYUtHTGhiNkJuZ1BNc0pmSnBOU3U5S2hnbTVnVjJ1UXlDZy82NDA?x-oss-process=image/format,png">

26.

                

```
normal_data = np.random.randn(3, 3)
print (normal_data)
ax = sns.heatmap(normal_data, center=0)    #center指定右侧图例的中心值

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV0J0RU9ka2FaMmVva2tuRGRzNmlhQmVWZXdpYm5WbUtzMmppY1lXZ05RUE5ob3kyRWI2WHNPdTJjdy82NDA?x-oss-process=image/format,png">

27.

                

```
flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
ax = sns.heatmap(flights, annot=True,fmt="d",linewidth=0.5)    #annot指定是否显示数据，fmt指定数据的显示格式,linewidth指定数据格子间的距离

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV0UyMDhVZVE1aEtFNVphTGljQ0pTaWJ0M2VINGhQc1czeHVoQk5uQ29aVHFiYjVIdEpCcGdNck93LzY0MA?x-oss-process=image/format,png">

28.

```
ax = sns.heatmap(flights, cmap="YlGnBu",cbar=True) #cmap指定图形颜色，cbar表示是否绘制右侧图例。

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJclAzejlZejJ2b1pJWXVxUDhkOWRIV3NNZ0FMNm91V3drZzRVcW9YakVlWmtLQVhUWDhUMXdFcEVQd0pJV3dzY01LWkhwSDh3WkNhQS82NDA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcmNjSFVSRTF0ZmRnOWo5em9zbzYwNGdvWmtBeGpkdGNQSHo4WmFtaWJjakZiTUhMZGxNOG1RbWhveHZxbUpIUzRpY09hN2dSVGp2M1dBLzY0MA?x-oss-process=image/format,png">
