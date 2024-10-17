
--- 
title:  prometheus监控软件的使用 
tags: []
categories: [] 

---
**目录**













































































### 知识点1：为什么需要监控？

>  
 **运维工作离不开监控**  
 **工具或者软件去帮助我们7*24监控我们的服务器和软件，是否还在正常的工作。如果不工作，马上告警（短信，电话，微信，钉钉），及时处理。 监控的价值： 防范事故与未然，减少事故带来的损失。 及时的发现问题，提醒工程师尽快的去解决问题，减少公司的损失             提升了产品的品质，增强了用户的信任** 


#### 一些常见的监控软件：

>  
 **1、cacti 仙人掌：出图比较好** 
 **2、nagios 监控脚本特别多** 
 **3、zabbix 集合cacti + nagios 的优点，企业里面用的很多** 
 **4、openfalcon  小米公司开源的监控软件** 
 **5、prometheus：开源的监控软件 ** 


**#############################################################################**

### 知识点2：prometheus 架构图 

<img alt="" height="739" src="https://img-blog.csdnimg.cn/8110cca056774cb3b5aeefcbc416562c.png" width="1200">

#### prometheus的组件

>  
 **1、tsdb：时序数据库** 
 **2、http server  web服务** 
 **3、pushgateway 中间件** 
 **4、alertmanager 告警的软件** 
 **5、exporter 收集数据，采集数据， ** 


#### prometheus获取数据的方式：

>  
 **1、pull server  --》pull --》client  主动的获取数据，避免大并发** 
 **2、push client --》push --》server  client 主动送数据过来，数据会非常新，会出现大量的数据同时push过来 ** 


**#############################################################################**

### 知识点3：使用容器起一个prometheus

```
[root@docker1 ~]# docker run -d -p 9090:9090 --name sc-prom-1 prom/prometheus
78c98ae2bbbb01ee70a9aa70755b463d21214bcac333221d06afc740b0567ecd
[root@docker1 ~]# docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS              PORTS                                       NAMES
78c98ae2bbbb   prom/prometheus        "/bin/prometheus --c…"   6 seconds ago   Up 5 seconds        0.0.0.0:9090-&gt;9090/tcp, :::9090-&gt;9090/tcp   sc-prom-1
ff30f9bc303c   wordpress:latest       "docker-entrypoint.s…"   37 hours ago    Up About a minute   0.0.0.0:80-&gt;80/tcp, :::80-&gt;80/tcp           my_wordpress-wordpress-1
c89b08470516   mariadb:10.6.4-focal   "docker-entrypoint.s…"   37 hours ago    Up About a minute   3306/tcp, 33060/tcp                         my_wordpress-db-1

```

#### 查看prometheus web端

<img alt="" height="740" src="https://img-blog.csdnimg.cn/c3ea2bf7abf54a69a87f3e9fba2d45c3.png" width="1200">

>  
 ** 默认是采集本机的数据** 
 **grafana 是非常专业的出图软件： 专门从别的数据库里抽取数据，然后通过图形展示工具，显示出来** 


**#############################################################################**

####  访问prometheus(localhost:9090/metrics) 

<img alt="" height="968" src="https://img-blog.csdnimg.cn/96e56156cdf64a098c26b7b8bdf3128d.png" width="1200">

 **#############################################################################**

### 知识点4：源码安装prometheus

#### 1、上传下载的源码包到linux机器

>  
 **准备两台linux服务器** 
 **一台为prometheus服务器** 


```
[root@prometheus ~]# ip a
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:a8:02:38 brd ff:ff:ff:ff:ff:ff
    inet 192.168.44.160/24 brd 192.168.44.255 scope global noprefixroute ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fea8:238/64 scope link 
       valid_lft forever preferred_lft forever

```

>  
 **一台为node节点服务器** 


```
[root@node_exporter ~]# ip a
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:37:b5:82 brd ff:ff:ff:ff:ff:ff
    inet 192.168.44.140/24 brd 192.168.44.255 scope global noprefixroute ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fe37:b582/64 scope link 
       valid_lft forever preferred_lft forever

```

>  
 ** 在prometheus服务器上面新建一个目录，并把prometheus源码包上传到这个目录下面** 


<img alt="" height="164" src="https://img-blog.csdnimg.cn/2dfff1561f9843b4a46b6e2653f05b15.png" width="987">

####  2、解压源码包，并重命名

<img alt="" height="258" src="https://img-blog.csdnimg.cn/8ccf0ba42b9d48328a9e0daa47d79df9.png" width="1191">

####  3、修改PATH变量

>  
 **永久修改可以在家目录下面的.bashrc里面添加PATH变量** 


```
[root@prometheus prometheus]# vim /root/.bashrc 
PATH=/prometheus/prometheus:$PATH

```

####  4、启动prometheus程序

>  
 **nohup ：屏蔽hup信号， &amp;将程序放到后台运行** 
 **--config.file=prometheus.yml  指定prometheus配置文件** 


```
[root@prometheus prometheus]# nohup ./prometheus --config.file=prometheus.yml &amp;
[1] 1773
[root@prometheus prometheus]# nohup: 忽略输入并把输出追加到"nohup.out"

[root@prometheus prometheus]# 
[root@prometheus prometheus]# jobs
[1]+  运行中               nohup ./prometheus --config.file=prometheus.yml &amp;

```

####  5、测试访问(默认是采集自己机器的数据)

<img alt="" height="750" src="https://img-blog.csdnimg.cn/4a4994a0fa6b4f42935336815dcdc8b7.png" width="1200">

<img alt="" height="956" src="https://img-blog.csdnimg.cn/c3af746c8eb243869ec4a80aa1ef955f.png" width="1200">

**#############################################################################** 

###  知识点5：采集不同机器的数据

>  
 **首先要在node节点机器上面安装node_exporter软件** 
 **上传node_exporter软件到节点机器上** 


#### 1、上传node_exporter软件，解压，并且重命令 

```
[root@node_exporter /]# mkdir node_exporter
[root@node_exporter /]# cd node_exporter/
[root@node_exporter node_exporter]# ls
node_exporter-1.4.0-rc.0.linux-amd64.tar.gz
[root@node_exporter node_exporter]# tar xf node_exporter-1.4.0-rc.0.linux-amd64.tar.gz 
[root@node_exporter node_exporter]# ls
node_exporter-1.4.0-rc.0.linux-amd64  node_exporter-1.4.0-rc.0.linux-amd64.tar.gz
[root@node_exporter node_exporter]# mv node_exporter-1.4.0-rc.0.linux-amd64 node_exporter
[root@node_exporter node_exporter]# ls
node_exporter  node_exporter-1.4.0-rc.0.linux-amd64.tar.gz
[root@node_exporter node_exporter]# 

```

#### 2、修改PATH变量

```
[root@node_exporter node_exporter]# vim /root/.bashrc 
PATH=/node_exporter/:$PATH

```

#### 3、执行node_exporter 代理程序

```
[root@node_exporter node_exporter]# cd node_exporter
[root@node_exporter node_exporter]# ls
LICENSE  node_exporter  NOTICE
[root@node_exporter node_exporter]# nohup ./node_exporter --web.listen-address 0.0.0.0:8080 &amp;
[1] 21107
[root@node_exporter node_exporter]# nohup: 忽略输入并把输出追加到"nohup.out"

```

>  
 **测试访问node_exporter程序运行情况** 


<img alt="" height="329" src="https://img-blog.csdnimg.cn/90e41d49bd404fa2b66f7987c4ec8d94.png" width="1200">

<img alt="" height="822" src="https://img-blog.csdnimg.cn/9dab20e24666489eb41109bd96a12645.png" width="1200">

#### 4、在prometheus服务器上面添加抓取数据的配置，添加node节点服务器，将抓取的数据存储到时序数据库里面

>  
 **修改prometheus.yml配置文件，添加node节点信息** 


<img alt="" height="261" src="https://img-blog.csdnimg.cn/108cb98c331945039275ee7821248975.png" width="1200">

####  5、修改了配置文件以后刷新prometheus服务

```
[root@prometheus prometheus]# ps aux|grep prometheus
root       1773  0.0  5.5 782340 55088 pts/1    Sl   17:10   0:01 ./prometheus --config.file=prometheus.yml
root       1831  0.0  0.0 112824   992 pts/1    R+   17:50   0:00 grep --color=auto prometheus
[root@prometheus prometheus]# kill -9  1773
[root@prometheus prometheus]# ps aux|grep prometheus
root       1833  0.0  0.0 112824   988 pts/1    R+   17:51   0:00 grep --color=auto prometheus
[1]+  已杀死               nohup ./prometheus --config.file=prometheus.yml
[root@prometheus prometheus]# nohup ./prometheus --config.file=prometheus.yml &amp;
[1] 1834
[root@prometheus prometheus]# nohup: 忽略输入并把输出追加到"nohup.out"

[root@prometheus prometheus]# 

```

#### 6、查看prometheus服务器上面 

 <img alt="" height="552" src="https://img-blog.csdnimg.cn/aca5a21bf2534225b499af89032fecc1.png" width="1200">

 <img alt="" height="794" src="https://img-blog.csdnimg.cn/dacbb413d7674419a63804087f96ddf4.png" width="1200">

 <img alt="" height="709" src="https://img-blog.csdnimg.cn/41980652e1d34f89883edef13ea549d0.png" width="1200">

<img alt="" height="978" src="https://img-blog.csdnimg.cn/99c41206da0d41acb6eacdafa6f67287.png" width="1200">

**############################################################################### **

###  知识点6：grafana 可视化监控指标展示工具

>  
 **概述--  美观、强大的可视化监控指标展示工具 grafana 是一款采用 go 语言编写的开源应用，主要用于大规模指标数据的可视化展现，是网络架构和应用分析中最流行的时序数据展示工具，目前已经支持绝大部分常用的时序数据库**  


####  1、下载grafana，上传到linux服务器

>  
 **官方是使用 wget来下载，但是这样速度太慢，所以选择直接将下载好的软件包传到linux服务器，然后使用yum安装 ** 


```
[root@prometheus /]# mkdir /grafana
[root@prometheus /]# cd grafana/
[root@prometheus grafana]# ls
grafana-enterprise-8.4.5-1.x86_64.rpm
[root@prometheus grafana]# yum install grafana-enterprise-8.4.5-1.x86_64.rpm 

```

####  2、启动grafana服务（service grafana-server start）

```
[root@prometheus grafana]# service grafana-server  start 
Starting grafana-server (via systemctl):                   [  确定  ]

```

查看端口

```
[root@prometheus grafana]# netstat -anplut | grep grafana
tcp6       0      0 :::3000                 :::*                    LISTEN      2165/grafana-server 

```

#### 3、在浏览器访问，登陆

>  
 **第一次登陆默认用户名admin，密码也是admin** 
 **登陆后会要求重置密码 ** 


<img alt="" height="884" src="https://img-blog.csdnimg.cn/d8a6099df27946b183700b5ea1e6ba0d.png" width="1200">

登陆成功页面：

<img alt="" height="893" src="https://img-blog.csdnimg.cn/d5bc9bc3401a4ff1b05db71c7b40d393.png" width="1200">

####  4、添加数据源

<img alt="" height="908" src="https://img-blog.csdnimg.cn/a6c0de2e7df4469fa8d5acaccf4bf552.png" width="1200">

<img alt="" height="871" src="https://img-blog.csdnimg.cn/8f27781ed6794db5812d6cd6de694911.png" width="1200">

<img alt="" height="816" src="https://img-blog.csdnimg.cn/5faabfa71c2647e7b30a8db2bf555933.png" width="1200">

 <img alt="" height="358" src="https://img-blog.csdnimg.cn/cf2fb0396ed54ed6a043d2d9fa936dd6.png" width="872">

>  
 **创建一个新的平板 （panel）** 


<img alt="" height="613" src="https://img-blog.csdnimg.cn/775b37ad774943d7b5f2a54b714f19ef.png" width="1200">

示例：开启cpu监控图 

 <img alt="" height="914" src="https://img-blog.csdnimg.cn/f4ecac383d264586ab794ea0d0a91fcc.png" width="1200">

 可以添加多个平板来监控多个性能

<img alt="" height="821" src="https://img-blog.csdnimg.cn/8d0c484729084fe99b5338a5bf3ef016.png" width="1200">

###  知识点7：grafana使用模板

** 导入别人已经写好了的grafana显示模板**

<img alt="" height="927" src="https://img-blog.csdnimg.cn/624be5807759441095d9ff4d91e26766.png" width="1200">

<img alt="" height="878" src="https://img-blog.csdnimg.cn/40fabea837a147a98f656989b40cec3a.png" width="1200">

#### <img alt="" height="977" src="https://img-blog.csdnimg.cn/dbbfcde0a4d9407c9f955c0ba93a92b4.png" width="1200">获取prometheus数据的流程

 <img alt="" height="522" src="https://img-blog.csdnimg.cn/b535d6beb81049768d7e4594b0aeb64e.png" width="1200">



**#############################################################################** 

### 知识点7：使用prometheus监控容器

 需要一台docker宿主机，使用docker容器来安装prometheus

#### 1、首先安装好compose容器编排工具

```
[root@docker1 ~]# docker compose version
Docker Compose version v2.7.0

```

####  2、新建prometheus.yml文件

```
[root@docker1 prom_docker]# vim prometheus.yml

```

```
[root@docker1 prom_docker]# cat prometheus.yml 
scrape_configs:
- job_name: cadvisor
  scrape_interval: 5s
  static_configs:
  - targets:
    - cadvisor:8080

```

#### 3、新建docker-compose.yml文件

```
version: '3.2'
services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
    - 9090:9090
    command:
    - --config.file=/etc/prometheus/prometheus.yml
    volumes:
    - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
    depends_on:
    - cadvisor
  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    container_name: cadvisor
    ports:
    - 8080:8080
    volumes:
    - /:/rootfs:ro
    - /var/run:/var/run:rw
    - /sys:/sys:ro
    - /var/lib/docker/:/var/lib/docker:ro
    depends_on:
    - redis
  redis:
    image: redis:latest
    container_name: redis
    ports:
    - 6379:6379
```

####  4、上传cadvisor.tar镜像文件，然后导入

<img alt="" height="365" src="https://img-blog.csdnimg.cn/72573a6fda1142299486239f2988d48c.png" width="1200">

####  5、启动docker compose容器

<img alt="" height="163" src="https://img-blog.csdnimg.cn/bc9ab7eb7e674573aaa5a3835cc1528c.png" width="1200">

 docker ps查看要起的容器都有没有起来

```
[root@docker1 prom_docker]# docker ps
CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS                            PORTS                                       NAMES
f57a714dfc4f   prom/prometheus:latest            "/bin/prometheus --c…"   7 seconds ago   Up 5 seconds                      0.0.0.0:9090-&gt;9090/tcp, :::9090-&gt;9090/tcp   prometheus
c13d7f40485f   gcr.io/cadvisor/cadvisor:latest   "/usr/bin/cadvisor -…"   7 seconds ago   Up 6 seconds (health: starting)   0.0.0.0:8080-&gt;8080/tcp, :::8080-&gt;8080/tcp   cadvisor
5912de449c1b   redis:latest                      "docker-entrypoint.s…"   7 seconds ago   Up 6 seconds                      0.0.0.0:6379-&gt;6379/tcp, :::6379-&gt;6379/tcp   redis

```

#### 6、访问cAdvisor 

<img alt="" height="872" src="https://img-blog.csdnimg.cn/603b6173d73c4719ab0deed950bd665f.png" width="1116">

 <img alt="" height="788" src="https://img-blog.csdnimg.cn/15399e6b31ed48f7a30e73ca305b9310.png" width="917">

<img alt="" height="655" src="https://img-blog.csdnimg.cn/986d45d6933347ee805a0d206b6db43e.png" width="725">

####  7、访问prometheus

<img alt="" height="551" src="https://img-blog.csdnimg.cn/c51b01cc6edc41339756a0e3b0ae0f40.png" width="1200">

**#############################################################################** 

### 知识点8：通过容器启动grafana

```
[root@docker1 prom_docker]# docker run -d -p 3001:3000 --name sc-grafana-1 grafana/grafana
Unable to find image 'grafana/grafana:latest' locally
latest: Pulling from grafana/grafana
9621f1afde84: Pull complete 
aba763cacd71: Pull complete 
d588f11a2a4a: Pull complete 
6b06ae62306b: Pull complete 
5f08e1bd5268: Pull complete 
e4bb29e6519a: Pull complete 
e38f4bb1b844: Pull complete 
d6ab276483db: Pull complete 
af0fb383295b: Pull complete 
Digest: sha256:3fe0cb0a7994a1b720f5d597e2043ee00ad2a5892e1a9280d895b5365fb55777
Status: Downloaded newer image for grafana/grafana:latest
80041e78b1a6bbd60689122e3d6eb6d55d34799ba4d98d0db2cf6624ccee2c48

```

测试访问：

<img alt="" height="979" src="https://img-blog.csdnimg.cn/d92155f27a304cd8bc2afe826e1f7d03.png" width="1200">

 

 
