
--- 
title:  网络实验之EtherChannel技术实践 
tags: []
categories: [] 

---
## 一、EtherChannel简介

  EtherChannel简单来说就是将多个物理端口绑定为一个逻辑端口，通过多个端口绑定，能充分利用现有端口来增加带宽。构成etherchannel的端口必须配置成相同的特性，如双工模式、速度、同为FE或GE端口、native VLAN,、VLAN range,、and trunking status and type.等当etherchannel中某一条link failed时，etherchannel中其它link照常工作。思科交换机最多允许绑定8个端口，EtherChannel端口既可以是二层端口，也可以捆绑为三层端口。二层EtherChannel一般用于VRRP冗余网关交换机之间的互联，三层EtherChannel一般用于核心、汇聚交换机之间的互联。

## 二、EtherChannel协议实践

### 1、实验环境说明

  博文实验环境采用GNS3模拟器搭建VTP网络实验环境，三层交换机使用3640，iso系统版本为c3640-jk9o3s-mz.124-10a.bin。

### 2、拓扑图

  EtherChannel技术常用于VRRP冗余网关交换机直接的互联或者汇聚、核心交换机之间的互联，主要作用是链路冗余。如下图所示，我们将SW1的f1/0、f1/1捆绑为一个EtherChannel，EtherChannel的主要用于VRRP网关交换机之间的互联，确保主备切换正常，不出现双主的情况。 <img src="https://img-blog.csdnimg.cn/6d1a49598c6c41db81195440869af63c.png" alt="在这里插入图片描述">

### 3、网络配置
- SW1交换机配置
```
SW1#vlan database 
SW1(vlan)#vlan 100
VLAN 100 added:
    Name: VLAN0100
SW1(vlan)#exi
APPLY completed.
Exiting....
SW1(config-if)#int range f1/0 -1
SW1(config-if-range)#sw mode acc 
SW1(config-if-range)#sw acc vlan 100
SW1(config-if-range)#channel-group 1 mode on
SW1(config-if)#int range f1/14 -15
SW1(config-if-range)#sw mode acc 
SW1(config-if-range)#sw acc vlan 100
SW1(config-if-range)#channel-group 2 mode on
SW1(config)#int port-channel 1
SW1(config-if)#sw mode acc
SW1(config-if)#sw acc vlan 100
SW1(config-if)#no shut
SW1(config)#int port-channel 2
SW1(config-if)#sw mode acc
SW1(config-if)#sw acc vlan 100
SW1(config-if)#no shut
SW1(config-if)#ip add 192.168.0.252 255.255.255.0
SW1(config-if)#vrrp 100 ip 192.168.0.254
SW1(config-if)#vrrp 100 priority 200
SW1(config-if)#vrrp 100 preempt
SW1(config-if)#no shut
SW1(config-if)#end
SW1#wr me

```
- SW2交换机配置
```
SW2#vlan database 
SW2(vlan)#vlan 100
VLAN 100 added:
    Name: VLAN0100
SW2(vlan)#exi
APPLY completed.
Exiting....
SW2(config-if)#int range f1/0 -1
SW2(config-if-range)#sw mode acc 
SW2(config-if-range)#sw acc vlan 100
Creating a port-channel interface Port-channel1 
SW2(config-if)#int range f1/14 -15
SW2(config-if-range)#sw mode acc 
SW2(config-if-range)#sw acc vlan 100
SW2(config-if-range)#channel-group 2 mode on
SW2(config-if-range)#int port-ch 1
SW2(config-if)#sw mode acc
SW2(config-if)#sw acc vlan 100
SW2(config-if)#no shut     
SW2(config-if-range)#int port-ch 2
SW2(config-if)#sw mode acc
SW2(config-if)#sw acc vlan 100
SW2(config-if)#no shut     
SW2(config-if)#int vlan 100
SW2(config-if)#ip add 192.168.0.253 255.255.255.0
SW2(config-if)#vrrp 100 ip 192.168.0.254
SW2(config-if)#vrrp 100 priority 150
SW2(config-if)#vrrp 100 preempt 
SW2(config-if)#no shut
SW2(config-if)#end
SW2#wr mem

```
- sw3交换机配置
```
sw3#vlan database 
sw3(vlan)#vlan 100
VLAN 100 added:
    Name: VLAN0100
sw3(vlan)#exi
APPLY completed.
Exiting....
sw3(config)#int range f1/0 -3
sw3(config-if-range)#sw mode acc
sw3(config-if-range)#sw acc vlan 100
sw3(config-if-range)#int range f1/0 -1
sw3(config-if-range)#channel-group 1 mode on
sw3(config-if-range)#int range f1/2 -3
sw3(config-if-range)#channel-group 2 mode on
sw3(config-if-range)#int port-c 1
sw3(config-if)#sw mode acc
sw3(config-if)#sw acc vlan 100
sw3(config-if)#int port-c 2
sw3(config-if)#sw mode acc
sw3(config-if)#sw acc vlan 100
sw3(config)#int f1/15
sw3(config-if)#sw mode acc
sw3(config-if)#sw acc vlan 100
sw3(config-if)#no shut
sw3(config-if-range)#end
Building configuration...
sw3#wr
[OK]

```

### 4、协议实践验证
- 检查etherchannel状态 <img src="https://img-blog.csdnimg.cn/e23006d90d1449fda66fe90ba4f9626d.png" alt="在这里插入图片描述">- 验证网络的通断性 <img src="https://img-blog.csdnimg.cn/ad92ddad1cc0494d879adf205f542552.png" alt="在这里插入图片描述">- 查看VRRP状态 <img src="https://img-blog.csdnimg.cn/1f36a8284ffb482db5f3a31eea922cb6.png" alt="在这里插入图片描述">- shutdown关闭F1/0和F1/15端口并检查通断性 <img src="https://img-blog.csdnimg.cn/1b97128d1d2145beb004869d75a6b498.png" alt="在这里插入图片描述">- 三层etherchannel测试
>  
 博主原本想继续验证展示三层etherchannel配置和效果的，经配置发现此iso及配置的模块下的端口不支持三层etherchannel配置，只好作罢。实际上配置是类似的，甚至还简单一点，我们只需要将三层端口加入etherchannel组，然后再port-channel上配置IP地址即可。 


## 三、总结
- 绑定后的端口默认继承原来物理接口的配置模式。- etherchannel不支持10M端口的绑定。- cisco的交换机不仅可以支持第二层etherchannel,还可以支持第三层etherchannel。- 一个etherchannel内所有的端口都必须具有相同的速率和双工模式。LACP只能是全双工。- 二层接口不能配置IP地址，不能宣告进路由协议，只能对二层以太网帧进行转发。- 三层接口可以配置IP地址，可运行路由协议，能接收IP包并且转发。- 使用port-channel load-balance配置etherchannel负载均衡模式，默认基于源地址；可以配置的方式有基于源MAC、源IP、目的MAC、目的IP、源和目的IP、源和目的MAC。
>  
 SW1(config)#port-channel load-balance ? dst-ip Dst IP Addr dst-mac Dst Mac Addr src-dst-ip Src XOR Dst IP Addr src-dst-mac Src XOR Dst Mac Addr src-ip Src IP Addr src-mac Src Mac Addr 

- 查看etherchannel负载均衡模式使用命令show etherchannel load-balance。
>  
 SW1#show etherchannel load-balance 

- 修复端口进入err-disable状态的方法
>  
 手动方法：shutdown端口后再no shutdown 自动方法： SW1(config)#errdisable recovery cause ? all Enable timer to recover from all causes bpduguard Enable timer to recover from bpdu-guard error disable state dtp-flap Enable timer to recover from dtp-flap error disable state link-flap Enable timer to recover from link-flap error disable state pagp-flap Enable timer to recover from pagp-flap error disable state rootguard Enable timer to recover from root-guard error disable state udld Enable timer to recover from udld error disable state SW1(config)#errdisable recovery cause all SW1(config)#errdisable recovery interval 30 

