
--- 
title:  第二章 Docker环境搭建 
tags: []
categories: [] 

---
请提前在PC端上装好虚拟机VMware Workstation Pro

>  
 **注意：第二、第三和第四章的全部步骤都是在虚拟机上的terminal上进行！！** 


#### 一、安装Docker

（1）使用命令卸载可能存在的旧版本：

```
User:$ sudo apt-get remove docker docker-engine docker-ce docker.io
```

（2）使用命令安装curl包：

```
User:$ sudo apt-get install curl
```

（3）添加Docker官方的GPG密钥：

```
User:$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

（4）安装最新版本的Docker CE以及相关工具：

```
User:$ sudo apt-get update &amp;&amp; sudo apt install docker-ce docker-ce-cli containerd.io
```

#### 二、验证Docker

（1）查看docker服务是否启动：

```
User:$ systemctl status docker
```

（2）若未启动，则启动docker服务：

```
User:$ sudo systemctl start docker
```

（3）测试运行hello world例程，如图7所示：

```
User:$ sudo docker run hello-world
```

<img alt="" height="94" src="https://img-blog.csdnimg.cn/direct/c25267b44dee40cfafd078780748a0ad.png" width="407">

图8

今天不学习，明天变垃圾！！！
