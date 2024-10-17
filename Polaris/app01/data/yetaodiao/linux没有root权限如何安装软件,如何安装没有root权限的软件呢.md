
--- 
title:  linux没有root权限如何安装软件,如何安装没有root权限的软件呢 
tags: []
categories: [] 

---
linux没有root权限如何安装软件：
1. rpm/deb包安装必须要root权限
2. 网上下载的Linux二进制文件，可以放到自己home目录下（记住要给执行权限，chmod +x）

并配好环境变量（可选），即可运行

3. 拥有源码，可以编译，然后安装到自己home目录下

一般流程都是：

```
./configure --prefix=$HOME/XXXX
make install -j$(lscpu)
```

4. Appimage等打包好的软件文件

给执行权限，放到自己的home目录下，双击就可以像Win下面点开程序一样运行了

<img alt="" height="223" src="https://img-blog.csdnimg.cn/fc886fcd717141fb8bac5654182cca6b.png" width="722">

 

如何安装没有root权限的软件,某些软件可以相关资源完全放在你的用户目录就行，比如pycharm，去找那种解压即用的，如果rpm或deb包就没办法了。

另外还可以找管理员帮忙装得了。

  

 
