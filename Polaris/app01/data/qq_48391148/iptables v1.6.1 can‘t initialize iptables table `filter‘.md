
--- 
title:  iptables v1.6.1: can‘t initialize iptables table `filter‘ 
tags: []
categories: [] 

---
Linux系统：AlmaLinux 9.2

容器内部加载iptables失败：

```
bash-4.4# iptables -nvL
iptables v1.6.1: can't initialize iptables table `filter': Table does not exist (do you need to insmod?)
Perhaps iptables or your kernel needs to be upgraded.

var code = "fb0d5928-c0ef-4a54-a1a3-7f7162b9bc13"
```

分析：

理论上来说，宿主机和容器是公用内核的，iptables是基于 iptable_filter这个模块的，

使用lsmod查看内核有没有加载这个模块，发现的确没有加载，



加载内核模块iptable_filter

```
[root@localhost ~]# modprobe iptable_filter
[root@localhost ~]# lsmod | grep ip
iptable_filter         16384  0
ip_tables              28672  1 iptable_filter
nf_defrag_ipv6         24576  1 nf_conntrack
nf_defrag_ipv4         16384  1 nf_conntrack

```

成功加载iptable_filter以后发现容器内就可以使用iptables了

```
bash-4.4# iptables -nvL
Chain INPUT (policy ACCEPT 8847 packets, 1353K bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain OUTPUT (policy ACCEPT 9207 packets, 1257K bytes)
 pkts bytes target     prot opt in     out     source               destination       
```


