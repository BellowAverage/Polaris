
--- 
title:  Matplotlib安装与配置 
tags: []
categories: [] 

---
### 1. Matplotlib 简介

`Matplotlib` 是 `Python` 生态系统的一个重要组成部分，是用于可视化的绘图库，它提供了一整套和 `matlab` 相似的命令 `API` 和可视化界面，可以生成出版质量级别的精美图形，`Matplotlib` 使绘图变得非常简单，在易用性和性能间取得了优异的平衡。

### 2. Matplotlib 安装

`Matplotlib` 的依赖包和 `Matplotlib` 本身在标准 `Python` 包存储库中均有以 `wheel` 文件的形式提供。因此，可以使用 `pip` 软件包管理工具轻松地将 `Matplotlib` 安装在 `MacOS`、`Windows`、`Linux` 等系统上。和许多第三方库的安装方法一样，安装 `Matplotlib` 只需命令行中，执行以下命令：

```
pip install -U matplotlib

```

需要注意的是：要安装 `Matplotlib` 库，计算机中必须已经安装 `Python`。如果使用的是 `Jupyter Notebook`，由于 `Jupyter Notebook` 附带了许多依赖库，如 `Numpy`、`Pandas`、`Matplotlib`、`Scikit Learn`等，则不必单独安装这些库。 安装完成后可以使用如下命令检查，确认安装成功：

```
pip list

```

<img src="https://img-blog.csdnimg.cn/ae02f30f7e40429581c5992150172810.png#pic_center" alt="验证Matplotlib的安装">

### 3. Matplotlib 配置

安装成功后，即可以在 `Python` 中像使用其它库一样导入和使用 `Matplotlib`，而无需更多文件的配置，通常我们将其导入后使用别名 `mpl`：

```
import matplotlib as mpl

```

`Matplotlib` 的配置更多的用于修改绘制图形的默认样式，`Matplotlib` 的配置文件中包含了各种默认的图形配置信息，我们可以通过修改这些配置信息修改全局参数进行自定义所绘制图形的样式，这些参数可以改变图形尺寸、配色方案、字体等一系列信息。 可以使用多种方式完成 `Matplotlib` 的绘图配置，本文主要介绍以下三种配置方式通过`配置文件`进行配置、通过 `rcParams['param_name']` 动态配置和通过 `matplotlib.rc()` 函数配置。

#### 3.1 通过配置文件进行配置

配置文件同样可以分为几个不同的级别，如果我们希望修改所有的图形使用的默认配置，则需要修改全局默认配置；而如果我们需要根据不同任务使用不同的配置，或者不同用户使用不同的配置，则需要修改局部配置文件，以能够在不同的用户和任务中使用不同图形配置。根据配置文件的作用范围，可以分为三个级别：全局配置文件、用户级配置文件和当前任务配置文件。 不同系统三个级别的文件位于不同目录，可以通过使用以下代码，查看配置文件的路径：

```
import matplotlib as mpl
import os

# 全局配置目录
print(mpl.__path__)
# 当前用户配置目录
print(mpl.get_configdir())
# 当前任务配置目录，即当前代码运行目录
print(os.getcwd())

```
- 全局配置文件 `mpl-data\matplotlibrc`，位于 `Matplotlib` 的安装目录直线，例如在 `Window` 下将其安装在 `D:\Program Files\Python39\lib\site-packages\matplotlib` 目录下，则全局配置文件的完整文件名为 `D:\Program Files\Python39\lib\site-packages\matplotlib\mpl-data\matplotlibrc`，默认情况下，图形使用此配置文件进行绘制。- 用户级配置文件 `.matplotlib\matplotlibrc`，位于用户目录之下，例如，用户目录为 `C:\Users\Brainiac\`，则相应配置文件为 `C:\Users\Brainiac\.matplotlib\matplotlibc`；如果不存在此文件，也可以根据全局配置文件与用户需求自定创建和修改。- 当前任务配置文件 `matplotlibrc`，即位于代码运行目录之下，可以用于为当前任务的代码定制 `Matplotlib` 配置，默认情况下不存在此文件，即默认使用全局或当前用户配置文件，我们可以根据需要创建此文件，并根据需要进行配置。
介绍了配置文件的位置后，我们通过查看全局配置文件，观察在配置文件中可以进行配置的相关图形属性，以下为一个全局配置文件示例：

<img src="https://img-blog.csdnimg.cn/5425760f1b2b490495d3e611a03ef1ce.png#pic_center" alt="matploblib配置文件">

`NOTE：`可以看到并不推荐直接修改全局配置文件，可以通过将此文件复制到用户及配置文件目录或当前任务配置文件目录中，并根据需要进行修改。配置文件的格式一般为 `属性名: 属性值`，如下配置线宽为 `1.5`：

```
lines.linewidth: 1.5

```

#### 3.2 通过 rcParams[‘param_name’] 配置

而如果我们仅仅想在当前文件中简单修改自定义配置，则可以通过 `rcParams['param_name']` 更快速的修改。通过使用以下代码，可以查看能够自定义配置的属性有哪些：

```
import matplotlib as mpl
# 可以使用以下三种方式
print(mpl.rc_params())
print(mpl.rcParamsDefault)
print(mpl.rcParams) 

```

得到的输出结果与配置文件中类似，格式同样为 `属性名: 属性值`：

```
...
font.size: 10.0
font.stretch: normal
font.style: normal
font.variant: normal
font.weight: normal
...

```

使用 `rcParams['param_name']` 方式修改配置的方式如下，其中 `param_name` 表示属性名：

```
import matplotlib as mpl

# 修改线条宽度为2
mpl.rcParams['lines.linewidth'] = 2
# 修改线条颜色为红色
mpl.rcParams['lines.color'] = 'r'

```

在实际应用中，最常用的两种配置包括中文和中文负号的显示，如果不进行配置，默认不支持显示中文与中文负号：

<img src="https://img-blog.csdnimg.cn/f6858e2e690e4c7a962ef9a766e59723.png#pic_center" alt="不支持中文"> 使用以下方式进行配置：

```
import matplotlib as mpl

#显示中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
#显示负号
mpl.rcParams['axes.unicode_minus']=False

```

配置后图形就可以正常显示中文和中文符号：

<img src="https://img-blog.csdnimg.cn/3991e0f1cbe345b89583fd21a6e77ce0.png#pic_center" alt="中文支持">

#### 3.3 通过 matplotlib.rc() 函数配置

同样我们也可以使用 `matplotlib.rc()` 函数进行配置，使用方法如下：

```
import matplotlib as mpl
# 修改线宽
mpl.rc('lines', linewidth=2, color='g')

```

其中 `rc` 函数的第一个参数为 `group` 表示属性所属的组，用于限定属性的作用域，例如在以上示例中线宽 `linewidth` 属于线 `lines` 用于限定只在线条中起作用，而对坐标轴等线宽 `linewidth` 不起作用，如果想要修改包括坐标轴在内的图形线宽 `linewidth` 则需要使用：

```
import matplotlib as mpl
# 修改整个图形线宽
mpl.rc('axes', linewidth=2)

```

### 相关链接

转https://blog.csdn.net/LOVEmy134611/article/details/124494810
