
--- 
title:  linux虚拟机固定IP的方法 
tags: []
categories: [] 

---
### linux虚拟机固定IP的方法

发现配置的虚拟机环境的3个虚拟机ip变化了，这就让我很无语啊。

解决方法：

>  
 进入到`/etc/sysconfig/network-scripts` 目录下面ls后有个文档（我的是`ifcfg-enp0s3`） `ifcfg-eno16777736`(不同机器后面数字会不相同)，编辑该文件内容，将`BOOTPROTO=dhcp`的值改为`static`，并在最后面加上： 


<img src="https://img-blog.csdnimg.cn/20210330095436112.png" alt="在这里插入图片描述">

```
//nat模式 设置了DNS1链接会很卡，建议不设置DNS1
DNS1=114.114.114.114
IPADDR=192.168.49.128
NETMASK=255.255.255.0
GATEWAY=192.168.49.1
//解释代码
DNS1=114.114.114.114    --dns地址
IPADDR=192.168.49.128   --需要设置的ip地址
NETMASK=255.255.255.0   --子网掩码
GATEWAY=192.168.49.1    --网关

```

<img src="https://img-blog.csdnimg.cn/20210330095631882.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **然后重启服务：service network restart**

不行就重启虚拟机。

完成！亲测。 <img src="https://img-blog.csdnimg.cn/20210330095615443.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
