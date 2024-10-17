
--- 
title:  Docker - 容器的网络模式 
tags: []
categories: [] 

---
**目录**























**容器的几种网络类型**

>  
 **bridge** 
 **host** 
 **none** 
 **container** 




### 一、bridge模式

>  
 **当Docker进程启动时，会在主机上创建一个名为docker0的虚拟网桥，此主机上启动的Docker容器会连接到这个虚拟网桥上。虚拟网桥的工作方式和物理交换机类似，这样主机上的所有容器就通过交换机连在了一个二层网络中。** 
 **bridge模式是docker的默认网络模式，不写--net参数，就是bridge模式。此模式会为每一个容器分配****Network Namespace****、设置IP等** 
 **使用docker run -p时，docker实际是在iptables做了DNAT规则，实现端口转发功能。可以使用iptables -t nat -vnL查看。** 
 **从docker0子网中分配一个IP给容器使用，并设置docker0的IP地址为容器的默认网关。** 


#### 查看容器的有哪几种网络类型

```
[root@docker1 ~]# docker network ls
NETWORK ID     NAME                   DRIVER    SCOPE
91333e76abbc   bridge                 bridge    local
ad3ad5fc6e99   host                   host      local
ab0e4d5d934b   none                   null      local

```

<img alt="" height="624" src="https://img-blog.csdnimg.cn/171fc6886b724febb67d4fcdd606d395.png" width="1200">



**##################################################################################**

### 二、host模式

>  
 **如果启动容器的时候使用host模式，那么这个容器将不会获得一个独立的Network Namespace，而是和宿主机共用一个Network Namespace。容器将不会虚拟出自己的网卡，配置自己的IP等，而是使用宿主机的IP和端口。但是，容器的其他方面，如文件系统、进程列表等还是和宿主机隔离的。** 
 **使用host模式的容器可以直接使用宿主机的IP地址与外界通信，容器内部的服务端口也可以使用宿主机的端口，不需要进行NAT，host最大的优势就是网络性能比较好，但是docker host上已经使用的端口就不能再用了，网络的隔离性不好。** 


<img alt="" height="579" src="https://img-blog.csdnimg.cn/96a4443266414a4785e5966d0caa889f.png" width="1200">

**##################################################################################** 

### 三、none模式

>  
  **使用none模式，Docker容器拥有自己的Network Namespace，但是，并不为Docker容器进行任何网络配置。** 
 **也就是说，这个Docker容器没有网卡、IP、路由等信息。需要我们自己为Docker容器添加网卡、配置IP等。** 
 **这种网络模式下容器只有lo回环网络，没有其他网卡。none模式可以在容器创建时通过--network=none来指定。** 
 **这种类型的网络没有办法联网，封闭的网络能很好的保证容器的安全性。** 


**##################################################################################**

### 四、container模式

>  
 **container模式就是很多容器共用一个ip地址** 
 **这个模式指定新创建的容器和已经存在的一个容器共享一个 network namespace，而不是和宿主机共享，新创建的容器不会创建自己的网阿卡，配置自己的ip，而是和一个指定的容器共享ip，端口范围等，同样，两个容器除了网络方面，其他的如文件系统，进程列表等还是隔离的，两个容器的进程可以通过lo网卡设备通信 ** 


**##################################################################################**

### 五、overlay模式

>  
 **overlay 网络用语连接不同机器上的docker容器，允许不同机器上的容器相互通信，同时支持对消息进行加密，实现跨主机之间的容器之间的通信** 


**##################################################################################**

```
[root@docker ~]# docker network ls
NETWORK ID     NAME        DRIVER    SCOPE
cc33db32b89e   bridge      bridge    local
ad3ad5fc6e99   host        host      local
ab0e4d5d934b   none        null      local

```

### 创建一个桥接类型的网卡

```
[root@docker ~]# docker network create --driver bridge sc-zhaojj
a3779e26931ff899dafa3ce8cb544954392ab100f751587497a21cd4bfafec58
[root@docker ~]# docker network ls
NETWORK ID     NAME        DRIVER    SCOPE
cc33db32b89e   bridge      bridge    local
ad3ad5fc6e99   host        host      local
ab0e4d5d934b   none        null      local
a3779e26931f   sc-zhaojj   bridge    local

```

**ip add 查看宿主机上的网卡，多出了br-a3779e26931f这个网卡  br ：bridge**

**默认创建的网卡是down状态的，因为还没有创建容器来使用它**

```
[root@docker ~]# ip a
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:08:e7:01 brd ff:ff:ff:ff:ff:ff
    inet 192.168.44.201/24 brd 192.168.44.255 scope global noprefixroute ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fe08:e701/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:59:c3:5a:cd brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:59ff:fec3:5acd/64 scope link 
       valid_lft forever preferred_lft forever
5: vethd6d36ce@if4: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue master docker0 state UP group default 
    link/ether 02:8f:9f:05:22:f6 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::8f:9fff:fe05:22f6/64 scope link 
       valid_lft forever preferred_lft forever
7: vethe1533b3@if6: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue master docker0 state UP group default 
    link/ether 7a:c1:18:68:c4:e2 brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::78c1:18ff:fe68:c4e2/64 scope link 
       valid_lft forever preferred_lft forever
9: veth150a13c@if8: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc noqueue master docker0 state UP group default 
    link/ether ba:71:96:2c:70:59 brd ff:ff:ff:ff:ff:ff link-netnsid 2
    inet6 fe80::b871:96ff:fe2c:7059/64 scope link 
       valid_lft forever preferred_lft forever
10: br-a3779e26931f: &lt;NO-CARRIER,BROADCAST,MULTICAST,UP&gt; mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:9a:59:a1:5c brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-a3779e26931f
       valid_lft forever preferred_lft forever

```

#### 使用刚才创建的网卡来创建容器

```
[root@docker ~]# docker run -d --name wangsh-nginx- -p 9901:80 --network sc-zhaojj  nginx
e61be6dd284f9a69356de22b3fb0a1388f7e3879082218a463d3aa3d83f1e5a9
doc[root@docker ~]# docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                                    NAMES
e61be6dd284f   nginx          "/docker-entrypoint.…"   24 seconds ago   Up 22 seconds   0.0.0.0:9901-&gt;80/tcp, :::9901-&gt;80/tcp                    wangsh-nginx-
53df509efe33   nginx          "/docker-entrypoint.…"   2 days ago       Up 2 days       0.0.0.0:8803-&gt;80/tcp, :::8803-&gt;80/tcp                    yangyj-nginx
3d6aa9a3116b   mysql:5.7.39   "docker-entrypoint.s…"   3 days ago       Up 3 days       33060/tcp, 0.0.0.0:33060-&gt;3306/tcp, :::33060-&gt;3306/tcp   sc-mysql-1
fc652e8c734a   nginx          "/docker-entrypoint.…"   4 days ago       Up 3 days       0.0.0.0:8090-&gt;80/tcp, :::8090-&gt;80/tcp                    sc-nginx

```

#### 查看刚才使用网卡创建的容器的ip地址

>  
 **可以看到，创建容器指定的网卡是 sc-zhaojj，这个网卡的IP地址是172.18.0.1** 


```
10: br-a3779e26931f: &lt;NO-CARRIER,BROADCAST,MULTICAST,UP&gt; mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:9a:59:a1:5c brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-a3779e26931f
       valid_lft forever preferred_lft forever
```

>  
 <h4 id="%E6%88%91%E4%BB%AC%E6%8C%87%E5%AE%9A%E7%BD%91%E5%8D%A1%E5%88%9B%E5%BB%BA%E7%9A%84%E5%AE%B9%E5%99%A8IP%E5%9C%B0%E5%9D%80%E6%98%AF%20%EF%BC%9A172.18.0.2">我们指定网卡创建的容器IP地址是 ：172.18.0.2</h4> 


```
[root@docker ~]# docker network inspect sc-zhaojj | egrep "IP"
        "EnableIPv6": false,
        "IPAM": {
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
[root@docker ~]# 

```


