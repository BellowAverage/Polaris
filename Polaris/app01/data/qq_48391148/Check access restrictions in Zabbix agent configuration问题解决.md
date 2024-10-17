
--- 
title:  Check access restrictions in Zabbix agent configuration问题解决 
tags: []
categories: [] 

---
>  
 **今天在使用功能zabbix get 测试与zabbix agent连通性的时候，发现zabbix get访问被拒绝，如图** 


```
[root@localhost zabbix]# zabbix_get -s 192.168.20.10 -p 10050 -k "system.cpu.load[all,avg1]"
zabbix_get [37745]: Check access restrictions in Zabbix agent configuration

```

>  
 **排查了一下，查看zabbix-agent的日志发现因为我的zabbix server和zabbix agent安装在同一台服务器上面，不允许使用ip访问，要改成127.0.0.1.** 


<img alt="" height="463" src="https://img-blog.csdnimg.cn/f6368a119aaf45baa39d15ebb693b576.png" width="1200">

>  
 ** 改了以后zabbix get 就可以成功获取数据了。** 


```
[root@localhost zabbix]# zabbix_get -s 127.0.0.1 -p 10050 -k "system.cpu.load[all,avg1]"
0.000000
[root@localhost zabbix]# zabbix_get -s 127.0.0.1 -p 10050 -k "system.hostname"
localhost.localdomain
[root@localhost zabbix]# zabbix_get -s 127.0.0.1 -p 10050 -k "system.uname"
Linux localhost.localdomain 3.10.0-1160.el7.x86_64 #1 SMP Mon Oct 19 16:18:59 UTC 2020 x86_64
[root@localhost zabbix]# 

```


