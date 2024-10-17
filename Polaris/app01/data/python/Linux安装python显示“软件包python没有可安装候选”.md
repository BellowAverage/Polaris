
--- 
title:  Linux安装python显示“软件包python没有可安装候选” 
tags: []
categories: [] 

---
在Linux中安装python时，调用“sudo apt-get install python”命令出现以下问题： **sudo apt-get install python [sudo] lyx 的密码： 正在读取软件包列表… 完成 正在分析软件包的依赖关系树… 完成 正在读取状态信息… 完成 没有可用的软件包 python，但是它被其它的软件包引用了。 这可能意味着这个缺失的软件包可能已被废弃， 或者只能在其他发布源中找到 然而下列软件包会取代它： python2-minimal:i386 python2:i386 python2-minimal python2 dh-python 2to3 python-is-python3 E: 软件包 python 没有可安装候选** <img src="https://img-blog.csdnimg.cn/ab70cd29d62a436da5c3acf158169c3f.png" alt="在这里插入图片描述">

解决方法，改用下面的命令安装（我的ubuntn版本是20.4）

```
sudo apt-get install software-properties-common

```

安装完后想要利用“pip”查看安装列表，需要先安装pip

```
sudo apt-get install python-pip

```

有了pip之后，如果直接输入“pip list”会显示错误，还需要继续更新到pip3 <img src="https://img-blog.csdnimg.cn/efd18d34b8c940a7b6c45938d9de0d51.png" alt="在这里插入图片描述"> 输入命令：

```
sudo apt install python3-pip

```

之后就可以直接利用“pip list”查看安装的包了 <img src="https://img-blog.csdnimg.cn/363bded7b4334ff0b191b02d6088b88b.png" alt="在这里插入图片描述">
