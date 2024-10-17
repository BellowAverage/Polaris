
--- 
title:  [SpringBoot Server]SpringBoot tomcat配置 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- <ul><li>


惯例，先摆一个。 cp配置跳转至第二章。 SpringBoot 默认嵌入的是tomcat，不同应用也提供了其他选择。

>  
 For **servlet stack applications**, the spring-boot-starter-web includes Tomcat by including spring-boot-starter-**tomcat**, but you can use spring-boot-starter-**jetty** or spring-boot-starter-**undertow** instead. For **reactive stack applications**, the spring-boot-starter-webflux includes Reactor Netty by including spring-boot-starter-reactor-**netty**, but you can use spring-boot-starter-**tomcat**, spring-boot-starter-**jetty**, or spring-boot-starter-undertow instead. 


关于服务器配置，初步的需要注意的事项为 并发数、请求响应。这些在tomcat中对应的分别是 工作线程数、最大请求连接数、响应时间。

>  
 当cpu线程数小于应用线程数时，操作系统使用时间片机制，采用线程调度算法，频繁的进行线程切换 


### 1、需要注意的通用配置

 通用配置中，个人认为需要注意的如下:
-  server.max-http-header-size Maximum size of the HTTP message header. HTTP请求头的最大大小，默认 8kb -  server.servlet.encoding.charset Charset of HTTP requests and responses. Added to the “Content-Type” header if not set explicitly. 默认HTTP请求的字符集，UTF-8 -  server.servlet.session.timeout Session timeout. If a duration suffix is not specified, seconds will be used. 默认session 超时时间为 30m -  server.ssl.enabled Whether to enable SSL support. 是否支持SSL 默认支持 true -  server.tomcat.max-http-form-post-size Maximum size of the form content in any HTTP post request. 默认 2MB -  server.tomcat.max-swallow-size Maximum amount of request body to swallow. 默认 2MB 
#### 1.1 tomca默认配置

其中，tomcat的默认配置如下: 可以看到，tomcat默认的最大工作线程数为200（Springboot 默认tomcat最大线程数），最小为10

<img src="https://img-blog.csdnimg.cn/1c962c62de964cbcabc29132db171d0a.png" alt="在这里插入图片描述">

### 2、通过application.yaml配置tomcat

```
# 并发数(工作线程数，默认就是200，最小10，按需求配置)
server.tomcat.threads.max=200
# 可维持请求数(默认是8192，不知道这个数字怎么来的，但是官网文档是这样写的)
server.tomcat.max-connections=8192
# 官网解释是请求最大列长度，英文和翻译我放下面，不会用，暂时没测出来
# Maximum queue length for incoming connection requests when all possible request processing threads are in use.(当所有可能的请求处理线程都在使用时，传入的连接请求的最大队列长度。)
server.tomcat.accept-count=100
# 设置请求超时时间
server.tomcat.connection-timeout: 30s
# 设置等待队列的请求的等待超时时间
# Time to wait for another HTTP request before the connection is closed. When not set the connectionTimeout is used. When set to -1 there will be no timeout.
server.tomcat.keep-alive-timeout: 


```

要注意的是，当最大请求连接数小于最大线程数时，tomcat处理（最大并发）以最大连接数为准。

>  
 具体测试看下一篇 


### 3、 ServerProperties类(略看一下，ServerProperties中有tomcat静态内部类)

>  
 @ConfigurationProperties for a web server (e.g. port and path settings). 


SpringBoot嵌入式网络服务器的参数配置类，也就是默认的tomcat配置类。 ServerProperties中有tomcat静态内部类，可以看到tomcat的默认配置，可以在内部静态类 Threads中看到tomcat默认的最大工作线程数，即 worker threads。 <img src="https://img-blog.csdnimg.cn/3974c6081aee47aeb6468c70cba4146b.png" alt="在这里插入图片描述">
