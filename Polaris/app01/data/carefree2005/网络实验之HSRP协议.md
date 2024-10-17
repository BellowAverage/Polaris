
--- 
title:  网络实验之HSRP协议 
tags: []
categories: [] 

---
## 一、HSRP协议简介

  HSRP：热备份路由器协议（HSRP：Hot Standby Router Protocol），是cisco平台一种特有的技术，是cisco的私有协议。该协议中含有多台路由器，对应一个HSRP组。该组中只有一个路由器承担转发用户流量的职责，这就是活动路由器。当活动路由器失效后，备份路由器将承担该职责，成为新的活动路由器。这就是热备份的原理。实现HSRP的条件是系统中有多台路由器，它们组成一个“热备份组”，这个组形成一个虚拟路由器。在任一时刻，一个组内只有一个路由器是活动的，并由它来转发数据包，如果活动路由器发生了故障，将选择一个备份路由器来替代活动路由器，但是在本网络内的主机看来，虚拟路由器没有改变。所以主机仍然保持连接，没有受到故障的影响，这样就较好地解决了路由器切换的问题。

## 二、HSRP协议实践

### 1、实验环境说明

  博文实验环境采用GNS3模拟器搭建VRRP网络实验环境，路由器使用c7200，iso系统版本为c7200-advipservicesk9-mz.124-20.T.bin；交换机使用c3600，iso系统版本为c3640-jk9o3s-mz.124-10a.bin。

### 2、拓扑图

  HSRP是思科常用的协议，在局域网网关上的冗余配置必不可少，也常用于链路上联的冗余互联配置。HSRP是冗余网关协议，顾名思义是运行在三层接口上的，但是也需要二层链路承载。HSRP既可以运行在三层接口上，也可以运行在VLAN接口上，博文实验环境如下图。上层链路接口HSRP运行在路由器的三层接口F0/0，下层互联接口配置在vlan接口上，互联地址段使用的是10.10.10.0/29。 <img src="https://img-blog.csdnimg.cn/256d5fe059414331b2d398590fcea916.png" alt="在这里插入图片描述">

### 3、网络配置文件

  R1路由器如下：

```
SW1#vlan database 
SW1(vlan)#vlan 10 
VLAN 10 added:
    Name: VLAN0010
SW1(vlan)#exit
APPLY completed.
Exiting....
SW1#conf t
SW1(config)#int range f1/0 -1
SW1(config-if-range)#sw mode acc
SW1(config-if-range)#sw acc vlan 10
SW1(config-if-range)#no shut
SW1(config-if-range)#end
SW1(config)#int vlan 10
SW1(config-if)#ip add 10.10.10.1 255.255.255.248
SW1(config-if)#standby 10 ip 10.10.10.3 
SW1(config-if)#standby priority 200
SW1(config-if)#standby preempt
SW1(config-if)#end
SW1# wr mem

```

  R2路由器如下：

```
SW2#vlan database  
SW2(vlan)#vlan 10
VLAN 10 added:
    Name: VLAN0010
SW2(vlan)#exit
APPLY completed.
Exiting....
SW2#conf t
SW2(config)#int range f1/0
SW2(config-if-range)#int range f1/0 -1
SW2(config-if-range)#sw mode acc
SW2(config-if-range)#sw acc vlan 10
SW2(config-if-range)#no shut
SW2(config-if-range)#exit
SW2(config)#int vlan 10
SW2(config-if)#ip add 10.10.10.2 255.255.255.248
SW2(config-if)#standby 10 ip 10.10.10.3         
SW2(config-if)#standby priority 150
SW2(config-if)#standby preempt 
SW2(config-if)#end

```

  SW1路由器如下：

```
R1#conf t
R1(config)#int f0/0
R1(config-if)#ip address 10.10.10.5 255.255.255.248
R1(config-if)#standby 20 ip 10.10.10.4
R1(config-if)#standby 20 priority 200
R1(config-if)#standby 20 preempt
R1(config-if)#no shut
R1(config-if)#end
R1#wr mem

```

  SW2路由器如下：

```
R2#conf t
R2(config)#int f0/0
R2(config-if)#ip address 10.10.10.6 255.255.255.248
R2(config-if)#standby 20 ip 10.10.10.4
R2(config-if)#standby 20 priority 150
R2(config-if)#standby 20 preempt
R2(config-if)#no shut
R2(config-if)#end
R2#wr mem

```

### 4、协议实践测试
- 查验HSRP运行状态，可以看到HSRP状态的主备及虚拟IP地址。
>  
 R1#show standby bri P indicates configured to preempt. | Interface Grp Pri P State Active Standby Virtual IP Fa0/0 20 200 P Active local 10.10.10.6 10.10.10.4 <img src="https://img-blog.csdnimg.cn/27e451376ac94733bc27bc8d491c9eb2.png" alt="在这里插入图片描述"> 

- 中断R1和SW1互联链路，然后从SW1和SW2交换机ping互联链路虚拟IP地址10.10.10.4。通过查看mac地址表
>  
 #在R1上关闭F0/0接口模拟链路中断，可以看到HSRP快速发送了状态切换 R1(config-if)#shut R1(config-if)# *Jan 4 20:40:52.539: %HSRP-5-STATECHANGE: FastEthernet0/0 Grp 20 state Active -&gt; Init R1(config-if)# *Jan 4 20:40:54.551: %LINK-5-CHANGED: Interface FastEthernet0/0, changed state to administratively down R1(config-if)# *Jan 4 20:40:54.551: %ENTITY_ALARM-6-INFO: ASSERT INFO Fa0/0 Physical Port Administrative State Down *Jan 4 20:40:55.551: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to down #在R2上可以看到HSRP状态快速发生了切换，由备切换未了主 R2# *Jan 4 20:40:52.615: %HSRP-5-STATECHANGE: FastEthernet0/0 Grp 20 state Standby -&gt; Active #通过在SW1上查看arp表可以知道虚拟IP地址10.10.10.4的mac地址是0000.0c07.ac14 SW1#show arp Protocol Address Age (min) Hardware Addr Type Interface Internet 10.10.10.1 - cc01.45cc.0000 ARPA Vlan10 Internet 10.10.10.4 2 0000.0c07.ac14 ARPA Vlan10 <img src="https://img-blog.csdnimg.cn/d11cce24dd76404b902d88ae3dc00b4c.png" alt="在这里插入图片描述"> 


## 三、总结
- HSRP是一种网关冗余协议，它通过在冗余网关之间共享协议和MAC，提供不间断的IP路径冗余。- HSRP在2个或多个路由器间创建虚拟MAC和虚拟IP，其实就是将多台物理的路由器组合成一台虚拟路由器。- HSRP的hello包包含priority(默认100)，hello间隔（默认3S），holdtime(默认10S)。- HSRP的hello包发向组播地址224.0.0.2(所有路由器)。- HSRP路由器的默认优先级是100， 优先级相同的情况下比较IP地址，越大越优。- HSRP存在六种状态： 1、Initial （刚启用HSRP时的初始状态） 2、learn (没有收到hello包，没有虚拟ip地址,等待收到hello包) 3、listen（收到hello包，有了虚拟ip地址,除了active和standby，其它路由器都是这个状态） 4、speak (检测到没有standby,周期发送hello包，开始选active和standby router) 5、Standby （没选到active的，除了active外优先级最高的router，会继续发hello包，只有一个） 6、active （选到的转发的router，会继续发hello包，只有一个）