
--- 
title:  服务器TIME_WAIT状态过多如何解决？ 
tags: []
categories: [] 

---
>  
 **最近部署了一台zabbix-server和zabbix-agent，在查看tcp连接的时候显示time_wait巨多** 


```
[root@zabbix-server alertscripts]# netstat -antp
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      2690/mysqld         
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1093/sshd           
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      1348/master         
tcp        0      0 0.0.0.0:10050           0.0.0.0:*               LISTEN      37538/zabbix_agentd 
tcp        0      0 0.0.0.0:10051           0.0.0.0:*               LISTEN      41728/zabbix_server 
tcp        0      0 127.0.0.1:10050         127.0.0.1:50420         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50418         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50566         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50410         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50422         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50404         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50397         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50396         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50530         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50528         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50424         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50430         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50585         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50522         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50494         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50486         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50428         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50510         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50562         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50412         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50514         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50556         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50490         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50402         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50580         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50478         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50436         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50434         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50542         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50406         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50400         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50394         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50540         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50426         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50482         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50578         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50432         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50444         TIME_WAIT   -                   
tcp        0    232 192.168.20.10:22        192.168.20.1:61855      ESTABLISHED 67497/sshd: root@pt 
tcp        0      0 127.0.0.1:10050         127.0.0.1:50520         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50438         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50414         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50488         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50458         TIME_WAIT   -                   
tcp        0      0 192.168.20.10:10051     192.168.20.11:51946     TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50584         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50568         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50546         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50476         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50446         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50448         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50442         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50552         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50560         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50472         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50538         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50498         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50504         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50570         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50416         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50508         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50576         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50518         TIME_WAIT   -                   
tcp        0      0 127.0.0.1:10050         127.0.0.1:50468         TIME_WAIT   -                   
tcp6       0      0 :::80                   :::*                    LISTEN      3388/httpd          
tcp6       0      0 :::22                   :::*                    LISTEN      1093/sshd           
tcp6       0      0 ::1:25                  :::*                    LISTEN      1348/master         
tcp6       0      0 :::10050                :::*                    LISTEN      37538/zabbix_agentd 
tcp6       0      0 :::10051                :::*                    LISTEN      41728/zabbix_server 
tcp6       0      0 192.168.20.10:80        192.168.20.1:52699      TIME_WAIT   -                   
tcp6       0      0 ::1:10051               ::1:34078               TIME_WAIT   -                   
tcp6       0      0 192.168.20.10:80        192.168.20.1:52705      FIN_WAIT2   76819/httpd         
tcp6       0      0 192.168.20.10:80        192.168.20.1:59917      TIME_WAIT   -                   
tcp6       0      0 ::1:10051               ::1:34016               TIME_WAIT   -                   
tcp6       0      0 ::1:10051               ::1:33984               TIME_WAIT   -                   
tcp6       0      0 ::1:10051               ::1:34130               TIME_WAIT   -                   
tcp6       0      0 ::1:10051               ::1:34040               TIME_WAIT   -                   
tcp6       0      0 192.168.20.10:80        192.168.20.1:52700      TIME_WAIT   -   
```

### 解决方法：在/etc/sysctl.conf里面修改两个内核参数

```
vim/etc/sysctl.conf
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1

```

>  
 **参数的意思是打开系统的time_wait的重用和快速回收** 


>  
 **然后执行 sysctl -p使之生效** 


```
[root@zabbix-server alertscripts]# sysctl -p
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1

```

效果：

>  
 **time_wait状态会逐渐减少至正常** 


```
[root@zabbix-server alertscripts]# netstat -anplut
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      2690/mysqld         
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1093/sshd           
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      1348/master         
tcp        0      0 0.0.0.0:10050           0.0.0.0:*               LISTEN      37538/zabbix_agentd 
tcp        0      0 0.0.0.0:10051           0.0.0.0:*               LISTEN      41728/zabbix_server 
tcp        0     36 192.168.20.10:22        192.168.20.1:61855      ESTABLISHED 67497/sshd: root@pt 
tcp6       0      0 :::80                   :::*                    LISTEN      3388/httpd          
tcp6       0      0 :::22                   :::*                    LISTEN      1093/sshd           
tcp6       0      0 ::1:25                  :::*                    LISTEN      1348/master         
tcp6       0      0 :::10050                :::*                    LISTEN      37538/zabbix_agentd 
tcp6       0      0 :::10051                :::*                    LISTEN      41728/zabbix_server 
tcp6       0      0 192.168.20.10:80        192.168.20.1:52842      TIME_WAIT   -                   
tcp6       0      0 192.168.20.10:80        192.168.20.1:52844      ESTABLISHED 76729/httpd         
tcp6       0      0 192.168.20.10:80        192.168.20.1:52843      ESTABLISHED 76775/httpd         
tcp6       0      0 192.168.20.10:80        192.168.20.1:52835      TIME_WAIT   -                   
tcp6       0      0 192.168.20.10:80        192.168.20.1:52839      TIME_WAIT   -                   
tcp6       0      0 192.168.20.10:80        192.168.20.1:52831      TIME_WAIT   -                   
tcp6       0      0 192.168.20.10:80        192.168.20.1:52841      TIME_WAIT   -                   
tcp6       0      0 192.168.20.10:80        192.168.20.1:52826      TIME_WAIT   -                   
tcp6       0      0 192.168.20.10:80        192.168.20.1:52836      TIME_WAIT   -                   
udp        0      0 127.0.0.1:323           0.0.0.0:*                           704/chronyd         
udp6       0      0 ::1:323                 :::*                                704/chronyd       
```


