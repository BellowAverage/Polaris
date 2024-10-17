
--- 
title:  虚拟机重启网络失败：Error:Failed to start LSB: Bring up/down networking的解决方法 
tags: []
categories: [] 

---
#### 问题描述

 一直正常运行的虚拟机，某次关机重启之后，发现SSH 无法连接

重启网络发现失败

service networkrestart

**解决方法**

```
[root@lexsaints ~]#systemctl stop NetworkManager
[root@lexsaints ~]#systemctl disable NetworkManager
[root@lexsaints ~]#systemctl restart  network
或
[root@lexsaints ~]#systemctl  restart NetworkManager
[root@lexsaints ~]#systemctl restart  network
```

**问题原因**

NetworkManager(NetworManager)是检测网络、自动连接网络的程序。

无论是无线还是有线连接，它都可以令您轻松管理。

对于无线网络,网络管理器可以自动切换到最可靠的无线网络。

利用网络管理器的程序可以自由切换在线和离线模式。

网络管理器可以优先选择有线网络，支持 VPN。

网络管理器最初由 Redhat 公司开发，现在由 GNOME 管理。

 
