
--- 
title:  在Linux中搭建Python环境 
tags: []
categories: [] 

---
### **<strong><strong>Python**</strong>**<strong>-3.9.5**</strong>**<strong>安装**</strong></strong>

**<strong>第一步，检查Linux系统是否自带Python。**</strong>

命令：python --version

<img alt="" height="68" src="https://img-blog.csdnimg.cn/c920e31590a84a8487718dbcaa7d5ef8.png" width="297">  



**<strong>第二步，安装依赖包。**</strong>

命令：yum -y install bzip2-devel gcc make ncurses-devel openssl-devel readline-devel sqlite-devel tk-devel zlib-devel

**<strong>第三步，下载Python-3.9.5安装包。**</strong>

登录Python官网：，或登录Python下载网址：<u><u>https://www.python.org/downloads/release/python-3</u></u><u><u>9</u></u><u><u>5/</u></u>下载Python-3.9.5中的“Gzipped source tarball”和“XZ compressed source tarball”。也可以使用wget命令下载。

命令：cd /usr/local/src

wget 

**<strong>第四步，解压Python-3.9.5安装包。**</strong>

命令：cd /usr/local/src

tar -xvJf Python-3.9.5.tar.xz

**<strong>第五步，编译安装Python-3.9.5。**</strong>

命令：cd /usr/local/src/Python-3.9.5

./configure prefix=/usr/local/Python-3.9.5

make &amp;&amp; make install

若结果显示下图的内容，则说明Python-3.9.5编译安装成功。

<img alt="" height="320" src="https://img-blog.csdnimg.cn/44326a1de1134f009a9ea520a27dc935.png" width="554">  



**<strong>第六步，配置Python环境变量。**</strong>

在配置文件/etc/profile中添加下面的代码：

```
export PATH=$PATH:/usr/local/Python-3.9.5/bin
```

# 使profile配置立即生效

命令：source /etc/profile

# 查看Python版本

命令：python3.9 -V

若结果显示“Python 3.9.5”，则说明Python-3.9.5安装成功。

### **<strong><strong>pip安装**</strong></strong>

**<strong>第一步，检查Python3是否自带pip。**</strong>

命令：pip3 --version

若结果显示“pip 9.0.3”，则说明Python3自带pip。

<img alt="" height="66" src="https://img-blog.csdnimg.cn/e7c1a986935448839c4bffdbae0b8bd3.png" width="487">  



**<strong>第二步，更新pip。**</strong>

命令：sudo pip3 install --upgrade pip

若结果显示“Successfully installed pip-21.1.1”，则说明pip更新成功。

**<strong>第三步，查看更新的pip版本。**</strong>

命令：python3.9 -m pip -V



<img alt="" height="56" src="https://img-blog.csdnimg.cn/5be75bcce61444eaac64d9d207ba0300.png" width="554">  
