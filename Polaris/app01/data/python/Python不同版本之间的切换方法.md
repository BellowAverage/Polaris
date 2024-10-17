
--- 
title:  Python不同版本之间的切换方法 
tags: []
categories: [] 

---
### 在使用Python的过程中难免会遇到不同的项目使用不通同的Python环境，这就引出Python环境的切换问题

#### 这篇文章以3.11.0与3.10.10之间的版本切换为列讲述

##### 首先我自己的电脑上同时安装了这两个版本的Python，并且都已经配置了环境变量

##### 1.两个版本的Python

<img src="https://img-blog.csdnimg.cn/7752a2056f8b4201ade997cbbc30b16e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/4db013f0bdab4f5d9dfd6ee59d62354f.png" alt="在这里插入图片描述">

##### 2.环境变量

<img src="https://img-blog.csdnimg.cn/a99b49ba6b064730a7d8bd2acf9d3244.png" alt="在这里插入图片描述">

##### 调出CMD（win+r，输入cmd,回车），输入python，可以看到目前的版本为3.10.10

<img src="https://img-blog.csdnimg.cn/61daac7c66b04a069f0a2ee75ebe02a4.png" alt="在这里插入图片描述">

##### 注意：这样在直接使用pip安装库的时候是安装到3.10.10版本下的

##### 这是因为目前3.10.10版本的环境变量在3.11.0上边，如下图

<img src="https://img-blog.csdnimg.cn/6e923806866144ae9a3af198a4a0c553.png" alt="在这里插入图片描述">

##### 将这两个版本的环境变量调整一下，将3.11.0版本的路径调到3.10.10之前，点击确定修改

<img src="https://img-blog.csdnimg.cn/e790ddb70e6141c18f5985573eb8d1cd.png" alt="在这里插入图片描述">

##### 重新打开CMD（win+r，输入cmd,回车），输入python，发现已经是3.11.0版本了

<img src="https://img-blog.csdnimg.cn/5f6cc29758d245ac89ba80675f1a018c.png" alt="在这里插入图片描述">

##### 注意：这样在直接使用pip安装库的时候是安装到3.11.0版本下的

##### 以上内容就是让大家更好的理解多个版本python环境下，到底是通过什么来控制在CMD中输入python时运行的不同版本，显然，是因为环境变量的原因，那如果说一直通过这种方式在不通的python版本下切换的话太麻烦也太费时间，下面要将的就是怎么能够快速使用不同的python环境，快速给不同版本的python安装不同的库

## 快速使用不同的python环境，快速给不同版本的python安装不同的库

## 切换环境：

##### 分别进入到两个不同版本Python的安装路径，将复制一个python.exe并重命名即可，以我目前环境为列，分别命名为了python310.exe与python311.exe，如下图

<img src="https://img-blog.csdnimg.cn/5c3a8db67acf45c293553c207b8087d0.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/617c5bf9af4242abb601b745b550f3ba.png" alt="在这里插入图片描述">

##### 注意：如果不复制python.exe，直接重命名会导致新建的虚拟环境出现问题，比如：pip命令不能用

##### 调出CMD（win+r，输入cmd,回车），输入python310，可以看到目前的版本为3.10.10，输入python311，可以看到目前的版本为3.11.0

<img src="https://img-blog.csdnimg.cn/dea615092f4141579e8791079cf20ecc.png" alt="在这里插入图片描述">

### 安装库：

##### 用以下命令安安装及查看：

```
安装库：
python-name -m pip install 包名
查看pip的版本：
python-name -m pip --version
查看pip的安装包的列表：
python-name -m pip list

```

##### 其中python-name为自己修改过后的python.exe的名称，比如我环境下查看安装的库

```
查看3.10.10版本：
python310 -m pip list
查看3.11.0版本：
python311 -m pip list

```

<img src="https://img-blog.csdnimg.cn/af2651bff0814e6395db910ab2ce7db7.png" alt="在这里插入图片描述">

##### 要执行不同环境下的库就要在库名前加上“自己修改过后的python.exe的名称 -m”

```
python-name -m

```

##### 比如我要运行3.11.0版本下的virtualenv库

<img src="https://img-blog.csdnimg.cn/1e3ac56668d14e50bacd9f10ac40c965.png" alt="在这里插入图片描述">

##### 如果在3.10.10下执行，会报错，因为在3.10.10版本下我未安装该库，所以会提示以下信息

<img src="https://img-blog.csdnimg.cn/5318b55919b0420a859b722e0897a6ad.png" alt="在这里插入图片描述">

##### 本文章结
