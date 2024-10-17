
--- 
title:  iftop工具详解——网络流量监控利器（详解+示例+实战） 
tags: []
categories: [] 

---
## 1 iftop命令

iftop是一款用于监控网络流量的命令行工具。它可以实时显示正在通过网络接口传输的数据流量信息，包括源和目标IP地址、端口号、数据传输速率等。 iftop 是 Linux 系统一个免费的网卡实时流量监控工具，类似于 top 命令。iftop 可以监控指定网卡的实时流量、端口连接信息、反向解析 IP 等，还可以精确显示本机网络流量及网络内各主机和本机相互通信的流量集合，非常适合于监控代理服务器或路由器的网络流量。 同时，iftop 对检测流量异常的主机非常有效，通过 iftop 的输出可以迅速定位主机流量异常的根源，这对于网络故障排查、网络安全检测是十分有用的。缺点就是无报表功能，且必须以 root 身份才能运行。

### 1.1 安装iftop

Centos上安装相关依赖包

```
yum install flex byacc  libpcap ncurses ncurses-devel libpcap-devel

```

下载安装：

```
wget http://www.ex-parrot.com/pdw/iftop/download/iftop-0.17.tar.gz
tar zxvf iftop-0.17.tar.gz
cd iftop-0.17
./configure
make &amp;&amp; make install

```

### 1.2 运行iftop

直接在命令行输入 iftop

```
iftop

```

<img src="https://img-blog.csdnimg.cn/564865e6d8df4799833386b4615dde38.png" alt="[图片]">

### 1.3 信息解读

在默认情况下，iftop显示系统第一块
