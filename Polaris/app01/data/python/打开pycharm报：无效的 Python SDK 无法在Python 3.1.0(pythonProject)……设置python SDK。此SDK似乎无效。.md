
--- 
title:  打开pycharm报：无效的 Python SDK 无法在Python 3.1.0(pythonProject)……设置python SDK。此SDK似乎无效。 
tags: []
categories: [] 

---
打开pycharm弹出这个提示

**无效的 Python SDK 无法在Python 3.1.0(pythonProject)……设置python SDK。此SDK似乎无效。**

<img alt="" height="871" src="https://img-blog.csdnimg.cn/9936e044a59244828b2c0a9416dc4858.png" width="1200">** 大概的原因是Python.exe的路径找不到了，**

**解决方法如下：**

1，关掉pycharm工具。

2，进入上面弹框中的路径（该环境路径下），我这里的是C:\Users\91423\PycharmProjects\pythonProject\venv\Scripts

进入这个路径后，看到有2个文件，分别是：python.exe和pythonw.exe

<img alt="" height="499" src="https://img-blog.csdnimg.cn/ad0cde1f22824987a0202aa95be68391.png" width="939">

3，进入自己电脑上python目录，看到也有这2个文件

<img alt="" height="494" src="https://img-blog.csdnimg.cn/b40704ee03f94aaf872207237e405d5c.png" width="948">

4，我们把python目录下的python.exe和pythonw.exe这2个文件复制一下，然后粘贴到上面第2步中该环境目录下的位置，替换掉之前的2个文件。

5，重新再启动pycharm，问题解决。

 

 
