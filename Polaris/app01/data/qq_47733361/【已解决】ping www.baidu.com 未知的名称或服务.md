
--- 
title:  【已解决】ping: www.baidu.com: 未知的名称或服务 
tags: []
categories: [] 

---
在执行ping www.baidu.com命令时，出现如下错误： <img src="https://img-blog.csdnimg.cn/b2de444cd30e458fb834805ab0b4f9ec.png#pic_center" alt="在这里插入图片描述">

## 解决办法：

### 一、找到自己电脑ip地址

找到虚拟机标题栏中的 **编辑** 选项，点击虚拟网络编辑器 <img src="https://img-blog.csdnimg.cn/8ada312d340b4717ad91feb7e01e17d5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_15,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 选择VMnet8，找到子网IP <img src="https://img-blog.csdnimg.cn/b2c0e42bb99b46539503a7a5a9be9e20.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 二、进入管理员界面

使用下面命令进入root用户，输入密码：

```
su root

```

### 二、编辑自己ip地址

使用下面命令进入vi编辑器，编辑自己ip等相关信息。

```
vim /etc/sysconfig/network-scripts/ifcfg-ens33

```

信息修改说明：

```
TYPE="Ethernet"
PROXY_METHOD="none"
BROWSER_ONLY="no"
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME="ens33"
UUID="4a25e1a2-9ca5-4220-8ecc-182e3abc25f5"
DEVICE="ens33"

//需要修改的地方
ONBOOT="yes"
BOOTPROTO="static"

//需要添加的地方
IPADDR=192.168.79.130  //修改为第一步中自己的ip地址，不要写 **.0**，最后一个数字最好为50至150之间
GATEWAY=192.168.79.2   //把ip中最后一个数字改为.2即可
NETMASK=255.255.255.0  //就这个
DNS1=192.168.79.2      //与GATEWAY一样即可

```

<img src="https://img-blog.csdnimg.cn/f7954779fe534f9f825f31d983b3f1c2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 进行保存退出。

**注：vi编辑器保存退出方法** 在修改完上述内容后，按Esc键，输入 **:wq** ，然后回车即可保存退出。

### 三、查看网卡ip

输入命令：

```
ifconfig

```

出现如下界面代表成功： <img src="https://img-blog.csdnimg.cn/9e337e9a916041f0b7c7b78702f3828f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 四、验证

输入下面命令：

```
ping www.baidu.com

```

<img src="https://img-blog.csdnimg.cn/11fa76d1dcfa4223899cc6fa69881f21.png" alt="在这里插入图片描述"> 成功运行！

## 所有命令截图：

<img src="https://img-blog.csdnimg.cn/1543d2dfef6046a28d74b44b3590236c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
[LCC@controller ~]$ su root
密码：
[root@controller LCC]# vim /etc/sysconfig/network-scripts/ifcfg-ens33
[root@controller LCC]# ifconfig
ens33: flags=4163&lt;UP,BROADCAST,RUNNING,MULTICAST&gt;  mtu 1500
        inet 192.168.79.130  netmask 255.255.255.0  broadcast 192.168.79.255
        inet6 fe80::e44d:3dca:c2d6:f154  prefixlen 64  scopeid 0x20&lt;link&gt;
        ether 00:0c:29:6a:27:b0  txqueuelen 1000  (Ethernet)
        RX packets 691  bytes 89714 (87.6 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 878  bytes 71082 (69.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73&lt;UP,LOOPBACK,RUNNING&gt;  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10&lt;host&gt;
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 3430  bytes 220953 (215.7 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3430  bytes 220953 (215.7 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

virbr0: flags=4099&lt;UP,BROADCAST,MULTICAST&gt;  mtu 1500
        inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255
        ether 52:54:00:c1:56:cc  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

[root@controller LCC]# 
[root@controller LCC]# ping www.baidu.com
PING www.a.shifen.com (39.156.66.18) 56(84) bytes of data.
64 bytes from 39.156.66.18 (39.156.66.18): icmp_seq=1 ttl=128 time=47.2 ms
64 bytes from 39.156.66.18 (39.156.66.18): icmp_seq=2 ttl=128 time=41.2 ms
64 bytes from 39.156.66.18 (39.156.66.18): icmp_seq=3 ttl=128 time=39.2 ms
64 bytes from 39.156.66.18 (39.156.66.18): icmp_seq=4 ttl=128 time=156 ms
64 bytes from 39.156.66.18 (39.156.66.18): icmp_seq=5 ttl=128 time=24.7 ms
64 bytes from 39.156.66.18 (39.156.66.18): icmp_seq=6 ttl=128 time=19.2 ms


```
