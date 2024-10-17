
--- 
title:  Linux 安装Python3 
tags: []
categories: [] 

---
### python3 下载地址





选择自己需要的版本、

此文中选择3.10.9

<img src="https://img-blog.csdnimg.cn/79231e155032452eaa1e33675d06853c.png" alt="在这里插入图片描述">

下载源码压缩包

<img src="https://img-blog.csdnimg.cn/1b1a70de9f474e3fa36feca7ef4cea59.png" alt="在这里插入图片描述">

可下载到本地后上传至Linux服务器也可以复制下载地址

```
wget https://www.python.org/ftp/python/3.10.9/Python-3.10.9.tgz

```

### python3 安装

yum 安装依赖包

```
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make  libffi-devel

```

解压python3源码压缩包

```
tar -xvf Python-3.10.9.tgz


```

开始安装 进入解压后的目录

```
cd Python-3.10.9/

./configure 
make
make install

```

### 建立软连接

此时python3已安装完成、 位置在/usr/local/bin

大多数Linux系统会预装python2版本、且不建议卸载python2 、卸载后有可能导致yum报错

此时进入/usr/bin/ 目录查看 python 命令、 发现指向 python2.7.5

重建软连接

备份原连接

```
mv /usr/bin/python /usr/bin/python.bak

```

建立新连接指向python3

```
ln -s /usr/local/bin/python3.10 /usr/bin/python

```

pip命令如不存在则直接新建

```
ln -s /usr/local/bin/pip3 /usr/bin/pip

```

### 配置pip源

家目录下创建配置文件 ~/.pip/pip.conf

```
mkdir ~/.pip

cd ~/.pip

vi pip.conf

```

编辑配置文件写入阿里云镜像

```
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com

```
