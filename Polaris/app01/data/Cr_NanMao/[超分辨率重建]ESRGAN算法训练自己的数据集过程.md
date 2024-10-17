
--- 
title:  [超分辨率重建]ESRGAN算法训练自己的数据集过程 
tags: []
categories: [] 

---
### 一、下载数据集及项目包

#### 1. 数据集

1.1 文件夹框架的介绍，如下图所示：主要有train和val，分别有高清（HR）和低清（LR）的图像。

<img alt="49fba6c5a72c46f783c38d026d9c9fea.png" src="https://img-blog.csdnimg.cn/direct/49fba6c5a72c46f783c38d026d9c9fea.png">

1.2 原图先通过分割尺寸的脚本先将数据集图片处理成两个相同的图像组（HR和LR）。

如训练x4的ESRGAN模型，那么我们需要将HR的图像尺寸与LR的图像尺寸比例是4:1。在我的训练中，我将HR的图像尺寸分割成了480x480，LR的图像分割成了120x120。如下图所示。

<img alt="02d7f278c58a4028b9556e4893f2daf2.png" src="https://img-blog.csdnimg.cn/direct/02d7f278c58a4028b9556e4893f2daf2.png"><img alt="2b2b4900214e49bd8927a05416e27963.png" src="https://img-blog.csdnimg.cn/direct/2b2b4900214e49bd8927a05416e27963.png">

随后将分割好的图像按照train和val的分类，分成如1.1图中的文件结构。



#### 2.  项目包

项目包下载链接：



### 二、训练ESRGAN

ESRGAN模型包括生成模型的训练和判别模型的训练。

#### 2.1 配置RRDBNet_train.py（生成模型）的参数及训练

2.1.1 训练的图像路径设置：dataroot_gt为HR图像的路径、dataroot_lq为LR图像的路径。

<img alt="b4135407eb394e5e88c0f6b7a9bbfe74.png" src="https://img-blog.csdnimg.cn/direct/b4135407eb394e5e88c0f6b7a9bbfe74.png">

2.1.2 batch_size_per_gpu为batchsize的设置，根据显存大小相应设置，显存越大可以设置的值越大，但是训练时间也会增大。

<img alt="b85607b6675943be8333ade0973e0958.png" src="https://img-blog.csdnimg.cn/direct/b85607b6675943be8333ade0973e0958.png">

2.1.3 val的数据集路径设置，dataroot_gt为HR的图像路径、dataroot_lq为LR图像的路径。

<img alt="e9aaf763718546b691fc73f7833abb25.png" src="https://img-blog.csdnimg.cn/direct/e9aaf763718546b691fc73f7833abb25.png">

2.1.4 训练迭代次数的设置，可以设置到10万或者更大

<img alt="d8fa66ce5b8549a5bda098c5096119d2.png" src="https://img-blog.csdnimg.cn/direct/d8fa66ce5b8549a5bda098c5096119d2.png">

2.1.5 训练结果指标的计算psnr和ssim。val_freq参数为保存结果的频率。下图中我的设置为1e3即1000轮保存一次。

<img alt="2ec083981275409aad6132abac2262e4.png" src="https://img-blog.csdnimg.cn/direct/2ec083981275409aad6132abac2262e4.png">

2.1.6 保存训练权重的频率设置。下图中我的设置为1e3，即为1000次保存一次训练权重。

<img alt="d1c49d2ca9794621996439725959ccca.png" src="https://img-blog.csdnimg.cn/direct/d1c49d2ca9794621996439725959ccca.png">

2.1.7 RRDBNet_train.py的训练

```
python basicsr/train.py -opt options\train\ESRGAN\train_RRDBNet_PSNR_x4.yml
```

#### 2.2 配置ESRGAN_train.py（判别模型）的参数及训练

2.2.1 ESRGAN_train.py的参数设置

ESRGAN_train.py的参数设置与RRDBNet_train.py相同，但是多了一个pretrain_network_g参数的设置，即填RRDBNet_train.py训练完以后最好的那次权重路径。

<img alt="f460f1cecc8c4956b0bd42975f900b53.png" src="https://img-blog.csdnimg.cn/direct/f460f1cecc8c4956b0bd42975f900b53.png">

2.2.2 ESRGAN_train.py的训练

```
python basicsr/train.py -opt options\train\ESRGAN\train_RRDBNet_PSNR_x4.yml
```

### 三、测试

#### 3.1 测试图片路径的设置

包括HR和LR的路径，分别为dataroot_gt和dataroot_lq。

<img alt="2a76c61344ac460ea021ebc7c57a2f35.png" src="https://img-blog.csdnimg.cn/direct/2a76c61344ac460ea021ebc7c57a2f35.png">

#### 3.2 ESRGAN模型权重的路径导入

在pretrain_network_g参数中导入ESRGAN模型训练完后生成的权重路径。

<img alt="6fa8fc39d6164d3183992b8b9806273f.png" src="https://img-blog.csdnimg.cn/direct/6fa8fc39d6164d3183992b8b9806273f.png">



### 四、训练中断后，继续训练

只需要在训练代码后加上--auto_resume

```
python basicsr/train.py -opt options\train\ESRGAN\train_RRDBNet_PSNR_x4.yml --auto_resume
```





------------------     今天不学习，明天变垃圾。    ---------------------




