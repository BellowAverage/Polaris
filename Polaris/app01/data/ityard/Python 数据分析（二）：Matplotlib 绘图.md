
--- 
title:  Python 数据分析（二）：Matplotlib 绘图 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- - <ul><li>- <ul><li>- - - - - 


### 1. 简介

Matplotlib 是 Python 提供的一个绘图库，通过该库我们可以很容易的绘制出折线图、直方图、散点图、饼图等丰富的统计图，安装使用 `pip install matplotlib` 命令即可，Matplotlib 经常会与  一起使用。

在进行数据分析时，可视化工作是一个十分重要的环节，数据可视化可以让我们更加直观、清晰的了解数据，Matplotlib 就是一种可视化实现方式。

### 2. 绘图

下面我们来学习一下如何使用 Matplotlib 绘制常用统计图。

#### 2.1 折线图

折线图可以显示随某一指标变化的连续数据。

##### 2.1.1 单线

首先，我们来看一下如何使用 Matplotlib 绘制一个简单的折线图，具体实现如下：

```
from matplotlib import pyplot as plt

x = range(1, 7)
y = [13, 15, 14, 16, 15, 17]
plt.title('折线图')
plt.xlabel('x 轴')
plt.ylabel('y 轴')
plt.plot(x, y)
plt.show()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200314105639485.PNG?#pic" alt="" width="500"> 我们在使用中文时可能会现乱码的问题，可以通过如下方式解决： ① 下载 ，放到 `site-packages\matplotlib\mpl-data\fonts\ttf` 目录下 ② 到 `site-packages\matplotlib\mpl-data` 目录下找到 `matplotlibrc` 文件，并修改如下两项即可

```
font.sans-serif     : SimHei, DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
axes.unicode_minus  : False

```

我们还可以改变折线的样式、颜色等，通过示例来看一下。

```
from matplotlib import pyplot as plt

x = range(1, 7)
y = [13, 15, 14, 16, 15, 17]
'''
figsize：设置图片的宽、高，单位为英寸
dpi：设置分辨率
'''
plt.figure(figsize=(8, 5), dpi=80)
plt.title('折线图')
plt.xlabel('x 轴')
plt.ylabel('y 轴')
'''
color：颜色
linewidth：线的宽度
marker：折点样式
linestyle：线的样式，主要包括：'-'、'--'、'-.'、':'
'''
plt.plot(x, y, color='red', marker='o', linewidth='1', linestyle='--')
# 保存
# plt.savefig('test.png')
plt.show()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200314134118963.PNG?#pic" alt="" width="500">

##### 2.1.2 多线

有时候我们可能存在多个指标对比的情况，也就是需要在一个图中绘制多条折线，比如：我们要了解张三、李四随着年龄增长体重的变化情况，示例如下所示：

```
from matplotlib import pyplot as plt

x = range(15, 25)
y1 = [50, 55, 58, 65, 70, 68, 70, 72, 75, 70]
y2 = [52, 53, 60, 63, 65, 68, 75, 80, 85, 72]
plt.figure(figsize=(10, 6), dpi=80)
plt.title('体重年龄折线图')
plt.xlabel('年龄（岁）')
plt.ylabel('体重（kg）')
plt.plot(x, y1, color='red', label='张三')
plt.plot(x, y2, color='blue', label='李四')
# 添加网格，alpha 为透明度
plt.grid(alpha=0.5)
# 添加图例
plt.legend(loc='upper right')
plt.show()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200314135941892.PNG?#pic" alt="" width="500">

##### 2.1.3 子图

Matplotlib 可以实现在一张图中绘制多个子图，我们通过示例来看一下。

```
from matplotlib import pyplot as plt
import numpy as np

a = np.arange(1, 30)
# 划分子图
fig, axs = plt.subplots(2, 2)
# 绘制子图
axs1 = axs[0, 0]
axs2 = axs[0, 1]
axs3 = axs[1, 0]
axs4 = axs[1, 1]
axs1.plot(a, a)
axs2.plot(a, np.sin(a))
axs3.plot(a, np.log(a))
axs4.plot(a, a ** 2)
plt.show()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200314144059229.PNG?#pic" alt="" width="500">

#### 2.2 散点图

散点图表示因变量随自变量而变化的大致趋势，我们通过示例来具体看一下如何绘制散点图。

```
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 20)
# 生成随机数
y = np.random.randint(0, 20, size=20)
plt.title('散点图')
plt.xlabel('x 轴')
plt.ylabel('y 轴')
plt.plot(x, y, 'ob')
plt.show()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200314150729556.PNG?#pic" alt="" width="500">

#### 2.3 直方图

直方图也被称为质量分布图，主要用来表示数据的分布情况，我们通过示例来看一下如何绘制直方图。

```
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数
d1 = np.random.randn(5000)
d2 = np.random.randn(4000)
'''
bins：直方图条目数
alpha：透明度
label：图例名
'''
plt.hist(d1, bins=50, label = 'label1', alpha=0.8)
plt.hist(d2, bins=50, label = 'label2', alpha=0.5)
plt.grid(alpha=0.3)
plt.title('直方图')
plt.xlabel('x 轴')
plt.ylabel('y 轴')
# 显示图例
plt.legend()
plt.show()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200314162827556.PNG?#pic" alt="" width="500">

#### 2.4 条形图

条形图宽度相同，用高度或长短来表示数据多少，它可以横置或纵置。

##### 2.4.1 纵置

首先，我们来看一下如何绘制纵向条形图，以学生成绩为例，看一下具体实现。

```
import matplotlib.pyplot as plt
import numpy as np

arr = np.arange(4)
x = ['张三', '李四', '王五', '赵六']
y = [77, 79, 70, 70]
'''
width：长条形宽度
label：图例名
'''
rects = plt.bar(arr, y, width=0.3, label='语文')
'''
参数1：中点坐标
参数2：显示值
'''
plt.xticks([idx for idx in range(len(x))], x)
plt.title('学生成绩条形图')
plt.xlabel('姓名')
plt.ylabel('成绩')
plt.legend()
# 在条形图上加标注
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
plt.show()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200314180430239.PNG?#pic" alt="" width="500">

##### 2.4.2 横置

我们接着再通过示例来看一下如何绘制横向条形图。

```
import matplotlib.pyplot as plt
import numpy as np

arr = np.arange(4)
y = ['张三', '李四', '王五', '赵六']
x = [88, 79, 70, 66]
plt.barh(range(4), x, 0.4, label='语文')
plt.yticks(range(4), y)
plt.xlabel('成绩')
plt.ylabel('姓名')
plt.title('学生成绩条形图')
plt.legend(loc='upper right')
for x, y in enumerate(x):
    plt.text(y + 0.2, x - 0.1, '%s' % y)
plt.show()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200314183020740.PNG?pic" alt="" width="500">

##### 2.4.3 多条

最后，我们来看一下一个学生要同时显示语文和数学两门成绩时，如何通过 Matplotlib 来绘制条形图。

```
import matplotlib.pyplot as plt
import numpy as np

arr = np.arange(4)
x = ['张三', '李四', '王五', '赵六']
y1 = [88, 75, 77, 66]
y2 = [77, 79, 70, 70]
'''
width：长条形宽度
label：图例名
'''
rects1 = plt.bar(arr, y1, width=0.3, label='语文')
rects2 = plt.bar(arr + 0.3, y2, width=0.3, label='数学')
'''
参数1：中点坐标
参数2：显示值
参数3：间距
'''
plt.xticks([idx + 0.15 for idx in range(len(x))], x, rotation=10)
plt.title('学生成绩条形图')
plt.xlabel('姓名')
plt.ylabel('成绩')
plt.legend()
# 编辑文本
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
plt.show()

```

看一下效果：

<img src="https://img-blog.csdnimg.cn/20200314174330789.PNG?#pic" alt="" width="500">

#### 2.5 饼图

饼图显示一个数据系列，我们通过示例来看一下如何绘制饼图。

```
import matplotlib.pyplot as plt

label_list = ['第一部分', '第二部分', '第三部分']
size = [50, 30, 20]
# 各部分颜色
color = ['red', 'green', 'blue']
# 各部分突出值
explode = [0, 0.1, 0]
'''
explode：设置各部分突出
label：设置图例显示内容
labeldistance：设置图例内容距圆心位置
autopct：设置圆里面文本
shadow：设置是否有阴影
startangle：起始角度，默认从 0 开始逆时针转
pctdistance：设置圆内文本距圆心距离
l_text：圆内部文本
p_text：圆外部文本
'''
patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1, autopct="%1.1f%%", shadow=False, startangle=90, pctdistance=0.6)
# 设置横轴和纵轴大小相等，这样饼才是圆的
plt.axis('equal')
plt.legend(loc='upper left')
plt.show()

```

看一下效果： <img src="https://img-blog.csdnimg.cn/20200314194636115.PNG?#pic" alt="" width="500">

<img src="https://img-blog.csdnimg.cn/20200215093746977.png#pic_center" alt="" width="500">
