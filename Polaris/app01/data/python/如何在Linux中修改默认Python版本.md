
--- 
title:  如何在Linux中修改默认Python版本 
tags: []
categories: [] 

---


#### 文章目录
- - - <ul><li>- - 


## 前言

如果你在Linux mint上安装了多个Python版本，你可能会发现系统默认使用的Python版本与您想要使用的版本不同。例如：我在linux mint中安装了anaconda，如下图所示，当我在终端下输入“python”时，默认启动的为anaconda中的python。假如我需要输入python时，默认开启的是python2.7。输入python3时再启动anaconda自带的python该怎么办呢？本文将介绍如何更改默认Python版本，以及如何在终端中指定特定的Python版本。 <img src="https://img-blog.csdnimg.cn/e61a3e542dfc4a1d86f61a5dbb2c0820.png#pic_center" alt="在这里插入图片描述">

## 解决方法

### 1.确定系统当前默认的python的位置

在终端中输入以下命令，可知道当前输入python所指向的路径。

```
which python

```

在此处我默认指向的是anaconda下的python。 <img src="https://img-blog.csdnimg.cn/cbd8e50d3bcd413db2da67af059cc5ec.png#pic_center" alt="在这里插入图片描述">

### 2.用python3启用Anaconda下的python

第一步中我们已经知道了anaconda下python的路径是在/root/anaconda/bin/python下的。 我们可以在终端中继续用vim打开“~/.bashrc”文件

```
vim ~/.bashrc

```

在文件末尾添加以下行

```
alias python3=/root/anaconda/bin/python

```

保存并关闭文件，然后输入以下命令以使更改生效

```
source ~/.bashrc

```

在终端中输入“python3”可测试出结果符合要求 <img src="https://img-blog.csdnimg.cn/5a8ea0d42d134d46937b5470772969d7.png#pic_center" alt="在这里插入图片描述">

### 3.用python启用系统下的python2.7

如果你希望用python命令启动Python2，可以按照以下步骤操作：

首先，使用以下命令在系统中安装Python2：

```
sudo apt-get install python2.7

```

然后，在终端中用vim打开“~/.bashrc”文件：

```
vim ~/.bashrc

```

在文件末尾添加下面行：

```
alias python=python2.7

```

保存并关闭文件，然后输入以下命令以使更改生效：

```
source ~/.bashrc

```

现在，当您在终端中输入“python”时，它将默认指向Python2版本 <img src="https://img-blog.csdnimg.cn/b6300bcfecd94c85aba63ac3cfb6d36c.png#pic_center" alt="在这里插入图片描述">

## 总结

在Linux系统中，你可以轻松更改默认Python版本，以便在终端中使用你喜欢的版本。如果你不确定要使用哪个版本，可以使用“which python”命令查找系统当前默认的Python版本。本文主要是依赖alias进行重定义而实现的。
