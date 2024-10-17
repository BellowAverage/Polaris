
--- 
title:  用 Python 动态模拟太阳系运转 
tags: []
categories: [] 

---
提到太阳系，大家可能会想到哥白尼和他的日心说，或是捍卫、发展日心说的斗士布鲁诺，他们像一缕光一样照亮了那个时代的夜空，对历史感兴趣的小伙伴可以深入了解一下，这里就不多说了。

太阳以巨大的引力使周边行星、卫星等绕其运转，构成了太阳系，它主要包括太阳、8 个行星、205 个卫星以及几十万个小行星等，本文我们使用 Python 来简单的动态模拟一下太阳系的运转。

### 实现

功能的实现，主要要到的还是 Python 的 pygame 库，我们先导入需要的所有 Python 库，代码如下所示：

```
import sys
import math
import pygame
from pygame.locals import *

```

接着定义一些常量（如：颜色、宽高等）及创建窗口，代码如下所示：

```
WHITE =(255, 255, 255)
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SandyBrown = (244, 164, 96)
PaleGodenrod = (238, 232, 170)
PaleVioletRed = (219, 112, 147)
Thistle = (216, 191, 216)
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("太阳系")
# 创建时钟(控制游戏循环频率)
clock = pygame.time.Clock()
# 定义三个空列表
pos_v = pos_e = pos_mm = []
# 地球、月球等行星转过的角度
roll_v = roll_e = roll_m = 0
roll_3 = roll_4 = roll_5 = roll_6 = roll_7 = roll_8 = 0
# 太阳的位置（中心）
position = size[0] // 2, size[1] // 2

```

我们先在窗口中画一个太阳，代码如下：

```
pygame.draw.circle(screen, YELLOW, position, 60, 0)

```

看一下效果： <img src="https://img-blog.csdnimg.cn/img_convert/9aa35b64436f73861a5649c6f5c57275.png" alt=""> 接着画一个地球，让其绕着太阳旋转，代码如下：

```
# 画地球
roll_e += 0.01  # 假设地球每帧公转 0.01 pi
pos_e_x = int(size[0] // 2 + size[1] // 6 * math.sin(roll_e))
pos_e_y = int(size[1] // 2 + size[1] // 6 * math.cos(roll_e))
pygame.draw.circle(screen, BLUE, (pos_e_x, pos_e_y), 15, 0)
# 地球的轨迹线
pos_e.append((pos_e_x, pos_e_y))
if len(pos_e) &gt; 255:
	pos_e.pop(0)
for i in range(len(pos_e)):
	pygame.draw.circle(screen, SILVER, pos_e[i], 1, 0)

```

看一下效果： <img src="https://img-blog.csdnimg.cn/img_convert/40500071888b26f5131ce8c5d4bae0d4.png" alt=""> 我们再接着画月球，代码如下：

```
# 画月球
roll_m += 0.1
pos_m_x = int(pos_e_x + size[1] // 20 * math.sin(roll_m))
pos_m_y = int(pos_e_y + size[1] // 20 * math.cos(roll_m))
pygame.draw.circle(screen, SILVER, (pos_m_x, pos_m_y), 8, 0)
# 月球的轨迹线
pos_mm.append((pos_m_x, pos_m_y))
if len(pos_mm) &gt; 255:
	pos_mm.pop(0)
for i in range(len(pos_mm)):
	pygame.draw.circle(screen, SILVER, pos_mm[i], 1, 0)

```

看一下效果： <img src="https://img-blog.csdnimg.cn/img_convert/39590764348fe369800762be547f6272.png" alt=""> 其他几个星球的实现也类似，代码如下：

```
# 其他几个行星
roll_3 += 0.03
pos_3_x = int(size[0] // 2 + size[1] // 3.5 * math.sin(roll_3))
pos_3_y = int(size[1] // 2 + size[1] // 3.5 * math.cos(roll_3))
pygame.draw.circle(screen, GREEN, (pos_3_x, pos_3_y), 20, 0)
roll_4 += 0.04
pos_4_x = int(size[0] // 2 + size[1] // 4 * math.sin(roll_4))
pos_4_y = int(size[1] // 2 + size[1] // 4 * math.cos(roll_4))
pygame.draw.circle(screen, SandyBrown, (pos_4_x, pos_4_y), 20, 0)
roll_5 += 0.05
pos_5_x = int(size[0] // 2 + size[1] // 5 * math.sin(roll_5))
pos_5_y = int(size[1] // 2 + size[1] // 5 * math.cos(roll_5))
pygame.draw.circle(screen, PaleGodenrod, (pos_5_x, pos_5_y), 20, 0)
roll_6 += 0.06
pos_6_x = int(size[0] // 2 + size[1] // 2.5 * math.sin(roll_6))
pos_6_y = int(size[1] // 2 + size[1] // 2.5 * math.cos(roll_6))
pygame.draw.circle(screen, PaleVioletRed, (pos_6_x, pos_6_y), 20, 0)
roll_7 += 0.07
pos_7_x = int(size[0] // 2 + size[1] // 4.5 * math.sin(roll_7))
pos_7_y = int(size[1] // 2 + size[1] // 4.5 * math.cos(roll_7))
pygame.draw.circle(screen, Thistle, (pos_7_x, pos_7_y), 20, 0)
roll_8 += 0.08
pos_8_x = int(size[0] // 2 + size[1] // 5.5 * math.sin(roll_8))
pos_8_y = int(size[1] // 2 + size[1] // 5.5 * math.cos(roll_8))
pygame.draw.circle(screen, WHITE, (pos_8_x, pos_8_y), 20, 0)

```

最后，我们来看一下整体实现的动态效果： <img src="https://img-blog.csdnimg.cn/img_convert/f436f4bf4466d06b8acbd6f4fd38ab66.gif" alt=""> 是不是有内味了。

### 总结

本文我们使用 Python 简单模拟了太阳系的运转，有兴趣的小伙伴可以自己运行一下代码或对功能做进一步扩展。

源码在公众号 **Python小二** 后台回复 **200812** 获取。

>  
 本文非首发于个人号 

