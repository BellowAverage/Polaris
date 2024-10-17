
--- 
title:  Spring Cloud 全链路追踪实现 
tags: []
categories: [] 

---
### 1 简介

在微服务架构下存在多个服务之间的相互调用，当某个请求变慢或不可用时，我们如何快速定位服务故障点呢？链路追踪的实现就是为了解决这一问题，本文采用 Sleuth + Zipkin + RabbitMQ + ES + Kibana 实现。

**Spring Cloud Sleuth**

<img src="https://img-blog.csdnimg.cn/20191002090758404.png#pic_center" alt="">
- Trace：从客户端请求到系统边界，再到系统边界返回客户端响应。- Span：每一次调用埋入一个调用记录，即为 “Span”，一系列有序的 Span 构成一个 Trace。
**Zipkin** Zipkin 是由 Twitter 公司开源的一个分布式追踪系统，用于收集服务的定时数据，实现数据的收集、存储、查找和展现。提供了可插拔的数据存储方式：In-Memory、MySql、Cassandra 以及 Elasticsearch。

**RabbitMQ** RabbitMQ 是一个开源的 AMQP 实现，服务器端用 Erlang 语言编写，支持多种客户端，用于在分布式系统中存储转发消息，在易用性、扩展性、高可用性等方面表现不俗。

**Elasticsearch** Elasticsearch（ES） 是一个基于Lucene构建的开源、分布式、RESTful 接口的全文搜索引擎。Elasticsearch 还是一个分布式文档数据库，其中每个字段均可被索引，而且每个字段的数据均可被搜索，ES 能够横向扩展至数以百计的服务器存储以及处理 PB 级的数据。可以在极短的时间内存储、搜索和分析大量的数据。

**Kibana** Kibana 可以为 Logstash 和 ElasticSearch 提供友好的日志分析 Web 界面，可以实现汇总、分析和搜索重要数据日志。

### 2 快速上手

##### 2.1 Zipkin 服务端

创建 zipkin-server 项目（也可到官方网站：  下载 JAR 包直接使用）

1）添加依赖

```
&lt;dependency&gt;
  &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
  &lt;artifactId&gt;spring-cloud-starter-netflix-eureka-client&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;io.zipkin.java&lt;/groupId&gt;
  &lt;artifactId&gt;zipkin-server&lt;/artifactId&gt;
  &lt;version&gt;2.11.8&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;io.zipkin.java&lt;/groupId&gt;
  &lt;artifactId&gt;zipkin-autoconfigure-ui&lt;/artifactId&gt;
  &lt;version&gt;2.11.8&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;io.zipkin.java&lt;/groupId&gt;
  &lt;artifactId&gt;zipkin-autoconfigure-collector-rabbitmq&lt;/artifactId&gt;
  &lt;version&gt;2.11.8&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;io.zipkin.java&lt;/groupId&gt;
  &lt;artifactId&gt;zipkin-autoconfigure-storage-elasticsearch-http&lt;/artifactId&gt;
  &lt;version&gt;2.8.4&lt;/version&gt;
&lt;/dependency&gt;

```

2）添加配置

```
spring:
  application:
    name: zipkin-server
server:
  port: 8033
eureka:
  client:
    serviceUrl:
      defaultZone: http://localhost:8088/eureka/
  instance:
      prefer-ip-address: true
management:
  metrics:
    web:
      server:
        auto-time-requests: false
zipkin:
  collector:
    rabbitmq:
      addresses: 192.168.233.128
      port: 5672
      username: zipkin
      password: zipkin
      virtual-host: vh1
      queue: zipkin
  storage:
    StorageComponent: elasticsearch
    type: elasticsearch
    elasticsearch:
      hosts: 192.168.233.171:9200
      cluster: elasticsearch
      index: zipkin
      index-shards: 5
      index-replicas: 1

```

3）启动类

```
@SpringBootApplication
@EnableEurekaClient
@EnableZipkinServer
public class ZipkinServerApplication {<!-- -->
  public static void main(String[] args) {<!-- -->
    SpringApplication.run(ZipkinServerApplication.class, args);
  }
}

```

访问 `http://localhost:8033/zipkin/` ，如图所示：

<img src="https://img-blog.csdnimg.cn/20191002085037471.jpg#pic_center" alt="">

##### 2.2 Zipkin 客户端

1）添加依赖

```
&lt;dependency&gt;
  &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
  &lt;artifactId&gt;spring-cloud-starter-netflix-eureka-client&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
  &lt;artifactId&gt;spring-boot-starter-amqp&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
  &lt;artifactId&gt;spring-cloud-starter-sleuth&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
  &lt;artifactId&gt;spring-cloud-starter-zipkin&lt;/artifactId&gt;
&lt;/dependency&gt;

```

2）添加配置

```
spring:
  sleuth:
    sampler:
      probability: 1.0
  zipkin:
    sender:
      type: RABBIT
  rabbitmq:
    addresses: 192.168.233.128
    port: 5672
    username: zipkin
    password: zipkin
    virtual-host: vh1

```

##### 2.3 测试

1）访问 Zipkin 客户端服务，如我本地 user-server `http://localhost:8061/user/findAll`

<img src="https://img-blog.csdnimg.cn/20191002085502767.jpg#pic_center" alt="">

2）点 “Find Traces”，看一下 Zipkin 服务端，如图所示：

<img src="https://img-blog.csdnimg.cn/20191002085611918.jpg#pic_center" alt=""> 3）访问 `http://192.168.233.171:5601` ，看一下 Kibana，配置一个index pattern，如图所示：

<img src="https://img-blog.csdnimg.cn/20191002085733423.jpg#pic_center" alt="">

4）修改默认时间格式，如图所示：

<img src="https://img-blog.csdnimg.cn/20191002085830735.jpg#pic_center" alt="">

5）看一下效果

<img src="https://img-blog.csdnimg.cn/20191002085920714.jpg#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
