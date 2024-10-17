
--- 
title:  基于kafka的日志收集分析平台 
tags: []
categories: [] 

---
**目录**













































































## **基于kafka的日志收集分析平台架构图**

<img alt="" height="590" src="https://img-blog.csdnimg.cn/4c3a8b32f6b14e77af4e29e9a5c6bd02.png" width="1200">

## ** 数据走向流程**

<img alt="" height="126" src="https://img-blog.csdnimg.cn/3d5d428d60a84c3cb3977f65d049fac8.png" width="1171">



## 一、项目目的

        主要是为了模拟企业在大数据背景下的日志收集、存储，分析，消费等流程。

## 二、项目环境

Windows10机器（测试用）、Linux（centos7）、Nginx（1.20.1）、Filebeat（7.17.5）、kafka（1.12）、zookeeper（3.6.3）、Pycharm2020.3、mysql（5.7.34）

## 三、项目步骤

### 准备好3台虚拟机搭建nginx集群

#### 配置好三台nginx机器的静态ip地址，防止dhcp模式动态获得ip地址对我们服务器造成影响

<img alt="" height="264" src="https://img-blog.csdnimg.cn/e0753acaa8df478e96584f50dfe22797.png" width="1094">

<img alt="" height="247" src="https://img-blog.csdnimg.cn/768994ac188c4afcb049a7c82406e709.png" width="1090">

<img alt="" height="231" src="https://img-blog.csdnimg.cn/22eb6a1f67be4b8bbe36edfeda6d478a.png" width="1099">

#### 三台机器都配置好dns

<img alt="" height="100" src="https://img-blog.csdnimg.cn/70d1e6aade0341798203ad09cc29900b.png" width="1097">

####  dns解析顺序：

>  
       1、浏览器的缓存       2、本地hosts文件  --linux（/etc/hosts）       3、找本地域名服务器  -- linux（/etc/resolv.conf） 


#### 修改主机名

```
[root@nginx-kafka01 /]# cat /etc/hostname 
nginx-kafka01

```

```
[root@nginx-kafka02 ~]# cat /etc/hostname 
nginx-kafka02

```

```
[root@nginx-kafka03 ~]# cat /etc/hostname
nginx-kafka03

```

#### 每一台机器上面写好域名解析

```
[root@nginx-kafka01 /]# cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.44.181 nginx-kafka01
192.168.44.182 nginx-kafka02
192.168.44.183 nginx-kafka03

```

#### 安装基本软件，解决依赖关系

```
   yum install wget lsof vim -y
```

#### 安装时间同步服务

```

    yum -y install chrony
```

设置开机自启，然后开机服务

```
	vim /etc/selinux/config
	SELINUX=disabled
```

```
systemctl enable chronyd
```

```
systemctl start chronyd
```

#### 关闭防火墙

```
    [root@nginx-kafka01 ~]# systemctl stop firewalld
    [root@nginx-kafka01 ~]# systemctl disable firewalld
```

#### 关闭selinux

selinux是linux里面的一个安全子系统，里面有许多关于安全的规则，很麻烦，会影响项目运行。

```
	vim /etc/selinux/config
	SELINUX=disabled
```

        selinux关闭 需要重启机器才能生效，可以看到selinux处于禁用状态

```
[root@nginx-kafka01 /]# getenforce
Disabled

```

#### nginx搭建

安装好epel源，本次nginx安装使用yum安装，以一台机器示例：

```
yum install epel-release -y
yum install  nginx -y
```

设置开机自启

```
systemctl enable nginx
```

启动nginx服务

```
systemctl start nginx
```

查看nginx是否启动成功

```
[root@nginx-kafka01 /]# ps aux | grep nginx
root       2098  0.0  0.0  40056   984 ?        Ss   7月24   0:00 nginx: master process /usr/sbinnginx
nginx      2179  0.0  0.0  40060  1180 ?        S    7月24   0:00 nginx: worker process

```

#### nginx配置文件修改

```
vim   nginx.conf

将 
   listen       80 default_server;
修改成：
   listen       80；
```

#### 新建我们的配置文件

```
vim  /etc/nginx/conf.d/sc.conf

server {
    listen 80 default_server;
    server_name  www.sc.com;

    root         /usr/share/nginx/html;

    access_log  /var/log/nginx/sc/access.log main;

    location  / {

    }
}

```

#### 语法检测，检测配置文件语法是否正确

```
[root@nginx-kafka01 html]# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: [emerg] open() "/var/log/nginx/sc/access.log" failed (2: No such file or directory)
nginx: configuration file /etc/nginx/nginx.conf test failed
[root@nginx-kafka01 html]# mkdir /var/log/nginx/sc
[root@nginx-kafka01 html]# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful

#重新加载nginx
nginx -s  reload

```

### 使用三台虚拟机搭建kafka和zookeeper集群

以一台机器示例

#### 安装java和kafka

```
yum install java wget  -y
```

```
wget   https://mirrors.bfsu.edu.cn/apache/kafka/2.8.1/kafka_2.12-2.8.1.tgz 
```

解压缩

```
tar  xf  kafka_2.12-2.8.1.tgz
```

#### 配置kafka

修改config /server.properties：

设置broker节点，这代表这台kafka机器

```
broker.id=1

```

```
zookeeper.connect=192.168.44.181:2181,192.168.44.182:2181,192.168.44.183:2181

```

#### 配置zookeeper

进入安装zookeeper的目录

将配置文件copy一份然后改名为zoo.cfg添加如下三行

```
server.1=192.168.0.94:3888:4888
server.2=192.168.0.95:3888:4888
server.3=192.168.0.96:3888:4888
```

3888和4888都是端口  一个用于数据传输，一个用于检验存活性和选举

创建/tmp/zookeeper目录 ，在目录中添加myid文件，文件内容就是本机指定的zookeeper id内容 如：在192.168.44.181机器上 echo 1 &gt; /tmp/zookeeper/myid

myid里面的id号要和broker节点号一致，分别设置三台机器。

**查看三台zookeeper的leader和follower情况**

**可以看到我设置的kafka02是leader，kafka01和kafka03是follower**

<img alt="" height="135" src="https://img-blog.csdnimg.cn/bb48dab62a134255989dd926c771acdf.png" width="1096">

<img alt="" height="156" src="https://img-blog.csdnimg.cn/a46b43c5564a426ca8fbc867f066d587.png" width="1096">

<img alt="" height="154" src="https://img-blog.csdnimg.cn/ee45d983d7794837afbba31a7d35f0db.png" width="1092">

#### 启动kafka

```
bin/kafka-server-start.sh -daemon config/server.properties
```

#### 启动zookeeper

```
[root@nginx-kafka01 bin]# ./zkCli.sh 

```

 此时我们应该看到三个brokers的id

```
[zk: localhost:2181(CONNECTED) 3] ls /
[admin, brokers, cluster, config, consumers, controller, controller_epoch, feature, isr_change_notification, latest_producer_id_block, log_dir_event_notification, sc, zookeeper]
[zk: localhost:2181(CONNECTED) 4] ls /brokers/ids
[1, 2, 3]

```

创建broker

```
[zk: localhost:2181(CONNECTED) 3] create /sc/yy
Created /sc/yy
[zk: localhost:2181(CONNECTED) 4] ls /sc
[page, xx, yy]
[zk: localhost:2181(CONNECTED) 5] set /sc/yy 90
[zk: localhost:2181(CONNECTED) 6] get /sc/yy
90
```

### 创建一个topic来测试kafka

#### **创建topic : **

```
bin/kafka-topics.sh --create --zookeeper 192.168.44.181:2181 --replication-factor 1 --partitions 1 --topic test

```

 效果图：

<img alt="" height="136" src="https://img-blog.csdnimg.cn/2598b7dfa73b4d2bbac2235e48b80967.png" width="1095">



#### 创建生产者

```
bin/kafka-console-producer.sh --broker-list 192.168.44.181:9092 --topic test

```

#### 创建消费者

```
bin/kafka-console-consumer.sh --bootstrap-server 192.168.44.181:9092 --topic test

```

**消费成功效果图：**

消费者消费到了生产者产生的数据

<img alt="" height="656" src="https://img-blog.csdnimg.cn/420b7ee947d44fe89ddf240f713cd332.png" width="1095">

### filebeat部署

安装

```
rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch
```

编辑 vim/etc/yum.repos.d/fb.repo

```
[elastic-7.x]
name=Elastic repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
​type=rpm-md
```

#### **yum安装filebeat**

```
yum  install  filebeat -y
```

设置开机自启

```
systemctl enable filebeat
```

修改filebeat配置文件，filebeat的配置文件是yml格式的，

首先将filebeat的配置文件**filebeat.yml**备份一份为**filebeat.yml.bak**

```
[root@nginx-kafka01 filebeat]# cp filebeat.yml filebeat.yml.bak

```

然后再将filebeat.yml文件清空，加上我们自己配置的一些配置

```
filebeat.inputs:
- type: log
  # Change to true to enable this input configuration.
  enabled: true
  # Paths that should be crawled and fetched. Glob based paths.
  paths:
    - /var/log/nginx/sc/access.log
#==========------------------------------kafka-----------------------------------
output.kafka:
  hosts: ["192.168.44.181:9092","192.168.44.182:9092","192.168.44.183:9092"]
  topic: nginxlog
  keep_alive: 10s

```

配置好了配置文件，就可以通过filebeat来收集nginx的日志了

#### **测试filebeat能否生产数据**

创建主题 ：nginxlog(这个主题是我们在filebeat指定好的，filebeat会将生产的数据都吐到这个主题里面)

```
bin/kafka-topics.sh --create --zookeeper 192.168.44.181:2181 --replication-factor 3 --partitions 1 --topic nginxlog
```

#### 启动filebeat服务

```
systemctl start  filebeat
```

可以看到，filebeat进程是启动成功了的

<img alt="" height="179" src="https://img-blog.csdnimg.cn/420f3388121745af80ffde73ba37d25a.png" width="1094">

####  接下来用kafka自带的消费者程序来测试一下我们能否消费到filebeat生产的nginxlog主题里面的数据

```
[root@nginx-kafka01 kafka_2.12-2.8.1]# bin/kafka-topics.sh --create --zookeeper 192.168.44.181:2181 --replication-factor 3 --partitions 1 --topic nginxlog

```

消费成功效果图：<img alt="" height="653" src="https://img-blog.csdnimg.cn/3d52cce8af7f4ff5abf16768dbabc56e.png" width="1097">

** 这个时候，我们可以刷新一下我们nginx的静态页面，没有问题的话，我们消费的数据会10秒刷新一次。**

<img alt="" height="503" src="https://img-blog.csdnimg.cn/06428950e14e4df1aa3a5d0113bed361.png" width="1200">

 效果图：



<img alt="" height="666" src="https://img-blog.csdnimg.cn/ea97553f60144d23a486a408fd872a41.png" width="1104">

####  可以到filebeat的记录数据的文件里面看一下消费者有没有成功消费到数据。（/var/lib/filebeat/registry/filebeat/）

```
[root@nginx-kafka01 filebeat]# less log.json 

```

<img alt="" height="374" src="https://img-blog.csdnimg.cn/55279d70e2c443f28eb893e19c55114d.png" width="1092">

###  编写python脚本，模拟消费者消费数据，然后将所需字段提取出来整理后放入数据库里面

```
import json
import requests
import time

taobao_url = "https://ip.taobao.com/outGetIpInfo?accessKey=alibaba-inc&amp;ip="
#查询ip地址的信息（省份和运营商isp），通过taobao网的接口
def resolv_ip(ip):
    response = requests.get(taobao_url+ip)
    if response.status_code == 200:
       tmp_dict = json.loads(response.text)
       prov = tmp_dict["data"]["region"]
       isp = tmp_dict["data"]["isp"]
       return prov,isp
    return None,None

#将日志里读取的格式转换为我们指定的格式
def trans_time(dt):
     #把字符串转成时间格式
    timeArray = time.strptime(dt, "%d/%b/%Y:%H:%M:%S")
    #timeStamp = int(time.mktime(timeArray))
    #把时间格式转成字符串
    new_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)    
    return new_time

import pymysql
def import_data(prov,isp,dt,ip,bt):
    conn = pymysql.connect(host='192.168.44.170',port=3306,user='wangsh',passwd='123456',db='kafka_data')
    # 创建游标
    cursor = conn.cursor()
    # 插入数据
    cursor.execute('insert into data(prov,isp,datetime,ip,bt) values("%s","%s","%s","%s","%s")' % (prov,isp,dt,ip,bt))
    conn.commit()
    conn.close()
    cursor.close()
#从kafka里获取数据，清洗为我们需要的ip，时间，带宽
from pykafka import KafkaClient
client = KafkaClient(hosts="192.168.44.181:9092,192.168.44.182:9092,192.168.44.183:9092")
topic = client.topics['nginxlog'] 
balanced_consumer = topic.get_balanced_consumer(
  consumer_group='testgroup',
  auto_commit_enable=True,    
  zookeeper_connect='nginx-kafka01:2181,nginx-kafka02:2181,nginx-kafka03:2181'
) 
consumer = topic.get_simple_consumer() 
for message in balanced_consumer:
   if message is not None: 
       line = json.loads(message.value.decode("utf-8"))
       log = line["message"]
       tmp_lst = log.split()
       ip = tmp_lst[0]
       dt = tmp_lst[3].replace("[","")
       bt = tmp_lst[9]
       dt = trans_time(dt)
       prov, isp = resolv_ip(ip)
       if prov and isp:
          print(prov,isp,dt,ip,bt)
          import_data(prov,isp,dt,ip,bt)

```

数据入库效果图：

 <img alt="" height="450" src="https://img-blog.csdnimg.cn/12d13a91b6514bcba97bb0d5fa289e0c.png" width="643">

 



### 日志收集平台详细架构图：

附带一些原理

<img alt="" height="750" src="https://img-blog.csdnimg.cn/32ede1ec99fe42a294359ae3e2d3a14f.png" width="1200">




