
--- 
title:  Linux防火墙报错：Failed to start firewalld.service Unit is masked 
tags: []
categories: [] 

---
## Linux防火墙报错：Failed to start firewalld.service: Unit is masked.

### 1、故障现象：

启动防火墙失败，报错情况如下：

```
systemctl start firewalld
# 报错：
Failed to start firewalld.service: Unit is masked.

```

原因是：（启动防火墙失败：防火墙被锁定）

### 2、解决方法：

解锁防火墙：（移除符号链接）

```
systemctl unmask firewalld.service
# 输出如下信息：
Removed symlink /etc/systemd/system/firewalld.service.

```

### 3、再次启动防火墙，查看状态：

```
systemctl start firewalld.service

systemctl status firewalld.service 
● firewalld.service - firewalld - dynamic firewall daemon
   Loaded: loaded (/usr/lib/systemd/system/firewalld.service; disabled; vendor preset: enabled)
   Active: active (running) since Mon 2023-08-21 16:53:18 CST; 1s ago
     Docs: man:firewalld(1)
     .......

```

Active: active (running) 看到这个已经代表启动防火墙了。

### 4、防火墙命令操作：
- 启动服务操作：
```
yum install firewalld  #安装firewalld 防火墙
systemctl start firewalld.service   #开启防火墙
systemctl stop firewalld.service    #关闭防火墙
systemctl enable firewalld.service  # 设置开机自动启动
firewall-cmd --reload  #在不改变状态的条件下重新加载防火墙

```
- 端口、ip限制：（注意：–permanent 是永久设置，没加则为临时）
```
#查看firewalld规则：
firewall-cmd --list-all

# 添加单个IP，允许单个IP访问所有端口：
firewall-cmd --permanent --add-source=192.168.18.6

#允许所有ip访问80端口：
firewall-cmd --add-port=80/tcp

# 允许指定IP访问本机8080端口
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.18.72" port protocol="tcp" port="8080" accept'

# 允许指定IP段访问本机8080-8090端口
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.18.0/24" port protocol="tcp" port="8080-8090" accept'

# 禁止指定IP访问本机8080端口
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.18.10" port protocol="tcp" port="8080" reject'

#移除第一条规则(所有的移除规则基本都是add改成remove)
firewall-cmd --permanent --remove-rich-rule='rule family="ipv4" source address="192.168.18.100" port protocol="tcp" port="8080" accept'

```
- 问题处理：
```
# 解决firewalld添加ip白名单不生效
firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.18.19" accept' --permanent
firewall-cmd --reload

```
