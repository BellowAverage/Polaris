
--- 
title:  【python】Python国内GDP经济总量数据分析可视化(源码+报告)【独一无二】 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>Python国内GDP经济总量数据分析可视化(源码+报告)【独一无二】</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - - <ul><li>- - - -  
  </li></ul> 
  
  


## 一、设计思路
1. 初始化与数据导入: 引入库: 导入 pyecharts用于数据处理。 导入 matplotlib.pyplot 用于基础的图形绘制。 导入 seaborn 用于高级图形绘制。 导入 WordCloud 用于生成词云图。 导入 pandas 用于数据处理。
设置:使用 plt.rcParams 修改默认设置，以确保图形中的中文可以正常显示。 数据读取:使用 pandas 的 read_csv 方法从 data.csv 文件中读取数据。

```
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import pandas as pd

```

```
plt.rcParams["font.sans-serif"] = ["SimHei"]

```

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 经济分析 ” 获取。👈👈👈 

1. 绘制总GDP的条形图: 数据排序:对数据按 ‘总GDP (亿元)’ 进行降序排序。图形绘制:设定图形的大小为15x8。使用 plt.barh 绘制条形图。设置X轴和Y轴的标签以及图形的标题。翻转Y轴的顺序使得GDP最高的省份在最上方。使用 plt.show 展示图形。
```
plt.figure(figsize=(15, 8))
data = data.sort_values(by='总GDP (亿元)', ascending=False)
plt.barh(data['省份'], data['总GDP (亿元)'], color='skyblue')
plt.xlabel('总GDP (亿元)')
plt.ylabel('省份')
plt.title('各省份总GDP数据条形图')
plt.gca().invert_yaxis()
plt.show()

```
1. 绘制GDP实际增速的折线图: 图形绘制:设定图形的大小为15x8。使用 sns.lineplot 绘制折线图，设置数据点的标记以及颜色。旋转X轴标签以避免重叠。设置图形的标题。使用 plt.show 展示图形。
```
# 生成各省份GDP实际增速的折线图：
plt.figure(figsize=(15, 8))
sns.lineplot(data=data, x='省份', y='实际增速', marker='o', color='green')
plt.xticks(rotation=45)
plt.title('各省份GDP实际增速折线图')
plt.show()

```

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 经济分析 ” 获取。👈👈👈 

1. 绘制总GDP、人均GDP与常住人口的气泡图:图形绘制:设定图形的大小为15x8。使用 sns.scatterplot 绘制气泡图，设置气泡大小与色调。设置图形的标题和图例位置。使用 plt.show 展示图形。
```
# 生成气泡图：
plt.figure(figsize=(15, 8))
sns.scatterplot(data=data, x='总GDP (亿元)', y='人均GDP (元)', size='常住人口 (万)', hue='省份', sizes=(50, 1000), palette='viridis')
plt.title('各省份总GDP、人均GDP、常住人口关系的气泡图')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

```
1. 绘制总GDP的词云图:词云图设置:指定字体路径，用于支持中文。使用 WordCloud 创建词云对象并从频率生成词云。图形绘制:设定图形的大小为10x6。使用 plt.imshow 显示词云图。关闭坐标轴显示。设置图形的标题。使用 plt.show 展示图形。保存图像:使用 wordcloud.to_file 将词云图保存为PNG格式的图片文件。
```
# 各省份总GDP数据的词云图：
font_path = 'msyh.ttc'
wordcloud = WordCloud(font_path=font_path, width=800, height=400, background_color='white').generate_from_frequencies(data.set_index('省份')['总GDP (亿元)'])
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('各省份总GDP数据词云图')
plt.show()
wordcloud.to_file("wordcloud_image.png")

```

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 经济分析 ” 获取。👈👈👈 


## 二、可视化分析

### 2.1 柱状图分析

从柱状图中可以看出，每个月的数值有所不同，其中一些月份的数值明显高于其他月份。显示了这些月份的出色表现。某些月份，数值则相对较低，不到2500。一般来说，可以观察到一个周期性的模式，某些月份的数值往往会上升，而其他月份则会下降。

<img src="https://img-blog.csdnimg.cn/direct/9f70d963f8c649eaaf2b2db23fb66049.png" alt="在这里插入图片描述">

### 2.2 折线图分析

柱状图表示的是每月的销售额、产量或其他相关指标的变化。而折线图可能表示的是累计值或年度总和的变化。柱状图显示了明显的季节性或月度波动，而折线图则更多地显示了长期趋势。两图结合，为我们提供了对某一指标在短期和长期内的完整视图。

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 经济分析 ” 获取。👈👈👈 


<img src="https://img-blog.csdnimg.cn/direct/8cdc38436ffb45d98fd11fa7cd3303ea.png" alt="在这里插入图片描述">

### 2.3 气泡图分析

在总GDP较高，且人均GDP也较高的区域有几个较大的气泡，这意味着这些省份在经济产值和人均财富方面均表现优越，并且有着较大的人口规模。在左下角区域有几个较小的气泡，表示这些省份的总GDP和人均GDP相对较低，同时城乡人口数也相对较少。在人均GDP相对较高但总GDP不是很高的区域也有一些省份，这可能表示这些省份的经济效率或人均生产力很高，但由于总人口不多，所以总GDP并不是很高。

<img src="https://img-blog.csdnimg.cn/direct/3058d4ff33334b3ca831205829a6fee5.png" alt="在这里插入图片描述">

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 经济分析 ” 获取。👈👈👈 


### 2.4 词云图

<img src="https://img-blog.csdnimg.cn/direct/3b9ba900ddd941c696c8f85123d3c49e.png" alt="在这里插入图片描述">

### 2.5 可视化大屏

<img src="https://img-blog.csdnimg.cn/direct/72f170b0fb6e4197be9d08e6ba8ee7ed.png" alt="在这里插入图片描述">

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 经济分析 ” 获取。👈👈👈 

