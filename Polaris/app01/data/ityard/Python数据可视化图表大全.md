
--- 
title:  Python数据可视化图表大全 
tags: []
categories: [] 

---
可视化图表种类如此之多，什么场景下应该用什么图表展示，是一个让人头秃的难题。

数据可视化的爱好者Severino Ribecca，他在自己的网站上收录了 60 种可视化图表样式以及它们分别适用于什么样的场景，并且推荐了相应的制作工具。

值得一看。

**点阵图**

<img src="https://img-blog.csdnimg.cn/img_convert/27026f182dce668bfc43ebb383b3f93e.png" alt="27026f182dce668bfc43ebb383b3f93e.png">

点阵图表 (Dot Matrix Chart) 以点为单位显示离散数据，每种颜色的点表示一个特定类别，并以矩阵形式组合在一起。

适合用来快速检视数据集中不同类别的分布和比例，并与其他数据集的分布和比例进行比较，让人更容易找出当中模式。

**点数图**

<img src="https://img-blog.csdnimg.cn/img_convert/6376d02129de48100924e9f69735165e.png" alt="6376d02129de48100924e9f69735165e.png">

点数图 (Point &amp; Figure Charts)也称为「P&amp;F 图」，使用由 X 和 O 符号组成的一系列方格来显示特定资产的供需关系。

这种图表与时间无直接关系，主要集中看资产的过滤价格表现；它也不会显示交易量，其目的只是显示任何供需关系上的变化，称为「突破」(breakouts)。

推荐制作的工具有：rpnf。

**弧线图**

<img src="https://img-blog.csdnimg.cn/img_convert/50cd6e5e919b3fe842ad10753dad0397.png" alt="50cd6e5e919b3fe842ad10753dad0397.png">

弧线图 (Arc Diagram) 是二维双轴图表以外另一种数据表达方式。在弧线图中，节点将沿着 X轴放置，然后再利用弧线表示节点与节点之间的连接关系。

弧线图适合用来查找数据共同出现的情况。但缺点是：不能如其他双轴图表般清楚显示节点之间的结构和连接，而且过多连接也会使图表难于阅读。

推荐的制作工具有：Protovis (编程语言)、D3 (编程语言)。

**折线图**

<img src="https://img-blog.csdnimg.cn/img_convert/0cd5dfd0b30b80004c766b0ba03f651c.png" alt="0cd5dfd0b30b80004c766b0ba03f651c.png">

折线图用于在连续间隔或时间跨度上显示定量数值，最常用来显示趋势和关系。

此外，折线图也能给出某时间段内的「整体概览」，看看数据在这段时间内的发展情况。

推荐的制作工具有：MS Excel、Apple Numbers、D3、DataHero、Datamatic、Datawrapper、Envision.js、Google Charts、Google Docs、Infogr.am、OnlineChartTool.com、SlemmaVega。

**平行坐标图**

<img src="https://img-blog.csdnimg.cn/img_convert/aaf80c311fb14ec22fe5911e532c5f46.png" alt="aaf80c311fb14ec22fe5911e532c5f46.png">

平行坐标图 (Parallel Coordinates Plots) 能显示多变量的数值数据，最适合用来比较同一时间的多个变量，并展示它们之间的关系。

当数据密集时，平行坐标图容易变得混乱、难以辨认。解决办法是通过互动技术，突出显示所选定的一条或多条线，同时淡化所有其他线条，让我们能更集中研究感兴趣的部分，并滤除干扰数据。

推荐的制作工具有：D3、Protovis、RAWGraphs、The R Graph Gallery、Vega。

**网络图**

<img src="https://img-blog.csdnimg.cn/img_convert/7dd58905cc2ff999bd1d3be0e27f5467.png" alt="7dd58905cc2ff999bd1d3be0e27f5467.png">

也称为「网络地图」或「节点链路图」，用来显示事物之间的关系类型。

这些节点通常是圆点或小圆圈，但也可以使用图标。

网络图主要有分别为「不定向」和「定向」两种。不定向网络图仅显示实体之间的连接，而定向网络图则可显示连接是单向还是双向（通过小箭头）。

网络图数据容量有限，并且当节点太多时会形成类似「毛球」的图案，使人难以阅读。

推荐的制作工具有：Cytoscape、Datamatic、Gephi、Graph-tool、Mike Bostock's Block、Plot.ly、sigmajs、Vega、ZoomCharts。

**象形图**

<img src="https://img-blog.csdnimg.cn/img_convert/39958053edb4fa3a79b68ce98889959f.png" alt="39958053edb4fa3a79b68ce98889959f.png">

象形图 (Pictogram Chart) 也称为「象形统计图」，使用图案来显示数据量。

使用图案能克服语言、文化和教育水平方面的差异，是更具代表性的数据显示方法。举个例子，如果数据是「5 辆车」，图中便会显示 5 个汽车图案。

推荐的制作工具有：Infogr.am、jChart。

**直方图**

<img src="https://img-blog.csdnimg.cn/img_convert/de1258d773b7298da84909f821f76d54.png" alt="de1258d773b7298da84909f821f76d54.png">

直方图适合用来显示在连续间隔或特定时间段内的数据分布，有助于估计数值集中位置、上下限值以及确定是否存在差距或异常值；也可粗略显示概率分布。

推荐的制作工具有：MS Excel、Apple Numbers、D3、Datavisual、Google Docs、Infogr.am、OnlineChartTool.com、Protovis、R Graph Gallery、Slemma。

**密度图**

<img src="https://img-blog.csdnimg.cn/img_convert/563c9a73560ef7fe443cd8c1f1dec724.png" alt="563c9a73560ef7fe443cd8c1f1dec724.png">

密度图 (Density Plot) 又称为「密度曲线图」，用于显示数据在连续时间段内的分布状况。

这种图表是直方图的变种，使用平滑曲线来绘制数值水平，从而得出更平滑的分布，并且它们不受所使用分组数量的影响，所以能更好地界定分布形状 。

推荐的制作工具有：The R Graph Gallery、Cookbook for R。

**人口金字塔**

<img src="https://img-blog.csdnimg.cn/img_convert/6a21a209529db6a643c53345b52d06f4.png" alt="6a21a209529db6a643c53345b52d06f4.png">

人口金字塔 (Population Pyramid) 也称为「年龄性别金字塔」，是彼此背靠背的一对直方图，显示所有年龄组和男女人口的分布情况。

人口金字塔最适合用来检测人口模式的变化或差异。多个人口金字塔放在一起更可用于比较各国或不同群体之间的人口模式。

推荐制作的工具有：AnyChart、D3 (重叠版本)、Vega、ZingChart。

**条形图**

<img src="https://img-blog.csdnimg.cn/img_convert/63d4dedfc2782ae3c4180e0293198d8d.png" alt="63d4dedfc2782ae3c4180e0293198d8d.png">

### 条形图 (Bar Chart) 也称为「棒形图」或「柱形图」，采用水平或垂直条形（柱形图）来比较不同类别的离散数值。

### 

### 图表其中一条轴代表要比较的具体类别，另一条则用作离散数值的标尺。

条形图的离散数据是分类数据，针对的是单一类别中的数量多少，而不会显示数值在某时间段内的持续发展。

推荐的制作工具有：MS Excel &amp; Apple Numbers、AnyChart、D3 、DataHero、Datamatic、Datawrapper、Google Charts、Google Docs、Infogr.am、OnlineChartTool.com、Protovis、Slemma、Vega、ZoomCharts。

**多组条形图**

<img src="https://img-blog.csdnimg.cn/img_convert/7ebe9509e0fc2a358302aecaa3cc2712.png" alt="7ebe9509e0fc2a358302aecaa3cc2712.png">

多组条形图也称为「分组条形图」或「复式条形图」，是条形图的变种。

多组条形图通常用来将分组变量或类别与其他数据组进行比较，也可用来比较迷你直方图，每组内的每个条形将表示变量的显著间隔。

但缺点是，当有太多条形组合在一起时将难以阅读。

推荐的制作工具有：D3、DataHero、Datavisual、Datawrapper、Infogr.am、NVD3.js、R Graph Gallery、Slemma、Vega、Visage、ZoomCharts。

**堆叠式条形图**

<img src="https://img-blog.csdnimg.cn/img_convert/c5b62dc5b94047fcc1ff49c0a10419d6.png" alt="c5b62dc5b94047fcc1ff49c0a10419d6.png">

跟多组条形图不同，堆叠式条形图 (Stacked Bar Graph) 将多个数据集的条形彼此重迭显示，适合用来显示大型类别如何细分为较小的类别，以及每部分与总量有什么关系。

堆叠式条形图共分成两种：
- 简单堆叠式条形图。将分段数值一个接一个地放置，条形的总值就是所有段值加在一起，适合用来比较每个分组/分段的总量。- 100% 堆叠式条形图。会显示每组占总体的百分比，并按该组每个数值占整体的百分比来绘制，可用来显示每组中数量之间的相对差异。
推荐的制作工具有：MS Excel、Apple Numbers、AnyChart、Datavisual、Datawrapper、Infogr.am、Slemma、ZingChart、ZoomCharts。

**不等宽柱状图**

<img src="https://img-blog.csdnimg.cn/img_convert/da3b0f496fc5e4402c409a04c4eb48b2.png" alt="da3b0f496fc5e4402c409a04c4eb48b2.png">

不等宽柱状图 (Marimekko Chart)也称为「马赛克图」，用来显示分类数据中一对变量之间的关系，原理类似双向的 100% 堆叠式条形图，但其中所有条形在数值/标尺轴上具有相等长度，并会被划分成段。

不等宽柱状图的主要缺点在于难以阅读，特别是当含有大量分段的时候。此外，我们也很难准确地对每个分段进行比较，因为它们并非沿着共同基线排列在一起。

因此，不等宽柱状图较为适合提供数据概览。

推荐的制作工具有：D3。

**面积图**

<img src="https://img-blog.csdnimg.cn/img_convert/cdf970d6696450719fc8e262d5b705a6.png" alt="cdf970d6696450719fc8e262d5b705a6.png">

面积图 (Area Graph) 是折线图的一种，但线下面的区域会由颜色或纹理填满。

跟折线图一样，面积图可显示某时间段内量化数值的变化和发展，最常用来显示趋势，而非表示具体数值。

两种较常用的面积图是分组式面积图和堆叠式面积图。分组式面积图在相同的零轴开始，而堆叠式面积图则从先前数据系列的最后数据点开始。

推荐的制作工具有：MS Excel &amp; Apple Numbers、D3、DataHero、Datamatic、Google Charts、Google Docs、Infogr.am、Protovis、Slemma、VegaOnlineChartTool.com。

**比例面积图**

<img src="https://img-blog.csdnimg.cn/img_convert/829324cf4adc9216d49686b7547b949a.png" alt="829324cf4adc9216d49686b7547b949a.png">

非常适合用来比较数值和显示比例（尺寸、数量等），以便快速全面地了解数据的相对大小，而无需使用刻度。

比例面积图通常使用正方形或圆形，常见技术错误是，使用长度来确定形状大小，而非计算形状中的空间面积，导致数值出现指数级的增长和减少。

推荐的制作工具有：D3、Datamatic、Datavisual、Infogr.am

**堆叠式面积图**

<img src="https://img-blog.csdnimg.cn/img_convert/cdb299447ffb313afd849ec522805c01.png" alt="cdb299447ffb313afd849ec522805c01.png">

堆叠式面积图 (Stacked Area Graph) 的原理与简单面积图相同，但它能同时显示多个数据系列，每一个系列的开始点是先前数据系列的结束点。

堆叠式面积图使用区域面积来表示整数，因此不适用于负值。总的来说，它们适合用来比较同一间隔内多个变量的变化。

推荐的制作工具有：MS Excel、Apple Numbers、DataHero、Datavisual、Google Docs、Infogr.am、OnlineChartTool、Slemma、Vega、ZingChart、ZoomCharts。

**量化波形图**

<img src="https://img-blog.csdnimg.cn/img_convert/cfdcd52aff1e74b5c439afa3e98eeb5c.png" alt="cfdcd52aff1e74b5c439afa3e98eeb5c.png">

这种图表是堆叠式面积图的一种变体，但其数值并非沿着固定直线轴来绘制，而是围绕着不断变化的中心基线。

通过使用流动的有机形状，量化波形图 (Stream Graph) 可显示不同类别的数据随着时间的变化，这些有机形状有点像河流，因此量化波形图看起来相当美观。

在量化波形图中，每个波浪的形状大小都与每个类别中的数值成比例。与波形图平行流动的轴用作时间刻度。我们也可以用不同颜色区分每个类别，或者通过改变色彩来显示每个类别的附加定量值。

此外，当他们以互动形式展示时，比静态或印刷出来更有效率。

推荐的制作工具有：Bob Rudis' GitHub、D3、infogr.am、JSFiddle、Lee Byron's GitHub、NVD3.js、plotDB、Protovis、RAWGraphs、Stream graph generator。

**雷达图**

<img src="https://img-blog.csdnimg.cn/img_convert/70491e4bcdf4ff0311f97af64adffdb9.png" alt="70491e4bcdf4ff0311f97af64adffdb9.png">

雷达图 (Radar Chart) 又称为「蜘蛛图」、「极地图」或「星图」，是用来比较多个定量变量的方法，可用于查看哪些变量具有相似数值，或者每个变量中有没有任何异常值。

此外，雷达图也可用于查看数据集中哪些变量得分较高/低，是显示性能表现的理想之选。

每个变量都具有自己的轴（从中心开始）。所有的轴都以径向排列，彼此之间的距离相等，所有轴都有相同的刻度。轴与轴之间的网格线通常只作指引用途。每个变量数值会画在其所属轴线之上，数据集内的所有变量将连在一起形成一个多边形。

推荐的制作工具有：Amcharts、AnyChart、Google Docs、jChartFX、Online Chart Tool、ZingChart。

**桑基图**

<img src="https://img-blog.csdnimg.cn/img_convert/cbef287959648ba9b94889a180bec1aa.png" alt="cbef287959648ba9b94889a180bec1aa.png">

桑基图 (Sankey Diagram) 用来显示流向和数量。

在每个流程阶段中，流向箭头或线可以组合在一起，或者往不同路径各自分开。我们可用不同颜色来区分图表中的不同类别，或表示从一个阶段到另一个阶段的转换。

推荐的制作工具有：RAWGraphs、Sankey Diagram Generator、Sankey Diagrams Blog Software List、Sankey Flow Show、SankeyMATIC、Tamc。

**平行集合图**

<img src="https://img-blog.csdnimg.cn/img_convert/e7981e6f805ad18cc36e8d1ba23582fe.png" alt="e7981e6f805ad18cc36e8d1ba23582fe.png">

平行集合图与桑基图类似，都显示流程和比例，但平行集合图不使用箭头，它们在每个所显示的线集 (line-set) 划分流程路径。

每个线集对应于一个维度/数据集，其数值/类别由该线集内的不同线段所表示。每条线的宽度和流程路径，均由类别总数的比例份数所决定。每条流程路径都可以用不同颜色代表，以显示和比较不同类别之间的分布。

推荐工具有：EagerEyes: ParallelSets、Jason Davies、Sankey Diagram Generator、SankeyMATIC。

**误差线**

<img src="https://img-blog.csdnimg.cn/img_convert/b0c46f9fc474893997e7598641aa67c3.png" alt="b0c46f9fc474893997e7598641aa67c3.png">

误差线可以作为一项增强功能来显示数据变化，通常用于显示范围数据集中的标准偏差、标准误差、置信区间或最小/最大值。

误差线总是平行于定量标尺的轴线，可以是垂直或水平显示（取决于定量标尺是在 Y 轴还是 X 轴上）。

推荐的工具有：AnyChart、Highcharts、plotly、Vega。

**树形结构图**

<img src="https://img-blog.csdnimg.cn/img_convert/52e6caed302fa246a7953eb5e13b8eae.png" alt="52e6caed302fa246a7953eb5e13b8eae.png">

树状结构图 (Treemap) 是一种利用嵌套式矩形显示层次结构的方法，同时通过面积大小显示每个类别的数量。

每个类别会获分配一个矩形区域，而其子类别则由嵌套在其中的小矩形代表。当不同数量被分配到各个类别时，这些矩形的面积大小会与此数量成正比显示。

Ben Shneiderman 最初开发树状结构图用来在计算机上显示大量文件目录，而不会占用太多屏幕空间，因此树状结构图是一种紧凑而且节省空间的层次结构显示方式，可让人快速了解结构。

推荐的制作工具有：AnyChart、D3、Datamatic、Google Charts、Google Docs、Infogr.am、jChartFX、RAWGraphs、Slemma、Vega、ZingChart。

**圆堆积图**

<img src="https://img-blog.csdnimg.cn/img_convert/ca60929523fd37c82147ba81b9611a18.png" alt="ca60929523fd37c82147ba81b9611a18.png">

圆堆积 (Circle Packing) 也称为「圆形树结构图」，是树形结构图的变体，使用圆形（而非矩形）一层又一层地代表整个层次结构。

每个圆形的面积也可用来表示额外任意数值，如数量或文件大小。我们也可用颜色将数据进行分类，或通过不同色调表示另一个变量。

虽然圆堆积看起来漂亮，但不及树形结构图般节省空间（因为圆圈内会有很多空白处），可是它实际上比树形结构图更能有效显示层次结构。

推荐的制作工具有：D3、D3 Zoomable、RAWGraphs。

**饼图**

<img src="https://img-blog.csdnimg.cn/img_convert/4905c66f8710cd4dc030dd83c0e22479.png" alt="4905c66f8710cd4dc030dd83c0e22479.png">

饼形图 (Pie Chart) 把一个圆圈划分成不同比例的分段，以展示各个类别之间的比例。

饼形图适合用来快速展示数据比例分布，但主要缺点是：不能显示太多项目、通常需要图例说明、不能准确比较。

制作工具有很多：D3、DataHero、Datamatic、Datavisual、Datawrapper、Google Charts、 Google Docs、Infogr.am、Protovis、OnlineChartTool.com、Slemma、ZingChart...

**圆环图**

<img src="https://img-blog.csdnimg.cn/img_convert/7d90153a321909980d25202e908980bb.png" alt="7d90153a321909980d25202e908980bb.png">

圆环图 (Donut Chart) 基本上就是饼形图，只是中间的部分被切掉。

不过，圆环图还是比饼形图略有优势，它让人不再只看「饼」的面积，反面更重视总体数值的变化：专注于阅读弧线的长度，而不是比较「饼与饼」之间的比例不同。

另外，圆环图中间的空白处更可以用来显示其他信息，因此更能节省空间。

推荐的制作工具有：D3、DataHero、Datamatic、Datavisual、Datawrapper、Google Docs、Infogr.am、Protovis、Slemma、Visage、ZingChart、ZoomCharts。

**南丁格尔玫瑰图**

<img src="https://img-blog.csdnimg.cn/img_convert/fde0fae0bbe5279a1eeadb2974487c87.png" alt="fde0fae0bbe5279a1eeadb2974487c87.png">

南丁格尔玫瑰图 (Nightingale Rose Charts) 又称为「极面积图」。

统计学家和医学改革家佛罗伦萨‧南丁格尔 (Florence Nightingale) 曾在克里米亚战争期间使用这种图表传达士兵身亡情况，故得名。

在南丁格尔玫瑰图中，代表数值的是分段面积，而不是其半径。

推荐的制作工具有：Datamatic、Infogr.am。

**旭日图**

<img src="https://img-blog.csdnimg.cn/img_convert/e313bd87a1cbacd9c218c850f13ccdbf.png" alt="e313bd87a1cbacd9c218c850f13ccdbf.png">

也称为「多层饼形图」或「径向树图」，通过一系列的圆环显示层次结构，再按不同类别节点进行切割。

推荐的制作工具有：Aculocity、D3、JavaScript InfoVis Toolkit、MS Office、Protovis、RAWGraphs、

**螺旋图**

<img src="https://img-blog.csdnimg.cn/img_convert/19296121864ec7b50309001d5fef944f.png" alt="19296121864ec7b50309001d5fef944f.png">

也称为「时间系列螺旋图」，沿阿基米德螺旋线 (Archimedean spiral) 画上基于时间的数据。

图表从螺旋形的中心点开始往外发展。螺旋图十分多变，可使用条形、线条或数据点，沿着螺旋路径显示。

螺旋图很适合用来显示大型数据集，通常显示长时间段内的数据趋势，因此能有效显示周期性的模式。

推荐的制作工具有：Arpit Narechania's Block。

**径向条形图**

<img src="https://img-blog.csdnimg.cn/img_convert/52770741421216bab8f34008edfa5bb1.png" alt="52770741421216bab8f34008edfa5bb1.png">

径向条形图是在极坐标系上绘制的条形图。

虽然看起来很美观，但径向条形图上条形的长度可能会被人误解。

推荐制作工具有：AnyChart。

**径向柱图**

<img src="https://img-blog.csdnimg.cn/img_convert/bde1e39a2ed02e1ed443cd4cd03c5365.png" alt="bde1e39a2ed02e1ed443cd4cd03c5365.png">

也称为「圆形柱图」或「星图」。

这种图表使用同心圆网格来绘制条形图。每个圆圈表示一个数值刻度，而径向分隔线则用作区分不同类别或间隔（如果是直方图）。

条形通常从中心点开始向外延伸，但也可以别处为起点以显示数值范围（如跨度图）。此外，条形也可以如堆叠式条形图般堆叠起来。

推荐的制作工具有：jChartFX、Bokeh。

**热图**

<img src="https://img-blog.csdnimg.cn/img_convert/6b574bac7791cc18a11364724c4d1ac5.png" alt="6b574bac7791cc18a11364724c4d1ac5.png">

热图 (Heatmap) 通过色彩变化来显示数据，当应用在表格时，热图适合用来交叉检查多变量的数据。

热图适用于显示多个变量之间的差异；显示当中任何模式；显示是否有彼此相似的变量；以及检测彼此之间是否存在任何相关性。

由于热图依赖颜色来表达数值，它比较适合用来显示广泛数值数据，因为要准确地指出色调之间的差异始终有难度，也较难从中提取特定数据点（除非在单元格中加入原始数据）。

推荐的制作工具有：MS Excel、Apple Numbers、Amcharts、AnyChart、Highcharts、jChartFX、plot.ly、R Graph、Zing Chart。

**散点图**

<img src="https://img-blog.csdnimg.cn/img_convert/b90e89c191a1effcaa0c324367657215.png" alt="b90e89c191a1effcaa0c324367657215.png">

散点图 (Scatterplot) 也称为「点图」、「散布图」或「X-Y 点图」，用来显示两个变量的数值（每个轴上显示一个变量），并检测两个变量之间的关系或相关性是否存在。

图表中可加入直线或曲线来辅助分析，并显示当所有数据点凝聚成单行时的模样，通常称为「最佳拟合线」或「趋势线」。

如您有一对数值数据，可使用散点图来查看其中一个变量是否在影响着另一个变量。可是请记住，相关性并非因果关系，也有可能存在另一个变量在影响着结果。

推荐的制作工具有：MS Excel、Apple Numbers、D3、DataHero、Datavisual、Google Charts、Google Docs、Infogr.am、OnlineChartTool.com、Vega、Visage、ZingChart。

**气泡图**

<img src="https://img-blog.csdnimg.cn/img_convert/f704e8e6a848b31e466eeea668a60190.png" alt="f704e8e6a848b31e466eeea668a60190.png">

气泡图是一种包含多个变量的图表，结合了散点图和比例面积图，圆圈大小需要按照圆的面积来绘制，而非其半径或直径。

通过利用定位和比例，气泡图通常用来比较和显示已标记/已分类的圆圈之间的关系。

可是，过多气泡会使图表难以阅读，但我们可以在图表中加入交互性功能来解决这个问题（点击或把鼠标悬停在气泡上以显示隐藏信息），也可选择重组或筛选分组类别。

推荐制作的工具有：AnyChart、Google Charts、Google Docs、Infogr.am、jChartFX、Online Chart Tool、RAWGraphs、Slemma、Visage、ZingChart

**气泡地形图**

<img src="https://img-blog.csdnimg.cn/img_convert/45d2c5eb9414f3f1af922523d3381999.png" alt="45d2c5eb9414f3f1af922523d3381999.png">

在这种数据地图中，指定地理区域上方会显示圆形图案，圆形面积与其在数据集中的数值会成正比。

气泡地图适合用来比较不同地理区域之间的比例，而不会受区域面积的影响。但气泡地图的主要缺点在于：过大的气泡可能会与地图上其他气泡或区域出现重迭。

推荐的制作工具有：AnyChart、CARTO、Datavisual、Khartis、Google docs、Polymaps、ZoomCharts。

**地区分布图**

<img src="https://img-blog.csdnimg.cn/img_convert/471b968580b2b60dff9a0bf6023a07bd.png" alt="471b968580b2b60dff9a0bf6023a07bd.png">

地区分布图通常用来显示不同区域与数据变量之间的关系，并把所显示位置的数值变化或模式进行可视化处理。

我们在地图上每个区域以不同深浅度的颜色表示数据变量，例如从一种颜色渐变成另一种颜色、单色调渐进、从透明到不透明、从光到暗，甚至动用整个色谱。

但缺点是无法准确读取或比较地图中的数值。此外，较大的地区会比较小区域更加显眼，影响读者对数值的感知。

绘制地区分布图时的常见错误：对原始数据值（例如人口）进行运算，而不是使用归一化值（例：计算每平方公里的人口）。

推荐的制作工具有：amMaps、D3、d3.geomap、Google Charts、Google Docs、DataHero、Datamatic、Datawrapper、Infogr.am、Kartograph、Polymaps、Slemma、Target Map.com、Vega。

**点示地图**

<img src="https://img-blog.csdnimg.cn/img_convert/94c79cea8b5dd42496ef8bd5e0ea42db.png" alt="94c79cea8b5dd42496ef8bd5e0ea42db.png">

点示地图 (Dot Map) 也称为「点示分布图」或「点示密度图」。在地理区域上放置相等大小的圆点，旨在检测该地域上的空间布局或数据分布。

点示地图共有两种：一对一（每点代表单一计数或一件物件）和一对多（每点表示一个特定单位，例如 1 点 = 10棵树）。

点示地图非常适合用来查看物件在某地域内的分布状况和模式，而且容易掌握，能提供数据概览。

推荐的制作工具有：AnyChart、CARTO、Datavisual、Infogr.am、Khartis、mbostock's blocks、R Graph Gallery、ZoomCharts。

**连接地图**

<img src="https://img-blog.csdnimg.cn/img_convert/9b9c17bea868a22eb9d127096ed6f585.png" alt="9b9c17bea868a22eb9d127096ed6f585.png">

连接地图 (Connection Map) 是用直线或曲线连接地图上不同地点的一种图表。

连接地图非常适合用来显示地理连接和关系，也可以通过研究连接地图上的连接分布或集中程度来显示空间格局。

推荐的制作工具是：AnyChart、ECharts、Javascript Maps、Curved、Straight、ZoomCharts。

**流向地图**

<img src="https://img-blog.csdnimg.cn/img_convert/051e83c317d07c4b6a0a936ac99050d7.png" alt="051e83c317d07c4b6a0a936ac99050d7.png">

流向地图 (Flow Map) 在地图上显示信息或物体从一个位置到另一个位置的移动及其数量，通常用来显示人物、动物和产品的迁移数据。

单一流向线所代表的移动规模或数量由其粗幼度表示，有助显示迁移活动的地理分布。

推荐的制作工具有：AnyChart。

**甘特图**

<img src="https://img-blog.csdnimg.cn/img_convert/9b9557438956409e0b2e704cadc84b52.png" alt="9b9557438956409e0b2e704cadc84b52.png">

甘特图 (Gantt Chart) 通常用作项目管理的组织工具，显示活动（或任务）列表和持续时间，也显示每项活动何时开始和结束。

甘特图适合用来规划和估计整个项目的所需时间，也可显示相互重迭的活动。

推荐的制作工具有：AnyChart、Amcharts、DHTMLX、GanttPro、Google Charts、Redbooth、RAWGraphs、Smartsheet。

**箱形图**

<img src="https://img-blog.csdnimg.cn/img_convert/d03d07e91727db5e580913b4d5bd8680.png" alt="d03d07e91727db5e580913b4d5bd8680.png">

箱形图又称为「盒须图」或「箱线图」，能方便显示数字数据组的四分位数，可以垂直或水平的形式出现。

从盒子两端延伸出来的线条称为「晶须」(whiskers)，用来表示上、下四分位数以外的变量。异常值 (Outliers) 有时会以与晶须处于同一水平的单一数据点表示。

箱形图通常用于描述性统计，是以图形方式快速查看一个或多个数据集的好方法。

推荐的制作工具有：AnyChart、D3、Protovis、R AWGraphs、R Graph Gallery、ZingChart。

**子弹图**

<img src="https://img-blog.csdnimg.cn/img_convert/8bcfb9a282dc7bafe80f04ea2d467c28.png" alt="8bcfb9a282dc7bafe80f04ea2d467c28.png">

子弹图 (Bullet Graph) 的功能类似于条形图，但加入更多视像元素，提供更多补充信息。

子弹图最初由 Stephen Few 开发，用来取代仪表盘上如里程表或时速表这类图形仪表，解决显示信息不足的问题，而且能有效节省空间，更可除掉仪表盘上一些不必要的东西。

推荐的制作工具有：am chartsAnyChart、D3、DimpleJS、IgniteUI、jChartFX 、moderndata.plot.ly、NVD3.js、Protovis。

**蜡烛图**

<img src="https://img-blog.csdnimg.cn/img_convert/532c5ab382e3af5bfce8a82212d820d6.png" alt="532c5ab382e3af5bfce8a82212d820d6.png">

又名「日本K线图」，通常用来显示和分析证券、衍生工具、外汇货币、股票、债券等商品随着时间的价格变动。

蜡烛图通过使用烛台式的符号来显示多种价格信息，例如开盘价、收盘价、最高价和最低价，每个代表单一时间段（每分钟、每小时、每天或每月）的交易活动。每个烛台符号沿着 X 轴上的时间刻度绘制，显示随着时间推移的交易活动。

但是，蜡烛图只能显示开盘价和收盘价之间的关系，而非两者之间所发生的事件，因此也无法用来解释交易波动的缘由。

推荐的制作工具有：Aaron Beppu's Block、amcharts、AnyChart、CanvasJS、ECharts、Google Chart、Google Docs、infogr.am、plotly、Protovis、ZingChart、ZoomCharts

**跨度图**

<img src="https://img-blog.csdnimg.cn/img_convert/997b3dcd4a956cc7242f61311354c86b.png" alt="997b3dcd4a956cc7242f61311354c86b.png">

也称为「范围条形/柱形图」或「浮动条形图」，用来显示数据集内最小值和最大值之间的范围，适合用来比较范围，尤其是已分类的范围。

跨度图只集中显示极端数值，不提供任何关于最小值和最大值之间的数值、整体平均值或数据分布等其他信息。

推荐制作工具有：AnyChart、D3, Arpit Narechania's Block、ZingChart。

**卡吉图**

<img src="https://img-blog.csdnimg.cn/img_convert/8a5614834a77dfebe2ecd94dc5b4115a.png" alt="8a5614834a77dfebe2ecd94dc5b4115a.png">

卡吉图 (Kagi Chart)能通过一系列线段显示价格表现，进而显示特定资产的一般供需水平。由于与时间无直接关系，它能更清晰地显示重要的价格走势。

推荐的制作工具有：D3、Arpit Narechania's Block、FusionCharts、Ragu Ramaswamy's Block、Wolfram Mathematica、

**美国线**

<img src="https://img-blog.csdnimg.cn/img_convert/5dc7cdad5d4335352206daf27698a8dc.png" alt="5dc7cdad5d4335352206daf27698a8dc.png">

美国线 (Open-high-low-close Charts) 也称为「OHLC 图」或「价格图」，通常用作交易工具，显示和分析证券、货币、股票、债券等商品随时间的价格变动。

推荐的制作工具有：Amcharts、AnyChart、ByteMuse.com、CanvasJS、jChartFX、Plotly、vaadin、Zing Chart。

**弦图**

<img src="https://img-blog.csdnimg.cn/img_convert/fb15606f05a08794aebe323d0115c4c9.png" alt="fb15606f05a08794aebe323d0115c4c9.png">

弦图 (Chord Diagram) 可以显示不同实体之间的相互关系和彼此共享的一些共通之处，因此这种图表非常适合用来比较数据集或不同数据组之间的相似性。

节点围绕着圆周分布，点与点之间以弧线或贝塞尔曲线彼此连接以显示当中关系，然后通过每个圆弧的大小比例再给每个连接分配数值。此外，也可以用颜色将数据分成不同类别，有助于进行比较和区分。

推荐的制作工具有：Circos、D3、R Graph Gallery、ZingChart。

**非彩带弦图**

<img src="https://img-blog.csdnimg.cn/img_convert/0d3f6f95279f1d81c1346cbea8d7cb02.png" alt="0d3f6f95279f1d81c1346cbea8d7cb02.png">

非彩带弦图 (Non-ribbon Chord Diagram) 是弦图的一个精简版本，仅显示节点和连接线，更加强调数据之间的连接关系。

推荐的制作工具有：Circos。

**树形图**

<img src="https://img-blog.csdnimg.cn/img_convert/85c8f26fc67ecf2bb73f0aa9bceab2e4.png" alt="85c8f26fc67ecf2bb73f0aa9bceab2e4.png">

树形图 (Tree Diagram) 也称为「组织图」或「链路图」，是通过树状结构表示层次结构的一种方式。

其结构通常由没有上级/父级成员的元素开始（根节点），然后加入节点，再用线连在一起，称为分支，表示成员之间的关系和连接。最后是枝叶节点（或称为末端节点），是没有子节点的成员。

树形图通常用于表示家庭关系和血统、分类学、进化科学、计算机科学与数学等，也是企业和组织的管理工具。

推荐的工具有：Datamatic、Google Charts、Google Docs、giffy、Zoomcharts。

**流程图**

<img src="https://img-blog.csdnimg.cn/img_convert/584cfc84674c42cf1cabe8bc869d2b20.png" alt="584cfc84674c42cf1cabe8bc869d2b20.png">

流程图 (Flow Chart) 使用一系列相互连接的符号绘制出整个过程，从而解释复杂和/或抽象的过程、系统、概念或算法的运作模式。

不同符号代表不同意思，每种都具有各自的特定形状。流程图以弧形矩形表示流程的开始和结束；线段或箭头用于显示从一个步骤到另一个步骤的方向或流程；简单的指令或动作用矩形来表示，而当需要作出决定时，则使用钻石形状...

推荐的制作工具有：asciiflow、Creately、draw.io、gliffy、GoJS、Google Drawings、LucidChart、MS Visio。

**脑力激荡图图**

<img src="https://img-blog.csdnimg.cn/img_convert/3e932d68ea6c98b5be4cdfb5cabb43aa.png" alt="3e932d68ea6c98b5be4cdfb5cabb43aa.png">

脑力激荡图也称为「心智图」，可以将相关想法、单词、图像和概念联合在一起。

脑力激荡图经常在项目初期使用，用来产生想法、查找关联、分类想法、组织信息、显示结构和一般学习。

推荐的制作工具有：Coggle、MindMup

**记数符号图表**

<img src="https://img-blog.csdnimg.cn/img_convert/3d15d1e46c995d4dffe2d4c872fc6bdd.png" alt="3d15d1e46c995d4dffe2d4c872fc6bdd.png">

记数符号图表 (Tally Chart) 既是记录工具，也可通过使用标记数字系统来显示数据分布频率。

在绘制记数符号图表时，将类别、数值或间隔放置在同一个轴或列（通常为 Y 轴或左侧第一列）上。每当出现数值时，在相应的列或行中添加记数符号。

完成收集所有数据后，把所有标记加起来并把总数写在下一列或下一行中，最终结果类似于直方图。

推荐的制作工具有：纸和笔。

**日历图**

<img src="https://img-blog.csdnimg.cn/img_convert/3bb75fdeb6efd1a9db519525f5861ee2.png" alt="3bb75fdeb6efd1a9db519525f5861ee2.png">

人类曾开发出各种日历系统作为组织工具，帮助我们提前做好计划。我们也把日历当作可视化工具，适用于显示不同时间段的活动事件的组织情况。

今天我们最常用的日历形式是公历，每个月份的月历由七个垂直列组成（代表每周七天），另有约五至六行以水平方式代表星期。

可是，日历格式并没有严格规定，所以市面上有各式各样不同的设计，只要能以时间顺序显示日期或时间单位便可。

推荐的制作工具有：TimeandDate.com、Calendar Creator、ZingChart

**时间线**

<img src="https://img-blog.csdnimg.cn/img_convert/3d42b4f53d11416c8a425fdb01cddc0a.png" alt="3d42b4f53d11416c8a425fdb01cddc0a.png">

时间线 (Timeline) 是以时间顺序显示一系列事件的图象化方式，主要功能是传达时间相关信息，用于分析或呈现历史故事。

如果是按比例绘制的时间线，我们可以通过查看不同事件之间的时间间隔，了解事件发生的时间或即将在何时发生，从中查找时间段内的事件是否遵循任何模式，或者事件在该时间段内如何分布。

有时时间线会与图表相互结合，显示定量数据随时间的变化。

推荐的制作工具有：Google Charts、Timeline.js、Tiki-Toki、Vega。

**时间表**

<img src="https://img-blog.csdnimg.cn/img_convert/51cf319f63d9aeaab95bf650867316f7.png" alt="51cf319f63d9aeaab95bf650867316f7.png">

时间表 (Timetable) 可用作预定事件、任务和行动的引用和管理工具。

使用表格按时间顺序和/或字母顺序组织数据，能有助用户快速进行引用。

**象形图**

<img src="https://img-blog.csdnimg.cn/img_convert/d55c7143ae9ee4371dfe91b8555389c9.png" alt="d55c7143ae9ee4371dfe91b8555389c9.png">

说明图旨在使用笔记、标签和图例来解释说明所显示的图像，以便解释概念或方法、描述物件或场所、显示事情的运作变化或帮助了解所显示的主题。

所使用的图像可以是象征性、图像化或真实相片。

**茎叶图**

<img src="https://img-blog.csdnimg.cn/img_convert/1418752655744777846220b815b365e8.png" alt="1418752655744777846220b815b365e8.png">

茎叶图 (Stem &amp; Leaf Plots) 又称为「枝叶图」，是一种按位数 (place value)组织数据的方法，可用来显示数据分布。

不变的位数由小至大、由上至下显示在中间的「茎」（通常是以十为单位），每个位数之内的数据则会成为「叶」并横向延伸。

除了向读者快速提供数据分布信息之外，茎叶图也可用于突出异常值和查找模式。如果您有两个数据集，则可使用背对背或双重茎叶图来比较两者。

推荐的制作工具有：CalculatorSoup、Easycalculation.com、Protovis。

**文氏图**

<img src="https://img-blog.csdnimg.cn/img_convert/ee9e63f6bcb725de7ccc9d6d368429d7.png" alt="ee9e63f6bcb725de7ccc9d6d368429d7.png">

文氏图 (Venn Diagram) 也称为「集合图」，显示集与集之间所有可能存在的逻辑关系，每个集通常以一个圆圈表示。

每个集都是一组具有共同之处的物件或数据，当多个圆圈（集）相互重迭时，称为交集 (intersection)，里面的数据同时具有重迭集中的所有属性。

推荐工具有：Datamatic、gliffy、R Graph Gallery、ZingChart。

**小提琴图**

<img src="https://img-blog.csdnimg.cn/img_convert/1fc23fb3673061626bb68656ac3b0268.png" alt="1fc23fb3673061626bb68656ac3b0268.png">

小提琴图 (Violin Plot) 结合了箱形图和密度图的特征，主要用来显示数据的分布形状。

中间的黑色粗条表示四分位数范围，从其延伸的幼细黑线代表 95% 置信区间，而白点则为中位数。

推荐的制作工具有：The R Graph Gallery、seaborn、z-m-k's Blocks。

**字云图**

<img src="https://img-blog.csdnimg.cn/img_convert/28d971077752861ffc065aef539628ec.png" alt="28d971077752861ffc065aef539628ec.png">

字云图 (Word Cloud) 也称为「标签云图」、「词云」等，每个此的大小与其出现频率成正比，以此显示不同单词在给定文本中的出现频率，然后将所有的字词排在一起，形成云状图案。

在字云图上使用颜色通常都是毫无意义的，主要是为了美观，但我们可以用颜色对单词进行分类。

推荐的制作工具有：D3、Datamatic、Infogr.am、R Graph Gallery、Vega、Visage、Wordclouds.com、Wordle、ZingChart。

推荐阅读  点击标题可跳转
- - - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/56917237919151e1599d251c9294d68f.gif" alt="56917237919151e1599d251c9294d68f.gif">
