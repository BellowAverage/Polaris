
--- 
title:  ubuntu 卸载 python2 安装python3 opencv 
tags: []
categories: [] 

---


### 1.卸载python2.7

`sudo apt-get remove python2.7`

### 2.卸载python2.7及其依赖

`sudo apt-get remove --auto-remove python2.7`

### 3.消除python2.7

`sudo apt-get purge python2.7 or sudo apt-get purge --auto-remove python2.7`



安装python3：

sudo apt-get install python3.8:

安装opencv-python：

pip install opencv-python，结果报错：

No module named 'skbuild'

解决方法：

pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple scikit-build



安装完成后，再次安装opencv-python发现还会会报错:

Problem with the CMake installation, aborting build. CMake executable is cmake 大致的意思是：CMake安装有问题，正在中止构建。 然后在终端输入：

pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple cmake 再次尝试，opencv-python安装成功 原文链接：https://blog.csdn.net/weixin_44996884/article/details/108678298
