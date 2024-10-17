
--- 
title:  windows下配置host 
tags: []
categories: [] 

---
首先，host文件的位置：

```
C:\Windows\System32\drivers\etc

```

然后通过文件打开hosts文件

在最后加入

```
ip地址    网络地址

```

  然后打开cmd：

```
ipconfig/flushdns

```

最后执行：

```
ipconfig/displaydns

```

然后crtl + F寻找，如果找得到的话配置成功
