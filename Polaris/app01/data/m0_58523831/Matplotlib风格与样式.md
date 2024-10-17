
--- 
title:  Matplotlib风格与样式 
tags: []
categories: [] 

---
### 1. Matplotlib 风格

为了满足不同的应用需求，`Matplotlib` 中包含了 `28` 种不同的风格，在进行绘图时，可以根据需要选择不同的绘图风格。使用以下代码可以获取 `Matplotlib` 中所有可用的风格：

```
import matplotlib as mpl
from matplotlib import pyplot as plt
# 查看 Matplotlib 可用绘图风格
print(plt.style.available)

```

打印出的可用风格如下：

```
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

```

使用 `plt.style.use("style")` 可以修改默认的绘图风格，其中 `style` 为 `Matplolib` 中可用的风格：

```
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
# 设置默认绘图风格为 seaborn-darkgrid
plt.style.use("seaborn-darkgrid")  
x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)
plt.plot(x, y)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/a0d234a42163420e82b7fc44ca57a449.png#pic_center" alt="Matplotlib风格">

可以看到，与在中绘制的相同图形相比，其风格具有较大差别。除此之外，`Maplotlib` 中还有一些非常有意思的风格，例如手绘风格：

```
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
# 启用手绘风格
plt.xkcd()
x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)
plt.plot(x, y)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/b8d16a4b529b4fa7bcefd19d6c9bff91.png#pic_center" alt="手绘风格">

可以看到，使用手绘风格的方法十分简单，只需要在绘图前，调用 `plt.xkcd()` 函数即可：

```
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
# 启用手绘风格
plt.xkcd()
data = [[10., 20., 30., 20.],[40., 25., 53., 18.],[6., 22., 52., 19.]]
x = np.arange(4)
plt.bar(x + 0.00, data[0], color = 'b', width = 0.25)
plt.bar(x + 0.25, data[1], color = 'g', width = 0.25)
plt.bar(x + 0.50, data[2], color = 'r', width = 0.25)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/b3e13c7abbd641e4831b38b83c05746a.png#pic_center" alt="手绘风格">

除了 `Matplotlib` 自带的预设风格外，我们也可以通过自定义颜色和样式来构建满足需求的自定义风格。

### 2. 使用自定义颜色

#### 2.1 自定义颜色

`Matplotlib` 中有多种定义颜色的方法，常见的方法包括：
1.   (`Triplets`)：颜色可以描述为一个实数三元组，即颜色的红、蓝、绿分量，其中每个分量在 `[0,1]` 区间内。因此，`(1.0, 0.0, 0.0)` 表示纯红色，而 `(1.0, 0.0, 1.0)` 则表示粉色。 1.  四元组 (`Quadruplets`)：它们前三个元素与三元组定义相同，第四个元素定义透明度值。此值也在 `[0,1]` 区间内。将图形渲染到图片文件中时，使用透明颜色可以使绘制图形与背景进行混合。 <li> 预定义名称：`Matplotlib` 将标准 `HTML` 颜色名称解释为实际颜色。例如，字符串 `red` 即可表示为红色。同时一些某些颜色的具有简洁的别名，如下表所示： 
  <table><tbody>|别名|颜色|显示
|b|blue<td bgcolor="#0000FF"></td>
|g|green<td bgcolor="#008000"></td>
|r|red<td bgcolor="#FF0000"></td>
|c|cyan<td bgcolor="#00FFFF"></td>
|m|magenta<td bgcolor="#FF00FF"></td>
|y|yellow<td bgcolor="#FFFF00"></td>
|k|black<td bgcolor="#000000"></td>
|w|white<td bgcolor="#FFF"></td>
</tbody></table> </li>1.  `HTML` 颜色字符串：`Matplotlib` 可以将 `HTML` 颜色字符串解释为实际颜色。这些字符串被定义为 `#RRGGBB`，其中 `RR`、`GG`和 `BB` 分别是使用十六进制编码的红色、绿色和蓝色分量。 1.  灰度字符串：`Matplotlib` 将浮点值的字符串表示形式解释为灰度，例如 `0.75` 表示中浅灰色。 
#### 2.2 使用自定义颜色绘制

通过设置 `plt.plot()` 函数的参数 `color` (或等效的简写为 `c`)，可以设置曲线的颜色，如下所示：

```
import numpy as np
import matplotlib.pyplot as plt
def pdf(x, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (x - mu) ** 2)
x = np.linspace(-6, 6, 1000)
for i in range(5):
    samples = np.random.standard_normal(50)
    mu, sigma = np.mean(samples), np.std(samples)
    plt.plot(x, pdf(x, mu, sigma), color = str(.15*(i+1)))
plt.plot(x, pdf(x, 0., 1.), color = 'k')
plt.plot(x, pdf(x, 0.2, 1.), color = '#00ff00')
plt.plot(x, pdf(x, 0.4, 1.), color = (0.9,0.9,0.0))
plt.plot(x, pdf(x, 0.4, 1.), color = (0.9,0.9,0.0,0.8))
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527164728318.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="使用自定义颜色绘制曲线图">

#### 2.3 使用自定义颜色绘制散点图

可以以同样的方式像控制曲线图一样控制散点图的颜色，有两种可用的形式：
1. 为所有点使用相同的颜色 ：所有点都将以相同的颜色显示。1. 为每个点定义不同的颜色：为每个点提供不同的颜色。
##### 2.3.1 为所有点使用相同的颜色

利用从二元高斯分布中提取的两组点 `y_1` 和 `y_2`，每一组中点的颜色相同：

```
import numpy as np
import matplotlib.pyplot as plt
y_1 = np.random.standard_normal((150, 2))
y_1 += np.array((-1, -1)) # Center the distrib. at &lt;-1, -1&gt;
y_2 = np.random.standard_normal((150, 2))
y_2 += np.array((1, 1)) # Center the distrib. at &lt;1, 1&gt;
plt.scatter(y_1[:,0], y_1[:,1], color = 'c')
plt.scatter(y_2[:,0], y_2[:,1], color = 'b')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527165743595.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="为所有点使用相同的颜色">

##### 2.3.2 为每个点定义不同的颜色

我们有时会遇到这样的绘图场景，需要为不同类别的点使用不同的颜色进行绘制，以观察不同类别间的差异情况。以为例，其数据集中数据类似如下所示：

```
5.0,3.3,1.4,0.2,Iris-setosa
7.0,3.2,4.7,1.4,Iris-versicolo

```

数据集的每个点都存储在以逗号分隔的列表中。最后一列给出每个点的标签(标签包含三类：`Iris-virginica`、`Iris-versicolor` 和 `Iris-Vertosa`)。在示例中，这些点的颜色将取决于它们的标签，如下所示：

```
import numpy as np
import matplotlib.pyplot as plt
label_set = (
    b'Iris-setosa',
    b'Iris-versicolor',
    b'Iris-virginica',
)
def read_label(label):
    return label_set.index(label)
data = np.loadtxt('iris.data', delimiter = ',', converters = {<!-- --> 4 : read_label })
color_set = ('c', 'y', 'm')
color_list = [color_set[int(label)] for label in data[:,4]]
plt.scatter(data[:,0], data[:,1], color = color_list)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527171030899.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="为每个点定义不同的颜色">

对于三种可能的标签，我们分别指定一种唯一的颜色，颜色在 `color_set` 中定义，标签在 `label_set` 中定义。`label_set` 中的第 `i` 个标签与 `color_set` 中的第 `i` 个颜色相关联。然后我们利用它们把标签列表转换成颜色列表 `color_list`。然后只需调用 `plt.scatter()` 一次即可显示所有点及其颜色。 除了以上方法外，我们也可以通过对三个不同的类别单独调用 `plt.scatter()` 来实现，但这将需要更多的代码。另外需要注意的是：如果两点有可能有相同的坐标，但有不同的标签，显示的颜色将是后绘制点的颜色，我们也可以使用带有透明通道的颜色值，用来显示重叠点。

#### 2.4 为散点图中数据点的边使用自定义颜色

与 `color` 参数控制点的颜色一样，可以使用 `edgecolor` 参数控制数据点的边的颜色，可以为每个点的边设置相同的颜色：

```
import numpy as np
import matplotlib.pyplot as plt
data = np.random.standard_normal((100, 2))
plt.scatter(data[:,0], data[:,1], color = '1.0', edgecolor='r')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/2021052718094576.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="为散点图中数据点的边使用自定义颜色">

除了为每个点的边设置相同的颜色外，也可以像在为每个点定义不同的颜色部分中介绍的一样为每个点的边设置不边的颜色。

#### 2.5 使用自定义颜色绘制条形图

控制绘制条形图使用的颜色与曲线图和散点图的工作原理相同，即通过可选参数 `color`：

```
import numpy as np
import matplotlib.pyplot as plt
w_pop = np.array([5., 30., 45., 22.])
m_pop = np.array( [5., 25., 50., 20.])
x = np.arange(4)
plt.barh(x, w_pop, color='m')
plt.barh(x, -m_pop, color='c')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527181656140.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="使用自定义颜色绘制条形图">

同样，使用 `plt.bar()` 和 `plt.barh()` 函数自定义颜色绘制条形图的工作方式与 `plt.scatter()` 完全相同，只需设置可选参数 `color`，同时也可以参数 `edgecolor` 控制条形边的颜色。`

```
import numpy as np
import matplotlib.pyplot as plt
values = np.random.random_integers(99, size = 50)
color_set = ('c', 'm', 'y', 'b')
color_list = [color_set[(len(color_set) * val) // 100] for val in values]
plt.bar(np.arange(len(values)), values, color = color_list)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527183020691.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="使用自定义颜色控制条形图中条形边的颜色">

#### 2.6 使用自定义颜色绘制饼图

自定义饼图颜色的方法类似于条形图：

```
import numpy as np
import matplotlib.pyplot as plt
color_set = ('c', 'm', 'y', 'b')
values = np.random.rand(6)
plt.pie(values, colors = color_set)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527183818354.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="使用自定义颜色绘制饼图">饼图接受使用 `colors` 参数(注意，此处是 `colors`，而不是在 `plt.plot()` 中使用的 `color` )的颜色列表。但是，如果颜色数少于输入值列表中的元素数，那么 `plt.pie()` 将循环使用颜色列表中的颜色。在示例中，使用包含四种颜色的列表，为了给包含六个值的饼图着色，其中有两个颜色将使用两次。

#### 2.7 使用自定义颜色绘制箱型图

使用以下代码，修改箱型图中线条颜色：

```
import numpy as np
import matplotlib.pyplot as plt
values = np.random.randn(100)
b = plt.boxplot(values)
for name, line_list in b.items():
    for line in line_list:
        line.set_color('m')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527185402682.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="使用自定义颜色绘制箱型图">

#### 2.8 使用色彩映射绘制散点图

如果要在图形中使用多种颜色，逐个定义每种颜色并不是最佳方案，色彩映射可以解决此问题。色彩映射用一个变量对应一个值(颜色)的连续函数定义颜色。`Matplotlib` 提供了几种常见的颜色映射；大多数是连续的颜色渐变。色彩映射在 `matplotib.cm` 模块中定义，提供创建和使用色彩映射的函数，它还提供了预定义的色彩映射选择。 函数 `plt.scatter()` 接受 `color` 参数的值列表，当提供 `cmap` 参数值时，这些值将被解释为色彩映射的索引：

```
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
n = 256
angle = np.linspace(0, 8 * 2 * np.pi, n)
radius = np.linspace(.5, 1., n)
x = radius * np.cos(angle)
y = radius * np.sin(angle)
plt.scatter(x, y, c = angle, cmap = cm.hsv)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527190556296.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="使用色彩映射绘制散点图"> 在 `matplotlib.cm` 模块中提供了大量预定义的色彩映射，其中 `cm.hsv` 包含全光谱的颜色。

#### 2.9 使用色彩映射绘制条形图

`plt.scatter()` 函数内置了对色彩映射的支持，其他一些绘图函数也内置支持色彩映射。但是，有些函数(如 `plt.bar()` )并未内置对色彩映射的支持，在这种情况下，`Matplotlib` 可以从颜色映射显式生成颜色：

```
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.colors as col
values = np.random.random_integers(99, size = 50)
cmap = cm.ScalarMappable(col.Normalize(0, 99), cm.binary)
plt.bar(np.arange(len(values)), values, color = cmap.to_rgba(values))
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527193659613.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="使用色彩映射绘制条形图"> 以上代码首先创建色彩映射 `cmap`，以便将 `[0, 99]` 范围内的值映射到 `matplotlib.cm.binary` 的颜色。然后，函数 `cmap.to_rgba` 将值列表转换为颜色列表。因此，尽管 `plt.bar()` 并未内置色彩映射支持，但依旧可以使用并不复杂的代码实现色彩映射。

#### 2.10 创建自定义配色方案

`Matplotlib` 使用的默认颜色考虑的主要对象是打印文档或出版物。因此，默认情况下，背景为白色，而标签、轴和其他注释则显示为黑色，在某些不同的使用环境中，我们可能需要使用的配色方案；例如，将图形背景设置为黑色，注释设置为白色。 在 `Matplotlib` 中，各种对象(如轴、图形和标签)都可以单独修改，但逐个更改这些对象的颜色配置并非最佳方案。我们可以使用在介绍的方法，通过修改配置集中改变所有对象，以配置其默认颜色或样式：

```
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
mpl.rc('lines', linewidth = 2.)
mpl.rc('axes', facecolor = 'k', edgecolor = 'w')
mpl.rc('xtick', color = 'w')
mpl.rc('ytick', color = 'w')
mpl.rc('text', color = 'w')
mpl.rc('figure', facecolor = 'k', edgecolor ='w')
mpl.rc('axes', prop_cycle = mpl.cycler(color=[(0.1, .5, .75),(0.5, .5, .75)]))
x = np.linspace(0, 7, 1024)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527202917184.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="创建自定义配色方案">

### 3. 使用自定义样式

#### 3.1 控制线条样式和线宽

在实践中，除了颜色，大多数情况下我们还要对图形的线条样式等进行控制，以为线条样式添加多样性。

##### 3.1.1 线条样式

```
import numpy as np
import matplotlib.pyplot as plt
def gaussian(x, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (x - mu) ** 2)
x = np.linspace(-6, 6, 1024)
plt.plot(x, gaussian(x, 0., 1.), color = 'y', linestyle = 'solid')
plt.plot(x, gaussian(x, 0., .5), color = 'c', linestyle = 'dashed')
plt.plot(x, gaussian(x, 0., .25), color = 'm', linestyle = 'dashdot')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210528123136446.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="控制线条样式"> 使用 `plt.plot()` 的 `linestyle` 参数来控制曲线的样式，其他可用线条样式包括：`solid`、`dashed`、`dotted`、`dashdot`。同样，线条样式设置不仅限于 `plt.plot()`，任何由线条构成的图形都可以使用此参数，也可以说 `linestyle` 参数可用于所有涉及线条渲染的命令。例如，可以修改条形图的线条样式：

```
import numpy as np
import matplotlib.pyplot as plt
n = 10
a = np.random.random(n)
b = np.random.random(n)
x = np.arange(n)
plt.bar(x, a, color='c')
plt.bar(x, a+b, bottom=a, color='w', edgecolor='black', linestyle = 'dashed')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210528130347762.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="修改条形图的线条样式">由于在条形图、饼图等图形中，默认的边线的颜色为白色，因此若要在白色背景上显示这些边线，需要通过 `edgecolor` 参数改变边线的默认颜色。

##### 3.1.2 线宽

使用 `linewidth` 参数可以修改线条的粗细。默认情况下，`linewidth` 设置为1个单位。利用线条的粗细可以在视觉上强调某条特定的曲线。

```
import numpy as np
import matplotlib.pyplot as plt
def gaussian(x, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (x - mu) ** 2)
x = np.linspace(-6, 6, 1024)
for i in range(64):
    samples = np.random.standard_normal(50)
    mu, sigma = np.mean(samples), np.std(samples)
    plt.plot(x, gaussian(x, mu, sigma), color = '.75', linewidth = .5)
plt.plot(x, gaussian(x, 0., 1.), color = 'c', linewidth = 3.)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210528131815806.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="控制线宽">

#### 3.2 控制填充样式

`Matplotlib` 提供了填充图案用于填充平面。这些填充图案，对于仅包含黑白两色的图形中具有重要作用。

```
import numpy as np
import matplotlib.pyplot as plt
n = 10
a = np.random.random(n)
b = np.random.random(n)
x = np.arange(n)
plt.bar(x, a, color='w', hatch='x', edgecolor='black')
plt.bar(x, a+b, bottom=a, color='w', edgecolor='black', hatch='/')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/202105281330473.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="控制填充样式">

具有填充呈现性的函数(如 `plt.bar()` )都可以使用可选参数 `hatch` 控制填充样式，此参数的可选值包括：`/`， `\`， `|`， `-`， `+`， `x`， `o`， `O`，`.` 和 `*`，每个值对应于不同的填充图案；`edgecolor` 参数可用于控制填充图案的颜色。

#### 3.3 控制标记

##### 3.3.1 控制标记样式

在中，我们已经了解了如何绘制曲线，并明白了曲线是由点之间的连线构成的；此外，散点图表示数据集中的每个点。而 `Matplotlib` 提供了多种形状，可以用其他类型的标记替换点的样式。 标记的指定方式包括以下几种：
<li> <pre><code>预定义标记：预定义的形状，表示为 `[0, 8]` 范围内的整数或某些预定义的字符串。
</code></pre> </li><li> <pre><code>顶点列表：值对列表，用作形状路径的坐标。
</code></pre> </li><li> <pre><code>正多边形：表示 `N` 边正多边形的三元组 `(N, 0, angle)` ，其中 `angle` 为旋转角度。
</code></pre> </li><li> <pre><code>星形多边形：它表示为三元组 `(N, 1, angle)`，代表 `N` 边正星形，其中 `angle` 为旋转角度。
</code></pre> </li>
```
import numpy as np
import matplotlib.pyplot as plt
a = np.random.standard_normal((100, 2))
a += np.array((-1, -1))
b = np.random.standard_normal((100, 2))
b += np.array((1, 1))
plt.scatter(a[:,0], a[:,1], color = 'm', marker = 'x')
plt.scatter(b[:,0], b[:,1], color = 'c', marker = '^')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210528142413717.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="控制标记样式">

可以看到，使用 `marker` 参数，可以为每个数据集合指定不同的标记。 我们已经学习了如何在散点图中为每个点定义不同的颜色，如果我们需要为每个点定义不同样式该怎么办呢？问题在于，与 `color` 参数不同，`marker` 参数不接受标记样式列表作为输入。因此，我们不能实现 `plt.scatter()` 的单次调来显示具有不同标记的多个点集。解决方案是，将每种类型的数据点分隔置不同集合中，并为每个集合单独调用 `plt.scatter()` 调用：

```
import numpy as np
import matplotlib.pyplot as plt
label_list = (
    b'Iris-setosa',
    b'Iris-versicolor',
    b'Iris-virginica',
)
colors = ['c','y','m']
def read_label(label):
    return label_list.index(label)
data = np.loadtxt('iris.data', delimiter = ',', converters = {<!-- --> 4 : read_label })
marker_set = ('^', 'x', '.')
for i, marker in enumerate(marker_set):
    data_subset = np.asarray([x for x in data if x[4] == i])
    plt.scatter(data_subset[:,0], data_subset[:,1], color = colors[i], marker = marker)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210528144446486.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="控制标记样式">对于 `plt.plot()`，也可以使用相同的标记参数访问标记样式。当数据点密集时，每个点都使用标记进行显示将会导致图片混乱，因此 `Matplotlib` 提供了 `markevery` 参数，允许每隔 `N` 个点显示一个标记：

```
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-6, 6, 1024)
y_1 = np.sinc(x)
y_2 = np.sinc(x) + 1
plt.plot(x, y_1, marker = 'x', color = '.75')
plt.plot(x, y_2, marker = 'o', color = 'k', markevery = 64)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210528151052378.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="控制标记样式">

##### 3.3.1 控制标记大小

标记的大小可选参数 `s` 进行控制：

```
import numpy as np
import matplotlib.pyplot as plt
a = np.random.standard_normal((100, 2))
a += np.array((-1, -1))
b = np.random.standard_normal((100, 2))
b += np.array((1, 1))
plt.scatter(a[:,0], a[:,1], c = 'm', s = 100.)
plt.scatter(b[:,0], b[:,1], c = 'c', s = 25.)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210528153242593.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="控制标记大小">标记的大小由 `plt.scatter()` 的参数 `s` 设置，但应注意它设置的是标记的表面积倍率而非半径。`plt.scatter()` 函数还可以接受列表作为 `s` 参数的输入，其表示每个点对应的大小：

```
import numpy as np
import matplotlib.pyplot as plt
m = np.random.standard_normal((1000, 2))
r_list = np.sum(m ** 2, axis = 1)
plt.scatter(m[:, 0], m[:, 1], c = 'w', edgecolor='c', marker = 'o', s = 32. * r_list)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210528154243915.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="控制标记大小">`plt.plot()` 函数允许在 `markersize` (或简写为 `ms` )参数的帮助下更改标记的大小，但是此参数不接受列表作为输入。

##### 3.3.3 创建自定义标记

虽然 `Matplotlib` 提供了多种标记形状。但是在某些情况下我们可能仍然找不到适合具体需求的形状。例如，我们可能希望使用公司徽标等作为形状。 在 `Matplotlib` 中，将形状描述为一条路径——一系列点的连接。因此，如果要定义我们自己的标记形状，必须提供一系列的点：

```
import numpy as np
import matplotlib.path as mpath
from matplotlib import pyplot as plt
shape_description = [
    ( 1., 2., mpath.Path.MOVETO),
    ( 1., 1., mpath.Path.LINETO),
    ( 2., 1., mpath.Path.LINETO),
    ( 2., -1., mpath.Path.LINETO),
    ( 1., -1., mpath.Path.LINETO),
    ( 1., -2., mpath.Path.LINETO),
    (-1., -2., mpath.Path.LINETO),
    (-1., -1., mpath.Path.LINETO),
    (-2., -1., mpath.Path.LINETO),
    (-2., 1., mpath.Path.LINETO),
    (-1., 1., mpath.Path.LINETO),
    (-1., 2., mpath.Path.LINETO),
    ( 0., 0., mpath.Path.CLOSEPOLY),
]
u, v, codes = zip(*shape_description)
my_marker = mpath.Path(np.asarray((u, v)).T, codes)
data = np.random.rand(8, 8)
plt.scatter(data[:,0], data[:, 1], c = 'm', marker = my_marker, s = 75)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210528155947943.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="创建自定义标识">

通过以上示例，可以看到，所有带有标记的 `plt` 绘图函数都有一个可选参数 `marker`，其参数值可以是预定义的 `Matplotlib` 标记，也可以是自定义的路径实例，路径对象在 `matplotlib.path` 模块中定义。 `Path` 对象的构造函数将坐标列表和指令列表作为输入；每个坐标一条指令，使用一个列表将坐标和指令融合在一起，然后将坐标列表和指令传递给路径构造函数，如下所示：

```
u, v, codes = zip(*shape_description)
my_marker = mpath.Path(np.asarray((u, v)).T, codes)

```

形状是通过光标的移动来描述的：
- `MOVETO`：此指令将光标移动到指定的坐标，并不画线。- `LINETO`：这将在光标当前点和目标点之间绘制直线，并将光标移动至目标点。- `CLOSEPOLY`：此指令仅用于关闭路径，每个形状都以这条指示结束。
理论上，任何形状都是可能的，我们只需要描述它的路径。但在实践中，如果想使用复杂的形状，最好可以提前进行转换工作。

转：https://blog.csdn.net/LOVEmy134611/article/details/124507939
