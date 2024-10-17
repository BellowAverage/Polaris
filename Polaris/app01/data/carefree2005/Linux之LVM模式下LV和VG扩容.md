
--- 
title:  Linux之LVM模式下LV和VG扩容 
tags: []
categories: [] 

---
## 一、LVM简介

  LVM (Logical Volume Manager) 是一个逻辑卷管理器，它允许用户将多个硬盘分区或者整个硬盘组成一个或多个逻辑卷。LVM 可以在运行时动态地改变逻辑卷的大小，而不需要关机或重新启动系统。它也可以将多个硬盘的存储空间组合在一起，形成一个大容量的存储池，使得数据的管理更加灵活和方便。LVM 已经成为了许多 Linux 发行版的标准功能之一，广泛应用于数据中心、服务器、虚拟化环境等场景中。如下图所示，简单来说LVM就是将分区或者磁盘逻辑转化为PV（Physical Volume），将PV加入到VG（Volume Group）中，再根据需求将VG中的存储空间分配到LV（Logical Volume）中。博文将以扩容/home分区磁盘空间为例介绍EXT4文件系统格式下LVM是如何进行磁盘扩容的。实际上LVM是支持动态调整的，包括扩容和减小，但实际操作中跟文件系统格式也有关系，ext4格式既可以扩容也可以减小（回收未使用的空间），xfs文件系统格式则只支持扩容。 <img src="https://img-blog.csdnimg.cn/5f62d313174c42efadd7ae64c9446276.png" alt="在这里插入图片描述">   实验环境说明：
- 操作系统：centos7.9- 文件系统格式：ext4
## 二、LV扩容

  LVM磁盘扩容时，我们先检查VG是否还有剩余空间，如果有我们从VG中分配所需磁盘空间给指定的LV即可。实验环境下/home分区大小为20G，使用的是LVM逻辑卷，假设我们需要调整/home分区大小为30G。 <img src="https://img-blog.csdnimg.cn/856a1fdf16444c178e5748c4b970416b.png" alt="在这里插入图片描述">

### 1、检查vg剩余空间

  使用vgdisplay命令我们可以看到vg名为centos_s178，已经分配的空间为42GB，剩余的空间为16.99GB。

>  
 [root@s178 ~]# vgdisplay — Volume group — VG Name centos_s178 … Alloc PE / Size 10752 / 42.00 GiB Free PE / Size 4350 / 16.99 GiB … <img src="https://img-blog.csdnimg.cn/b3098ecf514545a5b61e380c738ae285.png" alt="在这里插入图片描述"> 


### 2、查看LV逻辑卷名称和路径

  使用lvdisplay命令查看逻辑卷的情况，可以看到有多个逻辑卷，可以看到逻辑卷路径，逻辑卷名、所属VG、存储空间大小等。

>  
 [root@s178 ~]# lvdisplay — Logical volume — LV Path /dev/centos_s178/home LV Name home VG Name centos_s178 … LV Size 20.00 GiB … — Logical volume — LV Path /dev/centos_s178/root LV Name root VG Name centos_s178 … 


### 3、扩容指定大小的存储空间到LV

  使用lvextend命令扩容逻辑卷大小，-L参数扩容指定大小。

>  
 [root@s178 ~]# lvextend -L +10G /dev/centos_s178/home Size of logical volume centos_s178/home changed from 20.00 GiB (5120 extents) to 30.00 GiB (7680 extents). Logical volume centos_s178/home successfully resized. 


### 3、查看磁盘大小

<img src="https://img-blog.csdnimg.cn/84d24f7df4ca4a458938f97d7b377755.png" alt="在这里插入图片描述">

### 4、扩容空间写入文件系统

  resize2fs 命令将扩容空间写入文件系统，如果是xfs格式则可以使用命令xfs_growfs代替。

>  
 [root@s178 ~]# resize2fs /dev/centos_s178/home resize2fs 1.42.9 (28-Dec-2013) Filesystem at /dev/centos_s178/home is mounted on /home; on-line resizing required old_desc_blocks = 3, new_desc_blocks = 4 The filesystem on /dev/centos_s178/home is now 7864320 blocks long. 


### 5、再次验证

  使用df命令再次查看磁盘大小验证，发现/home分区已经调整为了30G大小。 <img src="https://img-blog.csdnimg.cn/b261a785c7d5414796c37998985f7d8c.png" alt="在这里插入图片描述">

## 三、PV扩容

  假设我们需要将/home分区扩容为40G，因为VG剩余空间只有16.99G，所以磁盘空间不足，需要先添加磁盘，将磁盘添加到VG中，再将指定空间分配到LV。

### 1、查看磁盘

  新添加或者插入一块磁盘/dev/sdb，使用fdisk命令可以看到。

>  
 [root@s178 ~]# fdisk -l Disk /dev/sda: 64.4 GB, 64424509440 bytes, 125829120 sectors … Disk /dev/sdb: 42.9 GB, 42949672960 bytes, 83886080 sectors 


### 2、磁盘分区

>  
 [root@s178 ~]# parted /dev/sdb GNU Parted 3.1 Using /dev/sdb Welcome to GNU Parted! Type ‘help’ to view a list of commands. (parted) mklabel gpt (parted) mkpart Partition name? []? disk2 File system type? [ext2]? ext4 Start? 1 End? -1 (parted) 


### 3、创建PV

>  
 [root@s178 ~]# pvcreate /dev/sdb1 Physical volume “/dev/sdb1” successfully created. 


### 4、查看PV信息

>  
 [root@s178 ~]# pvs PV VG Fmt Attr PSize PFree /dev/sda2 centos_s178 lvm2 a-- 42.00g 0 /dev/sda3 centos_s178 lvm2 a-- 16.99g 6.99g /dev/sdb1 lvm2 — &lt;40.00g &lt;40.00g [root@s178 ~]# vgs VG #PV #LV #SN Attr VSize VFree centos_s178 2 3 0 wz–n- 58.99g 6.99g [root@s178 ~]# vgscan Reading volume groups from cache. Found volume group “centos_s178” using metadata type lvm2 


### 5、扩容VG

>  
 [root@s178 ~]# vgextend centos_s178 /dev/sdb1 Volume group “centos_s178” successfully extended 


### 6、查看VG信息

>  
 [root@s178 ~]# vgdisplay — Volume group — VG Name centos_s178 System ID Format lvm2 Metadata Areas 3 Metadata Sequence No 7 VG Access read/write VG Status resizable MAX LV 0 Cur LV 3 Open LV 3 Max PV 0 Cur PV 3 Act PV 3 VG Size &lt;98.99 GiB PE Size 4.00 MiB Total PE 25341 Alloc PE / Size 13312 / 52.00 GiB Free PE / Size 12029 / &lt;46.99 GiB VG UUID tTBWJ4-BFKA-tP95-kRNh-kZ0G-nf51-d3XSUt 


### 7、扩容LV

  使用命令lvextend LV PV可以将某PV全部分配给指定的LV。使用lvextend命令扩容逻辑卷大小，记得使用-L参数时不带+是将磁盘扩展到指定大小，带+号则是扩容指定大小的空间。lvreduce命令可以减小逻辑卷大小。 <img src="https://img-blog.csdnimg.cn/998d9d2664944c8f81358e8aa01cbbfc.png" alt="在这里插入图片描述">

>  
 [root@s178 ~]# lvextend -L 40G /dev/centos_s178/home Size of logical volume centos_s178/home changed from 36.99 GiB (9470 extents) to 40.00 GiB (10240 extents). Logical volume centos_s178/home successfully resized. 


### 8、扩容空间写入文件系统

>  
 [root@s178 ~]# resize2fs /dev/centos_s178/home resize2fs 1.42.9 (28-Dec-2013) Filesystem at /dev/centos_s178/home is mounted on /home; on-line resizing required old_desc_blocks = 4, new_desc_blocks = 5 The filesystem on /dev/centos_s178/home is now 10485760 blocks long. 


### 9、验证扩容结果

<img src="https://img-blog.csdnimg.cn/3b558b9d226b406db43dde9f5abc08dd.png" alt="在这里插入图片描述">
