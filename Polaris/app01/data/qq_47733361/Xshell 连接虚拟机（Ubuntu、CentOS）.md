
--- 
title:  Xshell 连接虚拟机（Ubuntu、CentOS） 
tags: []
categories: [] 

---
对于一些linux的初学者来说，在没有自己的服务器时可以选择使用虚拟机来代替（如ubuntu、centos等）进行相关的学习。下面介绍下如何使用xshell来远程连接虚拟机。 注意：下面我以Ubuntu来举例说明。

### 1、创建虚拟机

虚拟机的创建网络上教程非常多，这里就不在赘述了。创建虚拟机并打开。

### 2、查找虚拟IP

右键**打开终端**，输入如下命令：

```
ifconfig

```

在ens33 下面找到如下即为此虚拟机的ip地址，先保存下来。 <img src="https://img-blog.csdnimg.cn/94353151d4784aab809d065674fb96c5.png" alt="在这里插入图片描述">

### 3、安装远程ssh服务

注意，由于xshell远程连接ubuntu是通过ssh协议的，所以，确保ubuntu安装ssh服务器：

```
sudo apt-get install openssh-server

```

<img src="https://img-blog.csdnimg.cn/ecb12994c9724681a7aa575ad7f53d98.png" alt="在这里插入图片描述">

如没有ssh，需要执行如下命令：

```
sudo apt-get install ssh

```

注：centos 系统请用下面命令

```
yum install openssh-server

```

### 4、开启ssh-server服务

#### 4.1 Ubuntu系统使用如下命令：

开启 ssh-server，在命令行输入 “service ssh start”，然后输入密码即可；

```
service ssh start

```

#### 4.1 Centos系统使用如下命令：

启动命令：

```
systemctl start sshd

```

停止服务：

```
systemctl stop sshd 

```

重启SSH服务：

```
systemctl restart sshd 

```

设置开机自启：

```
systemctl enable sshd

```

### 5、验证是否开启ssh-server服务

查看是否启动ssh，在命令行输入：“ps -e|grep ssh”。出现sshd表示成功。

```
ps -e|grep ssh

```

<img src="https://img-blog.csdnimg.cn/a1c3035d3f3b4e71a9813235c9e68205.png" alt="在这里插入图片描述">

```
netstat -antp | grep sshd

```

<img src="https://img-blog.csdnimg.cn/1483f9998612494eb0b954fd4a8dc14e.png" alt="在这里插入图片描述">

### 6、打开Xshell并新建会话

<img src="https://img-blog.csdnimg.cn/d8138417c018488a9f61ce6b36bab21a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/0b3409a51775443f8f460d0cea3034eb.png" alt="在这里插入图片描述"> 输入用户名： <img src="https://img-blog.csdnimg.cn/208fd4af4f9445d2aeef8eef48f37cf7.png" alt="在这里插入图片描述">

输入密码即可： <img src="https://img-blog.csdnimg.cn/dbcf6bffda2441068a941d3a0b226c77.png" alt="在这里插入图片描述">

### 7、连接成功

<img src="https://img-blog.csdnimg.cn/ee872a21b8b14645a0e5d2e8966f118c.png" alt="在这里插入图片描述">
