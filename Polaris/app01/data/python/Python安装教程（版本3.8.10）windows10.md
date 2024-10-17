
--- 
title:  Python安装教程（版本3.8.10）windows10 
tags: []
categories: [] 

---
        Python目前已支持市面上的各大主流操作系统，在Linux、Unix、Mac系统已经自带Python环境，本章将介绍在Windows系统上安装Python。一般下载 executable installer，x86 表示是 32 位的机器，x86-64 表示 64 位的机器。

>  
     本章系统为：Windows10，Python版本为：3.8.10 


**目录**























##  一、Python下载与安装

        前往Python官网，目前Windows系统适配的最新Python版本为3.11.0，我们这里安装的是3.8.10。有其他需求，安装流程基本一致。

###  (一). Python下载

#### **1、进入Python官网：**[]

<img alt="" height="332" src="https://img-blog.csdnimg.cn/e2d6fd95a8c14ca09e415db3f12fa260.png" width="630">

** **

#### **2、选择版本下载**

2020-01-01，Python官网已经停止维护Python2.7版本；

​官方推荐：使用Python3.X系列版本（不向下兼容python2.X版本）；

本此使用：Python3.8.10版本。

>  
 下载地址： 


<img alt="" height="237" src="https://img-blog.csdnimg.cn/54a7ed074147445f88888fd8f9d66cfb.png" width="636">



#### **3、安装**

**（1）双击安装包，进行安装。**

<img alt="" height="122" src="https://img-blog.csdnimg.cn/4e443aefc5d94fafa06e04b3fa7b0961.png" width="644">

** （2）选择自定义安装**

        提示：勾选Add Python 3.8 to PATH，这样就不用自行配置环境变量，程序会自动配置；

        注意：是将PATH勾选后，再点击Customize installation进入到下一步。如下图：

<img alt="" height="378" src="https://img-blog.csdnimg.cn/5b836df8addb491b86829ed4ae768a8b.png" width="615">

 

**（3）进入Optional Features**

        这个界面全部勾选即可，点击**Next**； 

<img alt="" height="408" src="https://img-blog.csdnimg.cn/166af42c6e11497496bcf352a021ee7a.png" width="663">

 

**（4）选择安装路径**

        注意：这里的默认的安装路径仍然是C盘。我们需要更改为自己想要安装的盘符，如D盘、E盘等。

        注意：要想不安装在C盘，请换安装位置！！！！！

<img alt="" height="403" src="https://img-blog.csdnimg.cn/f50a4d8205b944b689a846d3a92e32ca.png" width="655">

        前面是默认的勾选需要，也可以勾选前5个，我这里勾选的就是前5个。

        安装位置选择的是D盘。路径是：D:\Python\Python38

<img alt="" height="408" src="https://img-blog.csdnimg.cn/f917c78a5fa7432ab5a4974c09f90555.png" width="663">



** （5）等待安装、安装成功如下：**

<img alt="" height="360" src="https://img-blog.csdnimg.cn/8a16685d41ab45e88d9ba026d6749554.png" width="627">

 

###  （二）验证是否安装成功

**        1、按住Win键+R键，输入cmd。点确定进入CMD界面。**

<img alt="" height="272" src="https://img-blog.csdnimg.cn/d631cf02fc76414990c74e94a543f393.png" width="513">

**         2、输入Python，查看版本号**

>  
 输入：python -V 


        如果能够查看到版本号，证明安装成功！

<img alt="" height="104" src="https://img-blog.csdnimg.cn/07a0e4a1e6b24402a6e69a2dcc44ae38.png" width="456">

 

** 3、查看python位置**

>  
 输入：where python 


以上，就完成了Python环境的搭建。就可以进行python代码的编写了！到目前为止，就已经可以应付课上的开发任务了。





以下的内容，如果需要的话，可以自行根据相关教程进行学习。



## 二、集成开发环境安装（如果需要的话）

### （一）配置国内镜像

        默认情况下 pip 使用的是国外的镜像，在下载的时候速度非常慢，建议配置国内镜像。

        以下两个学习地址，用其中一个即可。

>  
 学习地址1： 


>  
 学习地址2： 


### （二）安装集成开发环境

        python自带了IDLE集成开发环境，可以进行集成开发，目前比较受欢迎的集成开发软件还有VScode，PyCharm。可根据自己需求进行下载。

        提示：我们已经完成了Python安装，以下的IDE安装，直接安装软件即可，不用重复安装python。



>  
 VScode安装： 
  


>  
 PyCharm安装： 
  


 

以上就是本章的Python安装教程了。


















