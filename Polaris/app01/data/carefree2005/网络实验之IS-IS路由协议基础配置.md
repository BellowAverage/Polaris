
--- 
title:  网络实验之IS-IS路由协议基础配置 
tags: []
categories: [] 

---
## 一、IS-IS路由协议简介

  IS-IS（Intermediate System-to-Intermediate System，中间系统到中间系统）路由协议最初是ISO（the International Organization for Standardization，国际标准化组织）为CLNP（Connection Less Network Protocol，无连接网络协议）设计的一种动态路由协议。运行IS-IS协议的网络包含了终端系统（End System）、中间系统（Intermediate System）、区域（Area）和路由域（Routing Domain）。一个路由器是Intermediate System（IS），一个主机就是End System（ES）。主机和路由器之间运行的协议称为ES-IS，路由器与路由器之间运行的协议称为IS-IS。区域是路由域的细分单元，IS-IS允许将整个路由域分为多个区域，IS-IS就是用来提供路由域内或一个区域内的路由。IS-IS与OSPF路由协议不同，OSPF是按照链路划分区域，IS-IS是按照路由器划分区域，一个路由器可以是level-1，level-1-2，level-2三种角色之一。IS-IS支持的路由条目更多，常用于城域网。

## 二、IS-IS路由协议配置实践

### 1、实验环境说明

  博文实验环境采用GNS3模拟器搭建IS-IS网络实验环境，路由器使用c7200，iso系统版本为c7200-advipservicesk9-mz.124-20.T.bin。

### 2、拓扑图

  如下拓扑图我们使用4台路由器完成IS-IS路由协议模拟实验，路由器R1和R2模拟核心区域路由器，区域编号49.01；路由器R3、R4模拟普通区域，区域编号分别为49.02和49.03。 <img src="https://img-blog.csdnimg.cn/824e95147d6e43a1804396a2e9f6a470.png" alt="在这里插入图片描述">

### 3、网络配置

  R1路由器配置如下：

```
R1#conf t
R1(config)#int g1/0
R1(config-if)#ip add 12.12.12.1 255.255.255.0
R1(config-if)#ip router isis
R1(config-if)#no shut
R1(config-if)#int f0/0
R1(config-if)#ip add 13.13.13.1 255.255.255.0
R1(config-if)#ip router isis        
R1(config-if)#no shut
R1(config-if)#exit
R1(config)#router isis
R1(config-router)#net 49.02.ca01.2424.001c.00
R1(config-router)#net 49.01.ca01.2424.001c.00
R1(config-router)#is-type level-1-2
R1(config-router)#log-adjacency-changes
R1(config-router)#end
R1#wr mem

```

  R2路由器配置如下：

```
R2#conf t
R2(config)#int g1/0
R2(config-if)#ip add 12.12.12.2 255.255.255.0
R2(config-if)#ip router isis
R2(config-if)#no shut
R2(config-if)#int f0/0
R2(config-if)#ip add 24.24.24.2 255.255.255.0
R2(config-if)#ip router isis        
R2(config-if)#no shut
R2(config-if)#exit
R2(config)#router isis
R2(config-router)#net 49.01.ca02.1fa0.001c.00
R2(config-router)#net 49.03.ca02.1fa0.001c.00
R2(config-router)#is-type level-1-2
R2(config-router)#log-adjacency-changes
R2(config-router)#end
R2#wr mem

```

  R3路由器配置如下：

```
R3#conf t
R3(config-if)#int f0/0
R3(config-if)#ip add 13.13.13.3 255.255.255.0
R3(config-if)#ip router isis        
R3(config-if)#no shut
R3(config-if)#exit
R3(config)#router isis
R3(config-router)#net 49.02.ca03.3e08.0008.00
R3(config-router)#is-type level-1
R3(config-router)#log-adjacency-changes
R3(config-router)#end
R3#wr mem

```

  R4路由器配置如下：

```
R4#conf t
R4(config-if)#int f0/0
R4(config-if)#ip add 24.24.24.4 255.255.255.0
R4(config-if)#ip router isis        
R4(config-if)#no shut
R4(config-if)#exit
R4(config)#router isis
R4(config-router)#net 49.02.ca04.27c8.0008.00
R4(config-router)#is-type level-1
R4(config-router)#log-adjacency-changes
R3(config-router)#end
R3#wr mem

```

### 4、协议验证测试
- IS-IS邻居验证，我们可以看到存在clns和IP两种邻居。
>  
 R1#show clns nei R1#show clns is-neighbors R1#show isis nei <img src="https://img-blog.csdnimg.cn/d96d09f0f206464482bab72d52a2b421.png" alt="在这里插入图片描述"> 

- IS-IS路由验证，查看管理距离值。IS-IS邻居建立成功后，互联路由就自动完成了路由宣告。 <img src="https://img-blog.csdnimg.cn/78452b32d2bb4b868fd7f8d9f754c7d6.png" alt="在这里插入图片描述">- 直连路由重发布
>  
 在R3和R4上创建loopback地址并重发布到ISIS中 #R3 R3(config)#int loop 0 R3(config-if)#ip add 3.3.3.3 255.255.255.255 R3(config-if)#router isis R3(config-router)#redistribute connected level-1 #R4 R4(config)#int loop 0 R4(config-if)#ip add 4.4.4.4 255.255.255.255 R4(config-if)#router isis R4(config-router)#redistribute connected level-1 #查看路由 <img src="https://img-blog.csdnimg.cn/b103e7fae6b04895a393a4fd4a7b2a4e.png" alt="在这里插入图片描述"> 

- 默认路由验证，level-1-2路由器默认会向level-1路由发布默认路由
>  
 #R1上创建loop0口 R1(config)#int loop 0 R1(config-if)#ip add 1.1.1.1 255.255.255.255 #R4上查看路由 <img src="https://img-blog.csdnimg.cn/1cd7a2b593614797854d085c772eee09.png" alt="在这里插入图片描述"> #R4上虽然没有1.1.1.1的明细路由，但是可以ping通1.1.1.1 <img src="https://img-blog.csdnimg.cn/47254d866da44511b6611d9ee84a6980.png" alt="在这里插入图片描述"> 


## 三、IS-IS知识点总结
- IS-IS除了IP路由，还需要CLNS地址；- IS-IS采用了分层结构，L1表示普通区域，L2表示骨干核心区域，L2区域只可以有一个；- IS-IS路由协议中，路由器有三种角色level-1，level-2-only，level1-1-2，思科路由器默认是level-1-2；- CLNS地址标识的是整个节点，包括区域+设备ID+进程三部分组成，可变长都8-20字节；- IS-IS工作在3层，其协议报文直接封装在数据链路层的帧结构中，跟IP无关；- IS-IS路由协议管理距离值115；- 一台ISIS路由器默认最多属于3个区域，通过max-area-addresses命令修改，可以设置为3-254。
## 四、CLNS地址说明
- 路由器使用的CLNS地址被称为NSAP（Network Service Access Point） NSAP＝Area + System ID + NSEL（8-20Bytes)，其中Area 1-13字节，Sytem ID 6字节，NSEL1个字节。- Area =IDP+HODSP，IDP标识机构码，HODSP标识区域。常用机构码47表示国际代码，49表示本地管理，类似于IP地址中的私有地址，所以我们模拟实验使用49机构码。- System ID 6字节，相当于OSPF中的router-id，一般用直接用mac地址作为system ID。- NSEL 1字节，标识设备中的进程，当NSEL＝00时，被称为NET（Network Entity Title）。