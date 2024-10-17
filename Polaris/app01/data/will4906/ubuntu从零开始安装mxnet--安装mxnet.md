
--- 
title:  ubuntu从零开始安装mxnet--安装mxnet 
tags: []
categories: [] 

---
mxnet的安装有多种方式，最简单的自然是pip直接安装。这里只说明gpu版本。

### pip安装

#### python准备

安装python, python-pip这些都不在赘述

#### 安装mxnet

`pip install mxnet-cu80==0.11.0`

#### 测试mxnet

```
python
import mxnet as mx
a = mx.nd.ones((2, 3), mx.gpu())
b = a * 2 + 1
b.asnumpy()
```

若输出结果如下

```
array([[ 3.,  3.,  3.],
       [ 3.,  3.,  3.]], dtype=float32)
```

表示安装正常。

### docker安装

#### 安装docker

安照，我们逐步安装  1. `apt update`  2. `sudo apt-get install \  apt-transport-https \  ca-certificates \  curl \  software-properties-common`  3. `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`  4. `sudo add-apt-repository \  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \  $(lsb_release -cs) \  stable"`  5. `sudo apt-get update`  6. `sudo apt install docker-ce`

#### 安装nvidia-docker-plugin
1. 于github中下载1. 安装nvidia-docker-plugin  `sudo dpkg -i nvidia-docker_1.0.1-1_amd64.deb`1. 安装nvidia-modprobe, `apt install nvidia-modprobe`1. 启动nvidia-docker-plugin，`nvidia-docker-plugin`，如若正常表示安装成功。
#### 下载Mxnet Docker镜像
1. `sudo docker pull mxnet/python:gpu`1. 启动镜像`nvidia-docker run -it mxnet/python:gpu bash`1. 和使用python安装的方式一样，我们测试执行上面的python，如果结果相同，表示安装成功。
至此我们ubuntu从零开始安装mxnet系列到此完结，感谢各位开发者的无私奉献。
