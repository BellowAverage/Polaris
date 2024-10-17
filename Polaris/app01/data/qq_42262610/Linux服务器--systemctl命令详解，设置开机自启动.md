
--- 
title:  Linux服务器--systemctl命令详解，设置开机自启动 
tags: []
categories: [] 

---


systemctl 是系统服务管理器命令。

**1.设置开机自启动**

```
systemctl enable nfs-server.service</code></strong></pre> 
2.停止开机自启动 
<pre><code>systemctl disable nfs-server.service
```

3.查看服务当前状态

```
systemctl status nfs-server.service
```

4.重新启动某服务

```
systemctl restart nfs-server.service
```

5.查看所有已启动的服务

```
systemctl list -units --type=service
```
