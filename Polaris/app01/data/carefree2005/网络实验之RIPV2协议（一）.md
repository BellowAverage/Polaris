
--- 
title:  网络实验之RIPV2协议（一） 
tags: []
categories: [] 

---
## 一、RIPV2协议简介

  RIP (Routing Information Protocol) 路由协议是一种相对古老，在小型以及同介质网络中得到了广泛应用的一种路由协议。RIP 采用距离向量算法，是一种距离向量协议。RIP-1是有类别路由协议（Classful Routing Protocol），它只支持以广播方式发布协议报文。RIP-1的协议报文无法携带掩码信息，它只能识别A、B、C类这样的自然网段的路由，因此RIP-1不支持非连续子网（Discontiguous Subnet）。RIP-2是一种无类别路由协议（Classless Routing Protocol），支持路由标记，在路由策略中可根据路由标记对路由进行灵活的控制。报文中携带掩码信息，支持路由聚合和CIDR（Classless Inter-Domain Routing，无类域间路由）。

## 二、RIPV2路由协议实践

### 1、实验环境说明

  博文实验环境采用GNS3模拟器搭建RIPV2网络实验环境，三层交换机使用3640，iso系统版本为c3640-jk9o3s-mz.124-10a.bin。

### 2、拓扑图

  如下图所示，我们使用4台三层交换机模拟RIP企业网，每台路由器下联一个局域网网段，路由器至少有两条链路与其他路由器互联。使用四台PC模拟四个局域网的终端，IP地址段分别为192.168.x.0/24。路由器之间互联地址为了简化记忆，方便配置，博主采用了12.12.12.0/24的样式，最后1位路由器ID，实际网络中互联地址常采用/30地址段进行互联。 <img src="https://img-blog.csdnimg.cn/b17daddbb7ca4907a4c9c4a17ba9149b.png" alt="在这里插入图片描述">

### 3、网络配置
- 路由器1配置
```
conf t
ip routing
interface Ethernet0/0
 ip address 192.168.1.254 255.255.255.0
 full-duplex
 no shutdown
!
interface Ethernet0/1
 ip address 12.12.12.1 255.255.255.0
 full-duplex
 no shutdown
!
interface Ethernet0/2
 ip address 14.14.14.1 255.255.255.0
 no shutdown
 full-duplex
!
router rip
 version 2
 redistribute connected
 network 12.12.12.0
 network 14.14.14.0
 no auto-summary
!
end
wr

```
- 路由器2配置
```
conf t
ip routing
interface Ethernet0/0
 ip address 192.168.2.254 255.255.255.0
 full-duplex
 no shutdown
!
interface Ethernet0/1
 ip address 12.12.12.2 255.255.255.0
 full-duplex
 no shutdown
!
interface Ethernet0/2
 ip address 23.23.23.2 255.255.255.0
 full-duplex
 no shutdown
!
router rip
 version 2
 redistribute connected
 network 12.12.12.0
 network 23.23.23.0
 no auto-summary
!
end
wr

```
- 路由器3配置
```
conf t
ip routing
interface Ethernet0/0
 ip address 192.168.3.254 255.255.255.0
 full-duplex
 no shutdown
!
interface Ethernet0/1
 ip address 23.23.23.3 255.255.255.0
 full-duplex
 no shutdown
!
interface Ethernet0/2
 ip address 34.34.34.3 255.255.255.0
 full-duplex
 no shutdown
!
router rip
 version 2
 redistribute connected
 network 23.23.23.0
 network 34.23.23.0
 no auto-summary
!
end
wr

```
- 路由器4配置
```
interface Ethernet0/0
 ip address 192.168.4.254 255.255.255.0
 full-duplex
 no shutdown
!
interface Ethernet0/1
 ip address 14.14.14.4 255.255.255.0
 half-duplex
 no shutdown
!
interface Ethernet0/2
 ip address 34.34.34.4 255.255.255.0
 full-duplex
 no shutdown
!
interface Ethernet0/3
 no ip address
 shutdown
 full-duplex
!
router rip
 version 2
 redistribute connected
 network 14.14.14.0
 network 34.34.34.0
 no auto-summary
!
end
wr

```

### 4、协议实践验证
- 网络通断性验证 在PC1上ping验证，通过如上的简单配置就可以实现PC1到PC2、PC3、PC4各主机的访问。我们只使用了RIP动态路由协议，没有配置任何的静态路由就实现了各网段之间的联通。 <img src="https://img-blog.csdnimg.cn/a9ac4d6bcb6349249fa23c89afe2801b.png" alt="在这里插入图片描述">- 链路中断测试 我们检查192.168.4.10路由是从14.14.14.4学到的；关闭e0/2端口后，我们马上检查路由发现已经没有192.168.4.10的路由；过大约15-30秒后再次检查路由发现已经从12.12.12.2学到了192.168.4.0/24网段的路由
```
R1#show ip route 192.168.4.10
Routing entry for 192.168.4.0/24
  Known via "rip", distance 120, metric 1
  Redistributing via rip
  Last update from 14.14.14.4 on Ethernet0/2, 00:00:18 ago
  Routing Descriptor Blocks:
  * 14.14.14.4, from 14.14.14.4, 00:00:18 ago, via Ethernet0/2
      Route metric is 1, traffic share count is 1

R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#int e0/2
R1(config-if)#shut
R1(config-if)#end
R1#wr mem
Building configuration...
[OK]
R1#
*Mar  1 10:50:26.633: %SYS-5-CONFIG_I: Configured from console by console
R1#show ip ro
*Mar  1 10:50:32.797: %LINK-5-CHANGED: Interface Ethernet0/2, changed state to administratively down
*Mar  1 10:50:33.797: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
R1#show ip route 192.168.4.10
% Network not in table
R1#show ip route 192.168.4.10
Routing entry for 192.168.4.0/24
  Known via "rip", distance 120, metric 3
  Redistributing via rip
  Last update from 12.12.12.2 on Ethernet0/1, 00:00:13 ago
  Routing Descriptor Blocks:
  * 12.12.12.2, from 12.12.12.2, 00:00:13 ago, via Ethernet0/1
      Route metric is 3, traffic share count is 1

```
- trace路由跟踪 通过trace路由跟踪我们可以看到PC1访问PC4的包访问路径是PC1-R1-R2-R3-R4-PC4。我们并没有重新配置路由，但是网络已经自动收敛后通了，这就是动态路由的好处。 <img src="https://img-blog.csdnimg.cn/e9e35b9946f741ab9f9ff551d6800a96.png" alt="在这里插入图片描述">- RIPV2配置检查
>  
 R1#show ip rip database R1#show ip protocols Routing Protocol is “rip” 


## 三、总结
- RIPV2协议是一种距离矢量协议，一般只适用于小型局域网- 以组播地址224.0.0.9发送更新。- RIPv2支持VLSM，更新发送时携带掩码信息。也只能以主类方式通告。