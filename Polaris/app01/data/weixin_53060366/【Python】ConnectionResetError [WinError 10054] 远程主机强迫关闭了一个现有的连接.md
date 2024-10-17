
--- 
title:  【Python】ConnectionResetError [WinError 10054] 远程主机强迫关闭了一个现有的连接 
tags: []
categories: [] 

---
## 【Python】ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接

>  
 今天在学习python时，遇到了一个问题，这个问题比较简单，但是网络上的答案众多，参差不齐，有说用try-expect重复调用函数的，还有设置response.close()，这都是觉得的答案，接下来我总结了一下我遇到的问题： 


今天写了一个用连接客户端与服务端脚本的脚本，主要功能是客户端给服务端发送命令，然后服务端执行，执行完后服务端给客户端返回执行结果。但是给我报错：

```
TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。

```

<img src="https://img-blog.csdnimg.cn/a0fb3b374ff24b1087e145db4947ea44.png#pic_center" alt="在这里插入图片描述">

查看了一下报错的原因，说是请求超时了，需要添加一个超时参数timeout，在创建socket前设置：

```
import socket
socket.setdefaulttimeout(500)

```

<mark>设置完果然不报错了，都是小问题啦。结果没高兴一会儿又给我报另一个错了！！</mark>

<img src="https://img-blog.csdnimg.cn/6d63f062723d4e639809f975ac815ad4.png#pic_center" alt="在这里插入图片描述">

继续网上找解决方案，结果很多都是说这是爬虫被服务器识别出来，服务端关闭了这个socket连接。但是这是我自己的服务器啊！我服务端的代码并没有关闭这个socket连接，为什么还会报这个错。

>  
 因为问题定位不清晰，网上搜了好久，终于找到了这篇博客：Python+socket完美实现TCP长连接保持存活 
 在网络开发使用TCP协议实现客户端和服务端通信时，某些场合需要保持长连接，在默认情况下，超过一定时间没有数据收发操作时，连接会自动断开，从而导致数据丢失。 


**客户端在创建socket之后，设置心跳：**

```
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))

```
