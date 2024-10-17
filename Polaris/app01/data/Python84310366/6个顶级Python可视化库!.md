
--- 
title:  6个顶级Python可视化库! 
tags: []
categories: [] 

---
如果你是Python可视化的新手，一些流行的可视化库包括Matplotlib、Seaborn、Plotly、Bokeh、Altair和Folium，以及大量的库和例子可能会让你感到不知所措。

当可视化一个DataFrame时，选择使用哪个可视化库确实是一个头疼的事情。

这篇文章云朵君将和大家一起学习每个库的**优点和缺点**。到最后，对它们的不同特点有更好的了解，在合适的时候更容易选择合适的库。

将通过专注于几个具体的属性来评价一个可视化工具的优缺点：

#### **互动性**

你想要交互式可视化吗？像Altair、Bokeh和Plotly这样的库允许你创建交互式图表，用户可以探索和互动。

另外，一些库（如Matplotlib）将可视化渲染成静态图像，使其适合在论文、幻灯片或演示中解释概念。

#### **语法和灵活性**

不同库的语法有什么不同？低级别的库，如Matplotlib，提供了广泛的灵活性，可以完成几乎任何事情。然而，API也是很复杂的。

像Altair这样的声明式库简化了数据到可视化的映射，提供了一个更直观的语法。

#### **数据类型和视觉化**

是否在处理专门的用例，如地理图或大数据集？考虑一个特定的库是否支持绘图类型或有效处理大型数据集。

### Matplotlib

Matplotlib可能是最常见的用于可视化数据的Python库。几乎所有对数据科学感兴趣的人都可能至少使用过一次Matplotlib。

#### 优点

##### 易于解释的数据属性

在分析数据时，快速了解数据分布情况往往非常有用的。

例如，如果你想检查拥有最多粉丝的前100名用户的分布情况，通常Matplotlib就足够了。

```
import matplotlib.pyplot as plt  
  
top_followers = new_profile.sort_values(by="followers", axis=0, ascending=False)[:100]  
  
fig = plt.figure()  
  
plt.bar(top_followers.user_name, top_followers.followers)  
plt.show()  

```

尽管Matplotlib的X轴表示方法并不理想，但该图可以让人清楚地了解数据的分布。

##### 多样性

Matplotlib的功能非常全面，能够生成各种类型的图形。Matplotlib的网站[2]提供了全面的文档和各种图形的图库，使得它很容易找到几乎任何类型的绘图的教程。

```
fig = plt.figure()  
  
plt.text(  
    0.6,  
    0.7,  
    "learning",  
    size=40,  
    rotation=20.0,  
    ha="center",  
    va="center",  
    bbox=dict(  
        boxstyle="round",  
        ec=(1.0, 0.5, 0.5),  
        fc=(1.0, 0.8, 0.8),  
    ),  
)  
  
plt.text(  
    0.55,  
    0.6,  
    "machine",  
    size=40,  
    rotation=-25.0,  
    ha="right",  
    va="top",  
    bbox=dict(  
        boxstyle="square",  
        ec=(1.0, 0.5, 0.5),  
        fc=(1.0, 0.8, 0.8),  
    ),  
)  
  
plt.show()  

```

#### 缺点

虽然Matplotlib几乎可以绘制任何东西，但生成非基本的图或为审美目的调整图可能很复杂。

如果你打算向他人展示你的数据，定制X轴、Y轴和其他绘图元素可能需要大量的努力。这是由于Matplotlib的低级接口造成的。

```
num_features = new_profile.select_dtypes("int64")  
correlation = num_features.corr()  
  
fig, ax = plt.subplots()  
im = plt.imshow(correlation)  
  
ax.set_xticklabels(correlation.columns)  
ax.set_yticklabels(correlation.columns)  
  
plt.setp(ax.get_xticklabels(),   
        rotation=45,   
        ha="right",   
        rotation_mode="anchor")  
plt.show()  

```

**经验之谈：Matplotlib** 能够制作任何绘图，但与其他库相比，创建复杂的绘图往往需要更多的代码。

### Seaborn

Seaborn是一个建立在Matplotlib之上的Python数据可视化库。它提供了一个更高层次的界面，简化了创建具有视觉吸引力的图的过程。

#### 优点

##### 减少的代码

Seaborn提供了一个更高层次的接口来生成与Matplotlib类似的图。这意味着你可以用更少的代码和更漂亮的视觉设计来实现类似的可视化。

例如，使用与之前相同的数据，我们可以创建一个热图，而无需明确设置x和y标签：

```
correlation = new_profile.corr()  
  
sns.heatmap(correlation, annot=True)  

```

这使得热图在视觉上更有吸引力，而不需要额外的配置。

##### 改善普通图表的美感

Seaborn是常见绘图类型的热门选择，如柱状图、箱形图、计数图和直方图。Seaborn不仅需要较少的代码来生成这些图，而且它们还具有增强的视觉美感。

在下面的例子中，由于Seaborn的默认设置，计数图在视觉上显得更加吸引人：

```
sns.set(style="darkgrid")  
titanic = sns.load_dataset("titanic")  
ax = sns.countplot(x="class", data=titanic)  

```

#### 缺点

Seaborn尽管有其优势，但并不像Matplotlib那样拥有广泛的绘图类型集合。虽然它在流行的绘图类型方面表现出色，但对于更专业或定制的绘图，它可能无法提供同样广泛的选项。

**经验之谈：Seaborn** 是Matplotlib的一个高级版本。尽管它没有像Matplotlib那样广泛的集合，但Seaborn可以用更少的代码使流行的绘图，如柱状图、盒状图、热图等看起来更漂亮。

### Plotly

Plotly[4]图形库提供了一种毫不费力的方式来创建交互式和高质量的图形。它提供了一系列类似于Matplotlib和Seaborn的图表类型，包括线图、散点图、面积图、条形图等等。

#### 优点

##### 与R相似

如果你熟悉在R中创建绘图，并在使用Python时怀念它的功能，Plotly是一个很好的选择。它允许你用Python实现同样水平的高质量绘图。

Plotly Express尤其突出，因为它只用一行Python代码就能创建令人印象深刻的图表。比如说：

```
import plotly.express as px  
  fig = px.scatter(  
    new_profile[:100],  
    x="followers",  
    y="total_stars",  
    color="forks",  
    size="contribution",  
)  
fig.show()  

```

##### 交互式图表创建

Plotly擅长创建交互式图表，这不仅增强了视觉吸引力，而且使观众能够更详细地探索数据。

让我们考虑一下前面的用Matplotlib创建的条形图例子。下面是如何用Plotly实现的：

```
top_followers = new_profile.sort_values(by="followers", axis=0, ascending=False)[:100]  
  
fig = px.bar(  
    top_followers,  
    x="user_name",  
    y="followers",  
)  
  
fig.show()  

```

通过类似的代码，Plotly可以生成一个交互式的图表，用户可以将鼠标悬停在每个条形图上，查看相应的用户和关注者数量。这种互动性使你的可视化的消费者有能力自己去探索数据。

##### 复杂地块中的简单性

Plotly简化了复杂图的创建，这在其他库中可能是个挑战。

例如，如果我们想在地图上可视化GitHub用户的位置，我们可以获得他们的经纬度，并据此绘制：

```
location_df = pd.read_csv(  
    "https://gist.githubusercontent.com/khuyentran1401/ce61bbad3bc636bf2548d70d197a0e3f/raw/ab1b1a832c6f3e01590a16231ba25ca5a3d761f3/location_df.csv",  
    index_col=0,  
)  
  
m = px.scatter_geo(  
    location_df,  
    lat="latitude",  
    lon="longitude",  
    color="total_stars",  
    size="forks",  
    hover_data=["user_name", "followers"],  
    title="Locations of Top Users",  
)  
  
m.show()  

```

只需几行代码，Plotly就能在地图上漂亮地表示用户的位置。气泡的颜色代表分叉的数量，而大小则与星星的总数相对应。

**经验之谈：Plotly** 是一个很好的选择，可以用最少的代码来创建交互式和出版质量的图表。它提供了广泛的可视化功能，并简化了创建复杂图表的过程。

### Altair

Altair[5]是一个强大的Python声明式统计可视化库，基于Vega-Lite。它在创建需要大量统计转换的图表时大放异彩。

#### 优点

##### 简单的可视化语法

Altair利用直观的语法来创建可视化。你只需要指定数据列和编码通道之间的联系，其余的绘图工作都是自动处理的。这种简单性使得信息的可视化变得快速而直观。

例如，使用泰坦尼克号的数据集来计算每个班级的人数：

```
import seaborn as sns  
import altair as alt  
  
titanic = sns.load_dataset("titanic")  
  
alt.Chart(titanic).mark_bar().encode(alt.X("class"), y="count()")  

```

Altair简洁的语法允许你专注于数据和它的关系，从而产生高效和富有表现力的可视化。

##### 易于数据转换

Altair使其在创建图表时毫不费力地进行数据转换。

例如，如果你想在泰坦尼克号数据集中找到每个性别的平均年龄，你可以在代码本身中进行转换：

```
hireable = (  
    alt.Chart(titanic)  
    .mark_bar()  
    .encode(x="sex:N", y="mean_age:Q")  
    .transform_aggregate(mean_age="mean(age)", groupby=["sex"])  
)  
  
hireable  

```

Altair的transform_aggregate()函数使你能够在飞行中汇总数据，并在你的可视化中使用这些结果。

你也可以使用`:N` 或`:Q`符号指定数据类型，如名义（没有任何顺序的分类数据）或定量（数值的衡量）。

查看数据转换的完整列表[6]。

##### 链接图表

Altair提供了令人印象深刻的将多个地块连接在一起的能力。你可以根据用户的互动，使用选择来过滤所附图块的内容。

例如，在散点图上直观地显示所选区间内每个阶层的人数：

```
brush = alt.selection(type="interval")  
  
points = (  
    alt.Chart(titanic)  
    .mark_point()  
    .encode(  
        x="age:Q",  
        y="fare:Q",  
        color=alt.condition(brush, "class:N", alt.value("lightgray")),  
    )  
    .add_selection(brush)  
)  
  
bars = (  
    alt.Chart(titanic)  
    .mark_bar()  
    .encode(y="class:N", color="class:N", x="count(class):Q")  
    .transform_filter(brush)  
)  
  
points &amp; bars  

```

当你在散点图中选择一个区间时，柱状图会动态更新以反映过滤后的数据。Altair连接图的能力允许高度互动的可视化和即时计算，不需要运行Python服务器。

#### 缺点

Altair的简单图表，如柱状图，可能看起来不像Seaborn或Plotly等库中的图表那样有风格，除非你指定自定义风格。

Altair建议在处理超过5000个样本的数据集时，在可视化之前对数据进行汇总。处理更大的数据集可能需要额外的步骤来管理数据大小和复杂性。

**经验之谈：Altair** 是创建复杂统计图表的绝佳选择。虽然它可能缺乏一些默认的样式选项，并且在处理大型数据集时有局限性，但Altair的简单性、数据转换能力和链接图使其成为统计可视化的强大工具。

### Bokeh

Bokeh是一个高度灵活的交互式可视化库，专为网络浏览器设计。

#### 优点

##### Matplotlib的交互式版本

在交互式可视化方面，Bokeh作为与Matplotlib最相似的库脱颖而出。Matplotlib是一个低级别的可视化库，而Bokeh同时提供了高级和低级别的接口。使用Bokeh，你可以创建类似于Matplotlib的复杂图，但代码行数更少，分辨率更高。

例如，Matplotlib的圆形图…

```
import matplotlib.pyplot as plt  
 fig, ax = plt.subplots()  
  
x = [1, 2, 3, 4, 5]  
y = [2, 5, 8, 2, 7]  
  
for x, y in zip(x, y):  
    ax.add_patch(  
        plt.Circle((x, y), 0.5, edgecolor="#f03b20", facecolor="#9ebcda", alpha=0.8)  
    )  
  
  
# Use adjustable='box-forced' to make the plot area square-shaped as well.  
ax.set_aspect("equal", adjustable="datalim")  
ax.set_xbound(3, 4)  
  
ax.plot()  # Causes an autoscale update.  
plt.show()  

```

…可以通过使用虚化技术实现更好的分辨率和更大的效用：

```
from bokeh.io import show, output_notebook  
from bokeh.models import Circle  
from bokeh.plotting import figure  
  
output_notebook()  
  
plot = figure(tools="tap", title="Select a circle")  
renderer = plot.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=50)  
  
selected_circle = Circle(fill_alpha=1, fill_color="firebrick", line_color=None)  
nonselected_circle = Circle(fill_alpha=0.2, fill_color="blue", line_color="firebrick")  
  
renderer.selection_glyph = selected_circle  
renderer.nonselection_glyph = nonselected_circle  
  
show(plot)  

```

##### 图表之间的联系

Bokeh使建立地块之间的联系变得非常容易。应用于一个图的变化可以自动反映在另一个具有类似变量的图中。这个功能允许探索多个地块之间的关系。

例如，如果你创建了三个并排的图形，并想观察它们的关系，你可以利用链接刷：

```
from bokeh.layouts import gridplot  
from bokeh.models import ColumnDataSource  
  
  
source = ColumnDataSource(new_profile)  
  
TOOLS = "box_select,lasso_select,help"  
TOOLTIPS = [  
    ("user", "@user_name"),  
    ("followers", "@followers"),  
    ("following", "@following"),  
    ("forks", "@forks"),  
    ("contribution", "@contribution"),  
]  
  
s1 = figure(tooltips=TOOLTIPS, title=None, tools=TOOLS)  
s1.circle(x="followers", y="following", source=source)  
  
s2 = figure(tooltips=TOOLTIPS, title=None, tools=TOOLS)  
s2.circle(x="followers", y="forks", source=source)  
  
s3 = figure(tooltips=TOOLTIPS, title=None, tools=TOOLS)  
s3.circle(x="followers", y="contribution", source=source)  
  
p = gridplot([[s1, s2, s3]])  
show(p)  

```

通过利用ColumnDataSource，数据可以在绘图之间共享。因此，当一个情节发生变化时，其他情节也会相应地自动更新。

#### 缺点

作为一个具有某种中间层次界面的库，Bokeh通常需要更多的代码来产生与Seaborn、Altair或Plotly相同的图。虽然Bokeh需要的代码比Matplotlib少，但与其他库相比，它可能需要额外的代码行来实现类似的质量输出。

例如，使用泰坦尼克号数据创建同样的计数图，除了需要提前转换数据外，如果我们想让图表看起来漂亮，还需要设置条形图的宽度和颜色。

如果我们不为条形图增加宽度，图表会是这样的：

```
from bokeh.transform import factor_cmap  
from bokeh.palettes import Spectral6  
  
titanic_groupby = titanic.groupby("class")["survived"].sum().reset_index()  
  
p = figure(x_range=list(titanic_groupby["class"]))  
p.vbar(  
    x="class",  
    top="survived",  
    source=titanic_groupby,  
    fill_color=factor_cmap(  
        "class", palette=Spectral6, factors=list(titanic_groupby["class"])  
    ),  
)  
show(p)  
  
from bokeh.transform import factor_cmap  
from bokeh.palettes import Spectral6  
  
titanic_groupby = titanic.groupby("class")["survived"].sum().reset_index()  
  
p = figure(x_range=list(titanic_groupby["class"]))  
p.vbar(  
    x="class",  
    top="survived",  
    source=titanic_groupby,  
    fill_color=factor_cmap(  
        "class", palette=Spectral6, factors=list(titanic_groupby["class"])  
    ),  
)  
show(p)  

```

因此，我们需要手动调整尺寸以使绘图更美观：

```
p = figure(x_range=list(titanic_groupby["class"]))  
p.vbar(  
    x="class",  
    top="survived",  
    width=0.9,  
    source=titanic_groupby,  
    fill_color=factor_cmap(  
        "class", palette=Spectral6, factors=list(titanic_groupby["class"])  
    ),  
)  
show(p)  

```

**经验之谈：Bokeh** 的独特优势在于它能够提供一系列的界面，从低到高，从而能够创建多功能的、具有视觉吸引力的图形。然而，与其他库相比，在追求类似的情节质量时，这种灵活性往往导致需要更多的代码。

### Folium

Folium[7]简化了在交互式小册子地图上实现数据可视化的过程。这个库提供了来自OpenStreetMap、Mapbox和Stamen的内置瓦片集。

#### 优点

##### 易于创建一个带有标记的地图

与Plotly、Altair和Bokeh等其他选项相比，Folium通过利用开放的街道地图提供了一种更直接的方法。这给人一种类似于谷歌地图的体验，而且代码最少。

还记得我们用Plotly创建的可视化Github用户位置的地图吗？有了Folium，我们可以进一步增强地图的外观。

```
import folium  
  
# 在一个列表中保存纬度、经度和地点的名称*  
lats = location_df["纬度"]  
lons = location_df["经度"]  
names = location_df["location"]  
  
# 用一个初始位置创建一个地图*  
m = folium.Map(location=[lats[0], lons[0]] )  
  
for lat, lon, name in zip(lats, lons, names):  
  # 用其他位置创建标记*  
  folium.Marker(  
    location=[lat, lon], popup=name, icon=folium.Icon(color="green")  
  ).add_to(m)  
  
m  

```

只用几行代码，我们就创建了一个显示用户位置的真实地图。

##### 添加地点

Folium通过允许加入标记，可以很容易地添加其他用户的潜在位置。

```
# 启用在地图中添加更多的位置  
m = m.add_child(folium.ClickForMarker(popup="Potential Location"))  

```

在地图上点击，就在你点击的地方生成一个新的位置标记。

##### 插件

Folium提供各种插件，可以与你的地图一起利用，包括Altair的插件。例如，如果我们想将全球Github用户的总星数热图可视化，并识别出拥有大量顶级用户和星数的地区，Folium热图插件就可以实现这一目的。

```
# heatmap  
  from folium.plugins import HeatMap  
  
m = folium.Map(location=[lats[0], lons[0]])  
  
HeatMap(data=location_df[["latitude", "longitude", "total_stars"]]).add_to(m)  
  
m  

```

**经验之谈：Folium** 只需几行代码就能创建互动地图。它提供了类似于谷歌地图的用户体验。

## 关于Python学习指南

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后给大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、自动化办公等学习教程。带你从零基础系统性的学好Python！</mark>

#### 👉Python所有方向的学习路线👈

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取）**</mark>

<img src="https://img-blog.csdnimg.cn/3c4ee87941694f3789398db3d52a2637.png#pic_center" alt="在这里插入图片描述">

#### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。

<img src="https://img-blog.csdnimg.cn/64c89bf6293d4699bf7ee8f34b9e69fd.png#pic_center" alt="在这里插入图片描述">

#### <mark>温馨提示：篇幅有限，已打包文件夹，获取方式在：文末</mark>

#### 👉Python70个实战练手案例&amp;源码👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/2017b67544f94e8898db755e2703224a.png#pic_center" alt="在这里插入图片描述">

#### 👉Python大厂面试资料👈

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自**阿里、腾讯、字节等一线互联网大厂**最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/3055c54d3224495987c589f150324d73.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b0751719fe914aec8c8d09f62f772e44.png#pic_center" alt="在这里插入图片描述">

#### 👉Python副业兼职路线&amp;方法👈

学好 Python 不论是就业还是做副业赚钱都不错，但要学会兼职接单还是要有一个学习规划。

<img src="https://img-blog.csdnimg.cn/01bcd7cbfd6d43fb85ef410766735154.png#pic_center" alt="在这里插入图片描述">

**👉** **这份完整版的Python全套学习资料已经上传，朋友们如果需要可以扫描下方CSDN官方认证二维码或者点击链接免费领取**【**`保证100%免费`**】

<font color="red">**点击免费领取《CSDN大礼包》： 安全链接免费领取**</font>
