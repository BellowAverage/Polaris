
--- 
title:  计算机网络 - NAT技术 
tags: []
categories: [] 

---
**目录**





















## NAT技术

### 知识点1：什么是NAT技术

>  
 **Network Address Translation  网络地址转换** 


>  
 ** 当在专用网内部的一些主机本来已经分配到了本地IP地址（即仅在本专用网内使用的专用地址），但又想和因特网上的主机通信（并不需要加密）时，可使用NAT方法。** 
 **这种方法需要在专用网（私网IP）连接到因特网（公网IP）的路由器上安装NAT软件。装有NAT软件的路由器叫做NAT路由器，它至少有一个有效的外部全球IP地址（公网IP地址）。这样，所有使用本地地址（私网IP地址）的主机在和外界通信时，都要在NAT路由器上将其本地地址转换成全球IP地址，才能和因特网连接。** 


###  知识点2：为什么需要NAT技术？

>  
 **ipv4版本的IP地址能用的大约有 43 亿左右，分给全球每个人一个ip地址都不够，将私网ip地址经过nat转换为公有ip，公有ip也可以经过nat转换为私有ip，解决了公网ip地址不足的问题，所有的局域网使用相同的公网地址** 


###  知识点3：NAT的优点和缺点

>  
 **优点** 
 **        节省了IP地址** 
 **        保护了内网用户，内网ip经过nat转换出去修改了源ip地址，导致外网用户不知道你的内网ip是多少** 
 **缺点** 
 **        转换了很多次，导致网络延迟** 


###  知识点4：NAT技术的原理

<img alt="" height="410" src="https://img-blog.csdnimg.cn/76ecf43d79284166b58f138987da6d3b.png" width="960">

>  
 ** 示例：局域网内的pc机想访问外网的服务器** 
 **        在网络层的数据包内，源IP地址是自己的IP地址 192.168.1.2  目的IP是服务器的IP地址 203.51.23.55，那么经过NAT路由器转换以后，源IP地址就会转换为一个公网IP地址** 
 **        125.25.65.3，这个公网IP是这整个局域网内的内网用户所共享的，所有局域网内的用户的ip地址经过NAT转换以后都会变成这个公网IP，最后由这个公网ip来和服务器进行连接** 
 **        服务器收到请求以后就要响应客户机，此时在网络层面上，数据包内的源IP地址为服务器自己的IP地址203.51.23.55，目的IP为125.25.65.3，数据到达后经过NAT路由器，会根据NAT映射表来将数据转发给对应的客户机。** 


###  知识点5：NAT映射表

 <img alt="" height="138" src="https://img-blog.csdnimg.cn/0265b4f16462420f8a67a0bc67e36114.png" width="725">

>  
 ** NAT映射表记录了源ip：端口  +   转换后的ip ： 端口  目的ip：目的端口** 
 **linux的nat转换功能是linux内核完成的，所以nat映射表在内核里面** 


###  知识点6：SNAT

**Linux里面的两种NAT**

>  
 **SNAT ：局域网   -----  外网     解决了出去的问题** 
 **DNAT ： 外网    -----  局域网   解决了进来的问题** 


>  
 ** 源地址转换 Source Network Address Translation** 
 **局域网主机共享同一个公网IP地址介入Internet** 
 **修改数据包的源IP地址** 


**SNAT策略的典型应用环境 **

>  
 ** 局域网主机共享同一个公网IP地址介入Internet** 


### ** 知识点7 ： SNAT实验**

 **网络拓扑图：**

<img alt="" height="750" src="https://img-blog.csdnimg.cn/f155aa0a2dbe470b8d023cbaf8e59d8c.png" width="1200">

 

>  
 **准备一台Linux服务器** 
 **        添加两个网卡，一个ens33作WAN口（桥接模式），一个ens37（仅主机模式）作LAN口，这台服务器用作路由转发** 
 **准备一台内网服务器** 
 **        准备一个网卡，ens33，设置仅主机模式，只和内网机器通信** 


** Linux服务器网络适配器选择**

<img alt="" height="285" src="https://img-blog.csdnimg.cn/dccc58ecddd5482dab677c29356ef39e.png" width="424">

** 内网服务器网络适配器选择：**

<img alt="" height="230" src="https://img-blog.csdnimg.cn/573ac5fe8d3047169a629db3380dbe17.png" width="409">

 

** Linux服务器ip配置：**

```
[root@localhost network-scripts]# cat ifcfg-ens33
BOOTPROTO="none"
NAME="ens33"
UUID="34628a10-c85e-4ed2-8b89-5dce6dd2c903"
DEVICE="ens33"
ONBOOT="yes"
IPADDR=192.168.1.100
PREFIX=24
GATEWAY=192.168.1.1
DNS1=114.114.114.114
[root@localhost network-scripts]# cat ifcfg-ens37
BOOTPROTO="none"
NAME="ens37"
DEVICE="ens37"
ONBOOT="yes"
IPADDR=192.168.30.254
PREFIX=24
[root@localhost network-scripts]# 

```

**内网服务器ip配置：**

```
[root@localhost network-scripts]# cat ifcfg-ens33
BOOTPROTO="none"
NAME="ens33"
UUID="34628a10-c85e-4ed2-8b89-5dce6dd2c903"
DEVICE="ens33"
ONBOOT="yes"
IPADDR=192.168.30.100
PREFIX=24
GATEWAY=192.168.30.254
DNS1=114.114.114.114
```

>  
 ** 配置好了以后进行第一次测试，使用内网服务器进行测试，测试结果应该是能ping通网关和192.168.1.100，但是ping不通192.168.1.1** 


<img alt="" height="600" src="https://img-blog.csdnimg.cn/b07ade40a1864f459893d4d15c4acf98.png" width="793">

>  
 **192.168.30.100能ping通网关192.168.30.254，也能ping通WAN口192.168.1.100** 
 **因为数据到达后会查路由表，发现192.168.1.0有直连路由可以到达，于是能ping通** 
 **但是ping不通H3c路由器，因为Linux服务器默认没有开启路由转发功能，需要我们手动设置** 


>  
 ** linux机器 默认不打开路由功能     0 表示不给其他的机器转发数据包     1 表示给其他的机器转发数据包 --&gt; 路由器** 


** 临时开启路由转发功能：**

>  
 **注意：/proc/目录是放在内核中的，内核在内存中运行，重启后这些内核参数是会恢复默认值的** 


```
[root@localhost /]# cat /proc/sys/net/ipv4/ip_forward
0
[root@localhost /]# echo 1 &gt;/proc/sys/net/ipv4/ip_forward
[root@localhost /]# cat /proc/sys/net/ipv4/ip_forward
1

```

**永久开启路由转发功能：**

```
[root@localhost /]# vim /etc/sysctl.conf 
net.ipv4.ip_forward = 1

```

**配置SNAT策略**

```
# 关闭防火墙
service firewalld stop

# 清空防火墙的filter规则
iptables -t filter -F

# 清空防火墙中nat的规则
iptables -t nat -F

# 开启snat功能
iptables -t nat -A POSTROUTING -s 192.168.30.0/24 -o ens33 -j SNAT --to-source 192.168.1.100

```

查看刚才配置的规则：

```
[root@localhost ~]# iptables -t nat -L -n
Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination         

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination         
SNAT       all  --  192.168.30.0/24      0.0.0.0/0            to:192.168.1.100

```

>  
 ** 利用iptables规则来给SNAT功能传递参数** 


**示例：**

```
iptables -t nat -A POSTROUTING -s 192.168.30.0/24 -o ens33 -j SNAT --to-source 192.168.1.100

```

```
	iptables -t nat -A POSTROUTING		是防火墙策略的位置
	iptables							是一个防火墙命令
	-t nat								指定在nat表
	-A add								增加
	POSTROUTING							是nat表里的一个位置

	-s 192.168.30.0/24					指定内网的源ip地址  source
	-o ens33							指定数据出去的接口  out interface
	-j SNAT								采用SNAT策略，将ip包里的源ip地址进行修改
	--to-source 192.168.1.100			告诉防火墙修改源ip地址为192.168.1.100 --&gt; WAN口的ip地址

```

完成后测试

都能ping通了。 

<img alt="" height="506" src="https://img-blog.csdnimg.cn/6e7757454c4440598e87a133c325ba87.png" width="607">

** 在网关使用了SNAT策略后：**

<img alt="" height="430" src="https://img-blog.csdnimg.cn/8f437a5e214a46c9b5f8cde3ccb19200.png" width="850">

 

### **知识点8：DNAT**

 DNAT策略的应用环境

>  
 **目标地址转换 Destination Network Address Translation** 
 **在Internet中发布位于企业局域网内的服务器** 
 **修改数据包的目标IP地址** 


** 在网关中使用了DNAT策略发布内网服务器**

<img alt="" height="456" src="https://img-blog.csdnimg.cn/5b65e5d0817d48abbd89b47654a62e3e.png" width="809">

 

** DNAT实验脚本**

```
#开启路由功能
echo 1 &gt;/proc/sys/net/ipv4/ip_forward
#关闭防火墙
service firewalld stop
#清空防火墙里的filter表的规则
iptables -t filter -F
#清空防火墙里的nat表的规则
iptables -t nat -F

#开启snat功能
iptables -t nat  -A POSTROUTING  -s  192.168.20.0/24 -o ens33 -j SNAT --to-source 192.168.2.130

#开启dnat功能,发布web服务器
iptables -t nat -A PREROUTING  -i ens33   -d 192.168.2.130  -p tcp  --dport 80 -j DNAT --to-destination 192.168.20.100:80

#开启dnat功能,发布ssh服务器
iptables -t nat -A PREROUTING  -i ens33   -d 192.168.2.130  -p tcp  --dport 2233 -j DNAT --to-destination 192.168.20.103:22
#开启dnat功能,发布mysql服务器
iptables -t nat -A PREROUTING  -i ens33   -d 192.168.2.130  -p tcp  --dport 3306 -j DNAT --to-destination 192.168.20.103:3306

```

 
