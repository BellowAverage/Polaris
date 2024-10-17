
--- 
title:  【python】asyncore 和 asyncio 异步套接字服务 
tags: []
categories: [] 

---
`asyncore` 模块是 Python 标准库的一部分，用于开发异步套接字服务和客户端。它提供了一个基于事件循环的框架，可以处理网络连接中的异步 I/O 操作。不过，需要注意的是，随着 Python 3.4 引入 `asyncio` 模块，`asyncore` 在新的 Python 项目中已经较少使用，因为 `asyncio` 提供了更加现代、灵活和强大的异步编程能力。

尽管 `asyncore` 在某些旧项目中仍然可能被使用，但对于新的项目，推荐使用 `asyncio`。下面将简要介绍 `asyncore` 的使用方式，以及为什么你可能会想要改用 `asyncio`。

#### `asyncore` 使用示例

下面是一个使用 `asyncore` 的简单服务器示例：

```
import asyncore
import socket

class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(1024)
        if data:
            self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        handler = EchoHandler(sock)

server = EchoServer('localhost', 8080)
asyncore.loop()

```

这个示例中创建了一个简单的回声服务器，它会将接收到的所有数据原样发送回客户端。

#### 为什么使用 `asyncio` 替代 `asyncore`
1. **现代化的 API**：`asyncio` 提供了一个现代化的、基于协程的 API，使得异步编程更加直观和易于理解。1. **更广泛的支持**：`asyncio` 是 Python 3.4 及之后版本的官方标准库的一部分，得到了广泛的支持和持续的更新。1. **更丰富的功能**：`asyncio` 提供了比 `asyncore` 更多的功能，包括对异步文件操作、子进程、队列以及更多网络协议的支持。
#### `asyncio` 示例

下面是一个使用 `asyncio` 实现的相同功能（回声服务器）的示例，以展示其与 `asyncore` 相比的简洁性和易用性：

```
import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {<!-- -->message} from {<!-- -->addr}")

    writer.write(data)
    await writer.drain()

    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, 'localhost', 8080)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {<!-- -->addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())

```

这个 `asyncio` 示例展示了如何用更现代的方式实现相同的功能。如果你正在开始一个新的项目，或者考虑升级现有的基于 `asyncore` 的代码，强烈推荐使用 `asyncio`。
