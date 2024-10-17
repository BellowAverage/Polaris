
--- 
title:  网络编程：TCP、IP、Socket 
tags: []
categories: [] 

---
## 网络编程

```
import socket
import threading

# 处理客户端的请求操作

def handle_client_request(service_client_socket, ip_port):
    # 循环接收客户端发送的数据
    while True:
        # 接收客户端发送的数据
        recv_data = service_client_socket.recv(1024)
        # 容器类型判断是否有数据可以直接使用if语句进行判断，如果容器类型里面有数据表示条件成立，否则条件失败
        # 容器类型: 列表、字典、元组、字符串、set、range、二进制数据
        if recv_data:
            print(recv_data.decode("gbk"), ip_port)
            # 回复
            service_client_socket.send("ok，问题正在处理中...".encode("gbk"))
    else:
        print("客户端下线了:", ip_port)
        break
# 终止和客户端进行通信
service_client_socket.close()

if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用，让程序退出端口号立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(("", 9090))
    # 设置监听, listen后的套接字是被动套接字，只负责接收客户端的连接请求
    tcp_server_socket.listen(128)
    # 循环等待接收客户端的连接请求
    while True:
        # 等待接收客户端的连接请求
        service_client_socket, ip_port = tcp_server_socket.accept()
        print("客户端连接成功:", ip_port)
        # 当客户端和服务端建立连接成功以后，需要创建一个子线程，不同子线程负责接收不同客户端的消息
        sub_thread = threading.Thread(target=handle_client_request, args=(service_client_socket, ip_port))
        # 设置守护主线程
        sub_thread.setDaemon(True)
        # 启动子线程
        sub_thread.start()

# tcp服务端套接字可以不需要关闭，因为服务端程序需要一直运行
# tcp_server_socket.close()

```

### IP

#### 概念
- 标识网络中设备的一个地址
#### 分类
- ipv4：点分10进制组成- ipv6：冒号16进制组成
### 端口

#### 概念
- 端口是传输数据的通道，好比教室的门，是数据传输必经之路。- 其实，每一个端口都会有一个对应的端口号，好比每个教室的门都有一个门牌号，想要找到端口通过端口号即可。
#### 端口号
- 操作系统为了统一管理这么多端口，就对端口进行了编号- 端口号有65536个。<li>分类 
  <ul><li>知名端口号 
    <ul>- 范围从0到1023- 一般程序员开发应用程序使用端口号称为动态端口号, 范围是从1024到65535。
#### 设备之间的数据传输
- 那么最终飞秋之间进行数据通信的流程是这样的，通过ip地址找到对应的设备，通过端口号找到对应的端口，然后通过端口把数据传输给应用程序。
#### 端口和端口号的关系
- 端口号可以标识唯一的一个端口。
### TCP

#### 概念
- 一种面向连接的、可靠的、基于字节流的传输层通信协议。
#### 特点
<li>面向连接 
  <ul>- 先建立连接在进行传输数据，数据传输完毕之后，断开连接释放系统资源- 采用发送应答机制- 超时重连- 错误校验- 流量控制和阻塞管理
#### 开发流程
<li> TCP 客户端程序开发 <h2>1.导包</h2> import socket <h2>2.创建客户端socket对象</h2> client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) <h2>3.与服务端socket建立连接</h2> client_socket.connect((‘192.168.36.49’, 9000)) <h2>4.发送数据</h2> send_data = ‘你好，我是客户端！’ client_socket.send(send_data.encode(‘gbk’)) <h2>5.接收数据</h2> recv_data = client_socket.recv(1024) print(recv_data.decode(‘gbk’)) <h2>6.关闭socket对象</h2> client_socket.close() 
  <ul><li> 
    - 创建客户端套接字对象 </li><li> 
    - 和服务端套接字建立连接 </li><li> 
    - 发送数据 </li><li> 
    - 接收数据 </li><li> 
    - 关闭客户端套接字 </li>
## 2.创建客户端socket对象

## 4.发送数据

## 6.关闭socket对象

TCP 服务端程序开发

## 1.导入模块

import socket

## 2.建立服务端socket对象

server_socket = socket.socket() server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

## 3.绑定端口号

server_socket.bind((’’, 8888))

## 4.设置监听

server_socket.listen(128)

## 5.等待客户端连接请求

client_socker, ip_port = (server_socket.accept()) print(‘IP为:%s \n端口号为:%s的客户端连接成功！！！’ % (ip_port[0], ip_port[1]))

## 6.接收数据

recv_data = client_socker.recv(1024).decode(‘gbk’) print(recv_data) if len(recv_data) == 0: print(‘IP为:%s \n端口号为:%s的客户端下线了！！！’ % (ip_port[0], ip_port[1])) else: print(‘IP为:%s \n端口号为:%s的客户端发送的数据为:%s’ % (ip_port[0], ip_port[1], recv_data))

## 7.发送数据

send_data = ‘不好意思！我睡着了！’ client_socker.send(send_data.encode(‘gbk’))

## 8.关闭socket

client_socker.close() server_socket.close()
<li> 
    - 导入socket模块 </li><li> 
    - 创建TCP套接字‘socket’ 
    <ul>- 参数1: ‘AF_INET’, 表示IPv4地址类型- 参数2: ‘SOCK_STREAM’, 表示TCP传输协议类型1. 绑定端口号‘bind’- 参数: 元组, 比如:(ip地址, 端口号)1. 设置监听‘listen’- 参数: 最大等待建立连接的个数1. 等待接受客户端的连接请求‘accept’1. 接收数据‘recv’- 参数: 表示每次接收数据的大小，单位是字节，注意: 解码成字符串使用decode()方法1. 发送数据‘send’- 参数: 要发送的二进制数据， 注意: 字符串需要使用encode()方法进行编码1. 关闭套接字- 关闭套接字‘socket’表示通信完成
### socket

#### 概念
- socket (简称 套接字) 是进程之间通信一个工具，好比现实生活中的插座，所有的家用电器要想工作都是基于插座进行，进程之间想要进行网络通信需要基于这个 socket。
#### 作用
- 负责进程之间的网络数据传输，好比数据的搬运工。
#### 使用场景
- 不夸张的说，只要跟网络相关的应用程序或者软件都使用到了 socket 。
### TCP网络应用程序的注意点介绍

#### 1. 当 TCP 客户端程序想要和 TCP 服务端程序进行通信的时候必须要先建立连接

#### 2. TCP 客户端程序一般不需要绑定端口号，因为客户端是主动发起建立连接的。

#### 3. TCP 服务端程序必须绑定端口号，否则客户端找不到这个 TCP 服务端程序。

#### 4. listen 后的套接字是被动套接字，只负责接收新的客户端的连接请求，不能收发消息。

#### 5. 当 TCP 客户端程序和 TCP 服务端程序连接成功后， TCP 服务器端程序会产生一个新的套接字，收发客户端消息使用该套接字。

#### 6. 关闭 accept 返回的套接字意味着和这个客户端已经通信完毕。

#### 7. 关闭 listen 后的套接字意味着服务端的套接字关闭了，会导致新的客户端不能连接服务端，但是之前已经接成功的客户端还能正常通信。

#### 8. 当客户端的套接字调用 close 后，服务器端的 recv 会解阻塞，返回的数据长度为0，服务端可以通过返回数据的长度来判断客户端是否已经下线，反之服务端关闭套接字，客户端的 recv 也会解阻塞，返回的数据长度也为0。

### socket之send和recv原理剖析

#### 1. 认识TCP socket的发送和接收缓冲区
- 当创建一个TCP socket对象的时候会有一个发送缓冲区和一个接收缓冲区，这个发送和接收缓冲区指的就是内存中的一片空间。
#### 2. send原理剖析
- send是不是直接把数据发给服务端?- 不是，要想发数据，必须得通过网卡发送数据，应用程序是无法直接通过网卡发送数据的，它需要调用操作系统接口，也就是说，应用程序把发送的数据先写入到发送缓冲区(内存中的一片空间)，再由操作系统控制网卡把发送缓冲区的数据发送给服务端网卡 。
#### 3. recv原理剖析
- recv是不是直接从客户端接收数据?- 不是，应用软件是无法直接通过网卡接收数据的，它需要调用操作系统接口，由操作系统通过网卡接收数据，把接收的数据写入到接收缓冲区(内存中的一片空间），应用程序再从接收缓存区获取客户端发送的数据。
#### 小结
- 不管是recv还是send都不是直接接收到对方的数据和发送数据到对方，发送数据会写入到发送缓冲区，接收数据是从接收缓冲区来读取，发送数据和接收数据最终是由操作系统控制网卡来完成。