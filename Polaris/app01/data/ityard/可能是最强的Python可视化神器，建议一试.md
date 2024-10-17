
--- 
title:  可能是最强的Python可视化神器，建议一试 
tags: []
categories: [] 

---
数据分析离不开数据可视化，我们最常用的就是pandas，matplotlib，pyecharts当然还有Tableau，看到一篇文章介绍plotly制图后我也跃跃欲试，查看了相关资料开始尝试用它制图。

### 1. Plotly

Plotly 是一款用来做数据分析和可视化的在线平台，功能非常强大,可以在线绘制很多图形比如条形图、散点图、饼图、直方图等等。而且还是支持在线编辑，以及多种语言python、javascript、matlab、R等许多API。它在python中使用也很简单，直接用pip install plotly就可以了。推荐最好在jupyter notebook中使用，pycharm操作不是很方便。使用Plotly可以画出很多媲美Tableau的高质量图：

<img src="https://img-blog.csdnimg.cn/img_convert/6b2af156fd0427035a070fca61f3308e.png" alt="6b2af156fd0427035a070fca61f3308e.png">

plotly制图

我尝试做了折线图、散点图和直方图，首先导入库：

```
from plotly.graph_objs import Scatter,Layout
import plotly
import plotly.offline as py
import numpy as np
import plotly.graph_objs as go
#setting offilne 离线模式
plotly.offline.init_notebook_mode(connected=True)
```

上面几行代码主要是引用一些库，plotly有在线和离线两种模式，在线模式需要有账号可以云编辑。我选用的离线模式，plotly设置为offline模式就可以直接在notebook里面显示了。

### 2. 制作折线图

```
N = 100
random_x = np.linspace(0,1,N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

#Create traces
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',
    name = 'markers'
)
trace1 = go.Scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines+markers',
    name = 'lines+markers'
)
trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines',
    name = 'lines'
)
data = [trace0,trace1,trace2]
py.iplot(data)
```

<img src="https://img-blog.csdnimg.cn/img_convert/4f13801acea7e11f3aa5cbaa56251a61.png" alt="4f13801acea7e11f3aa5cbaa56251a61.png">

折线图

随机设置4个参数，一个x轴的数字和三个y轴的随机数据，制作出三种不同类型的图。trace0是markers，trace1是lines和markers,trace3是lines。然后把三种图放在data这个列表里面，调用py.iplot(data)即可。绘制的图片系统默认配色也挺好看的~

### 3. 制作散点图

```
trace1 = go.Scatter(
     y = np.random.randn(500),
    mode = 'markers',
    marker = dict(
        size = 16,
        color = np.random.randn(500),
        colorscale = 'Viridis',
        showscale = True
    )
)
data = [trace1]
py.iplot(data)
```

把mode设置为markers就是散点图，然后marker里面设置一组参数，比如颜色的随机范围，散点的大小，还有图例等等。

<img src="https://img-blog.csdnimg.cn/img_convert/9e0cee8e5d58e5efd15ab53fd7959e84.png" alt="9e0cee8e5d58e5efd15ab53fd7959e84.png">

散点图

### 4. 直方图

```
trace0 = go.Bar(
    x = ['Jan','Feb','Mar','Apr', 'May','Jun',
         'Jul','Aug','Sep','Oct','Nov','Dec'],
    y = [20,14,25,16,18,22,19,15,12,16,14,17],
    name = 'Primary Product',
    marker=dict(
        color = 'rgb(49,130,189)'
    )
)
trace1 = go.Bar(
    x = ['Jan','Feb','Mar','Apr', 'May','Jun',
         'Jul','Aug','Sep','Oct','Nov','Dec'],
    y = [19,14,22,14,16,19,15,14,10,12,12,16],
    name = 'Secondary Product',
    marker=dict(
        color = 'rgb(204,204,204)'
    )
)
data = [trace0,trace1]
py.iplot(data)
```

直方图

直方图是我们比较常用的一种图形，plotly绘制直方图的方式跟我们在pandas里面设置的有点类似，他们非常直观的体现了不同月份两个生产力之间的差异。

上面的制图只是plotly的冰山一角，都是一些最基本的用法，它还有很多很酷的用法和图形，尤其是跟pandas结合画的图非常漂亮。比如一些股票的K线图，大家有兴趣可以研究研究~

链接在此：https://plot.ly/python/

作者：estate47链接：https://www.jianshu.com/p/e5fb1b5c0957

**往期推荐：**
- - - - - - - - - 