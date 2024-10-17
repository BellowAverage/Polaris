
--- 
title:  -bash: mkfs.vfat: command not found 
tags: []
categories: [] 

---
磁盘格式化命令提示未找到。



#### 现象：

使用mkfs.vfat格式化磁盘时，发现命令找不到：

```
[root@localhost ~]# mkfs.vfat /dev/sdb2
-bash: mkfs.vfat: command not found
```



#### 原因：

vfat文件系统是CentOS原生支持的，但是fat文件系统的管理工具mkfs.vfat，mkfs.fat却未必开始就已经安装好的，比如我最小安装的CentOS７就没有。

#### 解决：

先用yum查看mkfs.vfat工具 用的是哪个包：

```
yum provides mkfs.vfat
已加载插件：fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.ustc.edu.cn
 * extras: mirrors.ustc.edu.cn
 * updates: mirrors.nju.edu.cn
base                                                                                | 3.6 kB  00:00:00     
docker-ce-stable                                                                    | 3.5 kB  00:00:00     
extras                                                                              | 2.9 kB  00:00:00     
updates                                                                             | 2.9 kB  00:00:00     
(1/2): docker-ce-stable/7/x86_64/primary_db                                         |  95 kB  00:00:01     
(2/2): updates/7/x86_64/primary_db                                                  |  19 MB  00:00:02     
docker-ce-stable/7/x86_64/filelists_db                                              |  39 kB  00:00:00     
updates/7/x86_64/filelists_db                                                       |  11 MB  00:00:01     
dosfstools-3.0.20-10.el7.x86_64 : Utilities for making and checking MS-DOS FAT filesystems on Linux
源    ：base
匹配来源：
文件名    ：/usr/sbin/mkfs.vfat

```



直接安装dosfstools-3.0.20-10.el7.x86_64：

```
yum install -y dosfstools
```


