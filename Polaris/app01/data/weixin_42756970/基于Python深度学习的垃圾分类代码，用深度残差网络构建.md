
--- 
title:  基于Python深度学习的垃圾分类代码，用深度残差网络构建 
tags: []
categories: [] 

---
## 垃圾分类

完整代码下载地址：

##### 介绍

这是一个基于深度学习的垃圾分类小工程，用深度残差网络构建

##### 软件架构
1. 使用深度残差网络resnet50作为基石，在后续添加需要的层以适应不同的分类任务1. 模型的训练需要用生成器将数据集循环写入内存，同时图像增强以泛化模型1. 使用不包含网络输出部分的resnet50权重文件进行迁移学习，只训练我们在5个stage后增加的层
##### 安装教程
1. 需要的第三方库主要有tensorflow1.x，keras，opencv，Pillow，scikit-learn，numpy1. 安装方式很简单，打开terminal，例如：pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple1. 数据集与权重文件比较大，所以没有上传1. 如果环境配置方面有问题或者需要数据集与模型权重文件，可以在评论区说明您的问题，我将远程帮助您
##### 使用说明
1. 文件夹theory记录了我在本次深度学习中收获的笔记，与模型训练的控制台打印信息1. 迁移学习需要的初始权重与模型定义文件resnet50.py放在model下1. 训练运行trainNet.py，训练结束会创建models文件夹，并将结果权重garclass.h5写入该文件夹1. datagen文件夹下的genit.py用于进行图像预处理以及数据生成器接口1. 使用训练好的模型进行垃圾分类，运行Demo.py
##### 结果演示

<img src="https://img-blog.csdnimg.cn/a778952ff5f343938ba24adda148d4ac.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/371f8255382746e582ab98d3796e3011.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/49e4e75a76a34da98ea6a7879f29f208.png" alt="在这里插入图片描述"> 完整代码下载地址：
