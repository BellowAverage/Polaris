
--- 
title:  Ubuntu16.04安装Python3.8，3.7，3.9(含卸载方法，支持多版本共存) 
tags: []
categories: [] 

---
## Ubuntu16.04安装Python3.8，3.7，3.9(含卸载方法，支持多版本共存)



#### 文章目录
- - - - <ul><li>- - - - - - - - - - - - 


## 前言

本文将按照Python的各个版本进行介绍的是`Ubuntu16.04`下安装相应版本`Python`的过程，可选择所需的版本进行查看，各个版本的命令基本相同，其中`Python3.8的是图解版，其余的是命令版`。本文仅在Ubuntu16.04下测试过，对于其他系统版本未测试，一般情况下具有通用性，这里看个人情况而定。 本文对于Python安装的定位是：`独立安装，不修改或覆盖系统原有python的文件，包括软链接，易卸载`。

## 一、前期准备（所有版本）

### 1. 安装所需依赖

```
sudo apt-get install libffi-dev uuid-dev lzma-dev liblzma-dev libncurses5-dev libgdbm-dev sqlite3 libsqlite3-dev openssl tcl8.6-dev tk8.6-dev libreadline-dev zlib1g-dev build-essential bzip2 libbz2-1.0 libbz2-dev libc6-dev libdb-dev libexpat1 libexpat1-dev libgdbm3 libncursesw5-dev libpcap-dev libreadline5 libreadline6 libreadline6-dev libsqlite0 libsqlite0-dev libsqlite3-0 libssl-dev libssl1.0.0 libxml2-dev libxslt1-dev sqlite tcl tk tk-dev xz-utils zlib1g zlib1g-dev make  

```

<img src="https://img-blog.csdnimg.cn/6dffe80afa574f17baead728d77b094f.png" alt="在这里插入图片描述">

### 2. 配置Python版本切换

Ubuntu系统自带有`python2.7` 和`python3.5`，这里先添加这两个的版本切换，即使用`python`和`python3`两个命令时使用哪个版本的python，由于Ubuntu系统对自带的两个python有一定程度的依赖，本文是不建议切换上述`python`和`python3`两个命令的Python版本的，否则会带来一些问题。

>  
 **例如：升级Python后无法打开终端，系统启动总是提示软件更新时发生错误，无法打开系统设置的软件和更新界面等** ****命令的版本对应****：`python` =&gt; `python2.7`， `python3` =&gt; `python3.5` 


**① 查看候选列表中已有的Python版本（没有配置过的话，是不存在的）：**

```
sudo update-alternatives --list python

```

<img src="https://img-blog.csdnimg.cn/0cd26298bd7c42678009397159be0b02.png" alt="在这里插入图片描述"> **② 添加 python &amp; python3 指向选择** 最后的序号表示优先级，数字越大，优先级越高，会自动选取优先级高的作为默认指向，可手动更改默认指向，这里将系统默认的指向的优先级设置为100

```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 100
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 99
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 100

```

<img src="https://img-blog.csdnimg.cn/30dc5910c1d9448d8b1acff3922360f4.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/66abe660b8c8495f9b8ad43f14627978.png" alt="在这里插入图片描述"> **③ 查看候选列表中已有的Python版本**

```
sudo update-alternatives --list python
sudo update-alternatives --list python3

```

<img src="https://img-blog.csdnimg.cn/3fbd2dd2ca4b48ea8e299a268ac61800.png" alt="在这里插入图片描述">

>  
 此时，`python`指向`python2.7`，`python3`指向`python3.5` <img src="https://img-blog.csdnimg.cn/dc42712af8dc4da18b905684539464db.png" alt="在这里插入图片描述"> 


**④ 创建新版python的安装目录（便于卸载）**

```
cd /usr/local
sudo mkdir -p /usr/local/python
sudo chmod -R 777 ./python

```

<img src="https://img-blog.csdnimg.cn/ae4ce878b65d48339afb4315943e1acc.png" alt="在这里插入图片描述">

下面将进行各个版本的安装，至于版本号的选择，可自行到下面的网址去找，后续操作中修改其中的版本号即可。 官方网址：`https://www.python.org/ftp/python/` <img src="https://img-blog.csdnimg.cn/80a5ec8640934211b8eba2df5036e6aa.png" alt="在这里插入图片描述">

## 二、Python3.8（3.8.11–详细图解）

### 1.下载源码安装包

这里选的是Python3.8的3.8.11版，如果下载较慢，可尝试连接手机热点进行下载。如果已准备了安装包，可以跳过该步骤。

```
cd ~
wget https://www.python.org/ftp/python/3.8.11/Python-3.8.11.tgz

```

<img src="https://img-blog.csdnimg.cn/925f28fbff88432bad604145b482e51c.png" alt="在这里插入图片描述">

### 2.创建安装目录

在上述前期准备中，已经在`/usr/local`目录下创建了一个`python`目录，那么各个新安装的python都将放在这里（安装多个的情况下），那么需要对每个版本的进行独立分包。实际上安装时如果没有创建会自动创建。

```
cd /usr/local/python
mkdir ./python3.8

```

<img src="https://img-blog.csdnimg.cn/7e8a81101e684ed799f30411a88401a1.png" alt="在这里插入图片描述">

### 3.解压安装包

```
cd ~
tar -xf ~/Python-3.8.11.tgz

```

<img src="https://img-blog.csdnimg.cn/5f7ac7a62e524edfbd476e66b44d71db.png" alt="在这里插入图片描述">

### 4.配置将要安装的目录

这里的configure的参数配置有些门道，如果你想设置更多的东西，可以自行去查找。博主不想，所以下面的就足够了

```
cd ~/Python-3.8.11
./configure prefix=/usr/local/python/python3.8 --enable-optimizations

```

<img src="https://img-blog.csdnimg.cn/ea1108d48e174db58f607b19ea4f0ce9.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e51be0d9e979476a8db162c8224265b0.png" alt="在这里插入图片描述">

### 5.编译源码

很多教程都是编译和安装一起的，个人觉得，编译过程是会有一些问题的，例如某个模块不能编译，但是即使这样，安装还是会进行，这样就不是很好。 编译时间会比较长，耐心等待。。。。

```
cd ~/Python-3.8.11
make -j 2

```

<img src="https://img-blog.csdnimg.cn/ba95fb41f805423890b2cca9ffd72d88.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9abc13854e534d9c904d43957690e3bc.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/21889471e703459f9cdeb291efe5f054.png" alt="在这里插入图片描述">

### 6.安装

一定要使用`altinstall`，看过的教程有说明过使用`install`会覆盖安装，可能会导致Ubuntu崩溃的情况。

```
cd ~/Python-3.8.11
make altinstall  &gt;&amp;1|tee make.log

```

这里执行会很快，输出较多，没截到命令的图，看个结果吧。 <img src="https://img-blog.csdnimg.cn/887b031c87994106b3f66d85e79420c7.png" alt="在这里插入图片描述">

### 7.添加环境变量

```
gedit ~/.bashrc

```

添加以下内容，其中第一行注释属于个人喜好，可不添加

```
#[Python3.8]
export PATH=$PATH:/usr/local/python/python3.8/bin

```

<img src="https://img-blog.csdnimg.cn/450da55c20b54efd968425c7c821184a.png" alt="在这里插入图片描述"> 让环境变量生效

```
source ~/.bashrc

```

<img src="https://img-blog.csdnimg.cn/f341dc7021a042cbb107cc857a70bed8.png" alt="在这里插入图片描述">

### 8. 添加和选择python&amp;python3命令指向

****添加命令指向****【数值比前面设置的默认指向的优先级100小即可】

```
sudo update-alternatives --install /usr/bin/python python /usr/local/python/python3.8/bin/python3.8 38 
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/python/python3.8/bin/python3.8 38

```

<img src="https://img-blog.csdnimg.cn/b2a1dace898547eaa76ed8950884aaab.png" alt="在这里插入图片描述">

**选择`python`命令的默认版本**【这里只是查看，按回车即可】

>  
 可以2.7，3.5，3.8，至于选取的问题，随着使用情景不同而有所改变，但使用完最好更换为Ubuntu系统默认的指向（`python2.7`），此时已经是默认的指向，会自动选取优先级高的。 


```
sudo update-alternatives --config python

```

<img src="https://img-blog.csdnimg.cn/a3ce5b219ef747988073ad1a7b48ef3f.png" alt="在这里插入图片描述">

**选择`python3`命令的默认版本**【这里只是查看，按回车即可】

>  
 python3一般选择与Ubuntu系统默认的指向3.5，否则无法在启动器栏打开新终端。 


```
sudo update-alternatives --config python3

```

<img src="https://img-blog.csdnimg.cn/5b64dd091646436689557585d35ad4f4.png" alt="在这里插入图片描述">

>  
 这样之后，下面是各命令的启动版本 `python2` ==&gt; `python2.7` `python` ==&gt; `python2.7` `python3` ==&gt; `python3.5` `python3.5` ==&gt; `python3.5` `python3.8` ==&gt; `python3.8` 


<img src="https://img-blog.csdnimg.cn/0354dde92f4546dd8c291bb38579fea0.png" alt="在这里插入图片描述">

>  
 `pip` 指向自动跟随 `python` 的指向 `pip3` 指向自动跟随 `python3` 的指向 


### 9.pip安装依赖包

对于python3.8，安装后使用pip请以`python3.8 -m pip install xxx`的形式使用，同时，对于python3.8的使用，建议明确指明版本来使用，而不建议更改python3的指向，因为Ubuntu的图形界面一定程度上是依赖自带的两个版本的python，更改指向可能会带来意想不到的问题。

```
可更新python3.8自带的pip的版本，也可不更新，一般原版的更配，只是新版的进度条更好看，也没有版本更新警告。
python3.8 -m pip install --upgrade pip  
如果想切换回原版的
python3.8 -m pip install --upgrade pip==21.1.1

```

```
python3.8 -m pip install flask-socketio
python3.8 -m pip install numpy -i https://pypi.douban.com/simple/
python3.8 -m pip install pandas -i https://pypi.douban.com/simple/
python3.8 -m pip install kafka
python3.8 -m pip install kafka-python

```

<img src="https://img-blog.csdnimg.cn/48771f1d27134561a3b23fe211a870a9.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/bda33685883a4364b26169e0c4dfd227.png" alt="在这里插入图片描述">

### 10.删除安装文件

```
cd ~
sudo rm -r ./Python-3.8.11
rm -r ./Python-3.8.11.tgz

```

```
安装完成后建议重启一次系统

```

### 11.卸载方法（安装时`无需`操作）

这里给出卸载的命令，如果不需要了，可以进行卸载。

```
#1.移除指向
sudo update-alternatives --remove python /usr/local/python/python3.8/bin/python3.8
sudo update-alternatives --remove python3 /usr/local/python/python3.8/bin/python3.8
#2.删除安装目录，对于Linux而言便是卸载
rm -r /usr/local/python/python3.8
#3.移除环境变量
gedit ~/.bashrc
把上面添加的环境变量内容删除即可
source ~/.bashrc

```

## 三、Python3.7（3.7.9–已测试）

**1.下载源码安装包** 这里选的是Python3.7的3.7.9版，如果下载较慢，可尝试连接手机热点进行下载。如果已准备了安装包，可以跳过该步骤。

```
cd ~
wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz

```

**2.创建安装目录** 在上述前期准备中，已经在`/usr/local`目录下创建了一个`python`目录，实际上安装时如果没有创建会自动创建。

```
cd /usr/local/python
mkdir ./python3.7

```

**3.解压安装包**

```
cd ~
tar -xf ~/Python-3.7.9.tgz

```

**4.配置将要安装的目录**

```
cd ~/Python-3.7.9
./configure prefix=/usr/local/python/python3.7 --enable-optimizations

```

**5.编译源码** 3.7的编译时间相比其他版本会更长，耐心等待。。。。

```
cd ~/Python-3.7.9
make -j 2

```

**6.安装** 一定要使用`altinstall`，看过的教程有说明过使用`install`会覆盖安装，可能会导致Ubuntu崩溃的情况。

```
cd ~/Python-3.7.9
make altinstall  &gt;&amp;1|tee make.log

```

**7.添加环境变量**

```
gedit ~/.bashrc

```

添加以下内容，其中第一行注释属于个人喜好，可不添加

```
#[Python3.7]
export PATH=$PATH:/usr/local/python/python3.7/bin

```

让环境变量生效

```
source ~/.bashrc

```

**8. 添加和选择python&amp;python3命令指向** ****添加命令指向****【数值比前面设置的默认指向的优先级100小即可】

```
sudo update-alternatives --install /usr/bin/python python /usr/local/python/python3.7/bin/python3.7 37 
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/python/python3.7/bin/python3.7 37

```

**选择`python`命令的默认版本**【这里只是查看，按回车即可】 `*`号指向应当是Ubuntu系统默认的指向（`python2.7`）

```
sudo update-alternatives --config python

```

**选择`python3`命令的默认版本**【这里只是查看，按回车即可】 `*`号指向应当是Ubuntu系统默认的指向（`python3.5`）

```
sudo update-alternatives --config python3

```

>  
 python3.7的启动命令 `python3.7` ==&gt; `python3.7` 


**9.pip安装依赖包** 对于python3.7，安装后使用pip请以`python3.7 -m pip install xxx`的形式使用，同时，对于python3.7的使用，建议明确指明版本来使用，而不建议更改python3的指向，因为Ubuntu的图形界面一定程度上是依赖自带的两个版本的python，更改指向可能会带来意想不到的问题。

```
可更新python3.7自带的pip的版本，也可不更新，一般原版的更配，只是新版的进度条更好看，也没有版本更新警告。
python3.7 -m pip install --upgrade pip  
如果想切换回原版的
python3.7 -m pip install --upgrade pip==20.1.1

```

```
python3.7 -m pip install flask-socketio
python3.7 -m pip install numpy -i https://pypi.douban.com/simple/
python3.7 -m pip install pandas -i https://pypi.douban.com/simple/
python3.7 -m pip install kafka
python3.7 -m pip install kafka-python

```

**10.删除安装文件**

```
cd ~
sudo rm -r ./Python-3.7.9
rm -r ./Python-3.7.9.tgz

```

```
最好进行一次系统重启

```

**11.卸载方法（安装时无需操作）** 这里给出卸载的命令，如果不需要了，可以进行卸载。

```
#1.移除指向
sudo update-alternatives --remove python /usr/local/python/python3.7/bin/python3.7
sudo update-alternatives --remove python3 /usr/local/python/python3.7/bin/python3.7
#2.删除安装目录，对于Linux而言便是卸载
rm -r /usr/local/python/python3.7
#3.移除环境变量
gedit ~/.bashrc
把上面添加的环境变量内容删除即可
source ~/.bashrc

```

## 四、Python3.9（3.9.13–已测试）

**1.下载源码安装包** 这里选的是Python3.9的3.9.13版，如果下载较慢，可尝试连接手机热点进行下载。如果已准备了安装包，可以跳过该步骤。

```
cd ~
wget https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz

```

**2.创建安装目录** 在上述前期准备中，已经在`/usr/local`目录下创建了一个`python`目录，实际上安装时如果没有创建会自动创建。

```
cd /usr/local/python
mkdir ./python3.9

```

**3.解压安装包**

```
cd ~
tar -xf ~/Python-3.9.13.tgz

```

**4.配置将要安装的目录**

```
cd ~/Python-3.9.13
./configure prefix=/usr/local/python/python3.9 --enable-optimizations

```

**5.编译源码**

```
cd ~/Python-3.9.13
make -j 2

```

**6.安装**

```
cd ~/Python-3.9.13
make altinstall  &gt;&amp;1|tee make.log

```

**7.添加环境变量**

```
gedit ~/.bashrc

```

添加以下内容，其中第一行注释属于个人喜好，可不添加

```
#[Python3.9]
export PATH=$PATH:/usr/local/python/python3.9/bin

```

让环境变量生效

```
source ~/.bashrc

```

**8. 添加和选择python&amp;python3命令指向** ****添加命令指向****【数值比前面设置的默认指向的优先级100小即可】

```
sudo update-alternatives --install /usr/bin/python python /usr/local/python/python3.9/bin/python3.9 39 
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/python/python3.9/bin/python3.9 39

```

**选择`python`命令的默认版本**【这里只是查看，按回车即可】 `*`号指向应当是Ubuntu系统默认的指向（`python2.7`）

```
sudo update-alternatives --config python

```

**选择`python3`命令的默认版本**【这里只是查看，按回车即可】 `*`号指向应当是Ubuntu系统默认的指向（`python3.5`）

```
sudo update-alternatives --config python3

```

>  
 python3.9的启动命令 `python3.9` 


**9.pip安装依赖包** 对于python3.9，安装后使用pip请以`python3.9 -m pip install xxx`的形式使用，同时，对于python3.9的使用，建议明确指明版本来使用，而不建议更改python3的指向，因为Ubuntu的图形界面一定程度上是依赖自带的两个版本的python，更改指向可能会带来意想不到的问题。

```
可更新python3.9自带的pip的版本，也可不更新，一般原版的更配，只是新版的进度条更好看，也没有版本更新警告。
python3.9 -m pip install --upgrade pip  
如果想切换回原版的
python3.9 -m pip install --upgrade pip==22.0.4

```

```
python3.9 -m pip install flask-socketio
python3.9 -m pip install numpy -i https://pypi.douban.com/simple/
python3.9 -m pip install pandas -i https://pypi.douban.com/simple/
python3.9 -m pip install kafka
python3.9 -m pip install kafka-python

```

**10.删除安装文件**

```
cd ~
sudo rm -r ./Python-3.9.13
rm -r ./Python-3.9.13.tgz

```

```
最好进行一次系统重启

```

**11.卸载方法（安装时无需操作）** 这里给出卸载的命令，如果不需要了，可以进行卸载。

```
#1.移除指向
sudo update-alternatives --remove python /usr/local/python/python3.9/bin/python3.9
sudo update-alternatives --remove python3 /usr/local/python/python3.9/bin/python3.9
#2.删除安装目录，对于Linux而言便是卸载
rm -r /usr/local/python/python3.9
#3.移除环境变量
gedit ~/.bashrc
把上面添加的环境变量内容删除即可
source ~/.bashrc

```

```
对于Python的其他版本，安装方法都基本类似，只需要更改对应的版本号即可。

```
