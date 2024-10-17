
--- 
title:  centOS 7 安装python3.6.5 与 pyCharm搭建 
tags: []
categories: [] 

---
Linux版本：centos7.4

**安装python3后也完成了pip3，就可以使用pip3和python3执行命令行**

**centos7.4自带python2，所以使用时使用pip3和python3执行命令行**

**一、安装python3** 先安装Python3的依赖包

安装几个必须的包，以方便后续的操作

上 Python的官网 下载源码包，存放在压缩包目录（自定义）下

cd到压缩包目录下，解压出来

新建python3文件夹，作为安装路径

在解压出来的Python-3.6.5进行编译，编译到安装路径，并执行安装

cd Python-3.6.5

--prefix：安装路径

修改软连接

查看安装版本

pip更新

pip3 install --upgrade pip  （21.3.1）

安装第三方库

pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
