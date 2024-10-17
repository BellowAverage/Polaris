
--- 
title:  解决-bash telnet command not found 
tags: []
categories: [] 

---
## 解决-bash: telnet: command not found

telnet命令通常用来远程登录，例如安装了某服务，想 telnet远程登录查看一下，是否正常启动。

#### 1、linux安装：

当我在linux虚拟机下敲下telnet时，发现提示 -bash:telnet:command not found：

Linux centos 运行telnet命令，出现下面的错误提示：

```
[root@localhost ~]# telnet 127.0.0.1
-bash: telnet: command not found

```

### 第一步：我们先查看虚拟机有没有安装telnet客户端和telnet-server服务端

#rpm -q telnet

#rpm -q telnet-server

都是空白的话，说明没安装

### 第二步：下载telnet客户端和telnet-server 服务端

centos、安装telnet命令的方法.

```
    yum list telnet*              列出telnet相关的安装包
    yum install telnet-server          安装telnet服务
    yum install telnet.*           安装telnet客户端

```

#### 2、Windows安装：

控制面板 --》程序 --》 启用或关闭Windows功能 --》 Telnet客户端 <img src="https://img-blog.csdnimg.cn/d6ed40ee62144de5a86ce83758cf4206.png" alt="在这里插入图片描述">
