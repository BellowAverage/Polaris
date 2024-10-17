
--- 
title:  配置pcl（点云）环境遇到的问题（华南理工大学三维人体建模与测量） 
tags: []
categories: [] 

---
一. linux下sudo apt-get update和upgrade的区别

那我们要怎么安装呢？在ubuntu下，我们维护一个源列表，源列表里面都是一些网址信息，这每一条网址就是一个源，这个地址指向的数据标识着这台源服务器上有哪些软件可以安装使用。 sudo gedit /etc/apt/sources.list 在这个文件里加入或者注释（加#）掉一些源后，保存。这时候，我们的源列表里指向的软件就会增加或减少一部分。 接一下要做的就是： sudo apt-get update 这个命令，会访问源列表里的每个网址，并读取软件列表，然后保存在本地电脑。我们在新立得软件包管理器里看到的软件列表，都是通过update命令更新的。

update后，可能需要upgrade一下。 sudo apt-get upgrade 这个命令，会把本地已安装的软件，与刚下载的软件列表里对应软件进行对比，如果发现已安装的软件版本太低，就会提示你更新。如果你的软件都是最新版本，会提示： 升级了 0 个软件包，新安装了 0 个软件包，要卸载 0 个软件包，有 0 个软件包未被升级。 总而言之，update是更新软件列表，upgrade是更新软件。

二. ubuntu18.04LTS换源，解决更新失败问题

**第一步**：使用一个Editor编辑文件，在此使用Vim进行编辑

```
sudo vim /etc/apt/sources.list

```

**第二步**：修改该文件，将该文件中原来的内容全部删除，添加如下内容（此处以阿里源作为示例）

```
# 阿里源</code>`deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse``deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse``deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse``deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse``deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse``deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse``deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse``deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse``deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiversedeb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multivers`然后使用下面命令更新一下更新一下
</pre> 
<pre><code>sudo apt update &amp;&amp; sudo apt upgrade
```

等待其更新完成即可。

三. ubuntu下cmake的GUI界面（cmake和cmake-gui要一起安装）

1. 安装cmake的GUI界面

```
sudo apt-get install cmake-qt-gui
```

2. 打开界面

```
cmake-gui
```

四. make -j4    j4为编译时使用4线程

五.PCL与VTK编译问题 因为我需要编译PCL GPU版本(如果使用ubuntude 18.04arm架构,xavier、nano)，所以选择按照了文章的源码编译过程，我编译的版本是**VTK8.2和PCL1.11.0**。 VTK正常编译，PCL编译出错

[ 23%] Linking CXX executable ../bin/pcl_pcd_change_viewpoint /usr/local/lib/libvtkpng-8.2.so.1: undefined reference to `png_init_filter_functions_neon' collect2: error: ld returned 1 exit status tools/CMakeFiles/pcl_pcd_change_viewpoint.dir/build.make:177: recipe for target 'bin/pcl_pcd_change_viewpoint' failed make[2]: *** [bin/pcl_pcd_change_viewpoint] Error 1 CMakeFiles/Makefile2:7232: recipe for target 'tools/CMakeFiles/pcl_pcd_change_viewpoint.dir/all' failed make[1]: *** [tools/CMakeFiles/pcl_pcd_change_viewpoint.dir/all] Error 2 make[1]: *** Waiting for unfinished jobs....

看上去像是vtk的库编译出了问题，查到了类似问题undefined reference to `png_init_filter_functions_neon’

128 /*#  if (defined(__ARM_NEON__) || defined(__ARM_NEON)) &amp;&amp; \*/  129 #   if defined(PNG_ARM_NEON) &amp;&amp; (defined(__ARM_NEON__) || defined(__ARM_NEON)) &amp;&amp; \ 在VTK源码下的/ThirdParty/png/vtkpng中找到了pngpriv.h，讲128行替换成129行，之后重新编译VTK，然后再编译PCL，成功。

如何使用的是ubuntu的x86_64架构，怎不会出现错误，不需要伤处文件的修改。

六. Ubuntu16.04使用命令行安装java1.8（超简单）

sudo apt install openjdk-8-jre-headless

七.安装cmake3.22.1

  

官网下载页：

<img alt="" height="316" src="https://img-blog.csdnimg.cn/8f720e06106d48049515cce80eebc22e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcGFzc2lvbi1tYQ==,size_20,color_FFFFFF,t_70,g_se,x_16" width="1089">

下载这两个对应的版本

 要安装cmake时，必须同时安装cmake-gui(要一起安装，不然两个的版本不一致)

cmake-gui是进行一张图像页面，相当于cmake。  cmake-gui依赖于3.x版本或者4.x版本的Qt，所以如果原先没有安装QT的需要先安装。  安装4.x版本Qt：sudo apt-get install qt4-default

  然后执行配置脚本，此时cmake和cmake-gui会同时安装。

```
./bootstrap --qt-gui --qt-qmake=/usr/bin/qmake
```


|
