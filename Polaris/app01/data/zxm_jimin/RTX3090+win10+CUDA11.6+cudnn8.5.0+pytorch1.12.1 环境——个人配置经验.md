
--- 
title:  RTX3090+win10+CUDA11.6+cudnn8.5.0+pytorch1.12.1 环境——个人配置经验 
tags: []
categories: [] 

---
主要参考博客： 

配置时间：2022.9.14 以下是我亲测有效的使用 RTX 3090 的各部分安装版本： 电脑系统：window 10 python版本：3.8.13 pytorch版本：1.12.1 CUDA版本：11.6 cuDNN版本：8.5.0

以下是我个人安装教程，仅供参考，如果出现新问题我恐怕可不能解决，谨慎参考，大神请随意~



#### 文章目录
- - - - - - - - <ul><li>- - <ul><li>- - - 


## 第一步：安装Anaconda

**注意！！！注意安装的Anaconda是64位的，不然后面的pytorch不能找到对应版本！！！** 第一次失败： 后续安装pytorch时一直报错`Solving environment: failed with initial frozen solve. Retrying with flexible solve.` 网上查说是版本不对应的问题，一开始一直以为是python版本的问题，最后才发现是anaconda的版本错了。Anaconda装成32位的，还一直傻傻没有发现。。。 <img src="https://img-blog.csdnimg.cn/6aa6390764d840d09f8945c544b9ba4e.jpeg" alt="在这里插入图片描述" width="120" height="120"> <img src="https://img-blog.csdnimg.cn/8430e664f3d843da9775dc899f3512aa.png" alt="在这里插入图片描述">

检查版本 `conda info` <img src="https://img-blog.csdnimg.cn/f8a9d901bd464897bd043c709e0f498e.png" alt="在这里插入图片描述"> **重新安装了64位的Anaconda** <img src="https://img-blog.csdnimg.cn/fd6460ce0801487aa938f2090c2c6c36.png" alt="在这里插入图片描述"> 根据提示安装即可。

## 第二步：新建环境

1、打开anaconda prompt 2、命令行输入：`conda create --name pytorch_gpu python=3.8` python_gpu为anaconda下虚拟环境名称 <img src="https://img-blog.csdnimg.cn/e45161a165844de385bd0becce83e09a.png" alt="在这里插入图片描述"> 3、如果要启用创建的环境，输入指令：`conda activate pytorch_gpu` 关闭该环境的话，输入指令：`conda deactivate`

## 第三步：Cuda安装

**建议安装CUDA之前先安装VS**

不知道为什么，网上教程这样建议的，于是我还是安装了，**一定不要装在c盘！！！！！** 可选VS2013，体量小。 我直接官网下载，装的VS2019版本，选择C++开发工具即可。

<img src="https://img-blog.csdnimg.cn/955d35aa44194a04b8dc64b72e456d6b.png" alt="在这里插入图片描述"> Driver Version：512.50 CUDA Version：11.6

虽然自带CUDA，但是为了保险起见，重新**安装CUDA和cuDNN** 注意，安装完重启，否则`nvcc -V`可能没变

**1、进入官网检查版本对应** https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html <img src="https://img-blog.csdnimg.cn/6549473ce20047109c11f5855bb37213.png" alt="在这里插入图片描述"> 考虑到越新的版本可能对运算有优化，这里安装11.6版本

**2、下载安装包** CUDA下载网站，无需注册 https://developer.nvidia.com/cuda-toolkit-archive <img src="https://img-blog.csdnimg.cn/010f3d2fb7ba48bcbacb6f3ae0be28e3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d0bf03759f81411ba5046bf2fa53409c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 根据提示安装即可

## 第四步：cudnn安装

**1、检查cudnn是否安装** cmd下输入命令：`nvcc -V` 如果已经安装会出现详细信息，**注意，CUDA安装完重启，否则`nvcc -V`可能没变** cudnn安装好后： <img src="https://img-blog.csdnimg.cn/e9e9d5a0f26e489cb80b713b3c79738e.png" alt="在这里插入图片描述">

**2、下载安装包** cuDNN网址 

下载cuDNN需要注册NVIDIA账号并登录，我使用`163邮箱`可以正常收发邮件。邮箱验证完后，补全一些信息即可。 <img src="https://img-blog.csdnimg.cn/b72bb52769b84d1dac0d3e1388269b3d.png" alt="在这里插入图片描述"> 我下载的是最新版本：cudnn8.5.0 <img src="https://img-blog.csdnimg.cn/bdfd742a94704b558b6e5672e79dadb1.png" alt="在这里插入图片描述"> **4、安装cudnn** 安装CUDA完毕后

解压cuDNN压缩包，复制以下所有内容。 <img src="https://img-blog.csdnimg.cn/1f9dd535bd64450e9b6cc76a99bc3996.png" alt="在这里插入图片描述"> 打开路径 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.6

将刚才复制的内容粘贴到该文件夹。 这里与相似，大体上是这样 <img src="https://img-blog.csdnimg.cn/6f6201059c3648338d8c6b38d0463763.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_19,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ba4543e688da4a12bafc86b3774b50a0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_19,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 完成。

检查：

## 安装pytorch

按照官网建议  <img src="https://img-blog.csdnimg.cn/07fa90b57730430a825e2f507daf6071.png" alt="在这里插入图片描述"> 激活环境后安装

```
conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge

```

根据提示安装即可。

## 测试

全部安装好后测试，参考博客 、

```
import torch
print("Pytorch version：")
print(torch.__version__)
print("CUDA Version: ")
print(torch.version.cuda)
print("cuDNN version is :")
print(torch.backends.cudnn.version())

print("torch.cuda.is_available():",torch.cuda.is_available())           # cuda是否可用
print("torch.cuda.current_device():",torch.cuda.current_device())       # 返回当前设备索引
print("torch.cuda.device_count():",torch.cuda.device_count())           # 返回GPU的数量
print("torch.cuda.get_device_name(0):",torch.cuda.get_device_name(0))   # 返回gpu名字，设备索引默认从0开始

```

<img src="https://img-blog.csdnimg.cn/a18f302d61804295ae691ce2ed389d6b.png" alt="在这里插入图片描述"> cudnn的版本不知道为啥子不一样，不过应该是可以用~

## 备注

### 1、jupyter运行

配置： 注意配置环境变量！ <img src="https://img-blog.csdnimg.cn/fd62e881399d4898a1ceefbd2be44839.png" alt="在这里插入图片描述">

运行 ：anaconda prompt

```
cd / 路径
jupyter notebook ./

```

### 2、tensorflow-gpu安装

#### 1、新建环境

conda create --name tf_gpu python=3.8

#### 2、版本对应

<img src="https://img-blog.csdnimg.cn/c981147d26cf42e4b31bc3853d739655.png" alt="在这里插入图片描述">

#### 3、tensorflow_gpu安装

参考博客：

```
pip install -U tensorflow-gpu -i https://pypi.tuna.tsinghua.edu.cn/simple

```

<img src="https://img-blog.csdnimg.cn/3a9d2ccbb2f0448eb87277bc4c768f46.png" alt="在这里插入图片描述"> 帮我安装的tensorflow_gpu2.10.0 <img src="https://img-blog.csdnimg.cn/cdb9f1b1f2fd4f5595e9aed8e3c90d1c.png" alt="在这里插入图片描述"> python3.8.13 <img src="https://img-blog.csdnimg.cn/aea29fcc54ad46f7bc5d9dfc028b36f8.png" alt="在这里插入图片描述">

#### 4、测试

```
import tensorflow as tf
tf.test.is_gpu_available()

```

<img src="https://img-blog.csdnimg.cn/02e636cec5ec405ba1fa5412eb433689.png" alt="在这里插入图片描述"> 应该是没什么问题。

### 3、环境相关

**克隆环境** 如果要启用创建的环境：

```
conda activate pytorch_gpu

```

关闭该环境的话：

```
conda deactivate

```

**查看环境**

```
conda info --envs
# 或者
conda env list

```

**删除环境** 其中yyy是要卸载的环境名

```
conda uninstall -n yyy --all 

```

把本地的AAA环境克隆成BBB

```
conda create -n BBB --clone AAA

```

### 4、Pycharm运行问题

pycharm 运行测试代码时，报错： Original error was: DLL load failed while importing _multiarray_umath: 找不到指定的模块。 <img src="https://img-blog.csdnimg.cn/04952709ccf1445b8edd315cc7c0aa26.png" alt="在这里插入图片描述"> 经过百度： 应该时numpy版本问题，激活环境后，重装numpy conda uninstall numpy conda install numpy

<img src="https://img-blog.csdnimg.cn/988eadcd930c4d628592da2573160ee6.jpeg" alt="在这里插入图片描述" width="120" height="120"> 完结撒花~
