
--- 
title:  【架构师面试题库1】—etcd高可用集群搭建 
tags: []
categories: [] 

---
## 环境准备

**操作系统：CentOS7**

**搭建一个三节点的etcd集群**

```
机器名:etcd01 IP地址:192.168.154.133

机器名:etcd03 IP地址:192.168.154.145

机器名:etcd04 IP地址:192.168.154.146
```

## etcd包下载安装

**1、下载**

```
https://github.com/etcd-io/etcd/releases/download/v3.3.1/etcd-v3.3.1-linux-amd64.tar.gz
```

**2.复制二进制命令 到/usr/local/bin**

```
#解压软件包
tar -zxvf etcd-v3.3.1-linux-amd64.tar.gz

#将命令复制进环境
cd etcd-v3.3.1-linux-amd64
cp etcd etcdctl /usr/local/bin/
```

**3.在三个节点中创建数据目录**

```
#创建数据存储路径
mkdir -p /var/lib/etcd
```

4.在每个节点上创建etcd的systemd unit文件

```
vim /usr/lib/systemd/system/etcd.service #如果没有system目录则新创建一个
```

 三个节点配置如下：注意IP地址相关配置

**etcd01**

```
#etcd01节点

[Unit]
Description=etcd server
After=network.target
After=network-online.target
Wants=network-online.target

[Service]
Type=notify
WorkingDirectory=/var/lib/etcd/
ExecStart=/usr/local/bin/etcd --name etcd01 --initial-advertise-peer-urls http://192.168.154.133:2380 --listen-peer-urls http://192.168.154.133:2380 --listen-cli
ent-urls http://192.168.154.133:2379,http://127.0.0.1:2379 --advertise-client-urls http://192.168.154.133:2379 --initial-cluster-token etcd-cluster-1 --initial-c
luster etcd03=http://192.168.154.145:2380,etcd04=http://192.168.154.146:2380,etcd01=http://192.168.154.133:2380  --initial-cluster-state new --data-dir=/var/lib/
etcd

Restart=on-failure
RestartSec=5
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target                        
```

**etcd03节点**

```
vim /usr/lib/systemd/system/etcd.service #如果没有system目录则新创建一个
```

```
#etcd03节点

[Unit]
Description=etcd server
After=network.target
After=network-online.target
Wants=network-online.target

[Service]
Type=notify
WorkingDirectory=/var/lib/etcd/
ExecStart=/usr/local/bin/etcd --name etcd03 --initial-advertise-peer-urls http://192.168.154.145:2380 --listen-peer-urls http://192.168.154.145:2380 --listen-cli
ent-urls http://192.168.154.145:2379,http://127.0.0.1:2379 --advertise-client-urls http://192.168.154.145:2379 --initial-cluster-token etcd-cluster-1 --initial-c
luster etcd03=http://192.168.154.145:2380,etcd04=http://192.168.154.146:2380,etcd01=http://192.168.154.133:2380  --initial-cluster-state new --data-dir=/var/lib/
etcd

Restart=on-failure
RestartSec=5
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

**etcd04节点**

```
vim /usr/lib/systemd/system/etcd.service #如果没有system目录则新创建一个
```

```
#etcd04节点

[Unit]
Description=etcd server
After=network.target
After=network-online.target
Wants=network-online.target

[Service]
Type=notify
WorkingDirectory=/var/lib/etcd/
ExecStart=/usr/local/bin/etcd --name etcd04 --initial-advertise-peer-urls http://192.168.154.146:2380 --listen-peer-urls http://192.168.154.146:2380 --listen-cli
ent-urls http://192.168.154.146:2379,http://127.0.0.1:2379 --advertise-client-urls http://192.168.154.146:2379 --initial-cluster-token etcd-cluster-1 --initial-c
luster etcd03=http://192.168.154.145:2380,etcd04=http://192.168.154.146:2380,etcd01=http://192.168.154.133:2380  --initial-cluster-state new --data-dir=/var/lib/
etcd

Restart=on-failure
RestartSec=5
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target                   
```

**4.开启etcd服务：三个节点分别执行**

```
systemctl daemon-reload &amp;&amp; systemctl enable etcd &amp;&amp; systemctl start etcd
```

**5.相关查看命令**

**systemctl status etcd.service #查看运行状态**

```
# 节点的服务运行状态

● etcd.service - etcd server
   Loaded: loaded (/usr/lib/systemd/system/etcd.service; enabled; vendor preset: disabled)
   Active: active (running) since 三 2022-01-19 18:17:23 CST; 1h 29min ago
 Main PID: 4190 (etcd)
   Memory: 13.8M
   CGroup: /system.slice/etcd.service
           └─4190 /usr/local/bin/etcd --name etcd04 --initial-advertise-peer-urls http://192.168.154.146:2380 --listen-peer-urls http://192.168.154.146:2380 -...

1月 19 18:17:23 etcd04 etcd[4190]: serving insecure client requests on 192.168.154.146:2379, this is strongly discouraged!
1月 19 18:17:23 etcd04 etcd[4190]: set the initial cluster version to 3.0
1月 19 18:17:23 etcd04 etcd[4190]: enabled capabilities for version 3.0
1月 19 18:17:24 etcd04 etcd[4190]: peer f5cee01588336622 became active
1月 19 18:17:24 etcd04 etcd[4190]: established a TCP streaming connection with peer f5cee01588336622 (stream Message writer)
1月 19 18:17:24 etcd04 etcd[4190]: established a TCP streaming connection with peer f5cee01588336622 (stream MsgApp v2 writer)
1月 19 18:17:24 etcd04 etcd[4190]: established a TCP streaming connection with peer f5cee01588336622 (stream Message reader)
1月 19 18:17:24 etcd04 etcd[4190]: established a TCP streaming connection with peer f5cee01588336622 (stream MsgApp v2 reader)
1月 19 18:17:27 etcd04 etcd[4190]: updated the cluster version from 3.0 to 3.3
1月 19 18:17:27 etcd04 etcd[4190]: enabled capabilities for version 3.3
```

**etcdctl member list #查看集群中各个节点**

```
#查看集群各节点

[root@etcd01 etcd]# etcdctl member list                      
23795efc1fd09208: name=etcd01 peerURLs=http://192.168.154.133:2380 clientURLs=http://192.168.154.133:2379 isLeader=true
5789f6b3099dcd29: name=etcd04 peerURLs=http://192.168.154.146:2380 clientURLs=http://192.168.154.146:2379 isLeader=false
f5cee01588336622: name=etcd03 peerURLs=http://192.168.154.145:2380 clientURLs=http://192.168.154.145:2379 isLeader=false
```

**etcdctl cluster-health #查看集群的健康情况**

```
[root@etcd01 etcd]# etcdctl cluster-health
member 23795efc1fd09208 is healthy: got healthy result from http://192.168.154.133:2379
member 5789f6b3099dcd29 is healthy: got healthy result from http://192.168.154.146:2379
member f5cee01588336622 is healthy: got healthy result from http://192.168.154.145:2379
```

###  推荐阅读

#### 【资源推荐】
-  <h4 id="%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%93%E7%94%A8%E7%B3%BB%E7%BB%9F">**渗透测试专用系统**</h4> - kali-linux-e17-2019.1a-amd64.iso系统镜像- - kali-linux-2018.4-amd64 操作系统- - manjaro-xfce-17.1.7-stable-x86_64.iso系统镜像- - WiFi专用渗透系统 nst-32-11992.x86_64.iso操作系统镜像- - Parrot-security-4.1_amd64.iso 操作系统镜像- - manjaro-xfce-17.1.7-stable-x86_64 操作系统- - cyborg-hawk-linux-v-1.1 操作系统- - <li> <h4 id="%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E7%9B%B8%E5%85%B3%E5%B7%A5%E5%85%B7">渗透测试相关工具</h4> - **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>    - 【kali常用工具】抓包工具Charles Windows64位 免费版- - 【kali常用工具】图印工具stamp.zip- - 【kali常用工具】brutecrack工具[WIFIPR中文版]及wpa/wpa2字典- - 【kali常用工具】EWSA 5.1.282-破包工具- - 【kali常用工具】Realtek 8812AU KALI网卡驱动及安装教程- - 【kali常用工具】无线信号搜索工具_kali更新- - 【kali常用工具】inssider信号测试软件_kali常用工具- - 【kali常用工具】MAC地址修改工具 保护终端不暴露- - 【kali常用工具】脚本管理工具 php和jsp页面 接收命令参数 在服务器端执行- 
#### 渗透测试相关工具
- **Java实现照片GPS定位【完整脚本】**- - **Python实现照片GPS定位【完整脚本】**- - **女神忘记相册密码 python20行代码打开【完整脚本】**- - **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- 
**python实战**
- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong>**<strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong>...</strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong>**<strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong>**<strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>
**【pygame开发实战开发30例 完整源码】**
- 
**【pygame游戏开发专栏，获取完整源码+教程】**
- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>-   - CSDN官方学习推荐 ↓ ↓ ↓- **CSDN出的Python全栈知识图谱，太强了，推荐给大家！**
<img alt="" height="625" src="https://img-blog.csdnimg.cn/20210607120133619.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="351">
