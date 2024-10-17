
--- 
title:  mysqlclient Windows 下安装报错解决方法 
tags: []
categories: [] 

---
用pip install mysqlclient时，出现了如下报错问题：

>  
 error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools 


<img alt="" height="623" src="https://img-blog.csdnimg.cn/b83e4e890191462ba8d709cb07c16741.png" width="1200">

最简单的解决方法就是手动下载wheel包

下载链接：

到这个地址去找相对应的mysqlclient资源，可以用快捷键ctrl+f搜索mysqlclient

<img alt="" height="789" src="https://img-blog.csdnimg.cn/ba276ad480b2402e91fd56bfeb0d535d.png" width="1200">

其中cp37对应python3.7，win64表示windows64位系统

这里由于当时我的python3.7版本下载的是32bit的，因此whl包也需要是32位的才可以支持。

大家可以留意一下自己的python版本，避免出现错误。

我这里选择**mysqlclient‑1.4.6‑cp37‑cp37m‑win32.whl**
1. 首先下载**mysqlclient‑1.4.6‑cp37‑cp37m‑win32.whl**这个资源文件。1. 在该资源所在路径打开命令行使用如下命令安装：1. pip install mysqlclient-1.4.6-cp37-cp37m-win32.whl
安装成功

<img alt="" height="182" src="https://img-blog.csdnimg.cn/2bba185b35af4f919c8834696f9dcbde.png" width="938">

 
