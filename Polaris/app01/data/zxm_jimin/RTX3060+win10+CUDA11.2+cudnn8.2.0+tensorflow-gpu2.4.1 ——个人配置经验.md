
--- 
title:  RTX3060+win10+CUDA11.2+cudnn8.2.0+tensorflow-gpu2.4.1 ——个人配置经验 
tags: []
categories: [] 

---
主要参考博客 

**配置时间：2021.10.26** 以下是我亲测有效的使用 RTX 3060 的各部分安装版本 电脑系统：window 10 python版本：3.6.13 tensorflow-gpu：2.4.1 CUDA版本：11.2 cuDNN版本：8.2.0.53

以下是我个人安装教程，仅供参考，如果出现新问题我恐怕可不能解决，谨慎参考，大神请随意~

**注意，我之前已经成功配置pytorch1.8.0 环境，故这里不会详细写：安装Anaconda 以及 安装CUDA和cuDNN。**

**其他博客的顺序如下： 1、安装Anaconda 2、安装CUDA和cuDNN 3、 安装tensorflow-gpu2.4.1**



#### 文章目录
- - - - 


## 第一步：安装Anaconda

详细步骤可参考我的上一篇博客

1、打开anaconda prompt 2、命令行输入： `conda create --name tf_gpu python=3.6` 3、命令行输入：`conda activate tf_gpu`

## 第二步：安装CUDA和cuDNN

详细步骤可参考我的上一篇博客

**没有进行任何改动**

## 第三步：安装tensorflow-gpu2.4.1

参考博客

1、打开anaconda prompt 2、命令行输入：`conda activate tf_gpu` 3、命令行输入：pip install tensorflow-gpu==2.4.1 <img src="https://img-blog.csdnimg.cn/2757b9618b23413da048e8d2a74e1bfc.png" alt="在这里插入图片描述"> **4、将该环境配置到Pycharm中：**

在File, settings中找到Python Interpreter, 点击设置按钮选择“Add” 选择Existing environment 将自己刚配置的tensorflow-gpu环境的地址选中 <img src="https://img-blog.csdnimg.cn/6f68fd097ae84159a93691e465a2d9d5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/8fdfdba94a944e8eb7463407443d0070.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 测试

```
import tensorflow as tf

print(tf.__version__)
print(tf.test.is_gpu_available())

```

返回False <img src="https://img-blog.csdnimg.cn/da7cce7ed6e54874911e7fde62aa682f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 采用原博主方法  虽然CUDA版本不一样，报错内容不一样，但是好像神奇的可以解决

解决方法： 1、在cuda安装目录下的bin文件夹下找到cusolver64_11.dll 我的目录是C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\bin 2、将其重新命名为cusolver64_10.dll <img src="https://img-blog.csdnimg.cn/be2bddee36034a36832396bafe9d5749.png" alt="在这里插入图片描述"> 返回True <img src="https://img-blog.csdnimg.cn/73bccbdca6734716ae1c2c3a024d3d77.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

在测试一下有没有影响pytorch的GPU使用 <img src="https://img-blog.csdnimg.cn/d028c09342b94bad8bb692173ccfe238.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 没有影响~

大功告成！
