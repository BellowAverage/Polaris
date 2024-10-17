
--- 
title:  ZooKeeper 集群部署 
tags: []
categories: [] 

---
<img alt="" height="524" src="https://img-blog.csdnimg.cn/375f930b23f34e3ebdfdfbc83e12ae02.png" width="1200">

**目录**













>  
 **部署ZooKeeper集群之前请先部署jdk** 
 **使用hadoop用户部署ZooKeeper集群** 


### 1、下载apache-zookeeper包

部署机器：

```
192.168.20.11 node1
192.168.20.12 node2
192.168.20.13 node3
```

依次在node1，node2，node3上部署：

```
# 进入安装目录
[hadoop@node1 local]$ cd /usr/local
# 下载apache-ZooKeeper二进制包
[hadoop@node1 local]$ sudo wget https://archive.apache.org/dist/zookeeper/zookeeper-3.6.3/apache-zookeeper-3.6.3-bin.tar.gz
```

```
# 解压
[hadoop@node1 local]$ sudo tar -xvf apache-zookeeper-3.6.3-bin.tar.gz
```

```
# 制作软链接
[hadoop@node1 local]$ sudo ln -s apache-zookeeper-3.6.3-bin apache-zookeeper
```

```
# 更改文件属主和属组为hadoop
[hadoop@node1 local]$ sudo chown hadoop:hadoop -R apache-zookeeper
[hadoop@node1 local]$ sudo chown hadoop:hadoop -R apache-zookeeper-3.6.3-bin
```

**################################################### **

### 2、修改配置

依次在node1，node2，node3上配置：

```
[hadoop@node1 apache-zookeeper]$ cd /usr/local/apache-zookeeper/conf
# 将zoo_sample.cfg 复制一份 改名为 zoo.cfg
[hadoop@node1 conf]$ sudo cp zoo_sample.cfg zoo.cfg

[hadoop@node1 conf]$ vim zoo.cfg 
dataDir=/data/zookeeper/data
server.1=192.168.20.11:2888:3888
server.2=192.168.20.12:2888:3888
server.3=192.168.20.13:2888:3888
```

启用jmx，在下面文件最后加上JMX配置

```
[hadoop@node1 apache-zookeeper]$ cd /usr/local/apache-zookeeper/bin/
[hadoop@node1 bin]$ vim zkEnv.sh 
JMXLOCALONLY=false
JMXDISABLE=false
JMXPORT=9998
JMXAUTH=false
JMXSSL=false
```

启用zkcli权限(for kafka eagle)， 下面文件77行之后，添加 # zkcli permission ...

```
[hadoop@node1 bin]$ vim zkServer.sh
# zkcli permission
ZOOMAIN="-Dzookeeper.4lw.commands.whitelist=* ${ZOOMAIN}"
```

<img alt="" height="152" src="https://img-blog.csdnimg.cn/c897a29f15984572b84360e8b3a42641.png" width="693">

 **################################################### **

### 3、添加服务器id

```
[hadoop@node1 data]$ sudo mkdir -p /data/zookeeper/data/
[hadoop@node1 data]$ sudo chown -R hadoop:hadoop zookeeper/
[hadoop@node1 data]$sudo echo 1 &gt; /data/zookeeper/data/myid

# 分别在node2和node3添加
[hadoop@node2 data]$sudo echo 2 &gt; /data/zookeeper/data/myid
[hadoop@node3 data]$sudo echo 3 &gt; /data/zookeeper/data/myid
```

**################################################### ** 

### 4、启动ZooKeeper集群

在node1和node2，node3操作：

```
[hadoop@node1 bin]$ ./zkServer.sh start &gt;/data/zookeeper/logs/startup.log 2&gt;&amp;1


# 查看ZooKeeper集群状态 可以看到三台机器，两个follower，一个leader
[hadoop@node1 bin]$ ./zkServer.sh status
/usr/local/jdk/bin/java
ZooKeeper JMX enabled by default
ZooKeeper remote JMX Port set to 9998
ZooKeeper remote JMX authenticate set to false
ZooKeeper remote JMX ssl set to false
ZooKeeper remote JMX log4j set to true
Using config: /usr/local/apache-zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: follower


[hadoop@node2 bin]$ ./zkServer.sh status
/usr/local/jdk/bin/java
ZooKeeper JMX enabled by default
ZooKeeper remote JMX Port set to 9998
ZooKeeper remote JMX authenticate set to false
ZooKeeper remote JMX ssl set to false
ZooKeeper remote JMX log4j set to true
Using config: /usr/local/apache-zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: follower


[hadoop@node3 bin]$ ./zkServer.sh status
/usr/local/jdk/bin/java
ZooKeeper JMX enabled by default
ZooKeeper remote JMX Port set to 9998
ZooKeeper remote JMX authenticate set to false
ZooKeeper remote JMX ssl set to false
ZooKeeper remote JMX log4j set to true
Using config: /usr/local/apache-zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost. Client SSL: false.
Mode: leader
```

**################################################### ** 

### 5、客户端连接

```
[hadoop@node1 bin]$ ./zkCli.sh -server 127.0.0.1:2181
[zk: 127.0.0.1:2181(CONNECTED) 0] ls /
[zookeeper]
# 创建永久节点
&gt; create /zk_test my_data
&gt; get /zk_test
&gt; set /zk_test junk
&gt; delete /zk_test
```

**################################################### ** 

### 6、添加新节点：

```
1. 更新所有服务器的配置文件

2. 先轮流重启 Follower

3. 最后重启 Leader
```


