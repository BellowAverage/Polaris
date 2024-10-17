
--- 
title:  Python学习笔记第七十一天（Matplotlib imsave） 
tags: []
categories: [] 

---


#### Python学习笔记第七十一天
- - <ul><li>- 


## Matplotlib imsave

imsave() 方法是 Matplotlib 库中用于将图像数据保存到磁盘上的函数。

通过 imsave() 方法我们可以轻松将生成的图像保存到我们指定的目录中。

imsave() 方法保存图片支持多种图像格式，例如 PNG、JPEG、BMP 等。

imsave() 方法的语法如下：

```
matplotlib.pyplot.imsave(fname, arr, **kwargs)

```

参数说明：
- fname：保存图像的文件名，可以是相对路径或绝对路径。- arr：表示图像的NumPy数组。- kwargs：可选参数，用于指定保存的图像格式以及图像质量等参数。
### imsave保存图像

以下是一个使用 imsave() 方法保存图像的简单实例：

```
# 实例 1
import matplotlib.pyplot as plt
import numpy as np

# 创建一个二维的图像数据
img_data = np.random.random((100, 100))

# 显示图像
plt.imshow(img_data)

# 保存图像到磁盘上
plt.imsave('test.png', img_data)

```

以上实例我们使用 imsave() 方法将这个图像保存到了当前目录下，文件名为 test.png。

由于没有指定图像格式，Matplotlib 库默认将其保存为 PNG 格式的文件。

打开当前目录，会发现一个 test.png 文件。

### 保存灰度图像和彩色图像

以下实例演示了如何使用 imsave() 方法将一个灰度图像和一个彩色图像保存到当前目录上

```
# 实例 2
import matplotlib.pyplot as plt
import numpy as np

# 创建一幅灰度图像
img_gray = np.random.random((100, 100))

# 创建一幅彩色图像
img_color = np.zeros((100, 100, 3))
img_color[:, :, 0] = np.random.random((100, 100))
img_color[:, :, 1] = np.random.random((100, 100))
img_color[:, :, 2] = np.random.random((100, 100))

# 显示灰度图像
plt.imshow(img_gray, cmap='gray')

# 保存灰度图像到磁盘上
plt.imsave('test_gray.png', img_gray, cmap='gray')

# 显示彩色图像
plt.imshow(img_color)

# 保存彩色图像到磁盘上
plt.imsave('test_color.jpg', img_color)

```

以上实例中我们使用了 numpy.random 模块分别创建了一幅灰度图像和一幅彩色图像，然后分别使用 imshow() 方法显示这两幅图像。

接着，我们使用 imsave() 函数将这两幅图像分别保存到了当前目录傻姑娘，文件名分别为 test_gray.png 和 test_color.jpg。

在保存灰度图像时，我们使用了 cmap 参数将其保存为灰度图像格式。

在保存彩色图像时，我们没有指定图像格式，Matplotlib 库默认将其保存为 JPEG 格式的文件（.jpg拓展名文件）。

## 后记

今天学习的是Python Matplotlib imsave学会了吗。 今天学习内容总结一下：
1. imsave保存图像1. 保存灰度图像和彩色图像