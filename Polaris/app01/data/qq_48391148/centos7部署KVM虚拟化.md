
--- 
title:  centos7部署KVM虚拟化 
tags: []
categories: [] 

---
**目录**



































## centos7部署KVM虚拟化平台

实验环境：VMware

Linux版本：centos7

### 1、新建一台虚拟机

<img alt="" height="354" src="https://img-blog.csdnimg.cn/43d5e4f4ba634c1ea3a723738f155ea4.png" width="725">

**################################################################## **

### 2、系统内的操作

#### 1、修改主机名

```
hostnamectl set-hostname kvm
bash
```

#### 2、挂载镜像光盘

```
vim /etc/fstab
/dev/cdrom /mnt iso9660 defaults 0 0
```

>  
 **mount -a  命令会对/etc/fstab文件里的分区进行挂载，这里使用这条命令可能会报错，镜像光盘可能挂载失败** 


```
[root@kvm ~]# mount -a
mount: /dev/sr0 写保护，将以只读方式挂载
mount: 在 /dev/sr0 上找不到媒体
[root@kvm ~]# df -Th
文件系统                类型      容量  已用  可用 已用% 挂载点
devtmpfs                devtmpfs  3.8G     0  3.8G    0% /dev
tmpfs                   tmpfs     3.9G     0  3.9G    0% /dev/shm
tmpfs                   tmpfs     3.9G   12M  3.8G    1% /run
tmpfs                   tmpfs     3.9G     0  3.9G    0% /sys/fs/cgroup
/dev/mapper/centos-root xfs        48G  1.5G   47G    4% /
/dev/sda1               xfs      1014M  151M  864M   15% /boot
/dev/mapper/centos-home xfs        24G   33M   24G    1% /home
tmpfs                   tmpfs     781M     0  781M    0% /run/user/0

```

>  
 **在VMware设置里面查看设备状态是否都已经连接** 


<img alt="" height="336" src="https://img-blog.csdnimg.cn/1917ece8c5ca48abb55f6b34cb83cdb7.png" width="719">

>  
 ** 再次挂载就成功了** 


```
[root@kvm dev]# mount -a
mount: /dev/sr0 写保护，将以只读方式挂载
[root@kvm dev]# df -Th
文件系统                类型      容量  已用  可用 已用% 挂载点
devtmpfs                devtmpfs  3.8G     0  3.8G    0% /dev
tmpfs                   tmpfs     3.9G     0  3.9G    0% /dev/shm
tmpfs                   tmpfs     3.9G   12M  3.8G    1% /run
tmpfs                   tmpfs     3.9G     0  3.9G    0% /sys/fs/cgroup
/dev/mapper/centos-root xfs        48G  1.5G   47G    4% /
/dev/sda1               xfs      1014M  151M  864M   15% /boot
/dev/mapper/centos-home xfs        24G   33M   24G    1% /home
tmpfs                   tmpfs     781M     0  781M    0% /run/user/0
/dev/sr0                iso9660   4.4G  4.4G     0  100% /mnt

```

**################################################################## ** 

#### 3、ssh优化

```
vim sshd_config 
UseDNS no
```

#### 4、设置本地yum仓库

```
[root@kvm ~]# cd /etc/yum.repos.d/
[root@kvm yum.repos.d]# mkdir repo.bak
[root@kvm yum.repos.d]# ls
CentOS-Base.repo  CentOS-Debuginfo.repo  CentOS-Media.repo    CentOS-Vault.repo          repo.bak
CentOS-CR.repo    CentOS-fasttrack.repo  CentOS-Sources.repo  CentOS-x86_64-kernel.repo
[root@kvm yum.repos.d]# mv CentOS-* repo.bak/
[root@kvm yum.repos.d]# ls
repo.bak
[root@kvm yum.repos.d]# mv repo.bak/ /tmp/

```

```
[root@kvm yum.repos.d]# vim kvm.repo
[kvm]
name=kvm
baseurl=file:///mnt
gpgcheck=0
enabled=1
```

```
[root@kvm yum.repos.d]# yum clean all
已加载插件：fastestmirror
正在清理软件源： kvm
Cleaning up list of fastest mirrors
Other repos take up 171 M of disk space (use --verbose for details)
[root@kvm yum.repos.d]# yum repolist
已加载插件：fastestmirror
Determining fastest mirrors
kvm                                                                                               | 3.6 kB  00:00:00     
(1/2): kvm/group_gz                                                                               | 153 kB  00:00:00     
(2/2): kvm/primary_db                                                                             | 3.3 MB  00:00:00     
源标识                                                     源名称                                                   状态
kvm                                                        kvm                                                      4,070
repolist: 4,070

```

#### 5、关闭防火墙，selinux

```
[root@kvm yum.repos.d]# systemctl stop firewalld
[root@kvm yum.repos.d]# systemctl disable firewalld
Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
[root@kvm yum.repos.d]# setenforce 0
[root@kvm yum.repos.d]# vim /etc/selinux/config 
SELINUX=disabled


```

**################################################################## **

### 3、安装KVM

```
#安装 GNOME 桌面环境 如果 Centos 装了图形界面可以不需要装
yum groupinstall -y "GNOME Desktop"

```

```
#KVM 模块
yum -y install qemu-kvm

```

```
#安装KVM 调试工具,可不安装
yum -y install qemu-kvm-tools

```

```
#构建虚拟机的命令行工具
yum -y install virt-install

```

```
#qemu 组件,创建磁盘、启动虚拟机等
yum -y install qemu-img

```

```
#网络支持工具
yum -y install bridge-utils

```

```
#虚拟机管理工具
yum -y install libvirt

```

```
#图形界面管理虚拟机
yum -y install virt-manager

```

>  
 **检测cpu是否支持虚拟化** 


```
[root@kvm selinux]# cat /proc/cpuinfo | grep vmx

```

<img alt="" height="662" src="https://img-blog.csdnimg.cn/2436654dd78c49a585baaff44ad63fe5.png" width="1200">

>  
 ** 查看KVM模块是否已经安装** 


```
[root@kvm selinux]# lsmod | grep kvm
kvm_intel             188740  0 
kvm                   637289  1 kvm_intel
irqbypass              13503  1 kvm

```

设置开启启动界面的显示模式

```
ln -sf /lib/systemd/system/graphical.target /etc/systemd/system/default.target

```

**################################################################## ** 

### 4、设置KVM网络

>  
 **KVM网络的两种模式：** 
 **① NAT： 默认设置，数据包由 NAT 方式通过主机的接口进行传送，可以访问外网，但是无法从外部访问虚拟机网络 ② 网桥：这种模式允许虚拟机像一台独立的主机一样拥有网络，外部的机器可以直接访问到虚拟机内部，但需要网卡支持(一般有线网卡都支持)** 


>  
 ** ens33网卡设置：** 


```
[root@kvm network-scripts]# cat ifcfg-ens33 
BOOTPROTO="none"
NAME="ens33"
UUID="08e2fd65-cbd7-45d7-bdd3-0c508f676f9d"
DEVICE="ens33"
ONBOOT="yes"
#IPADDR=192.168.20.200
#PREFIX=24
#GATEWAY=192.168.20.2
#DNS1=114.114.114.114
BRIDGE=br0

```

>  
 **br0网卡设置** 


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
IPADDR=192.168.20.200
NETMASK=255.255.255.0
GATEWAY=192.168.20.2
DNS1=114.114.114.114

```

>  
 **重启网卡，查看ip，测试网络** 


```
[root@kvm network-scripts]# service network restart
Restarting network (via systemctl):                        [  确定  ]
[root@kvm network-scripts]# ip a
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast master br0 state UP group default qlen 1000
    link/ether 00:0c:29:fe:83:82 brd ff:ff:ff:ff:ff:ff
3: br0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:0c:29:fe:83:82 brd ff:ff:ff:ff:ff:ff
    inet 192.168.20.200/24 brd 192.168.20.255 scope global noprefixroute br0
       valid_lft forever preferred_lft forever
    inet6 fe80::8ff1:9cd3:6469:96b5/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
[root@kvm network-scripts]# ping www.baidu.com
PING www.a.shifen.com (112.80.248.76) 56(84) bytes of data.
64 bytes from 112.80.248.76 (112.80.248.76): icmp_seq=1 ttl=128 time=13.9 ms
64 bytes from 112.80.248.76 (112.80.248.76): icmp_seq=2 ttl=128 time=14.1 ms
64 bytes from 112.80.248.76 (112.80.248.76): icmp_seq=3 ttl=128 time=13.0 ms

```

**################################################################## ** 

### 5、KVM部署与管理

>  
 **创建KVM存储与镜像的目录，上传一个centos7的镜像文件，作为创建KVM虚拟机的镜像文件** 


```
[root@kvm network-scripts]# mkdir -p /data/data_kvm/iso
[root@kvm network-scripts]# mkdir -p /data/data_kvm/store

```

<img alt="" height="283" src="https://img-blog.csdnimg.cn/a66f7d9ae9594c07b7da41f52467f43e.png" width="804">

**################################################################## ** 

### 6、使用虚拟系统管理器管理虚拟机

>  
 ** 一切就绪以后，返回VMware虚拟机，进入刚才创建的KVM虚拟机，现在虚拟机会由刚才的字符界面，变成一个图形界面** 


<img alt="" height="830" src="https://img-blog.csdnimg.cn/52c42ece1c8f4adcaf0973351aaa21fd.png" width="1200">

<img alt="" height="528" src="https://img-blog.csdnimg.cn/e17437ba657947e887075839158263c3.png" width="1200">

<img alt="" height="761" src="https://img-blog.csdnimg.cn/f0f7096d718d4e8f86ec75cda24eb7b9.png" width="1200">

<img alt="" height="696" src="https://img-blog.csdnimg.cn/5e61f295cd1f4791af436c01be602772.png" width="1200">

#### 创建存储池 

>  
 **打开终端，进入命令行** 


 <img alt="" height="529" src="https://img-blog.csdnimg.cn/8c9a05cd923f4c2caa211f34e5ac85e8.png" width="874">

<img alt="" height="540" src="https://img-blog.csdnimg.cn/fc5bfac06aa74ef7826a5f161a164e1b.png" width="755">

<img alt="" height="392" src="https://img-blog.csdnimg.cn/4849cce2e53748be90ef1cf1cc5901d2.png" width="466">

**################################################################## ** 

#### 创建存储卷 

 <img alt="" height="532" src="https://img-blog.csdnimg.cn/2b2476a1faa84c7ba12f43715f8e1d66.png" width="910">

再次创建一个存储卷，存储iso镜像

<img alt="" height="494" src="https://img-blog.csdnimg.cn/477c23fc6b854579bead429d028441e7.png" width="727">

 <img alt="" height="385" src="https://img-blog.csdnimg.cn/55ff8d0e61cf4e8181d1e4e3880078bf.png" width="463">

**################################################################## ** 

#### 创建虚拟机 

 <img alt="" height="498" src="https://img-blog.csdnimg.cn/dc5d97746bdf44b8ae73f8504dd93274.png" width="664">

 <img alt="" height="537" src="https://img-blog.csdnimg.cn/b6494038405746e88bf386223bc517c1.png" width="882">

 <img alt="" height="272" src="https://img-blog.csdnimg.cn/f83c161ddeda44a79a4d5f09bc2bd835.png" width="401"><img alt="" height="308" src="https://img-blog.csdnimg.cn/64b04ea9bb734dda97bdca6ab656345c.png" width="399">

 <img alt="" height="481" src="https://img-blog.csdnimg.cn/08dde75ba4c14dc38c3cf3a7dff86c0e.png" width="404">

 <img alt="" height="654" src="https://img-blog.csdnimg.cn/db535e60745f48469e31a1742fafae9c.png" width="802">

>  
 **已进入虚拟机的安装页面 ，进入centos7的安装界面** 


 <img alt="" height="648" src="https://img-blog.csdnimg.cn/6355d3cb4ab1400da3f9ca3f29b0158f.png" width="800">

<img alt="" height="1007" src="https://img-blog.csdnimg.cn/b9d4cf4f6e1349ba910a7be122169094.png" width="1200">

 **################################################################## ** 

#### 命令行模式创建虚拟机

>  
 **刚才在图形界面开启了一台虚拟机，现在查看这台虚拟机的配置文件和磁盘的镜像文件** 


```
[root@kvm etc]# ls /etc/libvirt/qemu
autostart  centos7-test.xml  networks
[root@kvm etc]# ls /var/lib/libvirt/images/
centos7-test.qcow2

```

>  
 **先将虚拟机centos7-test停止，拷贝它的配置文件以及磁盘镜像** 


```
[root@kvm etc]# virsh list --all
 Id    名称                         状态
----------------------------------------------------
 2     centos7-test                   running

[root@kvm etc]# virsh shutdown centos7-test 
域 centos7-test 被关闭

[root@kvm etc]# virsh list --all
 Id    名称                         状态
----------------------------------------------------
 -     centos7-test                   关闭


```

```
[root@kvm etc]# cd /etc/libvirt/qemu/
[root@kvm qemu]# ls
autostart  centos7-test.xml  networks
[root@kvm qemu]# cp centos7-test.xml vm1.xml
[root@kvm qemu]# ls
autostart  centos7-test.xml  networks  vm1.xml
[root@kvm qemu]# cd /var/lib/libvirt/images/
[root@kvm images]# ls
centos7-test.qcow2
[root@kvm images]# cp centos7-test.qcow2 vm1.img
[root@kvm images]# ls
centos7-test.qcow2  vm1.img

```

>  
 **修改配置文件** 


<img alt="" height="233" src="https://img-blog.csdnimg.cn/ea89cbbe4c5d4fc2b758e0abd0ef7741.png" width="831">

 <img alt="" height="256" src="https://img-blog.csdnimg.cn/a13d740defd54602844ba77b7e822746.png" width="947">

<img alt="" height="216" src="https://img-blog.csdnimg.cn/0ae407136cfa460989d55eaf35c13f4c.png" width="701">

>  
 **创建虚拟机** 


```
[root@kvm qemu]# virsh define /etc/libvirt/qemu/vm1.xml 
定义域 vm1（从 /etc/libvirt/qemu/vm1.xml）

```

>  
 **重启kvm服务器** 


```
[root@kvm qemu]# systemctl restart libvirtd

```

>  
 **开启路由转发** 


```
[root@kvm qemu]# vim /etc/sysctl.conf 
net.ipv4.ip_forward = 1

```

```
[root@kvm qemu]# sysctl -p
net.ipv4.ip_forward = 1

```

>  
 **查看创建的虚拟机** 


```
[root@kvm ~]# virsh list  --all
 Id    名称                         状态
----------------------------------------------------
 1     centos7-test                   running
 2     vm1                            running

```













 参考：
