
--- 
title:  python环境移植，制作可以移植的python环境 
tags: []
categories: [] 

---
### 1 背景

一般ubuntu16.04默认安装了python2.7和python3.5，ubuntu18.04默认安装了python2.7和python3.6。有些情况我们开发可能会依赖更高的python解释器，但是在较低版本ubuntu或者其他Linux系统上安装 python3.6以上版本会很麻烦。我们考虑制作一个python3.8虚拟环境，将虚拟环境拷贝到目标服务器，source activate指令 进入虚拟环境就可以直接运行python3.8。我们找到了一种简单的制作python3.8虚拟环境的方法，那就是基于anaconda3修改相关的环境变量，anaconda是python的发行版。

### 2 制作可移植环境

#### 2.1 Anaconda下载

Anaconda和Python版本是对应的，所以需要选择安装对应Python2.7版本的还是Python3.8版本或其他版本的，根据自己的需要下载合适的安装包。    我下载的Anaconda3，对应python3.8.3版本 终端下载

```
wget Anaconda3-2019.03-Linux-x86_64.sh

```

#### 2.2 Anaconda安装

我们下载下来的是一个.sh的shell文件，开始安装
1. 运行sh文件
```
bash Anaconda3-2019.03-Linux-x86_64.sh

```
1. 注册信息确定输入“yes”
```
➜  ~ Please answer 'yes' or 'no':
➜  ~ &gt;&gt;&gt; yes

```
1. 安装完成后，收到加入环境变量的提示信息，输入yes1. 提示信息“Do you wish to proceed with the installation of Microsoft VSCode? [yes|no]”，输入no；1. 重启终端，即可使用Anaconda31. 若在终端输入 python，仍然会显示Ubuntu自带的python版本，我们执行：
```
➜  ~  sudo vim ~/.bashrc
➜  ~  export PATH="/home/xxx/anaconda3/bin:$PATH"
➜  ~  source ~/.bashrc

```
1. 运行python
```
➜  ~  python
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; exit()

```

很完美！

#### 2.3 可移植python环境制作

接下来是我们本文要说的关键，我们一起来制作一下可移植环境吧
1. 进入/home/xxx/anaconda3目录下(当然这个目录要看你自己的家目录)1. 修改启动文件:vim bin/activate，改成下边那个熊样就OK可
```
#!/bin/sh
PYTHONHOME=$1
sed -i -e "1,1c #!$PYTHONHOME/bin/python" "$PYTHONHOME/bin/conda"
sed -i -e "1,1c #!$PYTHONHOME/bin/python" "$PYTHONHOME/bin/pip"
sed -i -e "1,1c #!$PYTHONHOME/bin/python" "$PYTHONHOME/bin/pip3"
export PYTHONHOME=$PYTHONHOME
export _CE_M=''
export _CE_CONDA=''
export "PYTHONPATH=$PYTHONHOME/bin/python3.8"
export "CONDA_PYTHON_EXE=$PYTHONHOME/bin/python"
export "CONDA_EXE=$PYTHONHOME/bin/conda"
export "PATH=$PYTHONHOME/bin:$PYTHONHOME/bin:$PYTHONHOME/bin:$PYTHONHOME/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
export "CONDA_DEFAULT_ENV=python38"
export "CONDA_PROMPT_MODIFIER=(python38)"
# Copyright (C) 2012 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
\. "$PYTHONHOME/etc/profile.d/conda.sh" || return $?
conda activate "$@"

```
1. 修改conda.sh文件，vim etc/profile.d/conda.sh 注释掉下面几个环境变量：
```
#export CONDA_EXE='/home/xxx/anaconda3/bin/conda'
#export _CE_M=''
#export _CE_CONDA=''
#export CONDA_PYTHON_EXE='/home/xxx/anaconda3/bin/python'

```
1. 很完美，我们的可移植的python环境就做好了，打包成anaconda3.tar.gz1. 当然这个可移植的环境，有个缺点就是比较大，打包完成后是2G左右。因为python依赖的lib库比较多，所以想瘦身有点不现实。
### 3 使用说明
- 将anaconda3.tar.gz解压（解压后文件大约5.1G）到任意目录记为： /xxx/xxx/- 进入解压的目录：cd /xxx/xxx/anaconda3- 启动虚拟环境：执行命令source bin/activate /xxx/xxx/anaconda3 注：/xxx/xxx/anaconda3一定要是绝对路径
```
➜  anaconda3 source bin/activate /home/wuhao/anaconda3
(base) ➜  anaconda3 python
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; 

```
- 一点毛病没有，nice！