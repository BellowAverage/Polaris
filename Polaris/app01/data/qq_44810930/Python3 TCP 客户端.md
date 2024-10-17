
--- 
title:  Python3 TCP 客户端 
tags: []
categories: [] 

---
下面是一个简单的 Python TCP 客户端示例代码，用于与之前提到的 EchoServer 进行通信：

```
import socket

server_address = ('localhost', 8888)

# 创建 TCP 客户端套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 连接到服务器
    client_socket.connect(server_address)
    print('Connected to server')

    while True:
        message = input("Enter a message to send to server (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        message = message + "\r\n"  # 因为tcp服务端设置了 set_terminator(b"\r\n")
        # 发送消息给服务器
        client_socket.sendall(message.encode())

        # 接收服务器返回的消息
        data = client_socket.recv(1024)
        print(f"Received from server: {<!-- -->data.decode()}")

except Exception as e:
    print(f"An error occurred: {<!-- -->e}")

finally:
    # 关闭客户端套接字
    client_socket.close()


```

这段代码实现了一个简单的 TCP 客户端，它会不断地向服务器发送消息，并接收服务器返回的消息。用户可以在控制台上输入消息，客户端会将消息发送给服务器并打印出服务器返回的消息。当用户输入 “exit” 时，客户端会退出。

你可以运行这段代码并输入消息来和 EchoServer 进行通信。记得先运行 EchoServer 以确保客户端能够成功连接。
