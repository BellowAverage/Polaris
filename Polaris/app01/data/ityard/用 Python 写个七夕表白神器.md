
--- 
title:  用 Python 写个七夕表白神器 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20200824193607729.PNG#pic" alt="" width="1200"> 今天是七夕节，相比于现代人自创的 502，不对是 520，七夕才是中国传统意义上的情人节，本文分享几个 Python 表白程序，情侣可以现学现用，单身的话也可以先收藏一下，说不定下次就用上了。

### 爱心树

首先，我们来画一棵长满爱心果实的树。

<img src="https://img-blog.csdnimg.cn/20200824201551978.PNG#pic_center" alt="" width="500">

主要实现代码：

```
# 画爱心
def love(x, y): 
    lv = turtle.Turtle()
    lv.hideturtle()
    lv.up()
    # 定位
    lv.goto(x, y)
    # 画圆弧
    def curvemove():  
        for i in range(20):
            lv.right(10)
            lv.forward(2)

    lv.color('red', 'pink')
    lv.speed(10000000)
    lv.pensize(1)
    lv.down()
    lv.begin_fill()
    lv.left(140)
    lv.forward(22)
    curvemove()
    lv.left(120)
    curvemove()
    lv.forward(22)
    # 画完复位
    lv.left(140)  
    lv.end_fill()

# 画树
def tree(branchLen, t):
    # 剩余树枝太少要结束递归
    if branchLen &gt; 5:
        # 如果树枝剩余长度较短则变绿
        if branchLen &lt; 20:  
            t.color("green")
            t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
            t.down()
            t.forward(branchLen)
            love(t.xcor(), t.ycor())  
            t.up()
            t.backward(branchLen)
            t.color("brown")
            return
        t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))
        t.down()
        t.forward(branchLen)
        # 以下递归
        ang = random.uniform(15, 45)
        t.right(ang)
        # 随机决定减小长度
        tree(branchLen - random.uniform(12, 16), t)  
        t.left(2 * ang)
        # 随机决定减小长度
        tree(branchLen - random.uniform(12, 16), t)  
        t.right(ang)
        t.up()
        t.backward(branchLen)

```

### 表白气球

我们接着看一下表白气球的实现，要实现的效果是：随机生成各种颜色向上漂浮的气球，点击气球会破。

<img src="https://img-blog.csdnimg.cn/20200824201617856.gif#pic_center" alt="" width="500">

主要实现代码如下：

```
# 气球
balloons = []
# 颜色
color_option = ["red", "blue", "green", "purple", "pink", "yellow", "orange"]
# 气球大小
size = 50
# 气球线
def line(x, y, a, b, line_width=1, color_name="black"):
    up()
    goto(x, y)
    down()
    color(color_name)
    width(line_width)
    goto(a, b)

def distance(x, y, a, b):
    # 判断鼠标点击位置和气球坐标的距离
    return ((a - x) ** 2 + (b - y) ** 2) ** 0.5
def tap(x, y):
    for i in range(len(balloons)):
        # 判断是否点击气球队列中的其中一个
        if distance(x, y, balloons[i][0], balloons[i][1]) &lt; (size / 2):
            # 删除气球
            balloons.pop(i)  
            return  
def draw():
    # 清除画布
    clear()
    for i in range(1, (len(balloons) + 1)):  
        line(balloons[-i][0], balloons[-i][1], balloons[-i][0], balloons[-i][1] - size * 1.5, 1)
        up()  
        goto(balloons[-i][0], balloons[-i][1])
        # 画原点，参数为大小和颜色
        dot(size, balloons[-i][2])
        # 改变纵坐标，模仿气球上升
        balloons[-i][1] = balloons[-i][1] + 1
    # 修改画布
    update()  
def gameLoop():
    # 1/50 的概率生成一个气球
    if randrange(0, 50) == 1:
        # 气球坐标，在边框位置减去气球大小
        x = randrange(-200 + size, 200 - size)
        # 随机在颜色队列选择一个颜色
        c = choice(color_option)
        # 添加气球队列
        balloons.append([x, -200 - size, c])  
    draw()
    ontimer(gameLoop, 10)  

```

### 表白卡

我们可以通过 Python 在原有照片上添加一些适合主题的诗词来制作表白卡。

原图：

<img src="https://img-blog.csdnimg.cn/20200824201640439.png#pic_center" alt="" width="500">

效果图：

<img src="https://img-blog.csdnimg.cn/20200824201705562.png#pic_center" alt="" width="500">

主要实现代码如下：

```
img = cv2.imread('test.png')
mask = np.zeros(img.shape[:2], np.uint8)
size = (1, 65)
bgd = np.zeros(size, np.float64)
fgd = np.zeros(size, np.float64)
rect = (1, 1, img.shape[1], img.shape[0])
cv2.grabCut(img, mask, rect, bgd, fgd, 10, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 1, 255)
img = img.astype(np.int32)
img *= mask2[:, :, np.newaxis]
img[img&gt;255] = 255
img =img.astype(np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = Image.fromarray(img, 'RGB')
img.save('test1.jpg')
fp = open(r"word.txt", "r", encoding="utf-8")
text = fp.read()
mask_pic=np.array(Image.open(r"test1.jpg"))
wordcloud = WordCloud(font_path='hyr3gjm.ttf',mask=mask_pic,max_words=200).generate(text)
image=wordcloud.to_image()
image.save("wordcloud2.png")
cloud_data = np.array(image)
alpha = np.copy(cloud_data[:,:,0])
alpha[alpha&gt;0] = 255
new_image = Image.fromarray(np.dstack((cloud_data, alpha)))
card = Image.open("test.png")
card = card.convert("RGBA")
card.paste(new_image, (0,0), mask=new_image)
card.save("card.png")

```

当然了，除了这些还可以画玫瑰花什么的，可以看一下：。

>  
 欢迎微信搜索 **Python小二**，第一时间阅读、获取源码，回复关键字 **1024** 可以免费领取个人整理的各类编程语言学习资料。 

