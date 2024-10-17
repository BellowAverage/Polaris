
--- 
title:  01 MongoDB的概述、应用场景、下载方式、连接方式和发展历史等 
tags: []
categories: [] 

---
基础篇（能解决工作中80%的问题）:
1.   1.   1.   1.   1.   1.   
进阶篇:
1.   1.   1.   1.   1.   1.   1.   
其它:
1.   1.   
#### 一. mongo概述

##### 1.1 参考学习网站

官网地址：

官方文档：

菜鸟教程: 

w3cschool: 

书栈网: 

##### 1.2 MongoDB的介绍

MongoDB 是一个可拓展、开源、表结构自由、用 C++ 语言编写且面向文档的高性能分布式数据库。为 WEB 应用提供可扩展的高性能数据存储解决方案。

MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。

MongoDB 将数据存储为一个文档，数据结构由键值(key=&gt;value)对组成。MongoDB 文档类似于 JSON 对象。字段值可以包含其他文档，数组及文档数组。

附：

##### 1.3 MongoDB适合做什么

mongo适合存储大量关联性不强的数据；大批量，高并发，不规则；

mongo存储结构: 库、集合、文档、字段，和mysql: 库、表、行、列非常像。

但mongo不需要预先定义表结构，数据的字段可以任意变动，并发写入的速度也远远超过关系型数据库。

##### 1.4 MongoDB主要特点
- **面向集合存储：** 容易存储json类型和对象类型的数据，操作起来比较简单；- **支持查询以及动态查询：** MongoDB 支持丰富的查询操作，MongoDB 几乎支持SQL中的大部分查询。查询指令使用JSON形式的标记，可轻易查询文档中内嵌的对象及数组；- **多语言支持：** 如python, java, c++, php, C#等。- **自带强大的计算框架：**：关系型数据库提供了group by等分组聚集函数，而mongo提供了更加强大的MapReduce方案，同时MongoDB还提供了Spark连接器，为海量数据的统计，分析提供了便利性。Mongodb中的Map/reduce主要是用来对数据进行批量处理和聚合操作。Map函数调用emit(key,value)遍历集合中所有的记录，将key与value传给Reduce函数进行处理。- **复制集保证数据的高可用性：** MongoDB支持复制集（replset）,复制集支持备份、自动故障转移等特性。MongoDB 支持主从复制机制，可以实现数据备份、故障恢复、读扩展等功能。而基于副本集的复制机制提供了自动故障恢复的功能，确保了集群数据不会丢失。- **多文档事务的支持：** 4.0版本开始支持复制集部署模式，该特性在4.2版本更加完善，并开始支持分片集群部署模式。这个关键特性促使mongo具有关系型数据库的高并发能力，能够支持对ACID要求比较高的应用场景，从而替代关系型数据库；- **分片集群实现高可拓展性：** MongoDB支持自动分片sharding，分片的功能是实现海量数据分布式存储，分片通常与复制集配合起来使用，实现读写分离，负载均衡。- **模式自由：** 表结构可拓展，集合(表)中文档(一行记录)的字段(拥有的列)是可以变化的。- **支持完全索引：** 可以在任意属性上建立索引，包含内部对象。MongoDB的索引和RDBMS 的索引基本一样，可以在指定属性、内部对象上创建索引以提高查询的速度。除此之外，MongoDB 还提供创建基于地理空间的索引的能力。- **支持聚合：**；MongoDB提供强大的聚合工具，如count、group 等，支持使用MapReduce 完成复杂的聚合任务。- **使用高效的二进制数据存储：** 包括大型对象（如视频）。使用二进制格式存储，可以保存任何类型的数据对象。- **可以通过网络访问：** 可以通过网络远程访问MongoDB 数据库。- **GridFS功能：** GridFS是MongoDB中的一个内置功能，可以用于存放大量小文件。
##### 1.5 MongoDB主要应用场景：

**1. `网站实时数据处理`**：它非常适合实时的插入、更新与查询，并具备网站实时数据存储所需的复制及高度伸缩性。

**2. `缓存`**：由于性能很高，它适合作为信息基础设施的缓存层。在系统重启之后，由它搭建的持久化缓存层可以避免下层的数据源过载。

**3. `高伸缩性的场景`**：非常适合由数十或数百台服务器组成的数据库，它的路线图中已经包含对MapReduce引擎的内置支持。

**4. `大尺寸、低价值的数据`**：使用传统的关系型数据库存储一些数据时可能会比较昂贵，在此之前，很多时候程序员往往会选择传统的文件进行存储。

**5. `用于对象及JSON 数据的存储`**： Mongo 的BSON 数据格式非常适合文档化格式的存储及查询。

**不适用的场景如下**： 1）要求高度事务性的系统：例如，银行或会计系统。传统的关系型数据库目前还是更适用于需要大量原子性复杂事务的应用程序。

2）传统的商业智能应用：针对特定问题的BI 数据库会产生高度优化的查询方式。对于此类应用，数据仓库可能是更合适的选择。

3）复杂的跨文档（表）级联查询。

##### 1.6 MongoDB 应用案例

下面列举一些公司MongoDB的实际应用：
1.  **Craiglist** 上使用MongoDB的存档数十亿条记录。 1.  **FourSquare**，基于位置的社交网站，在Amazon EC2的服务器上使用MongoDB分享数据。 1.  **Shutterfly**，以互联网为基础的社会和个人出版服务，使用MongoDB的各种持久性数据存储的要求。 1.  **bit.ly**, 一个基于Web的网址缩短服务，使用MongoDB的存储自己的数据。 1.  **spike.com**，一个MTV网络的联营公司， spike.com使用MongoDB的。 1.  **Intuit公司**，一个为小企业和个人的软件和服务提供商，为小型企业使用MongoDB的跟踪用户的数据。 1.  **sourceforge.net**，资源网站查找，创建和发布开源软件免费，使用MongoDB的后端存储。 1.  **etsy.com** ，一个购买和出售手工制作物品网站，使用MongoDB。 1.  **纽约时报**，领先的在线新闻门户网站之一，使用MongoDB。 1.  **CERN**，著名的粒子物理研究所，欧洲核子研究中心大型强子对撞机的数据使用MongoDB。 
##### 1.7 常见编程语言操作MongoDB案例

python 操作monog: 

java 操作mongo: 

php 操作mongo: 

nodejs 操作mongo: 

#### 二. mongo的下载及驱动支持

可以在mongodb官网下载该安装包，mongo各平台下载地址: 

1、Windows 安装可参考: 

2、linux 安装可参考: 

3、mac 安装可参考: 

MongoDB有官方的驱动如下： C、C++、C# 、.NET、Erlang、Haskell、Java、JavaScript、Lisp、node.JS、Perl、PHP、Python、Ruby、Scala、Go等等。

#### 三. MongoDB工具和连接方式

##### 3.1 监控工具：

MongoDB提供了网络和系统监控工具Munin，它作为一个插件应用于MongoDB中。 Gangila是MongoDB高性能的系统监视的工具，它作为一个插件应用于MongoDB中。 基于图形界面的开源工具 Cacti, 用于查看CPU负载, 网络带宽利用率,它也提供了一个应用于监控 MongoDB 的插件。

##### 3.2 可视化界面:

Fang of Mongo – 网页式,由Django和jQuery所构成。 Futon4Mongo – 一个CouchDB Futon web的mongodb山寨版。 Mongo3 – Ruby写成。 MongoHub – 适用于OSX的应用程序。 Opricot – 一个基于浏览器的MongoDB控制台, 由PHP撰写而成。 Database Master — Windows的mongodb管理工具 RockMongo — 最好的PHP语言的MongoDB管理工具，轻量级, 支持多国语言。

##### 3.3 标准 URI 连接语法：

`mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]`

如使用用户名密码连接: `mongodb://admin:123456@localhost/test` 以安全模式连接到replica set，并且等待至少两个复制服务器成功写入，超时时间设置为2秒: `mongodb://host1,host2,host3/?safe=true;w=2;wtimeoutMS=2000`

**参数说明：**: `mongodb://` 这是固定的格式，必须要指定。

`username:password@` 可选项，如果设置，在连接数据库服务器之后，驱动都会尝试登录这个数据库

`host1` 必须的指定至少一个host, host1 是这个URI唯一要填写的。它指定了要连接服务器的地址。如果要连接复制集，请指定多个主机地址。

`portX` 可选的指定端口，如果不填，默认为27017

`/database` 如果指定username:password@，连接并验证登录指定数据库。若不指定，默认打开 test 数据库。

`?options` 是连接选项。如果不使用/database，则前面需要加上/。所有连接选项都是键值对name=value，键值对之间通过&amp;或;（分号）隔开

**连接选项说明：** `1. replicaSet=name`: 验证replica set的名称, 如：Impliesconnect=replicaSet.

`2. slaveOk=true|false`:

>  
 true:在connect=direct模式下，驱动会连接第一台机器，即使这台服务器不是主。在connect=replicaSet模式下，驱动会发送所有的写请求到主并且把读取操作分布在其他从服务器。 false: 在 connect=direct模式下，驱动会自动找寻主服务器. 在connect=replicaSet 模式下，驱动仅仅连接主服务器，并且所有的读写命令都连接到主服务器。 


`3. safe=true|false`:

>  
 true: 在执行更新操作之后，驱动都会发送getLastError命令来确保更新成功。(还要参考 wtimeoutMS). false: 在每次更新之后，驱动不会发送getLastError来确保更新成功。 


`4. w=n`: 驱动添加 { w : n } 到getLastError命令. 应用于safe=true。

`5. wtimeoutMS=ms`: 驱动添加 { wtimeout : ms } 到 getlasterror 命令. 应用于 safe=true.

`6. fsync=true|false`:

>  
 true: 驱动添加 { fsync : true } 到 getlasterror 命令.应用于 safe=true. false: 驱动不会添加到getLastError命令中。 


`7. journal=true|false`: 如果设置为 true, 同步到 journal (在提交到数据库前写入到实体中). 应用于 safe=true

`8. connectTimeoutMS=ms`: 可以打开连接的时间。

`9. socketTimeoutMS=ms`: 发送和接受sockets的时间。

#### 四. mongo的发展历史

`2007年`，Mongodb由位于纽约的一个名为10gen的组织开发，现在被 称为MongoDB

`2009年`，经过将近2年的开发，10gen开发了出了MongoDB的皱形并将它开源以及正式命名为mongoDB，同时成立开源社区，通过社区运营MongoDB。

`2009 年 2 月`发布了MongoDB 1.0 ，提供了大部分基本的查询功能。

`2009 年 12 月`发布了 MongoDB 1.2 引入了 map-reduce，支持大规模数据处理。在看到 MongoDB 的巨大潜力之后，10gen 公司迅速壮大了团队。

`2010 年 3 月 `发布了MongoDB 1.4，引入了后台索引创建。据说这是mongoDB第一个真正的产品

`2010 年 8 月 `发布了MongoDB 1.6 ) 引入了一些主要特性，比如用于水平伸缩的分片、具备自动故障转移能力的副本集以及对 IPv6 的支持。到了 2012 年，10gen 有 100 名员工，公司开始提供 24/7 服务。

`2012 年 5 月 23 日`，发布了 MongoDB2.1 .该版本采用全新架构，包含诸多增强。

`2012 年 6 月 6 日` ，发布了MongoDB2.0.6 ，分布式文档数据库。

`2012 年 8 月`，MongoDB 2.2 版本 发布 ，引入了聚合管道，可以将多个数据处理步骤组合成一个操作链。

`2013 年` MongoDB推出第一款商业版本MongoDB Enterprise Advanced

`2013 年 4 月 23 日`， MongoDB 2.4.3 发布，此版本包括了一些性能优化，功能增加以及bug修复

`2013 年 8 月 20 日`，MongoDB 2.4.6 发布，仍然是以性能优化，功能增强及bug修复为主

`2015 年 3 月 `MongoDB 3.0 发布，包含了新的，WiredTiger 存储引擎、可插拔存储引擎API，增加了50个副本集限制和安全改进，同年晚些时候又发布了3.2版本，支持文档验证、部分索引和一些主要的聚合增加。

`2016 年 `MongoDB推出了 Atlas服务，MongoDB Atlas 与公有云服务厂商（谷歌、微软Azure）合作，这一年，MongoDB 爆出了非常严重的安全门事件，黑客通过MongoDB 的默认监听地址 0.0.0.0删除数据，并且通过此漏洞进行勒索，支付0.2到0.5的比特币就可以恢复数据。

`2017 年 10 月` MongDB 公司成立10周年之际，顺利通过IPO在 纽交所上市，开盘24美元，公司估值达到16亿美元，并获得1.92亿美元的筹资。

`2017 年 11 月 `发布 MongoDB 3.6 ，为多集合连接查询、变更流和使用 JSON 模式进行文档验证提供了更好的支持。

`2018 年 6 月 `发布 MongoDB 4.0，这一版本发布获得了广泛的关注， 提供了跨文档事务处理能力。这是一个重要的里程碑，MongoDB 已经为高数据完整性需求做好了准备。

`2019 年 3 月 18 日`， Forrester授予MongoDB NoSQL 领导者称号

`2019 年 10 月` MongoDB 4.2 发布 ，开始支持分布式事务。

`2020 年 10 月` ， MongoDB的社区版版本是4.4.1,扩展性和性能增强，降低复制延迟，可用性和容错性增强，查询能力和易用性增强，MongoDB云平台的功能更新。MongoDB 逐渐的从一个专注于数据库服务的厂商，转变为提供数据平台服务的厂商。

截至`2021 年 7 月` MongoDB发布最新5.0版本，支持了时间序列数据平台、在线重新分片、版本化API等新特性，在应用场景覆盖面、数据管理效率、应用程序兼容性等方面做了很大增强。

现在的MongoDB，截至 2020 年，MongoDB 的全球下载量达到了 1.1 亿次。MongoDB 公司目前有 2000 多名员工，有超过 18000 名付费客户，其中有很多客户同时使用 MongoDB Atlas 和 MongoDB 企业版。截至 2020 年 8 月，MongoDB 社区版版本是 4.4。大多数大公司在内部的一些场景中使用社区版。MongoDB 社区版仍然是开源的，除了一些关键特性外，它与 MongoDB 企业版差不多。

❤️ 如果觉得有用，感谢一键三连哦 ！！！❤️
