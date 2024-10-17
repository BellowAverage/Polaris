
--- 
title:  使用numpy处理图片——基础操作 
tags: []
categories: [] 

---


#### 大纲
- - - - 


numpy是一款非常优秀的处理多维数组的Python基础包。在现实中，我们最经常接触的多维数组相关的场景就是图像处理。本系列将通过若干篇对图像处理相关的探讨，来介绍numpy的使用方法，以获得直观的体验。 本系列使用的照片使用的是RGBA色彩空间模型，即一个像素点，要通过R（Red红色）、G（Green绿色）、B（Blue蓝色）和A（Alpha通道）组成。前三种三原色比较好理解，即一个颜色可以通过红绿蓝三种颜色组成；Alpha则是代表透明度，0代表完全透明，255代表完全不透明，中间的数值则代表相应程度的半透明。 <img src="https://img-blog.csdnimg.cn/direct/08b714d83d754034bce887f41649e4f5.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/direct/28a573740c5140ae962b310eb3d384cc.png" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/direct/dfa045f6265e4bafa76550e30a26f4ce.png" alt="请添加图片描述"> 可以看到Alpha 255的图片，背景是白色的，且是不透明的；而Alpha 0背景区域是完全透明。 一张图片，我们看成是一个像素组成的二维数组； <img src="https://img-blog.csdnimg.cn/direct/ac63daafaa574f4d856f5211b42329e4.png" alt="在这里插入图片描述"> 如果每个像素用RGBA表示，则演变成一个三维数组。只是之前的每个元素变成了一个长度为4的维度。

## 准备工作

下面是一张960*1536，背景色是白色，完全不透明的图片——example.png。后面我们将针对这张图片做相关处理。 <img src="https://img-blog.csdnimg.cn/direct/1bdfcadd204d4a8f825f8644bd80a56d.png" alt="请添加图片描述"> 为了能读取图片，我们需要安装另外一个python包

```
pip3 install pillow

```

## 图片像素大小

如果翻译成numpy相关的知识，就是获取数组的大小。这儿我们要使用。

```
from PIL import Image
import numpy as np
img = Image.open('example.png')
data = np.array(img)
print(data.shape)

```

>  
 (960, 1536, 4) 


可以见得我们将图片变成了一个3维数组：960表示高度，1536表示宽度，4表示深度。 <img src="https://img-blog.csdnimg.cn/direct/2a72a9edf56f4bfc850ae758c3dc4f43.png" alt="在这里插入图片描述">

## 修改透明度

如果翻译成numpy相关的知识，就是修改数组中第三个维度（RGBA）的第四个位置（A）的值。

```
from PIL import Image
import numpy as np
img = Image.open('example.png')
data = np.array(img)

data[:,:,3]= 32

newImg = Image.fromarray(data)
newImg.save('alpha32.png')

```

上面代码将Alpha通道值改成了32，即一种半透明状态。 代码的第6行，第一个“:”表示所有的第一维度（高），第二个“:”表示所有的第二维度（宽），3表示Alpha通道所在的RGBA中的下标。 这种写法，比逐个遍历数据要方便的多。 <img src="https://img-blog.csdnimg.cn/direct/aaf7570c2086415984f4551f3e8e8689.png" alt="请添加图片描述">

## 代码地址


