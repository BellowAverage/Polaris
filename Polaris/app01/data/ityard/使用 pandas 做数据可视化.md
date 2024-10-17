
--- 
title:  使用 pandas 做数据可视化 
tags: []
categories: [] 

---
>  
  来源：大邓和他的Python 
 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1Nuekh2ODBWUzJYeGNGNEJpYjUzazJUcTZ6QWhMOTZVaWJLdkhwNlJNd2I3c2VrMU8wZzlmaHhqR0ZpYncvNjQw?x-oss-process=image/format,png">

数据可视化可以让我们很直观的发现数据中隐藏的规律，察觉到变量之间的互动关系，可以帮助我们更好的给他人解释现象，做到一图胜千文的说明效果。

常见的数据可视化库有:
- matplotlib 是最常见的2维库，可以算作可视化的必备技能库，由于matplotlib是比较底层的库，api很多，代码学起来不太容易。- seaborn 是建构于matplotlib基础上，能满足绝大多数可视化需求。更特殊的需求还是需要学习matplotlib- pyecharts 上面的两个库都是静态的可视化库，而pyecharts有很好的web兼容性，可以做到可视化的动态效果。
但是在数据科学中，几乎都离不开pandas数据分析库，而pandas可以做
- 数据采集 - 数据读取  pd.read_csv/pd.read_excel- 数据清洗(预处理)  - **可视化，兼容matplotlib语法(今天重点)**
在本文我们可以学到用pandas做
- 导入数据- 绘制最简单的图plot()- 多个y的绘制图- 折线图、条形图、饼形图和散点图绘制- 统计信息绘图- 箱型图- 轴坐标刻度- plot()更多精细化参数- 可视化结果输出保存
#### **准备工作**

如果你之前没有学过pandas和matpltolib,我们先安装好这几个库

```
!pip3 install numpy
!pip3 install pandas
!pip3 install matplotlib

```

已经安装好，现在我们导入这几个要用到的库。使用的是伦敦天气数据，一开始我们只有12个月的小数据作为例子

```
#jupyter notebook中需要加这行代码
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#读取天气数据
df = pd.read_csv('data/london2018.csv')
df

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhmZXNqVW9CZWVHYXNvamQ5MDRnQjZpYVNsOEhaZFpJaWNxWlNXUFhudnVRTmxtOGRVTjRrYXUxUS82NDA?x-oss-process=image/format,png">

#### **plot最简单的图**

选择Month作为横坐标，Tmax作为纵坐标，绘图。

大家注意下面两种写法

```
#写法1
df.plot(x='Month', y='Tmax')
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhRcVFpYTRvYU5zN3NZcExkRXc0VU1TVUo1WmljaWJremlhZENiQnBOaWEzdW1rdW1Edkl0RlEwSFE1dy82NDA?x-oss-process=image/format,png">
- 横坐标轴参数x传入的是df中的列名Month- 纵坐标轴参数y传入的是df中的列名Tmax
#### **折线图**

上面的图就是折线图，折线图语法有三种
- df.plot(x='Month', y='Tmax')- df.plot(x='Month', y='Tmax', kind='line')- df.plot.line(x='Month', y='Tmax')
```
df.plot.line(x='Month', y='Tmax')
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhRcVFpYTRvYU5zN3NZcExkRXc0VU1TVUo1WmljaWJremlhZENiQnBOaWEzdW1rdW1Edkl0RlEwSFE1dy82NDA?x-oss-process=image/format,png">

```
#grid绘制格线
df.plot(x='Month', y='Tmax', kind='line', grid=True)
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhuUFVqRXdpY1A4Y2ljSzNRN2tOV1FiZGpvZWFUcmliOUJGNHRnWmljeXVES1VDZENxczdBemtsT05BLzY0MA?x-oss-process=image/format,png">

#### **多个y值**

上面的折线图中只有一条线， 如何将多个y绘制到一个图中

比如Tmax， Tmin

```
df.plot(x='Month', y=['Tmax', 'Tmin'])
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhvMnl3RDdpYkRMQTNmeklNbVZFSUhuaWJYUENTS2tuWUo3WURHd0FIZ0NJa3ZISTRpYWljS3ZZaklnLzY0MA?x-oss-process=image/format,png">

#### **条形图**

```
df.plot(x='Month', 
        y='Rain', 
        kind='bar')
#同样还可以这样画
#df.plot.bar(x='Month', y='Rain')
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhuMHZMYnZEaGdwdnZlNnBqcGliRHc4NERPREdOaWJwNGF6c3RYQVVMNlJLS05MOERaNE5EbldEUS82NDA?x-oss-process=image/format,png">

#### **水平条形图**

bar环卫barh，就可以将条形图变为水平条形图

```
df.plot(x='Month', 
        y='Rain', 
        kind='barh')
#同样还可以这样画
#df.plot.bar(x='Month', y='Rain')
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhJU3Q0SGljaWFjd0Ewa01Makg3emp3cFFsbVg3aWFmN3M0NmJjc1BYclR4eGdYaEJnbHZDTWxRWlEvNjQw?x-oss-process=image/format,png">

多个变量的条形图

```
df.plot(kind='bar',
        x = 'Month',
       y=['Tmax', 'Tmin'])
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhsV21jNFc2MXdlWmlhd3BpYVlqRXE2NW9sdXZhTGYwTDc5b2dDWFkzTXZWRVNpYU1XaEt2cWFtOFEvNjQw?x-oss-process=image/format,png">

#### **散点图**

```
df.plot(kind='scatter',
        x = 'Month',
        y = 'Sun')
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1Nuekg1Z0VYbnNpY2NpYmljY05hT2owZ2NkSnlsV3NrcXltdzhaaFhjVlMxR0VFamdQakpTcFRyU3A2aWNnLzY0MA?x-oss-process=image/format,png">

#### **饼形图**

```
df.plot(kind='pie', y='Sun')
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhZbGdpY2ljM3JHOGZFV3lUQ1EzR0hsb25oSGFjQ0lwVDBFblI5aWNINzhiaWJCWmlhQWNPNzE2cFVUdy82NDA?x-oss-process=image/format,png">

上图绘制有两个小问题:
- legend图例不应该显示- 月份的显示用数字不太正规
```
df.index = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
df.plot(kind='pie', y = 'Sun', legend=False)
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhSRGliaWFudnZSQ2RpYmxzaFlqRGlhckZCNlV2S2tWbkZSdmI4Z3hLeWtvMDJPdlRMa3k1cFNIODJ3LzY0MA?x-oss-process=image/format,png">

#### **更多数据**

一开头的数据只有12条记录(12个月)的数据，现在我们用更大的伦敦天气数据

```
import pandas as pd
df2 = pd.read_csv('data/londonweather.csv')
df2.head()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekgwMHNIYUdpY0tFc0Iwa2lhaWFpY2J6SzdHRFZlTWtpYzBpYkREUEh6YUNXdFhncmhRRUxlWDBlTmw2amcvNjQw?x-oss-process=image/format,png">

```
df2.Rain.describe()

```

```
count    748.000000
mean      50.408957
std       29.721493
min        0.300000
25%       27.800000
50%       46.100000
75%       68.800000
max      174.800000
Name: Rain, dtype: float64

```

上面一共有748条记录, 即62年的记录。

#### 箱型图

```
df2.plot.box(y='Rain')
#df2.plot(y='Rain', kind='box')
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhETWpoaWNMRTZEcmtINXA2RmpIT3hqUE1CdFBEcVg2UE85Z2RnQVFCSmV3NnpNc0RMQ0RSWTRRLzY0MA?x-oss-process=image/format,png">

#### **直方图**

```
df2.plot(y='Rain', kind='hist')
#df2.plot.hist(y='Rain')
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhHZGhzRTNXUHVWVGliRzNuMVRzV2wxTHJ6endTTURFZlBnV3Y0Z1hjUk5wTThpYVlMUFRQTkU1dy82NDA?x-oss-process=image/format,png">

纵坐标的刻度可以通过bins设置

```
df2.plot(y='Rain', kind='hist', bins=[0,25,50,75,100,125,150,175, 200])
#df2.plot.hist(y='Rain')
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhCYnc2TWx6M0Q3MWg0MnRheWJSMUp3MFdVZTBpYjFOV1VENWljZWlieThyaWFQeDVrWHBrcDR3enFnLzY0MA?x-oss-process=image/format,png">

#### **多图并存**

```
df.plot(kind='line',
         y=['Tmax', 'Tmin', 'Rain', 'Sun'], #4个变量可视化
         subplots=True,   #多子图并存
         layout=(2, 2),   #子图排列2行2列
         figsize=(20, 10)) #图布的尺寸
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhpYVAzWnk1d3IzN0U1dHpkVW1nTVZvNDVNa0U2VGlibUsxdUpQY09OOGlhVWU3RzN6RlZuMzg5RncvNjQw?x-oss-process=image/format,png">

```
df.plot(kind='bar',
         y=['Tmax', 'Tmin', 'Rain', 'Sun'], #4个变量可视化
         subplots=True,   #多子图并存
         layout=(2, 2),   #子图排列2行2列
         figsize=(20, 10)) #图布的尺寸
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhMQnB6QjVpY0pGeGhiaWJPMWFlVzZBMWVaNFlYT2ZpY0RUZFhXS3plcUNDU0djSGdVT1IzYVJ1encvNjQw?x-oss-process=image/format,png">

#### **加标题**

给可视化起个标题

```
df.plot(kind='bar',
         y=['Tmax', 'Tmin'], #2个变量可视化
         subplots=True,   #多子图并存
         layout=(1, 2),   #子图排列1行2列
         figsize=(20, 5),#图布的尺寸
         title='The Weather of London')  #标题
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhXYnlIRExJYThHRUdkUWhOcVhkZG1MTm5sRlA3OFlyYXY2cVp2V2hoTGJ2YlpNaWIxN1paa2FnLzY0MA?x-oss-process=image/format,png">

### **保存结果**

可视化的结果可以存储为图片文件

```
df.plot(kind='pie', y='Rain', legend=False, figsize=(10, 5), title='Pie of Weather in London')
plt.savefig('img/pie.png')
plt.show()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhQcTN2ejQ2M2liQ2hXNEhITDRpY2xicE1SaWNvcVFad1JvTlhGZ0c2dTJYbm4xZFpaWVNvS0VORHcvNjQw?x-oss-process=image/format,png">

#### **df.plot更多参数**

df.plot(x, y, kind, figsize, title, grid, legend, style)
- x 只有dataframe对象时，x可用。横坐标- y 同上，纵坐标变量- kind 可视化图的种类，如line,hist, bar, barh, pie, kde, scatter- figsize 画布尺寸- title 标题- grid 是否显示格子线条- legend 是否显示图例- style 图的风格
查看plot参数可以使用help

```
import pandas as pd
help(pd.DataFrame.plot)

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9pYk9Ganh3aWNraWI0N2NHSGliRm5WejVSV0dhM0NuQ1NuekhrSlJKRUI0VEQ3elpFWm9Nb2hvZzVIdzVkMEFHR1Z0a2xpY0JoWkZzUHNpYWVjcVhtMWt6TzR5dy82NDA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcmNjSFVSRTF0ZmRnOWo5em9zbzYwNGdvWmtBeGpkdGNQSHo4WmFtaWJjakZiTUhMZGxNOG1RbWhveHZxbUpIUzRpY09hN2dSVGp2M1dBLzY0MA?x-oss-process=image/format,png">
