
--- 
title:  VMware之esxcli命令 
tags: []
categories: [] 

---
## 一、esxcli命令简介

  esxcli命令是用于管理VMware ESXi主机的命令行实用程序。它允许管理员在主机上执行各种管理任务，如配置网络设置、存储、虚拟机等。实际上我们在控制台的所有操作最终都会转换为命令在后台执行。以下是一些常见的esxcli命令：
- esxcli network ip命令：用于配置网络设置，如IP地址、子网掩码、网关等。- esxcli storage命令：用于管理存储，如创建、删除、格式化数据存储。- esxcli vm命令：用于管理虚拟机，如创建、删除、启动、停止虚拟机。- esxcli system命令：用于管理系统设置，如配置NTP服务器、主机名等。- esxcli hardware命令：用于管理硬件设置，如查看主机硬件信息、配置RAID控制器等。- esxcli software命令：用于管理软件设置，如安装、升级、卸载软件包。- esxcli network firewall命令：用于配置防火墙规则。
  总之，esxcli命令是VMware ESXi主机管理的重要工具，可以帮助管理员更轻松地管理主机和虚拟机。

## 二、esxcli命令使用示例

### 1、查看命令版本

  随着命令版本的更新迭代，详细命令可能会略有差别，此博文命令示例均是在esxcli 7.0.0版本上的操作示例，主机操作系统为ESXi 7.0.1版本。

>  
 [root@localhost:~] esxcli --version Script ‘esxcli’ version: 7.0.0 


### 2、查看操作系统版本

>  
 [root@localhost:~] esxcli software baseimage get ESXi:7.0.1-0.0.16850804 [root@localhost:~] esxcli system version get Product: VMware ESXi Version: 7.0.1 Build: Releasebuild-16850804 Update: 1 Patch: 0 


### 3、查看主机IP地址

>  
 [root@localhost:~] esxcli network ip interface ipv4 get Name IPv4 Address IPv4 Netmask IPv4 Broadcast Address Type Gateway DHCP DNS ---- ------------ ------------- -------------- ------------ ------------ -------- vmk0 10.2.129.100 255.255.255.0 10.2.129.255 STATIC 10.2.129.254 false 


### 4、查看主机路由

>  
 [root@localhost:~] esxcli network ip route ipv4 list Network Netmask Gateway Interface Source ---------- ------------- ------------ --------- ------ default 0.0.0.0 10.2.129.254 vmk0 MANUAL 10.2.129.0 255.255.255.0 0.0.0.0 vmk0 MANUAL 


### 5、查看网卡MAC地址

>  
 [root@localhost:~] esxcli network nic list Name PCI Device Driver Admin Status Link Status Speed Duplex MAC Address MTU Description ------ ------------ ------ ------------ ----------- ----- ------ ----------------- ---- ----------- vmnic0 0000:04:00.0 ntg3 Up Up 1000 Full 08:92:04:b2:00:86 1500 Broadcom Corporation NetXtreme BCM5720 Gigabit Ethernet vmnic1 0000:04:00.1 ntg3 Up Down 0 Half 08:92:04:b2:00:87 1500 Broadcom Corporation NetXtreme BCM5720 Gigabit Ethernet 


### 6、设置网卡IP

>  
 [root@localhost:~] esxcli network ip interface ipv4 set --ipv4=192.168.0.100 --netmask=255.255.255.0 --gateway=192.168.0.1 


### 7、查看防火墙状态

>  
 [root@localhost:~] esxcli network firewall get Default Action: DROP Enabled: true Loaded: true 


### 8、查看防火墙策略列表

  可以对防火墙策略进行调整，但是此调整仅限对现有策略的禁用、启用、限制IP地址等，并没有add新增一条规则的命令。

>  
 [root@localhost:~] esxcli network firewall ruleset list Name Enabled --------------------------- ------- sshServer true sshClient false 


### 9、查看虚拟机列表

>  
 [root@localhost:~] esxcli vm process list <img src="https://img-blog.csdnimg.cn/0ac77e07632b485db99d99a4df8651d0.png" alt="在这里插入图片描述"> 


### 10、设置系统主机名

>  
 [root@localhost:~] esxcli system hostname set --host=wfs100 


### 11、查看系统账户列表

  使用此命令可以查看系统当前的账户列表，也可以执行增加(add)、删除(remove)和修改(set)账户的操作。

>  
 [root@wfs100:~] esxcli system account list User ID Description ------- ----------- root Administrator dcui DCUI User vpxuser VMware VirtualCenter administration account 


### 12、重启系统

  可以执行reboot重启系统或者poweoff命令关机。

>  
 [root@wfs100:~] esxcli system shutdown reboot 


### 13、查看存储适配器

  此命令查看的是HBA卡信息，如下显示HBA卡型号为DELL的H745。

>  
 [root@wfs100:~] esxcli storage core adapter list HBA Name Driver Link State UID Capabilities Description -------- -------- ---------- -------------------- ------------ ----------- vmhba0 lsi_mr3 link-n/a sas.5ec2a720410cb600 (0000:65:00.0) Broadcom Dell PERC H745 Front vmhba1 vmw_ahci link-n/a sata.vmhba1 (0000:00:11.5) Intel Corporation Lewisburg SATA AHCI Controller vmhba2 vmw_ahci link-n/a sata.vmhba2 (0000:00:17.0) Intel Corporation Lewisburg SATA AHCI Controller 


### 14、查看服务器cpu信息

>  
 [root@wfs100:~] esxcli hardware cpu global get CPU Packages: 2 CPU Cores: 24 CPU Threads: 48 Hyperthreading Active: true Hyperthreading Supported: true Hyperthreading Enabled: true HV Support: 3 


### 15、查看服务器内存信息

>  
 [root@wfs100:~] esxcli hardware memory get Physical Memory: 136863825920 Bytes Reliable Memory: 0 Bytes NUMA Node Count: 2 


### 16、查看服务器电源信息

>  
 [root@wfs100:~] esxcli hardware power policy get Id: 2 Name: Balanced Short Name: dynamic 


### 17、查看服务器型号

>  
 [root@wfs100:~] esxcli hardware platform get Platform Information UUID: 0x4c 0x4c 0x45 0x44 0x0 0x42 0x46 0x10 0x80 0x53 0xb3 0xc0 0x4f 0x34 0x54 0x33 Product Name: PowerEdge R750xs Vendor Name: Dell Inc. Serial Number: 3BFS4T3 Enclosure Serial Number: 3BFS4T3 BIOS Asset Tag: IPMI Supported: true 


### 18、查看PCI直通通道数量

>  
 [root@wfs100:~] esxcli hardware pci pcipassthru list Device ID Enabled ------------ ------- 0000:03:00.0 false 0000:04:00.0 false 0000:04:00.1 false 0000:65:00.0 false 


### 19、获取命令帮助

  esxcli是一个命令集，可以查询和操作的内容很多，如果不确定命令参数如何输入，我们都可以在最后加上–help先获取命令的帮助，然后再进一步操作和执行。

<img src="https://img-blog.csdnimg.cn/4b2340ff792845d696c0b5ab0f9f7923.png" alt="在这里插入图片描述">

## 三、esxcli命令语法及参数说明

### 1、使用语法

>  
 esxcli [options] {namespace}+ {cmd} [cmd options] 


### 2、参数选项说明

<th align="left">参数选项</th><th align="left">参数说明</th>
|------
<td align="left">–formatter=FORMATTER</td><td align="left">覆盖要用于给定命令的格式化程序。可用的格式化程序：xml、csv、keyvalue</td>
<td align="left">–screen-width=SCREENWIDTH</td><td align="left">设置文本格式时使用指定的屏幕宽度</td>
<td align="left">–debug</td><td align="left">启用调试或内部使用选项</td>
<td align="left">–version</td><td align="left">显示脚本的版本信息</td>
<td align="left">-?, --help</td><td align="left">显示脚本的使用信息</td>

### 3、命名空间说明

<th align="center">命名空间</th><th align="left">说明</th>
|------
<td align="center">amsd</td><td align="left">用于Gen10命令的无代理管理服务（AMS）</td>
<td align="center">amshelper</td><td align="left">Gen9命令的无代理管理服务（AMS）</td>
<td align="center">bootcfg</td><td align="left">引导配置实用程序</td>
<td align="center">daemon</td><td align="left">用于控制使用守护程序SDK（DSDK）构建的守护程序的命令。</td>
<td align="center">device</td><td align="left">设备管理器命令</td>
<td align="center">esxcli</td><td align="left">在esxcli系统本身上操作的命令，允许用户获取其他信息。</td>
<td align="center">fcoe</td><td align="left">VMware fcoe命令。</td>
<td align="center">graphics</td><td align="left">VMware图形命令。</td>
<td align="center">hardware</td><td align="left">VMKernel硬件财产和用于配置硬件的命令。</td>
<td align="center">iscsi</td><td align="left">VMware iscsi命令。</td>
<td align="center">network</td><td align="left">与ESX主机上的网络维护相关的操作。这包括各种各样的命令来操作虚拟网络组件（vswitch、portgroup等）以及本地主机IP、DNS和常规主机网络设置。</td>
<td align="center">nvme</td><td align="left">VMware nvme驱动程序操作。</td>
<td align="center">rdma</td><td align="left">与ESX主机上的远程直接内存访问（rdma）协议栈有关的操作。</td>
<td align="center">sched</td><td align="left">VMKernel系统财产和用于配置调度相关功能的命令。</td>
<td align="center">sma</td><td align="left">Gen10命令的系统管理助手（sma）反向代理服务</td>
<td align="center">sofrware</td><td align="left">管理ESXi软件映像和软件包</td>
<td align="center">ssacli</td><td align="left">智能存储管理员CLI</td>
<td align="center">storage</td><td align="left">VMware存储命令。</td>
<td align="center">system</td><td align="left">VMKernel系统财产和用于配置内核核心系统和相关系统服务的财产的命令。</td>
<td align="center">testevent</td><td align="left">测试事件实用程序</td>
<td align="center">vm</td><td align="left">允许用户控制虚拟机操作的少量操作。</td>
<td align="center">vsan</td><td align="left">VMware vsan命令</td>
