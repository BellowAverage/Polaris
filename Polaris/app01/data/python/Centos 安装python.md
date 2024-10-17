
--- 
title:  Centos 安装python 
tags: []
categories: [] 

---
1.下载python包

```
wget  https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz
```

2.下载python3编译的依赖包

```
yum install -y gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

3.解压缩源码包

```
tar -zxvf /usr/local/software/tars/Python-3.9.10.tgz
```

4. 创建python的安装目录

```
mkdir -p  /usr/local/software/python
```

5.移动解压后的Python源码包到python目录

```
mv  /usr/local/software/tars/Python-3.9.10   /usr/local/software/python
```

6.进入解压后的目录并且执行

```
cd /usr/local/software/python/Python-3.9.10
./configure --prefix=/usr/local/software/python/  # 指定安装目为/usr/local/software/python/
```

7.编译

```
make
```

8.编译安装

```
make install
```

9.添加linux环境变量 使用root账号

```
vi /etc/profile

在末尾添加

#python

PATH=/usr/local/software/python/bin:$PATH

保存后  执行
source /etc/profile
```

10.修改python的链接指向

```
mv /usr/bin/python3 /usr/bin/python3.bak

ln -s /usr/local/software/python/bin/python3 /usr/bin/python3
```

  
