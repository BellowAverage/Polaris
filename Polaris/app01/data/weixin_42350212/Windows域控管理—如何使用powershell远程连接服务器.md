
--- 
title:  Windows域控管理—如何使用powershell远程连接服务器 
tags: []
categories: [] 

---
<img alt="" height="147" src="https://img-blog.csdnimg.cn/b10caa4a02714d5cbc55bebf3352d593.png" width="356">



管理员权限运行Powershell，

输入Enable-PsRemoting开启Powershell远程管理，

远程端和被远程端都需要启用，另外说明一下，

WinRM也就是Powershell远程管理时使用的端口



**1.在服务器上 用管理员权限 执行 Enable-PSRemoting 命令**

之后会有一堆的确认操作 全部YES就好了



**2 在客户端上 执行 Enter-PSSession IP地址 -Credential 域名\用户名**

例如：Enter-PSSession 192.168.3.1 -Credential abc\administrator



域之间的电脑通信，使用命令

```
Enter-PSSession -Computer "LexMadrid"
```

就可以进入管理

<img alt="" height="369" src="https://img-blog.csdnimg.cn/9d9a559701f340da8218df3531178471.png" width="587">


