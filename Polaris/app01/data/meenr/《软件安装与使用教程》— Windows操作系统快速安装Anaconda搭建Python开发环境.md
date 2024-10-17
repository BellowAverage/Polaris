
--- 
title:  《软件安装与使用教程》— Windows操作系统快速安装Anaconda搭建Python开发环境 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- - - <ul><li>- - <ul><li>- 


### 关于Anaconda

Anaconda是一个开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项。 包含了大量的科学包，一次安装减少了后续很多再去安装第三方包和依赖等。Anaconda 个人版是世界上最受欢迎的 Python 分发平台，在全球拥有超过 2500 万用户。Anaconda 是 Python 数据科学开发的首选平台。开源个人版（分发版）是在单台机器上执行 Python/R 数据科学和机器学习的最简单方法。它是为独立从业者开发的工具包，可以使用数千个开源包和库。

### 下载Anaconda

本文提供的Anaconda安装包是Python3.7版本的，有官网、微信公众号和百度网盘三个下载Anaconda个人版安装包的渠道，下载地址如下： （注：官网服务器在国外，如下载速度较慢可使用另外两个地址或联系作者帮忙带下） 下载地址1： https://www.anaconda.com/products/individual 下载地址2： https://mp.weixin.qq.com/s/vuhCgLXN-MB6FS2s2hvV9Q 下载地址3： 链接：https://pan.baidu.com/s/1ahYDAv31pO-qnxdwjswCZQ 提取码：xvx8

============================================

**建议下载安装Python版本为<mark>3.6~3.9</mark>的Anaconda环境，Anaconda版本与Python版本及操作系统之间对照关系，可参见另一篇文章：**  https://blog.csdn.net/meenr/article/details/121453499

==========================================================

### 安装Anaconda

本文仅提供Windows系统安装步骤，如在安装中有任何问题或者需要Mac及Linux系统安装指导欢迎留言评论。

#### 安装步骤

下载完成后鼠标选中<mark>python3.7Anaconda3-2019.07-Windows-x86_64.exe</mark>，右键选择**以管理员身份运行** ① <img src="https://img-blog.csdnimg.cn/d9b9e018c7c6491592f7248221d677cd.png" alt="在这里插入图片描述"> ② 安装程序运行后，可根据以下图示进行操作： <img src="https://img-blog.csdnimg.cn/9c405be527a346ef993309bfd28f5a7d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5omR6YCa5Lq7,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="390" height="320"> ③ <img src="https://img-blog.csdnimg.cn/6b0db6916ae0428ea26a810496931995.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5omR6YCa5Lq7,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="390" height="320">

④ <img src="https://img-blog.csdnimg.cn/ca9bdfa4131d4cdc95cd8231f66759b2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5omR6YCa5Lq7,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="390" height="320"> ⑤ **安装路径推荐：D:\software\Anaconda3** <img src="https://img-blog.csdnimg.cn/2bdc86ef11764557a7b03a9934e5432d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5omR6YCa5Lq7,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="390" height="320"> ⑥ <img src="https://img-blog.csdnimg.cn/6d98cedf8f714a418a8ffec917902f9f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5omR6YCa5Lq7,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="390" height="320"> ⑦ 等待安装完成

#### 安装问题与注意事项

–【随时更新】–

##### 问题1

**第⑥步两个选项都勾选上，后续无需再手动配置环境变量。**新手建议只安装一个版本的Python，推荐Python3.6~Python3.9版本，如安装Anaconda前已安装Python官方解释器，建议卸载干净后再装Anaconda，只用Anaconda即可。

##### 问题2

如计算机上已安装python3.7则会在最后一步选择默认环境时给出 冲突的提示，建议卸载原python，并重启计算机后再安装Anaconda。新手建议只安装一个版本的Python，推荐Python3.6~Python3.9版本

<img src="https://img-blog.csdnimg.cn/fee55a79496949518dd7e48098f8c667.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5omR6YCa5Lq7,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="390" height="320">

<img src="https://img-blog.csdnimg.cn/b87b08158703445d8998cfd136a93e31.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5omR6YCa5Lq7,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="390" height="320">

<img src="https://img-blog.csdnimg.cn/0efe78a91aa14ccfabc71192ea2603c6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5omR6YCa5Lq7,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" width="390" height="320">

安装完毕，后建议重启一次计算机。下面一篇文章将介绍Python开发常用开发工具 Spyder、Jupyter和Pycharm的使用。 文章地址：  https://blog.csdn.net/meenr/article/details/121503827
