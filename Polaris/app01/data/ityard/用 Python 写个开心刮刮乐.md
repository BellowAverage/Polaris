
--- 
title:  用 Python 写个开心刮刮乐 
tags: []
categories: [] 

---
刮刮卡通常指卡上的一种覆盖数字和字母密码等的涂层，通常包括纸质和电子两种类型，刮刮卡在市场上有着比较广泛的应用，我们见到最多的应该是各类抽奖活动了，本文我们使用 Python 来做一个简单的抽奖刮刮卡。

首先，我们弄几张图片做底板，如下所示：

<img src="https://img-blog.csdnimg.cn/20210306152230518.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

从图中我们可以看到底图包括：一等奖、二等奖、谢谢惠顾三种，如果我们参与过刮刮卡抽奖的话，会发现几乎刮开都是谢谢惠顾之类的，也就是有个概率的问题，这里我们也简单设置一下，一等奖放一张、二等奖放两张、谢谢惠顾放三张，生成刮刮卡时随机使用底图就可以了。

实现刮刮卡，我们主要用到是 pygame 模块，之前做小游戏时已经用到过几次了，大家应该都比较熟悉，下面看一下具体实现。

我们先定义一下常量，如：路径、图片类型、颜色等，代码实现如下：

```
path = 'prize'
ptype = ['jpg', 'png', 'bmp', 'JPG', 'PNG', 'BMP']
# 窗口大小
screen_size = (600, 400)
white = (255, 255, 255, 20)
gray = (192, 192, 192)

```

然后创建一个窗口，代码实现如下：

```
pygame.init()
pygame.mouse.set_cursor(*pygame.cursors.diamond)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('刮一刮抽奖')

```

接着从所有底图中随机取出一张绑定到窗口，代码实现如下：

```
filenames = os.listdir(path)
filenames = [f for f in filenames if f.split('.')[-1] in ptype]
imgpath = os.path.join(path, random.choice(filenames))
image_used = pygame.transform.scale(pygame.image.load(imgpath), screen_size)
screen.blit(image_used, (0, 0))

```

再接着做一个灰色的图层覆盖到底图上，代码实现如下：

```
surface = pygame.Surface(screen_size).convert_alpha()
surface.fill(gray)
screen.blit(surface, (0, 0))

```

最后，我们定义一下鼠标事件，在鼠标移动经过的地方，将图层置为透明，漏出底图，代码实现如下：

```
mouse_event = pygame.mouse.get_pressed()
if mouse_event[0]:
	pygame.draw.circle(surface, white, pygame.mouse.get_pos(), 40)
elif mouse_event[-1]:
	surface.fill(gray)
	image_used = pygame.transform.scale(pygame.image.load(imgpath), screen_size)

```

一起来看一下实现效果：

<img src="https://img-blog.csdnimg.cn/20210306152312146.gif#pic_center" alt="">

是不是有内味了。

源码在公众号 **Python小二** 后台回复 **200715** 获取

>  
 本文非首发于个人号 

