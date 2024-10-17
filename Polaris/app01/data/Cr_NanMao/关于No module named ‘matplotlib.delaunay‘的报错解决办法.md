
--- 
title:  关于No module named ‘matplotlib.delaunay‘的报错解决办法 
tags: []
categories: [] 

---
在学习《Python计算机视觉》这本书中，3.2.2分段仿射扭曲的这节内容。书本中的代码是



```
# Delaunay_Image.py
import matplotlib.delaunay as md
from pylab import *
from numpy import *


x, y = array(random.standard_normal((2, 100)))
centers, edges, tri, neighbors = Delaunay(x, y)

figure()
for t in tri:
    t_ext = [t[0], t[1], t[2], t[0]]    # 将第一个点加入到最后
    plot(x[t_ext], y[t_ext], 'r')

plot(x, y, '*')
axis('off')
show()
```

```
# warp.py
import homography
from numpy import *
from scipy import ndimage
import matplotlib.delaunay as md


def image_in_image(im1, im2, tp):
    """ 使用仿射变换将im1放置在im2上，使用im1图像的角和tp尽可能的靠近
     tp是齐次表示的，并且是按照从左上角逆时针计算的"""

    # 扭曲的点
    m, n = im1.shape[:2]
    fp = array([[0, m, m, 0], [0, 0, n, n], [1, 1, 1, 1]])

    # 计算仿射变换，并且将其应用于图下你过im1
    H = homography.Haffine_from_points(tp, fp)
    im1_t = ndimage.affine_transform(im1, H[:2, :2], (H[0, 2], H[1, 2]), im2.shape[:2])
    alpha = (im1_t &gt; 0)

    return (1 - alpha) * im2 + alpha * im1_t


def alpha_for_triangle(points, m, n):
    """ 对于带有由points定义角点的三角形，创建大小为（m，n）的alpha图（在归一化的齐次坐标意义下）"""

    alpha = zeros((m, n))
    for i in range(min(points[0]), max(points[0])):
        for j in range(min(points[1]), max(points[1])):
            x = linalg.solve(points, [i, j, 1])
            if min(x) &gt; 0:
                alpha[i, j] = 1
    return alpha


def triangulate_points(x, y):
    """ 二维点的Delaunay三角剖分 """

    centers, edges, tri, neighbors = Delaunay(x, y)
    return tri
```

运行以上代码会出现：No module named 'matplotlib.delaunay'的报错，可在Delaunay.py和warp.py中将以下代码修改，从而解决此问题：

```
# Delaunay_Image.py

# 将 import matplotlib.delaunay as md 改为

from scipy.spatial import Delaunay
。。。

x, y = array(random.standard_normal((2, 100)))

# 将centers, edges, tri, neighbors = Delaunay(x, y)改为

tri = Delaunay(np.c_[x, y]).simplices

。。。。
```

```
# warp.py
import homography
from numpy import *
from scipy import ndimage
# 将import matplotlib.delaunay as md改为

from scipy.spatial import Delaunay


。。。

def triangulate_points(x, y):
    """ 二维点的Delaunay三角剖分 """

    # 将centers, edges, tri, neighbors = Delaunay(x, y)改为

    tri = Delaunay(np.c_[x, y]).simplices

    return tri

```

一共4处地方需要修改。改完之后运行结果如下图所示：

<img alt="" height="1052" src="https://img-blog.csdnimg.cn/f3869f267e564b4aa79d6f8a062c1e5c.png" width="1200">



----  今天不学习，明天变废物！----


