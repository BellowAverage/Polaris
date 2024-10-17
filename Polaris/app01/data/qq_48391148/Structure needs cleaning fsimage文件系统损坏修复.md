
--- 
title:  Structure needs cleaning fsimage文件系统损坏修复 
tags: []
categories: [] 

---
>  
 **最近清除数据的时候发现有些文件无法rm** 


```
[root@node101 application_1691504014432_0002]# rm -rf ls:*
[root@node101 application_1691504014432_0002]# ls
ls: 无法访问flink-dist-cache-8f72398e-9254-42d4-a14d-a0def99b493d: Structure needs cleaning

```

>  
 **以下操作可能会删除文件系统中一些异常数据，有重要数据请****备份****再操作。** 


```
# 首先查看文件系统挂载情况
[root@node101 application_1691504014432_0002]# df -Th
文件系统       类型      容量  已用  可用 已用% 挂载点
devtmpfs       devtmpfs   16G     0   16G    0% /dev
tmpfs          tmpfs      16G     0   16G    0% /dev/shm
tmpfs          tmpfs      16G  432K   16G    1% /run
tmpfs          tmpfs      16G     0   16G    0% /sys/fs/cgroup
/dev/vda1      xfs        25G   13G   13G   50% /
/dev/vdb       ext4      197G  3.3G  185G    2% /data
tmpfs          tmpfs     3.2G     0  3.2G    0% /run/user/0

```

>  
 **我这里是/data出现了异常，所以先将/dev/vdb这块磁盘取消挂载** 


```
[root@node101 ~]# umount /dev/vdb

```

>  
 **操作时不要位于要取消挂载的目录内，不然会出现以下报错** 


```
[root@node101 application_1691504014432_0002]# umount /dev/vdb
umount: /data: target is busy.

```

>  
 **使用文件系统修复工具修复** 


```
[root@node101 ~]# fsck.ext4 /dev/vdb
e2fsck 1.42.9 (28-Dec-2013)
/dev/vdb contains a file system with errors, 强制检查.
第一步: 检查inode,块,和大小
第二步: 检查目录结构

```

>  
 **最后修复好了以后再重新将文件系统挂载好** 


```
[root@node101 data]# mount /dev/vdb
[root@node101 data]# df -Th
文件系统       类型      容量  已用  可用 已用% 挂载点
devtmpfs       devtmpfs   16G     0   16G    0% /dev
tmpfs          tmpfs      16G     0   16G    0% /dev/shm
tmpfs          tmpfs      16G  432K   16G    1% /run
tmpfs          tmpfs      16G     0   16G    0% /sys/fs/cgroup
/dev/vda1      xfs        25G   13G   13G   50% /
tmpfs          tmpfs     3.2G     0  3.2G    0% /run/user/0
/dev/vdb       ext4      197G  3.3G  185G    2% /data

```
