
--- 
title:  【虚拟机】VM + CentOS7 + Python3.8安装与配置 
tags: []
categories: [] 

---
## VM + CentOS环境安装


- 在“**软件选择**”选择是否安装图形用户界面
## Python3.8 下载与安装

安装依赖包

```
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel


```

创建目录

```
sudo mkdir /usr/local/python3 

```

下载安装包（根据需求选择版本）

```
wget --no-check-certificate https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz 

```

解压

```
tar xzvf Python-3.8.2.tgz

```

<img src="https://img-blog.csdnimg.cn/7ed91729d7c1439eaefe81a13ad592f2.png" alt="在这里插入图片描述">

进入目录，安装

```
cd Python-3.8.2
sudo ./configure --prefix=/usr/local/python3
sudo make
sudo make install

```

——

<img src="https://img-blog.csdnimg.cn/4eba24f6ccdb490f8b97d60e9c6d6279.png" alt="在这里插入图片描述">

——

<img src="https://img-blog.csdnimg.cn/6ab1f73082084bc29c710881919fa2be.png" alt="在这里插入图片描述">

——

### 修改系统默认Python编译器

删除默认python软连接

```
rm /usr/bin/python  

```

创建软连接

```
sudo ln -s /usr/local/python3/bin/python3 /usr/bin/python

```

<img src="https://img-blog.csdnimg.cn/7f0ed9bb8b82468eb9097302d76284ee.png" alt="在这里插入图片描述">

### 查看Python版本

```
python

```

<img src="https://img-blog.csdnimg.cn/43f13efca0fc431abec6d17dcb6d36b9.png" alt="在这里插入图片描述">

**exit()** 退出

### pip升级

```
python -m pip install --upgrade pip

```

<img src="https://img-blog.csdnimg.cn/4801aeef961c4f33951bc829356ab6c9.png" alt="在这里插入图片描述">

### 修改.bashrc文件添加PATH环境变量

参考：，原因与必要性暂且不清楚

打开文件

```
vim ~/.bashrc

```

进入文件后，按 **i** 键进入插入模式，在最后一行添加：

>  
 export PATH=/usr/local/python3/bin/:$PATH 


**esc**，输入 **:wq** ，**回车**，保存并退出 <img src="https://img-blog.csdnimg.cn/7871f97c048641509733d03bc65b30cc.png" alt="在这里插入图片描述">

配置生效

```
source ~/.bashrc

```

|
|------

## doccano安装（待补全）
- 
在文档中说明有3种使用方式：

<img src="https://img-blog.csdnimg.cn/1a5b0fb9a2524db6b43461f78c54967f.png" alt="在这里插入图片描述">

### pip方式

pip方式要求Python版本为3.8+，低版本安装不成功（**！！！以后相关情况一定要先看官方文档！！！**）

安装

```
pip install doccano

```

<img src="https://img-blog.csdnimg.cn/912d8f851c1b483f93c169d9d8428a7e.png" alt="在这里插入图片描述">

**大失败！！！**

### docker方式





## 问题记录

### 安装了两个版本的Python导致的一系列问题

centos7原本就安装了Python2，这个Python2是不能删除的，因为有很多系统命令，比如yum要用到。

这就存在 yum 依赖 python 2, 而个人使用 python 3 所导致的各种问题。

解决办法一般是修改提示的错误文件，将“python”改为“python2”
1. except yum.Errors.RepoError, e： <img src="https://img-blog.csdnimg.cn/ec03c6720e564f5e8a1d8461f025988b.png" alt="在这里插入图片描述"> 解决方法： 修改提示错误文件
```
vim /usr/bin/yum-config-manager

```

将提示文件第一行 “**#!/usr/bin/python**” 改为 “**#!/usr/bin/python2**”
1. except OSError, e: 相同解决方法