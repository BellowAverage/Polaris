
--- 
title:  windows下安装protobuf for python 
tags: []
categories: [] 

---
安装好麻烦，尤其是我不能联网 不能使用ezsetup

记录下 我的安装过程~

1、去code.google.com下载protobuf2.5.0，我下载了两个，一个是源码，一个是win32。源码用于安装环境，win exe可以直接编译proto文件

2、安装环境的第一步是，安装protoc 编译器。 我按照install.txt  readme.txt 中的安装的，找到python部分。

3、用cmd进入解压的目录，网上是这样说的，

 安装protobuf编译器

 ./configure --prefix=dist; make; make install; 配置bin路径。可是这个是Linux环境下的。

 我的步骤是： sh configure (我的configure指令不能直接用，但是我可以使用sh，不知道是否因为之前装过好多的linux环境)

 make

 make check

 make install

 如果这些都能用的话，那么恭喜你，基本OK了，这个是环境搭建，耗得时间是最多的。如果不行的话，我估计你得搜索下如何能够使用这么指令。

 或者编译C++代码，这个我不会。install中有教程。

 4、然后cd python 这个目录下，有setup.py 和ezsetup.py 我用的是setup.py因为我连不上网。

  我的步骤是：

 python setup.py build

 python setup.py test

 python setup.py install

 我最开始没有使用build，所以一直安装不成功。So，要 build and run the test, then install

  

 我的电脑到这里就成功了。环境配置 太恶心了，尤其是我的还连不上网。

 心得：好好看readme.txt install.txt等文档，耐下心仔细看。都有说明，找到你想要的部分。
