
--- 
title:  python版本升级从python3.8升级到python3.9 
tags: []
categories: [] 

---
查看操作系统版本：lsb_release -a  （本机是centos 7.6）

安装命令：

```
# 下载Python3.9.5
wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz
tar zxvf Python-3.9.5.tgz
# 安装必须的包
若未安装dnf，安装dnf命令如下：
前置依赖：
yum install epel-release 或者 yum install epel-release -y
安装dnf：
yum install dnf

dnf -y install gcc zlib* libffi-devel
cd Python-3.9.5/

#注意：prefix=/usr/local/python3是指定的python3.9安装目录，可设置成自己想要放的目录
./configure --prefix=/usr/local/python3 --enable-optimizations
make 
make install
# 删除原先的Python3和pip3  （让系统使用最新版本的python）
rm -rf /usr/bin/python3
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
rm -rf /usr/bin/pip3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

上述命令是新安装Python3.9.5版本，但原先电脑上安装的python版本依然存在，并未卸载。

可与下面的文章对照一起看：
