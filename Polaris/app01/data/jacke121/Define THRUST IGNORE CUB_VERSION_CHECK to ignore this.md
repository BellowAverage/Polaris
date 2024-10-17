
--- 
title:  Define THRUST IGNORE CUB_VERSION_CHECK to ignore this 
tags: []
categories: [] 

---




解决方法：

管理员权限打开：

"C:\xxx\NVIDIA GPU Computing Toolkit\CUDA\v11.8\include\thrust\system\cuda\config.h"

把    #ifndef THRUST_IGNORE_CUB_VERSION_CHECK给注释掉，

换成#ifdef THRUST_IGNORE_CUB_VERSION_CHECK

再编译。


