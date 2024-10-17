
--- 
title:  netstat命令详解 
tags: []
categories: [] 

---
### 1、下载netstat命令对应的软件包

```
yum install net-tools -y

```

### 2、netsta命令介绍

```
[root@vm01 ~]# man netstat


NETSTAT(8)                          Linux System Administrator's Manual                         NETSTAT(8)

NAME
       netstat  - Print network connections, routing tables, interface statistics, masquerade connections,
       and multicast memberships

```

>  
 **netstat命令：输出网络连接，路由表，接口状态，masquerade 连接，** 


### 3、netsta命令参数

```
-r：--route，显示路由表信息
-g：--groups，显示多重广播功能群组组员名单
-s：--statistics，按照每个协议来分类进行统计。默认的显示IP、IPv6、ICMP、ICMPv6、TCP、TCPv6、UDP和UDPv6 的统计信息。
-M：--masquerade，显示网络内存的集群池统计信息
-v：--verbose，命令显示每个运行中的基于公共数据链路接口的设备驱动程序的统计信息
-W：--wide，不截断IP地址
-n：进制使用域名解析功能。链接以数字形式展示(IP地址)，而不是通过主机名或域名形式展示
-N：--symbolic，解析硬件名称
-e：--extend，显示额外信息
-p：--programs，与链接相关程序名和进程的PID
-t：所有的 tcp 协议的端口
-x：所有的 unix 协议的端口
-u：所有的 udp 协议的端口
-o：--timers，显示计时器
-c：--continuous，每隔一个固定时间，执行netstat命令
-l：--listening，显示所有监听的端口
-a：--all，显示所有链接和监听端口
-F：--fib，显示转发信息库(默认)
-C：--cache，显示路由缓存而不是FIB
-Z：--context，显示套接字的SELinux安全上下文
```

###  4、常用组合参数 netstat -anplut

```
[root@zabbix-server ~]# netstat -anplut
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      2690/mysqld         
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1093/sshd           
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      1348/master         
tcp        0      0 0.0.0.0:10050           0.0.0.0:*               LISTEN      37538/zabbix_agentd 
tcp        0      0 0.0.0.0:10051           0.0.0.0:*               LISTEN      41728/zabbix_server 
tcp        0     36 192.168.20.10:22        192.168.20.1:59621      ESTABLISHED 118929/sshd: root@p 
tcp        0      0 127.0.0.1:10050         127.0.0.1:46618         TIME_WAIT   -                   
tcp6       0      0 :::80                   :::*                    LISTEN      3388/httpd          
tcp6       0      0 :::22                   :::*                    LISTEN      1093/sshd           
tcp6       0      0 :::3000                 :::*                    LISTEN      82302/grafana-serve 
tcp6       0      0 ::1:25                  :::*                    LISTEN      1348/master         
tcp6       0      0 :::10050                :::*                    LISTEN      37538/zabbix_agentd 
tcp6       0      0 :::10051                :::*                    LISTEN      41728/zabbix_server 
udp        0      0 127.0.0.1:323           0.0.0.0:*                           704/chronyd         
udp6       0      0 ::1:323                 :::*                                704/chronyd        
```

>  
 **各个字段的含义：** 
 **Proto：指的是协议，例如tcp，udp等** 
 **Recv-Q：表示收到的数据已经在本地接收缓冲，但是还有多少没有被进程取走，recv()如果接收队列Recv-Q一直处于阻塞状态，可能是遭受了拒绝服务 denial-of-service 攻击；** 
 **Send-Q：本地没有发生的数据，如果发送队列Send-Q不能很快的清零，可能是有应用向外发送数据包过快，或者是对方接收数据包不够快；** 
 **Local Address：本地IP：本地端口** 
 **Foreign Address：远程IP：远程端口** 
 **State：链接状态（established，lished等）** 
 **PID：进程PID号** 
 **Program name：程序名字** 


###  5、netstat -rn显示核心路由信息

```
[root@zabbix-server ~]# netstat -rn
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         192.168.20.2    0.0.0.0         UG        0 0          0 ens33
192.168.20.0    0.0.0.0         255.255.255.0   U         0 0          0 ens33

```


