
--- 
title:  Linux命令之网络命令ifconfig 
tags: []
categories: [] 

---
## 一、ifconfig命令简介

  ifconfig命令是Linux系统下的一个网络配置工具，用于查看和设置网络接口的配置信息。通过ifconfig命令，用户可以查看当前系统中所有网络接口的详细信息，如IP地址、子网掩码、广播地址等。同时，用户还可以使用ifconfig命令对网络接口进行配置，如启用或禁用网络接口、设置静态IP地址等。该命令与window环境下的ipconfig命令相似，容易出现混淆，当然这两个命令只能在各自的平台运行，输入验证下即可区分。

## 二、ifconfig命令使用示例

### 1、查看命令版本

  通过下面命令可以看到ifconfig命令属于net-tools工具的子命令，如果linux环境提示不存在此命令，centos环境下我们可以使用yum install -y net-tools命令安装此命令集。

>  
 [root@s166 ~]# ifconfig --version net-tools 2.10-alpha 


### 2、获取命令帮助

  通过–help参数获取命令帮助。我们可以看到该命令可以查看IP地址、状态信息；也可以配置IP地址、掩码等；还可以启用或者禁用网络接口。 <img src="https://img-blog.csdnimg.cn/7adfea69514c4144a418caf3da875d18.png" alt="在这里插入图片描述">

### 3、查看所有网卡的状态信息

  使用-a参数可以查看网卡的所有状态和配置信息。 <img src="https://img-blog.csdnimg.cn/6a2a6906f2f94f3486d57ec2bbf398a1.png" alt="在这里插入图片描述">

### 4、查看指定网卡的状态信息

>  
 [root@s166 ~]# ifconfig eth0 eth0: flags=4163&lt;UP,BROADCAST,RUNNING,MULTICAST&gt; mtu 1500 inet 192.168.0.166 netmask 255.255.255.0 broadcast 192.168.0.255 inet6 fe80::242c:be63:5997:1371 prefixlen 64 scopeid 0x20 ether de:d5:84:b3:41:cb txqueuelen 1000 (Ethernet) RX packets 24769 bytes 3211666 (3.0 MiB) RX errors 0 dropped 0 overruns 0 frame 0 TX packets 1192 bytes 101143 (98.7 KiB) TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0 


### 5、精简显示网卡信息

>  
 [root@s166 ~]# ifconfig -s Iface MTU RX-OK RX-ERR RX-DRP RX-OVR TX-OK TX-ERR TX-DRP TX-OVR Flg eth0 1500 25710 0 0 0 1406 0 0 0 BMRU lo 65536 0 0 0 0 0 0 0 0 LRU virbr0 1500 0 0 0 0 0 0 0 0 BMU 


### 6、禁用网卡

  使用****ifconfig 网卡名 down****命令可以关闭一个网卡，如下关闭lo网卡后，查看状态就没有UP和RUNNING显示了。该命令等同于****ifdown 网卡名**** 命令。

>  
 [root@s166 ~]# ifconfig lo down [root@s166 ~]# ifconfig lo lo: flags=8&lt;LOOPBACK&gt; mtu 65536 inet 127.0.0.1 netmask 255.0.0.0 loop txqueuelen 1000 (Local Loopback) RX packets 0 bytes 0 (0.0 B) RX errors 0 dropped 0 overruns 0 frame 0 TX packets 0 bytes 0 (0.0 B) TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0 


### 7、启用网卡

  使用****ifconfig 网卡名 up****命令可以启用一个网卡，开启之后，如果网卡是连接状态就可以看到网卡是UP状态。该命令等同于****ifup 网卡名**** 命令。

>  
 [root@s166 ~]# ifconfig lo up [root@s166 ~]# ifconfig lo lo: flags=73&lt;UP,LOOPBACK,RUNNING&gt; mtu 65536 inet 127.0.0.1 netmask 255.0.0.0 inet6 ::1 prefixlen 128 scopeid 0x10 loop txqueuelen 1000 (Local Loopback) RX packets 0 bytes 0 (0.0 B) RX errors 0 dropped 0 overruns 0 frame 0 TX packets 0 bytes 0 (0.0 B) TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0 


### 8、配置网卡IP地址

  使用ifconfig命令可以设置或者修改网卡IP地址，当然不建议使用这种方式修改当前远程连接的网卡IP地址。而且该方式配置物理网卡地址会导致默认路由等信息不可用，这种方式修改完成后会导致远程连接不上的情况，此种方式下可以通过重启网卡服务恢复网卡。因为此方式并不会修改网卡配置文件，只是临时修改网卡IP地址。 <img src="https://img-blog.csdnimg.cn/763d0279d5434ba8af76e958a1290f69.png" alt="在这里插入图片描述">

### 9、创建网卡别名

  我们可以给网卡创建别名并配置第二IP地址，这个地址是可以访问和连接的。 <img src="https://img-blog.csdnimg.cn/6a088c8e25e641968c20f14b742c3d8a.png" alt="在这里插入图片描述">

### 10、删除网卡

  我们也可以使用命令删除别名的网卡地址，删除之后同时删除了别名网卡信息。博主尝试了无法删除物理网卡和loopback网卡地址。

>  
 [root@s166 ~]# ifconfig eth0:1 del 192.168.0.167 


### 11、不带参数使用

  ifconfig命令也可以不带任何参数执行，显示的结果是状态为UP的网卡信息。 <img src="https://img-blog.csdnimg.cn/c8952e101cbb48008bda4fb781da617f.png" alt="在这里插入图片描述">

### 12、修改网卡mac地址

  使用命令ifconfig eth0 hw ether可以修改eth0网卡的MAC地址，当然一般不建议修改，MAC地址是网卡出厂的时候固定的，如果任意修改可能导致局域网内MAC地址冲突，出现网络故障。 <img src="https://img-blog.csdnimg.cn/16afcae8632541d4a236de3fe45bc711.png" alt="在这里插入图片描述">

## 三、ifconfig命令语法及参数说明

### 1、命令语法
- 用法1：#ifconfig- 用法2：#ifconfig [参数说明] &lt;interface&gt; [down/up/del] &lt;address&gt;[/&lt;prefixlen&gt;]]
### 2、参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-a</td><td align="left">显示所有网卡信息</td>
<td align="left">-s</td><td align="left">显示网卡简短信息，命令类似于netstat -i</td>
<td align="left">-v</td><td align="left">显示更详细信息，对于某些错误情况更加详细</td>
<td align="left">down</td><td align="left">禁用网卡</td>
<td align="left">up</td><td align="left">启用网卡</td>
<td align="left">hw</td><td align="left">设置网卡MAC地址信息</td>
