
--- 
title:  nginx负载均衡配置详解 
tags: []
categories: [] 

---
nginx作为一款企业级的代理服务器，不管是大中小各类生产项目中，均有广泛的使用，尤其是在前后端分离的项目中，nginx作为路由转发的功能是非常常用的；

在一些流量比较大的项目中，为了应对高并发的场景，后端服务往往采用集群部署，这时候，就需要使用到nginx的负载均衡功能；下面nginx 负载均衡配置详解步骤

### 实验准备

 - nginx服务器；
 - 两个后端服务；

### 实验步骤

**1、启动两个后端服务**

这里准备了两个springboot工程，编写了2个测试使用的接口，以端口号区分

```
@RestController
@RequestMapping("/api")
public class NginxController1 

    @GetMapping
    public String test1()
        return "success test1 8082";
    



```

```
@RestController
@RequestMapping("/api")
public class NginxController1 

    @GetMapping
    public String test1()
        return "success test1 8081";
    



```

启动之后，浏览器分别访问一下，确保服务是正常的




