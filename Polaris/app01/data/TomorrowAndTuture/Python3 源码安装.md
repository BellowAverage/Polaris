
--- 
title:  Python3 源码安装 
tags: []
categories: [] 

---
现在大部分都可以直接用 yum install python3 去直接安装 pyhon3 了，不过偶尔肯定也会有需求去安装不同版本的 python3，这时候源码包安装就会用上排场了；其实对任何软件，源码安装的方式都大同小异，无非就是解压、编译和安装。

### 1. 下载源码包

正常来说，首选当然是去官网下载（虽然有时候速度有些慢）：。比如说可以下载 Python3.7 的压缩源码包：

```
root@master ~# wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
root@master ~# ll Python-3.7.0.tar.xz 
-rw-r--r--. 1 root root 17M Aug 10 10:45 Python-3.7.0.tar.xz

```

### 2. 安装依赖库

```
yum install zlib-devel bzip2-devel openssl-devel gcc mysql-devel openldap sqlite-devel libffi-devel python3-devel
```

比较重要的依赖（**一定要 yum 安装一下，能让你后边少踩很多坑**）：**python3-devel、libffi-devel**

### 3. 解压源码包

```
root@master ~# tar -xf Python-3.7.0.tar.xz 
root@master ~# ll -d Python-3.7.0
drwxr-xr-x. 19 501 501 4.0K Aug 10 10:52 Python-3.7.0/

```

有的 xz 文件不能直接用 tar 解压，可以先用 xz 命令，再用 tar 解压。 

```
root@master ~/test# xz -d Python-3.7.0.tar.xz 
root@master ~/test# ll
total 78M
-rw-r--r--. 1 root root 78M Aug 28 11:23 Python-3.7.0.tar
root@master ~/test# tar -xf Python-3.7.0.tar 
root@master ~/test# ll
total 78M
drwxr-xr-x. 18  501  501 4.0K Jun 27  2018 Python-3.7.0/
-rw-r--r--.  1 root root  78M Aug 28 11:23 Python-3.7.0.tar

```

### 4. 编译安装

```
root@master ~# ./configure --prefix=/usr/local/python3.7
root@master ~# make
root@master ~# make install
```

### 5. 设置软连接

```
root@master ~# ln -fs /usr/local/python3.7/bin/python3 /usr/bin/python3
root@master ~# ln -fs /usr/local/python3.7/bin/pip3 /usr/bin/pip3
```


