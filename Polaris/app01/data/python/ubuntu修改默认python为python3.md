
--- 
title:  ubuntu修改默认python为python3 
tags: []
categories: [] 

---
### 1 ubuntu默认python

ubuntu 大多镜像版本都会携带python解释器：
- ubuntu16.04 python指令进入python2.7，默认python3.5 如果没有python我们需要自己安装，ubuntu16.04安装python需要下载源码编译安装：  选择心仪的python版本：
```
tar -zxvf Python-3.6.9.tgz
cd Python-3.6.9
./configure
make &amp;&amp; make install

```
- ubuntu18.04 python指令进入python2.7，默认python3.6.9 18.04系统安装python相对简单了
```
sudo apt-get update
sudo apt-get install python2.7 -y 	# 安装python2.7
sudo apt-get install python-pip -y 	# 安装python下载库pip工具
sudo apt-get install python3.6 -y  	# 安装python3.6
sudo apt-get install python3-pip -y # 安装python3下载库pip3工具

```

### 2 修改默认python脚本

（1）查看python可执行文件位置

```
➜  bin whereis python   
python: /usr/bin/python3.5m /usr/bin/python3.5 /usr/lib/python2.7 /usr/lib/python3.5 /etc/python3.5 /usr/local/bin/python3.6 /usr/local/bin/python3.6m-config /usr/local/bin/python3.6m /usr/local/bin/python3.6-config /usr/local/lib/python3.6 /usr/local/lib/python3.5

```

（2）我的python3.6可执行文件在/usr/local/bin/python3.6，我们只需要将/usr/bin/python删掉，创建指向python3.6的软连接即可：

```
➜  /usr sudo rm /usr/bin/python
➜  /usr sudo ln -s /usr/local/bin/python3.6 /usr/bin/python


```

（3）终端执行python指令

```
➜  /usr python
Python 3.6.9 (default, Oct 14 2022, 11:19:55) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; 

```

没有问题，大功告成
