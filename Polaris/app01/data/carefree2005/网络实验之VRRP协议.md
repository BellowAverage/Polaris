
--- 
title:  网络实验之VRRP协议 
tags: []
categories: [] 

---
## 一、VRRP协议简介

  虚拟路由冗余协议(Virtual Router Redundancy Protocol，简称VRRP)是由IETF提出的解决局域网中配置静态网关出现单点失效现象的路由协议。VRRP是一种路由容错协议，也可以叫做备份路由协议。一个局域网络内的所有主机都设置缺省路由，当网内主机发出的目的地址不在本网段时，报文将被通过缺省路由发往外部路由器，从而实现了主机与外部网络的通信。当缺省路由器down掉（即端口关闭）之后，内部主机将无法与外部通信，如果路由器设置了VRRP时，那么这时，虚拟路由将启用备份路由器，从而实现全网通信。   在VRRP协议中，有两组重要的概念：VRRP路由器和虚拟路由器，主控路由器和备份路由器。VRRP路由器是指运行VRRP的路由器，是物理实体；虚拟路由器是指VRRP协议创建的，是逻辑概念。一组VRRP路由器协同工作，共同构成一台虚拟路由器。该虚拟路由器对外表现为一个具有唯一固定的IP地址和MAC地址的逻辑路由器。处于同一个VRRP组中的路由器具有两种互斥的角色：主控路由器和备份路由器，一个VRRP组中有且只有一台处于主控角色的路由器，可以有一个或者多个处于备份角色的路由器VRRP协议从路由器组中选出一台作为主控路由器，负责ARP解析和转发IP数据包，组中的其他路由器作为备份的角色并处于待命状态，当由于某种原因主控路由器发生故障时，其中的一台备份路由器能在瞬间的时延后升级为主控路由器，由于此切换非常迅速而且不用改变IP地址和MAC地址，故对终端使用者系统是透明的。(以上内容来自百度百科)

## 二、VRRP协议实践

### 1、实验环境说明

  博文实验环境采用GNS3模拟器搭建VRRP网络实验环境，三层交换机使用3640，iso系统版本为c3640-jk9o3s-mz.124-10a.bin。

### 2、拓扑图

  如下拓扑图所示，我们使用vpc终端wuhs-pc模拟局域网终端主机，规划IP地址为192.168.0.10。配置一台接入交换机，纯二层交换机，模拟局域网，二层交换机通过双上联到两个主备网关交换机。使用SW1、SW2模拟局域网网关交换机。使用SW3模拟互联网，通过loopback地址172.16.0.1模拟互联网终端。此实验环境使用静态路由协议，所以SW1、SW2和SW3之间也将通过VRRP协议互联。 <img src="https://img-blog.csdnimg.cn/58cd805b203f47f1bd59363a8e56888e.png" alt="在这里插入图片描述">

### 3、网络配置
- 交换机一配置
```
SW1#conf t
SW1(config)#hostname SW1
SW1(config)#track 100 interface e0/1 line-protocol
SW1(config)#track 20 interface e0/0 line-protocol
SW1(config)#int e0/1
SW1(config-if)#ip address 192.168.0.252 255.255.255.0
SW1(config-if)#vrrp 100 ip 192.168.0.254
SW1(config-if)#vrrp 100 priority 200
SW1(config-if)#vrrp 100 preempt
SW1(config-if)#vrrp 100 track 20 decrement 100
SW1(config)#int e0/0
SW1(config-if)#ip address 10.10.10.1 255.255.255.0
SW1(config-if)#vrrp 20 ip 10.10.10.3
SW1(config-if)#vrrp 20 priority 200
SW1(config-if)#vrrp 20 preempt
SW1(config-if)#vrrp 20 track 100 decrement 100
SW1(config-if)#no shut
SW1(config-if)#exit
SW1(config)#ip route 0.0.0.0 0.0.0.0 10.10.10.4
SW1(config)#ip routing
SW1(config)#end
SW1#wr

```
- 交换机二配置
```
SW2#conf t
SW2(config)#hostname SW2
SW2(config)#int e0/1
SW2(config-if)#ip address 192.168.0.253 255.255.255.0
SW2(config-if)#vrrp 100 ip 192.168.0.254
SW2(config-if)#vrrp 100 priority 150
SW2(config-if)#vrrp 100 preempt
SW2(config)#int e0/0
SW2(config-if)#ip address 10.10.10.2 255.255.255.0
SW2(config-if)#vrrp 20 ip 10.10.10.3
SW2(config-if)#vrrp 20 priority 150
SW2(config-if)#vrrp 20 preempt 
SW2(config-if)#no shut
SW2(config-if)#exit
SW2(config)#ip route 0.0.0.0 0.0.0.0 10.10.10.4
SW2(config)#ip routing
SW2(config)#end
SW2#wr

```
- 交换机三配置
```
SW3#conf t
SW3(config)#hostname SW3
SW3(config)#int e0/0 
SW3(config-if)#ip add 10.10.10.4 255.255.255.0
SW3(config-if)#no shut
SW3(config-if)#int loop 0
SW3(config-if)#ip add 172.16.0.1 255.255.255.0
SW3(config-if)#exit
SW3(config)#ip route 192.168.0.0 255.255.255.0 10.10.10.3
SW3(config)#ip routing
SW3(config)#end
SW3#wr

```

### 4、协议实践测试
-  网络通断性测试 如下图，说明整个网络拓扑我们已经打通，从192.168.0.10这个PC终端可以ping通模拟互联网的loopback地址172.16.0.1。 <img src="https://img-blog.csdnimg.cn/eff46ba105cc4fd79b33be3d21609a27.png" alt="在这里插入图片描述"> -  trace路由验证 trace 172.16.0.1地址我们可以发现当前路由走的是252地址这个交换机 <img src="https://img-blog.csdnimg.cn/a34ee0d1334949329196f8eb65230df2.png" alt="在这里插入图片描述"> -  VRRP状态检查 可以看到当前SW1为VRRP的master，SW2为backup角色。 <img src="https://img-blog.csdnimg.cn/0227131c0a564eee932724509c6d85af.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d6674461eaaf42feb1c57021f3e72f13.png" alt="在这里插入图片描述"> -  模拟局域网交换机到SW1链路down 我们通过shutdown e0/1端口的方式模拟局域网到主网关252的链路down，可以发现vrrp随之发送了切换。再次通过PC终端模拟trace路径，发现路由走的253交换机，这就是VRRP的用途，冗余网关路由协议，主网关交换机故障的时候自动切换到了备网关，不需要我们人工手动进行切换。 <img src="https://img-blog.csdnimg.cn/7275a5cf0ed7473691f5657b04ad7d80.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6a1272901d8049989202d1364dd858a4.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5ea1f06aa411428495b9982d5f45d39a.png" alt="在这里插入图片描述"> -  模拟链路恢复 开启端口模拟链路恢复，可以看到252交换机主动抢占主，重新成为网关交换机。 <img src="https://img-blog.csdnimg.cn/39f3a30e49324d9cb62b45e4d499fa06.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5163c9a6e46d406b8560d547b6fd8584.png" alt="在这里插入图片描述"> 
## 三、实验总结
- VRRP优先级值越大越优先，默认100- VRRP抢占模式下，主网关交换机恢复会自动抢占为主，默认抢占模式- VRRP协议需要二层链路承载- 上下行链路均为VRRP协议需要配置track进行联动