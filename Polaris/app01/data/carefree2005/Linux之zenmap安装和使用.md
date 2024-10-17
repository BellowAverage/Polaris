
--- 
title:  Linux之zenmap安装和使用 
tags: []
categories: [] 

---
## 一、zenmap简介

  Zenmap是一个开源的网络扫描器，它是Nmap的图形用户界面（GUI）版本。Nmap是一个强大的网络扫描工具，用于发现网络上的主机、服务和开放端口。Zenmap通过提供一个直观的界面，使用户能够更容易地使用Nmap的功能。Zenmap提供了一些高级功能，如扫描配置文件管理、扫描配置文件导入和导出、扫描结果导出等。它还提供了一些可视化工具，如拓扑图和端口状态图，以帮助用户更好地理解扫描结果。Zenmap支持多种操作系统，包括Windows、Linux和Mac OS X。它是一个功能强大且易于使用的网络扫描工具，适用于网络管理员、安全专家和普通用户。因为在window环境下新建扫描命令profile和扫描结果对比两个功能点击时都导致程序奔溃，所以博主觉得在linux环境下进行安装测试。环境说明： 操作系统：centos7.6
- zenmap版本：7.94- nmap版本：7.94- python版本：3.6.15
## 二、安装步骤

### 1、安装python3

  python3的安装参考博文。安装完成后检查验证python3的版本。

>  
 [root@s146 x86_64]# python3 -V Python 3.10.10 [root@s146 x86_64]# which python3 /usr/local/bin/python3 


### 2、下载nmap-7.94-1.x86_64.rpm

>  
 [root@s146 opt]# wget https://nmap.org/dist/nmap-7.94-1.x86_64.rpm 


### 3、安装rpmrebuild

>  
 [root@s146 opt]# yum install -y rpmrebuild 


### 4、重新编译nmap-7.94-1.x86_64.rpm

  由于python3和python是两个独立的版本，python3安装后命令为python3，所以我们还需要修改rpm包的内容或者将python命令软链接修改到python3上，考虑到yum命令对python2有依赖，修改了python软链接会导致yum命令无法使用，建议重新编译nmap的rpm包，修改依赖说明和要求。

>  
 [root@s146 opt]# rpmrebuild -enp nmap-7.94-1.x86_64.rpm <img src="https://img-blog.csdnimg.cn/direct/604c2e203a9345d5b68ea17d9a348f45.png" alt="在这里插入图片描述"> 


### 5、安装nmap-7.94-1.x86_64.rpm

  这里记得使用yum方式安装，不要使用rpm命令安装，使用rpm命令安装还是会报错提示python版本不对。

>  
 [root@s146 opt]# cd /root/rpmbuild/RPMS/x86_64/ [root@s146 x86_64]# yum install -y nmap-7.94-1.x86_64.rpm 


### 6、nmap版本验证

>  
 [root@s146 x86_64]# nmap -V Nmap version 7.94 ( https://nmap.org ) Platform: x86_64-redhat-linux-gnu Compiled with: nmap-liblua-5.4.4 openssl-3.0.8 nmap-libssh2-1.10.0 nmap-libz-1.2.13 nmap-libpcre-7.6 nmap-libpcap-1.10.4 nmap-libdnet-1.12 ipv6 Compiled without: Available nsock engines: epoll poll select 


### 7、安装nmap-ncat

>  
 [root@s146 opt]# rpm -vhU https://nmap.org/dist/ncat-7.94-1.x86_64.rpm Retrieving https://nmap.org/dist/ncat-7.94-1.x86_64.rpm Preparing… ################################# [100%] file /usr/bin/ncat from install of ncat-2:7.94-1.x86_64 conflicts with file from package nmap-ncat-2:6.40-19.el7.x86_64 file /usr/share/man/man1/ncat.1.gz from install of ncat-2:7.94-1.x86_64 conflicts with file from package nmap-ncat-2:6.40-19.el7.x86_64 


### 8、安装nping

>  
 [root@s146 opt]# rpm -vhU https://nmap.org/dist/nping-0.7.94-1.x86_64.rpm Retrieving https://nmap.org/dist/nping-0.7.94-1.x86_64.rpm Preparing… ################################# [100%] Updating / installing… 1:nping-2:0.7.94-1 ################################# [100%] 


### 9、下载zenmap-7.94-1.noarch.rpm

>  
 [root@s146 opt]# wget --no-check-certificate https://nmap.org/dist/zenmap-7.94-1.noarch.rpm 


### 10、重新编译zenmap-7.94-1.noarch.rpm

>  
 [root@s146 opt]# rpmrebuild -enp zenmap-7.94-1.noarch.rpm 


### 11、安装zenmap-7.94-1.noarch.rpm

>  
 [root@s146 opt]# cd /root/rpmbuild/RPMS/noarch/ [root@s146 noarch]# rpm -Uvh zenmap-7.94-1.noarch.rpm Preparing… ################################# [100%] Updating / installing… 1:zenmap-2:7.94-1 ################################# [100%] 


### 12、安装PyGObject

>  
 [root@s146 bin]# pip3 install pycairo … Successfully installed pycairo-1.20.1 [root@s146 bin]# pip3 install PyGObject … Successfully installed PyGObject-3.42.2 


## 三、使用简介

### 1、启动程序

<img src="https://img-blog.csdnimg.cn/direct/17dec669f54b4df5847a2219ce1d8ccb.png" alt="在这里插入图片描述">

### 2、扫描一个主机

<img src="https://img-blog.csdnimg.cn/direct/b9d8fbff644a49999cd7fe6d01e927f2.png" alt="在这里插入图片描述">

### 3、扫描一个网段

<img src="https://img-blog.csdnimg.cn/direct/2543e88087cf41c09cbd19e81ec61bae.png" alt="在这里插入图片描述">

### 4、新建profile

  在上一篇博文中我们在windows环境下安装了zenmap，简单使用正常的，新建profile和对比扫描结果都是程序奔溃，博主继续这一批博文目的就是想看看这两个更实用的功能是什么样子的。新建或者编辑profile界面如下，一共包括配置、扫描、Ping、脚本、目标、源、其他、定时（汉化版本翻译为定时，暂时就用这个吧），各页签的主要配置项有多行，博主知识有限，还没有深入研究和测试，这里不过多赘述。总之linux环境下新建和编辑profile都可以正常使用。 <img src="https://img-blog.csdnimg.cn/direct/cf21dc30ffc84e33991a204bb5a34747.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/a171929102cb40aabefa95c0ac969e3a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/929c60b9f4d647b7a0050db7a1638fa4.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/36b68c7bf8ce487a8949b1ba883ccd34.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/090dc826db864507abd9f22bdbf29ded.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/9953a47b25b14fdfa9e9b10688bcdf63.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/97762d9bc5e14a768276e310b57a06d0.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/92dad3af2772455da998ade69f68c427.png" alt="在这里插入图片描述">

### 5、比较两次扫描结果

  这个是快速扫描和快速扫描plus这种模式下扫描结果差别对比。 <img src="https://img-blog.csdnimg.cn/direct/b2700c8c8bc94a7082faaeaa4d02a23f.png" alt="在这里插入图片描述">

## 四、QA

### 1、安装nmap-7.94时报错要求python3.0以上
- 报错信息： [root@s146 ~]# rpm -vhU https://nmap.org/dist/nmap-7.94-1.x86_64.rpm Retrieving https://nmap.org/dist/nmap-7.94-1.x86_64.rpm error: Failed dependencies: python &gt;= 3.0 is needed by nmap-2:7.94-1.x86_64- 报错原因：系统环境下的python版本不满足要求 [root@s146 ~]# python -V Python 2.7.5- 解决方案：安装python3以上，下载rpm包，重新编译rpm并安装。
### 2、安装zenmap-7.94是报错要求python3.0以上
- 报错信息：error: Failed dependencies: python &gt;= 3.0 is needed by zenmap-2:7.94-1.noarch- 报错原因：软件依赖python3.0以上- 解决方案：安装python3以上，下载rpm包，重新编译rpm并安装。
### 3、启动zenmap时报错找不到gi模块
- 报错信息：ModuleNotFoundError: No module named ‘gi’- 报错原因：未安装gi模块- 解决方案：安装PyGObject软件包，gi模块是PyGObject的一部分。
>  
 [root@s146 bin]# pip3 install pycairo [root@s146 bin]# pip3 install PyGObject 

