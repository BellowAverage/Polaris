
--- 
title:  FastDFS文件存储 
tags: []
categories: [] 

---
## FastDFS文件存储

#### 1. FastDFS介绍
- 用`c语言`编写的一款开源的轻量级分布式文件系统。- 功能包括：文件存储、文件访问（文件上传、文件下载）、文件同步等，解决了大容量存储和负载均衡的问题。特别适合以文件为载体的在线服务，如相册网站、视频网站等等。- 为互联网量身定制，充分考虑了冗余备份、负载均衡、线性扩容等机制，并注重高可用、高性能等指标。- 可以帮助我们搭建一套高性能的文件服务器集群，并提供文件上传、下载等服务。 <img src="https://img-blog.csdnimg.cn/20200211130210944.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><li>FastDFS架构包括Client、Tracker server和Storage server 
  <ul>- `Client`请求`Tracker`进行文件上传、下载，`Tracker`再调度`Storage`完成文件上传和下载。- Storage群中的**横向可以扩容，纵向可以备份**。
#### 2. FastDFS上传和下载流程

<img src="https://img-blog.csdnimg.cn/20200211130242790.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

#### 3. FastDFS文件索引

<img src="https://img-blog.csdnimg.cn/20200211130359835.png" alt="在这里插入图片描述">
<li> FastDFS上传和下载流程可以看出都涉及到一个数据叫文件索引（file_id）。 
  <ul>- **文件索引（file_id）**是客户端上传文件后Storage返回给客户端的一个字符串，是以后访问该文件的索引信息。
文件索引（file_id）信息包括：组名、虚拟磁盘路径、数据两级目录、文件名等信息。
- **组名**：文件上传后所在的 Storage 组名称。- **虚拟磁盘路径**：Storage 配置的虚拟路径，与磁盘选项`store_path*`对应。如果配置了`store_path0`则是`M00`，如果配置了`store_path1`则是`M01`，以此类推。- **数据两级目录**：Storage 服务器在每个虚拟磁盘路径下创建的两级目录，用于存储数据文件。- **文件名**：由存储服务器根据特定信息生成，文件名包含:源存储服务器IP地址、文件创建时间戳、文件大小、随机数和文件拓展名等信息。 <img src="https://img-blog.csdnimg.cn/20200211130430358.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">