
--- 
title:  用Python画一棵带音乐的雪夜圣诞树 
tags: []
categories: [] 

---
本文我们用 Python 来画一棵带音乐效果的雪夜圣诞树，基本思路如下：
- 用 Python 画一棵圣诞树作为背景图- 在圣诞树背景图中添加雪落效果及音乐
下面来看一下具体实现。

首先，我们来画一棵圣诞树，主要用到的 Python 库为 turtle，主要代码实现如下：

```
n = 80.0
turtle.setup(700, 700, 0, 0)
turtle.speed("fastest")
turtle.screensize(bg='black')
turtle.left(90)
turtle.forward(3 * n)
turtle.color("orange", "yellow")
turtle.begin_fill()
turtle.left(126)
for i in range(5):
    turtle.forward(n / 5)
    turtle.right(144)
    turtle.forward(n / 5)
    turtle.left(72)
turtle.end_fill()
turtle.right(126)
turtle.color("dark green")
turtle.backward(n * 4.8)
def tree(d, s):
    if d &lt;= 0: return
    turtle.forward(s)
    tree(d - 1, s * .8)
    turtle.right(120)
    tree(d - 3, s * .5)
    turtle.right(120)
    tree(d - 3, s * .5)
    turtle.right(120)
    turtle.backward(s)
tree(15, n)
turtle.backward(n / 2)
for i in range(200):
    a = 200 - 400 * random.random()
    b = 10 - 20 * random.random()
    turtle.up()
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.down()
    if random.randint(0, 1) == 0:
        turtle.color('tomato')
    else:
        turtle.color('wheat')
        turtle.circle(2)
        turtle.up()
        turtle.backward(a)
        turtle.right(90)
        turtle.backward(b)
time.sleep(60)

```

看一下效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb2wwMWxLT3hacDhpYTJKNW1pYXNuUGZ5Rzd2U2hldUxnc0ppY2ljb0tyZHFtSVBicmQ4eWliZ3haSkN4SU1oMEVUNmljYzh4YmJzczlCRGN0dy82NDA?x-oss-process=image/format,png">

接着将圣诞树作为背景图添加雪落效果及音乐，主要用到的 Python 库为 pygame，主要代码实现如下：

```
# 初始化 pygame
pygame.init()
#设置屏幕宽高，根据背景图调整
bg_img = "bg.png"
bg_size = (609, 601)
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("雪夜圣诞树")
bg = pygame.image.load(bg_img)
# 雪花列表
snow_list = []
for i in range(150):
    x_site = random.randrange(0, bg_size[0])   # 雪花圆心位置
    y_site = random.randrange(0, bg_size[1])   # 雪花圆心位置
    X_shift = random.randint(-1, 1)         # x 轴偏移量
    radius = random.randint(4, 6)           # 半径和 y 周下降量
    snow_list.append([x_site, y_site, X_shift, radius])
# 创建时钟对象
clock = pygame.time.Clock()
# 添加音乐
track = pygame.mixer.music.load('my.mp3')  # 加载音乐文件
pygame.mixer.music.play() # 播放音乐流
pygame.mixer.music.fadeout(600000)  # 设置音乐结束时间
done = False
while not done:
    # 消息事件循环，判断退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(bg, (0, 0))
    # 雪花列表循环
    for i in range(len(snow_list)):
        # 绘制雪花，颜色、位置、大小
        pygame.draw.circle(screen, (255, 255, 255), snow_list[i][:2], snow_list[i][3] - 3)
        # 移动雪花位置（下一次循环起效）
        snow_list[i][0] += snow_list[i][2]
        snow_list[i][1] += snow_list[i][3]
        # 如果雪花落出屏幕，重设位置
        if snow_list[i][1] &gt; bg_size[1]:
            snow_list[i][1] = random.randrange(-50, -10)
            snow_list[i][0] = random.randrange(0, bg_size[0])
    # 刷新屏幕
    pygame.display.flip()
    clock.tick(30)
# 退出
pygame.quit()

```

看一下最终效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJb2wwMWxLT3hacDhpYTJKNW1pYXNuUGZ5NVcxdGt0NkhUVHFKNEZWQWlick1vS1lXdjczRlRNM3l6R1ZYWkN6S0xrRHVJc0lTMFlvdmppY0EvNjQw?x-oss-process=image/format,png">

这里就不放视频了，大家如果想听一下音乐效果可以自己获取源码执行一下。

源码及相应文件在公号后台回复**201225**获取。

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">
