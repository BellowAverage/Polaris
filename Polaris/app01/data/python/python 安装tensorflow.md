
--- 
title:  python 安装tensorflow 
tags: []
categories: [] 

---
**事情是这样滴**

### 一、安装对应的python版本

```
当前tensorflow 2的版本只支持3.6以上的版本，千万注意了

```

我们直接在conda 中安装python
- **先创建虚拟环境**
```

conda create -n tensorflow1 python=3.6

```
- **直接安装tensorflow**
```
conda activate tensorflow1

```

```
查看tensorflow版本
anaconda search -t conda tensorflow

```

```
查看可以下载的版本
anaconda show anaconda/tensorflow

```

```
运行
conda install --channel https://conda.anaconda.org/anaconda tensorflow=1.8.0

```
