
--- 
title:  DNS域名系统 - CDN内容分发网络 
tags: []
categories: [] 

---
**目录**









































### 知识点1：什么是DNS域名系统

>  
 **DNS（Domain Name System 域名系统）** 
 **早期使用hosts文件解析域名，但这样会导致一些问题** 
 **        主机名称重复** 
 **        主机维护困难** 
 **        hosts文件只能给自己做解析** 


####  DNS系统的作用：

>  
 **        正向解析：根据主机名称（域名）查找对应的IP地址** 
 **        反向解析：根据IP地址查找对应的主机域名** 


#### DNS系统的分布式数据结构

<img alt="" height="524" src="https://img-blog.csdnimg.cn/02462bceee0748fba98e4151935f592f.png" width="980">

**######################################################################################## **  

#### /etc/named/named.ca 文件：13台根域名服务器存放的文件

```
[root@wangsh ~]# cat /var/named/named.ca 

; &lt;&lt;&gt;&gt; DiG 9.11.3-RedHat-9.11.3-3.fc27 &lt;&lt;&gt;&gt; +bufsize=1200 +norec @a.root-servers.net
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 46900
;; flags: qr aa; QUERY: 1, ANSWER: 13, AUTHORITY: 0, ADDITIONAL: 27

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1472
;; QUESTION SECTION:
;.				IN	NS

;; ANSWER SECTION:
.			518400	IN	NS	a.root-servers.net.
.			518400	IN	NS	b.root-servers.net.
.			518400	IN	NS	c.root-servers.net.
.			518400	IN	NS	d.root-servers.net.
.			518400	IN	NS	e.root-servers.net.
.			518400	IN	NS	f.root-servers.net.
.			518400	IN	NS	g.root-servers.net.
.			518400	IN	NS	h.root-servers.net.
.			518400	IN	NS	i.root-servers.net.
.			518400	IN	NS	j.root-servers.net.
.			518400	IN	NS	k.root-servers.net.
.			518400	IN	NS	l.root-servers.net.
.			518400	IN	NS	m.root-servers.net.

;; ADDITIONAL SECTION:
a.root-servers.net.	518400	IN	A	198.41.0.4
b.root-servers.net.	518400	IN	A	199.9.14.201
c.root-servers.net.	518400	IN	A	192.33.4.12
d.root-servers.net.	518400	IN	A	199.7.91.13
e.root-servers.net.	518400	IN	A	192.203.230.10
f.root-servers.net.	518400	IN	A	192.5.5.241
g.root-servers.net.	518400	IN	A	192.112.36.4
h.root-servers.net.	518400	IN	A	198.97.190.53
i.root-servers.net.	518400	IN	A	192.36.148.17
j.root-servers.net.	518400	IN	A	192.58.128.30
k.root-servers.net.	518400	IN	A	193.0.14.129
l.root-servers.net.	518400	IN	A	199.7.83.42
m.root-servers.net.	518400	IN	A	202.12.27.33
a.root-servers.net.	518400	IN	AAAA	2001:503:ba3e::2:30
b.root-servers.net.	518400	IN	AAAA	2001:500:200::b
c.root-servers.net.	518400	IN	AAAA	2001:500:2::c
d.root-servers.net.	518400	IN	AAAA	2001:500:2d::d
e.root-servers.net.	518400	IN	AAAA	2001:500:a8::e
f.root-servers.net.	518400	IN	AAAA	2001:500:2f::f
g.root-servers.net.	518400	IN	AAAA	2001:500:12::d0d
h.root-servers.net.	518400	IN	AAAA	2001:500:1::53
i.root-servers.net.	518400	IN	AAAA	2001:7fe::53
j.root-servers.net.	518400	IN	AAAA	2001:503:c27::2:30
k.root-servers.net.	518400	IN	AAAA	2001:7fd::1
l.root-servers.net.	518400	IN	AAAA	2001:500:9f::42
m.root-servers.net.	518400	IN	AAAA	2001:dc3::35

;; Query time: 24 msec
;; SERVER: 198.41.0.4#53(198.41.0.4)
;; WHEN: Thu Apr 05 15:57:34 CEST 2018
;; MSG SIZE  rcvd: 811

```

 **######################################################################################## ** 

### DNS的记录类型

<img alt="" height="380" src="https://img-blog.csdnimg.cn/8dbd9fc9a6934b55b137f17b960e27cf.png" width="744">

**######################################################################################## **  

####  DNS的解析过程

<img alt="" height="661" src="https://img-blog.csdnimg.cn/8fb7fc2068d84b809d610f3dbc25024a.png" width="957">

>  
 ** 以www.sxkeji.com.cn为例:** 
 **首先客户机会先查看浏览器缓存里面有没有对应的域名解析记录，如果没有就到hosts文件里面查找，如果hosts文件里面没有就到本地域名服务器里面查询，** 
 **如果本地域名服务器里面也没有的话，就到根DNS服务器里面查询，根DNS服务器收到查询后发现是以.cn结尾的，于是就让本地域名服务器去cn服务器查询** 
 **cn服务器发现是以com.cn结尾的，就让本地域名服务器去com.cn服务器查询，com.cn服务器又指向sxkeji.com.cn服务器，sxkeji.com服务器就告诉本地域名服务器www.sxkeji.com  web服务器的IP地址，然后本地域名服务器就告诉客户机这个web服务器的IP地址，然后客户机就可以访问这个服务器。** 


**######################################################################################## **  

### DNS服务器的类型

>  
 **缓存域名服务器** 
 **        也称为高速缓存服务器** 
 **        通过向其他域名查询获得域名 -- ip地址记录** 
 **        将域名查询结果缓存到本地** 
 **主域名服务器** 
 **        特定DNS区域的官方服务器，就有唯一性，权威性** 
 **        负责维护该区域内所有域名 -- ip的映射记录** 
 **从域名服务器** 
 **        也称为辅助域名服务器** 
 **        其维护的 域名 -- ip 地址记录来源于主域名服务器 ** 


**######################################################################################## **

###  知识点2：搭建DNS服务器

#### 1、下载bind软件

```
[root@wangsh ~]# yum install bind -y

```

#### 2、启动

```
[root@wangsh ~]# service named start
Redirecting to /bin/systemctl start named.service

```

#### 3、查看服务有没有启动

>  
 **查询使用UDPP协议** 
 **主从复制使用TCP** 


```
[root@wangsh ~]# ps aux| grep named
named      1541  0.0  5.7 168300 57484 ?        Ssl  11:31   0:00 /usr/sbin/named -u named -c /etc/named.conf
root       1565  0.0  0.0 112824   988 pts/0    R+   11:32   0:00 grep --color=auto named
[root@wangsh ~]# ss -anplut | grep name
udp    UNCONN     0      0      127.0.0.1:53                    *:*                   users:(("named",pid=1541,fd=512))
udp    UNCONN     0      0         [::1]:53                 [::]:*                   users:(("named",pid=1541,fd=513))
tcp    LISTEN     0      10     127.0.0.1:53                    *:*                   users:(("named",pid=1541,fd=21))
tcp    LISTEN     0      128    127.0.0.1:953                   *:*                   users:(("named",pid=1541,fd=23))
tcp    LISTEN     0      10        [::1]:53                 [::]:*                   users:(("named",pid=1541,fd=22))
tcp    LISTEN     0      128       [::1]:953                [::]:*                   users:(("named",pid=1541,fd=24))

```

#### 4、验证本机能否作为dns服务器提供域名解析

>  
 **首先修改本机的resolv.conf文件，这个文件存放了DNS客户机的一些配置** 
 **默认应该是114.114.114.114，我们将它修改成127.0.0.1，让它使用我们本机作为dns服务器** 


```
[root@wangsh ~]# vim /etc/resolv.conf
nameserver 127.0.0.1

```

**然后ping一下www.baidu.com看能否上网，如果ping的通就表示我们刚才配置的dns服务器是可以使用的**

```
[root@wangsh ~]# ping 114.114.114.114
PING 114.114.114.114 (114.114.114.114) 56(84) bytes of data.
64 bytes from 114.114.114.114: icmp_seq=1 ttl=128 time=30.6 ms
64 bytes from 114.114.114.114: icmp_seq=2 ttl=128 time=28.4 ms
^C
--- 114.114.114.114 ping statistics ---
3 packets transmitted, 2 received, 33% packet loss, time 2008ms
rtt min/avg/max/mdev = 28.427/29.523/30.620/1.109 ms
[root@wangsh ~]# ping www.baidu.com
PING www.a.shifen.com (14.215.177.38) 56(84) bytes of data.
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=1 ttl=128 time=35.8 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=2 ttl=128 time=33.0 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=3 ttl=128 time=32.1 ms
^C
--- www.a.shifen.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2702ms
rtt min/avg/max/mdev = 32.125/33.676/35.833/1.573 ms

```

但是目前我们的dns服务器只能给自己的机器做域名解析

**######################################################################################## ** 

### 知识点3：如何让别的机器也能使用我们的dns服务器？

#### 1、修改/etc/named.conf文件

默认配置：

<img alt="" height="257" src="https://img-blog.csdnimg.cn/b3e361bc926248939cab82674470e6b7.png" width="1098">

>  
 ** 将监听端口和ip地址都修改为any** 
 **默认只允许本机来查询，将allow-query也修改为any，允许任何机器访问** 


修改后的配置：

<img alt="" height="250" src="https://img-blog.csdnimg.cn/2c4e3ba2d5194cdda376fa2ecb41ca95.png" width="1038">

####  2、刷新服务，关闭防火墙和selinux

```
[root@wangsh ~]# service named restart
Redirecting to /bin/systemctl restart named.service
[root@wangsh ~]# service firewalld stop
Redirecting to /bin/systemctl stop firewalld.service
[root@wangsh ~]# setenforce 0
[root@wangsh ~]# getenforce 
Permissive


```

#### 3、测试

>  
 **使用一台linux服务器，修改/etc/resolv.conf文件，指定刚才配置的dns服务器，发现任然可以正常上网** 


```
[root@nginx-server ~]# vim /etc/resolv.conf 
nameserver 192.168.44.132

```

```
[root@nginx-server ~]# ping 114.114.114.114
PING 114.114.114.114 (114.114.114.114) 56(84) bytes of data.
64 bytes from 114.114.114.114: icmp_seq=1 ttl=128 time=27.9 ms
^C
--- 114.114.114.114 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 27.951/27.951/27.951/0.000 ms
[root@nginx-server ~]# ping www.baidu.com
PING www.a.shifen.com (14.215.177.38) 56(84) bytes of data.
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=1 ttl=128 time=45.2 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=2 ttl=128 time=32.3 ms
64 bytes from 14.215.177.38 (14.215.177.38): icmp_seq=3 ttl=128 time=143 ms
^C
--- www.a.shifen.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 3016ms
rtt min/avg/max/mdev = 32.384/73.648/143.321/49.544 ms

```

**######################################################################################## **

### 知识点4：dig命令，nslookup命令，host命令

>  
 **dig是一个用于查询DNS名称服务器的灵活工具** 


```
[root@wangsh ~]# dig www.baidu.com

; &lt;&lt;&gt;&gt; DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.9 &lt;&lt;&gt;&gt; www.baidu.com
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 37874
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;www.baidu.com.			IN	A

;; ANSWER SECTION:
www.baidu.com.		941	IN	CNAME	www.a.shifen.com.
www.a.shifen.com.	189	IN	A	14.215.177.39
www.a.shifen.com.	189	IN	A	14.215.177.38

;; Query time: 26 msec
;; SERVER: 114.114.114.114#53(114.114.114.114)
;; WHEN: 五 9月 09 15:31:30 CST 2022
;; MSG SIZE  rcvd: 101

```

>  
 **nslookup命令是一个查询dns域名服务器的程序** 


```
[root@wangsh ~]# nslookup www.baidu.com
Server:		114.114.114.114
Address:	114.114.114.114#53

Non-authoritative answer:
www.baidu.com	canonical name = www.a.shifen.com.
Name:	www.a.shifen.com
Address: 14.215.177.38
Name:	www.a.shifen.com
Address: 14.215.177.39

```

>  
 **host是一个执行DNS查找的简单实用程序。 ** 


```
[root@wangsh ~]# host www.baidu.com
www.baidu.com is an alias for www.a.shifen.com.
www.a.shifen.com has address 14.215.177.38
www.a.shifen.com has address 14.215.177.39
[root@wangsh ~]# host www.jd.com
www.jd.com is an alias for www.jd.com.gslb.qianxun.com.
www.jd.com.gslb.qianxun.com is an alias for www.jdcdn.com.
www.jdcdn.com is an alias for img20.360buyimg.com.s.galileo.jcloud-cdn.com.
img20.360buyimg.com.s.galileo.jcloud-cdn.com is an alias for img20.jcloud-cdn.com.
img20.jcloud-cdn.com has address 175.6.49.3

```

**######################################################################################## **

### 知识点5：什么是CDN？

>  
 **CDN的全称是Content Delivery Network，即内容分发网络，CDN是构建的现有网络基础之上的智能虚拟网络，依靠部署在全国各地的边缘服务器，通过中心平台的负载均衡，内容分发，调度等功能模块，使用户就近获取所需内容，降低网络拥塞，提高用户访问响应速度和命中率，CDN的关键技术主要有内容存储和分发技术** 


#### CDN的优势

>  
 **1、提高网站访问速度和提高用户访问的成功性** 
 **2、加强网站的安全和源站的安全** 
 **3、可扩展性高，突发或者意外情况扩展速度快** 
 **4、维护成本低** 



