
--- 
title:  Linux系统安装Python3环境（超详细）_linux 安装python3 
tags: []
categories: [] 

---


#### 文章目录
- - <ul><li><ul><li>- - - <ul><li><ul><li>- - - - <ul><li>- - - - - - - 


## 前言

本文基于如下Linux系统版本：

<img src="https://img-blog.csdnimg.cn/20181205135253731.png#pic_center" alt="">

#### 1、默认情况下，Linux会自带安装Python，可以运行python --version命令查看

如图： <img src="https://img-blog.csdnimg.cn/20181205114121673.png#pic_center" alt="">

我们看到Linux中已经自带了Python2.7.5。再次运行python命令后就可以使用python命令窗口了（Ctrl+D退出python命令窗口）。

#### 2、查看Linux默认安装的Python位置

<img src="https://img-blog.csdnimg.cn/20181205114638860.png#pic_center" alt="">

看到/usr/bin/python和/usr/bin/python2都是软链接，/usr/bin/python指向/usr/bin/python2，而/usr/bin/python2最终又指向/usr/bin/python2.7。所以运行python/python2/python2.7是一样的，如图： <img src="https://img-blog.csdnimg.cn/49796a08168348bbace58b55ac5bb19d.png#pic_center" alt="在这里插入图片描述">

#### 3、安装python3

###### （1）下载

linux下执行

```
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz


```

或者，登录Python Source Releases | Python.org，找到对应版本（我们以Python 3.6.5为例）如图：

<img src="https://img-blog.csdnimg.cn/20181205140734407.png#pic_center" alt="">

###### （2）文件上传

将文件上传到Linux系统的某个目录下，根据自己情况上传，本例上传到了/root/tools目录下，如图：

<img src="https://img-blog.csdnimg.cn/20181205141052576.png#pic_center" alt="">

###### （3）解压

执行tar -zxvf Python-3.6.5.tgz命令，将文件解压到当前目录，如图：<img src="https://img-blog.csdnimg.cn/20181205131636273.png#pic_center" alt="">

###### （4）准备编译环境

执行如下命令：

```
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel


```

解释说明一下（标记核心的包务必安装。例如不安装libffi-devel，则会导致pandas导入时报错）：

>  
 yum -y install zlib-devel bzip2-devel openssl-devel**(核心)** ncurses-devel sqlite-devel readline-devel tk-devel gcc make gdbm-devel db4-devel libpcap-devel xz-devel**(核心)** libffi-devel**(核心)** 


安装python需要的依赖。成功后（Complete!），如图： <img src="https://img-blog.csdnimg.cn/4bdc0f9162524c9eb8982355ffc40dc8.png#pic_center" alt="在这里插入图片描述">

如果python是3.7版本，还需要安装libffi-devel。整个编译过程1分钟左右。

如果遇到如下问题：

>  
 Loaded plugins: fastestmirror 00:00:00 Could not retrieve mirrorlist http://mirrorlist.centos.org/?release=7&amp;arch=x86_64&amp;repo=os&amp;infra=stock error was 14: curl#6 - “Could not resolve host: mirrorlist.centos.org; Unknown error” 
 One of the configured repositories failed (Unknown), and yum doesn’t have enough cached data to continue. At this point the only safe thing yum can do is fail. There are a few ways to work “fix” this: 
 <pre><code> 1. Contact the upstream for the repository and get them to fix the problem.

 2. Reconfigure the baseurl/etc. for the repository, to point to a working  
    upstream. This is most often useful if you are using a newer  
    distribution release than is supported by the repository (and the  
    packages for the previous distribution release still work).

</code></pre> 


一般是不能连接外网，每个情况不一样，我的解决方案，执行如下命令

```
vi  /etc/sysconfig/network-scripts/ifcfg-ens33


```

每个人的Linux中ifcfg-ens33名称不一定完全一样。我的配置如下：

>  
 TYPE=Ethernet 
 PROXY_METHOD=none 
 BROWSER_ONLY=no 
 #BOOTPROTO=none 
 DEFROUTE=yes 
 IPV4_FAILURE_FATAL=no 
 IPV6INIT=yes 
 IPV6_AUTOCONF=yes 
 IPV6_DEFROUTE=yes 
 IPV6_FAILURE_FATAL=no 
 IPV6_ADDR_GEN_MODE=stable-privacy 
 NAME=ens33 
 UUID=296fb7a9-961a-46ea-bc1b-678cca49d40a 
 DEVICE=ens33 
 ONBOOT=yes 
 IPADDR=192.168.189.111 
 GATEWAY=192.168.189.2 
 NETMASK=255.255.255.0 
 DNS1=8.8.8.8 
 PREFIX=24 
 IPV6_PRIVACY=no 


配置好保存，执行service network restart重启网络服务。然后再重新执行上面的yum安装命令即可。

（5）编译安装

执行cd Python-3.6.5进入解压后的Python-3.6.5目录下，依次执行如下三个命令（其中–prefix是Python的安装目录）：

```
./configure --prefix=/root/training/Python-3.6.5
make
make install


```

执行第一步时提示（./configure --enable-optimizations），不要执行，忽略即可（若不小心执行了，则删除解压文件Python-3.6.5.tgz重新解压即可）。执行下图命令会在**make &amp;&amp; make install** 时导致 **Could not import runpy module** 错误（参考：

<img src="https://img-blog.csdnimg.cn/af0d5f43b9754dee9ec431a665c5965c.png#pic_center" alt="在这里插入图片描述">

安装成功后，如图： <img src="https://img-blog.csdnimg.cn/5b79a8c697484e478decbb09c0afb85e.png#pic_center" alt="在这里插入图片描述">

我们看到，同时安装了setuptools和pip工具。进入到/root/training/Python-3.6.5安装目录，如图： <img src="https://img-blog.csdnimg.cn/20181205132418781.png#pic_center" alt="">

（6）创建软链接

还记得开始，Linux已经安装了python2.7.5，这里我们不能将它删除，如果删除，系统可能会出现问题。我们只需要按照与Python2.7.5相同的方式为Python3.6.5创建一个软链接即可，我们把软链接放到/usr/local/bin目录下，如图：<img src="https://img-blog.csdnimg.cn/20181205134913739.png#pic_center" alt="">

pip3也同理需要软连接：

<img src="https://img-blog.csdnimg.cn/dfdc5333cfef489aa0fd2ae4a55c5290.png#pic_center" alt="在这里插入图片描述">

此时，我们在命令窗口运行python3，如图：<img src="https://img-blog.csdnimg.cn/20181205134959464.png#pic_center" alt="">

安装成功！当然此时还是可以使用Python2.7.5版本（运行python/python2/python2.7即可）。

（7）配置环境变量

配置环境变量主要是能快速使用pip3安装命令。

执行 vi ~/.bash_profile，打开配置文件，添加如下配置：

```
#配置python
export PYTHON_HOME=/root/training/Python-3.6.5
export PATH=$PYTHON_HOME/bin:$PATH


```

保存退出（:wq），执行source ~/.bash_profile命令使配置生效。执行echo命令，查看是否配置成功，如图：<img src="https://img-blog.csdnimg.cn/20181205143055635.png#pic_center" alt="">

#### 总结报错解决

###### 问题一：

安装时报错ModuleNotFoundError: No module named '_ctypes’的解决办法

1、执行如下命令：

```
yum install libffi-devel 



```

2、从"./configure …"重新安装

###### 问题二：

pip3 install时报错“pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.”

先安装openssl-dev，然后重新编译安装，只是在编译的过程中加入 --enable-optimizations

**ubuntu：**

```
sudo apt-get install libffi-dev


```

**centos7**

```
yum install libffi-devel -y


```

**-END-**

<mark>**读者福利：如果大家对Python感兴趣，这套python学习资料一定对你有用**</mark>

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以根据这些资料规划好学习计划和方向。 


<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习、Python量化交易等习教程。带你从零基础系统性的学好Python！</mark>

## 零基础Python学习资源介绍

① Python所有方向的<mark>学习路线图</mark>，清楚各个方向要学什么东西

② 600多节<mark>Python课程视频</mark>，涵盖必备基础、爬虫和数据分析

③ 100多个<mark>Python实战案例</mark>，含50个超大型项目详解，学习不再是只会理论

④ 20款主流手游迫解 <mark>爬虫手游逆行迫解教程包</mark>

⑤ <mark>爬虫与反爬虫攻防</mark>教程包，含15个大型网站迫解

⑥ <mark>爬虫APP逆向实战</mark>教程包，含45项绝密技术详解

⑦ 超<mark>300本Python电子好书</mark>，从入门到高阶应有尽有

⑧ 华为出品独家<mark>Python漫画教程</mark>，手机也能学习

⑨ 历年互联网企业<mark>Python面试真题</mark>,复习时非常方便

<img src="https://img-blog.csdnimg.cn/7c1055f9bb6e41af9262556bdf20e084.png#pic_center" alt="在这里插入图片描述">

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取哈）**</mark> <img src="https://img-blog.csdnimg.cn/9f969354b48f4e3ab0253e89203deca2.png#pic_center" alt="在这里插入图片描述">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/6cf364e7eeb64b0da07021bce5a59ec6.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

## 资料领取

<mark>上述这份完整版的Python全套学习资料已经上传网盘，朋友们如果需要可以微信扫描下方二维码输入“领取资料” 即可自动领取</mark> <font color="red" size="3"> **或者**</font> 【】领取
