
--- 
title:  Linux搭建Apache（秒懂超详细） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**努力不一定有回报，但一定会有收获加油！一起努力，共赴美好人生！** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 **♥️小刘私信可以随便问，只要会绝不吝啬，感谢CSDN让你我相遇！** 


镜像

网址:www.centos.org下载点，其文章包含两个镜像，可私聊博主进行获取，不懂可以私信点个赞吧谢谢大家！！！



**目录**



























### 一、准备工作

用到的VMware版本为17.0.1

系统为centos7

采用的是源码包安装搭建Apache环境

### 二、开始搭建

#### 1.查看是否安装httpd

```
rpm -qa | grep httpd
```

效果：

<img alt="" height="1094" src="https://img-blog.csdnimg.cn/ffb61fe844554b259ac72f1388e2cdf9.png" width="1200">

并没有安装任何的httpd

#### 2.跳转路径，弹出镜像

```
cd
eject

```

效果：

<img alt="" height="333" src="https://img-blog.csdnimg.cn/ffb6c342c6484041b1af44813ef82697.png" width="1200">

<img alt="" height="519" src="https://img-blog.csdnimg.cn/8705c85aa8f74fb8a8ece44ccb771023.png" width="1041">

没有结果，查看虚拟机设置，发现已经弹出

#### 3.重新挂载镜像并且进入安装路径

```
mount /dev/sr0   /media/
cd /media/Packages
```

效果：

<img alt="" height="689" src="https://img-blog.csdnimg.cn/7da222db188d4cb980c685930bbc9533.png" width="1200">

进入以后就可以进行源码安装了

#### 4.安装所需文件

```
rpm -ivh apr-1.4.8-3.el7.x86 64.rpm
rpm -ivh apr-devel-1.4.8-3.el7.x86 64.rpm
rpm -ivh cyrus-sasl-devel-2.1.26-20.el7 2.x86 64.rpm
rpm -ivh expat-devel-2.1.0-8.el7.x86 64.rpm
rpm -ivh libdb-devel-5.3.21-19.el7.x86 64.rpm
rpm -ivh openldap-devel-2.4.40-13.el7.x86 64.rpm
rpm -ivh apr-util-devel-1.5.2-6.el7.x86 64.rpm
rpm -ivh apr-util-1.5.2-6.el7.x86 64.rpm
rpm -ivh pcre-devel-8.32-15.el7 2.1.x86 64.rpm
rpm -ivh pcre-8.32-15.el7 2.1.x86 64.rpm
```

效果

<img alt="" height="289" src="https://img-blog.csdnimg.cn/955a5291a38e4d3a87a225972752d7ed.png" width="822">一条一条执行上面所有命令，即可

#### 5.更换httpd镜像

```
cd
eject
mount /dev/sr0 /media
cd /media
ls
```

效果

```
tar zxf http
```

<img alt="" height="130" src="https://img-blog.csdnimg.cn/4767f5f497a640018825efc0ef77cd52.png" width="1013">

<img alt="" height="175" src="https://img-blog.csdnimg.cn/fd15c46cdbf14a0daa445984419fdb08.png" width="1012">

可以看到我们的镜像挂载上来了，下面也有压缩包



#### 6、解压包

```
tar zxf httpd-2.4.25.tar.gz -C  /usr/src
```

效果：

<img alt="" height="93" src="https://img-blog.csdnimg.cn/57b54b7c32874d7286847a8f8f8a84dc.png" width="1200">

将httpd文件解压到/usr/src中

#### 7.开启功能并且使用make和make install进行编译安装

```
cd /usr/src/httpd-2.4.25.tar.gz
./configure --prefix=/usr/local/httpd --enable-so --enable-rewrite --enable-charset-lite --enable-cgi &amp;&amp; make &amp;&amp; make install
```

效果：

<img alt="" height="1130" src="https://img-blog.csdnimg.cn/a869ecbb30fe43108f0bc738b58a1431.png" width="1200">

#### 8、关闭障碍

1.防火墙

2.SELinux

```
systemctl stop firewalld.service  //关闭防火墙
setenforce 0     //关闭SELinux

```

#### 9.绝对路径开启服务

```
/usr/local/httpd/bin/apachectl start
```

效果

<img alt="" height="179" src="https://img-blog.csdnimg.cn/4d2e0cf285a64ab8bba3d4c0716b262c.png" width="1200">

### 10、最后浏览器访问回环地址：127.0.0.1

<img alt="" height="626" src="https://img-blog.csdnimg.cn/e8cf0f929a8444b9acc495682fb104f3.png" width="1200">

成功！！！！

>  
 ♥️关注，就是我创作的动力 
 ♥️点赞，就是对我最大的认可 
 ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 

