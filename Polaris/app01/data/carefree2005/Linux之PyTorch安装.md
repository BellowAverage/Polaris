
--- 
title:  Linux之PyTorch安装 
tags: []
categories: [] 

---
## 一、PyTorch简介

  PyTorch是一个开源的Python机器学习库，基于Torch，用于自然语言处理等应用程序。2017年1月，由Facebook人工智能研究院（FAIR）基于Torch推出PyTorch。PyTorch的前身是Torch，其底层和Torch框架一样，但是使用Python重新写了很多内容，不仅更加灵活，支持动态图，而且提供了Python接口。它是由Torch7团队开发，是一个以Python优先的深度学习框架，不仅能够实现强大的GPU加速，同时还支持动态神经网络。PyTorch既可以看作加入了GPU支持的numpy，同时也可以看成一个拥有自动求导功能的强大的深度神经网络。除了Facebook外，它已经被Twitter、CMU和Salesforce等机构采用。

## 二、安装步骤

### 1、操作系统选择

  查看，可以看到PyTorch支持Linux、Mac、window平台、支持conda、pip、源码等安装方式，也支持CPU、cuda、ROCm计算平台，我们点击环境选择可以发现目前只有linux系统是支持全语言、全安装方式、全计算平台的，所以我们选择linux操作系统作为系统环境。另外机器学习计算要求glibc版本要求较高，centos搭载的内核和glbic版本较低，Ubuntu搭载的内核版本都较新，所以机器学习主机建议使用Ubuntu操作系统。目前cuda更新支持的最低Ubuntu版本为18.04，所以建议使用Ubuntu18.04以上的操作系统。 <img src="https://img-blog.csdnimg.cn/95a15eb0f47e4280adf9f8b20f2941a8.png" alt="在这里插入图片描述">

>  
 wuhs@s169:~$ cat /etc/os-release NAME=“Ubuntu” VERSION=“18.04.6 LTS (Bionic Beaver)” 


### 2、Anaconda3安装

  如上所示，PyTorch支持的安装方式有多种，博主拟采用conda安装方式，建议先安装Anaconda3，可以根据我们需要创建不同虚拟环境，虚拟环境下安装不同的机PyTorch版本，虚拟环境支持互不影响。Ubuntu环境下anaconda的安装见博文。

>  
 wuhs@s169:~$ wget https://mirrors.bfsu.edu.cn/anaconda/archive/Anaconda3-2022.10-Linux-x86_64.sh wuhs@s169:~$ sh Anaconda3-2022.10-Linux-x86_64.sh wuhs@s169:~$ source ~/.bashrc 


### 3、查看Python版本

  不同的PyTorch版本要求的Python版本是不一样的，所以安装好anaconda3后我们检查当前的Python版本，默认初始化都是当前anaconda3发布时对应的Python最新版本，当然我们也可以使用conda创建所需的Python环境版本。我们在查看PyTorch、torchvision、Python版本匹配要求。 <img src="https://img-blog.csdnimg.cn/fb030cca3caa40d7bdea7a818d22942e.png" alt="在这里插入图片描述">

>  
 (base) wuhs@s169:~$ python -V Python 3.9.13 


### 4、安装PyTorch

  如下第二步，PyTorch官网我们可以在选择操作系统、安装方式、编程语言、计算平台后生成对应的安装命令。

>  
 (base) wuhs@s169:~$ conda install pytorch torchvision torchaudio cpuonly -c pytorch Collecting package metadata (current_repodata.json): done Solving environment: done  ## Package Plan ## <img src="https://img-blog.csdnimg.cn/ce4a8b8e19cf4b7f8346d36c903f13fb.png" alt="在这里插入图片描述"> Proceed ([y]/n)? y … 


### 5、版本验证

>  
 (base) wuhs@s169:~$ python Python 3.9.13 (main, Aug 25 2022, 23:26:10) [GCC 11.2.0] :: Anaconda, Inc. on linux Type “help”, “copyright”, “credits” or “license” for more information. &gt;&gt;&gt; import torch &gt;&gt;&gt; torch.**version** ‘1.13.1’ &gt;&gt;&gt; 


## 三、指定版本安装

### 1、创建虚拟环境

>  
 (base) wuhs@s169:~$ conda create -n pytorch python=3.9 … (base) wuhs@s169:~$ conda activate pytorch (pytorch) wuhs@s169:~$ 


### 2、安装指定版本的PyTorch

  安装指定版本的PyTorch的时候我们需要在GitHub官网PyTorch频道查看匹配版本，conda安装的时候指定版本号，具体版本号可以查看，PyTorch版本和TorchAudio对应关系见 。当然如果我们指定版本错误的情况下，安装的时候会报错，我们根据报错提示核验是哪个软件版本指定错误，再去官网合适确认修正后重新安装即可。 <img src="https://img-blog.csdnimg.cn/917458b25a8344739b299ebddc0a2c1b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/758b7b4681ca4f4286be564d3daae351.png" alt="在这里插入图片描述">

>  
 (pytorch) wuhs@s169:~$ conda install pytorch<mark>1.12.0 torchvision=0.13.0 torchaudio</mark>0.12.0 cpuonly -c pytorch … 

