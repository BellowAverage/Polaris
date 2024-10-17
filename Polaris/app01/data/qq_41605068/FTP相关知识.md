
--- 
title:  FTP相关知识 
tags: []
categories: [] 

---
FTP的port和pasv模式的工作方式：  

**一、ftp的port和pasv模式的工作方式**        FTP使用2个TCP端口，首先是建立一个命令端口（控制端口），然后再产生一个数据端口。国内很多教科书都讲ftp使用21命令端口和20数据端口，这个应该是教书更新太慢的原因吧。实际上FTP分为主动模式和被动模式两种，ftp工作在主动模式使用tcp 21和20两个端口，而工作在被动模式会工作在大于1024随机端口。FTP最权威的参考见RFC 959，有兴趣的朋友可以仔细阅读的文档了解FTP详细工作模式和命令。目前主流的FTP Server服务器模式都是同时支持port和pasv两种方式，但是为了方便管理安全管理防火墙和设置ACL了解FTP Server的port和pasv模式是很有必要的。

**1.1 ftp port模式（主动模式）**        主动方式的FTP是这样的：客户端从一个任意的非特权端口N（N&gt;1024）连接到FTP服务器的命令端口(即tcp 21端口)。紧接着客户端开始监听端口N+1，并发送FTP命令“port N+1”到FTP服务器。最后服务器会从它自己的数据端口（20）连接到客户端指定的数据端口（N+1），这样客户端就可以和ftp服务器建立数据传输通道了。ftp port模式工作流程如下图所示：

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/14218a598bb9f1bff5fc9e932845387d.png">

针对FTP服务器前面的防火墙来说，必须允许以下通讯才能支持主动方式FTP： 1、客户端口&gt;1024端口到FTP服务器的21端口 （入：客户端初始化的连接 S&lt;-C） 2、FTP服务器的21端口到客户端&gt;1024的端口（出：服务器响应客户端的控制端口 S-&gt;C） 3、FTP服务器的20端口到客户端&gt;1024的端口（出:服务器端初始化数据连接到客户端的数据端口 S-&gt;C） 4、客户端&gt;1024端口到FTP服务器的20端口（入：客户端发送ACK响应到服务器的数据端口 S&lt;-C）

如果服务器的ip为192.168.10.1在H3C 8500的GigabitEthernet 2/1/10 上创建in acl策略允许ftp 主动模式其他禁止： rule permit tcp source 192.168.10.1 0 source-port eq 21 destination-port gt 1024 rule permit tcp source 192.168.10.1 0 source-port eq 20 destination-port gt 1024 rele deny ip

**1.2 ftp pasv模式（被动模式）**        在被动方式FTP中，命令连接和数据连接都由客户端。当开启一个FTP连接时，客户端打开两个任意的非特权本地端口（N &gt; 1024和N+1）。第一个端口连接服务器的21端口，但与主动方式的FTP不同，客户端不会提交PORT命令并允许服务器来回连它的数据端口，而是提交PASV命令。这样做的结果是服务器会开启一个任意的非特权端口（P &gt; 1024），并发送PORT P命令给客户端。然后客户端发起从本地端口N+1到服务器的端口P的连接用来传送数据。ftp pasv模式工作流程如下图所示：

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/3a40bde2ee3716aed6bd4843b5b3dccb.png">

对于服务器端的防火墙来说，必须允许下面的通讯才能支持被动方式的FTP: 1、客户端&gt;1024端口到服务器的21端口 （入：客户端初始化的连接 S&lt;-C） 2、服务器的21端口到客户端&gt;1024的端口 （出：服务器响应到客户端的控制端口的连接 S-&gt;C） 3、客户端&gt;1024端口到服务器的大于1024端口 （入：客户端初始化数据连接到服务器指定的任意端口 S&lt;-C） 4、服务器的大于1024端口到远程的大于1024的端口（出：服务器发送ACK响应和数据到客户端的数据端口 S-&gt;C）

如果服务器的ip为192.168.10.1在H3C 8500的GigabitEthernet 2/1/10 上创建in acl策略允许ftp 主动模式其他禁止： rule permit tcp source 192.168.10.1 0 source-port eq 21 destination-port gt 1024 rule permit tcp source 192.168.10.1 0 source-port gt 1024 destination-port gt 1024 rele deny ip

**二、ftp的port和pasv模式的工作方式**        ftp的port和pasv模式最主要区别就是数据端口连接方式不同，ftp port模式只要开启服务器的21和20端口，而ftp pasv需要开启服务器大于1024所有tcp端口和21端口。重网络安全的角度来看的话似乎ftp port模式更安全，而ftp pasv更不安全，那么为什么RFC要在ftp port基础再制定一个ftp pasv模式呢？其实RFC制定ftp pasv模式的主要目的是为了数据传输安全角度出发的，因为ftp port使用固定20端口进行传输数据，那么作为黑客很容使用sniffer等探嗅器抓取ftp数据，这样一来通过ftp port模式传输数据很容易被黑客窃取，因此使用pasv方式来架设ftp server是最安全绝佳方案。        如果作为一个有经验的网络管理员就会发现使用ftp pasv方式会给网络安全很大隐患，那就是ftp pasv需要开启服务器tcp大于1024所有端口，这样对服务器的安全保护是非常不利的。在此我建议两种方法来完善FTP Pasv模式的端口开放问题，第一种就是使用弱洞扫描工具比如Xscan找出服务器开放的端口然后使用acl把端口deny掉，另外一种方法就是使用具有状态检测防火墙开启ftp pasv的端口。        在ftp pasv模式下是使用状态检测防火墙比acl最大的好处就是使用状态检测防火墙只要开启ftp 21端口就可以了，状态检测防火墙会检测客户端口连接ftp server的21命令端口，一但检测客户端使用ftp 21命令端口然后就会允许这个Session使用ftp服务器大于1024端口，而其他方式是无法直接访问ftp服务器大于1024端口。通过状态检测防火墙就可以保证ftp 服务器大于1024端口只对FTP Session开放了。目前像IPTable、ISA Server 2000/2004/2006、以及主流硬件防火墙都可以支持状态检测。
