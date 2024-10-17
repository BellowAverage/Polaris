
--- 
title:  Matplotlib快速入门 
tags: []
categories: [] 

---
### 1. Matplotlib 常用模块

`Matplotlib` 库中主要包含两个重要模块 `pyplob` 和 `pylab`。`pyplot` 是 `Matplotlib` 中的一个重要模块，在后续教程中，我们会经常使用 `pyplot`，该模块允许我们自动、隐式地创建图形及其轴，以实现所需的绘图；使用该模块，可以实现图形的快速绘制，而不需要进行任何图形或轴的实例化。 `pylab` 是 `Matplotlib` 的另一个重要模块，在需要使用矩阵、执行数学运算等函数功能时可以使用该模块，通常情况下不建议使用该模块。

### 2. Matplotlib 常用概念

我们已经知道，`Matplotlib` 是一个功能强大的绘图库，可以用于绘图许多类型的图，包括、直方图、轮廓图、散点图、箱型图等等。在继续使用 `Matplolib` 进行绘图之前，我们首先对 `Matplolib` 中常用的一些基本概念和术语进行介绍，以对 `Matplolib` 有更好的了解。使用 `Matplotlib` 创建的图形包含很多部分，主要有 `Figure`，`Axis`，`Axes`，`Artist`。
- `Figure`：`Figure` 是用于创建不同绘图的画布，`Matplotlib` 图形中的 `Figure` 可以包含一个或多个 `axes/plots`。- `Axis`：`Matplotlib` 图形中的轴 `axis` 用于限制绘制图形的边界，基本上类似于数学中的坐标轴概念；例如，对于 `3` 维绘图，包含 `X` 轴、`Y` 轴和 `Z` 轴。- `Axes`：`axes` 通常可以被视为一个绘图 `plot`，图形中可以包含多个 `axes`。- `Artist`：一个 `Matplotlib` 生成图形中的一切都是 `Artist` 对象，也可以说 `Artist` 是所有其它类的父类，大多数 `artist` 都是在 `axes` 上所绑定，包括文本对象、`Line2D` 对象等。
以上概念间的相关关系如下图所示：

<img src="https://img-blog.csdnimg.cn/ad6d47ab0fd84044a95d6398e1a50676.png#pic_center" alt="Matplotlib 常用概念">

### 3. Matplotlib 简单示例

#### 3.1 导入 Matplotlib 库

在代码中使用 `Matplotlib` 库时，通常我们会使用一些约定俗成的别名用于简化代码：

```
import matplotlib as mpl
from matplotlib import pyplot as plt

```

这种导入方法对于以下三种 `Matplotlib` 的使用方式都是通用的。

#### 3.1 编写 Python 脚本绘制图形

接下来，我们编写一个入门示例，首先利用 `Numpy` 创建 `NumPy` 数组，然后使用 `Matplotlib` 将其可视化。 我们首先编写一个名为 `fistplt.py` 的文件，并在其中键入以下代码：

```
# fistplt.py
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(6)
y = x ** 3 + 5 * x - 10
plt.plot(x, y)
plt.show()

```

在以上代码中，`np.arange(start, stop, step)` 函数用于以给定的间隔 `step` 创建间距均匀的数列，起始值 `start` 和间隔 `step` 参数的默认值分别为 `0` 和 `1`，该函数的返回值不包含停止值 `stop`，即返回半开区间 `[start, stop)`。在以上示例中，我们创建了一个以 `0` 开始，以 `5` 结束的数组，即 `[0, 1, 2, 3, 4, 5]`。接下来，我们使用函数 y = x 3 + 5 × x − 10 y=x^3+5\times x-10 y=x3+5×x−10 根据输入 x x x，创建了函数值 y y y，用于绘制 `2D` 图形。 接下来，我们使用函数 `plot()` 将其可视化，`plot(x, y)` 用于绘制一条曲线，其中，曲线点的 `x` 坐标在列表 `x` 中给出，曲线点的 `y` 坐标在列表 `y` 中给出，`plot()` 函数还包含一些其它的可选参数用于控制曲线样式。 最后 `show()` 函数用于显示绘制的图形，`show()` 函数会启动一个事件循环，查找所有当前 `Figure` 对象，并打开一个或多个显示 `Figure` 的交互式窗口。通常 `plt.show()` 函数在一个 `Python` 脚本中只能使用一次，通常位于脚本末尾，应尽量避免在同一脚本中多次使用 `show()` 函数。 因此我们可以总结使用 `Matplotlib` 进行绘图的基本步骤：
- 准备数据，可以使用纯 `Python` 创建，也可以读取外部文件或使用 `Numpy` 等其他库获取所需展示的数据- 使用绘图函数进行绘制，例如本节所用 `plot()` 函数用于绘制曲线图，后续的学习中，我们也将学习其它多种不同绘图函数，包括柱状图 `bar()`，饼图 `pie()` 等等- 将绘图结果进行展示 `show()` 或保存 `savefig('file_name')`，需要注意的是，不能在 `show()` 之后 `savefig()`，这是由于使用 `show()` 函数后，画布会进行刷新，再进行保存时只会保存空白图形
编写代码完成后，在命令行提示符下使用命令：`python firstplt.py` 运行上述脚本，它会打开一个绘图窗口，其中显示的代码中所绘制的图形：

<img src="https://img-blog.csdnimg.cn/72b2586a8b874636b4548fe2e97924d7.png#pic_center" alt="绘图窗口">

如上图所示，可以看到绘图窗口中还包含多个图标，其中：

|项目|Value
|------
|<img src="https://img-blog.csdnimg.cn/20210526200434521.png#pic_left=30x30" alt="“保存”图标">|此按钮用于将所绘制的图形另存为所需格式的图片，包括png，jpg，pdf，svg等常见格式
|<img src="https://img-blog.csdnimg.cn/20210526200620854.png#pic_left=30x30" alt="“调节”图标">|此按钮用于调整图片的尺寸，边距等图片属性
|<img src="https://img-blog.csdnimg.cn/20210526200838407.png#pic_left=30x30" alt="“缩放”图标">|此按钮用于缩放图片，用于观察图形细节，单击此按钮后，在图形上使用鼠标左键拖拽进行放大，使用鼠标右键拖拽进行缩小
|<img src="https://img-blog.csdnimg.cn/20210526201008106.png#pic_left=30x30" alt="“移动”图标">|此按钮用于移动图形，可以与“缩放”按钮结合观察放大后图片的具体细节，同时，单击此按钮后，在图形上使用鼠标右键拖拽可以缩放坐标轴的比例
|<img src="https://img-blog.csdnimg.cn/20210526201100299.png#pic_left=30x30" alt="“还原”图标">|此按钮用于将图形恢复到其初始状态，取消缩放、移动等操作

`NOTE：`在之后的教程中，我们主要使用这种方式进行讲解，但是相关的绘图方法与接下来要讲的两种 `Matplotlib` 使用方式完全相同。

#### 3.2 在 Jupyter Notebook 中使用Matplotlib

`Jupyter Notebook` 是一个基于浏览器的交互式数据分析工具，用于将相关描述、代码、图形、HTML元素以及多种内容组合到一个可执行文档中。如果要 `Jupyter Notebook` 中以交互方式展示绘图结果，使用 `%matplotlib` 命令，除此之外，在 `Jupyter Notebook` 中，还可以选择将图形直接嵌入 Notbook 中：

```
%matplotlib inline

```

命令 `%matplotlib inline` 会将绘图结果静态的嵌入到 `Jupyter Notebook` 中，而使用命令 `%matplotlib` 后 `Matplotlib` 绘制仍将打开一个交互式绘图窗口来绘制图形。 然后导入 Matplotlib 的方法与在脚本中完全一致：

```
import matplotlib as mpl
from matplotlib import pyplot as plt

```

在下图中，可以看到使用 `%matplotlib` 命令时，仍会打开一个交互式绘图窗口来进行绘制。

<img src="https://img-blog.csdnimg.cn/02129711e6cd4580bd280fe140d234df.png#pic_center" alt="交互式绘图"> 而在下图中，可以看到使用 `%matplotlib inline` 命令则会将绘图结果直接静态的嵌入到 `Jupyter Notebook` 中。

<img src="https://img-blog.csdnimg.cn/f6c487d9cd48472a951e43ce11adc5d5.png#pic_center" alt="静态绘图">

#### 3.3 在 IPython Shell 中使用 Matplotlib

如果要在 `IPython Shell` 中使用 `Matplotlib` 模式，需要在启动 `ipython` 后使用 `%matplotlib` 魔法命令：

```
%matplotlib

```

运行以上命令时，它将给出 Matplotlib 所使用的后端：

```
Using matplotlib backend: Qt5Agg

```

在执行上述魔法命令后，通过导入 `Matplotlib` 库就可以使用 `Matplotlib` 库，这与其它方式使用 `Matploblib` 时的导入方式完全相同：

```
import matplotlib as mpl
from matplotlib import pyplot as plt

```

接下里，使用任何绘图函数命令都将打开一个交互式绘图窗口来绘制图形。

```
In [1]: %matplotlib
Using matplotlib backend: Qt5Agg

In [2]: import matplotlib as mpl
   ...: from matplotlib import pyplot as plt
   ...: import numpy as np

In [3]: x = np.arange(6)
   ...: y = x ** 3 + 5 * x - 10
   ...: plt.plot(x,y)
Out[3]: [&lt;matplotlib.lines.Line2D at 0x7f1a0e4b2550&gt;]

```

转：https://blog.csdn.net/LOVEmy134611/article/details/124507911
