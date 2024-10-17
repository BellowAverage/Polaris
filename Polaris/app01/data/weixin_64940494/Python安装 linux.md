
--- 
title:  Python安装 linux 
tags: []
categories: [] 

---
        上一篇文章中我们演示了Python在windows环境下的安装流程，本文就介绍一下python在Linux环境下是如何安装的。

        服务器环境：Linux CentOS 7.4

        Python版本：3.10.6

**一、安装Python依赖**

        这里我们直接通过yum安装，输入下列命令进行安装。

>  
 yum install zlib-devel bzip2-devel opssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc libffi-devel 


**二、安装Python**

1. 在Python官网上找到Linux环境的Python源码安装包，下载地址：，复制下载连接。

<img alt="" height="255" src="https://img-blog.csdnimg.cn/ea0f1577d60145ada5dcaf10008b92db.png" width="485">

进入到对应的python版本下。

<img alt="" height="417" src="https://img-blog.csdnimg.cn/8f67f108077e472ea369055fd97ef459.png" width="1200"> 右键&gt;复制链接地址。

2. 在Linux服务器下，通过wget下载安装包，我这里安装包下载的路径是/usr/local/ 。

>  
 wget  


 3. 下载完之后，tar解压安装包。

>  
 tar -xvf Python-3.10.6.tgz 


4. 进入到解压文件中，进行预配置,配置路径为 /usr/local/python/。

>  
 cd Python-3.10.6 
 ./configure --prefix=/usr/local/python 


5. 编译&amp;安装

>  
 make &amp; make install 


**三、创建软连接**

1. 修改linux默认的Python版本

Linux系统默认会安装一个Python,命令行中输入python可以看到默认的版本号。

<img alt="" height="83" src="https://img-blog.csdnimg.cn/fec34f534c6d49d8b5f2b16c592f0e5e.png" width="552">

 先删除默认的python安装程序。

>  
 rm -f /usr/bin/python 


2. 将最新的python3.10.6创建软链接。

>  
 ln -s /usr/local/python/bin/python3.10 /usr/bin/python 


创建完软连接之后在输入python,可以看到已经是我们安装的最新版本了。

<img alt="" height="76" src="https://img-blog.csdnimg.cn/873d852993504b74af97b3201aa38f43.png" width="695">

 3. 修改yum依赖默认的python版本

创建软连接后会破坏yum程序的正常使用，yum的代码只兼容python2，所以要用python2的解释器，因此要将python改为python2

>  
 vi /usr/libexec/urlgrabber-ext-down 


将首行的python 改为 python2 

<img alt="" height="87" src="https://img-blog.csdnimg.cn/27088ef7e84d425abee630e964a585a4.png" width="541">

>  
 vi /usr/bin/yum 


 也同样的将首行的python 改为 python2

<img alt="" height="83" src="https://img-blog.csdnimg.cn/336ce8b5259641dbba2ec10640caf5ef.png" width="469">

4. 修改防火墙的python 版本

>  
  vi /usr/bin/firewall-cmd 


将首行的python 改为 python2

<img alt="" height="89" src="https://img-blog.csdnimg.cn/65d08b779d284b589e43b025ad8167c7.png" width="392">

>  
 vi /usr/sbin/firewalld  


<img alt="" height="107" src="https://img-blog.csdnimg.cn/038f16c3cbce4e3c8a34481a48057a49.png" width="578">

         修改完这几个文件之后python的安装已经完成，yum依赖和防火墙的python也都修改成为最新版本的python了。

5. 创建pip3的软连接

        pip是Python包的管理工具。

>  
 ln -s /usr/local/python/bin/pip3.10 /usr/bin/pip3 


        安装第三方包时使用pip3命令
