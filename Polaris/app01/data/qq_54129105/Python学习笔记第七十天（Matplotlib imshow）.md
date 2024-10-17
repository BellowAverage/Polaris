
--- 
title:  Python学习笔记第七十天（Matplotlib imshow） 
tags: []
categories: [] 

---


#### Python学习笔记第七十天
- - <ul><li>- - - - - 


## Matplotlib imshow

imshow() 函数是 Matplotlib 库中的一个函数，用于显示图像。

imshow() 函数常用于绘制二维的灰度图像或彩色图像。

imshow() 函数可用于绘制矩阵、热力图、地图等。

imshow() 方法语法格式如下：

```
imshow(X, cmap=None, norm=None, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, 
	extent=None, shape=None, filternorm=1, filterrad=4.0, imlim=None, resample=None, url=None, *, data=None, **kwargs)

```

参数说明：
- X：输入数据。可以是二维数组、三维数组、PIL图像对象、matplotlib路径对象等。- cmap：颜色映射。用于控制图像中不同数值所对应的颜色。可以选择内置的颜色映射，如gray、hot、jet等，也可以自定义颜色映射。- norm：用于控制数值的归一化方式。可以选择Normalize、LogNorm等归一化方法。- aspect：控制图像纵横比（aspect ratio）。可以设置为auto或一个数字。- interpolation：插值方法。用于控制图像的平滑程度和细节程度。可以选择- nearest、bilinear、bicubic等插值方法。- alpha：图像透明度。取值范围为0~1。- origin：坐标轴原点的位置。可以设置为upper或lower。- extent：控制显示的数据范围。可以设置为[xmin, xmax, ymin, ymax]。- vmin、vmax：控制颜色映射的值域范围。- filternorm 和 filterrad：用于图像滤波的对象。可以设置为None、- antigrain、freetype等。- imlim： 用于指定图像显示范围。- resample：用于指定图像重采样方式。- url：用于指定图像链接。 以下是一些 imshow() 函数的使用实例。
### 显示灰度图像

```
# 实例 1
import matplotlib.pyplot as plt
import numpy as np

# 生成一个二维随机数组
img = np.random.rand(10, 10)

# 绘制灰度图像
plt.imshow(img, cmap='gray')

# 显示图像
plt.show()

```

以上实例中我们生成了一个 10x10 的随机数组，并使用 imshow() 函数将其显示为一张灰度图像。

我们设置了 cmap 参数为 gray，这意味着将使用灰度颜色映射显示图像。

### 显示彩色图像

```
# 实例 2
import matplotlib.pyplot as plt
import numpy as np

# 生成一个随机的彩色图像
img = np.random.rand(10, 10, 3)

# 绘制彩色图像
plt.imshow(img)

# 显示图像
plt.show()

```

以上实例中我们生成了一个 10x10 的随机彩色图像，并使用 imshow() 函数将其显示出来。

由于彩色图像是三维数组，因此不需要设置 cmap 参数。

### 显示热力图

```
# 实例 3
import matplotlib.pyplot as plt
import numpy as np

# 生成一个二维随机数组
data = np.random.rand(10, 10)

# 绘制热力图
plt.imshow(data, cmap='hot')

# 显示图像
plt.colorbar()
plt.show()

```

以上实例中我们生成了一个 10x10 的随机数组，并使用 imshow() 函数将其显示为热力图。

我们设置了 cmap 参数为 hot，这意味着将使用热度颜色映射显示图像。

此外，我们还添加了一个颜色条（colorbar），以便查看数据的值与颜色之间的关系。

### 显示地图

```
# 实例 4
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 加载地图图像, 下载个地图的jpg图片即可
img = Image.open('map.jpg')

# 转换为数组
data = np.array(img)

# 绘制地图
plt.imshow(data)

# 隐藏坐标轴
plt.axis('off')

# 显示图像
plt.show()

```

以上实例中我们加载了一张地图图像，并将其转换为数组。

然后，我们使用 imshow() 函数将其显示出来，并使用 axis(‘off’) 函数隐藏了坐标轴，以便更好地查看地图。

### 显示矩阵

```
# 实例 5
import matplotlib.pyplot as plt
import numpy as np

# 生成一个随机矩阵
data = np.random.rand(10, 10)

# 绘制矩阵
plt.imshow(data)

# 显示图像
plt.show()

```

以上实例中我们生成了一个随机矩阵，并使用 imshow() 函数将其显示为一张图像。

由于矩阵也是二维数组，因此可以使用 imshow() 函数将其显示出来。

### 更多实例

以下创建了一个 4x4 的二维 numpy 数组，并对其进行了三种不同的 imshow 图像展示。

第一张展示了灰度的色彩映射方式，并且没有进行颜色的混合（blending）。 第二张展示了使用viridis颜色映射的图像，同样没有进行颜色的混合。 第三张展示了使用viridis颜色映射的图像，并且使用了双立方插值方法进行颜色混合。

```
# 实例 6
import matplotlib.pyplot as plt
import numpy as np

n = 4

# 创建一个 n x n 的二维numpy数组
a = np.reshape(np.linspace(0,1,n**2), (n,n))

plt.figure(figsize=(12,4.5))

# 第一张图展示灰度的色彩映射方式，并且没有进行颜色的混合
plt.subplot(131)
plt.imshow(a, cmap='gray', interpolation='nearest')
plt.xticks(range(n))
plt.yticks(range(n))
# 灰度映射，无混合
plt.title('Gray color map, no blending', y=1.02, fontsize=12)

# 第二张图展示使用viridis颜色映射的图像，同样没有进行颜色的混合
plt.subplot(132)
plt.imshow(a, cmap='viridis', interpolation='nearest')
plt.yticks([])
plt.xticks(range(n))
# Viridis映射，无混合
plt.title('Viridis color map, no blending', y=1.02, fontsize=12)

# 第三张图展示使用viridis颜色映射的图像，并且使用了双立方插值方法进行颜色混合
plt.subplot(133)
plt.imshow(a, cmap='viridis', interpolation='bicubic')
plt.yticks([])
plt.xticks(range(n))
# Viridis 映射，双立方混合
plt.title('Viridis color map, bicubic blending', y=1.02, fontsize=12)
# 显示图像
plt.show()

```

## 后记

今天学习的是Python Matplotlib imshow学会了吗。 今天学习内容总结一下：
1. 显示灰度图像1. 显示彩色图像1. 显示热力图1. 显示地图1. 显示矩阵1. 更多实例