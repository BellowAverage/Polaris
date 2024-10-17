
--- 
title:  dell服务器开机卡在PCIe device errors页面 
tags: []
categories: [] 

---
在安装和调试实验室dell服务器的过程中遇到了一些问题，特此记录一下。

**问题：**<img alt="" class="has" src="https://img-blog.csdnimg.cn/20191019165508608.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx,size_16,color_FFFFFF,t_70"> 如上图所示，dell服务器在开机或重启的时候，会出现如上图所示的页面，大致问题如下：

```
UEERI0077: One or more PCIe device errors occurred in the previous boot. Check the 
System Event Log (SEL) to ientify the PCIe device with errors, and then update its 
firmware.
```

按了F1后便可以正常进入系统，但是对于一台服务器而言，这是无法忍受的，因为你无法像使用笔记本一样随时可以现场操控服务器。

解决方法见我的另一个博客：
