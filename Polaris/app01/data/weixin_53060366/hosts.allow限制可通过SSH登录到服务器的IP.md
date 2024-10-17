
--- 
title:  hosts.allow限制可通过SSH登录到服务器的IP 
tags: []
categories: [] 

---
## hosts.allow限制可通过SSH登录到服务器的IP

网络防火墙是阻挡非授权主机访问网络的第一道防护，但是它们不应该仅有一道屏障。Linux使用了两个文件!。/etc/hosts.allow和/etc/hosts.deny，根据网络请求的来源限制对服务的访问。

hosts.allow文件列出了允许连接到一个特定服务的主机，而hosts.deny文件则负责限制访问。不过，这两个文件只控制对有hosts access功能的服务(如xinetd所管理的那些服务、sshd和某些配置的sendmail)的访问。

**Linux服务器针对固定的IP进行禁止、允许登录:** linux 服务器通过设置/etc/hosts.allow和/etc/hosts.deny这个两个文件进行限制。
- 优先级：hosts.allow大于hosts.deny
### hosts.allow与hosts.deny

hosts.allow可以允许某个或者某段IP地址远程 SSH 登录服务器；hosts.deny可以限制某个或者某段IP地址远程 SSH 登录服务器，方法比较简单，且设置后立即生效，不需要重启服务，具体如下：

```
1.限制所有的ssh
除非从192.168.1.0——127上来。
hosts.deny:
in.sshd:ALL
hosts.allow:
in.sshd:192.168.1.0/255.255.255.128

```

```
2.封掉218.64.87.0——127的telnet
hosts.deny
in.sshd:218.64.87.0/255.255.255.128

```

```
3.限制所有人的TCP连接，除非从192.168.1.0——127访问
hosts.deny
ALL:ALL
hosts.allow
ALL:192.168.1.0/255.255.255.128

```

```
4、允许指定ip访问ssh
vim /etc/hosts.allow
sshd:10.11.10.10x:allow 
sshd:10.11.10.11x:allow 
sshd:10.11.10.10x:allow 

vim /etc/hosts.deny
sshd:all:deny

```
