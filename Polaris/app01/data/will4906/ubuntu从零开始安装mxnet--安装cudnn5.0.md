
--- 
title:  ubuntu从零开始安装mxnet--安装cudnn5.0 
tags: []
categories: [] 

---
在经过之前的各项安装和准备工作，之后。  接下来我们安装cudnn，cudnn的安装比较简单，不过下载可能稍微比较麻烦些。

#### 下载cudnn

我们先要在nvidia的官网注册个账号。然后才能选择对应的cudnn版本下载安装。根据的要求我们下载5.0的版本。下载下来的内容是个压缩包。

#### 安装cudnn

我们将下载下来的压缩包解压缩，会出来一个cuda文件夹，里面分为include和lib64两个文件夹，我们需要将对应文件夹下的文件拷贝到之前安装cuda8.0的位置下的对应文件夹下。  给个例子，  `sudo cp cuda/include/cudnn.h /usr/local/cuda-8.0/include`  `sudo cp cuda/lib64/lib* /usr/local/cuda-8.0/lib64`

#### 测试安装

在官网中下载cudnn_sample，解压，然后进入  `cd cudnn-sample-v5/mnistCUDNN`  `make`  `./mnistCUDNN`  最后如果出现test passed表示测试成功。  <img src="https://img-blog.csdn.net/20171013004101017?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">
