
--- 
title:  Python学习笔记第七十二天（Matplotlib imread） 
tags: []
categories: [] 

---


#### Python学习笔记第七十二天
- - <ul><li>- - - 


## Matplotlib imread

imread() 方法是 Matplotlib 库中的一个函数，用于从图像文件中读取图像数据。

imread() 方法返回一个 numpy.ndarray 对象，其形状是 (nrows, ncols, nchannels)，表示读取的图像的行数、列数和通道数：

如果图像是灰度图像，则 nchannels 为 1。 如果是彩色图像，则 nchannels 为 3 或 4，分别表示红、绿、蓝三个颜色通道和一个 alpha 通道。 imread() 方法的语法如下：

```
matplotlib.pyplot.imread(fname, format=None)

```

参数说明：
- fname：指定了要读取的图像文件的文件名或文件路径，可以是相对路径或绝对路径。- format ：参数指定了图像文件的格式，如果不指定，则默认根据文件后缀名来自动识别格式。
### 读取图像数据

以下实例演示了如何使用 imread 函数从一张图像文件中读取图像数据，并将其显示出来

```
# 实例 1
import matplotlib.pyplot as plt

# 读取图像文件         图片任意即可，这里拿地图举例
img = plt.imread('map.jpeg')

# 显示图像
plt.imshow(img)
plt.show()

```

以上实例中我们首先使用 imread() 方法从名为 map.jpeg 的图像文件中读取了图像数据，并将其存储在 img 变量中。

然后我们使用imshow() 方法显示了这张图像。

注意：我们在显示图像时没有指定颜色映射，这是因为 imread() 方法已经将图像数据按照正确的颜色映射转换成了 RGB 格式，因此我们可以直接使用默认的颜色映射来显示图像。

### 修改图像

我们可以通过更改 numpy 数组来修改图像。

例如，如果我们将数组乘以一个数 0≤≤1，我们将图像变暗

```
# 实例 2
import matplotlib.pyplot as plt

# 读取图像文件         图片任意即可，这里拿老虎举例
img_array = plt.imread('tiger.jpeg')
tiger = img_array/255
#print(tiger)

# 显示图像
plt.figure(figsize=(10,6))

for i in range(1,5):
    plt.subplot(2,2,i)
    x = 1 - 0.2*(i-1)
    plt.axis('off') #hide coordinate axes
    plt.title('x={:.1f}'.format(x))
    plt.imshow(tiger*x)

plt.show()

```

### 裁剪图像

以下实例用于裁剪图像

```
# 实例 3
import matplotlib.pyplot as plt

# 读取图像文件
img_array = plt.imread('tiger.jpeg')
tiger = img_array/255
#print(tiger)

# 显示图像
plt.figure(figsize=(6,6))
plt.imshow(tiger[:300,100:400,:])
plt.axis('off')
plt.show()

```

### 图像颜色

如果我们将 RGB 颜色的绿色和蓝色坐标的数组元素设置为 0，我们将得到红色的图像：

```
# 实例 3
import matplotlib.pyplot as plt

# 读取图像文件
img_array = plt.imread('tiger.jpeg')
tiger = img_array/255
#print(tiger)

# 显示图像
red_tiger = tiger.copy()

red_tiger[:, :,[1,2]] = 0

plt.figure(figsize=(10,10))
plt.imshow(red_tiger)
plt.axis('off')
plt.show()

```

## 后记

今天学习的是Python Matplotlib imread学会了吗。 今天学习内容总结一下：
1. 读取图像数据1. 修改图像1. 裁剪图像1. 图像颜色