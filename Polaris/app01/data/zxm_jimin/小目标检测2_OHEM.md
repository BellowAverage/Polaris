
--- 
title:  小目标检测2_OHEM 
tags: []
categories: [] 

---
主要参考：

有参考很多文章与博客，有的可能忘记放出处了，侵权请联系，马上修改~



#### 文章目录
- - - <ul><li>


## Online Hard-Example Mining（在线难例挖掘）

RPN网络（两阶段网络中，使用区域提议网络RPN在产生目标区域建议框）中目标可能被很多框标记，这些框中有的包含了整个目标；**有的框可能只包含不完全的目标，这类框是错的，可以将其判定为难例。** 通过不断被难例训练就可以使网络具有更好的鲁棒性。

通常，每个图像随机选择256个ROI（这个应该是可以指定的），一些作为前景（目标），一些作为背景。

在OHEM方法中，将传统的ROI的随机选择替换为基于其损失值的选择。在排序前要进行 NMS非极大抑制，区域根据其loss损失值进行排序，只有足够高的区域才会传递给分类学习模块。

这确保了对网络错误最多的样本（困难的样本）的学习，分别对背景和前景对象进行选择，以确保在每个梯度下降步骤中有足够数量的正样本和负样本。

## 网络

<img src="https://img-blog.csdnimg.cn/2ef3531dbde647718b492c084c132609.png" alt="在这里插入图片描述"> OHEM中有两组ROI Network，其中 **(a)是绿色** 是一个可读(read-only)的ROI Network，每次只读取权重后进行forward，不参与反向传播和梯度更新

**(b)是红色** 一个正常功能的ROI Network

对于给定图像，在(a)可读ROI网络 中会对所有的ROI区域计算loss，loss的大小可以反映难易程度。随后会对loss进行排序，选择前batch size个样本送入(b)可读可写的 ROI 网络中，进行执行前向计算和反向传播更新网络。

### OHEM和Focal loss

OHEM和Focal loss为了解决类间差别大 都做了两件事： 一是正负样本的平衡 二是难例挖掘

**OHEM**本身用在了一个**two-stage**的模型上，那么正负样本就是可控的，OHEM做的事情是难例挖掘的过程；

**Focal loss**应用在**one-stage**模型上，无论如何正负样本都不能自由组合，所以只能靠最后计算损失的时候抑制负样本，抑制简单样本，挖掘难例。 Focal loss有两个部分，一个是平衡交叉熵系数 和Focal loss新增的系数 。 <img src="https://img-blog.csdnimg.cn/1b58d6445458498cbbec90d6f9fc7bce.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/838b70ac04c949cba5cd6c59f82f9f39.png" alt="在这里插入图片描述"> 关于Focal loss的详细结束可以移步我其他的文章。

<img src="https://img-blog.csdnimg.cn/52a92b0608cc4d9299520187dde77ed5.jpeg#pic_center" alt="在这里插入图片描述" width="30%">
