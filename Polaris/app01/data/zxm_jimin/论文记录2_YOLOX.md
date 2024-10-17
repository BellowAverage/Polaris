
--- 
title:  论文记录2_YOLOX 
tags: []
categories: [] 

---
**注：此文为阅读笔记，参考了很多论文，博客，如有侵权请联系，我附上原出处。** 文章大部分内容主要来自以下博客： 大佬 Bubbliiiing 的讲解  大佬 霹雳吧啦Wz 的讲解 ；  



#### 文章目录
- - - - - <ul><li>- - - - - - <ul><li>- 


## YOLO X

论文：https://arxiv.org/pdf/2107.08430.pdf github地址：https://github.com/Megvii-BaseDetection/YOLOX 其他大佬自己实现博客：https://blog.csdn.net/weixin_44791964/article/details/120476949?spm=1001.2014.3001.5501

## 创新点

1、主干部分：使用了Focus网络结构，这个结构是在YoloV5里面使用到比较有趣的网络结构，具体操作是在一张图片中每隔一个像素拿到一个值，这个时候获得了四个独立的特征层，然后将四个独立的特征层进行堆叠，此时宽高信息就集中到了通道信息，输入通道扩充了四倍。

2、分类回归层：Decoupled Head，以前版本的Yolo所用的解耦头是一起的，也就是分类和回归在一个1X1卷积里实现，YoloX认为这给网络的识别带来了不利影响。在YoloX中，Yolo Head被分为了两部分，分别实现，最后预测的时候才整合在一起。

3、数据增强：Mosaic数据增强。

4、Anchor Free：不使用先验框。

5、SimOTA ：为不同大小的目标动态匹配正样本。

## 

原论文作者认为，然而，在过去的两年中，目标检测学术界的主要进展集中在anchor-free detectors、dvanced label assignment strategies（高级标签分配）和end-to-end(NMS-free) detectors。这些新技术还没有集成到YOLO系列中，如YOLO V4和YOLO V5。

并且原论文作者可能考虑到YOLO V4和YOLO V5用到许多tricks对anchor-based detectors进行优化，而且不好直接在其基础上进行进一步改进，故选择YOLO V3 作为起点( set YOLOv3-SPP as the default YOLOv3).

并且 1、代码已开源。 2、源码提供了ONNX, TensorRT, NCNN, and Openvino版本，相信能减少很多部署所需要的时间，对工业界相当友好，相信很快就能应用于工业界。

## 网络架构

### Backbone

**DarkNet53** 相比原始的YOLOv3，本论文的YOLOv3 baseline对训练策略做了如下改动： 1.加入EMA权重更新 2.加入cosine lr schedule 3.加入IoU loss 4.加入IoU-aware branch

**CSPDarknet** 此外，YOLOX中还有以YOLO V5的CSPDarknet做为Backbone进行分析 具体可以参考博客： 此大佬有给出详细的网络结构图及代码复现 <img src="https://img-blog.csdnimg.cn/15f77dad75fa468e80de064c36f82cc3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

1、使用了残差网络Residual，CSPDarknet中的残差卷积可以分为两个部分，主干部分是一次1X1的卷积和一次3X3的卷积；残差边部分不做任何处理，直接将主干的输入与输出结合。 残差网络的特点是容易优化，并且能够通过增加相当的深度来提高准确率。其内部的残差块使用了跳跃连接，缓解了在深度神经网络中增加深度带来的梯度消失问题。 <img src="https://img-blog.csdnimg.cn/cb40c780d0524cfc88dcbab60abf315e.png" alt="在这里插入图片描述">

2、使用CSPnet网络结构，CSPnet结构并不算复杂，就是将原来的残差块的堆叠进行了一个拆分，拆成左右两部分：主干部分继续进行原来的残差块的堆叠；另一部分则像一个残差边一样，经过少量处理直接连接到最后。因此<img src="https://img-blog.csdnimg.cn/dfd81aa2fed94aa59ac3069dc76d01e3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 可以认为CSP中存在一个大的残差边。

3、使用了Focus网络结构，这个网络结构是在YoloV5里面使用到的网络结构，具体操作是在一张图片中每隔一个像素拿到一个值，这个时候获得了四个独立的特征层，然后将四个独立的特征层进行堆叠，此时宽高信息就集中到了通道信息，输入通道扩充了四倍。拼接起来的特征层相对于原先的三通道变成了十二个通道。 <img src="https://img-blog.csdnimg.cn/919393986edb4b1397e1253856657428.png" alt="在这里插入图片描述">

4、使用了SiLU激活函数，SiLU是Sigmoid和ReLU的改进版。SiLU具备无上界有下界、平滑、非单调的特性。SiLU在深层模型上的效果优于 ReLU。可以看做是平滑的ReLU激活函数。 <img src="https://img-blog.csdnimg.cn/c720a5d93de44d9d9eee592fbd6d604d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### Neck

**SPP** 使用了SPP结构，通过不同池化核大小的最大池化进行特征提取，提高网络的感受野。在YoloV4中，SPP是用在FPN里面的，在YoloX中，SPP模块被用在了主干特征提取网络中。

YoloX提取多特征层进行目标检测，一共提取三个特征层（类似FPN，具体可以看我上一篇博客）

### Head

**Decoupled head** YoloX中的YoloHead与之前版本的YoloHead不同。 以前版本的Yolo所用的Head是（Cls、Reg、Obj）一起的，也就是分类和回归在一个1X1卷积里实现，认为这给网络的识别带来了不利影响。

YOLO X实验发现这给网络的识别带来了不利影响。故进行两点改进：

①将预测分支解耦极大的改善收敛速度。在YoloX中，Yolo Head被分为了两部分，分别实现，最后预测的时候才整合在一起。

②相比较于非解耦的端到端方式，解耦能带来 **4.2%** AP提升。

<img src="https://img-blog.csdnimg.cn/a231c7737e184895a89aff7f34c44d1d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

对于每一个特征层，我们可以获得**三个预测结果**，分别是：

1、**Reg**(h,w,4)用于判断每一个特征点的回归参数-目标框的坐标信息（x，y，w，h），回归参数调整后可以获得预测框。

2、**Obj**(h,w,1)用于判断每一个特征点是否包含物体（即判断目标框是前景还是背景）。

3、**Cls**(h,w,num_classes)用于判断每一个特征点所包含的物体种类。

将三个预测结果进行堆叠Concat，每个特征层获得的结果为：**Out(h,w,4+1+num_classses)** 前四个参数用于判断每一个特征点的回归参数，回归参数调整后可以获得预测框； 第五个参数用于判断每一个特征点是否包含物体； 最后num_classes个参数用于判断每一个特征点所包含的物体种类。

>  
 https://zhuanlan.zhihu.com/p/441980709 YOLOX论文参考了上述两篇2020CVPR的论文（一篇设计了双头RCNN，将全连接用于分类，卷积用于回归；一篇根据分类和回归在空间维度上不对齐，提出了TSD再空间维度上解耦分类和回归）使用解耦头替换yolov3的耦合的检测头。 上图中对于FPN(特征金字塔网络)得的特征，先用1x1的卷积层将其特征通道降为256，然后在分类和回归两个分支各用两个3x3的卷积层，并在回归分支添加IoU分支。 


<img src="https://img-blog.csdnimg.cn/d74a5a121af94bbaa106e9f44756bd3d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## Strong data augmentation

使用Mosaic和MixUp技术 可以看我上一篇博客，原理差不多。

## Anchor-free

目前，有一些工作表明，anchor-free detectors的性能可以与anchor-based detectors相当。

**anchor的问题：** 参考博客：https://zhuanlan.zhihu.com/p/392221567

①使用anchor时，为了调优模型，需要对数据聚类分析，确定最优锚点，缺乏泛化性。

②anchor机制增加了Head复杂度，增加了每幅图像预测数量（针对coco数据集，yolov3使用416 * 416图像推理， 会产生3 * (13 * 13+26 * 26+52 * 52）* 85=5355个预测结果)。 使用ancho-freer可以**减少调整参数数量**，减少涉及的**使用技巧**

将YOLO 转化成 anchor-free manner 从原有一个特征图预测3组anchor减少成只**预测1组**，直接预测4个值（左上角xy坐标和box高宽）。减少了参数量和GFLOPs（每秒10亿次的浮点运算数），使速度更快，且表现更好。

作者在**正样本**选择方式做过以下几个尝试：

①只将**物体中心点所在的位置认为是正样本**，一个gt最多只会有一个正样本。AP达到42.9%。

②**Multi positives**。直接将中心3 * 3区域都认为是正样本，即从上述策略每个gt有1个正样本增长到9个正样本。且AP提升到45%，已经超越U版yolov3的44.3%AP。

③**SimOTA**

## Multi positives 正样本

在YoloX中，**物体的真实框落在哪些特征点内就由该特征点来预测**。

对于每一个真实框，我们会求取所有特征点与它的空间位置情况。作为正样本的特征点需要满足以下几个特点： 1、特征点落在物体的真实框内。 2、特征点距离物体中心尽量要在一定半径内。

特点1、2保证了属于正样本的特征点会落在物体真实框内部，特征点中心与物体真实框中心要相近。

上面两个条件仅用作正样本的而初步筛选，在YoloX中，我们使用了SimOTA方法进行动态的正样本数量分配。

## SimOTA

先看一下原论文里的效果： <img src="https://img-blog.csdnimg.cn/50632d5c57294ee184cdf523861377fc.png" alt="在这里插入图片描述"> SimOTA不仅减少训练时间，而且避免额外的参数。在YOLOv3的基础上将AP从45.0%提升到47.3%。（但是没有提到YOLOv5）

### OTA

**OTA**(Optimal Transport Assignment) 在目标检测中，有时候经常会出现一些**模棱两可的anchor**。 如下图，即某一个anchor，按照正样本匹配规则，会匹配到两个gt，Retinanet这样基于IoU分配是会把anchor分配给**IoU最大**的gt。

而OTA作者认为，将**模糊的anchor**分配给任何gt或背景都会对其他gt的梯度造成**不利影响**。 因此，对模糊anchor样本的分配是特殊的，除了局部视图之外还需要其他信息。因此，更**好的分配策略**应该摆脱对每个gt对象进行最优分配的惯例，而转向**全局最优**的思想，换句话说，为图像中的所有gt对象找到全局的高置信度分配。（和DeTR中使用使用**匈牙利算法**一对一分配有点类似） <img src="https://img-blog.csdnimg.cn/b2fae7a0dbc2412eb3fb860894512eca.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### Cost代价矩阵

<img src="https://img-blog.csdnimg.cn/6ea34a3ca610407b82c90e7be1bc270b.png" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/b9bed60df7a740d8b3becef91bf9d661.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/34739bdb8932460f90bf131d54d328eb.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5d8ff7bfda764b0cb2516942795b9429.png" alt="在这里插入图片描述"> **Cost代价矩阵**，代表每个真实框和每个特征点之间的代价关系，Cost代价矩阵的目的是**自适应的找到**当前特征点应该去拟合的真实框，重合度越高越需要拟合，分类越准越需要拟合，在一定半径内越需要拟合。

Cost代价矩阵由三个部分组成：

```
cost = (
            pair_wise_cls_loss                     # 1、每个gt和当前特征点预测框的类别预测准确度
            + 3.0 * pair_wise_ious_loss            # 2、每个gt和当前特征点预测框的重合程度
            + 100000.0 * (~is_in_boxes_and_center) # 3、每个gt的中心是否落在了特征点的定半径内
        )

```

<img src="https://img-blog.csdnimg.cn/0fbb60041a7a4a0bb4620d423aefb940.png" alt="在这里插入图片描述">

>  
 每个真实框和当前特征点预测框的重合程度越高，代表这个特征点已经尝试去拟合该真实框了，因此它的Cost代价就会越小。 每个真实框和当前特征点预测框的种类预测准确度越高，也代表这个特征点已经尝试去拟合该真实框了，因此它的Cost代价就会越小。 每个真实框的中心如果落在了特征点的一定半径内，代表这个特征点应该去拟合该真实框，因此它的Cost代价就会越小。 


将每一个预先选到的anchor point（上图中打橙色勾）都去对 每一个gt 做一个cost 计算（上面的代码） 就可以得到cost矩阵 <img src="https://img-blog.csdnimg.cn/818078639c264441b566d6f81ae2174a.png" alt="在这里插入图片描述">

### 动态匹配-正样本

在SimOTA中，不同目标设定不同的正样本数量(dynamic_k)，动态匹配的正样本设置的关键在于如何确定 dynamic_k

>  
 以旷视科技​官方回答中的蚂蚁和西瓜为例子，传统的正样本分配方案常常为同一场景下的西瓜和蚂蚁分配同样的正样本数，那要么蚂蚁有很多低质量的正样本，要么西瓜仅仅只有一两个正样本。对于哪个分配方式都是不合适的。 


以下是大佬们总结的流程：

#### 1、 计算每个gt框和anchor point 的 **IoU矩阵、 cost矩阵**。

<img src="https://img-blog.csdnimg.cn/0f269c5aff454d0a9906f18d74316142.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/70f4c90bd790446eac127bbb51be957a.png" alt="在这里插入图片描述"> **对每个gt 选取 前n_candidate_k 个anchor point**

#### 2、每个gt有 dynamic_ks 个anchor point与之对应（动态分配）

**对每一个gt（每一行）对应的IoU进行求和，然后向下取整 ==&gt; dynamic_ks** 代表每个gt有 dynamic_ks 个anchor point与之对应（动态分配）。 <img src="https://img-blog.csdnimg.cn/f0de1013cf554e959ce591c1c7d3ae26.png" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/fced87fbaf534319b80cda15ccd6353d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/16af8ef5f91f4c7aba0d62b78d914294.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6add55e6322047218b28f7971c9daf7b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/90931b587c894611a5a1cdae0cb4fda0.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d5b557de55da45bdb2bee8377c20faf4.png" alt="在这里插入图片描述"> 根据以上流程就能找到所有的正样本以及正样本对应的GT了，那么剩下的Anchor Point全部归为负样本。

<img src="https://img-blog.csdnimg.cn/b0d737fac0db4d19a24bd974e9bd892a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 损失函数

YoloX的损失由三个部分组成： 1、**Reg部分**，由第三部分可知道每个真实框对应的特征点，获取到每个框对应的特征点后，取出该特征点的预测框，利用真实框和预测框计算IOU损失，作为Reg部分的Loss组成。 2、**Obj部分**，由第三部分可知道每个真实框对应的特征点，所有真实框对应的特征点都是正样本，剩余的特征点均为负样本，根据正负样本和特征点的是否包含物体的预测结果计算交叉熵损失，作为Obj部分的Loss组成。 3、**Cls部分**，由第三部分可知道每个真实框对应的特征点，获取到每个框对应的特征点后，取出该特征点的种类预测结果，根据真实框的种类和特征点的种类预测结果计算交叉熵损失，作为Cls部分的Loss组成。 <img src="https://img-blog.csdnimg.cn/16581b8ea10949ac95f297c957c419f4.png" alt="在这里插入图片描述">

## 实验效果

为了公平比较，选择了300次迭代训练的所有模型。比较了COCO 2017测试开发中不同目标探测器的速度和精度。 <img src="https://img-blog.csdnimg.cn/0849d09013c04ce2bc0cec4270506c13.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

（1）Yolox-Nano Yolox-Nano是Yolox系列最小的结构，网络参数只有0.91M。 （2）Yolox-Tiny （3）Yolox-Darknet53 Yolox-Darknet53是在Yolov3的基础上，进行的改进，也是后面主要介绍的网络结构。 （4）Yolox-s Yolox-s是在Yolov5-s的基础上，进行的改进，也是后面主要介绍的网络结构。 （5）Yolox-m （6）Yolox-l （7）Yolox-x

```
depth_dict = {'nano': 0.33, 'tiny': 0.33, 's' : 0.33, 'm' : 0.67, 'l' : 1.00, 'x' : 1.33,}
width_dict = {'nano': 0.25, 'tiny': 0.375, 's' : 0.50, 'm' : 0.75, 'l' : 1.00, 'x' : 1.25,}

```
