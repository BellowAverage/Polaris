
--- 
title:  搭建KVM虚拟化 
tags: []
categories: [] 

---
## 搭建KVM虚拟化



#### 文章目录
- - <ul><li>- - - <ul><li>- - - - - - - <ul><li>- 


### 1、虚拟化的由来：

美国环境保护EPA报告中曾经统计过一组统计数据:：EPA研究服务器和数据中心得能源效率时发现，实际上服务器只有5%得时间时在工作的，其他时间一直处于休眠状态；

那么通过虚拟化技术将一台计算机虚拟为多台逻辑计算机，在一台计算机上同时运行多个逻辑计算机，同时每个逻辑计算机可运行不同的操作系统，应用程序都可以在相互独立的空间内运行而互相不影响，从而提高计算机的工作效率。

<img src="https://img-blog.csdnimg.cn/53478c87d8244876ad8166f42aaf59c3.png#pic_center" alt="在这里插入图片描述">

### 2、虚拟化技术实现方式：

01、在一个操作系统中(win10) 模拟多个操作系统(centos、win10、suse)，同时每个操作系统可以跑不同的服务(nginx，tomcat等) ，从而实现一台宿主机搭建一个集群(从整体)。

02、通过软件/应用程序的方式，来实现物理硬件的功能。 比如ensp软件的形式模拟出硬件设备(二、三层交换机、三层路由器、PC机、防火墙等)。

**虚拟化？**

通过虚拟化技术将一台计算机虚拟为多台逻辑计算机，在一台计算机上同时运行多个逻辑计算机， 同时每个逻辑计算机可运行不同的操作系统，应用程序都可以在相互独立的空间内运行而互相不影响，从而提高计算机的工作效率。

### 3、虚拟化类型：

01）全虚拟化：将物理硬件资源全部通过软件的方式抽象化，最后进行调用。 使用的方法：使用hypervisor (VMM) 软件，其原理是在底层硬件和服务器之间建立一个抽象层，而基于核心的虚拟机是面向Linux系统的开源产品hypervisor(VMM)可以捕捉CPU的指令,为指令访问硬件控制器和外设充当中介。 02）半虚拟化：需要修改操作系统。 03）直通：直接使用物理硬件资源(需要支持，还不完善)。
- Xen支持的虚拟化技术:全虚拟化，半虚拟化- KVM:支持的虚拟化技术:全虚拟化
#### VMM（hypervisor）的功能：
1. 对物理资源进行逻辑分割(转化为虚拟资源)。1. 调用虚拟资源供与应用程序(虚拟机)。
### 4、KVM概述：
- KVM (Kernel-based Vritual Machine) --基于内核的虚拟机。- KVM是基于虚拟化扩展的X86硬件的开源Linux原生的全虚拟化方案( 要求cpu支持Intel-VT-x或AMD-V)。- KVM(组件)内嵌于内核模块中，模拟处理器和内存以支持虚拟机运行。- 虚拟机被实现为常规的Linux进程，由标准Linux调度程序进行调度。- 虚拟机的每个虚拟CPU被实现为一个常规的Linux 进程。这使得KMV能够使用Linux 内核的已有功能，但KVM本身不执行任何模拟。需要客户空间程序(虚拟机)通过/dev/kvm(此虚拟设备需要开起硬件辅助虚拟化才能看到)。- 接口设置一个客户机虚拟服务器的地址空间，并且由Qemu模拟I/O (ioctl) 进行调度资源和维护管理。- Libvirt: KVM的管理工具，除了可以管理KVM这类VMM，还可以管理Xen，VirtualBox， 甚至openStack底层。- Libvirt包含3个组件:后台daemon程序libvirtd、API库、命令行工具virsh。
### 5、KVM架构与原理：
-  客户机(guestOs) ：VM中的OS为Guestos -  客户机在操作系统中运行的模式，客户机分为内核模式和用户模式，作用如下: -  用户模式： -  为用户提供虚拟机管理的用户空间工具以及代表用户执行I/O，Qemu工作在此模式下(Qemu的主要功能) -  linux内核模式： -  模拟CPU、 内存，实现客户模式切换，处理从客户模式的推出，KVM即运行在此模式下。 
### 6、KVM核心组件：
1. 在内核层：KVM模块将物理资源逻辑分割为虚拟化资源。1. 在抽象层：Qemn组件，会和内核层的KVM进行对接，调用所需的资源。
### 7、KVM工作流程：
1. 用户模式的Qemu利用接口libkvm通过ioctl系统调用进入内核模式。KVM驱动为虚拟机分割创建虚拟CPU和虚拟内存；1. 然后执行VMLAU :NCH指令进入客户模式，装载Guest OS并运行。Guest OS运行过程中如果发生异常，则暂停Guest OS的运行并保存当前状态同时退出到内核模式来处理这些异常。1. 内核模式处理这些异常时如果不需要I/o则处理完成后重新进入客户模式。如果需要I/o则进入到用户模式，则由Qemu 来处理I/O， 处理完成后进入内核模式，再进入客户模式。
<img src="https://img-blog.csdnimg.cn/4011157e96244a26b4a97b1cc2f24682.png#pic_center" alt="在这里插入图片描述">

### 8、部署KVM虚拟化：

#### 1、实验准备：

虚拟机设置–处理器–勾选虚拟化 Intel-VT-x/EPT 或 AMD-V/RVI(V) 添加磁盘并给大的内存

<img src="https://img-blog.csdnimg.cn/a11737e3e4cd4b14985e48b221e42207.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/77d4240d8fcf497495c6cb8589490c34.png#pic_center" alt="在这里插入图片描述">

```
mkdir /mount
#设置自动挂载
vim /etc/fstab
/dev/cdrom /mount iso9660 defaults 0 0

mount -a
#查看挂载情况
df -hT

```

<img src="https://img-blog.csdnimg.cn/7882ef34b8234cab99a7d8553ce93e45.png#pic_center" alt="在这里插入图片描述">

#### 2、环境优化：

设置DNS反向解析，设置为NO 可以让客户端ssh连接服务器；

```
vim /etc/ssh/sshd_config 
115 UseDNS no		##取消注释，yes改为no

```

<img src="https://img-blog.csdnimg.cn/8a305232e9064da5a0177e2bb5ed02da.png#pic_center" alt="在这里插入图片描述">

#### 3、制作本地yum仓库：

```
cd /etc/yum.repos.d/
mkdir bak
mv *.repo bak

vim local.repo
[local]
name=kvm
baseurl=file:///mount
gpgcheck=0
enable=1

#清理缓存
yum clean all
yum makecache

```

<img src="https://img-blog.csdnimg.cn/34b90da823a54804936535c10fde6c58.png#pic_center" alt="在这里插入图片描述">

#### 4、安装KVM基本组件：

```
yum groupinstall -y "GNOME Desktop"		##安装GNOME桌面环境，若装了图形界面可以不需要安装
yum -y install qemu-kvm		##安装KVM模块

yum -y install qemu-kvm-tools	##安装KVM调试工具，可不安装

yum -y install virt-install		##构建虚拟机的命令行工具

yum -y install qemu-img		##qemu组件，创建磁盘、启动虚拟机等

yum -y install bridge-utils		##网络支持工具

yum -y install libvirt		##虚拟机管理工具

yum -y install virt-manager		##图形界面管理虚拟机

cat /proc/cpuinfo | grep vmx		##检测cpu是否支持虚拟化

```

<img src="https://img-blog.csdnimg.cn/e2f0e0a1c87b49a09e8f165e9be2dab5.png#pic_center" alt="在这里插入图片描述">

```
lsmod | grep kvm
#查看kvm模块是否已安装；lsmod:显示已载入的系统模块

ln -sf /lib/systemd/system/graphical.target /etc/systemd/system/default.target

```

<img src="https://img-blog.csdnimg.cn/56f5150b18494ee6904266b69e9f1924.png#pic_center" alt="在这里插入图片描述">

#### 5、设置KVM网络：

KVM网络的两种模式：
1. NAT：默认设置，数据包由NAT方式通过主机的接口进行传送，可以访问外网，但是无法从外部访问虚拟机网络。1. 网桥：这种模式允许虚拟机像一台独立的主机一样拥有网络，外部的机器可以直接访问到虚拟机内部，但需要网卡支持(一般有线网卡都支持)。
这里使用Bridge网桥模式进行部署：

```
vim /etc/sysconfig/network-scripts/ifcfg-ens33 

TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=none            #修改为none
#IPADDR=192.168.111.10    #IP配置都注释掉
#NETMASK=255.255.255.0
#GATEWAY=192.168.111.2
#DNS=8.8.8.8
DEFROUTE=yesIPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
UUID=1415e5f2-2565-47a5-ad95-898e43f81c66
DEVICE=ens33
ONBOOT=yes
BRIDGE=br0             #设置网桥模式，关联br0网卡

```

**创建、编辑网桥：**

```
vim /etc/sysconfig/network-scripts/ifcfg-br0

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
IPADDR=192.168.111.100      #IP自定义，通过修改Xshell属性的IP地址可再次使用xshll连接
NETMASK=255.255.255.0
GATEWAY=192.168.111.2

#重启网卡服务
systemctl restart network
ifconfig   #查看一下

```

**注意：**这时因为网卡文件被更改，无法连接xshell，需要虚拟机操作。

#### 6、KVM部署与管理：

##### 01）创建KVM存储和镜像数据的目录、上传centos7镜像；

```
mkdir -p  /data/data_kvm/iso
mkdir -p /data/data_kvm/store

#上传虚拟机镜像文件
CentOS-7-x86_64-DVD-1810-7.6.iso	##使用XFTP 7 上传文件

cp -p CentOS-7-x86_64-DVD-1810-7.6.iso /data/data_kvm/iso/	#需要确保属主属组是root

```

##### 02）使用虚拟系统管理器管理虚拟机：

虚拟机操作，输入virt-manager，弹出虚拟系统管理器；

<img src="https://img-blog.csdnimg.cn/0fd8f6f3c2e24404bb1d1e99a7497e53.png#pic_center" alt="在这里插入图片描述">

1、创建存储池swl_store，双击 QEMU/KVM;

<img src="https://img-blog.csdnimg.cn/cf61304a40dd4c90a7ca318ce054b457.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/da81bfcd6eb14d5d98cb23e458d1c9b4.png#pic_center" alt="在这里插入图片描述">

2、创建存储卷store_01 创建存储池store_01，默认的格式是qcow2，虚拟化的格式，支持KVM虚拟化的格式，也是支持qemu组件的格式。

<img src="https://img-blog.csdnimg.cn/18f365fcabed4a28bf7ac869da7ea1b0.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/64fe768faa4c401790c531ce6b401fc0.png#pic_center" alt="在这里插入图片描述">

3、创建镜像池swl_iso，与存储池一样的步骤；

<img src="https://img-blog.csdnimg.cn/e402883817af491fa7c4f3026a974d07.png#pic_center" alt="在这里插入图片描述">

4、创建虚拟机，QEMU/KVM右击新建；

<img src="https://img-blog.csdnimg.cn/1b371c2c4cf442449b087c6a5c0e22f9.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/cb4d2e16c9db45399ea0dc633d8d0571.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b376b28ae56a429aae2988936240c5de.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/0b9f19950ef049eabf9b8f031e269a4d.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/4d50d6e683ed461ca1cb2c7fb3363055.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/92c5f56f07bd4c6dbd204e2ba11dd12c.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a3955a0fc57d454499ef4fd57ba5f824.png#pic_center" alt="在这里插入图片描述">

5、后面就跟虚拟机安装是一样的步骤了。

<img src="https://img-blog.csdnimg.cn/9ffbffc03fc54834b0e3a1e93a65cb32.png#pic_center" alt="在这里插入图片描述">

### 9、总结：
1. 全虚拟化：将物理硬件资源全部通过软件的方式抽象化，最后进行调用1. 半虚拟化：需要修改操作系统(以软件形式模拟物理硬件功能+物理硬件资源的加强型支持)1. 直通：直接使用物理硬件资源(需要支持，还不完善)
KVM虚拟化架构的三种模式：
1. 客户模式(guestOs)1. 用户模式1. linux内核模式