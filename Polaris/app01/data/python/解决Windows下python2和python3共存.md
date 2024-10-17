
--- 
title:  解决Windows下python2和python3共存 
tags: []
categories: [] 

---
目前，Python3和Python2互相并不完全兼容，这就造成了很多Python代码或者是脚本在版本不对应的情况下无法执行，所以说，在一台电脑上同时拥有Python2和Python3是很有必要的，也能更高效的处理工作，节省时间。

其实要解决Python2和Python3共存也很简单，提供如下方案：

## 1、下载Python2和Python3的安装包(或者叫解释器)

下载地址：

根据自己需要的版本下载即可，安装包都比较小。

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/348c3f796bcb4385994763f07632abf8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA54Of6Zuo5aSp6Z2S6Imy,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

下载后，直接安装即可。

安装过程注意安装路径，默认是安装到C盘，可以根据需要进行更改安装路径。

<img alt="" height="272" src="https://img-blog.csdnimg.cn/492af74ddb184690858efa1bb2afaf4f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA54Of6Zuo5aSp6Z2S6Imy,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

## 2、设置环境变量

由于我们安装了两个版本的Python，因此为了方便系统能够准确识别到指定的Python版本，所以我们需要设置环境变量。

将Python安装路径及其安装路径下的Scripts设置到Path变量里。

这里设置Scripts文件夹的目的是为了方便识别pip。

<img alt="" height="353" src="https://img-blog.csdnimg.cn/9c8cec3ccc5549b297758b25a938fbb2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA54Of6Zuo5aSp6Z2S6Imy,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"> 

##  3、修改Python编译器的名字

为了能够准确定位Python2和Python3，我们需要将默认的Python编辑器的名称进行修改。

**NO.1. **修改Python2安装目录下：python.exe修改为python2.exe，pythonw.exe修改为pythonw2.exe

**NO.2. **修改Python3安装目录下：python.exe修改为python3.exe，pythonw.exe修改为pythonw3.exe

 修改完成后，在命令行下分别输入python2和python3就可以进入对应版本的python环境。

<img alt="" height="337" src="https://img-blog.csdnimg.cn/8505c06781a647c8895d22606b003a73.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA54Of6Zuo5aSp6Z2S6Imy,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

## 4、设置pip

python环境在安装包的时候需要使用到包管理工具——pip，而pip也是需要对应版本的。在python的安装目录Scripts下可以看到 默认是存在pip的，但是在命令行下，并不能直接定位到，因此需要重新分别安装两个版本对应的pip，使得两个python版本的pip也能够共存。

### python2：

```
python2 -m pip install --upgrade pip
```

<img alt="" height="527" src="https://img-blog.csdnimg.cn/ea652ea70890488286cbf548e92b6ade.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA54Of6Zuo5aSp6Z2S6Imy,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

### python3:

```
python3 -m pip install --upgrade pip
```

<img alt="" height="413" src="https://img-blog.csdnimg.cn/08eab5ca13974f5db204e3ec073a8b8f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA54Of6Zuo5aSp6Z2S6Imy,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

安装完成之后，可以使用pip2 -V 或者pip3 -V查看对应的pip版本了。

 <img alt="" height="207" src="https://img-blog.csdnimg.cn/37e110c3afa34c5f8eeac14ce20fa3f3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA54Of6Zuo5aSp6Z2S6Imy,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

 
