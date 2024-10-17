
--- 
title:  网络实验之VTP协议 
tags: []
categories: [] 

---
## 一、VTP协议简介

  VLAN中继协议，VTP，VLAN TRUNKING PROTOCOL，是CISCO专用协议，大多数交换机都支持该协议。VTP负责在VTP域内同步VLAN信息，这样就不必在每个交换上配置相同的VLAN信息。如协议名称，VTP协议需要依赖trunk链路承载。VTP是一种消息协议，使用第2层帧，在全网的基础上管理VLAN的添加、删除和重命名，以实现VLAN配置的一致性。可以用VTP管理网络中VLAN1到1005。有了VTP，就可以在一台交换机上集中进行配置变更，所作的变更会被自动传播到网络中所有其他的交换机上。（前提是在同一个VTP域）。VTP协议需要为了实现此功能，必须先建立一个VTP管理域，VTP有三种运行模式Server、Transparent、Client，Server模式是默认模式，各模式的区别如下：

<th align="left">功能项</th><th align="left">Server</th><th align="left">Client</th><th align="left">Transparent（透明模式）</th>
|------
<td align="left">增/删/改</td><td align="left">√</td><td align="left">×</td><td align="left">√（仅在本地有效）</td>
<td align="left">转发VTP(vlan)信息</td><td align="left">√</td><td align="left">√</td><td align="left">√</td>
<td align="left">同步vlan信息</td><td align="left">√</td><td align="left">√</td><td align="left">×</td>
<td align="left">保存NVRAM</td><td align="left">√</td><td align="left">×</td><td align="left">√</td>

## 二、VTP协议实践

### 1、实验环境说明

  博文实验环境采用GNS3模拟器搭建VTP网络实验环境，三层交换机使用3640，iso系统版本为c3640-jk9o3s-mz.124-10a.bin。

### 2、拓扑图

  如下拓扑图，网络中存在三个网段，分别属于不同的vlan，网关位于SW1交换机上。SW1交换机作为VTP的server，负责维护整个VTP域的vlan信息，SW3和SW4作为末端交换机，配置VTP client模式，从SW1同步vlan信息。SW2配置为transparent模式，可以传递VTP信息，但是不更新本地vlan信息，自行维护。 <img src="https://img-blog.csdnimg.cn/32325730f46e4ecbabb151b6ee6ef4e1.png" alt="在这里插入图片描述">

### 3、网络配置

  初始配置的情况下，SW1手动创建了vlan100-102，并配置了interface100-102的网关地址，SW2手动创建了vlan100，SW3-SW4通过VTP自动学习到vlan100-102。
- 交换机SW1配置
```
#如下是vlan database模式下配置
SW1#vlan database 
SW1(vlan)#vtp server 
SW1(vlan)#vtp domain sunsite
SW1(vlan)#vlan 100 name vlan100
SW1(vlan)#vlan 101 name vlan101
SW1(vlan)#vlan 102 name vlan102
SW1(vlan)#exit
#如下是全局模式下配置
conf t
hostname SW1
interface FastEthernet0/14
 switchport mode trunk
 switchport trunk allow vlan all
 switchport trunk encapsulation dot1q
 no shutdown 
!
interface FastEthernet0/15
 switchport mode trunk
 switchport trunk allow vlan all
 switchport trunk encapsulation dot1q
 no shutdown
!
interface Vlan100
 ip address 192.168.0.254 255.255.255.0
 no shutdown 
!
interface Vlan101
 ip address 192.168.1.254 255.255.255.0
 no shutdown 
!
interface Vlan102
 ip address 192.168.2.254 255.255.255.0
 no shutdown 
!

```
- 交换机SW2配置
```
#如下是vlan database模式下配置
SW2#vlan database 
SW2(vlan)#vtp transparent
SW2(vlan)#vlan 100 name vlan100
SW2(vlan)#exit
#如下是全局模式下配置
conf t
hostname SW2
interface FastEthernet0/0
 switchport mode access
 switchport access vlan 100
 no shutdown
!
interface FastEthernet0/14
 switchport mode trunk
 switchport trunk allow vlan all
 switchport trunk encapsulation dot1q
 no shutdown 
!
interface FastEthernet0/15
 switchport mode trunk
 switchport trunk allow vlan all
 switchport trunk encapsulation dot1q
 no shutdown
!

```
- 交换机SW3配置
```
#如下是vlan database模式下配置
SW3#vlan database 
SW3(vlan)#vtp client 
SW3(vlan)#vtp domain sunsite
SW3(vlan)#exit
#如下是全局模式下配置
conf t
hostname SW3
interface FastEthernet0/0
 switchport mode access
 switchport access vlan 100
 no shutdown
!
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 101
 no shutdown
!
interface FastEthernet0/2
 switchport mode access
 switchport access vlan 102
 no shutdown
!
interface FastEthernet0/15
 switchport mode trunk
 switchport trunk allow vlan all
 switchport trunk encapsulation dot1q
 no shutdown
!

```
- 交换机SW4配置
```
#如下是vlan database模式下配置
SW4#vlan database 
SW4(vlan)#vtp client 
SW4(vlan)#vtp domain sunsite
SW4(vlan)#exit
#如下是全局模式下配置
conf t
hostname SW4
interface FastEthernet0/0
 switchport mode access
 switchport access vlan 100
 no shutdown
!
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 101
 no shutdown
!
interface FastEthernet0/2
 switchport mode access
 switchport access vlan 102
 no shutdown
!
interface FastEthernet0/15
 switchport mode trunk
 switchport trunk allow vlan all
 switchport trunk encapsulation dot1q
 no shutdown
!

```

### 4、协议实践验证
- vtp client模式下的vlan同步情况检查 我们可以看到SW3,SW4虽然没有配置任何自定义vlan，但是通过VTP server学到了vlan100,vlan101,vlan102的配置。 <img src="https://img-blog.csdnimg.cn/cca395cda3e14de294c051a49e96246c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/18974b64a06d4e3e92fd28fa32b87933.png" alt="在这里插入图片描述">- vlan100网络通断性验证 <img src="https://img-blog.csdnimg.cn/fc437f068f974364a21610812dc11636.png" alt="在这里插入图片描述">- vlan101网络通断性验证 <img src="https://img-blog.csdnimg.cn/c493919e5efd401c8361ca095f29dee7.png" alt="在这里插入图片描述">- 交换机SW2上配置vlan101信息后验证PC2和网关的网络通断性 <img src="https://img-blog.csdnimg.cn/e0b826c1a60a40a9ad5bbcdd36a30188.png" alt="在这里插入图片描述">- SW1上删除vlan102，查看vtp client变化 vlan信息同步是随即发送的，但是网络的通断性恢复还需要一些时间，主要是vlan的变化，需要重新计算生成树，待生成树收敛完成网络就恢复通了。
>  
 SW1#vlan database SW1(vlan)#no vlan 102 Deleting VLAN 102… SW1(vlan)#exi APPLY completed. Exiting… SW1# <img src="https://img-blog.csdnimg.cn/1993eec308794d3eaaa03d553acff129.png" alt="在这里插入图片描述"> 

- vtp域密码认证 我们在server端配置vtp域的密码认证，因为client端没有配置密码，所以不会同步更新。
>  
 SW1#vlan database SW1(vlan)#vtp pass SW1(vlan)#vtp password cisco Password already set to cisco. SW1(vlan)#vlan 103 name vlan103 VLAN 103 modified: Name: vlan103 SW1(vlan)#exit APPLY completed. Exiting… <img src="https://img-blog.csdnimg.cn/ae38cceda1484dde831ad6c96c41a459.png" alt="在这里插入图片描述"> 

- 客户端配置vtp认证密码 vlan信息没有修改的情况下同步信息5分钟更新一次，认证密码不一致时不会进行更新。
>  
 #SW1 SW1#vlan database SW1(vlan)#vtp pass SW1(vlan)#vtp password cisco Password already set to cisco. SW1(vlan)#exit APPLY completed. Exiting… #SW2 SW2#vlan database SW2(vlan)#vtp pass SW2(vlan)#vtp password yhxx Password already set to yhxx SW2(vlan)#exit APPLY completed. Exiting… <img src="https://img-blog.csdnimg.cn/1edc5a3be9cd41c986d0bd60c72d4ae3.png" alt="在这里插入图片描述"> 


<img src="https://img-blog.csdnimg.cn/1541132a947c4f2f96f5a42799c3b0b6.png" alt="在这里插入图片描述">

## 三、总结
- VTP信息每5分钟通告一次， 或 触发更新(VLAN配置改变时通告)。- VTP通告帧发向组播MAC地址，0100.0ccc.cccc。- VTP有四种消息类型：1、汇总通告 2、子网通告 3、通告请求 4、VTP加入消息。- VTP的同步是由低版本号的交换机跟着高版本号的交换机做同步。- 每当修改VLAN信息一次，版本号就加1，版本低的SW跟版本高的SW学习VLAN信息。