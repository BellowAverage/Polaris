
--- 
title:  Hbase 集群的安装部署 
tags: []
categories: [] 

---
**目录**















**部署集群：**

```
192.168.20.11 node1
192.168.20.12 node2
192.168.20.13 node3

```

<img alt="" height="570" src="https://img-blog.csdnimg.cn/1d8e341d5fee42af8a9cc7d199732064.png" width="1200">

 

### 1、下载HBase二进制源码包

在node1，node2，node3上操作

```
[hadoop@node1 ~]$ cd /usr/local
[hadoop@node1 local]$ sudo wget https://archive.apache.org/dist/hbase/2.4.8/hbase-2.4.8-bin.tar.gz
[hadoop@node1 local]$ sudo tar -xvf hbase-2.4.8-bin.tar.gz
[hadoop@node1 local]$ sudo ln -s hbase-2.4.8 hbase
[hadoop@node1 local]$ sudo  chown -R  hadoop:hadoop hbase
[hadoop@node1 local]$ sudo  chown -R  hadoop:hadoop hbase-2.4.8
```

**##################################################### **

### 2、配置环境变量

```
[hadoop@node1 conf]$ cd /usr/local/hbase/conf
[hadoop@node1 conf]$ vim conf/hbase-env.sh
export JAVA_HOME=/usr/local/jdk
export HBASE_HEAPSIZE=4G
export HBASE_MANAGES_ZK=false
export HBASE_PID_DIR=/data/hbase
```

**##################################################### ** 

### 3、配置ZooKeeper和Hbase配置项

在node1，node2，node3上操作



```
[hadoop@node1 conf]$ cd /usr/local/hbase/conf
# 配置ZooKeeper和Hbase配置项
# 将 hbase-site.xml 中的内容替换为如下内容
[hadoop@node1 conf]$ vim hbase-site.xml 


 
 &lt;!-- hbase是否部署为集群模式  --&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.cluster.distributed&lt;/name&gt;
    &lt;value&gt;true&lt;/value&gt;
  &lt;/property&gt;
  &lt;!--zookeeper 集群ip --&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.zookeeper.quorum&lt;/name&gt;
    &lt;value&gt;node1,node2,node3&lt;/value&gt;
  &lt;/property&gt;
  &lt;!--zookeeper data dir --&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.zoopkeeper.property.dataDir&lt;/name&gt;
    &lt;value&gt;/data/zookeeper/data&lt;/value&gt; 
  &lt;/property&gt;
  &lt;!--要把hbase的数据存储hdfs上的路径 --&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.rootdir&lt;/name&gt;
    &lt;value&gt;hdfs://node1:9000/hbase&lt;/value&gt;
  &lt;/property&gt;
  &lt;!--hbase 数据目录 --&gt;
   &lt;property&gt;
     &lt;name&gt;hbase.tmp.dir&lt;/name&gt;
     &lt;value&gt;/data/hbase/tmp&lt;/value&gt;
   &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.unsafe.stream.capability.enforce&lt;/name&gt;
    &lt;value&gt;false&lt;/value&gt;
  &lt;/property&gt;

  &lt;!-- Flink Secondary Index --&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.regionserver.wal.codec&lt;/name&gt;
    &lt;value&gt;org.apache.hadoop.hbase.regionserver.wal.IndexedWALEditCodec&lt;/value&gt;
  &lt;/property&gt;

  &lt;property&gt;
    &lt;name&gt;hbase.column.max.version&lt;/name&gt;
    &lt;value&gt;2&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.regionserver.global.memstore.size&lt;/name&gt;
    &lt;value&gt;0.2&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.regionserver.global.memstore.size.lower.limit&lt;/name&gt;
    &lt;value&gt;0.8&lt;/value&gt;
  &lt;/property&gt;

  &lt;!-- 实际的Block Size = Heap size * hfile.block.cache.size， 需要重启才能生效，HDFS读较多时，可以增加zhe --&gt;
  &lt;property&gt;
    &lt;name&gt;hfile.block.cache.size&lt;/name&gt;
    &lt;value&gt;0.2&lt;/value&gt;
  &lt;/property&gt;

  &lt;!--bytes,每个用户写缓存数，默认2097152; 总消耗内存=hbase.client.write.buffer * hbase.regionserver.handler.count --&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.hregion.memstore.flush.size&lt;/name&gt;
    &lt;value&gt;134217728&lt;/value&gt;
  &lt;/property&gt;

  &lt;!--RPC handler，default 30--&gt;
  &lt;property&gt;
    &lt;name&gt;dfs.namenode.service.handler.count&lt;/name&gt;
    &lt;value&gt;48&lt;/value&gt;
  &lt;/property&gt;

  &lt;!-- Phoenix error--&gt;
  &lt;property&gt;
    &lt;name&gt;phoenix.coprocessor.maxServerCacheTimeToLiveMs&lt;/name&gt;
    &lt;value&gt;300000&lt;/value&gt;
  &lt;/property&gt;

  &lt;!-- Region Split Policy --&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.regionserver.region.split.policy&lt;/name&gt;
    &lt;value&gt;org.apache.hadoop.hbase.regionserver.DisabledRegionSplitPolicy&lt;/value&gt;
  &lt;/property&gt;

  
  &lt;!-- Compacting 604800000 --&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.hstore.compactionthreshold&lt;/name&gt;
    &lt;value&gt;5&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.hstore.compaction.max&lt;/name&gt;
    &lt;value&gt;10&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.hstore.blockingStoreFiles&lt;/name&gt;
    &lt;value&gt;16&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.hregion.majorcompaction&lt;/name&gt;
    &lt;value&gt;0&lt;/value&gt;
  &lt;/property&gt;

  &lt;property&gt;
    &lt;name&gt;hbase.hstore.compaction.throughput.higher.bound&lt;/name&gt;
    &lt;value&gt;20971520&lt;/value&gt;
    &lt;description&gt;The default is 20 MB/sec&lt;/description&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.hstore.compaction.throughput.lower.bound&lt;/name&gt;
    &lt;value&gt;10485760&lt;/value&gt;
    &lt;description&gt;The default is 10 MB/sec&lt;/description&gt;
  &lt;/property&gt;

```

**##################################################### ** 

### 4、修改regionservers文件

>  
 **在node1，node2，node3上操作** 


```
[hadoop@node1 conf]$ vim regionservers 
node1
node2
node3
```

**##################################################### ** 

### 5、修改冲突jar包

>  
 **hbase和hadoop都有slf4j-log4j12-1.7.30.jar包，启动hbase的时候会有冲突** 
 **修改hbase的jar包名。** 


```
[hadoop@node1 lib]$ cd /usr/local/hbase/lib/client-facing-thirdparty/
[hadoop@node1 client-facing-thirdparty]$ mv slf4j-log4j12-1.7.30.jar slf4j-log4j12-1.7.30.jar.bak
```

**##################################################### ** 

### 6、查看相关进程是否启动

```
[root@node1 ~]# jps
42128 HRegionServer
42848 ResourceManager
33729 QuorumPeerMain
41893 HMaster
40664 NameNode
40824 DataNode
44442 Jps



[root@node2 ~]# jps
15410 HRegionServer
17013 Jps
15813 NodeManager
15021 DataNode
15133 SecondaryNameNode
1583 Bootstrap
12223 QuorumPeerMain




[root@node3 ~]# jps
13058 NodeManager
7766 QuorumPeerMain
13531 Jps
12715 HRegionServer
12412 DataNode

```

**##################################################### ** 

### 7、访问hbase页面

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/182326bacf264eccbb62b3a51b79f355.png" width="1200">

 
