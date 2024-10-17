
--- 
title:  Go 语言 Web 应用怎么使用 Nginx 部署？ 
tags: []
categories: [] 

---
**目录**









## 前言

>  
 本文我们介绍怎么使用 Nginx 部署 Go 语言开发的 Web 应用，从而将 Nginx 的强大功能赋能给 Go 语言开发的 Web 应用。 


1 

### 介绍

Golang 标准库 net/http 和 Go 语言 Web 框架，比如 Gin、Beego 和 Iris 等，可以很方便地构建一个 Web 应用。

Nginx 是一个 HTTP 和反向代理服务器、一个邮件代理服务器和一个通用的 TCP/UDP 代理服务器。本文重点不是介绍 Nginx，感兴趣的读者朋友们请自行查阅 Nginx 相关资料了解更多。

为什么我们还需要使用 Nginx 部署 Go 语言开发的 Web 应用呢？

因为我们可以使用 Nginx 提供的反向代理功能，将 Go 语言开发的 Web 应用接入 Nginx，从而将 Nginx 的强大功能赋能到 Go 语言开发的 Web 应用中。

本文我们介绍怎么使用 Nginx 部署一个 Go 语言开发的 Web 应用。

2 

### 构建一个 Web 应用

首先，我们需要先构建一个 Web 应用，Gin 是一个用 Golang 编写的 HTTP Web 框架。为了方便，我们使用 Gin 框架构建一个 Web 应用。

示例代码：

```
package main

import "github.com/gin-gonic/gin"

func main() {
 r := gin.Default()
 r.GET("/ping", func(c *gin.Context) {
  c.JSON(200, gin.H{
   "message": "pong",
  })
 })
 r.Run() // 监听并在 0.0.0.0:8080 上启动服务
}
```

 阅读上面这段代码，使用 Gin 框架构建一个监听 8080 端口的 Web 应用。

运行代码，使用浏览器访问 http://YourIP:8080/ping，返回结果是 {"message":"pong"}。

3 

### 使用 Nginx 部署

使用终端通过 ssh 方式登录到 Linux 服务器，执行命令 nginx -t，通过输出结果我们可以得到 Nginx 配置文件的路径。

```
# nginx -t
nginx: the configuration file /usr/local/openresty/nginx/conf/nginx.conf syntax is ok
nginx: configuration file /usr/local/openresty/nginx/conf/nginx.conf test is successful
```

 根据输出结果可知，Nginx 配置文件的路径是 /usr/local/openresty/nginx/conf/nginx.conf。

编辑 Nginx 配置文件：

```
server {
    listen 8081;
    location / {
        proxy_pass http://127.0.0.1:8080;
    }
}
```

 在 http{} 块中，新增以上代码，Nginx 监听 8081 端口，访问 Nginx 的 8081 端口，反向代理到监听 8080 端口的 Go 语言开发的 Web 应用，如果读者朋友们有自己的域名，还可以将域名配置到 server{} 块中。

保存并退出 Nginx 配置文件后，执行命令 nginx -t 测试配置文件语法是否有误，没有问题的话，执行命令 nginx -s reload，重新加载配置文件（前提是 Nginx 已启动，如果 Nginx 还未启动，可以执行命令 nginx，启动 Nginx）。

然后，在浏览器访问 http://YourIP:8081/ping，返回结果也是 {"message":"pong"}。

4 

### 总结

本文我们介绍怎么使用 Nginx 部署 Go 语言开发的 Web 应用，从而将 Nginx 的强大功能赋能给 Go 语言开发的 Web 应用。

实际上，就是使用 Nginx 的反向代理功能，将 Nginx 监听端口收到的请求转发到 Go 语言开发的 Web 应用监听的端口上。

建议读者朋友们自行操作一遍，从而加深体会。感兴趣的读者朋友们，关于 Gin 框架 和 Nginx 的更多内容，请自行查阅参考资料了解更多。

**参考资料：**

https://gin-gonic.com/docs/ https://nginx.org/en/
