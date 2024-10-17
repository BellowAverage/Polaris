
--- 
title:  linux centos上安装python3.11.x详细完整教程 
tags: []
categories: [] 

---
#### 一. 安装步骤

注意： 1、安装python3.11的其他版本替换下面的版本信息即可。(如想安装3.11.5将案例中的3.11.0替换成3.11.5即可)

```
#下载最新的软件安装包
wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz

#解压缩安装包
tar -xzf Python-3.11.0.tgz

#安装源码编译需要的编译环境
yum -y install gcc zlib zlib-devel libffi libffi-devel

#可以解决后期出现的方向键、删除键乱码问题，这里提前避免。
yum install readline-devel

#安装openssl11，后期的pip3安装网络相关模块需要用到ssl模块。
yum install openssl-devel openssl11 openssl11-devel

#设置编译FLAG，以便使用最新的openssl库
export CFLAGS=$(pkg-config --cflags openssl11)
export LDFLAGS=$(pkg-config --libs openssl11)

#进入刚解压缩的目录
cd /root/Python-3.11.0

#指定python3的安装目录为 /usr/python 并使用ssl模块，指定目录好处是后期删除此文件夹就可以完全删除软件了。
./configure --prefix=/usr/python --with-ssl

#就是源码编译并安装了，时间会持续几分钟。
make
make install

#指定链接，此后我们系统的任何地方输入python3就是我们安装的
ln -s /usr/python/bin/python3 /usr/bin/python3
ln -s /usr/python/bin/pip3 /usr/bin/pip3

#这个最新版python3了，可看到版本信息
python3 --version 
pip3 -V

```

若要卸载，直接 `rm -rf /usr/python`即可

#### 二. 报错处理

###### 1. make编译的时候出现报错

<img src="https://img-blog.csdnimg.cn/de1e97d86bde48a3bf7cfd452c8aeb6c.png" alt="在这里插入图片描述"> 即

```
‘Could not build the ssl module!

Python requires a Openssl 1.1.1 or newer’'

```

如果不处理此报错，会出现：`ModuleNotFoundError: No module named '_ssl'` 的问题。是因为较新版本的python3开始使用openssl11进行支持了。

解决方案请参考：

###### 2、报错出现‘No package openssl11 available’：

解决方法：多数是你没有安装EPEL（即企业版linux扩展包），使用以下方法即可:`yum install epel-release`
