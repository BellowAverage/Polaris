
--- 
title:  linux部署zookeeper 
tags: []
categories: [] 

---
## linux部署zookeeper

#### 1、单机部署zk

ZooKeeper服务器是用Java创建的，它需要在JVM上运行，所以需要使用JDK1.6及以上版本，一般都是jdk1.8。

选择自己安装本地的jdk，而不是centos自带的openjdk。 查看本地安装的jdk：

```
java -version
java version "1.8.0_201"
Java(TM) SE Runtime Environment (build 1.8.0_201-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.201-b09, mixed mode)

```

#### 2、下载zookeeper压缩包

 找到对应的版本下载即可，我这里选择的是 3.5.8版本。 <img src="https://img-blog.csdnimg.cn/e9e73eaa0b174fd4ada3044cbd969c7c.png" alt="在这里插入图片描述">

#### 3、安装zookeeper

在 /usr 目录下新建 zookeeper目录，然后将 下载的 zookeeper压缩包拷贝到这个新建的 zookeeper目录中。

```
cd /usr
mkdir zookeeper
cd  zookeeper
tar -zxvf apache-zookeeper-3.5.8-bin.tar.gz
mv apache-zookeeper-3.5.8-bin zookeeper-3.5.8

```

在 /usr/zookeeper/zookeeper-3.5.8 文件夹下，创建dataDir 、dataLogDir文件夹。dataDir存放快照日志，dataLogDir存放事务日志。 如果不配置dataLogDir，那么事务日志也会写在dataDir目录中。这样会严重影响zk的性能。因为在zk吞吐量很高的时候，产生的事务日志和快照日志太多。

```
mkdir -p dataDir
mkdir dataLogDir

```

#### 4、修改配置文件

在Zookeeper的安装目录下的conf文件下，默认为：zoo_sample.cfg文件，没有 zoo.cfg 。但是zookeeper在启动的时候默认使用的是zoo.cfg这个配置文件。所以，我们需要配置zoo.cfg文件。

```
cd conf
cp -p zoo_sample.cfg zoo.cfg
vi zoo.cfg

# 存放数据文件，找到并修改,指向了外部创建的那两个文件的路径
dataDir=/usr/zookeeper/zookeeper-3.5.8/dataDir
# 存放日志文件
dataLogDir=/usr/zookeeper/zookeeper-3.5.8/dataLogDir

```

#### 5、启动zk

```
cd /usr/zookeeper/zookeeper-3.5.8/bin
./zkServer.sh start

1.重启ZooKeeper，./zkServer.sh restart

2.停止ZooKeeper，./zkServer.sh stop

3.启动ZooKeeper CLI (ZooKeeper客户端)，./zkCli.sh

```

zookeeper默认端口是2181，可以netstat查看。
