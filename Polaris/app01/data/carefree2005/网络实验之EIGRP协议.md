
--- 
title:  网络实验之EIGRP协议 
tags: []
categories: [] 

---
## 一、EIGRP协议简介

  EIGRP:Enhanced Interior Gateway Routing Protocol 即 增强内部网关路由协议。也翻译为 加强型内部网关路由协议。 EIGRP是Cisco公司的私有协议（2013年已经公有化）。 EIGRP结合了链路状态和距离矢量型路由选择协议的Cisco专用协议，采用弥散修正算法（DUAL）来实现快速收敛，可以不发送定期的路由更新信息以减少带宽的占用，支持Appletalk、IP、Novell和NetWare等多种网络层协议。

## 二、EIGRP协议实践

### 1、实验环境

  博文实验环境采用GNS3模拟器搭建EIGRP网络实验环境，路由器使用c7200，iso系统版本为c7200-advipservicesk9-mz.124-20.T.bin。

### 2、拓扑图

  EIGRP是思科私有协议，在数通产品发展早期，思科一家独大，运营商、各大企业主流的数通产品都是思科的，所以很多企业网内部的动态路由协议也使用了EIGRP协议。不过随着华为、H3C、锐捷等数通厂商的崛起，EIGRP协议也慢慢的退出了历史舞台，现在已经很少在国内的大型企业网见到了。我们使用三台路由器模拟EIGRP协议的基础配置。通过network宣告互联网段路由，然后查看EIGRP路由的管理距离值。重发布直连路由到EIGRP中，查看外部路由的管理距离值。 <img src="https://img-blog.csdnimg.cn/b17c72b78c3449888962a87fdb37c963.png" alt="在这里插入图片描述">

### 3、网络配置

  R1路由器配置：

```
R1#conf t
R1(config)#int f0/0
R1(config-if)#no shut
R1(config-if)#ip add 12.12.12.1 255.255.255.0
R1(config-if)#int g1/0
R1(config-if)#no shut
R1(config-if)#ip add 13.13.13.1 255.255.255.0
R1(config-if)#exit
R1(config)#ip routing
R1(config)#router eigrp 100
R1(config-router)#network 12.12.12.0 0.0.0.255
R1(config-router)#network 13.13.13.0 0.0.0.255
R1(config-router)#end
R1#wr mem

```

  R2路由器配置：

```
R2#conf t
R2(config)#int f0/0
R2(config-if)#no shut
R2(config-if)#ip add 12.12.12.2 255.255.255.0
R2(config-if)#int f0/1
R2(config-if)#no shut
R2(config-if)#ip add 23.23.23.2 255.255.255.0
R2(config-if)#exit
R2(config)#ip routing
R2(config)#router eigrp 100
R2(config-router)#network 12.12.12.0 0.0.0.255
R2(config-router)#network 23.23.23.0 0.0.0.255
R2(config-router)#end
R2#wr mem

```

  R3路由器配置：

```
R3#conf t
R3(config)#int f0/0
R3(config-if)#no shut
R3(config-if)#ip add 23.23.23.3 255.255.255.0
R3(config-if)#int g1/0
R3(config-if)#no shut
R3(config-if)#ip add 13.13.13.3 255.255.255.0
R3(config-if)#exit
R3(config)#ip routing
R3(config)#router eigrp 100
R3(config-router)#network 23.23.23.0 0.0.0.255
R3(config-router)#network 13.13.13.0 0.0.0.255
R3(config-router)#end
R3#wr mem

```

### 4、协议验证测试
- 验证EIGRP邻居 可以看到，三个路由器之间已经两两建立了邻居关系。
>  
 R1#show ip eigrp nei IP-EIGRP neighbors for process 100 H Address Interface Hold Uptime SRTT RTO Q Seq (sec) (ms) Cnt Num 1 13.13.13.3 Gi1/0 13 00:58:01 24 200 0 9 0 12.12.12.2 Fa0/0 13 00:58:28 26 200 0 8 

- 验证EIGRP内部路由管理距离值 <img src="https://img-blog.csdnimg.cn/0e9c8173ea60416195d2d58ecf8d8e93.png" alt="在这里插入图片描述">- 验证外部路由发布到EIGRP协议中的管理距离值
>  
 #在R2上创建三个loopback地址 R2(config-if)#int loop 0 R2(config-if)#ip add 192.168.0.254 255.255.255.0 R2(config-if)#int loop 1 R2(config-if)#ip add 192.168.1.254 255.255.255.0 R2(config-if)#exit R2(config)#router eigrp 100 R2(config-router)#redistribute connected #在R1上查看外部路由的管理距离值 <img src="https://img-blog.csdnimg.cn/b592333afcaa4367aa6306c4f270b183.png" alt="在这里插入图片描述"> 

- 验证不等价负载均衡路由配置
>  
 #首先查看当前路由，R1通过R2和R3都可以学习到23.23.23.0/24网段路由，因为G1/0口的开销值小，所以路由表中显示的是从G1/0口学习到，即从R3学习到该网段路由。 <img src="https://img-blog.csdnimg.cn/2d66a43d79474ea79433729558ccd538.png" alt="在这里插入图片描述"> 


#修改variance参数值

>  
 R1(config)#router eigrp 100 R1(config-router)#variance 2 #再次查看路由表 <img src="https://img-blog.csdnimg.cn/cdc191e7e7f24edaa535643e910957ee.png" alt="在这里插入图片描述"> 


## 三、总结
- 通过发送和接收Hello包来建立和维持邻居关系，并交换路由信息；- 采用组播（224.0.0.10）或单播进行路由更新；- EIGRP的管理距离为90或170；- 采用增量更新，减少带宽占用；- 支持可变长子网掩码（VLSM），默认开启自动汇总功能；- 支持IP、IPX和AppleTalk等多种网络层协议；- 对每一种网络协议，EIGRP都维持独立的邻居表、拓扑表和路由表；- EIGRP使用Diffusing Update算法（DUAL）来实现快速收敛并确保没有路由环路；- 存储整个网络拓扑结构的信息，以便快速适应网络变化；- 支持等价和非等价的负载均衡；- 使用可靠传输协议（RTP）保证路由信息传输的可靠性。- 无缝连接数据链路层协议和拓扑结构，EIGRP不要求对OSI参考模型的2层协议进行特别的配置。