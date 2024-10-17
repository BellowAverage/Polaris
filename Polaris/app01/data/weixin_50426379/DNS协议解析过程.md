
--- 
title:  DNS协议解析过程 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li>- - - <ul><li>- - <ul><li>- 


### 一、什么是DNS协议

DNS是<mark>域名系统（Domain Name Service）<mark>的缩写，我们通常用来识别主机的方式有两种，一种是通过</mark>主机名</mark>，另外一种是通过<mark>IP地址</mark>。主机名便于我们的记忆，而路由器则更喜欢定长的、有着层次结构的IP地址。所以需要一个能<mark>将域名转变到IP地址的目录服务</mark>，这就是域名服务器存在的意义。

### 二、DNS解析过程

<img src="https://img-blog.csdnimg.cn/a9617ea5faf24990a5a0efcc054c14a9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAd2hfMTEx,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

当用户在浏览器中输入www.baidu.com的时候，DNS解析大概会有以下过程：
1. 首先浏览器会<mark>检查自身缓存</mark>是否解析过这个域名的IP地址，如果有即缓存命中，那么解析结束；1. 如果浏览器缓存中没有，那么浏览器会检查<mark>操作系统缓存</mark>中是否有相应的解析过的结果。而操作系统也有一个域名解析的过程。<mark>像我们熟悉的hosts文件</mark>，如果用户在这里定义了一个域名对应的IP地址，那么浏览器会首先使用这里定义的IP地址；1. 如果此时还没有命中域名，才会真正地去<mark>请求本地域名服务器</mark>（LDNS）来解析这个域名，这台服务器一般在你的城市的某个角落，距离你不是很远，并且这台服务器的性能很好，一般这里会缓存域名解析的结果。大约80%的域名解析到这里就完成了；1. 如果LDNS仍然没有命中，那么LDNS就会向<mark>根域名服务器</mark>（Root Server）发起域名请求解析；1. 根域名服务器返回给LDNS一个所查询域的主域名服务器（gTLD Server，国际顶尖域名服务器，如.com、.cn、.org等）地址；1. 此时LDNS再发送请求到上一步返回的gTLD的IP地址；1. 接受请求的gTLD查找并返回这个域名对应的Name Server的地址，这个Name Server就是网站注册的域名服务器；1. Name Server根据映射关系表找到目标IP地址，并将其返回给LDNS；1. LDNS缓存这个域名和对应的IP；1. LDNS把解析的结果返回给用户，用户根据TTL值缓存到本地系统缓存中，域名解析过程至此结束。
### 三、DNS服务器的体系架构

#### 1. DNS的传输层协议

从上面内容我们了解了DNS主要解析流程，<mark>DNS主要作用就是将主机域名转换为IP地址</mark>。当用户主机的DNS客户端接收到应用程序的这种转换请求时（例如调用gethostbyname()系统函数），那么就会向网络中发送一个DNS查询报文。需要了解的是，DNS请求和回答报文的下层都是<mark>使用UDP数据报</mark>经过<mark>53端口</mark>发送的。

那么为什么使用UDP（User Datagram Protocol）这样面向无连接的，尽最大能力交付的不可靠数据连接，而不是使用TCP（Transmission Control Protocol）这样的面向连接的可靠数据连接。

因为相比较与TCP来说，一次UDP域名服务器的交换可以短到只有两个报文，一个查询报文、一个响应报文。一次TCP交换则至少包含九个传送报文：三次握手初始化TCP会话、一个查询报文、一个响应报文、四次挥手的TCP中断连接（或许是八个报文，毕竟连接建立时第二个ACK报文是可以携带数据的，谁知道呢，反正也比两个报文要多）。<mark>所以考虑到效率的原因，TCP连接的开销更大，故而采用UDP作为DNS的传输层协议</mark>。

当然还有另外一点需要注意，整个DNS服务体系中，并不是只有UDP一种协议存在，上述域名解析时使用的是UDP，但是在<mark>区域传送时还是使用TCP</mark>。辅域名服务器会定时（一般是三小时）向主域名服务器进行查询以便了解数据是否有变动。如有变动，则会执行一次区域传送，进行数据同步。区域传送将使用TCP而不是UDP，因为数据同步传送的数据量比一个请求和应答的数据量要多得多，使用TCP更加可靠。

#### 2.DNS的分布式集群工作方式

DNS解析过程有两种类型：<mark>分布域名解析和集中式域名解析。</mark>

##### 集中式域名解析

DNS的一种简单设计是在因特网上只使用一个DNS服务器，该服务器包含了所有的映射。<mark>在这种集中式设计中，客户直接将所有查询直接发往单一的DNS服务器，同时该DNS服务器直接对所有的查询客户做出响应。尽管这种设计十分简单，但是由于因特网有着数据量巨大的主机。这种集中式设计会有以下问题：①单点故障：如果该DNS服务器奔溃，整个因特网随之瘫痪；②通信容量：单个DNS服务器不得不处理所有的DNS查询</mark>。

##### 分布式域名解析

所以单一DNS服务器上运行集中式数据库完全没有可扩展能力。因此，DNS采用了分布式的设计方案。

事实上<mark>DNS服务器是一种分布式并且分层次的数据库系统</mark>，从上面DNS的解析过程中我们也看出来了，DNS系统中有多种类型的DNS服务器，它们之间以层次划分开来： <img src="https://img-blog.csdnimg.cn/d8e2aa098c6547f8984cc5401535ec6c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAd2hfMTEx,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

根DNS服务器：根域名服务器提供TLD服务器的IP地址； 顶级域（DNS）服务器：对于每个顶级域（如com、org、net）都有TLD服务器（或集群服务器）。TLD服务器提供了DNS服务器的IP地址； 权威DNS服务器：在因特网上具有公共可访问主机（如Web服务器和邮件服务器）的每个组织机构必须提供公共可访问的DNS记录，这些记录将这些主机的名字映射为IP地址。多数大学和大公司是实现和维护它们自己的基本和辅助（备份）的权威DNS。

原文链接：https://blog.csdn.net/Allen_Adolph/article/details/107778499
