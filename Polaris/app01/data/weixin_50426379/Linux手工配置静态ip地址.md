
--- 
title:  Linux手工配置静态ip地址 
tags: []
categories: [] 

---
## 手工配置静态ip地址



#### 文章目录
- - <ul><li>- - - 


### 1.查看ip地址

```
[root@nginx-kafka01 network-scripts]# ip a
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:be:d0:14 brd ff:ff:ff:ff:ff:ff
    inet 192.168.72.130/24 brd 192.168.72.255 scope global ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:febe:d014/64 scope link 
       valid_lft forever preferred_lft forever
# 192.168.72.130是ip地址

```

### 2.查看网关

```
# 查看网关
[root@nginx-kafka01 network-scripts]# ip route
default via 192.168.72.2 dev ens33 
# 192.168.72.2是网关

```

示例：

<img src="https://img-blog.csdnimg.cn/img_convert/7afcb02797f0a0f774cbc86bc051dc53.png" alt="image.png">

### 3.静态配置手工ip地址

下面配置的ip地址和网关直接用上面看到的ip和网关

```
[root@nginx-kafka01 ~]# cd /etc/sysconfig/network-scripts/
[root@nginx-kafka01 network-scripts]# ls
ifcfg-ens33  
[root@nginx-kafka01 network-scripts]# cat ifcfg-ens33 
BOOTPROTO="none"  #静态获得ip地址
NAME="ens33"      #网卡名称
DEVICE="ens33"    #设备名称
ONBOOT="yes"      #开机启动
IPADDR=192.168.72.130  #ip地址
PREFIX=24              #子网掩码
GATEWAY=192.168.72.2   #网关
DNS1=114.114.114.114   #DNS域名解析

```

示例：

<img src="https://img-blog.csdnimg.cn/img_convert/97c9ec9b14f7019d8e8370e394c2297c.png" alt="image.png">

### 4.重启配置文件

```
service network restart
# 或者
ifdown ens-33
ifup ens-33
# 因为NetworkManager和network服务只能运行其中一个
# 如果上面命令启动网卡失败，尝试使用下面这条命令
[root@nginx-kafka01 system]# ps -ef |grep -i  network
root       2382      1  0 09:44 ?        00:00:00 /usr/sbin/NetworkManager --no-daemon
root       2428   2349  0 09:58 pts/1    00:00:00 grep --color=auto -i network
# 如果有NetworkManager进程，就使用下面这条命令
[root@nginx-kafka01 ~]# systemctl restart NetworkManager

# 为什么可以用systemctl？
# 通过yum安装的软件几乎都在/usr/lib/systemd/system/里面有个对应的.service文件
# NetworkManager有对应的NetworkManager.service文件，所以通过systemctl管理程序
[root@nginx-kafka01 system]# cd /usr/lib/systemd/system/
[root@nginx-kafka01 system]# ls|grep Network
NetworkManager-dispatcher.service
NetworkManager.service
NetworkManager-wait-online.service

```

systemctl使用详情：
