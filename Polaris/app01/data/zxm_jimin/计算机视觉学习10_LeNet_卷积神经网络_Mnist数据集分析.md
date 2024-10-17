
--- 
title:  计算机视觉学习10_LeNet_卷积神经网络_Mnist数据集分析 
tags: []
categories: [] 

---


#### 文章目录
- - - - - - 


## 原理部分

卷积神经网络参考：https://my.oschina.net/u/876354/blog/1620906 LeNet神经网络参考：https://my.oschina.net/u/876354/blog/1632862 **1、局部感知** 人类对外界的认知一般是从局部到全局、从片面到全面，类似的，在机器识别图像时也没有必要把整张图像按像素全部都连接到神经网络中，在图像中也是局部周边的像素联系比较紧密，而距离较远的像素则相关性较弱，因此可以采用局部连接的模式（将图像分块连接，这样能大大减少模型的参数），如下图所示： <img src="https://img-blog.csdnimg.cn/20190602194706467.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **2、参数（权值）共享** 每张自然图像（人物、山水、建筑等）都有其固有特性，也就是说，图像其中一部分的统计特性与其它部分是接近的。这也意味着这一部分学习的特征也能用在另一部分上，能使用同样的学习特征。因此，在局部连接中隐藏层的每一个神经元连接的局部图像的权值参数（例如5×5），将这些权值参数共享给其它剩下的神经元使用，那么此时不管隐藏层有多少个神经元，需要训练的参数就是这个局部图像的权限参数（例如5×5），也就是卷积核的大小，这样大大减少了训练参数。如下图 <img src="https://img-blog.csdnimg.cn/20190602194613773.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**3、池化** 随着模型网络不断加深，卷积核越来越多，要训练的参数还是很多，而且直接拿卷积核提取的特征直接训练也容易出现过拟合的现象。回想一下，之所以对图像使用卷积提取特征是因为图像具有一种“静态性”的属性，因此，一个很自然的想法就是对不同位置区域提取出有代表性的特征（进行聚合统计，例如最大值、平均值等），这种聚合的操作就叫做池化，池化的过程通常也被称为特征映射的过程（特征降维），如下图： <img src="https://img-blog.csdnimg.cn/20190602194639185.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## LeNet5

回顾了卷积神经网络（CNN）上面的三个特点后，下面来介绍一下CNN的经典模型：手写字体识别模型**LeNet5**。 LeNet5诞生于1994年，是最早的卷积神经网络之一， 由Yann LeCun完成，推动了深度学习领域的发展。在那时候，没有GPU帮助训练模型，甚至CPU的速度也很慢，因此，LeNet5通过巧妙的设计，利用卷积、参数共享、池化等操作提取特征，避免了大量的计算成本，最后再使用全连接神经网络进行分类识别，这个网络也是最近大量神经网络架构的起点，给这个领域带来了许多灵感。 LeNet5的网络结构示意图如下所示： <img src="https://img-blog.csdnimg.cn/20190602200234306.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> LeNet5由7层CNN（不包含输入层）组成，上图中输入的原始图像大小是32×32像素，卷积层用Ci表示，子采样层（pooling，池化）用Si表示，全连接层用Fi表示。下面逐层介绍其作用和示意图上方的数字含义。

<img src="https://img-blog.csdnimg.cn/20200201115201217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**1、C1层（卷积层）：6@28×28** 该层使用了6个卷积核，每个卷积核的大小为5×5，这样就得到了6个feature map（特征图）。 （1）特征图大小 每个卷积核（5×5）与原始的输入图像（32×32）进行卷积，这样得到的feature map（特征图）大小为（32-5+1）×（32-5+1）= 28×28 卷积过程如下图所示： <img src="https://img-blog.csdnimg.cn/20190602195109952.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 卷积核与输入图像按卷积核大小逐个区域进行匹配计算，匹配后原始输入图像的尺寸将变小，因为边缘部分卷积核无法越出界，只能匹配一次，如上图，匹配计算后的尺寸变为Cr×Cc=（Ir-Kr+1）×（Ic-Kc+1），其中Cr、Cc，Ir、Ic，Kr、Kc分别表示卷积后结果图像、输入图像、卷积核的行列大小。 （2）参数个数 由于参数（权值）共享的原因，对于同个卷积核每个神经元均使用相同的参数，因此，参数个数为（5×5+1）×6= 156，其中5×5为卷积核参数，1为偏置参数 （3）连接数 卷积后的图像大小为28×28，因此每个特征图有28×28个神经元，每个卷积核参数为（5×5+1）×6，因此，该层的连接数为（5×5+1）×6×28×28=122304 **2、S2层（下采样层，也称池化层）：6@14×14** （1）特征图大小 这一层主要是做池化或者特征映射（特征降维），池化单元为2×2，因此，6个特征图的大小经池化后即变为14×14。回顾本文刚开始讲到的池化操作，池化单元之间没有重叠，在池化区域内进行聚合统计后得到新的特征值，因此经2×2池化后，每两行两列重新算出一个特征值出来，相当于图像大小减半，因此卷积后的28×28图像经2×2池化后就变为14×14。 这一层的计算过程是：2×2 单元里的值相加，然后再乘以训练参数w，再加上一个偏置参数b（每一个特征图共享相同的w和b)，然后取sigmoid值（S函数：0-1区间），作为对应的该单元的值。卷积操作与池化的示意图如下： <img src="https://img-blog.csdnimg.cn/20190602195441428.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> （2）参数个数 S2层由于每个特征图都共享相同的w和b这两个参数，因此需要2×6=12个参数 （3）连接数 下采样之后的图像大小为14×14，因此S2层的每个特征图有14×14个神经元，每个池化单元连接数为2×2+1（1为偏置量），因此，该层的连接数为（2×2+1）×14×14×6 = 5880

注： 关于池化层与下采样层，个人理解，就是一个东西，两个名字而已。 参考：https://blog.csdn.net/qq_41621362/article/details/88766768

**位置** 池化或子采样层通常紧跟在CNN中的卷积层之后。

**常用方法** 最大值池化（max-pooling）：对邻域内特征点取最大值。 平均值池化（mean-pooling）：对邻域内特征点求平均。 **作用** 降维，减少网络要学习的参数数量。 防止过拟合。 可以扩大感知野。 可以实现不变性:平移不变性,旋转不变性,尺度不变性。

**3、C3层（卷积层）：16@10×10** C3层有16个卷积核，卷积模板大小为5×5。 （1）特征图大小 与C1层的分析类似，C3层的特征图大小为（14-5+1）×（14-5+1）= 10×10 （2）参数个数 需要注意的是，C3与S2并不是全连接而是部分连接，有些是C3连接到S2三层、有些四层、甚至达到6层，通过这种方式提取更多特征，连接的规则如下表所示： <img src="https://img-blog.csdnimg.cn/20190602195615135.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 例如第一列表示C3层的第0个特征图（feature map）只跟S2层的第0、1和2这三个feature maps相连接，计算过程为：用3个卷积模板分别与S2层的3个feature maps进行卷积，然后将卷积的结果相加求和，再加上一个偏置，再取sigmoid得出卷积后对应的feature map了。其它列也是类似（有些是3个卷积模板，有些是4个，有些是6个）。因此，C3层的参数数目为（5×5×3+1）×6 +（5×5×4+1）×9 +5×5×6+1 = 1516 （3）连接数 卷积后的特征图大小为10×10，参数数量为1516，因此连接数为1516×10×10= 151600 **4、S4（下采样层，也称池化层）：16@5×5** （1）特征图大小 与S2的分析类似，池化单元大小为2×2，因此，该层与C3一样共有16个特征图，每个特征图的大小为5×5。 （2）参数数量 与S2的计算类似，所需要参数个数为16×2 = 32 （3）连接数 连接数为（2×2+1）×5×5×16 = 2000 **5、C5层（卷积层）：120** （1）特征图大小 该层有120个卷积核，每个卷积核的大小仍为5×5，因此有120个特征图。由于S4层的大小为5×5，而该层的卷积核大小也是5×5，因此特征图大小为（5-5+1）×（5-5+1）= 1×1。这样该层就刚好变成了全连接，这只是巧合，如果原始输入的图像比较大，则该层就不是全连接了。 （2）参数个数 与前面的分析类似，本层的参数数目为120×（5×5×16+1） = 48120 （3）连接数 由于该层的特征图大小刚好为1×1，因此连接数为48120×1×1=48120 **6、F6层（全连接层）：84** （1）特征图大小 F6层有84个单元，之所以选这个数字的原因是来自于输出层的设计，对应于一个7×12的比特图，如下图所示，-1表示白色，1表示黑色，这样每个符号的比特图的黑白色就对应于一个编码。 <img src="https://img-blog.csdnimg.cn/20190602195654139.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 该层有84个特征图，特征图大小与C5一样都是1×1，与C5层全连接。 （2）参数个数 由于是全连接，参数数量为（120+1）×84=10164。跟经典神经网络一样，F6层计算输入向量和权重向量之间的点积，再加上一个偏置，然后将其传递给sigmoid函数得出结果。 （3）连接数 由于是全连接，连接数与参数数量一样，也是10164。 **7、OUTPUT层（输出层）：10** Output层也是全连接层，共有10个节点，分别代表数字0到9。如果第i个节点的值为0，则表示网络识别的结果是数字i。 （1）特征图大小 该层采用径向基函数（RBF）的网络连接方式，假设x是上一层的输入，y是RBF的输出，则RBF输出的计算方式是： <img src="https://img-blog.csdnimg.cn/20190602195900905." alt="在这里插入图片描述"> 上式中的Wij的值由i的比特图编码确定，i从0到9，j取值从0到7×12-1。RBF输出的值越接近于0，表示当前网络输入的识别结果与字符i越接近。 （2）参数个数 由于是全连接，参数个数为84×10=840 （3）连接数 由于是全连接，连接数与参数个数一样，也是840

通过以上介绍，已经了解了LeNet各层网络的结构、特征图大小、参数数量、连接数量等信息，下图是识别数字3的过程，可对照上面介绍各个层的功能进行一一回顾： <img src="https://img-blog.csdnimg.cn/20190602200050617.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## 数据与实验可视化

Mnist数据集中的数据是这样的（部分截图） <img src="https://img-blog.csdnimg.cn/20190603005636125.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 每个数字都有60K左右张训练图像 每个数字都有10K左右张训练图像 直接训练的结果： <img src="https://img-blog.csdnimg.cn/20190603010142730.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 可以看到正确率还是很高的

我们将（随机抽取的部分样本中）识别错误的图片单独保存下来 文件名的第一个数字为模型匹配的结果

0 <img src="https://img-blog.csdnimg.cn/20190603010334570." alt="在这里插入图片描述"> 1 <img src="https://img-blog.csdnimg.cn/20190603010535333.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2019060301060017.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 2 <img src="https://img-blog.csdnimg.cn/20190603010623977.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 3 <img src="https://img-blog.csdnimg.cn/20190603010654288.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 4 <img src="https://img-blog.csdnimg.cn/20190603010722475.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 5 <img src="https://img-blog.csdnimg.cn/20190603010753516.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190603010807854.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 6 <img src="https://img-blog.csdnimg.cn/20190603010831692." alt="在这里插入图片描述"> 7 <img src="https://img-blog.csdnimg.cn/20190603010859271.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 8 <img src="https://img-blog.csdnimg.cn/20190603010924227." alt="在这里插入图片描述"> 9 <img src="https://img-blog.csdnimg.cn/20190603010950948.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## 匹配结果分析

我个人认为最难匹配的反而是轮廓相似的数字，特别是有局部轮廓相似

**以数字8举例：** <img src="https://img-blog.csdnimg.cn/20190603011735255." alt="在这里插入图片描述"> 这些数字都被匹配为8 <img src="https://img-blog.csdnimg.cn/20190603011948376.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 圈出的黄色圆圈出，有类似**椭圆**的拐角 圈出的蓝色方框出，有类似的有点**倾斜的直线** 因此它们很容易与8匹配上 在数字1，9中，有倾斜的直线有许多都匹配成了8 <img src="https://img-blog.csdnimg.cn/20190603012240529.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190603012518921.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **以数字3举例：** 这些数字都被匹配为3 <img src="https://img-blog.csdnimg.cn/20190603012918530.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 都是有一个向上拐的尖角，而且其弧度相近

而数字3的错误匹配中 <img src="https://img-blog.csdnimg.cn/20190603013102464.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 有许多向上的尖角不常规，从而导致错误匹配

诸如此类的原因还有很多，没办法全部描述出来

我个人归纳为如下几点：

**1、特征相似，局部特征相似 2、走势相似 3、结构相似**

## 个人数据匹配

<img src="https://img-blog.csdnimg.cn/20190603014007825.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 大部分图片都匹配失败 与上面分析的原因相近。

## 代码节选

```
import tensorflow as tf
import numpy as np
import tkinter as tk
import os
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import filedialog
import time


def creat_windows():
    win = tk.Tk() # 创建窗口
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    ww, wh = 400, 450
    x, y = (sw-ww)/2, (sh-wh)/2
    win.geometry("%dx%d+%d+%d"%(ww, wh, x, y-40)) # 居中放置窗口

    win.title('手写体识别') # 窗口命名

    bg1_open = Image.open("timg.jpg").resize((300, 300))
    bg1 = ImageTk.PhotoImage(bg1_open)
    canvas = tk.Label(win, image=bg1)
    canvas.pack()


    var = tk.StringVar() # 创建变量文字
    var.set('')
    tk.Label(win, textvariable=var, bg='#C1FFC1', font=('宋体', 21), width=20, height=2).pack()

    tk.Button(win, text='选择图片', width=20, height=2, bg='#FF8C00', command=lambda:main(var, canvas), font=('圆体', 10)).pack()
    
    win.mainloop()

def main(var, canvas):

    ip='9'
    L=os.listdir('D:\workspace\\untitled\Mnist手写体训练\Mnist手写体训练\mnist_test\\'+ip)
    print(L)
    global i
    for i in range(0,len(L),15):
        file_path ='D:\workspace\\untitled\Mnist手写体训练\Mnist手写体训练\mnist_test\\'+ip+'\\'+L[i]
        print(L[i])
        bg1_open = Image.open(file_path).resize((28, 28))
        pic = np.array(bg1_open).reshape(784, )
        bg1_resize = bg1_open.resize((300, 300))
        bg1 = ImageTk.PhotoImage(bg1_resize)
        canvas.configure(image=bg1)
        canvas.image = bg1
        init = tf.global_variables_initializer()
        with tf.Session() as sess:
            sess.run(init)
            saver = tf.train.import_meta_graph('save/model.meta')  # 载入模型结构
            saver.restore(sess, 'save/model')  # 载入模型参数
            graph = tf.get_default_graph()  # 加载计算图
            x = graph.get_tensor_by_name("x-input:0")  # 从模型中读取占位符变量
            keep_prob = graph.get_tensor_by_name("keep_prob:0")
            y_conv = graph.get_tensor_by_name("y-pred:0")  # 关键的一句  从模型中读取占位符变量
            prediction = tf.argmax(y_conv, 1)
            predint = prediction.eval(feed_dict={x: [pic], keep_prob: 1.0},
                                      session=sess)  # feed_dict输入数据给placeholder占位符
            answer = str(predint[0])
        var.set("预测的结果是：" + answer)
        if answer!=ip:
            bg1_open.save('D:\workspace\\untitled\Mnist手写体训练\Mnist手写体训练\wrong\\'+ip+'\\'+answer+'_'+str(i)+'.png')





if __name__ == "__main__":
    creat_windows()

```
