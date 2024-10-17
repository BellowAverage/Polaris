
--- 
title:  图像超分经典网络 SRGAN精确解析 
tags: []
categories: [] 

---
**SRGAN 核心思想**

早期超分辨率方法的优化目标都是降低低清图像和高清图像之间的均方误差。降低均方误差，确实让增强图像和原高清图像的相似度更高。但是，图像的相似度指标高并不能代表图像的增强质量就很高。

为什么 SRGAN 的增强结果那么清楚呢？这是因为 SRGAN 使用了一套新的优化目标。SRGAN 使用的损失函数既包括了** GAN 误差，也包括了感知误差**。这套新的优化目标能够让网络生成看起来更清楚的图片，而不仅仅是和原高清图像相似度更高的图片。

#### 基于 GAN 的超分辨率网络

如前文所述，以优化**均方误差为目标的超分辨率模型难以复原图像的细节**。其实，超分辨率任务和图像生成任务类似，都需要一个“老师”来指导优化目标。SRGAN 把 GAN 框架运用到了超分辨率任务上。原来的生成器 G 随机生成图像，现在用来输出高清图像；原来的判定器 D 用来判定图像是否属于某数据集，现在 D 用来判断一幅图像是否是高清图像。

具体来说，相比基础的 GAN，在 SRGAN 中， D 的真图输入是高清图像 IHR 。而 G 的输入从随机噪声 z 变成了高清图像退化后的低清图像 ILR 。这样，$G$就不是在随机生成图像，而是在根据一幅低清图像生成一幅高清图像了。

借助 GAN 的架构，SRGAN 能够利用 D 指导高清图像生成。但是，超分辨率任务毕竟和图像生成任务有一些区别，不能只用这种对抗误差来约束网络。因此，除了使用对抗误差外，SRGAN 还使用了一种**内容误差。这种内容误差用于让低清图片和高清图片的内容对齐**，起到了和原均方误差一样的作用。

#### 基于感知的内容误差

在介绍 SRGAN 的内容误差之前，需要对“内容误差”和“感知误差”这两个名词做一个澄清。在 SRGAN 的原文章中，作者把内容误差和对抗误差之和叫做感知误差。但是，后续的大部分文献只把这种内容误差叫做感知误差，不会把内容误差和对抗误差放在一起称呼。在后文中，我也会用“感知误差”来指代 SRGAN 中的“内容误差”。

在深度卷积神经网络（CNN）火起来后，人们开始研究为什么 CNN 能够和人类一样识别出图像。经实验，人们发现两幅图像经 VGG（一个经典的 CNN）的某些中间层的输出越相似，两幅图像从观感上也越相似。这种相似度并不是基于某种数学指标，而是和人的感知非常类似。

VGG 的这种“感知性”被运用在了风格迁移等任务上。也有人考虑把这种感知上的误差运用到超分辨率任务上，并取得了不错的结果。

SRGAN 也使用了这种感知误差，以取代之前常常使用的逐像素均方误差。这种感知误差的计算方法如下：VGG 有很多中间层，用于计算感知误差的中间层 i 是可调的。假如我们用 ϕi(I) 表示图像 I 经 VGG 的第 i 层的中间输出结果， ϕi(I)x,y 表示中间输出结果在坐标 (x,y) 处的值，则感知误差的公式如下：

<img alt="" height="54" src="https://img-blog.csdnimg.cn/a82fc3f2bf2542e2bd2d960aede29eeb.png" width="541">

直观上解释这个公式，就是先把高清图像 IHR 送入 VGG，再把高清图像退化出来的低清图像 ILR 送入生成器，并把生成器的输出 G(ILR) 也送入 VGG。两幅图片经 VGG 第 i 层生成的中间结果的逐像素均方误差，就是感知误差。

算上之前的对抗误差，一个图像超分辨率网络的总误差如下：

LSR=Lp+wLG

这里的 w 用于调整两个误差的相对权重，原论文使用 w=10−3 。

** 生成网络的构建**

<img alt="" height="289" src="https://img-blog.csdnimg.cn/e0941431ef2046ea8d485b6a39272a5e.png" width="954">

**生成网络的构成如上图所示**，生成网络的作用是输入一张低分辨率图片，生成高分辨率图片。：

**SRGAN的生成网络由三个部分组成。 1、低分辨率图像进入后会经过一个卷积+RELU函数。 2、然后经过B个残差网络结构，每个残差结构都包含两个卷积+标准化+RELU，还有一个残差边。 3、然后进入上采样部分，在经过两次上采样后，原图的高宽变为原来的4倍，实现分辨率的提升。**

**前两个部分用于特征提取，第三部分用于提高分辨率。**

```
import math
import torch
from torch import nn

class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(channels, channels, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.prelu = nn.PReLU(channels)
        self.conv2 = nn.Conv2d(channels, channels, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)

    def forward(self, x):
        short_cut = x
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.prelu(x)

        x = self.conv2(x)
        x = self.bn2(x)

        return x + short_cut

class UpsampleBLock(nn.Module):
    def __init__(self, in_channels, up_scale):
        super(UpsampleBLock, self).__init__()
        self.conv = nn.Conv2d(in_channels, in_channels * up_scale ** 2, kernel_size=3, padding=1)
        self.pixel_shuffle = nn.PixelShuffle(up_scale)
        self.prelu = nn.PReLU(in_channels)

    def forward(self, x):
        x = self.conv(x)
        x = self.pixel_shuffle(x)
        x = self.prelu(x)
        return x

class Generator(nn.Module):
    def __init__(self, scale_factor, num_residual=16):
        upsample_block_num = int(math.log(scale_factor, 2))

        super(Generator, self).__init__()

        self.block_in = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=9, padding=4),
            nn.PReLU(64)
        )

        self.blocks = []
        for _ in range(num_residual):
            self.blocks.append(ResidualBlock(64))
        self.blocks = nn.Sequential(*self.blocks)
        
        self.block_out = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64)
        )

        self.upsample = [UpsampleBLock(64, 2) for _ in range(upsample_block_num)]
        self.upsample.append(nn.Conv2d(64, 3, kernel_size=9, padding=4))
        self.upsample = nn.Sequential(*self.upsample)

    def forward(self, x):
        x = self.block_in(x)
        short_cut = x
        x = self.blocks(x)
        x = self.block_out(x)

        upsample = self.upsample(x + short_cut)
        return torch.tanh(upsample)

```

** 判别网络的构建**

<img alt="" height="215" src="https://img-blog.csdnimg.cn/451fc66e93614ae2998fc122a4f9328e.png" width="942">

**判别网络的构成如上图所示**：

S**RGAN的判别网络由不断重复的 卷积+LeakyRELU和标准化 组成。 对于判断网络来讲，它的目的是判断输入图片的真假，它的输入是图片，输出是判断结果。**

**判断结果处于0-1之间，利用接近1代表判断为真图片，接近0代表判断为假图片。**

**判断网络的构建和普通卷积网络差距不大，都是不断的卷积对图片进行下采用，在多次卷积后，最终接一次全连接判断结果**。  

```
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.LeakyReLU(0.2),

            nn.Conv2d(64, 64, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),

            nn.Conv2d(128, 128, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),

            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2),

            nn.Conv2d(256, 256, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2),

            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(0.2),

            nn.Conv2d(512, 512, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(0.2),

            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(512, 1024, kernel_size=1),
            nn.LeakyReLU(0.2),
            nn.Conv2d(1024, 1, kernel_size=1)
        )

    def forward(self, x):
        batch_size = x.size(0)
        return torch.sigmoid(self.net(x).view(batch_size))

```

**训练思路****SRGAN的训练可以分为生成器训练和判别器训练： 每一个step中一般先训练判别器，然后训练生成器。**

**一、判别器的训练 在训练判别器的时候我们希望判别器可以判断输入图片的真伪，因此我们的输入就是真图片、假图片和它们对应的标签。**

**因此判别器的训练步骤如下：**

**1、随机选取batch_size个真实高分辨率图片。 2、利用resize后的低分辨率图片，传入到Generator中生成batch_size个虚假高分辨率图片。 3、真实图片的label为1，虚假图片的label为0，将真实图片和虚假图片当作训练集传入到Discriminator中进行训练。**

**二、生成器的训练 在训练生成器的时候我们希望生成器可以生成极为真实的假图片。因此我们在训练生成器需要知道判别器认为什么图片是真图片。**

**因此生成器的训练步骤如下：**

**1、将低分辨率图像传入生成模型，得到虚假高分辨率图像，将虚假高分辨率图像获得判别结果与1进行对比得到loss。（与1对比的意思是，让生成器根据判别器判别的结果进行训练）。2、将真实高分辨率图像和虚假高分辨率图像传入VGG网络，获得两个图像的特征，通过这两个图像的特征进行比较获得loss**

  
