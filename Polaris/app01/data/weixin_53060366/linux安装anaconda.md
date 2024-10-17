
--- 
title:  linux安装anaconda 
tags: []
categories: [] 

---
## linux安装anaconda

### 1、下载anaconda：

Conda 是一个强大的包管理器和环境管理器，您可以在 Windows 的 Anaconda Prompt 或 macOS 或 Linux 的终端窗口中与命令行命令一起使用。

换句话说，我把Conda理解为前端的npm或yarn，后端的maven。它们都是用来管理依赖包。
-  可以从官网下载包，然后上传到服务器。 -  也可以直接服务器上下载： 
```
wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh

```

### 2、安装anaconda：

```
chmod +x Anaconda3-2023.03-1-Linux-x86_64.sh 
./Anaconda3-2023.03-1-Linux-x86_64.sh

```

按`ENTER`继续，一路回车键继续。

有 yes|no 的地方就输入yes，其他地方继续按回车就完事了。

```
Thank you for installing Anaconda3!

===========================================================================

```

到这里就是完成了。

这时关闭终端，再打开终端会在前面显示（base）表示安装成功，以后终端会默认打开在conda环境。

<img src="https://img-blog.csdnimg.cn/b38b27ec5fa6455ea40818908e861e6a.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/6ddf4448e7f6405eab5d5cf7f76b1902.png#pic_center" alt="在这里插入图片描述">

输入python -V 可以查看Python版本。

<img src="https://img-blog.csdnimg.cn/3164bd3c4ce54ee78830caf5fba85ba8.png#pic_center" alt="在这里插入图片描述">

更多anaconda的使用命令，可以查看这篇文章。****
