
--- 
title:  Linux之网络性能测试工具netperf实践 
tags: []
categories: [] 

---
## 一、netperf简介

  Netperf是一种网络性能的测量工具，主要针对基于TCP或UDP的传输。Netperf根据应用的不同，可以进行不同模式的网络性能测试，即批量数据传输（bulk data transfer）模式和请求/应答（request/reponse）模式。Netperf测试结果所反映的是一个系统能够以多快的速度向另外一个系统发送数据，以及另外一个系统能够以多快的速度接收数据。   Netperf工具以client/server方式工作。server端是netserver，用来侦听来自client端的连接，client端是netperf，用来向server发起网络测试。在client与server之间，首先建立一个控制连接，传递有关测试配置的信息，以及测试的结果；在控制连接建立并传递了测试配置信息以后，client与server之间会再建立一个测试连接，用来来回传递着特殊的流量模式，以测试网络的性能。

## 二、安装步骤

### 1、安装gcc编译环境

>  
 [root@s142 ~]# yum install -y gcc* 


### 2、下载netperf软件包

>  
 [root@s142 software]# wget https://github.com/HewlettPackard/netperf/archive/refs/tags/netperf-2.7.0.zip 


### 3、解压软件包

>  
 [root@s142 software]# unzip netperf-2.7.0.zip 


### 4、预编译

>  
 [root@s142 software]# cd netperf-netperf-2.7.0/ [root@s142 netperf-netperf-2.7.0]# ./configure 


### 5、编译

>  
 [root@s142 netperf-netperf-2.7.0]# make make all-recursive … make[2]: Leaving directory `/opt/software/netperf-netperf-2.7.0’ make[1]: Leaving directory `/opt/software/netperf-netperf-2.7.0’ 


### 5、安装

>  
 [root@s142 netperf-netperf-2.7.0]# make install 


### 6、查看命令版本

>  
 [root@s142 netperf-netperf-2.7.0]# netserver -V Netperf version 2.7.0 [root@s142 netperf-netperf-2.7.0]# netperf -V Netperf version 2.7.0 


### 7、获取命令帮助

  实际上如果不执行编译安装命令，也可以在src目录下找到命令，并直接执行命令。当然我们执行了编译安装就不需要切换到编译目录下执行命令了，可以在任意目录下执行这两个命令。

>  
 [root@s142 src]# ./netserver --help ./netserver: invalid option – ‘-’  Usage: netserver [options]  Options: -h Display this text -D Do not daemonize -d Increase debugging output -f Do not spawn chilren for each test, run serially -L name,family Use name to pick listen address and family for family -N No debugging output, even if netperf asks -p portnum Listen for connect requests on portnum. -4 Do IPv4 -6 Do IPv6 -v verbosity Specify the verbosity level -V Display version information and exit -Z passphrase Expect passphrase as the first thing received <img src="https://img-blog.csdnimg.cn/d67576e4e9814684a6fa91b1d054f742.png" alt="在这里插入图片描述"> 


## 三、netperf网络性能测试实践

### 1、测试规划

  netperf工具工作模式为server/client模式，所以我们需要两台测试服务器，都安装netperf工具，然后一端模式服务端，一端模拟客户端。 <img src="https://img-blog.csdnimg.cn/cc89426ebce1428c884f9bee1553e9e9.png" alt="在这里插入图片描述">

### 2、批量数据（TCP流）传输测试
- 在s152服务器上运行服务端 Netperf缺省情况下进行TCP批量传输，即-t TCP_STREAM。测试过程中，netperf向netserver发送批量的TCP数据分组，以确定数据传输过程中的吞吐量。
>  
 [root@s152 netperf-netperf-2.7.0]# netserver -p 8888 Starting netserver with host ‘IN(6)ADDR_ANY’ port ‘8888’ and family AF_UNSPEC [root@s152 netperf-netperf-2.7.0]# netstat -tnpl |grep 8888 tcp6 0 0 :::8888 ::😗 LISTEN 9043/netserver 

- 在s142客户端上测试连接 通过测试结果可以看到使用16384字节大小socket发送缓存，接受缓存大小为87380字节，历时10.26秒，带宽吞吐量为93.96Mbit/s。
>  
 [root@s142 netperf-netperf-2.7.0]# netperf -H 192.168.0.152 -p 8888 <img src="https://img-blog.csdnimg.cn/9af2a1bfc5e644f4ac6004a555f9f683.png" alt="在这里插入图片描述"> 


### 3、批量数据（UDP流）传输测试
- 在s152服务器上运行服务端 Netperf测试UDP数据包无需在服务器端指定参数，所以不用重启服务器端，只需要在客户端加上-t UDP_STREAM
>  
 [root@s152 netperf-netperf-2.7.0]# netserver -p 8888 

- 在s142客户端上测试连接 UDP测试结果有两行，第一行显示的是客户端的发送统计，这里的吞吐量表示Netperf向本地socket发送分组的能力。第二行显示的是服务器端接收的情况，由于UDP协议的不可靠性，远端系统的接收吞吐量要远远小于发送出去的吞吐量。
>  
 [root@s142 netperf-netperf-2.7.0]# netperf -t UDP_STREAM -H 192.168.0.152 -p 8888 – -m 1024 -M 1024 -s 16384 -S 16384<img src="https://img-blog.csdnimg.cn/a2d2ef52d76e4aa0ba3f800d65c78daf.png" alt="在这里插入图片描述"> 


### 4、TCP长连接性能测试
- 测试请求/应答（request/response）网络流量的性能，TCP_RR模式 TCP_RR方式的测试对象是多次TCP request和response的交易过程，但是它们发生在同一个TCP连接中，这种模式常常出现在数据库应用中。数据库的client程序与server程序建立一个TCP连接以后，就在这个连接中传送数据库的多次交易过程。Netperf输出的结果也是由两行组成。第一行显示本地系统的情况，第二行显示的是远端系统的信息。
>  
 [root@s142 netperf-netperf-2.7.0]# netperf -t TCP_RR -H 192.168.0.152 -p 8888 [root@s142 netperf-netperf-2.7.0]# netperf -t TCP_RR -H 192.168.0.152 -p 8888 – -r 500,500 <img src="https://img-blog.csdnimg.cn/d940fa020fe347e680b3828b97e846c5.png" alt="在这里插入图片描述"> 


### 5、TCP短连接性能测试
- 测试请求/应答（request/response）网络流量的性能，TCP_CRR模式 与TCP_RR不同，TCP_CRR为每次交易建立一个新的TCP连接。最典型的应用就是HTTP，每次HTTP交易是在一条单独的TCP连接中进行的。因此，由于需要不停地建立新的TCP连接，并且在交易结束后拆除TCP连接，交易率一定会受到很大的影响。
>  
 [root@s142 netperf-netperf-2.7.0]# netperf -t TCP_CRR -H 192.168.0.152 -p 8888 [root@s142 netperf-netperf-2.7.0]# netperf -t TCP_CRR -H 192.168.0.152 -p 8888 – -r 500,500 <img src="https://img-blog.csdnimg.cn/12afca49b4954aaca1ec2495e7902244.png" alt="在这里插入图片描述"> 


## 四、常用参数说明

### 1、netserver命令常用参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-h</td><td align="left">获取命令帮助</td>
<td align="left">-V</td><td align="left">查看命令版本</td>
<td align="left">-p</td><td align="left">指定监听端口</td>
<td align="left">-4</td><td align="left">指定IPv4协议</td>
<td align="left">-6</td><td align="left">指定IPv6协议</td>
<td align="left">-D</td><td align="left">不在后台运行，默认后台运行</td>
<td align="left">-d</td><td align="left">增加debug输出</td>
<td align="left">-L</td><td align="left">使用主机名监听</td>
<td align="left">-N</td><td align="left">不输出debug信息</td>

### 2、netperf命令常用参数说明

  netperf命令格式为：netperf [global options] – [test specific options] 如下列表中的-m,-r这些参数都是测试专有参数，需要写在–后。

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-t testname</td><td align="left">指定进行的测试类型（TCP_STREAM，UDP_STREAM，TCP_RR，TCP_CRR，UDP_RR），可以通过man netperf命令查看有哪些类型</td>
<td align="left">-H ip</td><td align="left">指定远端运行netserver的server IP地址</td>
<td align="left">-p port</td><td align="left">指定远端运行netserver的port端口</td>
<td align="left">-L testlen</td><td align="left">指定测试时间，默认10s，单位秒</td>
<td align="left">-V</td><td align="left">查看命令版本</td>
<td align="left">-h</td><td align="left">获取命令帮助</td>
<td align="left">-s size</td><td align="left">设置本地系统的socket发送与接收缓冲大小</td>
<td align="left">-S size</td><td align="left">设置远端系统的socket发送与接收缓冲大小</td>
<td align="left">-m size</td><td align="left">设置本地系统发送测试分组的大小</td>
<td align="left">-M size</td><td align="left">设置远端系统接收测试分组的大小</td>
<td align="left">-r req,resp</td><td align="left">设置request和reponse分组的大小</td>
<td align="left">-D</td><td align="left">对本地与远端系统的socket设置TCP_NODELAY选项</td>
