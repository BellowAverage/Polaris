
--- 
title:  VirtualBox 部署 KVM 虚拟化 
tags: []
categories: [] 

---
### 什么是KVM技术？

>  
 **KVM（Kernel-based Virtual Machine）是一种开源的虚拟化技术，它是Linux内核的一部分。KVM通过将Linux内核转换为Hypervisor，允许在同一物理主机上运行多个虚拟机实例，每个实例可以独享一部分系统资源。 KVM的工作原理是将Linux内核扩展为虚拟化管理程序，它直接在硬件上运行，并提供了虚拟化所需的核心功能。KVM利用CPU的虚拟化扩展（如Intel的VT-x和AMD的AMD-V）来创建和管理虚拟机。虚拟机通过QEMU（Quick EMUlator）进行模拟，并提供实际运行的硬件和设备，使操作系统和应用程序能够在虚拟机中运行。 ** 
  
 **KVM的主要特点包括： ** 
 **1. 性能：KVM直接在物理主机的硬件上运行，与传统的基于模拟的虚拟化方式相比，可以获得更好的性能。虚拟机可以直接访问物理主机上的硬件资源，并使用硬件辅助虚拟化技术提高性能。** 
  
 **2. 安全性：KVM利用硬件辅助虚拟化技术，并通过Linux内核的安全功能来保护虚拟机之间的隔离。虚拟机之间无法相互访问，从而增加了安全性。** 
  
 **3. 灵活性：KVM可以运行多种操作系统，包括Linux、Windows和其他主流操作系统。它提供了丰富的管理工具和API，使用户可以方便地创建、配置和管理虚拟机。** 
  
 **4. 可扩展性：KVM支持多个虚拟CPU和大量的内存，可以满足不同应用的需求。它还支持虚拟机的迁移和复制，可以在不同的物理主机之间平衡负载和提高可用性。 总之，KVM是一种强大而灵活的虚拟化技术，它结合了Linux内核的强大功能和虚拟化的优势，为用户提供了高性能、安全性和灵活性的虚拟化解决方案。 ** 


>  
 **首先要使用virtualbox部署KVM，首先需要开启cpu等硬件的虚拟化，** 
 **需要达到如图效果：** 


<img alt="" height="498" src="https://img-blog.csdnimg.cn/4c497390c64e4fafad70e4c9b834928a.png" width="729">

### 查看cpu是否支持虚拟化 

>  
 ** 查看CPU是否可以虚拟化：出现vmx或svm其一即说明CPU支持虚拟化。** 


<img alt="" height="533" src="https://img-blog.csdnimg.cn/5062743f73f54146a6045eff57a3d177.png" width="936">

###  进行操作之前关闭防火墙，selinux

```
[root@kvm yum.repos.d]# systemctl stop firewalld
[root@kvm yum.repos.d]# systemctl disable firewalld
Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
[root@kvm yum.repos.d]# setenforce 0
[root@kvm yum.repos.d]# vim /etc/selinux/config 
SELINUX=disabled
```

### 安装KVM软件依赖包：

```
yum install qemu-kvm libvirt virt-install bridge-utils -y

```

>  
 **查看KVM模块是否安装：** 


```
[root@kvm system]# lsmod | grep kvm
kvm_intel             188740  0 
kvm                   637289  1 kvm_intel
irqbypass              13503  1 kvm

```

>  
 **查看虚拟化管理工具libvirtd服务是否启动** 


```
[root@kvm system]# systemctl status libvirtd
● libvirtd.service - Virtualization daemon
   Loaded: loaded (/usr/lib/systemd/system/libvirtd.service; enabled; vendor preset: enabled)
   Active: active (running) since 三 2023-06-28 16:04:31 CST; 30min ago
     Docs: man:libvirtd(8)
           https://libvirt.org
 Main PID: 2235 (libvirtd)
    Tasks: 19 (limit: 32768)
   CGroup: /system.slice/libvirtd.service
           ├─2235 /usr/sbin/libvirtd
           ├─2351 /usr/sbin/dnsmasq --conf-file=/var/lib/libvirt/dnsmasq/default.conf --l...
           └─2352 /usr/sbin/dnsmasq --conf-file=/var/lib/libvirt/dnsmasq/default.conf --l...

6月 28 16:11:42 kvm dnsmasq[2351]: using nameserver 114.114.114.114#53
6月 28 16:11:42 kvm dnsmasq[2351]: using nameserver 2400:3200::1#53
6月 28 16:13:45 kvm dnsmasq[2351]: reading /etc/resolv.conf
6月 28 16:13:45 kvm dnsmasq[2351]: using nameserver 2400:3200::1#53
6月 28 16:13:45 kvm dnsmasq[2351]: no servers found in /etc/resolv.conf, will retry
6月 28 16:13:45 kvm dnsmasq[2351]: reading /etc/resolv.conf
6月 28 16:13:45 kvm dnsmasq[2351]: using nameserver 114.114.114.114#53
6月 28 16:13:48 kvm dnsmasq[2351]: reading /etc/resolv.conf
6月 28 16:13:48 kvm dnsmasq[2351]: using nameserver 114.114.114.114#53
6月 28 16:13:48 kvm dnsmasq[2351]: using nameserver 2400:3200::1#53
[root@kvm system]# 

```

### 设置KVM网络

>  
 **首先在目前正常使用的网卡配置文件里面配置如下：** 


>  
 **KVM网络的两种模式：** 
 **① NAT： 默认设置，数据包由 NAT 方式通过主机的接口进行传送，可以访问外网，但是无法从外部访问虚拟机网络 ② 网桥：这种模式允许虚拟机像一台独立的主机一样拥有网络，外部的机器可以直接访问到虚拟机内部，但需要网卡支持(一般有线网卡都支持)** 


```
[root@kvm network-scripts]# cat ifcfg-enp0s3 
TYPE="Ethernet"
BOOTPROTO="static"
NAME="enp0s3"
UUID="3bdb5b05-6bd2-401c-93f5-bae94e5c1cd5"
DEVICE="enp0s3"
ONBOOT="yes"
#IPADDR=192.168.126.100
#GATEWAY=192.168.126.1
#PREFIX=24
#DNS1=114.114.114.114
BRIDGE=br0

```

>  
 **设置br0网卡：** 


```
[root@kvm network-scripts]# cat ifcfg-br0 
TYPE=Bridge
BOOTPROTO=static
DEFROUTE=yes
PEERDNS=yes
PEERROUTES=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_PEERDNS=yes
IPV6_PEERROUTES=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=br0
DEVICE=br0
ONBOOT=yes
IPADDR=192.168.126.100
NETMASK=255.255.255.0
GATEWAY=192.168.126.1
DNS1=114.114.114.114

```

>  
 **重启网络服务：** 


```
service network restart
```

>  
 **再次查看ip配置，发现已经多了一块br0网卡** 


```
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast master br0 state UP group default qlen 1000
    link/ether 08:00:27:dd:13:32 brd ff:ff:ff:ff:ff:ff
3: virbr0: &lt;NO-CARRIER,BROADCAST,MULTICAST,UP&gt; mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 52:54:00:42:58:b4 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
       valid_lft forever preferred_lft forever
4: virbr0-nic: &lt;BROADCAST,MULTICAST&gt; mtu 1500 qdisc pfifo_fast master virbr0 state DOWN group default qlen 1000
    link/ether 52:54:00:42:58:b4 brd ff:ff:ff:ff:ff:ff
6: br0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 08:00:27:dd:13:32 brd ff:ff:ff:ff:ff:ff
    inet 192.168.126.100/24 brd 192.168.126.255 scope global noprefixroute br0
       valid_lft forever preferred_lft forever
    inet6 2408:8640:8fe:f5:6033:8508:1cb4:4393/64 scope global noprefixroute dynamic 
       valid_lft 2592000sec preferred_lft 604800sec
    inet6 fe80::1f5a:3c2d:6054:f2d5/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever

# 测试网络

[root@kvm network-scripts]# ping www.baidu.com
PING www.a.shifen.com (112.80.248.75) 56(84) bytes of data.
64 bytes from 112.80.248.75 (112.80.248.75): icmp_seq=1 ttl=55 time=13.5 ms
64 bytes from 112.80.248.75 (112.80.248.75): icmp_seq=2 ttl=55 time=12.5 ms

```

### KVM部署与管理

>  
 **创建KVM存储与镜像的目录，上传一个centos7的镜像文件，作为创建KVM虚拟机的镜像文件** 


```
mkdir -p /data/data_kvm/iso
mkdir -p /data/data_kvm/store

```

```
[root@kvm ~]# cd /data/data_kvm/iso/
[root@kvm iso]# ls
CentOS-7-x86_64-DVD-2009.iso

```

### 命令行模式创建虚拟机

virt-install 选项含义：

>  
 --name：指定创建的虚拟机的名称。 
 --ram：指定虚拟机的内存大小。 
 --vcpu：指定虚拟机的虚拟CPU数量。 
 --disk：指定虚拟机的磁盘路径和大小。 
 --size：指定虚拟机磁盘大小，一般跟在--disk后面，用 ， 隔开。 
 --network：指定虚拟机的网络设置。 
 --cdrom：指定虚拟机的光盘路径，用于安装操作系统。 
 --graphics：指定虚拟机的图形设置，比如VNC连接等。 
 --os-variant：指定虚拟机的操作系统类型。 
 --location：指定虚拟机的操作系统安装源。 


```
virt-install --connect qemu:///system --virt-type kvm --name KVM_test --memory 512 --vcpu 1 --disk /data/data_kvm/store/KVM_test.qcow2,size=10 --location /data/data_kvm/iso/CentOS-7-x86_64-DVD-2009.iso  --network bridge=br0 --graphics none --extra-args='console=ttyS0'

```

>  
 **进入安装页面：要将[!] 变成 [X] 后才能继续安装系统。（其实就是centos的安装顺序，只是由图形界面变成了字符界面。）** 


<img alt="" height="528" src="https://img-blog.csdnimg.cn/35da56857845482a907a176f2d423ca7.png" width="850">

>  
 **输入相对应的指令来配置系统。 ** 


<img alt="" height="902" src="https://img-blog.csdnimg.cn/c705b8bb55a94e459ee446753b5af710.png" width="839">

系统安装中

<img alt="" height="529" src="https://img-blog.csdnimg.cn/291fb79e509b4eea85f378af78792fa3.png" width="917">

查看此时的系统负载情况：

<img alt="" height="294" src="https://img-blog.csdnimg.cn/449afbccca91471384e42d46e0658118.png" width="772">

```
[root@kvm ~]# virsh list
 Id    名称                         状态
----------------------------------------------------
 1     KVM_test                       running

```


