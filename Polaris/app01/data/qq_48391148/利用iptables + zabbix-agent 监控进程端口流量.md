
--- 
title:  利用iptables + zabbix-agent 监控进程端口流量 
tags: []
categories: [] 

---
>  
 **这几天部署了一台ARM架构的linux系统的监控，服务器系统上没有任何工具可以获取数据来获取端口流量，yum，apt-get软件包管理工具都没有，所以想获取数据比较困难。** 
 **最终决定使用iptables来添加几条指定端口的规则来统计入站流量和出站流量** 


### 入站流量在INPUT上添加

监控10010端口的入站流量情况，注意不要加动作，不要影响系统原有iptables规则

```
iptables -A INPUT -p tcp --dport 10010

```

### 出站流量在OUTPUT上添加

```
iptables -A OUTPUT -p tcp --sport 10010
```

### 查看10010端口入站流量情况

```
iptables -nvL INPUT -x

Chain INPUT (policy ACCEPT 260 packets, 30519 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
       260        30519            tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:10010

```

### 查看10010端口出站流量情况

```
iptables -nvL OUTPUT -x 

Chain OUTPUT (policy ACCEPT 163 packets, 10513 bytes)
    pkts      bytes target     prot opt in     out     source               destination         
       163        10513            tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp spt:10010

```

### 添加zabbix-agent自定义Userparameter

```
vim /etc/zabbix/etc/zabbix_agentd.conf

UserParameter=process_10010_in,sudo iptables -vnL INPUT -x |grep 10010|awk '{print $2}'
UserParameter=process_6379_out,sudo iptables -vnL OUTPUT -x |grep 10010|awk '{print $2}'


然后重启zabbix-agent服务

sbin/zabbix_agentd -c /etc/zabbix_agentd.conf

```

### 在zabbixWEB端添加监控项

>  
 **依次添加要监控的监控项即可** 


<img alt="" height="536" src="https://img-blog.csdnimg.cn/5fdc8d232c0043568f2c0da12085a33d.png" width="1135">

 <img alt="" height="266" src="https://img-blog.csdnimg.cn/da18038287a0427887c406acfd2f0244.png" width="973">

 

 

 
