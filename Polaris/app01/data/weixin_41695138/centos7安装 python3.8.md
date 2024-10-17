
--- 
title:  centos7安装 python3.8 
tags: []
categories: [] 

---
参考 

### centos7安装 python3.8
1. python 的下载地址： 进入python官网:python.org <img src="https://img-blog.csdnimg.cn/002b8acead034f76b2c98c5850a37f92.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/72df089c8544477b8b7dc9732d3213a7.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/27c951d44b9448dcae27b73a49d6a4e8.png" alt="在这里插入图片描述">
### 安装python
1. 新建文件夹： /usr/local/python3.8 mkdir -p /usr/local/python3.8**加粗样式** <img src="https://img-blog.csdnimg.cn/10f5ecdfcc2e489a997e2268d5217830.png" alt="在这里插入图片描述">1. 上传下载好的文件至 /usr/local/python3.8 可通过ftp，也可通过 rz -e,请根据自己的情况进行处理 <img src="https://img-blog.csdnimg.cn/05eeb390e1b5439d9c25723a57b7ebd0.png" alt="在这里插入图片描述">1. 安装python需要的依赖 安装 ssl
```
 yum install openssl-devel 

```

安装依赖 yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make yum install libffi-devel -y

配置python3需要先安装gcc：yum install -y gcc <img src="https://img-blog.csdnimg.cn/36db1b8504ff474a837ea48e59ac31fc.png" alt="在这里插入图片描述"> 安装所需的包：yum -y install ncurses-devel libuuid-devel zlib zlib-devel sqlite-devel readline-devel tkinter tcl-devel tk-devel lzma gdbm-devel xz-devel libffi-devel <img src="https://img-blog.csdnimg.cn/9e62b73315d64becadb92918e8700ec6.png" alt="在这里插入图片描述"> 如果没有安装这些依赖，python在编译的时候，会出错！！！ 5. 解压python: tar -zxvf Python-3.8.12.tgz cd Python-3.8.12/ <img src="https://img-blog.csdnimg.cn/83c14d567b1d4099b70d083074a92295.png" alt="在这里插入图片描述"> 6. 进入解压后的目录进行编译和安装

```
./configure
make&amp;&amp;make install

```

<img src="https://img-blog.csdnimg.cn/8a839def5bfa471b8da95be9437ace69.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ba606a8ed92e46e7ac788a4ac9ad95cb.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1a8ac3b95dab4f099b2f7e573d8e1604.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/627bb5a9b9a1442ab48b3bd8153721c0.png" alt="出现这种婆娘个情况，则说明安装成功">

### 建立命令软链接

虽然python3.8.12安装成功了，但默认输入python还是显示是2.7版本的。如果要用python3.8.12需要输入python3即可，有时候不太方便。可以通过修改软链接的方式将默认的python指向python3.8.12。 先看一下默认的python及新安装的python3都安装在哪里

```
[root@localhost Python-3.8.12]# which python
/usr/bin/python
[root@localhost Python-3.8.12]# which python3
/usr/local/bin/python3
[root@localhost Python-3.8.12]# 

```

可以看到默认的python路径为/usr/bin/python，python3的路径为/usr/local/bin/python3 将python3的软链接加到python上

```
[root@localhost Python-3.8.12]# mv /usr/bin/python /usr/bin/python.bak 
[root@localhost Python-3.8.12]# ln -s /usr/local/bin/python3 /usr/bin/python
[root@localhost Python-3.8.12]# 

```

通过python -V命令查看python版号

```
[root@localhost Python-3.8.12]# python -V
Python 3.8.12

```

pip命令也可以修改，python3.8.12默认的pip是pip3，CentOS7的python2.7默认没有安装pip. 输入pip命令的时候提示命令没有找到

```
[root@localhost Python-3.8.12]# pip
-bash: pip: 未找到命令

```

这时也可以通过建立软链接的方式将pip命令链接到pip3上。首先看pip3命令在哪?

```
[root@localhost Python-3.8.12]# which pip3
/usr/local/bin/pip3

```

然后建立pip到pip3的软链接

```
[root@localhost Python-3.8.12]# ln -s /usr/local/bin/pip3 /usr/bin/pip
[root@localhost Python-3.8.12]# pip

```

```
[root@localhost Python-3.8.12]# pip -V
pip 21.1.1 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)

```

### 配置yum

安装python3改完软链接以后发现yum命令报错了，yum是依赖python2.7的，你把python改成了3.8了，所以报错了。

```
[root@localhost Python-3.8.12]# yum
  File "/usr/bin/yum", line 30
    except KeyboardInterrupt, e:
                            ^
SyntaxError: invalid syntax

```

可以修改yum里对python2的依赖即可。虽然安装了python3但是系统里python2依旧还在系统里，可以通过python2来指定用python2.7的命令，首先来看下python2的命令在哪里

```
[root@localhost Python-3.8.12]# which python2
/usr/bin/python2

```

可以cd到/usr/bin目录下 通过ls -alh|grep python查看python命令的详细情况。

```
[root@localhost bin]# pwd
/usr/bin

```

```
[root@localhost bin]# pwd
/usr/bin
[root@localhost bin]# ls -alh|grep python
lrwxrwxrwx.  1 root root      22 8月  19 13:20 python -&gt; /usr/local/bin/python3
lrwxrwxrwx.  1 root root       9 8月  19 13:11 python2 -&gt; python2.7
-rwxr-xr-x.  1 root root    7.0K 6月  28 23:30 python2.7
lrwxrwxrwx.  1 root root       7 8月  19 13:11 python.bak -&gt; python2
[root@localhost bin]# 

```

可以看到python软连接是执行的python3命令，python2是执行的python2.7的命令

```
vi /usr/libexec/urlgrabber-ext-down 


```

修改对python的依赖，修改成python2或python2.7都可以。 <img src="https://img-blog.csdnimg.cn/6ad59e9f501b4e419ef6f077645ced66.png" alt="在这里插入图片描述">

```
vi /usr/bin/yum


```

<img src="https://img-blog.csdnimg.cn/27a30c4b0c3f43ba8edf29bac4fcebf3.png" alt="在这里插入图片描述">

修改完这两个文件后，再敲yum命令就不会报错了。 <img src="https://img-blog.csdnimg.cn/feb0e42ac7f947b89d7b2f28a1c90fae.png" alt="在这里插入图片描述">
