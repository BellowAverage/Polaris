
--- 
title:  torch3d mented_sort.cuh(338): error: invalid combination of type specifiers 
tags: []
categories: [] 

---
安装pytorch3d时，

mented_sort.cuh(338): error: invalid combination of type specifiers

cuda自带的cub编译报错：

```
C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8/include\cub/device/dispatch/dispatch_segmented_sort.cuh(338): error: invalid combination of type specifiers

C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8/include\cub/device/dispatch/dispatch_segmented_sort.cuh(338): error: expected an identifier

C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8/include\cub/device/dispatch/dispatch_segmented_sort.cuh(379): error: expected a member name
```

3 errors detected in the compilation of "D:/research/code/pytorch3d/pytorch3d/csrc/pulsar/cuda/renderer.backward.gpu.cu". renderer.backward.gpu.cu

 然后下载cub代码，release 版本，



cuda11.8，cub版本：1.70

设置CUB_HOME环境变量

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/e59f39edada04eb985e4ab2c31280959.png" width="1200">



编译安装继续报错，说版本不匹配，

解决方法：

管理员权限打开：

"C:\xxx\NVIDIA GPU Computing Toolkit\CUDA\v11.8\include\thrust\system\cuda\config.h"

把    #ifndef THRUST_IGNORE_CUB_VERSION_CHECK给注释掉，

换成#ifdef THRUST_IGNORE_CUB_VERSION_CHECK

再编译。



设置参数：

```
set DISTUTILS_USE_SDK=1
set PYTORCH3D_NO_NINJA=1

```

python setup.py install


