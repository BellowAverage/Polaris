
--- 
title:  C#联合Halcon深度学习源代码分享1 预处理图像2图像识别测试3误差分析（含导入步骤文档，含中文注释） （附源码链接） 
tags: []
categories: [] 

---


#### C#联合Halcon深度学习源代码分享
- <ul><li>- <ul><li>- - - - - - 


### 1 预处理图像

#### 1.1 选择图像目录

所选目录可以是同时包含训练图像和测试图像的主目录,也可以是训练图像目录或测试图像目录,优先选择主目录.如本例提供图片选择mnist_images、Train_images或Test_images目录（不知道本例图片在哪的请先将“mnist_images.rar”解压后使用）. 如果使用其它图像，需要目录格式与本例一致.

#### 1.2 预处理图像

在进行此步图像预处理时，如果使用其它图像，可以先对图像进行裁剪、旋转、翻转或滤波等普通图像处理,然后再使用深度学习算法处理图像使其能够用于训练.参考Halcon算子描述preprocess_dl_classifier_images. 预处理后的数据会自动保存在mnist_images\Preprocessed_images文件夹内.如果提示已有预处理好的数据，可以跳过此步直接开始训练，也可以选择删除已有数据重新预处理图像. <img src="https://img-blog.csdnimg.cn/a40fe4b3b0684ce9a54c3a799c400f49.png" alt="在这里插入图片描述">

### 2 训练分类器

#### 2.1 参数设置

建议使用不同参数设置多次进行训练，了解不同参数设置对训练的影响，可以找到更好的训练参数设置. 注意：BatchSize太大容易导致显存溢出，太小可能不收敛；NumEpochs训练次数越多需要时间越长；LearningRate学习率太大收敛速度快但可能会陷入局部最优，学习率太小收敛速度慢，所需训练次数多；TrainingPercent训练数据太少可能会过拟合；ValidationPercent用于验证的数据比例. 学习率变化曲线表达公式：LearningRate(Epoch) = InitialLearningRate * Math.Pow(LearningRateStepRatio , Math.Floor(Epoch / LearningRateStepEveryNthEpoch)); <img src="https://img-blog.csdnimg.cn/4c950177564c49abaae325deddf7ad74.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/97cf35059eb44193b5565a63fb5fcb05.png" alt="在这里插入图片描述">

#### 2.3 保存分类器

训练完成会自动保存训练模型结果，训练模型默认保存名称为"classifier+图像文件夹名称.hdl"，默认保存目录为当前程序运行目录，点击此按钮可以手动另存到其它地方，分类器扩展名应为.hdl

#### 2.4 误差分析

以验证数据集计算训练模型的预测值与实际值得差异，生成混淆矩阵显示.可以分析哪类数据容易被识别错误. <img src="https://img-blog.csdnimg.cn/9a846774feba4b2ea62e831c5b1d639b.png" alt="在这里插入图片描述">

### 3 图像识别测试

#### 3.1 读取分类器

如果已有训练好的分类器，可以不进行前面1、2两步，直接读取已训练好的分类器进行测试.如果刚刚完成了分类器训练，此步也可以不操作，程序会默认将前面训练的结果用于测试.

#### 3.2 测试分类器

测试图像可以手动选择新图像测试，也可以随机从测试图片文件夹中自动选择图片；注意，测试图像也需要使用训练模型时相同的深度学习算法处理预处理图像后再测试. <img src="https://img-blog.csdnimg.cn/74e2fe9c6a8d4edbaa122f1f1d7672ec.png" alt="在这里插入图片描述"> 除了本例图像外，还可以使用其他图像集进行训练和测试 <img src="https://img-blog.csdnimg.cn/67390cf803634fe5a1837b8aa22c0268.png" alt="在这里插入图片描述">


