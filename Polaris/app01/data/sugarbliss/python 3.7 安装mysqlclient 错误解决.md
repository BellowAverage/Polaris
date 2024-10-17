
--- 
title:  python 3.7 安装mysqlclient 错误解决 
tags: []
categories: [] 

---
Running setup.py install for mysqlclient ... error

### 解决方法

到这个地址下载自己**python版本**对应的资源  

其中cp27对应python2.7 win32表示window32位，win64表示windows64位系统。

我们需要的是这个：

<img alt="" class="has" height="359" src="https://img-blog.csdnimg.cn/20191121175034377.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N1Z2FyYmxpc3M=,size_16,color_FFFFFF,t_70" width="968">

一定要下载**对应的版本**才能成功，对应的**python**可以到**cmd**里输入**python**查看

<img alt="" class="has" height="153" src="https://img-blog.csdnimg.cn/20191121180126585.png" width="1003">

 

下载完成后**进入下载的目录下，然后使用pip install mysqlclient包名.whl**

**比如：pip install mysqlclient-1.4.5-cp37-cp37m-win32.whl**

<img alt="" class="has" height="74" src="https://img-blog.csdnimg.cn/20191121175603352.png" width="737">

然后就**Successfully**了 ，就可以愉快的安装**mysqlclient**了。

 

 

 
