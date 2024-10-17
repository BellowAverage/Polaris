
--- 
title:  -bash: fork: retry: Resource temporarily unavailable 问题解决 
tags: []
categories: [] 

---
错误提示： -bash: fork: retry: Resource temporarily unavailable

>  
 **错误分析：之前已经出现过这种资源限制的报错提醒，然后整个系统可用的连接数就已经用完了，无法使用工具来获取系统信息，所以将运行的任务脚本kill后开多个窗口，打开top，监控资源，但是当资源限制提示出现后发现cpu和内存还有很多空余，所以猜想是linux资源限制问题。** 


<img alt="" height="1195" src="https://img-blog.csdnimg.cn/71b0f9e9d9e24632aff7f4c0a1332ed7.png" width="1200">

因为是使用root用户跑的任务脚本，每次跑到25000左右，线程数50000左右就会出现资源限制，所以修改ulimit，将一些可能影响资源的限制放开，设置为unlimited或者设置一个较高的上限。

>  
 **修改/etc/security/limits.conf 配置文件，修改软限制和硬限制** 


```
[root@130-171 security]# vim limits.conf   
root soft nofile 655360
root hard nofile 655360
* hard nproc 655350
* soft nproc 655350
```

>  
 **修改/etc/security/limits.d/20-nproc.conf，修改进程数量限制** 


```
[root@130-171 limits.d]# cat 20-nproc.conf 
# Default limit for number of user's processes to prevent
# accidental fork bombs.
# See rhbz #432903 for reasoning.
*          soft    nproc     unlimited
root       soft    nproc     unlimited
*          hard    nproc     unlimited
root       hard    nproc     unlimited
```

修改完以后重启系统生效。

>  
 **查看ulimit资源限制。** 


```
[root@130-171 log]# ulimit -a
core file size          (blocks, -c) unlimited
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 32133
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 655360
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) unlimited
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```

>  
 **继续运行任务程序后发现，资源限制仍然存在。** 
 **查看系统日志/var/log/message 过滤错误信息 fork，发现报错信息。发现是kernel内核cgroup机制限制了资源** 


<img alt="" height="177" src="https://img-blog.csdnimg.cn/60485ea494424e6bbcb2ec97c4c55bdf.png" width="1200">

>  
 **在Linux系统中，用户slice（User Slice）是systemd服务管理器（systemd）用于组织和管理与用户相关的进程的一种机制。每个登录到系统的用户都会有一个对应的用户slice，用于管理该用户的所有进程。** 
 **用户slice的名称通常是user-.slice，其中是用户的实际用户ID。例如，对于用户ID为1000的用户，其用户slice名称可能是user-1000.slice。** 
 **用户slice是systemd中的一个Cgroup（控制组），Cgroups是一种用于管理进程组的机制。Cgroups可以用来限制进程的资源使用，例如CPU、内存和进程数量（PIDs）。用户slice通过Cgroups为每个用户提供一个隔离的环境，使得每个用户的进程可以独立运行，并且资源之间不会互相干扰。** 
 **当用户登录到系统时，systemd会为该用户创建一个对应的用户slice，并将用户的所有进程分配到该slice中。这样，每个用户的进程都会受到用户slice的资源限制。例如，每个用户的进程数量限制（PIDs限制）可以单独设置，这样即使某个用户的进程数量超出了限制，也不会影响其他用户的进程。** 
 **通过用户slice，系统管理员可以更好地管理和控制每个用户的进程，确保系统资源的合理分配和使用。同时，用户slice还可以为每个用户提供一种隔离的环境，防止不同用户之间的进程干扰和影响。** 


>  
 **使用systemctl status user-0.slice 命令查看root用户的slice限制，果然是slice限制了资源。** 


<img alt="" height="404" src="https://img-blog.csdnimg.cn/70e60acdcaba4f4ca15f369b9b1a433e.png" width="730">

>  
 **可以使用命令：systemctl set-property user-0.slice TaskMax=80000来设置limit限制的task数** 


<img alt="" height="258" src="https://img-blog.csdnimg.cn/cabbc2729e4e43deafb868ef8273cd46.png" width="794">

>  
 **然后查看slice状态。发现已经修改完成。** 


<img alt="" height="465" src="https://img-blog.csdnimg.cn/329d88ef18d94af0853606186e32d282.png" width="814">

最后再运行任务程序，发现资源限制问题没有再出现。

>  
 **也可以在/etc/systemd/system.control/user-0.slice.d/50-TasksMax.conf配置文件里面来配置tasksmax参数** 


```
[root@130-171 user-0.slice.d]# vim 50-TasksMax.conf

# This is a drop-in unit file extension, created via "systemctl set-property"

# or an equivalent operation. Do not edit.

[Slice]

TasksMax=200000
```


