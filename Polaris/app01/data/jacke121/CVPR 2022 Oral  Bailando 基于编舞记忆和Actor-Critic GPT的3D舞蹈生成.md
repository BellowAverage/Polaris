
--- 
title:  CVPR 2022 Oral | Bailando: 基于编舞记忆和Actor-Critic GPT的3D舞蹈生成 
tags: []
categories: [] 

---
**目录**







### 测试结果：

预测有3个步骤，速度比较慢





### 02 提出的方法

 1. 针对舞蹈序列的VQ-VAE和编舞记忆

与之前的方法不同，我们不学习从音频特征到 3D 关键点序列的连续域的直接映射。相反，我们先让神经网络“观看”大量的舞蹈数据，自己从里面“总结”出有意义的舞蹈元素，并且记录下来成为“编舞记忆”。

编舞记忆中，每个元素都是从专业舞蹈中提取的符合空间要求的标准舞姿。具体来说，我们设计了一个针对人体姿态序列的VQ-VAE（Vector Quantized Variational Auto-Encoder）网络，对舞蹈数据的姿态序列进行编码和量化到一个编码本Z中。



<img alt="" height="411" src="https://img-blog.csdnimg.cn/img_convert/7f6df22544614471714c7a9411163bb4.webp?x-oss-process=image/format,png" width="1080">

Z表示VQ-VAE的量化编码本，即“编舞记忆”，其中每一个元素都代表着一个标准的舞姿。为了使舞蹈记忆能涵盖更广泛的舞蹈动作，我们对舞蹈动作的上下身用独立的VQ-VAE进行学习，分别得到上下半身的编码本，并对上下半身进行组合式的拼接。我们还单独学习一个网络分支Dv，用于预测人体关键点的整体位移。

训练VQ-VAE的损失函数分为：



<img alt="" height="73" src="https://img-blog.csdnimg.cn/img_convert/184d10a707c59cf1959c7266e52341df.webp?x-oss-process=image/format,png" width="1080">

其中，重构函数不仅考虑到对关键点位置P的重构，还考虑到对一阶（速度）和二阶（加速度）导数的重构。



<img alt="" height="72" src="https://img-blog.csdnimg.cn/img_convert/a87df7d81be2a8dd510235b9053b1462.webp?x-oss-process=image/format,png" width="1080">

**2. 动作GPT （motion GPT）**

在我们从舞蹈数据中总结出了标准的舞姿库“编舞记忆”后，编舞的任务就变成了对音乐的每一时刻，选择一个合适的舞姿与之对应。这一步我们用到了GPT（Generative Pretrained Transformer）。



<img alt="" height="295" src="https://img-blog.csdnimg.cn/img_convert/5b817b490e658d33e2764fa1f1714d72.png" width="1080">

对于每一时刻t，GPT根据0到t-1时刻的音乐（m）、上半身（u）和下半身（l）信息来预测t时刻的上、下半身舞姿，并对每一个存在编舞记忆中的舞姿计算一个概率。而GPT的学习则是通过对预测的概率与真实动作之间的Cross-Entropy损失函数进行优化。

**3. “演员-评论家”(Actor-Critic)学习**

GPT的训练是直接而有效的。然而，这个框架有一个弊端，即很难向损失函数中加入一些人工定义的正则化项（比如希望让生成的舞蹈更加符合音乐节拍），因为GPT的学习的对象是舞姿在编舞记忆中的编号。

为了解决这个问题，我们采用了一种名为“演员-评论家”的强化学习框架。具体来说，我们把GPT前3层视作一个表示当前状态的“状态网络”，后几层视作一个产生“动作”的“演员网络”，并单独引入一个新的GPT分支作为“评论家网络”。评论家网络的打分和人工设计的奖励函数R，将决定GPT生成的舞蹈是好的（应该鼓励），还是不好的（应该避免），并通过对相应损失函数的优化提升GPT的效果。



<img alt="" height="440" src="https://img-blog.csdnimg.cn/img_convert/65fdac5075c2fef7ebdbe56ce325b0ab.png" width="1080">

### **03 实验结果**

**1. 对比实验**


