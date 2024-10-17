
--- 
title:  ubuntu从零开始安装mxnet--安装cuda8.0 
tags: []
categories: [] 

---
CUDA是一种由NVIDIA推出的通用并行计算架构，该架构使GPU能够解决复杂的计算问题。  根据的说法，我们应该安装的是cuda8.0的版本。

#### 下载cuda

这里笔者给出了最新版cuda的下载地址，，8.0版本的下载地址不明原因无法打开。笔者给出了百度云的地址，不过只有Ubuntu16.04 cuda8.0.61版本。链接:  密码: jcrj  如果小伙伴自行下载请选择.run文件进行下载，因为其他方式，笔者进行了多次尝试都很难成功。

#### 驱动准备

安装nvidia显卡驱动，可以看一下笔者的上一篇文章

#### 运行cuda安装文件
1. 安装辅助的库  `sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libgl1-mesa-glx libglu1-mesa libglu1-mesa-dev`1. 运行文件  `./cuda_8.0.61_375.26_linux.run`<li>运行流程  
  1. 运行一开始会让我们阅读一段非常长的协议，我们可以通过ctrl + c跳过这段。并在之后第一个问题输入accept同意以上协议。1. 不要安装nvidia驱动！！！！（关键），在问题中输入n  <img src="https://img-blog.csdn.net/20171012173326812?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">1. 接下来我们只需要输入yes和保持默认路径即可1. 安装成功  <img src="https://img-blog.csdn.net/20171012173408222?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title=""></li>
#### 检查和补充安装
<li>执行`nvcc -V`会出现两种情况。  
  <ol><li>第一种是我们之前的安装没有完全安装完成，会有如下提示  <img src="https://img-blog.csdn.net/20171012173628037?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">  
    <ul>- 我们只需要根据提示执行`sudo apt install nvidia-cuda-toolkit`即可，不过可能时间有点久，请耐心等待。<li>第一种是我们之前的安装没有完全安装完成，会有如下提示  <img src="https://img-blog.csdn.net/20171012173628037?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">  
    1. 我们只需要根据提示执行`sudo apt install nvidia-cuda-toolkit`即可，不过可能时间有点久，请耐心等待。</li>1. 经过一番耐心等待之后，安装完成，再次输入`nvcc -V`，得到如下结果  <img src="https://img-blog.csdn.net/20171012175430363?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">
#### 运行一个例子

在安装完成后，我们可以尝试运行官方给的一个sample，如果我们之前安装的时候按照默认路径安装的话，不出意外会在`/root/NVIDIA_CUDA-8.0_Samples`文件夹下。  1. 执行`cd /root/NVIDIA_CUDA-8.0_Samples/1_Utilities/deviceQuery`进入文件夹  2. 执行`make`编译文件  3. 执行`./deviceQuery`，如果出现了Result = PASS字样，恭喜，之前的步骤全部成功，可以进行下一步。  <img src="https://img-blog.csdn.net/20171012180254380?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">

#### 添加环境变量

编辑`vim /etc/profile`，在最后面添加

```
export PATH=$PATH:/usr/local/cuda-8.0/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-8.0/lib64
export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/cuda-8.0/lib64
```

最后执行`source /etc/profile`
