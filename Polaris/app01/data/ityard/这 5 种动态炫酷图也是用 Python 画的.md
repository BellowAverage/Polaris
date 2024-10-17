
--- 
title:  这 5 种动态炫酷图也是用 Python 画的 
tags: []
categories: [] 

---
>  
  作者：Liana Mehrabyan 
  来源：机器之心 
 

数据可以帮助我们描述这个世界、阐释自己的想法和展示自己的成果，但如果只有单调乏味的文本和数字，我们却往往能难抓住观众的眼球。而很多时候，一张漂亮的可视化图表就足以胜过千言万语。本文将介绍 5 种基于 Plotly 的可视化方法，你会发现，原来可视化不仅可用直方图和箱形图，还能做得如此动态好看甚至可交互。

对数据科学家来说，讲故事是一个至关重要的技能。为了表达我们的思想并且说服别人，我们需要有效的沟通。而漂漂亮亮的可视化是完成这一任务的绝佳工具。本文将介绍 **5 种非传统的可视化技术**，可让你的数据故事更漂亮和更有效。这里将使用 Python 的 Plotly 图形库（也可通过 R 使用），让你可以毫不费力地生成动画图表和交互式图表。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXOGliY2FYUENKQmFnd29QYkd0WURUV0J2emZVSWJuM2lhSVJCWGpUY0FhdHlvbkhpYW9Sb1M3QUVCMnFiUHRpYmJUc2ljV2liY1I0V3lpY2lhellBLzY0MA?x-oss-process=image/format,png">

那么，Plotly 有哪些好处？Plotly 的整合能力很强：可与 Jupyter Notebook 一起使用，可嵌入网站，并且完整集成了 Dash——一种用于构建仪表盘和分析应用的出色工具。

**启动**

如果你还没安装 Plotly，只需在你的终端运行以下命令即可完成安装：

```
pip install plotly
```

安装完成后，就开始使用吧！

**动画**

在研究这个或那个指标的演变时，我们常涉及到时间数据。**Plotly 动画工具仅需一行代码就能让人观看数据随时间的变化情况**，如下图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9LbVhQS0ExOWdXOGliY2FYUENKQmFnd29QYkd0WURUV0JjMjRkMmlhZjA0QVRKRXphUFdYaWFPQlNjTHd1TmFvYWlhOFJ4MmNqRGF5M2RSRmVGMG5md0szQWcvNjQw?x-oss-process=image/format,png">

代码如下：

```
import plotly.express as px
from vega_datasets import data
df = data.disasters()
df = df[df.Year &gt; 1990]
fig = px.bar(df,
             y="Entity",
             x="Deaths",
             animation_frame="Year",
             orientation='h',
             range_x=[0, df.Deaths.max()],
             color="Entity")
# improve aesthetics (size, grids etc.)
fig.update_layout(width=1000,
                  height=800,
                  xaxis_showgrid=False,
                  yaxis_showgrid=False,
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  title_text='Evolution of Natural Disasters',
                  showlegend=False)
fig.update_xaxes(title_text='Number of Deaths')
fig.update_yaxes(title_text='')
fig.show()
```

只要你有一个时间变量来过滤，那么几乎任何图表都可以做成动画。下面是一个制作散点图动画的例子：

```
import plotly.express as px
df = px.data.gapminder()
fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=55,
    range_x=[100, 100000],
    range_y=[25, 90],

    #   color_continuous_scale=px.colors.sequential.Emrld
)
fig.update_layout(width=1000,
                  height=800,
                  xaxis_showgrid=False,
                  yaxis_showgrid=False,
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)')

```

**太阳图**

太阳图（sunburst chart）是一种可视化 group by 语句的好方法。**如果你想通过一个或多个类别变量来分解一个给定的量**，那就用太阳图吧。

假设我们想根据性别和每天的时间分解平均小费数据，那么相较于表格，这种双重 group by 语句可以通过可视化来更有效地展示。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9LbVhQS0ExOWdXaWNwRzRpYnJpY0RqaHNlRk9HWTNRbmM0NzNWakxWZmFITUFiTjlZS05OdzZlT0FSS1k0RmtKZU11emphZHhKSzd3aWN3U0Y2R05pYTRCV253LzY0MA?x-oss-process=image/format,png">

这个图表是交互式的，让你可以自己点击并探索各个类别。你只需要定义你的所有类别，并声明它们之间的层次结构（见以下代码中的 parents 参数）并分配对应的值即可，这在我们案例中即为 group by 语句的输出。

```
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
df = px.data.tips()
fig = go.Figure(go.Sunburst(
    labels=["Female", "Male", "Dinner", "Lunch", 'Dinner ', 'Lunch '],
    parents=["", "", "Female", "Female", 'Male', 'Male'],
    values=np.append(
        df.groupby('sex').tip.mean().values,
        df.groupby(['sex', 'time']).tip.mean().values),
    marker=dict(colors=px.colors.sequential.Emrld)),
                layout=go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)'))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0),
                  title_text='Tipping Habbits Per Gender, Time and Day')
fig.show()

```

现在我们向这个层次结构再添加一层：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9LbVhQS0ExOWdXaWNwRzRpYnJpY0RqaHNlRk9HWTNRbmM0N3BLS25pYkg4UlFoaWFtdlk0UE94cVRaZXgwZ3BYNmJUcWljOGdreTBTTTljSkJNVnIyNkY0dmVKZy82NDA?x-oss-process=image/format,png">

为此，我们再添加另一个涉及三个类别变量的 group by 语句的值。

```
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
df = px.data.tips()
fig = go.Figure(go.Sunburst(labels=[
    "Female", "Male", "Dinner", "Lunch", 'Dinner ', 'Lunch ', 'Fri', 'Sat',
    'Sun', 'Thu', 'Fri ', 'Thu ', 'Fri  ', 'Sat  ', 'Sun  ', 'Fri   ', 'Thu   '
],
                            parents=[
                                "", "", "Female", "Female", 'Male', 'Male',
                                'Dinner', 'Dinner', 'Dinner', 'Dinner',
                                'Lunch', 'Lunch', 'Dinner ', 'Dinner ',
                                'Dinner ', 'Lunch ', 'Lunch '
                            ],
                            values=np.append(
                                np.append(
                                    df.groupby('sex').tip.mean().values,
                                    df.groupby(['sex',
                                                'time']).tip.mean().values,
                                ),
                                df.groupby(['sex', 'time',
                                            'day']).tip.mean().values),
                            marker=dict(colors=px.colors.sequential.Emrld)),
                layout=go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)'))
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0),
                  title_text='Tipping Habbits Per Gender, Time and Day')

fig.show()

```

**平行类别**

另一种探索类别变量之间关系的方法是以下这种流程图。**你可以随时拖放、高亮和浏览值，非常适合演示时使用。**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9LbVhQS0ExOWdXaWNwRzRpYnJpY0RqaHNlRk9HWTNRbmM0N1VseWNYMHpkd3JVbkdpYTBwb3F4WGljU3RTaWNrb0NTdHBHM0RRRzZxc0ttajk5bmtFMkw0TWN5US82NDA?x-oss-process=image/format,png">

代码如下：

```
import plotly.express as px
from vega_datasets import data
import pandas as pd
df = data.movies()
df = df.dropna()
df['Genre_id'] = df.Major_Genre.factorize()[0]
fig = px.parallel_categories(
    df,
    dimensions=['MPAA_Rating', 'Creative_Type', 'Major_Genre'],
    color="Genre_id",
    color_continuous_scale=px.colors.sequential.Emrld,
)
fig.show()

```

**平行坐标图**

平行坐标图是上面的图表的连续版本。这里，**每一根弦都代表单个观察**。这是一种可用于识别离群值（远离其它数据的单条线）、聚类、趋势和冗余变量（比如如果两个变量在每个观察上的值都相近，那么它们将位于同一水平线上，表示存在冗余）的好用工具。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9LbVhQS0ExOWdXaWNwRzRpYnJpY0RqaHNlRk9HWTNRbmM0NzZXQ2lhT29yb2ViYTFMT2liaWF2R1NlVW9iUjVaVW9JOFFhVDJjM01SRXVqdnZROGs4UlNiWHFFQS82NDA?x-oss-process=image/format,png">

代码如下：

```
 import plotly.express as px
from vega_datasets import data
import pandas as pd
df = data.movies()
df = df.dropna()
df['Genre_id'] = df.Major_Genre.factorize()[0]
fig = px.parallel_coordinates(
    df,
    dimensions=[
        'IMDB_Rating', 'IMDB_Votes', 'Production_Budget', 'Running_Time_min',
        'US_Gross', 'Worldwide_Gross', 'US_DVD_Sales'
    ],
    color='IMDB_Rating',
    color_continuous_scale=px.colors.sequential.Emrld)
fig.show()

```

**量表图和指示器**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXaWNwRzRpYnJpY0RqaHNlRk9HWTNRbmM0NzU5SVBrNWV0VFg3aWFpY1hyaWNJSXYxbDZJTUN6WDN1WlNpYWg3QmliSzF2ZVJvemE5UnNPcEdteHh3LzY0MA?x-oss-process=image/format,png">

量表图仅仅是为了好看。**在报告 KPI 等成功指标并展示其与你的目标的距离时，可以使用这种图表。**

指示器在业务和咨询中非常有用。它们可以通过文字记号来补充视觉效果，吸引观众的注意力并展现你的增长指标。

```
 import plotly.graph_objects as go
fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 4.3,
    mode = "gauge+number+delta",
    title = {'text': "Success Metric"},
    delta = {'reference': 3.9},
    gauge = {'bar': {'color': "lightgreen"},
        'axis': {'range': [None, 5]},
             'steps' : [
                 {'range': [0, 2.5], 'color': "lightgray"},
                 {'range': [2.5, 4], 'color': "gray"}],
          }))
fig.show()

```

**原文链接：https://towardsdatascience.com/5-visualisations-to-level-up-your-data-story-e131759c2f41**

```

分享或在看是对我最大的支持 

```
