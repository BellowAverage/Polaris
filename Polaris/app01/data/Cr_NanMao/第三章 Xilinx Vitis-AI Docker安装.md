
--- 
title:  第三章 Xilinx Vitis-AI Docker安装 
tags: []
categories: [] 

---
首先，下载（附件4 Vitis-AI-master.tar.gz），将附件4解压到虚拟机上； 链接：https://pan.baidu.com/s/1VEG0nFxXQmw6in1Mh2WYvA  提取码：fpga  复制这段内容打开「百度网盘APP 即可获取」

然后，在虚拟机terminal命令行中，进入Vitis-AI-master\docker文件夹路径下，运行dpu-compiler-docker-install.sh，该脚本用于Vitis-AI Docker镜像下载到虚拟机本地上，命令如下：

```
User:$ ./dpu-compiler-docker-install.sh
```

<img alt="" height="439" src="https://img-blog.csdnimg.cn/direct/433e13c4b8de43c38adf6215cb016158.png" width="547">

图9

      随后，使用docker镜像命令查看是否下载完成，命令如下：

```
User:$ docker images
```

<img alt="" height="58" src="https://img-blog.csdnimg.cn/direct/b6bf8b55fb334ad6a82e3270b4895878.png" width="562">

图10

      最后，返回到上一级目录，运行如下命令，启动Vitis-AI Docker：

```
User:$ ./dpu-compiler-docker.sh
```

      启动成功后，显示如下：

<img alt="" height="323" src="https://img-blog.csdnimg.cn/direct/a3e836013c714bb3afe3480fa6467b00.png" width="398">

图11

今天不学习，明天变垃圾！！！
