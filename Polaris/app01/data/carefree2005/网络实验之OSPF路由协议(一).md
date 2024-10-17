
--- 
title:  网络实验之OSPF路由协议(一) 
tags: []
categories: [] 

---
## 一、OSPF路由协议简介

  开放式最短路径优先（Open Shortest Path First，OSPF）路由协议是用于网际协议（IP）网络的链路状态路由协议。该协议使用链路状态路由算法的内部网关协议（IGP），在单一自治系统（AS）内部工作。适用于IPv4的OSPFv2协议定义于RFC 2328，RFC 5340定义了适用于IPv6的OSPFv3。OSPF是广泛使用的一种动态路由协议，它属于链路状态路由协议，具有路由变化收敛速度快、无路由环路、支持变长子网掩码（VLSM）和汇总、层次区域划分等优点。在网络中使用OSPF协议后，大部分路由将由OSPF协议自行计算和生成，无须网络管理员人工配置，当网络拓扑发生变化时，协议可以自动计算、更正路由，极大地方便了网络管理。

## 二、OSPF路由协议实践

### 1、实验环境

  博文实验环境采用GNS3模拟器搭建OSPF网络实验环境，路由器使用c7200，iso系统版本为c7200-advipservicesk9-mz.124-20.T.bin。

### 2、拓扑图

  OSPF是我们企业网中最常用的动态路由协议，通过OSPF我们可以实现路由的自动更新和配置，尤其是在大企业网中可以极大的减少路由配置的工作，而且路由可以完成自动更新和收敛，非常的好用。如下拓扑图，我们使用三台路由器模拟OSPF动态路由协议的企业网。通过network宣告路由，实现路由的学习和发布。然后在R1上配置loop 1，通过重发布直连路由实现路由表的更新和发布。 <img src="https://img-blog.csdnimg.cn/902b5e73871848c8b87b02699e407d01.png" alt="在这里插入图片描述">

### 3、网络配置

  R1路由器配置：

```
R1#conf t
R1(config)#ip routing
R1(config)#int f0/0 
R1(config-if)#ip add 12.12.12.1 255.255.255.0
R1(config-if)#no shut
R1(config-if)#int f0/1
R1(config-if)#ip add 13.13.13.1 255.255.255.0
R1(config-if)#no shut
R1(config-if)#ip add 1.1.1.1 255.255.255.0
R1(config-if)#no shut
R1(config)#router ospf 100
R1(config-router)#router-id 1.1.1.1
R1(config-router)#network 12.12.12.0 0.0.0.255 area 0
R1(config-router)#network 13.13.13.0 0.0.0.255 area 0
R1(config-router)#network 1.1.1.0 0.0.0.255 area 1
R1(config-router)#end
R1#wr mem

```

  R2路由器配置：

```
R2#conf t
R2(config)#ip routing 
R2(config)#int f0/0
R2(config-if)#no shut
R2(config-if)#ip add 12.12.12.2 255.255.255.0
R2(config-if)#int f0/1
R2(config-if)#ip add 23.23.23.2 255.255.255.0
R2(config-if)#no shut
R2(config-if)#int loop 0
R2(config-if)#ip add 2.2.2.2 255.255.255.0
R2(config-if)#no shut
R2(config-if)#router ospf 100
R2(config-router)#router-id 2.2.2.2
R2(config-router)#network 12.12.12.0 0.0.0.255 area 
R2(config-router)#network 23.23.23.0 0.0.0.255 area 0
R2(config-router)#network 2.2.2.0 0.0.0.255 area 2
R2(config-router)#end
R2#wr mem

```

  R3路由器配置：

```
R3#conf t
R3(config)#ip routing 
R3(config)#int f0/0
R3(config-if)#ip add 13.13.13.3 255.255.255.0
R3(config-if)#no shut
R3(config-if)#int f0/1
R3(config-if)#ip add 23.23.23.3 255.255.255.0
R3(config-if)#no shut
R3(config)#int loop 0
R3(config-if)#ip add 3.3.3. 
R3(config-if)#no shut
R3(config-if)#router ospf 100
R3(config-router)#rou
R3(config-router)#router-id 3.3.3.3
R3(config-router)#netwo
R3(config-router)#network 13.13.13.0 0.0.0.255 area 0
R3(config-router)#network 23.23.23.0 0.0.0.255 area 0
R3(config-router)#network 23.23.23.0 0.0.0.255 area 0
R3(config-router)#network 3.3.3.0 0.0.0.255 area 3
R3(config-router)#end
R3#wr mem

```

### 4、协议验证测试
- OSPF邻居验证   使用show ip ospf nei命令查看邻居状态，可以看到不同的链路上角色不一样，有的是BDR，有的是DR。 #在R1上查看OSPF邻居
>  
 R1#show ip ospf nei  Neighbor ID Pri State Dead Time Address Interface 3.3.3.3 1 FULL/BDR 00:00:32 13.13.13.3 FastEthernet0/1 2.2.2.2 1 FULL/DR 00:00:33 12.12.12.2 FastEthernet0/0 #在R2上查看OSPF邻居 R2#show ip ospf nei  Neighbor ID Pri State Dead Time Address Interface 3.3.3.3 1 FULL/BDR 00:00:33 23.23.23.3 FastEthernet0/1 1.1.1.1 1 FULL/BDR 00:00:37 12.12.12.1 FastEthernet0/0 #在R3上查看OSPF邻居 R3#show ip ospf nei  Neighbor ID Pri State Dead Time Address Interface 2.2.2.2 1 FULL/DR 00:00:34 23.23.23.2 FastEthernet0/1 1.1.1.1 1 FULL/DR 00:00:36 13.13.13.1 FastEthernet0/0 

- OSPF路由验证   完成OSPF动态路由协议的基础配置后，我们验证各路由器的路由器，是否包含R1、R2、R3个网段的路由。
>  
 R1#ping 2.2.2.2  Type escape sequence to abort. Sending 5, 100-byte ICMP Echos to 2.2.2.2, timeout is 2 seconds: !!! Success rate is 100 percent (5/5), round-trip min/avg/max = 20/29/32 ms R1#ping 3.3.3.3  Type escape sequence to abort. Sending 5, 100-byte ICMP Echos to 3.3.3.3, timeout is 2 seconds: !!! Success rate is 100 percent (5/5), round-trip min/avg/max = 32/39/56 ms <img src="https://img-blog.csdnimg.cn/794a00de08ef48ecaecb8942459dc317.png" alt="在这里插入图片描述"> 

- 重发布路由验证   在R1上配置默认路由，然后重发布到OSPF中，然后在R2和R3上
>  
 R1(config)#int loop 1 R1(config-if)#ip add 11.11.11.11 255.255.255.0 R1(config)#router ospf 100 R1(config-router)#redistribute connected subnets <img src="https://img-blog.csdnimg.cn/0f7eed88ce8f48b2a738dca7af72868c.png" alt="在这里插入图片描述"> 


## 三、实验总结

  此博文只是OSPF的基础实验，OSPF的area 0区域建议使用全互联的方式，会根据router-id大小选举DR和BDR。

### 1、OSPF的基本特性
- OSPF属于IGP，是Link-State协议，基于IP Pro 89。OSPF报文封装进ip包。- 采用SPF算法（Dijkstra算法）计算最佳路径。- 快速响应网络变化。- 以较低频率（每隔30分钟）发送定期更新，被称为链路状态刷新。- 网络变化时是触发更新。- 支持等价的负载均衡。
### 2、OSPF维护的3张表
- Neighbor Table： 　确保直接邻居之间能够双向通信。- Topology Table： 　LSDB(Link-State DataBase），同一区域的所有路由器LSDB相同。- Routing Table： 　对LSDB应用SPF算法，选择到达目标地址的最佳路由放入路由表。
### 3、OSPF的区域划分

  OSPF采用层次设计，用Area来分隔路由器。区域中的路由器保存该区域中所有链路和路由器的详细信息；但只保存其他区域路由器和链路的摘要信息。

### 4、设置Route-ID的优先顺序
- 手工指定Route-ID x.x.x.x（可任意，但区域内不能重复）- 自动选择最大的Loopback IP作route-id- 自动选择最大的物理接口IP（接口必须是激活状态）