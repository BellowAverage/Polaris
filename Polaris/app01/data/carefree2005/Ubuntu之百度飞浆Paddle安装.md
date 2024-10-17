
--- 
title:  Ubuntu之百度飞浆Paddle安装 
tags: []
categories: [] 

---
## 一、Paddle简介

  百度飞桨（PaddlePaddle）是百度基于深度学习技术研发的开源深度学习平台，提供全面的深度学习框架和工具，支持多种深度学习算法和模型，包括图像识别、自然语言处理、语音识别等领域。飞桨采用动态图和静态图相结合的方式，具有高效、灵活、易用的特点，帮助用户快速构建和训练深度学习模型，加速深度学习应用的落地。同时，百度飞桨还提供了丰富的深度学习应用场景案例和实践教程，帮助用户深入了解深度学习技术和应用。博文实验环境如下：
- 操作系统：Ubuntu20.04.3 LTS- cuda版本：11.6- python版本：3.8- Paddle版本：2.4
## 二、安装步骤

### 1、安装anconda3

  推荐使用pip或者conda方式安装，所以建议先创建一个python虚拟环境，可以先安装anconda3用于创建和管理python虚拟环境。安装步骤见博文。

>  
 wuhs@jqxxpc:~$ wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2020.02-Linux-x86_64.sh wuhs@jqxxpc:~$ sh Anaconda3-2020.02-Linux-x86_64.sh 


### 2、创建paddle虚拟环境

>  
 (base) wuhs@jqxxpc:~$ conda create --name paddle python=3.8 (base) wuhs@jqxxpc:~$ conda activate paddle (paddle) wuhs@jqxxpc:~$ 


### 3、官网选择安装方式获取安装命令

  访问，选择需要安装的飞浆版本，操作系统类型、安装方式、计算平台。博主这里是Ubuntu系统，配置有显卡选择的cuda11.6计算平台，查看cuda版本使用nvcc -V命令。关于cuda的安装可以参考博文。 <img src="https://img-blog.csdnimg.cn/d01346f85b5f4234b0480b25336f90fb.png" alt="在这里插入图片描述">

### 4、执行安装命令

  点击复制按钮，复制安装命令，在paddle虚拟环境下直接执行此命令。

>  
 (paddle) wuhs@jqxxpc:~$ conda install paddlepaddle-gpu==2.4.2 cudatoolkit=11.6 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge … Proceed ([y]/n)? y … Preparing transaction: done Verifying transaction: done Executing transaction: | b’By downloading and using the CUDA Toolkit conda packages, you accept the terms and conditions of the CUDA End User License Agreement (EULA): https://docs.nvidia.com/cuda/eula/index.html\n’ | b’By downloading and using the cuDNN conda packages, you accept the terms and conditions of the NVIDIA cuDNN EULA -\n https://docs.nvidia.com/deeplearning/cudnn/sla/index.html\n’ done 


### 5、安装验证

  安装完成后，输入python命令进入python交互模式，使用如下方式查看验证paddle是否安装成功，看到“PaddlePaddle is installed successfully! ”说明安装成功。使用paddle.__version__查看paddle版本。

>  
 (paddle) wuhs@jqxxpc:~$ python &gt;&gt;&gt; import paddle &gt;&gt;&gt; paddle.utils.run_check() Running verify PaddlePaddle program … PaddlePaddle works well on 1 GPU. W0509 17:21:14.797003 3684118 fuse_all_reduce_op_pass.cc:79] Find all_reduce operators: 2. To make the speed faster, some all_reduce ops are fused during training, after fusion, the number of all_reduce ops is 2. PaddlePaddle works well on 2 GPUs. PaddlePaddle is installed successfully! Let’s start deep learning with PaddlePaddle now. #使用paddle.__version__查看paddle版本。 &gt;&gt;&gt; import paddle &gt;&gt;&gt; paddle.**version** ‘2.4.2’ 

