
--- 
title:  Linux系统下Python的下载与安装 
tags: []
categories: [] 

---
## Linux系统下Python的下载与安装

### 1- 下载安装前准备

>  
 **linux中需提前安装前置依赖环境** 命令如下： yum install wget zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make zlib zlib-devel libffi-devel -y 


<img src="https://img-blog.csdnimg.cn/57bd2cea0d6f463196fb2c36a89cfa53.png#pic_center" alt="在这里插入图片描述">

### 2- 下载Python程序

#### 2.1- 获取python程序源码
1. **进入python官网（），找到linux系统的安装包** <img src="https://img-blog.csdnimg.cn/0643d2bd15694bd69ceeed2e150b852a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a2683239e5e749e9aa1aafa64b95b14f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5af53d1f29de43e6a2abbbfaa09862f7.png" alt="在这里插入图片描述">1. **Gzipped source tarball上右键，选择复制链接地址** <img src="https://img-blog.csdnimg.cn/73e0633d05b74e818fe89f4612bd2875.png" alt="在这里插入图片描述">
#### 2.2- linux终端中下载源码包

>  
 wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz 


<img src="https://img-blog.csdnimg.cn/f88da1b4210b4a789c690d965aed61a0.png" alt="在这里插入图片描述">

### 3- 安装pyhton

#### 3.1- 解压源码包

1.**查看下载的源码包**

>  
 [root@localhost ~]# ls -l 


<img src="https://img-blog.csdnimg.cn/a4c9f84948c44e20921bf6911b66c745.png" alt="在这里插入图片描述"> 2. **对压缩包进行解压**

>  
 tar -xvf Python-3.11.1.tgz 


<img src="https://img-blog.csdnimg.cn/b6a0ce11aa8d4f418cdecd471d7f815c.png" alt="在这里插入图片描述">

#### 3.2- 编译和安装
1. **进入解压后目录**
>  
 [root@localhost ~]# cd Python-3.11.1/ 


<img src="https://img-blog.csdnimg.cn/f3e2f22cc3dc46678650550b95580b68.png" alt="在这里插入图片描述">
1. **配置源码编译后的安装路径**
>  
 ./configure --prefix=/usr/local/python3.11 


<img src="https://img-blog.csdnimg.cn/2f53b3d52af04ded897f42ac3fbeaec3.png" alt="在这里插入图片描述">
1. **开始编译和安装（大约10分钟）**
>  
 make &amp;&amp; make install 


<img src="https://img-blog.csdnimg.cn/d3fd83610b5c415eb177486894095ebb.png" alt="在这里插入图片描述">
1.  **编译完成后，cd配置的安装路径下，并查看文件夹内容 我这里配置的安装路径:/usr/local/python3.11/** <img src="https://img-blog.csdnimg.cn/f3bb251a96f14484ae240d57ec945c29.png" alt="在这里插入图片描述"> 1.  **查看bin目录下是否有python3.11，此时已经完成python安装** 
<img src="https://img-blog.csdnimg.cn/02f52d336f1d43788b4e538bcec8c6b1.png" alt="在这里插入图片描述">

### 4- 创建软链接
- ****此时python环境已经安装成功，但为了使用方便，需删除linux自带的旧版pyhton环境，并为新版本python创建软链接****
#### 4.1- 删除旧版Python环境
1. **linux系统中默认安装python2版本环境，目录在/usr/bin/python/下**
>  
 [root@localhost bin]# /usr/bin/python 


<img src="https://img-blog.csdnimg.cn/14fee8d03a29430288cfe12d9b81ba62.png" alt="在这里插入图片描述">
1. **输入exit()回车退出python环境后，删除python2版本**
>  
 [root@localhost bin]# rm -f /usr/bin/python 


#### 4.2- 创建软链接
1. **将新安装的python3.11版本链接至/usr/bin/python/**
>  
 [root@localhost bin]# ln -s /usr/local/python3.11/bin/python3.11 /usr/bin/python 

1. **输入python进行验证** <img src="https://img-blog.csdnimg.cn/0b997f284f2b4657a48a182c982daae2.png" alt="在这里插入图片描述">
### 5- 修复yum程序
- ****linux系统中yum程序默认使用python2版本，现在将最新版python顶替了python2版本，所以要修改yum相关配置，以确保python完成安装的同时，yum程序运行不会收到影响，修改如下：****1. **修改/usr/libexec/urlgrabber-ext-down，修改后:wq保存退出**
>  
 [root@localhost bin]# vi /usr/libexec/urlgrabber-ext-down 


<img src="https://img-blog.csdnimg.cn/c5e80b434d2a4acf9de3cb401d97f319.png" alt="在这里插入图片描述">
1. **修改/usr/bin/yum文件，修改后:wq保存退出**
>  
 [root@localhost bin]# vi /usr/bin/yum 


<img src="https://img-blog.csdnimg.cn/e301e70cf1a94bdaaf6f7ee3f9bf326a.png" alt="在这里插入图片描述">

## Linux系统安装Pyhthon环境大功告成，冲吧！
