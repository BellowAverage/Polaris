
--- 
title:  Python 3 中，`asynchat`异步通信 
tags: []
categories: [] 

---
在 Python 3 中，`asynchat` 是基于 `asyncore` 的一个高层抽象模块，用于处理异步通信协议。它提供了一种简单的方式来创建自定义的异步通信协议，并处理通信中的错误和异常。

`asynchat` 模块主要作用是将网络数据流**分割**成消息或者数据包，并将每个消息或者数据包作为一个单独的事件处理。这使得你可以更方便地处理异步通信协议中的消息传输和处理。

以下是一个简单的示例代码，演示了如何使用 `asynchat` 创建一个简单的 Echo 服务器：

```
import asyncore
import asynchat
import socket

class EchoHandler(asynchat.async_chat):
    def __init__(self, conn):
        asynchat.async_chat.__init__(self, conn)
        self.set_terminator(b"\r\n")
        self.data = []

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        message = b"".join(self.data)
        self.data = []
        self.push(message + b"\r\n")

class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(1)

    def handle_accept(self):
        conn, addr = self.accept()
        print(f"Accepted connection from {<!-- -->addr}")
        handler = EchoHandler(conn)

server = EchoServer('localhost', 8888)
asyncore.loop()

```

在这个示例中，我们定义了一个继承自 `asynchat.async_chat` 的 `EchoHandler` 类来处理服务器的逻辑。在 `__init__` 方法中，我们设置了消息分割符为 `\r\n`，并创建了一个空的缓冲区数组 `self.data`。

在 `collect_incoming_data` 方法中，我们将接收到的数据添加到缓冲区数组中，并在 `found_terminator` 方法中将缓冲区数组中的所有数据合并成一个消息，并将其发送回客户端。

在 `EchoServer` 类中，我们创建了一个 TCP 套接字并绑定到指定的主机和端口上。然后我们通过调用 `listen` 方法开始监听传入的连接。

`handle_accept` 方法被触发时，表示有新的连接进来。我们通过调用 `accept` 方法来接受连接，并创建了一个 `EchoHandler` 对象来处理连接。

最后，我们创建了一个 `EchoServer` 对象并调用 `asyncore.loop` 方法来启动事件循环，开始监听网络事件。


