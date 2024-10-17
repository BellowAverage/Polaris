
--- 
title:  关于NameError: name ‘ histogram‘ is not defined报错的处理方法 
tags: []
categories: [] 

---


以下代码是工具包imtools.py：

```
import os

# 工具包
def get_imlist(path):
    """ 返回目录中所有JPG图像的文件名列表 """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im, sz):
    """ 使用PIL对象重新定义图像数组的大小 """
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
    """ 对一幅灰度图像进行直方图均衡化 """
    # 计算图像的直方图
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()   # 累积分布函数
    cdf = 255 * cdf / cdf[-1]   # 归一化
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf

def compute_average(imlist):
    """ 计算图像列表的平均图像 """
    # 打开第一幅图像，将其存储在浮点型数组中
    average = array(Image.open(imlist[0]), 'f')
    for imnae in imlist[1:]:
        try:
            average += array(Image.open(imname))
        except:
            print(imname + '...skipped')
        averageim /= len(imlist)
    # 返回uint8类型的平均图像
    return array(averageim, 'uint8')
```

以下代码是Histogram_Average.py：

```
from PIL import Image
from pylab import *
import imtools

# 直方图均衡化
im = array(Image.open('AquaTermi_lowcontrast.JPG').convert('L'))
im2, cdf = imtools.histeq(im)

figure()
gray()
subplot(221)
axis('off')
title(r'before')
imshow(im)

subplot(222)
axis('off')
title(r'after')
imshow(im2)

subplot(223)
hist(im.flatten(), 128)

subplot(224)
hist(im2.flatten(), 128)

show()

```

当运行Histogram_Average.py时出现报错NameError: name ' histogram' is not defined：<img alt="" height="406" src="https://img-blog.csdnimg.cn/e0469f1d591842ac8b54d18dc11d0b95.png" width="1200">



问题出现在工具包imtools.py中没有提前导入numpy包，只需要在imtools.py开头添加

```
from numpy import *
```

在添加之后运行 Histogram_Average.py 结果如下图所示：

<img alt="" height="420" src="https://img-blog.csdnimg.cn/48f4ef58eaac41b6b970449b5711b1ca.png" width="496">



bug完美解决！！希望以后学习的时候一定顺利～
