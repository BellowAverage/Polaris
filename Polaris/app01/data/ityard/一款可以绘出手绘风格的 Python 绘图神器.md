
--- 
title:  一款可以绘出手绘风格的 Python 绘图神器 
tags: []
categories: [] 

---
>  
  https://github.com/chenjiandongx/cutecharts 
 

今天，给大家介绍一个很酷的 **Python 手绘风格可视化神包：cutecharts。**

和 Matplotlib 、pyecharts 等常见的图表不同，使用这个包可以生成下面这种看起来像手绘的各种图表，在一些场景下使用效果可能会更好。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2ZGQnRvekxiNG91b3pCYTZ5YUFpYlNFaWJiaWJpYVN6dWVWMTlhaWFlT2liZGRBSXE2OENWUWgyQ1hpYU9RLzY0MA?x-oss-process=image/format,png" title="">

GitHub 地址：

https://github.com/chenjiandongx/cutecharts

怎么画出这些图表呢，很简单，一行命令先安装好该库：

```
pip install cutecharts

```

也可以使用源码安装的方式：

```
$ git clone https://github.com/chenjiandongx/cutecharts.git
$ cd cutecharts
$ pip install -r requirements.txt
$ python setup.py install

```

下面就介绍下每个图表如何绘制。

首先是一些图表共通的参数：

#### Commons

不同图表有着部分相同的方法。

**`__init__`**

```
Params                                          Desc
------                                          ----
title: Optional[str] = None                     图表标题
width: str = "800px"                            图表宽度
height: str = "600px"                           图表高度
assets_host: Optional[str] = None               引用资源 Host

```

**`render`**

```
Params                                          Desc
------                                          ----
dest: str = "render.html"                       渲染的文件路径
template_name: str = "basic_local.html"         渲染使用的模板，一般不需要修改   

```

**`render_notebook`**

```
Params                                          Desc
------                                          ----
template_type: str = "basic"                    渲染使用的模板类型，一般不需要修改 

```

**`load_javascript`**

```
加载 JS 依赖，在 JupyterLab 渲染时使用。

```

### Bar（柱状图）

>  
  cutecharts.charts.Bar 
 

#### API

>  
  cutecharts.charts.Bar.set_options 
 

```
Params                                          Desc
------                                          ----
labels: Iterable                                X 坐标轴标签数据
x_label: str = ""                               X 坐标轴名称
y_label: str = ""                               Y 坐标轴名称
y_tick_count: int = 3                           Y 轴刻度分割段数
colors: Optional[Iterable] = None               label 颜色数组
font_family: Optional[str] = None               CSS font-family

```

>  
  cutecharts.charts.Bar.add_series 
 

```
Params                                          Desc
------                                          ----
name: str                                       series 名称
data: Iterable                                  series 数据列表

```

#### Demo

>  
  Bar-基本示例 
 

```
from cutecharts.charts import Bar
from cutecharts.components import Page
from cutecharts.faker import Faker


def bar_base() -&gt; Bar:
    chart = Bar("Bar-基本示例")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    return chart

bar_base().render()
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2ZqZHE3VmljellEN3g4Vm5TZW1UUVlWZk5ET1dtN3laalJNSmliU2Q0Y2liWGJlY25XdXhnWVl2T3cvNjQw?x-oss-process=image/format,png" title="img">

>  
  Bar-调整颜色 
 

```
def bar_tickcount_colors():
    chart = Bar("Bar-调整颜色")
    chart.set_options(labels=Faker.choose(), y_tick_count=10, colors=Faker.colors)
    chart.add_series("series-A", Faker.values())
    return chart
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2ZrSDlWdk52NEd0c21nN1BoQlZBOFhRVGljTFZpY2MzcE84R0dLMWlhVlFEeWJiTDRPZ0N4VWJyM2cvNjQw?x-oss-process=image/format,png" title="img">

### Line（折线图）

>  
  cutecharts.charts.Line 
 

#### API

>  
  cutecharts.charts.Line.set_options 
 

```
Params                                          Desc
------                                          ----
labels: Iterable                                X 坐标轴标签数据
x_label: str = ""                               X 坐标轴名称
y_label: str = ""                               Y 坐标轴名称
y_tick_count: int = 3                           Y 轴刻度分割段数
legend_pos: str = "upLeft"                      图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
colors: Optional[Iterable] = None               label 颜色数组
font_family: Optional[str] = None               CSS font-family

```

>  
  cutecharts.charts.Line.add_series 
 

```
Params                                          Desc
------                                          ----
name: str                                       series 名称
data: Iterable                                  series 数据列表

```

#### Demo

>  
  Line-基本示例 
 

```
from cutecharts.charts import Line
from cutecharts.components import Page
from cutecharts.faker import Faker


def line_base() -&gt; Line:
    chart = Line("Line-基本示例")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart
line_base().render()
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2ZvOFRFMXZ4Tjc3V2Z0VWVrU1gwaHdDYW1NaWNxcGJBaGVHZ21XOHV6eTFWU3FVMG5uN1Y5RGlhZy82NDA?x-oss-process=image/format,png" title="img">

>  
  Line-Legend 位置 
 

```
def line_legend():
    chart = Line("Line-Legend 位置")
    chart.set_options(labels=Faker.choose(), legend_pos="upRight")
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2Z0bVRwUkZicVNJamtmb2ViY0M2ZWNmU1lwb1BNZ2ljWUw0aWFSOEs5YlkxOXdlZW9xYkJ5RmpwZy82NDA?x-oss-process=image/format,png" title="img">

>  
  Line-调整颜色 
 

```
def line_tickcount_colors():
    chart = Line("Line-调整颜色")
    chart.set_options(labels=Faker.choose(), colors=Faker.colors, y_tick_count=8)
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2ZWQmlic0I0OUhsa0xzSmZtTU1kamh5OVViUllMWkZJbzNOcnFmVDl1aDlla1Jwd2drbEk3QlZ3LzY0MA?x-oss-process=image/format,png" title="img">

### Pie（饼图）

>  
  cutecharts.charts.Pie 
 

#### API

>  
  cutecharts.charts.Pie.set_options 
 

```
Params                                          Desc
------                                          ----
labels: Iterable                                数据标签列表
inner_radius: float = 0.5                       Pie 图半径
legend_pos: str = "upLeft"                      图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
colors: Optional[Iterable] = None               label 颜色数组
font_family: Optional[str] = None               CSS font-family

```

>  
  cutecharts.charts.Pie.add_series 
 

```
Params                                          Desc
------                                       ----
data: Iterable                                  series 数据列表

```

#### Demo

>  
  Pie-基本示例 
 

```
from cutecharts.charts import Pie
from cutecharts.components import Page
from cutecharts.faker import Faker


def pie_base() -&gt; Pie:
    chart = Pie("Pie-基本示例")
    chart.set_options(labels=Faker.choose())
    chart.add_series(Faker.values())
    return chart


pie_base().render()
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2Zua1FpYm00bDlZaWE1bjJvUGhBaWNkcmlhek1IME82RkNqdVd4c0lNcmliTEFGSDhwWmgyQXA4VFY0US82NDA?x-oss-process=image/format,png" title="img">

>  
  Pie-Legend 
 

```
def pie_legend_font():
    chart = Pie("Pie-Legend")
    chart.set_options(
        labels=Faker.choose(),
        legend_pos="downLeft",
        font_family='"Times New Roman",Georgia,Serif;',
    )
    chart.add_series(Faker.values())
    return chart
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2Z4UERtcTJBTGliTE4wbk9YTEtzUmZiZnhiVHp0MXlVd2FlaWFub3c1ZUNrZVZJODFJY1Q4cG5sUS82NDA?x-oss-process=image/format,png" title="img">

>  
  Pie-Radius 
 

```
def pie_radius():
    chart = Pie("Pie-Radius")
    chart.set_options(
        labels=Faker.choose(),
        inner_radius=0,
    )
    chart.add_series(Faker.values())
    return chart
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2Y1Vlp5MGVPSE13N0lpY0M4QktWMnVMVWljY3QwTk5TTGc5YVpRQktoYVh2YThwR3VUZXViNHFnZy82NDA?x-oss-process=image/format,png" title="img">

### Radar（雷达图）

>  
  cutecharts.charts.Radar 
 

#### API

>  
  cutecharts.charts.Radar.set_options 
 

```
Params                                          Desc
------                                          ----
labels: Iterable                                数据标签列表
is_show_label: bool = True                      是否显示标签
is_show_legend: bool = True                     是否显示图例
tick_count: int = 3                             坐标系分割刻度
legend_pos: str = "upLeft"                      图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
colors: Optional[Iterable] = None               label 颜色数组
font_family: Optional[str] = None               CSS font-family

```

>  
  cutecharts.charts.Radar.add_series 
 

```
Params                                          Desc
------                                          ----
name: str                                       series 名称
data: Iterable                                  series 数据列表

```

#### Demo

>  
  Radar-基本示例 
 

```
from cutecharts.charts import Radar
from cutecharts.components import Page
from cutecharts.faker import Faker


def radar_base() -&gt; Radar:
    chart = Radar("Radar-基本示例")
    chart.set_options(labels=Faker.choose())
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart


radar_base().render()
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJUGJHODh4eVliZUlpYlpnOXlVaWNnaFI1WmsxUnNGVGRVRzJpYzgwc0MzcmZiTUFUTlAyU2N3RERXZFZ3d2JGSHBUbGJvN0V1aWFpYXpSZWljZy82NDA?x-oss-process=image/format,png">

>  
  Radar-颜色调整 
 

```
def radar_legend_colors():
    chart = Radar("Radar-颜色调整")
    chart.set_options(labels=Faker.choose(), colors=Faker.colors, legend_pos="upRight")
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJUGJHODh4eVliZUlpYlpnOXlVaWNnaFI1RlVwMGxoV3NKUTZRVXZ3SUdmeFBOM1RpY1BkUDhkN1JXOXJ0cUR6Y093Y3FpYU1hRTVTRXA3aWFnLzY0MA?x-oss-process=image/format,png">

### Scatter（散点图）

>  
  cutecharts.charts.Scatter 
 

#### API

>  
  cutecharts.charts.Scatter.set_options 
 

```
Params                                          Desc
------                                          ----
x_label: str = ""                               X 坐标轴名称
y_label: str = ""                               Y 坐标轴名称
x_tick_count: int = 3                           X 轴刻度分割段数
y_tick_count: int = 3                           Y 轴刻度分割段数
is_show_line: bool = False                      是否将散点连成线
dot_size: int = 1                               散点大小
time_format: Optional[str] = None               日期格式
legend_pos: str = "upLeft"                      图例位置，有 "upLeft", "upRight", "downLeft", "downRight" 可选
colors: Optional[Iterable] = None               label 颜色数组
font_family: Optional[str] = None               CSS font-family

```

>  
  cutecharts.charts.Scatter.add_series 
 

```
Params                                          Desc
------                                          ----
name: str                                       series 名称
data: Iterable                                  series 数据列表，[(x1, y1), (x2, y2)]

```

#### Demo

>  
  Scatter-基本示例 
 

```
from cutecharts.charts import Scatter
from cutecharts.components import Page
from cutecharts.faker import Faker


def scatter_base() -&gt; Scatter:
    chart = Scatter("Scatter-基本示例")
    chart.set_options(x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart


scatter_base().render()
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2ZmWTJhVmNXZTl5WFBNZ3VLam5vZkRSNmliNVZadXhVSENBQmNEeU9lU3JpYUloejU0ZTBrVEFRUS82NDA?x-oss-process=image/format,png" title="img">

>  
  Scatter-散点大小 
 

```
def scatter_dotsize_tickcount():
    chart = Scatter("Scatter-散点大小")
    chart.set_options(dot_size=2, y_tick_count=8)
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2ZVNnEwQmljRkQ5NDFjczZ1V2xjUGJpYTRXZVlWeHVjVFdienBSNUZKRzlNMDFOUkJXVTdKRUlpYncvNjQw?x-oss-process=image/format,png" title="img">

>  
  Scatter-散点连成线 
 

```
def scatter_show_line():
    chart = Scatter("Scatter-散点连成线")
    chart.set_options(y_tick_count=8, is_show_line=True)
    chart.add_series(
        "series-A", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    chart.add_series(
        "series-B", [(z[0], z[1]) for z in zip(Faker.values(), Faker.values())]
    )
    return chart
```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy90UnJ4U0Y5SVVJT1hIUFB3U3lHaWFCTGp6cU5Qc0txd2ZhQmNZeFNzd1BBTWwwelhwQkxqc2tGNGpPRUticXl1UXlBY0tqREZTYUJvRWNHdWRUVEJuZ3cvNjQw?x-oss-process=image/format,png" title="img">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 
