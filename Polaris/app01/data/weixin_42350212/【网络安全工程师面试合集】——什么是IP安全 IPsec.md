
--- 
title:  【网络安全工程师面试合集】——什么是IP安全 IPsec 
tags: []
categories: [] 

---
>  
 大家好，我是Lex 喜欢欺负超人那个Lex 
 擅长领域：python开发、网络安全渗透、Windows域控Exchange架构 
 代码干货满满，建议收藏+实操！！！有问题及需要，请留言哦~~ 


## <img alt="" height="458" src="https://img-blog.csdnimg.cn/ac00da8cdfda43f183b7e8a0959768f7.gif" width="360">



### 2.10.1. 简介

IPsec（IP Security）是IETF制定的三层隧道加密协议，它为Internet上传输的数据提供了高质量的、可互操作的、基于密码学的安全保证。特定的通信方之间在IP层通过加密与数据源认证等方式，提供了以下的安全服务：

 <li> 数据机密性（Confidentiality） 
  <ul>
   - IPsec发送方在通过网络传输包前对包进行加密。
  
数据完整性（Data Integrity）

   - IPsec接收方对发送方发送来的包进行认证，以确保数据在传输过程中没有被篡改。
  
数据来源认证（Data Authentication）

   - IPsec在接收端可以认证发送IPsec报文的发送端是否合法。
  
防重放（Anti-Replay）

   - IPsec接收方可检测并拒绝接收过时或重复的报文。
  
### 2.10.2. 优点

IPsec具有以下优点：

 &lt;
