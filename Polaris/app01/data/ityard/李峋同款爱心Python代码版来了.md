
--- 
title:  李峋同款爱心Python代码版来了 
tags: []
categories: [] 

---
最近看到不少关于李峋同款爱心的视频、文章，今天我们也分享一下李峋同款爱心 Python 代码版。要问李峋是谁？我也不太清楚，大家可自行百度，这个是我百度的结果，仅供参考。

简单来说李峋同款爱心就是一个动态的♥型效果，主要 Python 代码实现如下：

```
def __init__(self, generate_frame=20):
# 原始爱心坐标集合
self._points = set()  
# 边缘扩散效果点坐标集合
self._edge_diffusion_points = set()  
# 中心扩散效果点坐标集合
self._center_diffusion_points = set()  
# 每帧动态点坐标
self.all_points = {}  
self.build(2000)
self.random_halo = 1000
self.generate_frame = generate_frame
for frame in range(generate_frame):
 self.calc(frame)

def build(self, number):
for _ in range(number):
 t = random.uniform(0, 2 * pi)
 x, y = heart(t)
 self._points.add((x, y))
# 爱心内扩散
for _x, _y in list(self._points):
 for _ in range(3):
  x, y = scatter_inside(_x, _y, 0.05)
  self._edge_diffusion_points.add((x, y))
# 爱心内再次扩散
point_list = list(self._points)
for _ in range(4000):
 x, y = random.choice(point_list)
 x, y = scatter_inside(x, y, 0.17)
 self._center_diffusion_points.add((x, y))

@staticmethodstaticmethod
def calc_position(x, y, ratio):
force = 1 / (((x - X) ** 2 +
     (y - Y) ** 2) ** 0.520)
dx = ratio * force * (x - X) + random.randint(-1, 1)
dy = ratio * force * (y - Y) + random.randint(-1, 1)
return x - dx, y - dy

def calc(self, generate_frame):
ratio = 10 * curve(generate_frame / 10 * pi)
halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
halo_number = int(
 3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))
all_points = []
# 光环
heart_halo_point = set()
for _ in range(halo_number):
 t = random.uniform(0, 2 * pi)
 x, y = heart(t, shrink_ratio=11.6)
 x, y = shrink(x, y, halo_radius)
 if (x, y) not in heart_halo_point:
  heart_halo_point.add((x, y))
  x += random.randint(-14, 14)
  y += random.randint(-14, 14)
  size = random.choice((1, 2, 2))
  all_points.append((x, y, size))
# 轮廓
for x, y in self._points:
 x, y = self.calc_position(x, y, ratio)
 size = random.randint(1, 3)
 all_points.append((x, y, size))
# 内容
for x, y in self._edge_diffusion_points:
 x, y = self.calc_position(x, y, ratio)
 size = random.randint(1, 2)
 all_points.append((x, y, size))
self.all_points[generate_frame] = all_points
for x, y in self._center_diffusion_points:
 x, y = self.calc_position(x, y, ratio)
 size = random.randint(1, 2)
 all_points.append((x, y, size))
self.all_points[generate_frame] = all_points
```

实现效果如下：

源码已经整理好了，获取方式如下：

1、点击**下方**图片拉到文末点**喜欢作者**赞赏 **4** 元



2、我核实后会直接回复你源码下载链接，如未能及时回复可以添加小二微信，小二直接用微信发你~

<img src="https://img-blog.csdnimg.cn/img_convert/bc731bae3add64cbe0f187f6af29dd44.jpeg" alt="bc731bae3add64cbe0f187f6af29dd44.jpeg">

**不是机器人**

**耐心等待，不要着急**
- - - 