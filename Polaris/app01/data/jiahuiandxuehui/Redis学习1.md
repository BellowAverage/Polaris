
--- 
title:  Redis学习1 
tags: []
categories: [] 

---
## NOSql型数据库

>  
 NoSQL（Not Only SQL）是一种数据库管理系统的范畴，它不使用传统的关系型数据库管理系统（RDBMS）模型。相对于传统的关系型数据库，NoSQL 数据库在数据存储和检索方面提供了更多的灵活性和可伸缩性，通常适用于不同类型的应用场景。以下是一些常见的 NoSQL 数据库类型和其特点： 
 文档数据库（Document Database）： 
 代表：MongoDB、CouchDB 特点：数据以文档的形式存储，通常使用 JSON 或 BSON 格式。这种数据库适用于具有半结构化或不确定性数据的应用程序，例如博客平台或内容管理系统。 
 键值存储（Key-Value Store）： 
 代表：Redis、Amazon DynamoDB 特点：数据以键值对的形式存储，非常适合需要快速读取和写入数据的应用程序，如缓存系统。 列族数据库（Column-family Database）： 
 代表：Apache Cassandra、HBase 特点：数据以列族的形式存储，适用于需要大规模存储和高度可扩展性的应用程序，如分布式日志记录和时间序列数据。 


>  
 图数据库（Graph Database）： 
 代表：Neo4j、Amazon Neptune 特点：用于存储和查询图形数据，适用于社交网络、推荐系统和网络分析等应用程序。 


>  
 搜索引擎（Search Engine）： 
 代表：Elasticsearch、Apache Solr 特点：专门用于全文搜索和复杂查询的数据库，适用于日志分析、实时搜索和内容检索应用。 


>  
 对象存储数据库（Object Store）： 
 代表：Amazon S3、Google Cloud Storage 特点：主要用于存储大规模二进制或非结构化数据，例如图片、视频和文档。这些服务通常在云环境中使用。 
 时序数据库（Time-Series Database）： 
 代表：InfluxDB、OpenTSDB 特点：专门用于存储和查询时间序列数据，如传感器数据、监控指标和日志数据。 选择合适的 NoSQL 数据库取决于应用程序的需求，包括数据模型、性能要求、可扩展性和一致性要求等因素。通常，NoSQL 数据库更适用于大规模、高度分布式、半结构化或不规则数据的应用程序，而关系型数据库更适用于需要强一致性和复杂事务的应用程序。不同的数据库类型在不同的应用场景中都有其优势。 


ACID：事务的四个特性原子性（atomicity，或称不可分割性）、一致性（consistency）、隔离性（isolation，又称独立性）、持久性（durability）。

#### 单体架构面临的问题

<img src="https://img-blog.csdnimg.cn/231dafe8e2af4df1a0fc1c169254b8d2.png" alt="在这里插入图片描述">

#### 使用负载均衡分布式集群

<img src="https://img-blog.csdnimg.cn/3d9e29566a064f4c9345ad5c150ae879.png" alt="在这里插入图片描述">

##### 解决CPU问题

<img src="https://img-blog.csdnimg.cn/e295700ea1374c65a34c6036fdf5e9bb.png" alt="在这里插入图片描述">

##### 解决IO压力

<img src="https://img-blog.csdnimg.cn/bb7999e27e124786b6fac59144f6564f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/be4247a9e54241d19d70be7f76cc030f.png" alt="在这里插入图片描述">

## 单线程+多路IO复用技术

<img src="https://img-blog.csdnimg.cn/f0eb0040a31045f4827d6b1fed8b4add.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/041c0571927348feaa2f6db671b0a2d4.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/dd0582cebb1040279acd62108b585784.png" alt="在这里插入图片描述"> Redis 使用了一种称为 “I/O 多路复用” 的技术来提高其性能和并发处理能力。I/O 多路复用是一种高效的 I/O 处理机制，允许一个进程同时监听多个文件描述符（通常是套接字或文件），并在其中任何一个文件描述符准备好进行读取或写入时，立即执行相应的操作，而不需要阻塞等待。

在 Redis 中，I/O 多路复用机制主要用于处理客户端连接和网络通信，以及处理持久性操作（例如 RDB 快照和 AOF 日志追加）。

以下是 Redis 中的 I/O 多路复用的一些关键要点：

>  
 事件循环：Redis 使用一个事件循环来监听客户端套接字和持久性操作的事件。这个事件循环在 Redis 主线程中运行，它使用操作系统提供的I/O 多路复用机制来检测文件描述符上的可读和可写事件。 


>  
 客户端连接：当有新的客户端连接请求时，Redis 使用 I/O 多路复用机制来接受连接并将新的客户端套接字添加到事件循环中以进行后续通信。 


>  
 非阻塞操作：Redis 的网络通信和持久性操作都是非阻塞的，这意味着 Redis 不会等待数据准备就绪，而是通过事件循环轮询检查数据是否可读或可写。这种方式允许 Redis 在处理多个客户端请求时保持高效。 


>  
 文件事件处理器：Redis 使用文件事件处理器来处理不同类型的事件，包括套接字事件和持久性事件。它可以同时处理多个事件，以提高并发性能。 


>  
 复用系统调用：Redis 使用操作系统提供的 I/O 多路复用系统调用，如 select、poll 或更高效的 epoll（在Linux上）或 kqueue（在BSD上），以便在多个文件描述符上等待事件。 


I/O 多路复用是 Redis 高性能的关键因素之一，它允许 Redis 在单线程或多线程模式下高效地处理大量的并发请求。这种设计使得 Redis 特别适用于读密集型工作负载，如缓存和实时分析，以及需要保持低延迟的应用程序。同时，Redis 也支持多个客户端同时连接，每个客户端都可以独立进行读写操作，而不会相互阻塞。这使得 Redis 成为了许多现代应用中的首选数据存储和缓存解决方案之一。
