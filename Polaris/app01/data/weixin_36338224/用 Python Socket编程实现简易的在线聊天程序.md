
--- 
title:  用 Python Socket编程实现简易的在线聊天程序 
tags: []
categories: [] 

---
### 1.什么是socket？

说到网络编程，难免要提到socket？

那什么是socket呢，中文名叫"套接字"，更难理解了吧。

通俗来讲，socket表示一个网络连接，通过这个连接，使得主机间或者一台计算机上的进程间可以通讯。

不管是不同主机，还是同一主机。既然是通信，必定有一个发送方，一个接收方。对应一个客户端，和一个服务端。

### 3.3.2 创建客户端
- 创建socket，建立连接
```
import socket

# 指定IPv4协议（AF_INET），IPv6协议请使用AF_INET6
# 指定使用TCP协议（SOCK_STREAM），UDP协议请使用SOCK_DGRAM
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 参数是一个tuple，tuple里指定服务器地址（域名或ip）和端口号
sock.connect(('www.sina.com.cn', 80))
```
- 发送数据
```
# 注意这里str格式要遵循HTTP协议标准。
# 注意结尾一定要用 \r\n\r\n
sock.send("GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\n\r\n".encode("utf-8"))
```
- 接收数据
```
buffer = []
while True:
    # 每次最多接收1k字节
    d = sock.recv(1024)
    if d:
        # Python3接收到为bytes类型，要转为str
        buffer.append(str(d))
    else:
        break
data = ''.join(buffer)
```

### 3.3.3 创建服务端
- 创建socket
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
- 绑定ip和port
```
# 注意以元组格式传入，可以是某网卡的公网ip，或0.0.0.0，或127.0.0.1
sock.bind(('127.0.0.1', 9999))
```
- 监听端口
```
# 指定等待连接的最大数量
sock.listen(5)
```
- 接收数据
```
while True:
    # 接受一个新连接，阻塞的，只有接收到新连接才会往下走
    sock, addr = s.accept()
    # 每一次连接，都要创建新线程，否则一次只能处理一个连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
```
- 连接处理函数
```
def tcplink(sock, addr):
    while True:
        data = sock.recv(1024)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
```

### 3.3.4 socket工作流程

<img src="https://img-blog.csdnimg.cn/20201027130627168.png" alt="">

### 3.3.5 socket公共函数汇总
- 发送数据
```
# 发送TCP数据，返回值：发送的字节当量
sk.send("data string")

# 完整发送TCP数据，频繁调用send方法，确保数据发送完成
sk.sendall("data string")

# 发送UDP数据
sk.sendto("data string",address)
```
- 接收数据
```
# 接收TCP数据，一次最大只接收1k数据
sk.recv(1024)

# 接收UDP数据，一次只接收1k数据，返回值：数据和发送方ip
(data,address) = sk.recvfrom(1024)
```
- 获取socket信息
```
# 获取远程socket的addr,port
(addr, port) = sk.getpeername()

# 获取本地socket的addr,port
(addr, port) = sk.getsockname()
```
- 获取其他信息
```
import socket

# 获取当前主机名
HostName = socket.gethostname()

# 获取当前主机的ip
HOST = socket.gethostbyname(HostName)

# 获取当前socket连接的文件描述符
file_no = sk.fileno()
```
- 设置socket
```
# 设置连接的超时时间
sk.settimeout(timeout)
sk.gettimeout()

# 设置为非阻塞模式，默认是0（阻塞）
# 非阻塞下，accept和recv时一旦无数据，则报错：socket.Error
sk.setblocking(1)

# 设置socket内部参数，
# 具体有哪些参数，可以查看socket类的python源码
sk.setsockopt(level,optname,value)
sk.getsockopt(level,optname)
```

### 3.3.6 搭建在线聊天机器人

通过上面的学习，我们知道，同主机下或不同主机下的两个进程要进行通信（TCP/UDP，不管是消息传输还是文件传输），必定要借助socket这个桥梁。

那接下来，我们就一起来完成这个实战项目。

**思路**：首先，客户端和服务端建立socket连接，然后客户端向服务端发送消息，服务端接收消息，并调用 图灵机器人API接口，获取回复返回给客户端。

在这里，我们需要先去图灵机器人(

一切准备就绪，就可以写我们的代码了。
- 客户端
```
import socket
import time

class ChatClient:
    def __init__(self, username, port):
        self.username = username
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("127.0.0.1", port))

    def send_msg(self, msg):
        self.socket.send("{username}::{msg}".format(username=self.username,msg=msg).encode("utf-8"))

    def recv_msg(self):
        data=self.socket.recv(1024)
        if data:
            print("\n【机器人小图】"+" "+time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
            print(data.decode("utf-8"))
            return True
        return False

    def main(self):
        data = self.socket.recv(1024)
        print(data.decode("utf-8"))
        msg = input("请输入消息：")
        self.send_msg(msg)
        while True:
            if self.recv_msg():
                msg=input("\n我：")
                self.send_msg(msg)
                if msg == "exit":
                    print("聊天室已关闭")
                    break

if __name__ == '__main__':
    cc = ChatClient(username="小明", port=9999)
    cc.main()
```
- 服务端
```
import socket
import time
import threading
import requests
import json


class ChatServer:
    def __init__(self, port):
        # 绑定服务器的ip和端口，注意以tuple的形式
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("0.0.0.0", port))
        self.socket.listen(5)
        # 图灵机器人，授权码
        self.key = "your tuling robot key"
        print("正在监听 127.0.0.1 ：{}...".format(port))

    def tcplink(self, sock, addr):
        # 每次连接，开始聊天前，先欢迎下。
        sock.send("你好，欢迎来到机器人聊天器！".encode("utf-8"))
        while True:
            data = sock.recv(1024).decode("utf-8")
            print(sock.getpeername())
            print(sock.getsockname())
            print(sock.fileno())
            username = data.split("::")[0]
            msg = data.split("::")[1]
            if msg == "exit":
                break
            if msg:
                print("【"+username+"】 "+time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
                print(msg)
                response = self.get_response(msg)
                sock.send(response.encode("utf-8"))
        sock.close()
        print("与 {} 结束聊天！".format(username))

    def get_response(self, info):
        # 调用图灵机器人API
        url = 'http://www.tuling123.com/openapi/api?key=' + self.key + '&amp;info=' + info
        res = requests.get(url)
        res.encoding = 'utf-8'
        jd = json.loads(res.text)
        return jd['text']

    def main(self):
        while True:
            sock, addr = self.socket.accept()
            t=threading.Thread(target=self.tcplink, args=(sock, addr))
            t.start()

if __name__ == '__main__':
    cs = ChatServer(port=9999)
    cs.main()
```

将服务端程序跑起来，然后运行客户端，看下效果。 <img src="https://img-blog.csdnimg.cn/20201027130627871.png" alt="">
