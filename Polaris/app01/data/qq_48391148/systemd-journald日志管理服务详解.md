
--- 
title:  systemd-journald日志管理服务详解 
tags: []
categories: [] 

---
>  
 journald参考文档： 




>  
 **Amazonlinux2023系统默认不再安装rsyslog，因此在amazonlinux2中的诸多日志文件例如/var/log/message默认不可用。** 


>  
 **AWS官方文档建议使用systemd的journalctl接口和相关包文件。** 
 **systemd-journald：** 
 **journald系统主要由三个系统日志服务组件组成：** 
 **守护程序：systemd-journald** 
 **配置文件：/etc/systemd/journald.conf** 
 **日志搜索程序：journalctl** 


### 配置文件主要配置：

>  
 **配置文件路径：/etc/systemd/journald.conf** 
 **所有选项都在[Journal]部分配置** 


>  
 [Journal] #Storage=auto 
 Storage可选的值有：volatile、persistent、auto、none 
 volatile：日志数据文件存储在内存中，即/run/log/journal下 
 persistent：日志数据文件存储在磁盘中，即/var/log/journal下 
 auto:日志数据文件存储在磁盘中，即/var/log/journal下，但是这个目录必须存在 
 none：关闭存储，丢弃所有日志数据 


>  
 [Journal] Compress=yes Seal=yes SplitMode=none 
 Compress：布尔值，默认启用，日志数据会被压缩 
 Seal：布尔值，数据加密 
 SplitMode：可选值有：uid和none，uid会将日志文件按用户uid进行切割，none则所有日志记录在一个文件中，但是非root用户无法访问自己的日志数据。 


>  
 [Journal] SystemMaxUse=50M SystemMaxFileSize=50M SystemMaxFiles=1 RuntimeMaxUse=50M RuntimeMaxFileSize=50M RuntimeMaxFiles=1 
 SystemMaxUse：日志最多可以使用多少空间，默认为自己文件系统的10% 
 SystemMaxFileSize：日志文件最大大小 
 SystemMaxFiles：保留的最多文件数 
 RuntimeMaxUse=50M：存储在内存中的日志文件大小 
 RuntimeMaxFileSize=50M：存储在内存中最大文件大小 
 RuntimeMaxFiles=1：存储的最多文件数 


### journalctl主要用法

#### 查看所有系统文件：journalctl

#### 默认是分页显示的，可以正则匹配，输入? 内容进行匹配

<img alt="" height="554" src="https://img-blog.csdnimg.cn/f428ffa9edd947f889a85ffb20548046.png" width="1200">

#### 只查看内核日志：journalctl -k

<img alt="" height="565" src="https://img-blog.csdnimg.cn/d38dfb10be924d399ccd31cbf8e8e9c7.png" width="1200">

#### 查看某个服务日志：journalctl -u mariadb

-u 指定服务单元，systemd下面的所有service都可以指定

<img alt="" height="627" src="https://img-blog.csdnimg.cn/f479a723415b40d4941f6f23eacc3c5e.png" width="1200">

#### 按时间查找日志：

>  
 几种写法： 
 journalctl --since "2023-11-01 00:00:00" --until "2023-11-03 00:00:00" 
 journalctl --since yesterday 
 journalctl --since 09:00 
 journalctl --since 09:00 --until "1 hour ago" 


 <img alt="" height="517" src="https://img-blog.csdnimg.cn/0c86e06ef9f34f03a1c7219a37ab5aed.png" width="1200">



#### journalctl默认以当前系统时间显示日志，可以指定时区显示

<img alt="" height="457" src="https://img-blog.csdnimg.cn/e37fd0f6887b4c00909680e097812b76.png" width="1200">

#### 查看最新的日志：journalctl -r

<img alt="" height="422" src="https://img-blog.csdnimg.cn/eb0f05282e784dca9d91a0de61d1d941.png" width="1200">

#### 按日志级别查找日志：journalctl -p

可以按数字：journalctl -p 0 (0-8)

可以按等级：emerg alert crit err warning notice info debug none

<img alt="" height="414" src="https://img-blog.csdnimg.cn/c0828a7b9a4d4c1381427e4ed70d3f42.png" width="1200">

#### 查看某个用户的日志：

>  
 journalctl _UID=1000 --since today 


<img alt="" height="498" src="https://img-blog.csdnimg.cn/4e178a9cb12547f89b6f61e67b1e84c9.png" width="1200">
