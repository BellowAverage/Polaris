
--- 
title:  Hadoop - HDFS文件系统 
tags: []
categories: [] 

---
**目录**



























































## **HDFS文件系统 **

### **1、文件系统定义**

>  
 **文件系统是一种存储和组织数据的方法，实现了数据的存储，分离组织，访问和获取等操作，使得用户对文件访问和查找变得容易。** 
 **文件系统使用树形目录的抽象逻辑概念代替了硬盘等物理设备使用数据块的概念，用户不必关心数据底层存在硬盘哪里，只需要记住这个文件的所属目录和文件名即可。** 
 **文件系统通常使用硬盘和光盘这样的存储设备，并维护文件在设备中的物理位置。** 


>  
 **    所谓传统常见的文件系统更多指的的单机的文件系统，也就是底层不会横跨多台机器实现。比如windows操作系统 上的文件系统、Linux上的文件系统、FTP文件系统等等。     这些文件系统的共同特征包括：         1. 带有抽象的目录树结构，树都是从/根目录开始往下蔓延；         2. 树中节点分为两类：目录和文件；         3. 从根目录开始，节点路径具有唯一性。 ** 


**########################################################## **

### **2、大数据时代，面对海量数据，传统的文件存储系统会面临哪些挑战？**

>  
 **成本高：** 
 **​        传统存储硬件通用性差，设备投资加上后期维护，升级扩容的成本非常高** 
 **如何支撑高效率的计算分析：** 
 **​        传统的存储方式意味着数据：存储是存储，计算是计算，当需要处理数据的时候把数据移动过来，** 
 **​        程序和数据存储是属于不同的技术厂商实现，无法有机统一整合在一起。** 
 **性能差：** 
 **​        单节点I/O性能瓶颈无法逾越，难以支撑海量数据的高并发吞吐场景。** 
 **可扩展性差：** 
 **​        无法实现快速部署和弹性扩展，动态扩容，缩容成本高，技术实现难度大。** 


**########################################################## ** 

### **3、分布式存储系统的核心属性及功能含义**

>  
 **分布式存储系统核心属性** 
 **• 分布式存储** 
 **• 元数据记录** 
 **• 分块存储** 
 **• 副本机制** 


**########################################################## ** 

#### **一、分布式存储的优点**

>  
 **问题：数据量大，单机存储遇到瓶颈** 
 **解决：** 
 **​        单机纵向扩展：磁盘不够加磁盘，有上限瓶颈限制** 
 **​        多机横向扩展：机器不够加机器，理论上无限扩展** 


**########################################################## ** 

#### **二、元数据记录的功能**

>  
 **问题：** 
 **​        文件分布在不同机器上不利于寻找** 
 **解决：** 
 **​        元数据记录下文件及其存储位置信息，快速定位文件位置** 


** <img alt="" height="260" src="https://img-blog.csdnimg.cn/a3562e0fc770405190fc56e6d190f3d8.png" width="761">**

**########################################################## ** 

** **

#### **三、分块存储好处**

>  
 **问题：** 
 **​        文件过大导致单机存不下，上传下载效率低** 
 **解决：** 
 **​        文件分块存储在不同机器，针对块并行操作提高效率** 


** ########################################################## **

#### **四、副本机制的作用**

>  
 **问题：** 
 **​        硬件故障难以避免，数据易丢失** 
 **解决：** 
 **​        不同机器设置备份，冗余存储，保障数据安全** 


** ########################################################## **

### **4、HDFS简介**

>  
 **HDFS（Hadoop Distributed File System），意为：Hadoop分布式文件系统。** 
 **是Apache Hadoop核心组件之一，作为大数据生态圈最底层的分布式存储服务而存在，也可以说大数据首先要解决的问题就是海量数据的存储问题。** 


** <img alt="" height="450" src="https://img-blog.csdnimg.cn/fe544337644c40538922dcbaa27089bc.png" width="786">**

>  
 **HDFS主要是解决大数据如何存储问题的，分布式意味着HDFS是横跨多台计算机上的存储系统** 
 **HDFS是一种能够在普通硬件上运行的分布式文件系统，它是高度容错的，适应于具有大数据集的应用程序，它非常适于存储大型数据（例如TB和PB）。** 
 **HDFS使用多台计算机存储文件，并且提供同一的访问接口，像是访问一个普通文件系统一样使用分布式文件系统。** 


 <img alt="" height="408" src="https://img-blog.csdnimg.cn/18f446f6fd1843a18ca0beb6eeabd37a.png" width="808">

#### HDFS适用场景

<img alt="" height="312" src="https://img-blog.csdnimg.cn/866ca313ed804d5fb8f4b7b4d42334f6.png" width="832">

**########################################################## ** 

### 5、HDFS主从架构

>  
 **HDFS集群是标准的master/slave主从架构集群** 
 **一般一个HDFS集群是有一个Namenode和一定数目的Datanode组成** 
 **Namenode是HDSF主节点，Datanode是HDFS从节点，两种角色各司其职，共同协调完成分布式的文件存储服务** 
 **官方架构图中是一主五从模式，其中五个从角色位于两个机架（RACK）的不同服务器上面。** 


 <img alt="" height="496" src="https://img-blog.csdnimg.cn/b36bb460cf5c4d55974bdba0cf5b45fa.png" width="785">



#### 分块存储

>  
 HDFS中的文件在物理上是分块存储的，默认大小是128M，不足128M则本身就是一块 
 块的大小可以通过配置参数来规定，参数位于hdfs-default.xml中：dfs.blocksize 


#### 副本机制

>  
 文件的所有block都会有副本，副本系数可以在文件创建的时候指定，也可以在之后通过命令改变 
 副本数由参数dfs.replication控制，默认值是3，也就是会额外再复制2份，连同本身总共3份副本 


#### 元数据管理

>  
 **在HDFS中，Namenode管理的元数据具有两种类型。** 
 **文件自身属性信息** 
 **​        文件名称，权限，修改时间，文件大小，复制因子，数据块大小。** 
 **文件块位置映射信息** 
 **​        记录文件块和Datanode之间的映射信息，即哪个块位于哪个节点上。** 


#### 数据块存储

>  
 **文件的各个block的具体存储管理由DataNode节点管理** 
 **每一个block都可以在多个DataNode上存储** 


**########################################################## ** 

### 6、HDFS shell操作

>  
 **介绍：** 
 **​        命令行界面，是指用户通过键盘输入指令，计算机接收到指令后，予以执行一种人际交互方式** 
 **​        Hadoop提供了文件系统的shell命令行客户端：hadoop fs [options]** 


```
[hadoop@node1 mapreduce]$ hadoop fs
Usage: hadoop fs [generic options]
	[-appendToFile &lt;localsrc&gt; ... &lt;dst&gt;]
	[-cat [-ignoreCrc] &lt;src&gt; ...]
	[-checksum [-v] &lt;src&gt; ...]
	[-chgrp [-R] GROUP PATH...]
	[-chmod [-R] &lt;MODE[,MODE]... | OCTALMODE&gt; PATH...]
	[-chown [-R] [OWNER][:[GROUP]] PATH...]
	[-copyFromLocal [-f] [-p] [-l] [-d] [-t &lt;thread count&gt;] &lt;localsrc&gt; ... &lt;dst&gt;]
	[-copyToLocal [-f] [-p] [-ignoreCrc] [-crc] &lt;src&gt; ... &lt;localdst&gt;]
	[-count [-q] [-h] [-v] [-t [&lt;storage type&gt;]] [-u] [-x] [-e] &lt;path&gt; ...]
	[-cp [-f] [-p | -p[topax]] [-d] &lt;src&gt; ... &lt;dst&gt;]
	[-createSnapshot &lt;snapshotDir&gt; [&lt;snapshotName&gt;]]
	[-deleteSnapshot &lt;snapshotDir&gt; &lt;snapshotName&gt;]
	[-df [-h] [&lt;path&gt; ...]]
	[-du [-s] [-h] [-v] [-x] &lt;path&gt; ...]
	[-expunge [-immediate] [-fs &lt;path&gt;]]
```

```
[hadoop@node1 local]$ hadoop fs -ls /
[hadoop@node1 local]$ hadoop fs -mkdir /test
[hadoop@node1 local]$ hadoop fs -ls /
Found 1 items
drwxr-xr-x   - hadoop supergroup          0 2023-03-28 14:03 /test
```

```
HDFS Shell CLI 支持多种文件系统，包括本地文件系统（file:///）,分布式文件系统（hdfs://）

​		具体操作的是什么文件系统取决于命令中文件路径URL中的前缀协议。

​		如果没有指定前缀，则将会读取环境变量中的fs.defaultFS属性，以该属性值作为默认文件系统。
		hadoop dfs 只能操作HDFS文件系统（包括与Local FS间的操作），不过已经Deprecated；
		hdfs dfs 只能操作HDFS文件系统相关（包括与Local FS间的操作）,常用；
		hadoop fs 可操作任意文件系统，不仅仅是hdfs文件系统，使用范围更广；
		目前版本来看，官方最终推荐使用的是hadoop fs。当然hdfs dfs在市面上的使用也比较多。
```

#### 常用操作：

```
hadoop fs -mkdir [-p] &lt;path&gt; ... 
	path 为待创建的目录
	-p选项的行为与Unix mkdir -p非常相似，它会沿着路径创建父目录
```

```
hadoop fs -ls [-h] [-R] [&lt;path&gt; ...] 
	path 指定目录路径
	-h 人性化显示文件size
	-R 递归查看指定目录及其子目录
```

```
hadoop fs -put [-f] [-p] &lt;localsrc&gt; ... &lt;dst&gt;
	-f 覆盖目标文件（已存在下）
	-p 保留访问和修改时间，所有权和权限。
	localsrc 本地文件系统（客户端所在机器）
	dst 目标文件系统（HDFS）
```

```
hadoop fs -cat &lt;src&gt; ... 
	读取指定文件全部内容，显示在标准输出控制台。
	注意：对于大文件内容读取，慎重。
```

```
hadoop fs -get [-f] [-p] &lt;src&gt; ... &lt;localdst&gt;
	下载文件到本地文件系统指定目录，localdst必须是目录
	-f 覆盖目标文件（已存在下）
	-p 保留访问和修改时间，所有权和权限。
```

```
hadoop fs -cp [-f] &lt;src&gt; ... &lt;dst&gt; 
	-f 覆盖目标文件（已存在下）
```

```
hadoop fs -mv &lt;src&gt; ... &lt;dst&gt;
	移动文件到指定文件夹下
	可以使用该命令移动数据，重命名文件的名称
```

**########################################################## ** 

### 7、HDFS工作流程与机制

#### **主角色：NameNode**

>  
 **NameNode是Hadoop分布式文件系统的核心，架构中的主角色** 
 **NameNode维护和管理文件系统元数据，包括名称空间目录树结构，文件和块的位置信息，访问权限等信息** 
 **基于此，NameNode成为了访问HDFS的唯一入口** 
 **NameNode内部通过内存和磁盘文件两种方式管理元数据。** 
 **其中磁盘上的元数据文件包括Fsimage内存元数据镜像文件和edits log（Journal）编辑日志。** 


#### **namenode职责：**

>  
 **NameNode仅存储HDFS的元数据：文件系统中的所有文件的目录树，并跟踪整个集群中的文件，不存储实际数据** 
 **NameNode知道HDFS中任何给定文件的块列表及其位置，使用此信息NameNode知道如何从块中构建文件** 
 **NameNode不持久化存储每个文件中各个块所在的datanode的位置信息，这些信息会在系统启动时从DataNode重建** 
 **NameNode是Hadoop集群中的单点故障** 
 **NameNode所在及其通常会配置由大量内存（RAM）** 


#### **从角色：datanode**

>  
 **DataNode是Hadoop HDFS中的从角色，负责具体的数据块存储** 
 **DataNode的数量决定了HDFS集群的整体数据存储能力，通过和NameNode配合维护这数据块** 


#### **datanode职责**

>  
 **DataNode负责最终数据块block的存储，是集群的从角色，也称为Slave** 
 **DataNode启动时，会将自己注册到NameNode并汇报自己负责持有的块列表** 
 **当某个DataNode关闭时不会影响数据的可用性，NameNode将安排由其他DataNode管理的块进行副本复制** 
 **DataNode所在机器通常配置有大量的硬盘空间，因为实际数据存储在DataNode中。** 


**主角色辅助角色：secondarynamenode**

>  
 **SecondaryNameNode充当着NameNode的辅助节点，但不能替代NameNode** 
 **主要是帮助主角色进行元数据文件的合并动作，可以理解为主角色的秘书**  


<img alt="" height="408" src="https://img-blog.csdnimg.cn/9cd927a298924734a7adcb4525bbe00e.png" width="796">



**########################################################## **

### 8、HDFS读写数据的过程​​​​​​



#### 核心概念--Pipeline管道

>  
 **Pipeline，中文翻译为管道，这是HDFS在上传文件写数据过程中采用的一种数据传输方式** 
 **客户端将数据块写入第一个数据节点，第一个数据节点保存数据之后再讲块复制到第二个数据节点，后者保存后再将其复制到第三个数据节点** 




<img alt="" height="203" src="https://img-blog.csdnimg.cn/1ad7c873602a4fefa362ec41784f5ad0.png" width="630">

>  
 **为什么datanode之间采用pipeline线性传输，而不是一次给三个datanode拓扑式传输呢？** 
 **因为数据以管道的方式，顺序的沿着一个方向传输，这样能够充分利用每个机器的带宽，避免网络瓶颈和高延迟时的连接，最小化推送所有数据的延时** 
  
 **在线性推送模式下，每台机器的所有出口宽带都用于最快的速度传输数据，而不是在多个接受者之间分配宽带** 


#### **核心概念--ACK应答响应**

>  
 **ACK（Acknowledgs character）即是确认字符，在数据通信中，接收方发送给发送方的一种传输控制字符，表示发来的数据已经确认接收无误** 
  
 **在HDFS pipeline管道传输数据的过程中，传输的反方向会进行ACK校验，确保数据传输安全** 


#### 默认3个副本存储策略：

>  
 **第一块副本：优先客户端本地，否则随机。** 
 **第二块副本：不同于第一块副本的不同机架。** 
 **第三块副本：第二块副本相同机架不同机器。** 


<img alt="" height="484" src="https://img-blog.csdnimg.cn/48b5fbffdefc4126abf9069a66eefa06.png" width="784">

#### **写操作的整个过程：**

>  
 **1、HDFS客户端创建对象实例DistributedFileSystem， 该对象中封装了与HDFS文件系统操作的相关方法。** 
 **2、调用DistributedFileSystem对象的create()方法，通过RPC请求NameNode创建文件。 NameNode执行各种检查判断：目标文件是否存在、父目录是否存在、客户端是否具有创建该文件的权限。检查通过 ，NameNode就会为本次请求记下一条记录，返回FSDataOutputStream输出流对象给客户端用于写数据。** 
 **3、客户端通过FSDataOutputStream输出流开始写入数据。** 
 **4、客户端写入数据时，将数据分成一个个数据包（packet 默认64k）, 内部组件DataStreamer请求NameNode挑 选出适合存储数据副本的一组DataNode地址，默认是3副本存储。 DataStreamer将数据包流式传输到pipeline的第一个DataNode,该DataNode存储数据包并将它发送到pipeline的第 二个DataNode。同样，第二个DataNode存储数据包并且发送给第三个（也是最后一个）DataNode。** 
 **5、传输的反方向上，会通过ACK机制校验数据包传输是否成功；** 
 **6、客户端完成数据写入后，在FSDataOutputStream输出流上调用close()方法关闭。** 
 **7、DistributedFileSystem联系NameNode告知其文件写入完成，等待NameNode确认。 因为namenode已经知道文件由哪些块组成（DataStream请求分配数据块），因此仅需等待最小复制块即可成功返回 最小复制是由参数dfs.namenode.replication.min指定，默认是1.** 


<img alt="" height="364" src="https://img-blog.csdnimg.cn/5256f64e77cb4e5896c8e078994b89d9.png" width="791">

**########################################################## ** 

#### 读操作的整个过程：

>  
 **读操作的整个过程：** 
 **1、HDFS客户端创建对象实例DistributedFileSystem， 调用该对象的open()方法来打开希望读取的文件。** 
 **2、DistributedFileSystem使用RPC调用namenode来确定**文件中前几个块的块位置（分批次读取）信息**。** 
 **对于每个块，namenode返回具有该块所有副本的datanode位置地址列表，并且该地址列表是排序好的，与客户端的网络拓扑距离近的排序靠前。** 
 **3、DistributedFileSystem将FSDataInputStream输入流返回到客户端以供其读取数据。** 
 **4、客户端在FSDataInputStream输入流上调用read()方法。然后，已存储DataNode地址的InputStream连接到文件** 
 **中第一个块的最近的DataNode。数据从DataNode流回客户端，结果客户端可以在流上重复调用read（）。** 
 **5、当该块结束时，FSDataInputStream将关闭与DataNode的连接，然后寻找下一个block块的最佳datanode位置。这些操作对用户来说是透明的。所以用户感觉起来它一直在读取一个连续的流。** 
 **客户端从流中读取数据时，也会根据需要询问NameNode来检索下一批数据块的DataNode位置信息。** 
 **6、一旦客户端完成读取，就对FSDataInputStream调用close()方法。** 


<img alt="" height="364" src="https://img-blog.csdnimg.cn/03573d2b63184a65a7bba0893476150d.png" width="792">
