
--- 
title:  网络实验之DHCP及DHCP中继实验 
tags: []
categories: [] 

---
## 一、DHCP简介

  动态主机配置协议 DHCP（Dynamic Host Configuration Protocol，动态主机配置协议） 是 RFC 1541（已被 RFC 2131 取代）定义的标准协议，该协议允许服务器向客户端动态分配 IP 地址和配置信息。DHCP采用UDP作为传输协议，客户端发送消息到DHCP服务器的的67号端口，服务器返回消息给客户端的68号端口。DHCP协议支持C/S（客户端/服务器）结构，主要分为两部分：
- 1、DHCP客户端：通常为网络中的PC、打印机等终端设备，使用从DHCP服务器分配下来的IP信息，包括IP地址、DNS等。- 2、DHCP服务器：所有的IP网络设定信息都由DHCP服务器集中管理，并处理客户端的DHCP请求。
## 二、DHCP配置实践

### 1、实验环境说明

  博文实验环境采用GNS3模拟器搭建DHCP网络实验环境，路由器使用c7200，iso系统版本为c7200-advipservicesk9-mz.124-20.T.bin。

### 2、拓扑图

  DHCP是局域网必备可少的，我们手机、电脑等终端接入网络能获取到IP地址就是DHCP协议的功劳。通过DHCP协议可以减少我们接入网络时手动配置IP地址的工作，终端用户不需要了解网络结构，非常便捷。如下拓扑图，我们使用R1作为DHCP服务器，PC1通过dhcp协议获取IP地址、网关、dns等信息。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/735beb1481a749f2ad7c475eff8f4fd8.png">

### 3、DHCP server网络配置

  R1路由器作为DHCP服务器，配置如下。

```
R1(config)#no ip dhcp conflict logging
R1(config)#ip dhcp pool sunsite
R1(dhcp-config)#network 192.168.10.0 255.255.255.0
R1(dhcp-config)#default-router 192.168.10.254
R1(dhcp-config)#dns-server 114.114.114.114
R1(dhcp-config)#lease 0 4
R1(dhcp-config)#exit
R1(config)#ip dhcp excluded-address 192.168.10.250 192.168.10.254
R1(config)#ip dhcp ping packets 3
R1(config)#int f0/0
R1(config-if)#ip add 192.168.10.254 255.255.255.0
R1(config-if)#no shut

```

### 4、协议实践验证

  PC1上使用dhcp命令就可以通过dhcp获取到IP地址、网关、DNS等信息。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2bb7c734497147b194de41287661e772.png">

## 三、DHCP中继配置实践

### 1、实验环境说明

  博文实验环境采用GNS3模拟器搭建DHCP网络实验环境，路由器使用c7200，iso系统版本为c7200-advipservicesk9-mz.124-20.T.bin。

### 2、拓扑图

  R1作为DHCP server，R2配置DHCP中继，PC1和PC2通过DHCP server获取IP地址。其中pc1属于地址段192.168.10.x,网关地址在R1的F0/0，pc2属于地址段192.168.20.x,网关地址在R2的F0/0。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/87360542288e4441add088bf862ada1e.png">

### 3、网络配置

  R1路由器作为DHCP server路由器，新增配置如下。

```
R1(config)#ip routing
R1(config)#ip dhcp pool sunsite2
R1(dhcp-config)#network 192.168.20.0 255.255.255.0
R1(dhcp-config)#default-router 192.168.20.254
R1(dhcp-config)#dns-server 114.114.114.114
R1(dhcp-config)#lease 0 4
R1(dhcp-config)#exit
R1(config)#ip dhcp excluded-address 192.168.20.250 192.168.20.254
R1(config)#int f0/1
R1(config-if)#ip add 12.12.12.1 255.255.255.252
R1(config-if)#no shut
R1(dhcp-config)#exit
R1(config)#ip route 192.168.20.0 255.255.255.0 12.12.12.2
R1(config)#end
R1#wr mem

```

  R2作为DHCP中继路由器，配置如下：

```
R2(config-if)#int f0/0            
R2(config-if)#ip add 12.12.12.2 255.255.255.252
R2(config-if)#no shut
R2(config-if)#exit
R2(config)#ip routing 0.0.0.0 0.0.0.0 12.12.12.1
R2(config-if)#ip helper-address 12.12.12.1
R2(config)#int f0/1
R2(config-if)#ip add 12.12.12.2 255.255.255.252
R2(config-if)#no shut
R2(config-if)#end
R2#wr mem

```

### 4、协议实践验证

  PC2上使用dhcp命令就可以通过dhcp获取到IP地址、网关、DNS等信息，也可以ping通pc1主机地址。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9ddce909ff5f4f27ba8b724f37a65714.png"><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3c1acaea20874644848ecd42695eaa64.png">   查看IP和MAC地址绑定关系，可以查看到dhcp client地址分配情况。

>  
 R1#show ip dhcp binding Bindings from all pools not associated with VRF: IP address Client-ID/ Lease expiration Type Hardware address/ User name 192.168.10.1 0100.5079.6668.00 Jan 02 2023 01:46 PM Automatic 192.168.20.1 0100.5079.6668.01 Jan 02 2023 02:24 PM Automatic 


## 四、总结
- 在ＤＨＣＰ服务器上还必须有去ＰＣ所在网段的路由；- 在客户端设备和DHCP服务器不再同一广播域内的时候，中间设备即路由器必须要能够转发这种广播包，具体到cisco的设备上，则启用ip helper-address命令，来实现这种中继；- 在一台路由器上可以同时配很多个DHCP服务，取不同的名，接口根据自己的IP地址来决定下发哪一个DHCP服务。
  DHCP的请求过程：
- 1、client向server发送请求，发向广播地址 discover- 2、server向client回应一个IP，发向单播地址 offer- 3、client向server回应一个确认，发向广播地址，表示自已已得到IP地址，这样可以防止在网络上有多台DHCP服务器的情况下，其它服务器不会再给它分配IP request- 4、server再向client回应一个确认 acknowledge