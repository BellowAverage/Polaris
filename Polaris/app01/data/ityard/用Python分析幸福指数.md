
--- 
title:  用Python分析幸福指数 
tags: []
categories: [] 

---
<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcTIyWFdpY3diaDlXTGtsazJYNTF6dkdEWTN4UmtpY0NzT2huSlQ5V2xDejFvbnZ2c2RXd0JRb0IwaWNaZkNRaDl5SVJvaWM0MUlYd05XRVEvNjQw?x-oss-process=image/format,png">

>  
  作者：huny 
  https://www.cnblogs.com/huny/p/14146719.html 
 

世界上最幸福的国家有哪些？个人幸福和哪些指标相关？你幸福吗？如果不知道，那就进来看看这篇关于幸福的数据分析。

**1 前言**

民意测验机构盖洛普从2012年起，每年都会在联合国计划下发布《世界幸福指数报告》，报告会综合两年内150多个国家的国民对其所处社会、城市和自然环境等因素进行评价后，再根据他们所感知的幸福程度对国家进行排名。

《世界幸福指数报告》的编撰主要依赖于对150多个国家的1000多人提出一个简单的主观性问题：“如果有一个从0分到10分的阶梯，顶层的10分代表你可能得到的最佳生活，底层的0分代表你可能得到的最差生活。你觉得你现在在哪一层？”

最近看到的一个项目，非常的有意思。接下来我将用python带你来分析一下世界各国的幸福指数排名，以及和幸福有关系的因素。

**2 数据解释**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcVVwdnlFRUhwdW45U25pY2tlNjM0NE1JSjBpYUZ1WGFOSDA1MXVKdzRuU1dFdDU5RXBmakVWdHFhT0FPMWliUE1RUXRvR0p3elpmcTQ2dy82NDA?x-oss-process=image/format,png">

**3 数据准备**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcVVwdnlFRUhwdW45U25pY2tlNjM0NE12anI3TmVtOEpseklaOWliSTVCOWJDRlZocnV1ZnJxQmljSjFsVnd6d2dQemliS0xOSzd6VEhWM3cvNjQw?x-oss-process=image/format,png">

```
pip install -r requirement.txt 

```

**4 编码**

```


import numpy as np
import pandas as pd
import os,sys
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot, plot


#数列的路径
file_path = os.path.dirname(os.path.abspath(__file__))


# 读入数据
df_2015 = pd.read_csv(f'{file_path}/2015.csv')
df_2016 = pd.read_csv(f'{file_path}/2016.csv')
df_2017 = pd.read_csv(f'{file_path}/2017.csv')
df_2018 = pd.read_csv(f'{file_path}/2018.csv')
df_2019 = pd.read_csv(f'{file_path}/2019.csv')


# 新增列-年份
df_2015["year"] = str(2015)
df_2016["year"] = str(2016)
df_2017["year"] = str(2017)
df_2018["year"] = str(2018)
df_2019["year"] = str(2019)


# 合并数据
df_all = df_2015.append([df_2016, df_2017, df_2018, df_2019], sort=False)
df_all.drop('Unnamed: 0', axis=1, inplace=True)
df_all.head()
data = dict(type='choropleth',
            locations=df_2019['region'],
            locationmode='country names',
            colorscale='RdYlGn',
            z=df_2019['happiness'],
            text=df_2019['region'],
            colorbar={'title': '幸福指数'}) 


layout = dict(title='2019年世界幸福指数地图',
              geo=dict(showframe=True, projection={'type': 'azimuthal equal area'}))


choromap3 = go.Figure(data=[data], layout=layout)
plot(choromap3, filename=f'{file_path}/世界幸福地图.html')

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcVVwdnlFRUhwdW45U25pY2tlNjM0NE1vbVNyQXB0NlN4VFJUOWliVkprbm1PcVlJS3NpY2tIZlBhdE1DT295MGliRXExbmtlVWliYUt5cHp3LzY0MA?x-oss-process=image/format,png">

整体来看，北欧的国家幸福指数较高，如冰岛、丹麦、挪威、芬兰；东非和西非的国家幸福指数较低，如多哥、布隆迪、卢旺达和坦桑尼亚。

```


# 合并数据
rank_top10 = df_2019.head(10)[['rank', 'region', 'happiness']]
last_top10 = df_2019.tail(10)[['rank', 'region', 'happiness']]
rank_concat = pd.concat([rank_top10, last_top10])


# 条形图
fig = px.bar(rank_concat,
             x="region",
             y="happiness",
             color="region", 
             title="2019年全球最幸福和最不幸福的国家")


plot(fig, filename=f'{file_path}/2019世界幸福国家排行Top10和Last10.html')

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcVVwdnlFRUhwdW45U25pY2tlNjM0NE00OFJ5WjlQS2VQM1NnSkxKRHBMdHdGR0hXbDExWW9rOHk0N3ZzTzNKbHJORFNNRUxFTmhEancvNjQw?x-oss-process=image/format,png">

2019年报告，芬兰连续两年被评为“全球最幸福国家”。丹麦、挪威、冰岛、荷兰进入前五名，对比2018年报告，中国从86名下降到93名。

```
# 散点图
fig = px.scatter(df_all, x='gdp_per_capita',
                 y='happiness',
                 facet_row='year',
                 color='year',
                 trendline='ols'
                 ) 
fig.update_layout(height=800, title_text='人均GDP和幸福指数')
plot(fig, filename=f'{file_path}/GDP和幸福得分.html')

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcVVwdnlFRUhwdW45U25pY2tlNjM0NE1jV0hqbDZSb1NaSmU5TElCVVdpYnkyQjRNWkJpYnBqQVROQ1hLVW1VMnZER1dlRTVrSUFmSDFLdy82NDA?x-oss-process=image/format,png">

人均GDP与幸福得分呈高度线性正相关关系，GDP越高的国家，幸福水平相对越高。

```
# 散点图
fig = px.scatter(df_all, x='healthy_life_expectancy',
                 y='happiness',
                 facet_row='year',
                 color='year',
                 trendline='ols'
                 ) 
fig.update_layout(
    height=800, title_text='健康预期寿命和幸福指数')
plot(fig, filename=f'{file_path}/健康预期寿命和幸福得分.html')

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcVVwdnlFRUhwdW45U25pY2tlNjM0NE1URmNsOWh0S1dJejBxMnpxTGVSV05UVENtMUFUZWtIWXZ2M2dyWXJMOEtiWndVbGpOVGhtdWcvNjQw?x-oss-process=image/format,png">

慷慨程度与幸福得分呈高度线性正相关关系，慷慨程度越高的国家，幸福水平相对越高。

```
#散点图 
fig = px.scatter(df_all, x='social_support',
                 y='happiness',
                 facet_row='year',
                 color='year',
                 trendline='ols'
                 )
fig.update_layout(
    height=800, title_text='社会援助和幸福指数')
plot(fig, filename=f'{file_path}/社会援助和幸福得分.html')

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcVVwdnlFRUhwdW45U25pY2tlNjM0NE1haGFPaWJGU1V1T1N6VmxScXo3QzNzYU9KNWo2aGlhZXgyZzhUQ2tQakMzTndPcTNMTHJpY3BRcncvNjQw?x-oss-process=image/format,png">

**5 总结**

我们可以得出以下结论：

从影响因素相关图可以看出，在影响幸福得分的因素中，GDP、社会支持、健康预期寿命呈现高度相关，自由权呈现中度相关，国家的廉政水平呈现低度相关，慷慨程度则呈现极低的相关性；

GDP与健康预期寿命、社会支持之间存在高度相关。说明GDP高的国家，医疗水平和社会福利较为完善，人民的预期寿命也会越高；

健康预期寿命与社会支持之间存在中度相关性。

在公众号**Python小二**后台回复**幸福指数**获取使用数据。

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">

微信扫码关注，了解更多内容
