
--- 
title:  2023最新版Python 3.12.0安装使用指南 
tags: []
categories: [] 

---
## 2023最新版Python 3.12.0安装使用指南

### The Tutorial of Installing the Latest Python Version 3.12.0 for Windows

>  
 Python is a programming language that lets you work quickly and integrate systems more effectively. - www.python.org 


### 1. 安装最新版Python 3.12.0

要进行Python软件开发，首先要安装Python软件包。 本文简要介绍的Python 3最新版3.12.0的安装过程，希望对您有所帮助。

首先，访问Python官网： 在主页上方导航栏，选择**Download**，点击**Python 3.12.0**开始下载。 <img src="https://img-blog.csdnimg.cn/8501fec51b654a40aa3c320df7c81d59.png" alt="在这里插入图片描述">

于是，Chrome浏览器开始下载安装包，在**新版Chrome浏览器**中，下载进程如下图： <img src="https://img-blog.csdnimg.cn/e7cf06b6dec444e6b5aeecc6ddeb3b10.png" alt="在这里插入图片描述">

当下载完毕时，在Windows 10/11的**Downloads**(下载)文件夹里，找到该安装程序：**python-3.12.0-amd64.exe**文件，双击启动安装向导。

<img src="https://img-blog.csdnimg.cn/0ce2b1ba68f241eab54f9f22359aecc9.png" alt="在这里插入图片描述">

为了防止C:盘文件因系统故障或者无意丢失，我们可能需要将Python安装到其它分区（例如D:），于是，选择点击**Customize installation**(定制安装)，以便接下来选硬盘其它分区路径来安装Python。

保留默认勾选项“**Use admin privileges when installing py.exe**”(安装py.exe时使用管理员权限运行)。

在**Optional Features**（可选特性）对话框，保留默认勾选的四个选项，点击Next进入下一步。

<img src="https://img-blog.csdnimg.cn/1738e448c5c9469195da988cea319c99.png" alt="在这里插入图片描述">

在**Advanced Options**(高级选项)对话框中，增加选项**Add Python to environment variables**，即添加Python安装路径到环境变量；同时，为了使用便利，增加选项“**Install Python 3.12 for all users**”(为所有用户安装Python 3.12)；然后，选择”**Customize Install Location**”(定制安装路径)，修改默认路径到**D:\Python312**文件夹。

接下来，点击**Install**开始安装。

<img src="https://img-blog.csdnimg.cn/aff15c9cd3e849fdb1b2bea8a9428289.png" alt="在这里插入图片描述">

进入**Setup Progress**(安装过程), 如下图：

<img src="https://img-blog.csdnimg.cn/2f9c1467fac14a819826bbcc92138e90.png" alt="在这里插入图片描述">

安装过程会拷贝必要的文件，以及预编译Python标准库等；安装完毕后，出现**Setup was Successful**(安装成功)对话框，点击**Close**关闭安装向导。

此刻，已经完成了Python 3.12 for Windows的安装过程。

<img src="https://img-blog.csdnimg.cn/a5bd8a9121064837ab10919eccef9f9f.png" alt="在这里插入图片描述">

### 2. 验证Python安装

考虑到要运行Python, 随即点击左下角搜索栏Type here to search,输入**cmd**, 选择命令行提示符，并点击“**以管理员身份运行**”，如下图。

<img src="https://img-blog.csdnimg.cn/34151334d6d946b181df46142bb1962f.png" alt="在这里插入图片描述"> 在Windows终端命令行提示符，输入以下命令，确认当前安装Python的版本：

```
python –version

```

<img src="https://img-blog.csdnimg.cn/a34502d416314df2a5f523542971d7df.png" alt="在这里插入图片描述"> 接下来，输入**python**, 然后按Enter(回车)，进入Python程序命令行交互模式，出现“**&gt;&gt;&gt;**”提示符。

<img src="https://img-blog.csdnimg.cn/8261dff22266484a997ae6c79f47e2bd.png" alt="在这里插入图片描述"> 输入最简单的Python程序“Hello, world!"，如下命令：

```
&gt;&gt;&gt; print ”Hello, world!”

```

打印到终端窗口，如下所示。 <img src="https://img-blog.csdnimg.cn/29e3b6c285954556b66f8b768c21a1ba.png" alt="在这里插入图片描述"> 成功运行！

这说明Python 3.12.0 安装完毕，并成功搭载在Windows系统上。

### 3. IDLE交互式开发模式

Python安装完毕后，不但可以在Windows命令行(cmd) 使用交互模式，还可以使用安装程序自带的交互式开发工具IDLE。

>  
 IDLE有强大的交互式开发功能。 


在搜索栏输入关键字“IDLE“，可以搜索到**IDLE(Python 3.12 64-bit)**交互开发工具，点击”**以管理员身份运行**“，如下图：

<img src="https://img-blog.csdnimg.cn/f6d910bae476486da7849eb2bf9aabf3.png" alt="在这里插入图片描述">

这样，就打开了IDLE开发程序，如下图：

<img src="https://img-blog.csdnimg.cn/31d3dba761364cf6ab7ab1732975e90c.png" alt="在这里插入图片描述"> 执行最简单的”Hello world”程序，

```
&gt;&gt;&gt; print(“Hello, world!”)

```

同样运行成功！

至此，Python最新版安装程序就安装完毕了。使用Windows终端(cmd)或者IDLE开发工具，都可以启动Python编程工作了。

Python相关博文会持续发布。敬请关注。

喜欢请点赞，以激励我不断推出好文。😊

#### 相关阅读：
1. 1. 1. 1. 1. 