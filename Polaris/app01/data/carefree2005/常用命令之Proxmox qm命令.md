
--- 
title:  常用命令之Proxmox qm命令 
tags: []
categories: [] 

---
## 一、Proxmox简介

  Proxmox是一款基于Debian Linux的开源虚拟化平台，它允许用户在单个物理主机上运行多个虚拟机，并提供了许多高级功能，如高可用性、备份和恢复、集群管理等。Proxmox支持多种虚拟化技术，包括KVM和LXC，而且它还提供了一个易用的Web界面，使用户可以轻松管理虚拟机、存储和网络。Proxmox的主要目标是为企业和个人用户提供一种强大的虚拟化解决方案，同时保持易用性和可靠性。在Proxmox系统中，qm命令是用于管理虚拟机的命令行工具，其主要功能包括创建、启动、停止、删除、克隆、迁移、备份等。

## 二、命令使用示例

### 0、命令语法

  其中command是指create、stop、start这些虚拟机操作命令。qm command vmid是基础用法，不同的command有不同的参数选项。

>  
 #qm &lt;COMMAND&gt; [ARGS] [OPTIONS] 


### 1、查看虚拟机列表

>  
 root@s129:~# qm list <img src="https://img-blog.csdnimg.cn/d2506fcdd5e14cfbb97acb00ef618de2.png" alt="在这里插入图片描述"> 


### 2、创建一个虚拟机

  创建虚拟机的时候要求指定内存大小，CPU数量等参数。如下命令创建了一个8G内存，2C的虚拟机，虚拟机ID是182。创建虚拟机的时候需要设置的参数很多，建议还是通过图形化界面完成创建。

>  
 root@s129:~# qm create --memory 8192 --sockets 1 --cores 2 182 


### 3、启动虚拟机

>  
 root@s129:~# qm start 180 


### 4、停止虚拟机

>  
 root@s129:~# qm stop 180 


### 5、查看虚拟机状态

>  
 root@s129:~# qm status 180 status: running 


### 6、解锁虚拟机

  如果虚拟机在备份、克隆、迁移、快照等国产中可能出现错误，导致虚拟机锁定，这个时候会出现界面上无法关机、重启等，我们需要先解锁虚拟机，通过如下命令进行解锁。如果执行此命令还无法解锁，我们需要删除/run/lock/qemu-server/lock-180.conf下的锁文件。

>  
 root@s129:~# qm unlock 180 


### 7、暂停虚拟机

>  
 root@s129:~# qm suspend 180 


### 8、恢复虚拟机

>  
 root@s129:~# qm resume 180 


### 9、重启虚拟机

>  
 root@s129:~# qm reset 180 


### 10、查看虚拟机快照列表

  如果需要还原虚拟机快照，我们可以先 qm listsnapshot查看目前生成的快照列表。

>  
 root@s129:~# qm listsnapshot 180<img src="https://img-blog.csdnimg.cn/a8e7b0bbb9dc4165aea8cae175740f86.png" alt="在这里插入图片描述"> 


### 11、回滚虚拟机到指定快照

>  
 root@s129:~# qm rollback 180 init0 Logical volume “vm-180-disk-0” successfully removed Logical volume “vm-180-disk-0” created. 


### 12、查看虚拟机配置信息

>  
 root@s129:~# qm config 180 boot: order=scsi0;ide2;net0 cores: 1 ide2: local:iso/CentOS-8-x86_64-1905-dvd1.iso,media=cdrom memory: 4096 name: s180 net0: virtio=AE:DB:1A:1B:65:D5,bridge=vmbr0 numa: 0 ostype: l26 parent: init1 scsi0: local-lvm:vm-180-disk-0,size=60G scsihw: virtio-scsi-pci smbios1: uuid=c3751a2f-6ebe-4e8c-aeba-26949f6d7e83 sockets: 2 vmgenid: 95e6f105-d92e-4546-80df-10ca3d7cdcf0 


### 13、删除虚拟机

>  
 root@s129:~# qm destroy 182 


### 14、创建一个虚拟机快照

>  
 root@s129:~# qm snapshot 180 init3 -description snapshot-test snapshotting ‘drive-scsi0’ (local-lvm:vm-180-disk-0) Logical volume “snap_vm-180-disk-0_init3” created. root@s129:~# qm listsnapshot 180 Wide character in printf at /usr/share/perl5/PVE/GuestHelpers.pm line 160. `-&gt; init0 2023-01-03 16:25:08 centos8初始化安装完成 Wide character in printf at /usr/share/perl5/PVE/GuestHelpers.pm line 160. `-&gt; init1 2023-04-12 16:21:39 系统升级为centos8-stream稳定版 `-&gt; init2 2023-04-14 16:29:14 no-description `-&gt; init3 2023-04-14 16:34:49 snapshot-test `-&gt; current You are here! 


### 15、删除一个快照

>  
 root@s129:~# qm delsnapshot 180 init2 Logical volume “snap_vm-180-disk-0_init2” successfully removed root@s129:~# qm listsnapshot 180 Wide character in printf at /usr/share/perl5/PVE/GuestHelpers.pm line 160. `-&gt; init0 2023-01-03 16:25:08 centos8初始化安装完成 Wide character in printf at /usr/share/perl5/PVE/GuestHelpers.pm line 160. `-&gt; init1 2023-04-12 16:21:39 系统升级为centos8-stream稳定版 `-&gt; init3 2023-04-14 16:34:49 snapshot-test `-&gt; current You are here! 


### 16、克隆一个虚拟机

>  
 root@s129:~# qm clone 180 182 create full clone of drive scsi0 (local-lvm:vm-180-disk-0) Logical volume “vm-182-disk-0” created. drive mirror is starting for drive-scsi0 drive-scsi0: transferred 0.0 B of 60.0 GiB (0.00%) in 0s … drive-scsi0: transferred 60.0 GiB of 60.0 GiB (100.00%) in 7m 23s, ready all ‘mirror’ jobs are ready suspend vm trying to acquire lock… drive-scsi0: Cancelling block job drive-scsi0: Done. resume vm trying to acquire lock… 


### 16、迁移虚拟机到其他节点

  我们先查看集群其他节点的名称，然后执行迁移命令，如果存在本地主机配置，如本地CDDROM配置，会报错“can’t migrate local disk ‘local:iso/CentOS-8-x86_64-1905-dvd1.iso’: local cdrom image”,我们可以先编辑配置文件，将本地iso配置挂载取消，然后再执行迁移命令即可。

>  
 root@s129:~# pvecm nodes  Membership information ---------------------- Nodeid Votes Name 1 1 s129 (local) 2 1 s130 3 1 s128 root@s129:~# qm migrate 182 s128 


### 17、修改虚拟机参数

>  
 root@s129:~# qm set 180 -cores 1 update VM 150: -cores 1 root@s129:~# qm set 180 -memory 8192 update VM 181: -memory 8192 


### 18、进入虚拟机监视器

  使用qm monitor命令进入虚拟机控制台，可以执行查看虚拟机信息

>  
 root@s129:~# qm monitor 180 Entering Qemu Monitor for VM 180 - type ‘help’ for help qm&gt; info name s180 qm&gt; info version 6.0.0pve-qemu-kvm_6.0.0 qm&gt;help 

