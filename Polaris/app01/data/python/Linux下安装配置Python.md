
--- 
title:  Linux下安装配置Python 
tags: []
categories: [] 

---
一、下载与安装配置 官网地址：https://www.python.org/ <img src="https://img-blog.csdnimg.cn/47bc5843d1ee41b781952cd614cb6cc3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7d8a110268ea4d7f9c5ebc8b0f79e2da.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f6f59f4b4b7842779c76775b2de1d2b8.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/02c260bf52a04ddd88b8df33ea289cbc.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5cd022afcff846ac9e9a44abe9c151d4.png" alt="在这里插入图片描述"> 下载python包

wget https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz

下载python3编译的依赖包

yum install -y gcc patch libffi-devel python-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel 注意：上面的依赖安装需要使用root账号完成

二、解压安装

1.查看当前系统的python版本号（大部分linux系统下自带了python2，最好不要同一个系统下两个都存在，除非你清楚的知道该怎么区分它们）

python -V （这里的python目前指向的是python 2的链接）

主要是大写的V

我们需要安装的是Python3,（注意不要删除旧的，删除后yum就无法使用了）

2.查看python相关的文件

rpm -qa | grep python*

3.解压缩源码包

tar -zxvf /usr/local/software/tars/Python-3.9.10.tgz
1. 创建python的安装目录
mkdir /usr/local/software/python

5.移动解压后的Python源码包到python目录

mv /usr/local/software/tars/Python-3.9.10 /usr/local/software/python

6.进入解压后的目录并且执行

cd /usr/local/software/python/Python-3.9.10 ./configure --prefix=/usr/local/software/python/ # 指定安装目录为/usr/local/software/python/

7.编译

make

8.编译安装

make install

9.添加linux环境变量 使用root账号

vi /etc/profile

在末尾添加

#python

PATH=/usr/local/software/python/bin:$PATH

保存后 执行source /etc/profile

10.修改python的链接指向

[root@localhost ~]# mv /usr/bin/python /usr/bin/python.bak

[root@localhost ~]# ln -s /usr/local/software/python/bin/python3 /usr/bin/python

因为yum和firewall都依赖python，所以更改会导致它们不可用，需要修改配置

1.编辑yum

[root@localhost ~]# vi /usr/bin/yum

将第一行”#!/usr/bin/python” 改为 “#!/usr/bin/python2.7”即可

下面也同样：修改的”#!/usr/bin/python” 改为 “#!/usr/bin/python2.7”

[root@localhost ~]# vi /usr/libexec/urlgrabber-ext-down

2.编辑firewall，修改/usr/bin/firewall-cmd和/usr/sbin/firewalld文件，在这两个文件的首行的“python”都改为“python2.7”

[root@localhost ~]# vi /usr/bin/firewall-cmd

[root@localhost ~]# vi /usr/sbin/firewalld

验证是否修改成功 执行

[root@localhost ~]# python -V

Python 3.9.10

显示如上信息说明修改成功了！
