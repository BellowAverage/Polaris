
--- 
title:  linux为 home 目录扩容 
tags: []
categories: [] 

---
## linux为 /home 目录扩容

**转载地址：**

其实原理与LVM逻辑卷扩容一样，步骤为：
- 创建物理卷，可以是整个磁盘，也可以是分区（分区的话需要是 LVM类型）。- 查看 /home 或者 /root 在哪个卷组。- 卷组扩容。- /home 逻辑卷扩容。- 格式化文件系统


#### 文章目录
- - - <li> 
      <ul>- - - - - <li> 
        <ul>- - - - - 


## 问题背景

服务器（linux系统）磁盘空间不足，挂载了新硬盘之后，**对普通用户透明**的指定目录扩容（如/home）是最直接的方法，这样能够**避免迁移数据（目录拷贝）**，**不影响原分区**，尽可能减小对基础环境的影响。 系统发行版：
- 1- 2
## 基本概念

**物理卷(PV， physical volume)** **逻辑卷(LV，logical volume)** **逻辑分组（VG，volume group）** **逻辑分区** **LVM**

## 新增磁盘为指定目录扩容

方法基本完全照搬了。 这里记录了部分自己环境下的配置过程，有什么不明确的地方，请查看原文步骤； 讲解更加细致，最好仔细读一遍再动手，毕竟修改磁盘配置不是小事，谨慎点。

### 查看现有磁盘使用情况

参考命令：`df -h`，未挂载的硬盘并不能读取到

### 新增硬盘，并查看设备信息

新增加的硬件设备可以在/dev目录下查到，硬盘一般是/dev/fd* 查看新增的设备信息，`fdisk -l`，能够查看现有系统中能够读取到的所有磁盘信息（包括了未挂载的硬盘，但此处在不同发行版中稍有存疑）。 可进一步使用`cfdisk /dev/sd*`查看目标盘的分区信息。

### 创建

为新增加的硬盘创建逻辑卷：`pvcreate /dev/sdc` 成功则提示
- 1- 2
此时可以通过`pvdisplay`命令查看新增加的磁盘信息 ![在这里插入图片描述](https://img-blog.csdnimg.cn/235c7f271ddc4f1fac7fcb9438c0afce.png<img src="https://img-blog.csdnimg.cn/59aaa37a70e944a2a5e52ec6c680650b.png" alt="在这里插入图片描述"> 这里增加的是个1.09TB的硬盘

### 查看lv信息

通过`lvdisplay`命令查看逻辑卷信息，并重点关注“LV Path|Name|Size” ![在这里插入图片描述](https://img-blog.csdnimg.cn/9f63f5832f2e4e5aa3c5421798f475d7.png<img src="https://img-blog.csdnimg.cn/04911c18a90f431da9515dfbb07811a3.png" alt="在这里插入图片描述">

### 扩容

#### 确定扩容的信息

目录，这里以/home目录为例。 扩容前先利用命令`vgdisplay`查看扩容前的vg信息 <img src="https://img-blog.csdnimg.cn/81af621ebe3c44f599b182013c13f16d.png" alt="在这里插入图片描述">

#### 执行扩容命令

`vgextend centos /dev/sdc`，这样将新增磁盘挂载的磁盘扩容到VG Name 执行成功提示
- 1- 2
#### 再次查看VG信息

`vgdisplay` <img src="https://img-blog.csdnimg.cn/463c721158dd475f949d66e17881ae2f.png" alt="在这里插入图片描述"> 此时虽然VG已经扩容，但lv信息并未改变，通过命令`lvdisplay`和`df -h`所查看的信息尚未变化，也即尚未真正扩容。

#### lv扩容

执行命令`lvextend -L +1T /dev/centos/home`，命令格式 `lvextend -L [+size，单位可以是M|G|T，不超过新加磁盘的空间] 待扩容的逻辑卷` 执行结束提示成功 <img src="https://img-blog.csdnimg.cn/9fe4f17d9d5f46eea22c50e86595e6b9.png" alt="在这里插入图片描述">

这是，虽然lv信息已经改变，但是`df -h`还是没有变化，

#### 重置逻辑卷

这里注意，先用`blkid`命令查看文件系统类型 如果是Linux6.x使用的命令（ext格式）是 `resize2fs [参数]` 如果是linux7.x的系统使用命令（xfs格式）： `xfs_growfs [参数]` <img src="https://img-blog.csdnimg.cn/ceb39be5c4a143939d08c7991222dad4.png" alt="在这里插入图片描述"> 此时，再次查看磁盘信息，已成功扩容 <img src="https://img-blog.csdnimg.cn/f4cb46f2e2aa4bf696b28a894761f3eb.png" alt="在这里插入图片描述"> **重启服务器，仍然有效**

### 注意事项
1. 以上命令基本都需要管理员权限1. 扩容操作，对普通用户透明；无需迁移数据；1. 重启服务器，无需手工挂载新磁盘
## 相关资料

同样的问题，这里有一些其他的方法，比如，：挂载新硬盘后，将指定目录重新重定向到新的磁盘分区，但需要完全迁移数据到新磁盘，若目录较大，磁盘速度较慢，比较耗时（不清楚原目录的空间是否能够回收再利用）。一般的方法，在修改重定向后，还需要修改配置文件，保证重启后自动挂载新添加的磁盘。 还有一些方法，是在虚拟机环境下的指定目录扩容，如，并未测试在物理机环境上是否有效。  
