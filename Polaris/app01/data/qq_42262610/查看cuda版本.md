
--- 
title:  查看cuda版本 
tags: []
categories: [] 

---
```
cat  /usr/local/cuda/version.txt
```

或者

```
nvcc -V
```

问题1：nvidia-smi显示CUDA Version:11.4, 系统安装的是11.1，这有没有问题？

回答：nvidia-smi显示的CUDA Version是当前驱动的最高支持版本，因为CUDA是向下兼容的，所以最高支持版本以下的CUDA版本都是支持的，以图1为例，nvidia-smi显示最高版本支持为11.4，那11.4以及11.4一下的版本都是支持的。

问题2：用nvcc --V和cat /usr/local/cuda/version.txt版本不一致,

nvcc --V为9.1

at /usr/local/cuda/version.txt为10.2

解决办法：如下图所示，输入：

```
vi ~/.bashrc
```

然后将bashrc文件中的cuda版本号10.0。由于我之前在安装CUDA的时候，环境已经配置好了，即已经修改为10.0了，所以我的不需要再修改。如下图所示：

<img alt="" src="https://img-blog.csdnimg.cn/20200805185431978.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI1NjAzODI3,size_16,color_FFFFFF,t_70">

最后，再source一下就好了，即：

```
source ~/.bashrc
```

 现在输入nvcc --version或者nvcc -V变成10.0了，大功告成。 
