
--- 
title:  linux高级篇基础理论十一（GlusterFS） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


**目录**

































### GFS简介

GlusterFS是一个开源的分布式文件系统，同时也是Scale--Out存储解决方案Gluster的核心，在 存储数据方面具有强大的横向扩展能力，通过扩展不同的节点可以支持数PB级别的存储容量。 GlusterFS借助TCP/IP或InfiniBand RDMA网络将分散的存储资源汇聚在一起，统一提供存储服务，并使用单一全局命名空间来管理数据。GlusterFS基于可堆叠的用户空间以及无元的设计，可为各种不同的数据负载提供优异的性能。

#### 1、GlusterFS特点：

   扩展性和高性能    高可用性    全局统一命名空间    弹性卷管理    基于标准协议

#### 2、GFS术语
- Brick(存储块)：指可信主机池中由主机提供的用于物理存储的专用分区，是GlusterFS中的基本存储单元，同时也是可信存储池中服务器上对外提供的存储目录。存储目录的格式由服务器和目录的绝对路径构成，表示方法为SERVER:EXPORT,如192.168.1.4：data/mydir/- Volume(逻辑卷)：一个逻辑卷是一组Brick的集合。卷是数据存储的逻辑设备，类似于LVM中的逻辑卷。大部分Gluster管理操作是在卷上进行的。- FUSE(Filesystem inUserspace)：是一个内核模块，允许用户创建自己的文件系统，无须修改内核代码。- VFS:内核空间对用户空间提供的访问磁盘的接口。- Glusterd(后台管理进程)：在存储群集中的每个节点上都要运行<li> 
  <hr></li>
#### 3、GlusterFS的工作流程

<img alt="" height="383" src="https://img-blog.csdnimg.cn/direct/1675c726d5f44520892863ffb0105928.png" width="502">

(1)客户端或应用程序通过GlusterFS的挂载点访问数据。 (2)Linux系统内核通过VFS API收到请求并处理 (3)VFS将数据递交给FUSE内核文件系统，并向系统注册一个实际的文件系统FUSE,而FUSE 文件系统则是将数据通过/dev/fuse设备文件递交给了GlusterFS client端。可以将FUSE文件系统理 解为一个代理。 (4)GlusterFS client收到数据后，client根据配置文件对数据进行处理 (5)经过GlusterFS client处理后，通过网络将数据传递至远端的GlusterFS Server,并且将数据写 入服务器存储设备。

#### 4、弹性HASH算法

弹性HASH算法使用Davies--Meyer算法，通过HASH算法得到一个32位的整数范围，假设逻辑卷中有W个存储单位Bck,则32位的整数范围将被划分为W个连续的子空间，每个空间对应一个 Bck。当用户或应用程序访问某一个命名空间时，通过对该命名空间计算HASH值，根据该HASH值所对应的32位整数空间定位数据所在的Bick。

##### 算法优点

保证数据平均分布在每一个Brick中 解决了对元数据服务器的依赖，进而解决了单点故障以及访问瓶颈

#### 5、GFS的七种卷的类型：
- 分布式卷：(Distribute volume):文件通过HASH算法分布到所有Brick Server上，这种卷是Glusterf的基础；以文件为单位根据HASH算法散列到不同的Brick,其实只是扩大了磁盘空间，如果有一块磁盘损坏，数据也将丢失，属于文件级的RADO 0,不具有容错能力。- 条带卷(Stripe volume)：类似RAID0,文件被分成数据块并以轮询的方式分布到多个BrickServer上，文件存储以数据块为单位，支持大文件存储，文件越大，读取效率越高。- 复制卷(Replica volume):将文件同步到多个Brick上，使其具备多个文件副本，属于文件级RAD1,具有容错能力。因为数据分散在多个Bick中，所以读性能得到很大提升，但写性能下降。- 分布式条带卷(Distribute Stripe volume):Brick Server数量是条带数(数据块分布的Brick数量)的倍数，兼具分布式卷和条带卷的特点。- 分布式复制卷(Distribute Replica volume):Brick Server数量是镜像数（数据副本数量）的倍数，兼具分布式卷和复制卷的特点。- 条带复制卷(Stripe Replica volume):类似RAID10,同时具有条带卷和复制卷的特点。- 分布式条带复制卷(Distribute Stripe Replicavolume):三种基本卷的复合卷，通常用于类Map- Reduce应用。
#### 6、GFS多卷的创建：

##### 分布式卷：

<img alt="" height="56" src="https://img-blog.csdnimg.cn/direct/e821c4140e5d4df2837071eea57cc8db.png" width="817">

##### 条带卷：

<img alt="" height="55" src="https://img-blog.csdnimg.cn/direct/29e45c27397e4b03b38a43ec348933e8.png" width="826">

##### 复制卷：

<img alt="" height="50" src="https://img-blog.csdnimg.cn/direct/6ff47657f5174893b33e6bc5f76f6c18.png" width="828">

##### 分布式条带卷：

<img alt="" height="61" src="https://img-blog.csdnimg.cn/direct/2995d33b26bc4555b9b16742e49a4b86.png" width="830">

##### 分布式复制卷：<img alt="" height="74" src="https://img-blog.csdnimg.cn/direct/0236c96a90b9496ea531afcd9b42c2c5.png" width="845">

###### 命令解析：

1：创建中共用4台服务器，分别为：node1/node2/node3/node4。

2：node1与node2服务器分别有四块磁盘，剩下两台分别有三块磁盘。

3：其中b3/c4/d5/e6/分别为实际挂载点

4：create后面参数为卷名，卷面后面关键字为创建卷的类型。

###### 命令补充：（重要）

查看卷的信息：gluster     volume     info     卷名    //（例如上方：dis-volume）

启动卷：gluster   volume    start  卷名    //（使用前必须开启）

挂载：mount    -t   glusterfs  node1:dis-volume   /test/dis    （node1:主机，dis-volume:卷名，     test/dis:挂载点）



>  
 人生要尽全力度过每一关,不管遇到什么困难不可轻言放弃！！！ 

