
--- 
title:  Pytorch Mac GPU 训练与测评 
tags: []
categories: [] 

---
今天中午看到Pytorch的官方博客发了Apple M1 芯片 GPU加速的文章，这是我期待了很久的功能，因此很兴奋，立马进行测试，结论是在MNIST上，速度与P100差不多，相比CPU提速1.7倍。当然这只是一个最简单的例子，不能反映大部分情况。这里详细记录操作的一步步流程，如果你也感兴趣，不妨自己上手一试。

#### 加速原理

苹果有自己的一套GPU实现API Metal，而Pytorch此次的加速就是基于Metal，具体来说，使用苹果的Metal Performance Shaders（MPS）作为PyTorch的后端，可以实现加速GPU训练。MPS后端扩展了PyTorch框架，提供了在Mac上设置和运行操作的脚本和功能。MPS通过针对每个Metal GPU系列的独特特性进行微调的内核来优化计算性能。新设备在MPS图形框架和MPS提供的调整内核上映射机器学习计算图形和基元。

因此此次新增的的device名字是mps, 使用方式与cuda 类似，例如：

```
import torch
foo = torch.rand(1, 3, 224, 224).to('mps')

device = torch.device('mps')
foo = foo.to(device)
复制代码
```

是不是熟悉的配方，熟悉的味道？可以说是无门槛即可上手。

此外发现，Pytorch已经支持下面这些device了，确实出乎意料:

 - cpu, cuda, ipu, xpu, mkldnn, opengl, opencl, ideep, hip, ve, ort, mps, xla, lazy, vulkan, meta, hpu

#### 环境配置

为了使用这个实验特性，你需要满足下面三个条件：

 1.  有一台配有Apple Silicon 系列芯片（M1, M1 Pro, M1 Pro Max, M1 Ultra)的Mac笔记本 
 1.  安装了arm64位的Python 
 1.  安装了最新的nightly 版本的Pytorch 

第一个条件需要你自己来设法满足，这篇文章对它的达到没有什么帮助。

假设机器已经准备好。我们可以从下载arm64版本的miniconda(文件名是Miniconda3 macOS Apple M1 64-bit bash,基于它安装的Python环境就是arm64位的。下载和安装Minicoda的命令如下：

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh 
chmod +x Miniconda3-latest-MacOSX-arm64.sh 
./Miniconda3-latest-MacOSX-arm64.sh 
复制代码
```

按照说明来操作即可，安装完成后，创建一个虚拟环境，通过检查platform.uname()[4] 是不是为arm64 来检查Python的架构:

```
conda config --env --set always_yes true
conda create -n try-mps python=3.8
conda activate try-mps
python -c "import platform; print(platform.uname()
```
