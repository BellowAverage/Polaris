
--- 
title:  ESRGAN超分辨重建模型x2和x4训练方法 
tags: []
categories: [] 

---
>  
 **注意：本训练方法是基于我的项目包中的ESRGAN模型，进行步骤说明的！** 
 **（1）项目包下载链接如下：** 
 ESRGAN运行代码项目包： 
 **（2）ESRGAN模型训练步骤教程链接如下：** 
 ESRGAN模型训练教程链接： 


##### 一、训练配置文件修改

打开项目代码包，进入到options/train/ESRGAN路径下，找到train_RRDBNet_PSNR_x4.yml配置文件并打开（x2倍的训练，请打开train_RRDBNet_PSNR_x2.yml）。因为我们将训练x4倍（x2倍）下采样的ESRGAN模型，所以需要将scale设置为4（设置为2）。

<img alt="" height="409" src="https://img-blog.csdnimg.cn/direct/cb05ee7939934257be93d40f785f63a0.png" width="955">

##### 二、 模型架构修改

在项目包basicsr/archs路径下，找到rrdbnet_arch.py脚本并打开，大概在117-119行左右有一个upsample上采样的过程，x4的训练中，需要执行两次上采样（在x2的训练中，需要执行一次上采样），因此，feat需要执行**两次**（执行**一次**，因此需要注释其中一个feat）。

<img alt="" height="443" src="https://img-blog.csdnimg.cn/direct/a25331cfa0834be0ac574d58b3dba660.png" width="1021">

##### 三、x4倍下采样ESRGAN模型训练开始

打开terminal，进入到项目运行包路径下，运行如下命令执行训练：

（1）x4倍训练：

```
python basicsr/train.py -opt I:\BasicSR\options\train\ESRGAN\train_RRDBNet_PSNR_x4.yml
```

（2）x2倍训练：

```
python basicsr/train.py -opt I:\BasicSR\options\train\ESRGAN\train_RRDBNet_PSNR_x2.yml
```



今天不学习，明天变垃圾！！！
