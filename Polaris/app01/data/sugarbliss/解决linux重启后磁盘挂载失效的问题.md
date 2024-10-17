
--- 
title:  解决linux重启后磁盘挂载失效的问题 
tags: []
categories: [] 

---
>  
 用mount挂载分区之后重启就没有了，原因是因为这个挂载是临时的，而不是永久的。磁盘Linux分区都必须挂载到目录树中的某个具体的目录上才能进行读写操作，然而在linux操作系统中fstab正是负责这一配置的。在开机的时候linux操作系统会调用fstab配置文件，根据该配置文件挂载分区到操作系统的。这是重启后挂载的分区丢失的根本原因，所以我们只需要修改/etc/fstab文件就能解决这个问题。 


#### 一、用df -Th命令查看你要挂载的磁盘信息

第一列是你**要挂载的设备**，第二列是**文件系统类型**，最后一列是**挂载点**，这几个后面要用到；

 <img alt="" height="213" src="https://img-blog.csdnimg.cn/20200630092725652.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N1Z2FyYmxpc3M=,size_16,color_FFFFFF,t_70" width="463">

#### 二、vi /etc/fstab命令，进入后再添加一列

<img alt="" height="178" src="https://img-blog.csdnimg.cn/20200630093854865.png" width="708">

#### 三、在修改/etc/fstab文件后，运行mount -a命令验证一下配置是否正确

 执行mount -a命令后，用df -h查看会发现磁盘已经挂载成功，说明输入没有错误。下次重启的时候系统就可以自动进行挂载了。完结撒花！
