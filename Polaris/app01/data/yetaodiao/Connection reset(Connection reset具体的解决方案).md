
--- 
title:  Connection reset(Connection reset具体的解决方案) 
tags: []
categories: [] 

---
Connection reset的解决方案有如下几个：1、出错了重试；2、客户端和服务器统一使用TCP长连接；3、客户端和服务器统一使用TCP短连接。

首先是Connection reset出错了重试：这种方案可以简单防止“Connection reset”错误，然后如果服务不是“幂等”的则不能使用该方法；比如提交订单操作就不是幂等的，如果使用重试则可能造成重复提单。然后是客户端和服务器统一使用TCP长连接：客户端使用TCP长连接很容易配置（直接设置HttpClient就好），而服务器配置长连接就比较麻烦了，就拿tomcat来说，需要设置tomcat的maxKeepAliveRequests、connectionTimeout等参数。另外如果使用了nginx进行反向代理或负载均衡，此时也需要配置nginx以支持长连接（nginx默认是对客户端使用长连接，对服务器使用短连接）。

<img alt="" height="305" src="https://img-blog.csdnimg.cn/3e4a3f1b7aa247ce845c86c0501f2bbf.png" width="568">

### **Connection reset**,在TCP首部中有6个标志位，其中一个标志位为RST，用于“复位”的。无论何时一个报文 段发往基准的连接（ referenced connection）出现错误，TCP都会发出一个复位报文段。如果双方需要继续建立连接，那么需要重新进行三次握手建立连接。

### **Connection reset的原因**

导致此异常的原因，总结下来有三种情况：

1.服务器端偶尔出现了异常，导致连接关闭

解决方法：
