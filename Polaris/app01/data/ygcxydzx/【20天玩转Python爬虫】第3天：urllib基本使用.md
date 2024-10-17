
--- 
title:  【20天玩转Python爬虫】第3天：urllib基本使用 
tags: []
categories: [] 

---
上次文章中我们介绍了http协议，包含请求和响应部分。请求就是客户端向服务器端发送请求信息，服务器收到请求后，处理请求并返回响应。

<img alt="" height="466" src="https://img-blog.csdnimg.cn/20210618102053437.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lnY3h5ZHp4,size_16,color_FFFFFF,t_70" width="638">

通过上图和前一章爬虫我们了解到，平时我们使用浏览器访问一些网站就是使用了HTTP协议。那同理网络爬虫也是要使用HTTP协议才可以发出请求和获取响应。

电脑或者笔记本是使用了浏览器（比如IE、Chrom、Safari等），通过浏览器我们就可以看到丰富多彩、包罗万象的网络信息。那如果我们使用网络爬虫来去访问Web服务器，Python编程是用什么发出了请求，又获取的响应呢？

在Python中，我们可以使用urllib模块和requests模块。本篇我们主要围绕urllib模块来去介绍。

首先urllib是Python自带的标准库，无需安装，可以直接使用。如果想系统性的学习urllib库，可以直接看它的官方文档。官方文档:

https://docs.python.org/zh-cn/3.7/library/urllib.html

首先，我们看一下urllib库的官方文档：

<img alt="" height="208" src="https://img-blog.csdnimg.cn/20210618102214704.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lnY3h5ZHp4,size_16,color_FFFFFF,t_70" width="745">

大家可以发现文档是把urllib分成了4部分：

 1. urllib.request请求模块
 1. urllib.error 异常处理模块
 1. urllib.parse 解析模块
 1. urllib.robotparser 文件解析模块

我们本篇也是围绕这4部分展开讲解。

## urllib.request请求模块

urllib.request 模块提供了最基本的构造 HTTP 请求的方法，利用它可以模拟浏览器的一个请求发起过程，同时它还带有处理 authenticaton （授权验证）， redirections （重定向)， cookies (浏览器Cookies）以及其它内容。

>  
 urllib.request.urlopen(url, data=None, [timeout, ]*, context=None) 打开统一资源定位地址 url，url可以是一个字符串或一个Request对象，返回一个HTTPResponse对象 参数说明： url就是要访问的网页的地址 data （附加参数）可选的，如果要添加 data ，它要求是字节流编码格式的内容即 bytes 类型，通过 bytes() 函数可以进行转化，另外如果你传递了这个 data 参数，它的请求方式就不再是 GET 方式请求，而是 POST 。 timeout （超时时间） 设置网站访问超时时间 context，必须是 ssl.SSLContext 类型，用来指定 SSL 设置 


我们来看一段通过urllib.request.urlopen访问百度首页的代码。

```
# 导包
import urllib.request
# 通过urllib.request.urlopen向百度发出请求，并获取响应
response = urllib.request.urlopen('http://www.baidu.com/')
# 查看返回的response的类型
print("查看 response 响应信息类型: ",type(response))
# 获取响应码
print(response.getcode())
# 读取响应内容
page = response.read()
# 打印响应内容
print(page)
```
