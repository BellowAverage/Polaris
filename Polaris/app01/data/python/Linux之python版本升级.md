
--- 
title:  Linux之python版本升级 
tags: []
categories: [] 

---
## 一、前言

  升级glibc的时候根据INSTALL升级说明，要求python版本3.4以上。所以需要对python版本进行升级。centos7默认安装的python版本为2.7.5，python通过yum安装也只能安装2.7.5版本，python3可以通过yum安装3.6.8版本。如果需要更高的版本，只能通过源码编译安装。此博文介绍源码安装方式升级python和python3版本，源码编译安装要求操作系统已经安装了gcc。环境说明如下：
- 操作系统：centos7.6- python版本：升级前版本2.7.5，升级后2.7.18- python3版本：升级前3.6.8，升级后版本3.8.8
## 二、python安装步骤

### 1、查看当前python版本

>  
 [root@s143 ~]# python -V Python 2.7.5 


### 2、yum安装python

>  
 [root@s143 ~]# yum install -y python2 Loaded plugins: fastestmirror Loading mirror speeds from cached hostfile * base: mirrors.aliyun.com * extras: mirrors.aliyun.com * updates: mirrors.aliyun.com Package python-2.7.5-90.el7.x86_64 already installed and latest version Nothing to do 


### 3、yum安装python3

>  
 [root@s143 ~]# yum install -y python3 Loaded plugins: fastestmirror Loading mirror speeds from cached hostfile Installed: python3.x86_64 0:3.6.8-18.el7  Dependency Installed: libtirpc.x86_64 0:0.2.4-0.16.el7 python3-libs.x86_64 0:3.6.8-18.el7 python3-pip.noarch 0:9.0.3-8.el7 python3-setuptools.noarch 0:39.2.0-10.el7  Complete! 


## 三、python2升级步骤

### 0、查找需要升级的版本

python官网（包括python和python3所有的版本）查找需要安装或者升级的版本。 <img src="https://img-blog.csdnimg.cn/b43795be3875425c9ae6c6c161e9894a.png" alt="在这里插入图片描述">

### 1、下载python新版本

>  
 [root@s143 opt]# wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz 


### 2、解压软件包

>  
 [root@s143 opt]# tar -zxvf Python-2.7.18.tgz 


### 3、预编译软件包

>  
 [root@s143 opt]# cd Python-2.7.18 [root@s143 Python-2.7.18]# ./configure --prefix=/usr 


### 4、编译软件包

>  
 [root@s143 Python-2.7.18]# make … running build_scripts creating build/scripts-2.7 copying and adjusting /opt/Python-2.7.18/Tools/scripts/pydoc -&gt; build/scripts-2.7 copying and adjusting /opt/Python-2.7.18/Tools/scripts/idle -&gt; build/scripts-2.7 copying and adjusting /opt/Python-2.7.18/Tools/scripts/2to3 -&gt; build/scripts-2.7 copying and adjusting /opt/Python-2.7.18/Lib/smtpd.py -&gt; build/scripts-2.7 changing mode of build/scripts-2.7/pydoc from 644 to 755 changing mode of build/scripts-2.7/idle from 644 to 755 changing mode of build/scripts-2.7/2to3 from 644 to 755 changing mode of build/scripts-2.7/smtpd.py from 644 to 755 /usr/bin/install -c -m 644 ./Tools/gdb/libpython.py python-gdb.py 


### 5、安装软件包

>  
 [root@s143 Python-2.7.18]# make install 


### 6、检查升级后的版本

>  
 [root@s143 Python-2.7.18]# python -V Python 2.7.18 


## 四、python3升级步骤

### 1、下载安装包

>  
 [root@s143 opt]# wget https://www.python.org/ftp/python/3.8.8/Python-3.8.8.tgz 


### 2、解压软件包

>  
 [root@s143 opt]# tar -zxvf Python-3.8.8.tgz 


### 3、预编译

注意在编译结束后会有提示"If you want a release build with all stable optimizations active (PGO, etc),please run ./configure --enable-optimizations"，加上–enable-optimizations预编译的话后续编译会报错“Could not import runpy module ”，原因是gcc版本太低，enable-optimizations参数要求gcc版本8.1.0以上。

>  
 [root@s143 opt]# cd Python-3.8.8 [root@s143 Python-3.8.8]# ./configure 


### 4、编译

>  
 [root@s143 Python-3.8.8]# make … if test `uname -s` = Darwin; then  cp python-config.py python-config;  fi 


### 5、编译安装

>  
 [root@s143 Python-3.8.8]# make install … Collecting setuptools Collecting pip Installing collected packages: setuptools, pip Successfully installed pip-18.1 setuptools-40.6.2 


### 6、升级后版本检查

>  
 [root@s143 Python-3.6.10]# python3 -V Python 3.8.8 


## 五、QA

### 1、安装python3.8.8的时候报错zlib not available
- 报错信息：zipimport.ZipImportError: can’t decompress data; zlib not available- 报错原因：没有安装zlib模块- 解决方案：安装zlib模块 [root@s143 bin]# yum install -y zlib*
### 2、安装完python之后yum报错File “/usr/bin/yum”, line 30
- 报错信息：File “/usr/bin/yum”, line 30 <img src="https://img-blog.csdnimg.cn/57cc959f71924fa589a41b87af3ff6ab.png" alt="在这里插入图片描述">- 报错原因：python软连接指向了python3版本，而yum要求python2版本。- 解决方案1：修改python命令软连接到python2 [root@s143 bin]# sln python2 python [root@s143 bin]# python -V Python 2.7.5- 解决方案2：修改/usr/bin/yum文件，将python改为python2 <img src="https://img-blog.csdnimg.cn/2d3b4ddc2f784b3e8bf76d84e4dbf74a.png" alt="在这里插入图片描述">
### 3、安装完成python之后yum安装报错File “/usr/libexec/urlgrabber-ext-down”, line 28
- 报错信息：File “/usr/libexec/urlgrabber-ext-down”, line 28- 报错原因：yum下载程序依赖python2- 解决方案1：修改python命令软连接到python2- 解决方案2：修改/usr/libexec/urlgrabber-ext-down文件，将python改为python2 <img src="https://img-blog.csdnimg.cn/39bba277f54645c3b1b2c04c046498a6.png" alt="在这里插入图片描述">
### 4、升级到python2.7.18后报错No module named rpm
- 报错信息：There was a problem importing one of the Python modules required to run yum. The error leading to this problem was: No module named rpm <img src="https://img-blog.csdnimg.cn/e6f3403854384561b4c197ecbee95b48.png" alt="在这里插入图片描述">- 报错原因：python2.7.18是python2的最新版本，已经移除了对yum的支持，centos8默认使用dnf软件包安装工具。- 解决方案：从其他centos7服务器拷贝一个python2.7.5到服务器/usr/bin目录下，然后重建python软链接。 <img src="https://img-blog.csdnimg.cn/70fd4f90085847f08a01421d8c5d5595.png" alt="在这里插入图片描述">