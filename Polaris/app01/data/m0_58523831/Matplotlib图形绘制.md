
--- 
title:  Matplotlib图形绘制 
tags: []
categories: [] 

---
### 1. 2D 图形绘制

#### 1.2 

在中，作为入门示例，我们已经了解了曲线图的绘制方法，为了完整起见，本节中我们首先简单回顾下，如何在使用 `Matplotlib` 绘制曲线图，同时介绍多曲线图等更复杂曲线图的绘制。

##### 1.2.1 简单曲线图的绘制

在以下示例中，我们绘制曲线 c o s ( x ) cos(x) cos(x)， x x x 在 [ 0 , 2 π ] [0, 2\pi] [0,2π] 区间内：

```
# cos_1.py
import math
import matplotlib.pyplot as plt
scale = range(100)
x = [(2 * math.pi * i) / len(scale) for i in scale]
y = [math.cos(i) for i in x]
plt.plot(x, y)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210526205845895.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="sin(x)"> 我们已经知道，`Matplotlib` 使用的数据可以有不同来源，接下来，我们以使用 `Numpy` 获取的数据为例，绘制 `[-10,10]` 区间内的曲线 y = x 3 + 5 x − 10 y=x^3+5x-10 y=x3+5x−10：

```
# plot_np.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 800)
y = x ** 3 + 5 * x - 10
plt.plot(x, y)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210526211027721.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="y=x^3+5x-10">

##### 1.2.2 绘制多曲线图

很多时候我们需要对比多组数据，以发现数据间的异同，此时就需要在一张图片上绘制多条曲线——多曲线图，下图展示了在同一图片中绘制函数 y = x y=x y=x、 y = x 2 y=x^2 y=x2， y = l o g e x y=log_ex y=loge​x 以及 y = s i n ( x ) y=sin(x) y=sin(x)：

```
# plot_multi_curve.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.1, 2 * np.pi, 100)
y_1 = x
y_2 = np.square(x)
y_3 = np.log(x)
y_4 = np.sin(x)
plt.plot(x,y_1)
plt.plot(x,y_2)
plt.plot(x,y_3)
plt.plot(x,y_4)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210526212345453.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="多曲线图"> `Note：`一条曲线的绘制需要调用一次 `plt.plot()`，而 `plt.show()` 只需调用一次。这种延迟呈现机制是 `Matplotlib` 的关键特性，我们可以在代码中的任何地方调用绘图函数，但只有在调用 `plt.show()` 时才会渲染显示图形。为了更好的说明这种延迟呈现机制，我们编写以下代码：

```
# deferred_rendering.py
import numpy as np
import matplotlib.pyplot as plt
def plot_func(x, y):
    x_s = x[1:] - y[:-1]
    y_s = y[1:] - x[:-1]
    plt.plot(x[1:], x_s / y_s)
x = np.linspace(-5, 5, 200)
y = np.exp(-x ** 2)
plt.plot(x, y)
plot_func(x, y)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210526214345286.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="延迟呈现示例">

可以看到，尽管其中一个 `plt.plot()` 是在 `plot_func` 函数中调用的，它对图形的呈现没有任何影响，因为 `plt.plot()` 只是声明了我们要呈现的内容，但还没有执行渲染。因此可以使用延迟呈现特性结合 `for` 循环、条件判断等语法完成复杂图形的绘制，同时也可以在同一张图中组合不同类型的统计图。

##### 1.2.3 读取数据文件绘制曲线图

很多情况下数据都是存储于文件中，因此，需要首先读取文件中的数据，再进行绘制，说明起见，以 `.txt` 文件为例，其他诸如 `Excel`、`CSV文件` 等同样可以进行读取，并用于可视化绘制。假设存在 `data.txt` 文件如下：

```
0 1
1 2
2 5
4 17
5 26
6 37

```

读取数据和绘制的代码如下：

```
# read_txt.py
import matplotlib.pyplot as plt
x, y = [], []
for line in open('data.txt', 'r'):
    values = [float(s) for s in line.split()]
    x.append(values[0])
    y.append(values[1])
plt.plot(x, y)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527102858792.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="绘制图形">

#### 1.2 

当绘制曲线图时，我们假设点与点之间存在序列关系。而散点图是简单地绘制点，它们之间并不存在连接。散点图来为两个序列中的每个相对应的数据对在坐标轴中对应的位置画一个点。

```
import numpy as np
import matplotlib.pyplot as plt
data = np.random.rand(1000, 2)
plt.scatter(data[:,0], data[:,1])
plt.show()

```

<img src="https://img-blog.csdnimg.cn/2021052710422742.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="散点图">

可以看到，函数 `plt.scatter()` 的调用方式与 `plt.plot()`完全相同，分别将点的 x 和 y 坐标序列作为输入参数。

#### 1.3 

条形图具有丰富的表现形式，常见的类型包括单组条形图，多组条形图，堆积条形图和对称条形图等。

##### 1.3.1 单组条形图

条形图的每种表现形式都可以绘制成垂直条形图或水平条形图，以单组条形图的两种绘制方式为例。

**(1) 垂直条形图**

```
import matplotlib.pyplot as plt
data = [10., 20., 5., 15.]
plt.bar(range(len(data)), data)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527105336249.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="垂直条形图">

`plt.bar()` 函数的作用是：接收两个参数，包括每个条形的 `x` 坐标和每个条形的高度。通过使用可选参数 `width`，`plt.bar()` 还可以控制条形图中条形的宽度：

```
import matplotlib.pyplot as plt
data = [10., 20., 5., 15.]
plt.bar(range(len(data)), data, width=0.5)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527110225118.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="修改条形图宽度"> **(2) 水平条形图**

如果更喜欢水平条形外观，就可以使用 `plt.barh()` 函数，在用法方面与 `plt.bar()` 基本相同，但是修改条形宽度(或者在水平条形图中应该称为高度)，需要使用参数 `height`：

```
import matplotlib.pyplot as plt
data = [10., 20., 5., 15.]
plt.barh(range(len(data)), data, height=0.5)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527111628808.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="水平条形图">

##### 1.3.2 多组条形图

当需要比较不同年份相应季度的销量等此类需求时，我们可能需要多组条形图。

```
import numpy as np
import matplotlib.pyplot as plt
data = [[10., 20., 30., 20.],[40., 25., 53., 18.],[6., 22., 52., 19.]]
x = np.arange(4)
plt.bar(x + 0.00, data[0], color = 'b', width = 0.25)
plt.bar(x + 0.25, data[1], color = 'g', width = 0.25)
plt.bar(x + 0.50, data[2], color = 'r', width = 0.25)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527112604612.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="多组条形图">

##### 1.3.3 堆积条形图

通过使用 `plt.bar()` 函数中的可选参数，可以绘制堆积条形图，`plt.bar()` 函数的可选参数 `bottom` 允许指定条形图的起始值。

```
import matplotlib.pyplot as plt
y_1 = [3., 25., 45., 22.]
y_2 = [6., 25., 50., 25.]
x = range(4)
plt.bar(x, y_1, color = 'b')
plt.bar(x, y_2, color = 'r', bottom = y_1)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527113350947.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="堆积条形图">

可以结合 `for` 循环，利用延迟呈现机制可以堆叠更多的条形：

```
import numpy as np
import matplotlib.pyplot as plt
data = np.array([[5., 30., 45., 22.], [5., 25., 50., 20.], [1., 2., 1., 1.]])
x = np.arange(data.shape[1])
for i in range(data.shape[0]):
    plt.bar(x, data[i], bottom = np.sum(data[:i], axis = 0))
plt.show() 

```

<img src="https://img-blog.csdnimg.cn/20210527114739374.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="堆叠条形图">

##### 1.3.4 对称条形图

例如，当我们想要绘制不同年龄段的男性与女性数量的对比时，一个简单且有用的技巧是对称绘制两个条形图：

```
import numpy as np
import matplotlib.pyplot as plt
w_pop = np.array([5., 30., 45., 22.])
m_pop = np.array( [5., 25., 50., 20.])
x = np.arange(4)
plt.barh(x, w_pop)
plt.barh(x, -m_pop)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527115428208.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="对称条形图">

图中女性人口的条形图照常绘制。然而，男性人口的条形图的条形图的条形图向左延伸，而不是向右延伸。可以使用数据的负值来快速实现对称条形图的绘制。

#### 1.4 饼图

饼图可以用于对比数量间的相对关系，`plt.pie()` 函数将一系列值作为输入，将值传递给 `Matplolib`，它就会自动计算各个值在饼图中的相对面积，并进行绘制：

```
import matplotlib.pyplot as plt
data = [10, 15, 30, 20]
plt.pie(data)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527120232309.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="饼图">

#### 1.5 直方图

直方图是概率分布的图形表示。事实上，直方图只是一种特殊的条形图。我们可以很容易地使用 `Matplotlib` 的条形图函数，并进行一些统计运算来生成直方图。但是，鉴于直方图的使用频率非常高，因此 `Matplotlib` 提供了一个更加方便的函数——`plt.hist()`。 `plt.hist()` 函数的作用是：获取一系列值作为输入。值的范围将被划分为大小相等的范围(默认情况下数量为 `10`)，然后生成条形图，一个范围对应一个条柱，一个条柱的高度是相应范围内中的值的数量，条柱的数量由可选参数 `bins`确定。

```
import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(1024)
plt.hist(x, bins = 20)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527121241999.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="直方图">

#### 1.6 箱形图

箱形图可以通过方便地显示一组值的中位数、四分位数、最大值和最小值来比较值的分布。

```
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(200)
plt.boxplot(data)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527124224116.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="箱型图">`Tips：plt.boxplot()函数的作用是：获取一组值，并自动计算平均值、中位数和其他统计量。` 箱形图描述：
1. 图中黄线是分布的中位数。1. 方形箱框包括从下四分位数Q1到上四分位数Q3的50%的数据。1. 下盒须的下四分位延伸到1.5 (Q3-Q1)。1. 上盒须从上四分位延伸至1.5 (Q3-Q1)。1. 离盒须较远的数值用圆圈标记。
要在单个图形中绘制多个箱形图，对每个箱形图调用一次`plt.boxplot()`是不可行。它会将所有箱形图画在一起，形成一个混乱的、不可读的图形。如果想要到达符合要求的效果，只需在一次调用`plt.boxplot()`中，同时绘制多个箱形图即可，如下所示：

```
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(200, 6)
plt.boxplot(data)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210527131240902.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA55u85bCP6L6J5Li2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="多箱形图">

### 2. 3D 图形绘制

绘制 `3D` 图形的函数使用方式与 `2D` 非常相似，在上节中，我们已经学习了一系列 `2D` 图形的绘制，接下里，我们在图中再添加一个维度以展示更多信息。

#### 2.1 3D 散点图

`3D` 散点图的绘制方式与 `2D` 散点图基本相同。

```
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# Dataset generation
a, b, c = 10., 28., 8. / 3.
def lorenz_map(x, dt = 1e-2):
    x_dt = np.array([a * (x[1] - x[0]), x[0] * (b - x[2]) - x[1], x[0] * x[1] - c * x[2]])
    return x + dt * x_dt
points = np.zeros((2000, 3))
x = np.array([.1, .0, .0])
for i in range(points.shape[0]):
    points[i], x = x, lorenz_map(x)
# Plotting
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Lorenz Attractor a=%0.2f b=%0.2f c=%0.2f' % (a, b, c))
ax.scatter(points[:, 0], points[:, 1],points[:, 2], zdir = 'z', c = 'c')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210621205434852.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="3D散点图">

需要注意的是，在弹出的交互式绘图窗口中，按住鼠标左键移动鼠标可以旋转查看三维图形。 接下来，我们详细讲解如何使用 `Matplotlib` 进行三维绘图，我们首先需要导入 `Matplotlib` 的三维扩展 `Axes3D`：

```
from mpl_toolkits.mplot3d import Axes3D

```

对于三维绘图，需要创建一个 `Figure` 实例并附加一个 `Axes3D` 实例：

```
fig = plt.figure()
ax = fig.gca(projection='3d')

```

之后，三维散点图的绘制方式与二维散点图完全相同：

```
ax.scatter(points[:, 0], points[:, 1],points[:, 2], zdir = 'z', c = 'c')

```

需要注意的是，绘制 `3D` 散点图需要调用 `Axes3D` 实例的 `scatter()` 方法，而非 `plt` 中的 `scatter` 方法。只有 `Axes3D` 中的 `scatter()` 方法才能解释三维数据。同时 `2D` 统计图中的注释也可以在 `3D` 图中使用，例如 `set_title()`、`set_xlabel()`、`set_ylabel()` 和 `set_zlabel()` 等。

#### 2.2 3D曲线图

与在 `3D` 空间中绘制散点图类似，绘制 `3D` 曲线图同样需要设置一个 `Axes3D` 实例，然后调用其 `plot()` 方法：

```
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# Dataset generation
a, b, c = 10., 28., 8. / 3.
def lorenz_map(x, dt = 1e-2):
    x_dt = np.array([a * (x[1] - x[0]), x[0] * (b - x[2]) - x[1], x[0] * x[1] - c * x[2]])
    return x + dt * x_dt
points = np.zeros((8000, 3))
x = np.array([.1, .0, .0])
for i in range(points.shape[0]):
    points[i], x = x, lorenz_map(x)
# Plotting
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Lorenz Attractor a=%0.2f b=%0.2f c=%0.2f' % (a, b, c))
ax.plot(points[:, 0], points[:, 1], points[:, 2], c = 'c')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210621210636217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="3D曲线图">

#### 2.3 3D标量场

到目前为止，我们看到的 `3D` 绘图方式类似与相应的 `2D` 绘图方式，但也有许多特有的三维绘图功能，例如将二维标量场绘制为 `3D` 曲面，`plot_surface()` 方法使用 x x x、 y y y 和 z z z 三个序列将标量场显示为三维曲面：

```
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
x_grid, y_grid = np.meshgrid(x, y)
z = np.sinc(np.sqrt(x_grid ** 2 + y_grid ** 2))
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot_surface(x_grid, y_grid, z, cmap=cm.viridis)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210621213108450.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="3D标量场"> 可以看到曲面上线条带有显著的色彩标识，如果不希望看到三维曲面上显示的曲线色彩，可以使用 `plot_surface()` 的附加可选参数：

```
ax.plot_surface(x_grid, y_grid, z, cmap=cm.viridis, linewidth=0, antialiased=False)

```

<img src="https://img-blog.csdnimg.cn/20210621213554604.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="3D标量场">同样，我们也可以仅保持曲线色彩，而曲面不使用其他颜色，这也可以通过 `plot_surface()` 的可选参数来完成：

```
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
x_grid, y_grid = np.meshgrid(x, y)
z = np.sinc(np.sqrt(x_grid ** 2 + y_grid ** 2))
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot_surface(x_grid, y_grid, z, edgecolor='b',color='w')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210621214703881.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="3D标量场"> 而如果我们希望消除曲面，而仅使用线框进行绘制，可以使用 `plot_wireframe()` 函数，`plot_wireframe()` 参数与 `plot_surface()` 相同，使用两个可选参数 `rstride` 和 `cstride` 用于令 `Matplotlib` 跳过 x x x 和 y y y 轴上指定数量的坐标，用于减少曲线的密度：

```
ax.plot_wireframe(x_grid, y_grid, z, cstride=10, rstride=10,color='c')

```

<img src="https://img-blog.csdnimg.cn/2021062121555171.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="3D标量场">

#### 2.4 绘制3D曲面

在前述方法中，使用 `plot_surface()` 来绘制标量：即 `f(x, y)=z` 形式的函数，但 `Matplotlib` 也能够使用更通用的方式绘制三维曲面：

```
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# Generate torus mesh
angle = np.linspace(0, 2 * np.pi, 32)
theta, phi = np.meshgrid(angle, angle)
r, r_w = .25, 1.
x = (r_w + r * np.cos(phi)) * np.cos(theta)
y = (r_w + r * np.cos(phi)) * np.sin(theta)
z = r * np.sin(phi)
# Display the mesh
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.plot_surface(x, y, z, color = 'c', edgecolor='m', rstride = 2, cstride = 2)
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210621221551421.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="绘制3D曲面"> 同样可以使用 `plot_wireframe()` 替换对 `plot_surface()` 的调用，以便获得圆环的线框视图：

```
ax.plot_wireframe(x, y, z, edgecolor='c', rstride = 2, cstride = 1)

```

<img src="https://img-blog.csdnimg.cn/20210621222403744.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="绘制3D曲面">

#### 2.5 在3D坐标轴中绘制2D图形

注释三维图形的一种有效方法是使用二维图形：

```
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
x_grid, y_grid = np.meshgrid(x, y)
z = np.exp(-(x_grid ** 2 + y_grid ** 2))
u = np.exp(-(x ** 2))
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_zlim3d(0, 3)
ax.plot(x, u, zs=3, zdir='y', lw = 2, color = 'm')
ax.plot(x, u, zs=-3, zdir='x', lw = 2., color = 'c')
ax.plot_surface(x_grid, y_grid, z, color = 'b')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210621223026597.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="注释三维图形">`Axes3D` 实例同样支持常用的二维渲染命令，如 `plot()`：

```
ax.plot(x, u, zs=3, zdir='y', lw = 2, color = 'm')

```

Axes3D 实例对 `plot()` 的调用有两个新的可选参数： `zdir` ：用于决定在哪个平面上绘制2D绘图，可选值包括 `x`、`y` 或 `z`； `zs` ：用于决定平面的偏移。 因此，要将二维图形嵌入到三维图形中，只需将二维原语用于 `Axes3D` 实例，同时使用可选参数，`zdir` 和 `zs`，来放置所需渲染图形平面。 接下来，让我们实际查看下在 `3D` 空间中堆叠 `2D` 条形图的示例：

```
import numpy as np
from matplotlib import cm
import matplotlib.colors as col
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# Data generation
alpha = 1. / np.linspace(1, 8, 5)
t = np.linspace(0, 5, 16)
t_grid, a_grid = np.meshgrid(t, alpha)
data = np.exp(-t_grid * a_grid)
# Plotting
fig = plt.figure()
ax = fig.gca(projection = '3d')
cmap = cm.ScalarMappable(col.Normalize(0, len(alpha)), cm.viridis)
for i, row in enumerate(data):
    ax.bar(4 * t, row, zs=i, zdir='y', alpha=0.8, color=cmap.to_rgba(i))
plt.show()

```

<img src="https://img-blog.csdnimg.cn/20210622103321342.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="堆叠2D图形">

#### 2.6 3D 柱状图

最后，我们来介绍 `3D` 柱状图的绘制。

```
import numpy as np
from matplotlib import cm
import matplotlib.colors as col
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# Data generation
alpha = np.linspace(1, 8, 5)
t = np.linspace(0, 5, 16)
t_grid, a_grid = np.meshgrid(t, alpha)
data = np.exp(-t_grid * (1. / a_grid))
# Plotting
fig = plt.figure()
ax = fig.gca(projection = '3d')
xi = t_grid.flatten()
yi = a_grid.flatten()
zi = np.zeros(data.size)
dx = .30 * np.ones(data.size)
dy = .30 * np.ones(data.size)
dz = data.flatten()
ax.set_xlabel('T')
ax.set_ylabel('Alpha')
ax.bar3d(xi, yi, zi, dx, dy, dz, color = 'c')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/2021062211064652.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xPVkVteTEzNDYxMQ==,size_16,color_FFFFFF,t_70#pic_center" alt="3D柱形图">

`3D` 柱体以网格布局定位，`bar3d()` 方法接受六个必需参数作为输入。前三个参数是每个柱体下端的 `x`、`y` 和 `z` 坐标：

```
xi = t_grid.flatten()
yi = a_grid.flatten()
zi = np.zeros(data.size)

```

`bar3d()` 方法将坐标列表作为输入，而不是网格坐标，因此需要对矩阵 `a_grid` 和 `t_grid` 调用flatten方法。`bar3d()` 方法的另外三个必需参数是每个柱体在每个维度的值。这里，柱状图的高度取自数据矩阵。柱形宽度和深度设置为 `0.30`：

```
dx = .30 * np.ones(data.size)
dy = .30 * np.ones(data.size)
dz = data.flatten()

```

转：https://blog.csdn.net/LOVEmy134611/article/details/124504526
