
--- 
title:  《 Python笔记》— 将Python程序代码打包封装为exe可执行文件 PyInstaller的快速使用 
tags: []
categories: [] 

---


#### 目录
- - <ul><li>- <ul><li>- - 


## 《 Python笔记》— 将Python程序代码打包封装为exe可执行文件

《 Python笔记》— 将Python程序代码打包封装为exe可执行文件，摆脱不同Windows操作系统电脑之间因python版本环境不兼容无法运行同一代码问题，在没有python环境的电脑也可以运行。

不仅如此，打包后的源码程序使用者是无法直接获得的，这样既避免了使用者误改源码，也将自己源码程序保密了，起到一定软件著佐权和版权保护的作用。

但是这样就又必然失去了开源的花花世界了，所以是否需要打包封装，需要开发者综合评估。

那么该怎么讲python源码程序打包为exe可执行程序呢？

**用PyInstaller**

>  
 PyInstaller是Python程序打包一定不得不说、不学、不用的的第三方包。 


<img src="https://img-blog.csdnimg.cn/94cdcc917ab2448fbf8ad04d5b94e128.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_8,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="200">

### 1、了解PyInstaller

#### 1.1 概述

PyInstaller将Python代码程序及其所有依赖项目捆绑到一个应用程序中。用户可以在不安装Python解释器或任何模块的情况下运行这个打包的应用程序。PyInstaller支持Python3.7及更高版本。

PyInstaller是针对主流三大操作系统：Windows、MacOS 和Linux进行布局测试的。但是，和别的应用程序软件一样，用PyInstaller打包的应用程序并不能在以上操作系统之间通用。 要制作Windows系统的应用程序，请在Windows上运行PyInstaller；要制作MacOS 系统的应用程序，请在MacOS 上运行PyInstaller；要制作Linux系统的应用程序，请在Linux上运行PyInstaller。

**截止2022年4月已发布的版本有： v5.0.1 、v5.0 、v4.10、 v4.9、 v4.8 、v4.7 、v4.6、 v4.5.1、 v4.5 、v4.4 、v4.2、 v4.1、 v4.0、 v3.6、 v3.5、 v3.4、 v3.3.1、 v3.3、 v3.2.1、 v3.2**

#### 1.2 系统要求

**Windows（32位/64位）：** PyInstaller可在Windows 8以上的Windows系统中运行。它可以创建图形窗口应用程序，同时也可以选择保留命令窗口的应用程序。 **macOS（64位）** PyInstaller可在MacOS 10.15以上的系统上运行。 **GNU/Linux（32位/64位）** PyInstaller要求ldd终端应用程序发现每个程序或共享库所需的共享库。

#### 1.3 Python要求

Python版本要求：Python3.7以上

### 2、安装PyInstaller

**pip 安装 命令**

```
pip install pyinstaller   # 默认安装
pip install pyinstaller==3.2.1  # 安装指定版本的
pip install pyinstaller -i https://pypi.douban.com/simple/  # 挂国内镜像安装

```

**更新版本 命令**

```
pip install --upgrade pyinstaller

```

**以源码文件形式安装最新版本**

```
pip install https://github.com/pyinstaller/pyinstaller/tarball/develop

```

### 3、使用PyInstaller将py文件打包exe文件

Win+R 打开运行 <img src="https://img-blog.csdnimg.cn/51a4108a5a3549ed868d838425109ca9.png" alt="在这里插入图片描述">

cd 到py文件所在的路径下，以下图为例 <img src="https://img-blog.csdnimg.cn/43a103bcabb04bb983da611d11c6f3cd.png" alt="在这里插入图片描述">

输入如下命令

```
pyinstaller -F Watermark.py –noconsole

```

<img src="https://img-blog.csdnimg.cn/e50b2ae7697c4ddeb5f9804915781a21.png" alt="在这里插入图片描述"> 等待执行完成，在py文件所在路径下会生成如下文件(夹)

生成的exe文件在dist文件夹中

### 更多内容

公众号地址： 

CSDN主页地址： 
