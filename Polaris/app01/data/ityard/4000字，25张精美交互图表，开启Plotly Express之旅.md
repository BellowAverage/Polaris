
--- 
title:  4000字，25张精美交互图表，开启Plotly Express之旅 
tags: []
categories: [] 

---
Plotly Express 是一个新的高级 Python 可视化库，它是 Plotly.py 的高级封装，为复杂图表提供简单的语法。最主要的是 Plotly 可以与 Pandas 数据类型 DataFrame 完美的结合，对于数据分析、可视化来说实在是太便捷了，而且是完全免费的，非常值得尝试

下面我们使用 Ployly 的几个内置数据集来进行相关图表绘制的演示

<img src="https://img-blog.csdnimg.cn/img_convert/1aafa3e1778209de3d202c63c8004377.png" alt="1aafa3e1778209de3d202c63c8004377.png">

数据集

Plotly 内置的所有数据集都是 DataFrame 格式，也即是与 Pandas 深度契合的体现

#### 不同国家历年GDP收入与人均寿命

包含字段：国家、洲、年份、平均寿命、人口数量、GDP、国家简称、国家编号

```
gap = px.data.gapminder()
gap2007 = gap.query("year==2007")
gap2007
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/9f5a2cbfd99325271487f1f3be079b32.png" alt="9f5a2cbfd99325271487f1f3be079b32.png">

#### 餐馆的订单流水

包含字段：总账单、小费、性别、是否抽烟、星期几、就餐时间、人数

```
tips = px.data.tips()
tips
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/24b6827472fd5f742e4a23f93f352f15.png" alt="24b6827472fd5f742e4a23f93f352f15.png">

#### 鸢尾花

包含字段：萼片长、萼片宽、花瓣长、花瓣宽、种类、种类编号

```
iris = px.data.iris()  
iris
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/cfbe8618bf592dd244f9bf8c5651eb53.png" alt="cfbe8618bf592dd244f9bf8c5651eb53.png">

#### 风力数据

包含字段：方向、强度、数值

```
wind = px.data.wind()  
wind
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/d403370334893146b78c2679a4e0c92c.png" alt="d403370334893146b78c2679a4e0c92c.png">

#### 2013年蒙特利尔市长选举投票结果

包括字段：区域、Coderre票数、Bergeron票数、Joly票数、总票数、胜者、结果(占比分类)

```
election = px.data.election() 
election
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/dfdebb9ed7be5db11db155602e0faf47.png" alt="dfdebb9ed7be5db11db155602e0faf47.png">

#### 蒙特利尔一个区域中心附近的汽车共享服务的可用性

包括字段：纬度、经度、汽车小时数、高峰小时

```
carshare = px.data.carshare()
carshare
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/08cf3bd8a3f7e8ba512d4a85261d4368.png" alt="08cf3bd8a3f7e8ba512d4a85261d4368.png">

<img src="https://img-blog.csdnimg.cn/img_convert/82705e33e258bc88cc323fe513ef466e.png" alt="82705e33e258bc88cc323fe513ef466e.png">

内置调色板

Plotly 还拥有众多色彩高级的调色板，使得我们在绘制图表的时候不再为颜色搭配而烦恼

#### 卡通片的色彩和序列

```
px.colors.carto.swatches()
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/86aac6b9a8dba776aecf320d99a3e3b3.png" alt="86aac6b9a8dba776aecf320d99a3e3b3.png">

#### CMOcean项目的色阶

```
px.colors.cmocean.swatches()
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/5e40b7d0f63b8cc013b7e80847e2a74f.png" alt="5e40b7d0f63b8cc013b7e80847e2a74f.png">

还有其他很多调色板供选择，就不一一展示了，下面只给出代码，具体颜色样式可以自行运行代码查看

ColorBrewer2项目的色阶

```
px.colors.colorbrewer
```

周期性色标，适用于具有自然周期结构的连续数据

```
px.colors.cyclical
```

分散色标，适用于具有自然终点的连续数据

```
px.colors.diverging
```

定性色标，适用于没有自然顺序的数据

```
px.colors.qualitative
```

顺序色标，适用于大多数连续数据

```
px.colors.sequential
```

<img src="https://img-blog.csdnimg.cn/img_convert/6fc294afc26c25454c3042a373cd5bee.png" alt="6fc294afc26c25454c3042a373cd5bee.png">

Plotly Express 基本绘图

#### 散点图

Plotly 绘制散点图非常容易，一行代码就可以完成

```
px.scatter(gap2007, x="gdpPercap", y="lifeExp")
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/8762703834a31ba458f32d048d4c969a.png" alt="8762703834a31ba458f32d048d4c969a.png">

还可以通过参数 color 来区分不同的数据类别

```
px.scatter(gap2007, x="gdpPercap", y="lifeExp", color="continent")
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/34aa3280b4776459274561ab25d3e68d.png" alt="34aa3280b4776459274561ab25d3e68d.png">

这里每个点都代表一个国家，不同颜色则代表不同的大洲

可以使用参数 size 来体现数据的大小情况

```
px.scatter(gap2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60)
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/9abfaff2a551407cf8b88f8a973c7aff.png" alt="9abfaff2a551407cf8b88f8a973c7aff.png">

还可以通过参数 hover_name 来指定当鼠标悬浮的时候，展示的信息

<img src="https://img-blog.csdnimg.cn/img_convert/3fff3d80ed1a2e47b80db38177072068.gif" alt="3fff3d80ed1a2e47b80db38177072068.gif">

还可以根据数据集中不同的数据类型进行图表的拆分

```
px.scatter(gap2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", 
           size_max=60, hover_name="country", facet_col="continent", log_x=True)
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/8ac7b9f4b5ca8b7105adeb4ba704bbe5.png" alt="8ac7b9f4b5ca8b7105adeb4ba704bbe5.png">

我们当然还可以查看不同年份的数据，生成自动切换的动态图表

```
px.scatter(gap, x="gdpPercap", y="lifeExp", color="continent", size="pop", 
           size_max=60, hover_name="country", animation_frame="year", animation_group="country", log_x=True,
          range_x=[100, 100000], range_y=[25, 90], labels=dict(pop="Population", gdpPercap="GDP per Capa", lifeExp="Life Expectancy"))
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/0470b27585c8d00caaf9c9fbf39b2670.gif" alt="0470b27585c8d00caaf9c9fbf39b2670.gif">

#### 地理信息图

Plotly 绘制动态的地理信息图表也是非常方便，通过这种地图的形式，我们也可以清楚的看到数据集中缺少前苏联的相关数据

```
px.choropleth(gap, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year", 
              color_continuous_scale=px.colors.sequential.Plasma, projection="natural earth")
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/d40c61251d58538fa7cae93ff3181d5d.gif" alt="d40c61251d58538fa7cae93ff3181d5d.gif">

#### 矩阵散点图

```
px.scatter_matrix(iris, dimensions=['sepal_width', 'sepal_length', 'petal_width', 'petal_length'], color='species', symbol='species')
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/197a8b665b8e616b94d9233377c41f4a.png" alt="197a8b665b8e616b94d9233377c41f4a.png">

#### 平行坐标图

```
px.parallel_coordinates(tips, color='size', color_continuous_scale=px.colors.sequential.Inferno)
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/4de4b0a18d1c7d851dd36f6387a1aa80.png" alt="4de4b0a18d1c7d851dd36f6387a1aa80.png">

#### 三元散点图

```
px.scatter_ternary(election, a="Joly", b="Coderre", c="Bergeron", color="winner", size="total", hover_name="district",
                   size_max=15, color_discrete_map = {"Joly": "blue", 
                   "Bergeron": "green", "Coderre":"red"} )
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/d65ae63a3531d494964e903f15b0d8f9.png" alt="d65ae63a3531d494964e903f15b0d8f9.png">

#### 极坐标线条图

```
px.line_polar(wind, r="frequency", theta="direction", color="strength", 
            line_close=True,color_discrete_sequence=px.colors.sequential.Plotly3[-2::-1])
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/93be472090b9940d7749a30691fd6395.png" alt="93be472090b9940d7749a30691fd6395.png">

#### 小提琴图

```
px.violin(tips, y="tip", x="sex", color="smoker", facet_col="day", facet_row="time",box=True, points="all", 
          category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]},
          hover_data=tips.columns)
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/018bdd9a3b93a08e8317d62185ade997.png" alt="018bdd9a3b93a08e8317d62185ade997.png">

#### 极坐标条形图

```
px.bar_polar(wind, r="frequency", theta="direction", color="strength",
            color_discrete_sequence= px.colors.sequential.Plotly3[-2::-1])
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/45adbb7aa3b98c52206bbfbc694ece9c.png" alt="45adbb7aa3b98c52206bbfbc694ece9c.png">

#### 并行类别图

```
px.parallel_categories(tips, color="size", color_continuous_scale=px.
            colors.sequential.Inferno)
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/91484e2ffc81756eddb8c791288730bf.png" alt="91484e2ffc81756eddb8c791288730bf.png">

#### 直方图

```
px.histogram(tips, x="total_bill", color="smoker",facet_row="day", facet_col="time")
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/86062f3f8ab0c48d8032f2688e9b916b.png" alt="86062f3f8ab0c48d8032f2688e9b916b.png">

#### 三维散点图

```
px.scatter_3d(election, x="Joly", y="Coderre", z="Bergeron", color="winner", 
              size="total", hover_name="district",symbol="result", 
              color_discrete_map = {"Joly": "blue", "Bergeron": "green", 
              "Coderre":"red"})
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/0e2e9f84b64c02324a7dffcc001208a1.png" alt="0e2e9f84b64c02324a7dffcc001208a1.png">

#### 密度等值线图

```
px.density_contour(iris, x="sepal_width", y="sepal_length", color="species")
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/c03f9614767966919b90aae3f0eaf692.png" alt="c03f9614767966919b90aae3f0eaf692.png">

#### 箱形图

```
px.box(tips, x="sex", y="tip", color="smoker", notched=True)
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/b85be8e4ad0fc04da48f87df1eec3f55.png" alt="b85be8e4ad0fc04da48f87df1eec3f55.png">

#### 地理坐标线条图

```
px.line_geo(gap.query("year==2007"), locations="iso_alpha", 
            color="continent", projection="orthographic")
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/17cca010cf6c0f0ee3a17710836087c7.png" alt="17cca010cf6c0f0ee3a17710836087c7.png">

#### 条线图

```
px.line(gap, x="year", y="lifeExp", color="continent", 
        line_group="country", hover_name="country",
        line_shape="spline", render_mode="svg")
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/5986772dfa00c18540630c4baa518204.png" alt="5986772dfa00c18540630c4baa518204.png">

#### 面积图

```
px.area(gap, x="year", y="pop", color="continent", 
        line_group="country")
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/bb792c4c1a7f7ef7ccf96784ce0c11d4.png" alt="bb792c4c1a7f7ef7ccf96784ce0c11d4.png">

#### 热力图

```
px.density_heatmap(iris, x="sepal_width", y="sepal_length", 
                   marginal_x="rug", marginal_y="histogram")
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/6afade2e9e094191621f1739b85b990f.png" alt="6afade2e9e094191621f1739b85b990f.png">

#### 条形图

```
px.bar(tips, x="sex", y="total_bill", color="smoker", barmode="group")
```

Output

<img src="https://img-blog.csdnimg.cn/img_convert/cc33da9e4338aed5cc3bfc07ca6016c0.png" alt="cc33da9e4338aed5cc3bfc07ca6016c0.png">

总体来说，Plotly/Plotly Express 还是非常强大绘图工具，值得我们细细研究~

好了今天的分享就到这里，后续还会分享更多 Plotly 相关的知识，喜欢的小伙伴记得**星标**公众号，还要记得点赞和**在看**哦！
