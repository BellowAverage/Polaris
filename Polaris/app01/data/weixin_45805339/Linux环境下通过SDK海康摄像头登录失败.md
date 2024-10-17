
--- 
title:  Linux环境下通过SDK海康摄像头登录失败 
tags: []
categories: [] 

---
### 问题：Linux环境下通过海康SDK打开摄像头失败

在Linux环境下，我们在QtCreator IDE开发环境通过海康SDK打开摄像头没有问题。然而通过Linuxdeployqt 打包程序，我们发现所有功能都正常，只有摄像头无法登录。显然代码是没有问题的，那么我们就需要考虑环境。 **我们可以从一下两个方面入手：** 1.程序依赖的库是否完全打包到程序运行文件中 2.海康动态库是否正确链接 显而易见我们的程序依赖是没有问题，那么就着重考虑海康动态库。不得不说海康埋了一个大坑，就是它的SDK会去读取LD_LIBRARY_PATH环境变量，来加载库动态库文件。大多开发人员是不知道这个的，所以可能会花费大量时间去解决这个问题，这样会造成很大的人工成本。

### 解决方法：添加LD_LIBRARY_PATH环境变量

添加环境变量有两种方法： 1.在家目录 ~/.bashrc 添加，对于当前用户每次打开终端都会执行，具体操作如下：

```
vim ~/.bashrc
# 添加如下代码，根据自己的系统信息添加
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/用户名/HKlib:/home/用户名/HKlib/HCNetSDKCom 

```

2.在QT代码中写入，推荐使用这个方法，方便打包之后的程序在不同的环境上运行，具体操作如下：

```
vim setHKenv.sh
# 添加如下内容
#!/usr/bin/env sh
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/用户名/HKlib:/home/用户名/HKlib/HCNetSDKCom

```

在qt代码中添加

```
QProcess::startDetached("./setHkenv.sh");

```
