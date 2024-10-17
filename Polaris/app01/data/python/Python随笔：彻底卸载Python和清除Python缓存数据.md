
--- 
title:  Python随笔：彻底卸载Python和清除Python缓存数据 
tags: []
categories: [] 

---
## 1.前言

当初安装Python时真是年少无知啊！把他安装在 C 盘了。现在C盘容量告急了，在卸载和迁移软件时发现不知不觉中Python已经快 1 GB 了。于是就打算卸载这个 Python ，在 D盘 再安装一个其他版本的。

## 2.彻底卸载Python

### 2.1

首先在命令行窗口查一下Python的版本

<img alt="" height="136" src="https://img-blog.csdnimg.cn/20200708141036457.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="543">

**如上图，输入python回车，我的是3.7.3版本**

### 2.2

然后就在 这个镜像网站下载对应的安装包



<img alt="" height="107" src="https://img-blog.csdnimg.cn/20200708141329782.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="465">

点进去下载下图红框的那个exe文件

<img alt="" height="169" src="https://img-blog.csdnimg.cn/20200708141450924.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="379">

### 2.3

下载完成后，点击运行，会出现如下界面。为了确保顺利卸载Python，先点击第二个Repair ,修复一下再回来卸载。

<img alt="" height="382" src="https://img-blog.csdnimg.cn/20200708141611270.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="620">

修复完成后可能需要重启电脑，那就重启电脑再回来运行这个安装包，这次点击第三个选项就可以卸载python了。

<img alt="" height="395" src="https://img-blog.csdnimg.cn/2020070814192915.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="642">

##  

## 3.清除python缓存数据

别以为在上面卸载python就完事了，其实上面python的卸载是不会清除缓存数据的，包括第三方库的数据也不会清除的。这时就需要我们手动清除了。

### 3.1 安装目录下的数据

<img alt="" height="485" src="https://img-blog.csdnimg.cn/20200708142255470.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="658">

找的安装的目录，把对应版本的python文件夹删除，我的如上图。

### 3.2 电脑缓存文件夹里的python数据

```
%USERPROFILE%\AppData\Local
```

把上面目录复制到文件管理软件，如下图

<img alt="" height="120" src="https://img-blog.csdnimg.cn/20200708143134965.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="689">

把能找到的python文件夹删除掉，如我找到的  pip ,python，Package Cache文件夹。

<img alt="" height="431" src="https://img-blog.csdnimg.cn/20200708143255588.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="1170">

### 3.3 清除环境变量

卸载时可能有一些环境变量还没有清除的，如我的下面图，还有两个与python3.7.3版本有关的环境变量

<img alt="" height="501" src="https://img-blog.csdnimg.cn/20200708143926432.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="694">

### 3.4 清除注册表数据

win+R 输入 regedit 进入注册表

<img alt="" height="164" src="https://img-blog.csdnimg.cn/20200708144102538.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="316">

找到如下图的路径（先到Software就好，在这个目录下看有没有pythonxxx版本的文件名，找到右键删除即可）

<img alt="" height="84" src="https://img-blog.csdnimg.cn/20200708144225353.png" width="728">

******************************************************************************

2020/7/18 更新

### 3.5 清除Roaming文件夹下python缓存

```
%USERPROFILE%\AppData\Roaming
```

<img alt="" height="162" src="https://img-blog.csdnimg.cn/20200718093547946.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NDYzNzM3,size_16,color_FFFFFF,t_70" width="803">

把能找到的与 python文件夹删除掉，如python，pip等。

 

 

 
