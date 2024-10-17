
--- 
title:  springboot+nacos动态配置-个人笔记 
tags: []
categories: [] 

---
### 导包

**版本自己选**

```
&lt;dependency&gt;
    &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
    &lt;artifactId&gt;spring-cloud-starter-alibaba-nacos-config&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
    &lt;artifactId&gt;spring-cloud-starter-alibaba-nacos-discovery&lt;/artifactId&gt;
&lt;/dependency&gt;

```

### nacos配置文件

<img src="https://img-blog.csdnimg.cn/20210319184257256.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### bootstrap.yml

>  
 bootstrap.yml会比application.yml优先加载 


<img src="https://img-blog.csdnimg.cn/20210319183859375.png" alt="在这里插入图片描述">

### springboot配置文件

```
spring:
  application:
    name: cca-admin-service
  profiles:
    active: test
  cloud:
    nacos:
      server-addr: #nacos地址
      config:
        enabled: true
        file-extension: yml
        refresh-enabled: true
        namespace: cca
        extension-configs:
          - data-id: api-common.yml
            refresh: true
          - data-id: redis.yml
            refresh: true
          - data-id: arango.yml
            refresh: true
          - data-id: rabbitmq.yml
            refresh: true
      discovery:
        enabled: true
        namespace: cca
        ip: admin.${<!-- -->spring.profiles.active}.cca.pub
        service: CCA-ADMIN-SERVICE

```

### 时间配置方式

>  
 在有些业务中，我们需要配置过期时间，但是我们又不想定义时间戳那种不直观的类型，我们可以使用以下这种 


**nacos配置**

>  
 d这个代表天，也可以使用比较常见的日期后缀 


```
invite: 7d

```

**实体类接口定义**

```
private Duration invite;

```

**用法例子**

```
setCache.add(key, userNoticeProperties.getCommunityUserCircleInvite().toMillis(), TimeUnit.MILLISECONDS);

```
