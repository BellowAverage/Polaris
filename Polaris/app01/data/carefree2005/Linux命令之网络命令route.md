
--- 
title:  Linux命令之网络命令route 
tags: []
categories: [] 

---
## 一、route命令简介

  route命令是Linux系统中的一个网络管理工具，用于显示和操作IP路由表。它可以用来查看当前系统的路由表信息，添加、删除或修改路由表项，以及显示路由表中的详细信息。route命令可以帮助用户诊断和解决网络连接问题，以及进行网络规划和优化。

## 二、route命令使用示例

### 1、查看命令版本

  route命令也属于net-tools工具集中的命令，如果linux系统没有此命令，我们可以通过安装net-tools软件包来安装此命令。

>  
 [root@s152 ~]# route --version net-tools 2.10-alpha +NEW_ADDRT +RTF_IRTT +RTF_REJECT +I18N +SELINUX AF: (inet) +UNIX +INET +INET6 +IPX +AX25 +NETROM +X25 +ATALK +ECONET +ROSE -BLUETOOTH HW: +ETHER +ARC +SLIP +PPP +TUNNEL -TR +AX25 +NETROM +X25 +FR +ROSE +ASH +SIT +FDDI +HIPPI +HDLC/LAPB +EUI64 


### 2、获取命令帮助

  通过–help或者-h参数可以获取命令帮助，route命令可以查看或者更新、修改、删除系统路由表。 <img src="https://img-blog.csdnimg.cn/835ef88524ae4764bd8ecaf499108a78.png" alt="在这里插入图片描述">

### 3、查看操作系统路由

  使用-n参数查看路由明细，当然不用参数也可以查看，-n表示不解析主机名。

>  
 [root@s152 ~]# route -n Kernel IP routing table Destination Gateway Genmask Flags Metric Ref Use Iface 0.0.0.0 192.168.0.1 0.0.0.0 UG 100 0 0 eth0 192.168.0.0 0.0.0.0 255.255.255.0 U 100 0 0 eth0 


### 4、添加一段路由

  使用add参数添加路由，可以添加一个网段也可以添加一个主机路由。

>  
 [root@s152 ~]# route add -net 192.168.122.0/24 gw 192.168.0.166 [root@s152 ~]# route -n Kernel IP routing table Destination Gateway Genmask Flags Metric Ref Use Iface 0.0.0.0 192.168.0.1 0.0.0.0 UG 100 0 0 eth0 192.168.0.0 0.0.0.0 255.255.255.0 U 100 0 0 eth0 192.168.122.0 192.168.0.166 255.255.255.0 UG 0 0 0 eth0 


### 5、删除一段路由

  使用del参数删除一段或者一个主机路由。

>  
 [root@s152 ~]# route del -net 192.168.122.0/24 [root@s152 ~]# route -n Kernel IP routing table Destination Gateway Genmask Flags Metric Ref Use Iface 0.0.0.0 192.168.0.1 0.0.0.0 UG 100 0 0 eth0 192.168.0.0 0.0.0.0 255.255.255.0 U 100 0 0 eth0 


### 5、添加一个主机路由

>  
 [root@s152 ~]# route add -host 192.168.122.1 gw 192.168.0.166 [root@s152 ~]# route -n Kernel IP routing table Destination Gateway Genmask Flags Metric Ref Use Iface 0.0.0.0 192.168.0.1 0.0.0.0 UG 100 0 0 eth0 192.168.0.0 0.0.0.0 255.255.255.0 U 100 0 0 eth0 192.168.122.1 192.168.0.166 255.255.255.255 UGH 0 0 0 eth0 [root@s152 ~]# ping 192.168.122.1 PING 192.168.122.1 (192.168.122.1) 56(84) bytes of data. 64 bytes from 192.168.122.1: icmp_seq=1 ttl=64 time=0.795 ms … 


### 6、添加一条禁止访问路由

  使用reject参数表示拒绝路由，用于访问安全控制，禁止主机访问明确不安全或者无权访问的主机。添加后查看路由表，状态为叹号，表示禁止访问，优先普通路由策略。 <img src="https://img-blog.csdnimg.cn/46e2a4be2c174893aa47c207434474df.png" alt="在这里插入图片描述">

### 7、删除默认路由

  使用del default gw删除默认网关。

>  
 [root@s166 ~]# route del default gw 192.168.0.1 [root@s166 ~]# route -n Kernel IP routing table Destination Gateway Genmask Flags Metric Ref Use Iface 192.168.0.0 0.0.0.0 255.255.255.0 U 100 0 0 eth0 192.168.122.0 0.0.0.0 255.255.255.0 U 0 0 0 virbr0 


### 8、添加默认路由

  使用add default gw添加默认网关。

>  
 [root@s166 ~]# route -n Kernel IP routing table Destination Gateway Genmask Flags Metric Ref Use Iface 192.168.0.0 0.0.0.0 255.255.255.0 U 100 0 0 eth0 192.168.122.0 0.0.0.0 255.255.255.0 U 0 0 0 virbr0 [root@s166 ~]# route add default gw 192.168.0.1 [root@s166 ~]# route -n Kernel IP routing table Destination Gateway Genmask Flags Metric Ref Use Iface 0.0.0.0 192.168.0.1 0.0.0.0 UG 0 0 0 eth0 192.168.0.0 0.0.0.0 255.255.255.0 U 100 0 0 eth0 192.168.122.0 0.0.0.0 255.255.255.0 U 0 0 0 virbr0 


## 三、route命令使用语法及参数说明

### 1、使用语法

查看路由用法：#route [-nNvee] [-FC] [] 更新路由用法：#route [-v] [-FC] {add|del|flush} …

### 2、参数说明

<th align="left">参数选项</th><th align="left">参数说明</th>
|------
<td align="left">-n</td><td align="left">直接使用 IP 地址，不进行 DNS 解析主机</td>
<td align="left">-ee</td><td align="left">显示更详细的路由信息</td>
<td align="left">add</td><td align="left">添加路由信息</td>
<td align="left">del</td><td align="left">删除路由信息</td>
<td align="left">target</td><td align="left">指定目标网络或主机。可以用 IP 地址或主机/网络名</td>
<td align="left">-net</td><td align="left">到一个网络的路由，后面接的是一个网络号地址</td>
<td align="left">-host</td><td align="left">到一个主机的路由，后面接的是一个主机地址</td>
<td align="left">netmask NM</td><td align="left">为添加的路由指定网络掩码，NM表示掩码地址，如255.255.255.0</td>
<td align="left">gw GW</td><td align="left">为发往目标网络/主机的任何分组指定网关</td>
<td align="left">dev lf</td><td align="left">指定由哪个网络设备出去，后面接网络设备名，如 etho 等</td>

### 3、Flags路由标记信息

<th align="left">Flags标记</th><th align="left">标记说明</th>
|------
<td align="left">U(route is up)</td><td align="left">表示此路由当前为启动状态</td>
<td align="left">H(target is a host)</td><td align="left">目标路由是一个主机(IP)而非网络</td>
<td align="left">R(reinstate route for dynamic routing):</td><td align="left">使用动态路由时，恢复路由信息标识</td>
<td align="left">G(use gateway)</td><td align="left">表示需要通过外部的主机(gateway)来转接传递数据</td>
<td align="left">M(modified from routing daemon or redirect)</td><td align="left">表示路由已经被修改了</td>
<td align="left">D(dynamically installed by daemon or redirect)</td><td align="left">已经服务设定为动态路由</td>
<td align="left">!(reject route )</td><td align="left">这个路由将不会被接受( 用来抵挡不安全的网络)</td>

## 四、静态路由永久配置方式

  我们使用route命令配置的路由都是临时生效，在网卡重启或者系统重启后配置失效，如果我们需要配置永久静态路由可以使用如下几种方式。
- 方式一：
>  
 vi /etc/sysconfig/network-scripts/route-eth0 #&lt;==默认不存在此文件 加入如下内容 192.168.1.0/24 via 10.0.0.254 

- 方式二：
>  
 vi /etc/sysconfig/static-routes #&lt;==默认不存在此文件 加入如下内容 any net 192.168.1.0/24 gw 10.0.0.254 

- 方式三：
>  
 vi /etc/rc.local 加入如下内容 route add -net 192.168.1.0/24 gw 10.0.0.254 

