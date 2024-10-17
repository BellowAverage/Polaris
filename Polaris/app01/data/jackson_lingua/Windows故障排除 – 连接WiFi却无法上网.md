
--- 
title:  Windows故障排除 – 连接WiFi却无法上网 
tags: []
categories: [] 

---
## Windows故障排除 – 连接WiFi却无法上网

### Windows Troubleshooting - Connecting WiFi but PC Cannot Browse Internet

By Jackson@ML

>  
 有个同学买了一台崭新的D品牌游戏本，i7处理器，英伟达RTX系列独立显卡及15寸液晶显示器，可谓功能强大。但是，Windows 11安装完毕后无法上网；重启仍无法解决，十分苦恼。 


本文简要介绍如何逐级检查和排除无法上网故障的方法，希望对读者有所帮助。

#### 1. 检查IP设置

在 Windows 命令行窗口(cmd)里，执行以下命令：

```
ipconfig /all

```

查看到IP地址段为：10.192.15.x, 于是继续用ping命令连接该网段网关:

```
ping 10.192.15.1

```

看到 TTL=64，测试通过！说明局域网从电脑连接到无线路由器的WiFi通道畅通。

#### 2. 验证网页访问

1） 打开EDGE浏览器（Windows默认安装），在地址栏输入 ，无法显示网页，具体原因未明。

2） 在命令行窗口 (cmd) 在此使用nslookup某知名网站IP地址，

```
nslookup xyz.com

```

总显示以下信息：

```
DNS request timed out.
Timeout was 2 seconds.
DNS request timed out.
    Timeout was 2 seconds.
DNS request timed out.
    Timeout was 2 seconds.
DNS request timed out.
    Timeout was 2 seconds.

```

循环往复不停止。

于是，不得不使用组合键 Ctrl + C 中断进程。由此判断极有可能为DNS服务器没有联通。

#### 3. 重置相关设置

由于怀疑是DNS设置问题，因此打开**控制面板 - 网络和Internet - 网络连接**，找到WLAN右键单击**WLAN**，点击**属性**；

在Internet协议版本4(TCP/IPV4)地址设置中，仍然选用DHCP来分配IP地址（因为所用无线路由器联网目前畅通）。

但在DNS设置中去除自动获得DNS服务器地址，选择使用下面的DNS服务器地址，在首选DNS服务器一栏，填写网关地址：192.168.15.1， 在备用DNS 服务器一栏输入测试DNS: 114.114.114.114. 确定退出。

此时，用 cmd 打开命令行窗口，重置网络配置，执行以下命令：

```
netsh int ip reset

```

<img src="https://img-blog.csdnimg.cn/direct/bf78ab1912104437acf2297a0bb3b6b7.png" alt="在这里插入图片描述">

执行完毕后，重启计算机并重新登录Windows。

再次打开浏览器，输入任意网址，便上网如飞！

技术好文陆续推出，敬请关注。

喜欢就点赞哈！您的认可，我的动力。😊
