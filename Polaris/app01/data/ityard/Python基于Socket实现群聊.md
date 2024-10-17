
--- 
title:  Python基于Socket实现群聊 
tags: []
categories: [] 

---
>  
  作者：huny 
  https://www.cnblogs.com/huny/p/14051152.html 
 

**1. 前言**

套接字(Sockets)是双向通信信道的端点。套接字可以在一个进程内，在同一机器上的进程之间，或者在不同主机的进程之间进行通信，主机可以是任何一台有连接互联网的机器。

套接字可以通过多种不同的通道类型实现：Unix域套接字，TCP，UDP等。套接字库提供了处理公共传输的特定类，以及一个用于处理其余部分的通用接口。

**1.1 socket模块：**

要创建套接字，必须使用套接字模块中的socket.socket()函数，该函数具有一般语法

```
s = socket.socket (socket_family, socket_type, protocol = 0)

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDRsR3FlYlhzbkVDRUNLaWJxWGlha0JONXp4azVMaDBab052a2haYzE3VFQwQ3YxMTByWFlWdVNsNjMzaWFHdVBMbWlidjZjUDQwbUZzRFEvNjQw?x-oss-process=image/format,png">

**1.2 常用方法**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUcDRsR3FlYlhzbkVDRUNLaWJxWGlha0JOWjUwN0NackVYNGVyOFk2MEM1QWphSjYxdHVwQTVDUWhENWcxZUZ3Y3cxdnNyNmNUaWNuOWtWdy82NDA?x-oss-process=image/format,png">

**2. 示例**

**2.1 服务器端**

```
#sever.py
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 8088
s.bind((host,port))
try:
    while True:
        receive_data,addr = s.recvfrom(1024)
        print("来自服务器" + str(addr) + "的消息:")
        print(receive_data.decode('utf-8'))
        msg = input('please input send to msg:')
        s.sendto(msg.encode('utf-8'),addr)
except:
    s.close()

```

2.2 客户端

```
#client.py
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
    while True:
        host = socket.gethostname()
        port = 8088
        send_data = input('please input msg:')
        s.sendto(send_data.encode('utf-8'),(host,port))
        msg,addr = s.recvfrom(1024)
        print("来自服务器" + str(addr) + "的消息:")
        print(msg.decode('utf-8'))
except:
    s.close()



```

**服务器示例**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUb0prZHdlcmZpY0ZzOWJvSXFsR2ZFaWFNUzBSTnhoMnh5eDBGNEtlTU16dDNvem5VenpqajZpYXBUV1JjRTRYWkFsQ3had1RTZjd6MURqQS82NDA?x-oss-process=image/format,png">

客户端示例

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUb0prZHdlcmZpY0ZzOWJvSXFsR2ZFaWFNaEg4c0d4U0RsOE9SVU9jeEgySEFPMFA2N0VUd3lFRGU4R1ZKZmdsbmlhaFVLR1dIdDdoeGdCUS82NDA?x-oss-process=image/format,png">

简易的UDP聊天实现了,下面我们来优化一下示例。

**3.示例优化**

服务端

```
#server.py
import socket
import logging


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建socket对象


    addr = ('127.0.0.1', 9999)
    s.bind(addr)  # 绑定地址和端口


    logging.info('UDP Server on %s:%s...', addr[0], addr[1])


    user = {}  # 存放字典{addr:name}
    while True:
        try:
            data, addr = s.recvfrom(1024)  # 等待接收客户端消息存放在2个变量data和addr里
            if not addr in user:  # 如果addr不在user字典里则执行以下代码
                for address in user:  # 从user遍历数据出来address
                    s.sendto(data + ' 进入聊天室...'.encode('utf-8'), address)  # 发送user字典的data和address到客户端
                user[addr] = data.decode('utf-8')  # 接收的消息解码成utf-8并存在字典user里,键名定义为addr
                continue  # 如果addr在user字典里，跳过本次循环


            if 'EXIT'.lower() in data.decode('utf-8'):#如果EXIT在发送的data里
                name = user[addr]   #user字典addr键对应的值赋值给变量name
                user.pop(addr)      #删除user里的addr
                for address in user:    #从user取出address
                    s.sendto((name + ' 离开了聊天室...').encode(), address)     #发送name和address到客户端
            else:   
                print('"%s" from %s:%s' %(data.decode('utf-8'), addr[0], addr[1]))  
                for address in user:    #从user遍历出address
                    if address != addr:  #address不等于addr时间执行下面的代码
                        s.sendto(data, address)     #发送data和address到客户端


        except ConnectionResetError:
            logging.warning('Someone left unexcept.')


if __name__ == '__main__':
    main()



```

客户端

```
#clinet.py
import socket
import threading


def recv(sock, addr):
    '''
    一个UDP连接在接收消息前必须要让系统知道所占端口
    也就是需要send一次，否则win下会报错
    '''
    sock.sendto(name.encode('utf-8'), addr)
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))




def send(sock, addr):
    '''
        发送数据的方法
        参数：
            sock：定义一个实例化socket对象
            server：传递的服务器IP和端口
    '''
    while True:
        string = input('')
        message = name + ' : ' + string
        data = message.encode('utf-8')
        sock.sendto(data, addr)
        if string.lower() == 'EXIT'.lower():
            break


def main():
    '''
        主函数执行方法，通过多线程来实现多个客户端之间的通信
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ('127.0.0.1', 9999)
    tr = threading.Thread(target=recv, args=(s, server), daemon=True)
    ts = threading.Thread(target=send, args=(s, server))
    tr.start()
    ts.start()
    ts.join()
    s.close()


if __name__ == '__main__':
    print("-----欢迎来到聊天室,退出聊天室请输入'EXIT(不分大小写)'-----")
    name = input('请输入你的名称:')
    print('-----------------%s------------------' % name)
    main()



```

支持多人的简易聊天室示例，多个客户端通过一个服务器进行之间通信。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUb0prZHdlcmZpY0ZzOWJvSXFsR2ZFaWFNVHJpY2dGQnEySjZLc1E5eG44YXJJaWJtRVJ6b3VNZ3pNbWxTVEppY2hGNnBvZ3BhOVVCdnE2M3JnLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUb0prZHdlcmZpY0ZzOWJvSXFsR2ZFaWFNWld1MmJUZ2prQ0ZycmpIdzlaZDhyMlRHVHFwaWFwb29MQTQ3SVV6QVd6Szd0RXZNTHNMTFEwUS82NDA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUb0prZHdlcmZpY0ZzOWJvSXFsR2ZFaWFNVFBCdmlhNVZUZzJjRlpNY3dqQ25pY0xNSVo0N0lWZ0xoTElta1hTaHh6ajlIOFBiWVI5SkRONVEvNjQw?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9maHVqem9RZTdUb0prZHdlcmZpY0ZzOWJvSXFsR2ZFaWFNb1k4YkxpYk92QTBhclR2N21YMGlhOXZpYk51aWNpYXZTSG9LdHlDRHV4ZlMyeENaeUVJdWNBaHFtaWJBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">
