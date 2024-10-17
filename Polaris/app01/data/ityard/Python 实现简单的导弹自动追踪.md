
--- 
title:  Python 实现简单的导弹自动追踪 
tags: []
categories: [] 

---
>  
  作者：半壶砂  
  https://www.cnblogs.com/halfsand/p/7976636.html 
 

自动追踪算法，在我们设计2D射击类游戏时经常会用到，这个听起来很高大上的东西，其实也并不是军事学的专利，在数学上解决的话需要去解微分方程，

这个没有点数学基础是很难算出来的。但是我们有了计算机就不一样了，依靠计算机极快速的运算速度，我们利用微分的思想，加上一点简单的三角学知识，就可以实现它。

好，话不多说，我们来看看它的算法原理，看图：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcmJMdWZmS0U5dmx1eEpGdTQ5SWU3ZkpDVmhlM2ljSWtpYmpNVmhKaEsxSmhnbEkwZm1VaWFMdGdYa0xiRFBpYzBqeE9jOTUzRGZJNGFlQkEvNjQw?x-oss-process=image/format,png">

由于待会要用pygame演示，他的坐标系是y轴向下，所以这里我们也用y向下的坐标系。

算法总的思想就是根据上图，把时间t分割成足够小的片段（比如1/1000，这个时间片越小越精确），每一个片段分别构造如上三角形，计算出导弹下一个时间片走的方向（即∠a）和走的路程（即vt=|AC|），这时候目标再在第二个时间片移动了位置，这时刚才计算的C点又变成了第二个时间片的初始点，这时再在第二个时间片上在C点和新的目标点构造三角形计算新的vt，然后进入第三个时间片，如此反复即可。

假定导弹和目标的初始状态下坐标分别是(x1,y1),(x,y)，构造出直角三角形ABE，这个三角形用来求∠a的正弦和余弦值，因为vt是自己设置的，我们需要计算A到C点x和y坐标分别移动了多少，移动的值就是AD和CD的长度，这两个分别用vt乘cosa和sina即可。

计算sina和cosa，正弦对比斜，余弦邻比斜，斜边可以利用两点距离公式计算出，即：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcmJMdWZmS0U5dmx1eEpGdTQ5SWU3ZjJheWVJMDNVNGoyQjJPdTBNdEs3MFNoQzIyUGF4R2Rtcmw1VWZ3ODhKUmJvZUNRRkpsZVoxQS82NDA?x-oss-process=image/format,png">

于是

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcmJMdWZmS0U5dmx1eEpGdTQ5SWU3ZjZKSk5icHdkb2JsVGFTNE5sNVRPaWFOT2ZJYm1rMWVDUkhMOFBGcVM3aWN5M2FreGhYRXNMdGZnLzY0MA?x-oss-process=image/format,png">

AC的长度就是导弹的速度乘以时间即 |AC|=vt，然后即可计算出AD和CD的长度，于是这一个时间片过去后，导弹应该出现在新的位置C点，他的坐标就是老的点A的x增加AD和y减去CD。

于是，新的C点坐标就是：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcmJMdWZmS0U5dmx1eEpGdTQ5SWU3ZkVxeGVRcDdLNnAzY3ViM3lpY3RzQnFrWDBZNHN4emJZcVd6ZFM1NmRnVWVScWxubGRzQ3pLTEEvNjQw?x-oss-process=image/format,png">

只要一直反复循环执行这个操作即可，好吧，为了更形象，把第一个时间片和第二个时间片放在一起看看：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcmJMdWZmS0U5dmx1eEpGdTQ5SWU3ZklvdTI4M2RYVmJLM3NEaWFOTzU3Z1IxMjdINkVaaWFZc2ZKZXdMTkcwaWExZWNvMDJqVFhZZjVpYkEvNjQw?x-oss-process=image/format,png">

第一个是时间片构造出的三角形是ABE，经过一个时间片后，目标从B点走到了D点，导弹此时在C点，于是构造新的三角形CDF，重复刚才的计算过程即可，图中的角∠b就是导弹需要旋转的角度,现实中只需要每个时间片修正导弹的方向就可以了，具体怎么让导弹改变方向，这就不是我们需要研究的问题了

好，由于最近在用Python的pygame库制作小游戏玩，接下来我们就用pygame来演示一下这个效果，效果如下图：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcmJMdWZmS0U5dmx1eEpGdTQ5SWU3ZkhoNWljNWtQT0Y2NjJrVFVLeDltdlF1RjFlMHZYdTJZbnN3VHB6aWN6clNQZ0lsRFcwaWFOOHBEUS82NDA?x-oss-process=image/format,png">

很简单的代码如下：

```
import pygame,sysfrom math import *pygame.init()screen=pygame.display.set_mode((800,700),0,32)missile=pygame.image.load('element/red_pointer.png').convert_alpha()x1,y1=100,600           #导弹的初始发射位置velocity=800            #导弹速度time=1/1000             #每个时间片的长度clock=pygame.time.Clock()old_angle=0while True:    for event in pygame.event.get():        if event.type==pygame.QUIT:            sys.exit()    clock.tick(300)    x,y=pygame.mouse.get_pos()          #获取鼠标位置，鼠标就是需要打击的目标    distance=sqrt(pow(x1-x,2)+pow(y1-y,2))      #两点距离公式    p=velocity*time               #每个时间片需要移动的距离    sina=(y1-y)/distance    cosa=(x-x1)/distance    angle=atan2(y-y1,x-x1)              #两点线段的弧度值    x1,y1=(x1+p*cosa,y1-p*sina)    d_angle = degrees(angle)        #弧度转角度    screen.blit(missile, (x1-missile.get_width(), y1-missile.get_height()/2))    dis_angle=d_angle-old_angle          #dis_angle就是到下一个位置需要改变的角度    old_angle=d_angle                    #更新初始角度    pygame.display.update()

```

如果仅把导弹考虑为一个质点的话，那么以上算法就已经足矣，我没有做导弹的旋转，因为一个质点也不分头尾不需要旋转，当然这前提得是你加载的导弹图片很小的时候不旋转看起来也没什么问题。但是在pygame里面做旋转并不是一件容易的事情(也可能是我无知)，好吧我们先把图片替换成一张矩形的，再加入旋转函数看看效果如何

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQXJyZnN1UDJuYUVCN2tVWUNwaWJpY00wNG5haWNUVEdYUExsUG93M05ORFRyNXNKT1pYSzZmSWgyNTIzSmRzb2Z1Yk1YcXFTcGNYZWx6US82NDA?x-oss-process=image/format,png">

```
missiled = pygame.transform.rotate(missile, -(d_angle))screen.blit(missiled, (x1-missile.get_width(), y1-missile.get_height()/2))

```

因为图片的坐标点是它的左上角的点，所以如果我们想让图片的坐标固定在箭头尖点，那么把图片实际打印位置x减少图片长度，y减少一半宽度就行。

但是实际运行效果并不好：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcmJMdWZmS0U5dmx1eEpGdTQ5SWU3ZlppYm41U3VENWliTUt3cWlhc0pVbFNSczZNVlppYWxQNVF1Mk9IbFBsMER0ZEVVcGlhWHZWZk5ueFBnLzY0MA?x-oss-process=image/format,png">

大致方向相同，但是图片箭头的尖点并没有一直跟随鼠标，这是为什么呢。经过我的研究（就因为这个问题没解决一直没发布），

我发现原来是这个图旋转的机制问题，我们看看旋转后的图片变成什么样了：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQXJyZnN1UDJuYUVCN2tVWUNwaWJpY00wcEozSnNwNER3M3JLb2RpY1VsV0FzemRhbkhHWmttbUl5bUlqaWNpY1NkTjJwY1pzZzk2RXdrbjJRLzY0MA?x-oss-process=image/format,png">

旋转后的图片变成了蓝色的那个范围，根据旋转角度的不同，所变成的图片大小也不一样，我们看旋转90的情况

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQXJyZnN1UDJuYUVCN2tVWUNwaWJpY00wc1NYdzl6SVoxMXZ5eWljd2ljT05id29YYVhwdHdpY2Z5a2MyaWNVN1NWcExZMElYeDNzaGpnTUhDUS82NDA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQXJyZnN1UDJuYUVCN2tVWUNwaWJpY00wY09zZkZiNDduaGpoNnFQb2lhMVY5U1A0cVltbm1icERJYjNvQTk2QXJ1T2ZxQU5ybHlKQXRhZy82NDA?x-oss-process=image/format,png">

我们发现，旋转后的图片不仅面积变大了，导弹头的位置也变了。那应该怎么解决这个问题呢？思路是，每一次旋转图片以后，求出旋转图的头位置（图中的绿色箭头点），然后把绿图的打印位置移动一下，下，x，y分别移动两个头的距离，就可以让旋转后的导弹头对准实际我们参与运算的那个导弹头的位置，移动后应该是这样的：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRQXJyZnN1UDJuYUVCN2tVWUNwaWJpY00wYUJMbkZiTk1saWEyQlZpYlh1bmt4QWJZYlRNUjBkdE1vYTBqTmZJYm1MVVcxeUZIQkUwTW9SYVEvNjQw?x-oss-process=image/format,png">

这样，两个导弹头的点就一致了。接下来我们分析求旋转后的导弹头的算法。根据旋转角度的不同，旋转角在不同象限参数不一样，所以我们分为这四种情况

1，2象限

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcmJMdWZmS0U5dmx1eEpGdTQ5SWU3ZklOdVc5V0FTYjh0YVJLa0xDYWFSMWliV2djWExnZFU3ZmZmTFNVTlZNMDg5cWJBSGwxRkppY2R3LzY0MA?x-oss-process=image/format,png">

3，4象限，它的旋转只有正负0—180，所以3，4象限就是负角

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcmJMdWZmS0U5dmx1eEpGdTQ5SWU3Zk5iT1RyRTd2RlFwVlZCNXhEa0lPcjQ5NVVzTk1mNGNkdmIwT0tpY0hUREFPUHB2TnJpYXMwdXZnLzY0MA?x-oss-process=image/format,png">

显示图片的时候我们将他移动

```
screen.blit(missiled, (x1-width+(x1-C[0]),y1-height/2+(y1-C[1])))

```

这里的（x1-width,y1-height/2）其实才是上图中的（x1,y1）

所以最后我们加入相关算法代码，效果就比较完美了

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9IWlcwd3dGeGJRQXJyZnN1UDJuYUVCN2tVWUNwaWJpY00wRzBqMVJzVFYzVWVCNVl0dlo3YXB2QXNWb2hCRzFHeEIwOFJNUWRqYXdZb0lGNXFqNjJ6VFZBLzY0MA?x-oss-process=image/format,png">

大功告成，最后附上全部的算法代码

```
import pygame,sysfrom math import *pygame.init()font1=pygame.font.SysFont('microsoftyaheimicrosoftyaheiui',23)textc=font1.render('*',True,(250,0,0))screen=pygame.display.set_mode((800,700),0,32)missile=pygame.image.load('element/rect1.png').convert_alpha()height=missile.get_height()width=missile.get_width()pygame.mouse.set_visible(0)x1,y1=100,600           #导弹的初始发射位置velocity=800            #导弹速度time=1/1000             #每个时间片的长度clock=pygame.time.Clock()A=()B=()C=()while True:    for event in pygame.event.get():        if event.type==pygame.QUIT:            sys.exit()    clock.tick(300)    x,y=pygame.mouse.get_pos()          #获取鼠标位置，鼠标就是需要打击的目标    distance=sqrt(pow(x1-x,2)+pow(y1-y,2))      #两点距离公式    p=velocity*time               #每个时间片需要移动的距离    sina=(y1-y)/distance    cosa=(x-x1)/distance    angle=atan2(y-y1,x-x1)              #两点间线段的弧度值    fangle=degrees(angle)               #弧度转角度    x1,y1=(x1+p*cosa,y1-p*sina)    missiled=pygame.transform.rotate(missile,-(fangle))    if 0&lt;=-fangle&lt;=90:        A=(width*cosa+x1-width,y1-height/2)        B=(A[0]+height*sina,A[1]+height*cosa)
    if 90&lt;-fangle&lt;=180:        A = (x1 - width, y1 - height/2+height*(-cosa))        B = (x1 - width+height*sina, y1 - height/2)
    if -90&lt;=-fangle&lt;0:        A = (x1 - width+missiled.get_width(), y1 - height/2+missiled.get_height()-height*cosa)        B = (A[0]+height*sina, y1 - height/2+missiled.get_height())
    if -180&lt;-fangle&lt;-90:        A = (x1-width-height*sina, y1 - height/2+missiled.get_height())        B = (x1 - width,A[1]+height*cosa )
    C = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    screen.fill((0,0,0))    screen.blit(missiled, (x1-width+(x1-C[0]),y1-height/2+(y1-C[1])))    screen.blit(textc, (x,y)) #鼠标用一个红色*代替    pygame.display.update()


分享或在看是对我最大的支持 

```
