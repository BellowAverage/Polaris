
--- 
title:  Ubuntu安装python3.10.6 
tags: []
categories: [] 

---
### Ubuntu 16.04安装python 3.10.6（通过源码安装）详细教程

最近学习python，想在Ubuntu下使用pycharm，发现pycharm不支持python3.5的解释器，就必须安装较高版本的python解释器，网上有很多版本，综合多个文档，完成安装，记录下来~ Ubuntu16.04默认安装了python2.7和python3.5，可通过终端输入python和python3查看（并通过exit（）返回终端）。 <img src="https://img-blog.csdnimg.cn/f13db5914716499b82585e00e4a9e51a.png#pic_center" alt="在这里插入图片描述">

**1.安装前期准备** 需安装libffi-devel库。

```
   sudo apt-get install libffi-dev

```

如出现无法找到安装包，可按顺序安装依赖包 <img src="https://img-blog.csdnimg.cn/4f7604fe681041cabfe88678534ea657.png" alt="在这里插入图片描述">

```
 sudo apt-get update
 sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus
 sudo apt-get install build-essential libncursesw5-dev libgdbm-dev libc6-dev
 sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
 sudo apt-get install libssl-dev openssl
 sudo apt-get install libffi-dev
 sudo apt-get install libxpm-dev libxext-dev 
 sudo apt-get install zlib1g-dev libbz2-dev libssl-dev libncurses5-dev libsqlite3-dev 

```

另外，安装以下依赖库

```
 sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

```

**2.安装python3.10.6** 进入python官网下载（https://www.python.org/downloads/），找到Linux版本，并找到对应版本，在对应版本上右击，复制下载链接。 <img src="https://img-blog.csdnimg.cn/10da7586d4664cfe97a3afa1b2b7cee7.png#pic_center" alt="在这里插入图片描述">

```
wget  https://www.python.org/ftp/python/3.10.6/Python-3.10.6.tgz

```

下载完成后，解压文件

```
tar -vxf Python-3.10.6.tgz

```

进入到解压后的文件夹中

```
cd Python-3.10.6

```

使用configure对文件进行配置，并利用–prefix=指定安装路径为/usr/local/python3.10.6

```
./configure --prefix=/usr/local/python3.10.6

```

```
./configure --enable-optimizations

```

编译

```
sudo make

```

安装

```
make install

```

出现问题就使用

```
sudo make altinstall

```

以上不出现问题的话，就完成了python解释器的安装~

为了在终端输入python时，使用安装的高版本python解释，需要将默认的解释器删除，并通过软链接新版的python解释器~ 默认安装的python解释器在/usr/bin/python 或 /usr/bin/python3 删除

```
sudo rm /usr/bin/python

```

软连接

```
sudo ln -s /usr/local/python3.10.6/bin/python3.10 /usr/bin/python

```

<img src="https://img-blog.csdnimg.cn/8208166eab6f4811ac80acc4d48f0b6f.png" alt="在这里插入图片描述"> 现在就可以方便地使用python解释器了~

如果还有不懂的，可以参考   
