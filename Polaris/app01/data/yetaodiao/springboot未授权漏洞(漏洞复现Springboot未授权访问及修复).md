
--- 
title:  springboot未授权漏洞(漏洞复现Springboot未授权访问及修复) 
tags: []
categories: [] 

---
### 1、springboot未授权漏洞问题描述 Actuator 是Springboot提供的用来对应用系统进行自省和监控的功能模块，借助于Actuator开发者可以很方便地对应用系统某些监控指标进行查看、统计等。

Actuator 的核心是端点 Endpoint，它用来监视应用程序及交互，spring-boot-actuator 中已经内置了非常多的Endpoint（health、info、beans、metrics、httptrace、shutdown等等），同时也允许我们自己扩展自己的Endpoints。每个 Endpoint 都可以启用和禁用。要远程访问 Endpoint，还必须通过 JMX 或 HTTP 进行暴露，大部分应用选择HTTP。

Actuator 在带来方便的同时，如果没有管理好，会导致一些敏感的信息泄露；可能会导致我们的服务器，被暴露到外网，服务器可能会沦陷。那我们来看一下，会出现什么安全的问题？  

## 2、springboot未授权漏洞是什么？

**未授权访问漏洞可以理解为需要安全配置或权限认证的地址、授权页面存在缺陷导致其他用户可以直接访问从而引发重要权限可被操作、数据库或网站目录等敏感信息泄露。**

### **3、禁止方法 在 llsydn-dev.properties 增加配置如下**

**management.endpoints.web.exposure.exclude=env,heapdump,threaddump,mappings 复制代码 这样 env 就被禁止访问了**
