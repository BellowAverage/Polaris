
--- 
title:  《python计算机视觉》关于‘numpy.float64‘ object cannot be interpreted as an integer错误的解决办法 
tags: []
categories: [] 

---
在《python计算机视觉》这本书的学习中，按照书中的代码敲完运行会发现这个报错：<img alt="" height="290" src="https://img-blog.csdnimg.cn/10c735ecb75445049ec931e6999b8ae0.png" width="1200">

运行代码如下：

```
#  Warp_Triangle_Image01.py

from pylab import *
import warp
from PIL import Image
from numpy import *



# 打开图像，并将其扭曲
fromim = array(Image.open('sunset_tree.jpg'))
x, y = meshgrid(range(5), range(6))
x = (fromim.shape[1]/4) * x.flatten()
y = (fromim.shape[0]/5) * y.flatten()

# 三角部分
tri = warp.triangulate_points(x, y)

# 打开图像和目标点
im = array(Image.open('turningtorso1.jpg'))
tp = loadtxt('turningtorso1_points.txt')   # dextination points

# 将点转换成齐次坐标
fp = vstack((y, x, ones((1, len(x)))))
tp = vstack((tp[:, 1], tp[:, 0], ones((1, len(tp)))))

# 扭曲三角形
im = warp.pw_affine(fromim, im, fp, tp, tri)

# 绘制图像
figure()
imshow(im)
warp.plot_mesh(tp[1], tp[0], tri)
axis('off')
show()

```

```
# warp.py
import homography
from scipy import ndimage
from scipy.spatial import Delaunay
from pylab import *
from numpy import *


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

    # centers, edges, tri, neighbors = Delaunay(x, y)
    tri = Delaunay(np.c_[x, y]).simplices
    return tri


def pw_affine(fromim, toim, fp, tp, tri):
    """ 从一幅图像中扭曲矩形图模块
    fromim = 将要扭曲的图像
    toim = 目标图像
    fp = 齐次坐标表示下，扭曲前的点
    tp = 齐次坐标表示下，扭曲后的点
    tri = 三角剖分 """

    im = toim.copy()

    # 检查图像是灰度图像还是彩色图像
    is_color = len(fromim.shape) == 3

    # 创建扭曲后的图像（如果需要对彩色图像的每个颜色通道进行迭代操作，那么有必要这样做）
    im_t = zeros(im.shape, 'uint8')

    for t in tri:
        # 计算仿射变换
        H = homography.Haffine_from_points(tp[:, t], fp[:, t])

        if is_color:
            for col in range(fromim.shape[2]):
                im_t[:, :, col] = ndimage.affine_transform(
                    fromim[:, :, col], H[:2, :2], (H[0, 2], H[1, 2]), im.shape[:2])
        else:
            im_t = ndimage.affine_transform(
                fromim, H[:2, :2], (H[0, 2], H[1, 2]), im.shape[:2])

        # 三角形的alpha
        alpha = alpha_for_triangle(tp[:, t], im.shape[0], im.shape[1])

        # 将三角形加入到图像中
        im[alpha &gt; 0] = im_t[alpha &gt; 0]

    return im


def plot_mesh(x, y, tri):
    """ 绘制三角形 """

    for t in tri:
        t_ext = [t[0], t[1], t[2], t[0]]   # 将第一个点加入到最后
        plot(x[t_ext], y[t_ext], 'r')
```

根据错误我们看到 warp.py 中的 alpha_for_triangle(points, m, n) 函数，报错说明min()和max()的参数是float64类型，应该将之转换成int类型。

```
 for i in range(min(points[0]), max(points[0])):
        for j in range(min(points[1]), max(points[1])):
```

修改后的代码如下所示：

```
  for i in range(int(min(points[0])), int(max(points[0]))):
        for j in range(int(min(points[1])), int(max(points[1]))):
```

修改后运行结果如下图所示：<img alt="" height="1048" src="https://img-blog.csdnimg.cn/80248ceb164b413aa06982ddd1b76554.png" width="1200">



----  今天不学习，明天变废物。 ----
