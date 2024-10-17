
--- 
title:  Node.js创建一个简单的服务器 
tags: []
categories: [] 

---
### 1.简介

简单的说 Node.js 就是运行在服务端的 JavaScript。为什么这么说呢，Node.js 是一个基于 Chrome JavaScript 运行时建立的一个平台，是一个事件驱动 I/O 服务端 JavaScript 环境，基于 Google 的 V8 引擎，V8 引擎执行 Javascript 的速度非常快，性能非常好。 那么让我们简单的创建一个node.js服务（前提条件你的操作平台上已经安装了node环境，网上有好多教程，我们在这篇文将就不详细介绍了）。

### 2.node服务分三部分组成：
1. require 指令：在 Node.js 中，使用 require 指令来加载和引入模块，引入的模块可以是内置模块，也可以是第三方模块或自定义模块。1. 创建服务器：服务器可以监听客户端的请求，类似于 Apache 、Nginx 等 HTTP 服务器。1. 接收请求与响应请求 服务器很容易创建，客户端可以使用浏览器或终端发送 HTTP 请求，服务器接收请求后返回响应数据。
### 3.创建服务器

#### 3.1 使用 require 指令来加载和引入模块

使用 require 指令来载入 http 模块，并将实例化的 HTTP 赋值给变量 http:

```
var http = require("http");

```

#### 3.2 创建服务器

vim server.js，使用 http.createServer() 方法创建服务器，并使用 listen 方法绑定 8888 端口。 函数通过 request, response 参数来接收和响应数据。

```
var http = require('http');

http.createServer(function (request, response) {<!-- -->

    // 发送 HTTP 头部 
    // HTTP 状态值: 200 : OK
    // 内容类型: text/plain
    response.writeHead(200, {<!-- -->'Content-Type': 'text/plain'});

    // 发送响应数据 "Hello World"
    response.end('Hello World\n');
}).listen(8888);

// 终端打印如下信息
console.log('Server running at http://127.0.0.1:9999/');

```

#### 3.3 启动服务

```
node server.js
Server running at http://127.0.0.1:9999/

```

打开浏览器访问：http://127.0.0.1:9999/，浏览器返回带有"Hello World"的网页。
