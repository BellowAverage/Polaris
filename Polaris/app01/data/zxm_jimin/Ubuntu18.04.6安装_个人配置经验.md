
--- 
title:  Ubuntu18.04.6安装_个人配置经验 
tags: []
categories: [] 

---
主要参考博客 

#### 文章目录
- - 


有几点不同之处：

## 暗夜精灵装ubuntu

参考博客： 1）请关闭BIOS中各种**安全启动选项**，能关的你就关掉吧。

2）安装时，按开机键后，在BIOS启动界面，按ESC，进入启动选项，不是BIOS选项，是启动选项，**选择USB启动**，注意不要选UEFI的USB启动选项。 <img src="https://img-blog.csdnimg.cn/ab95767808d042f88bc4a0af49f07ba1.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

3）这时开始安装ubuntu了，一开始就按ESC，这样就就有安装选项了，选择Install ubuntu，一般来说自动进入安装。

其他步骤按照  进行。

## 具体分区操作

**分区大小**： boot ：1G swap area : 32G / : 150G /home : 剩下空间（200G左右）

**进行手动分区**： 假设你留出的空闲分区为400G，点击空闲盘符，点击"+"进行分区，如下：

1）**efi**：如果是双硬盘，找到事先分好的**1G**空闲分区添加，**逻辑分区**，**空间起始位置**，**用于efi**。这个分区必不可少，用于安装ubuntu启动项。以下步骤单双硬盘就一样了，都在那个450G的空闲分区上添加

2）**swap**:中文是"交换空间"，充当ubuntu的虚拟内存，一般的大小为电脑物理内存的2倍左右，可以将其分为 **32G**，**逻辑分区**，**空间起始位置**，用于"swap"或"**交换空间**"

3）**/**:这是ubuntu 的根目录,用于安装系统和软件，相当于windows的C盘，我们将其分为 **150G**，**主分区**，**空间起始位置**，用于"**ext4日志文件系统**"，**挂载点为"/"**（根据你的磁盘空间调整，可以大一点，毕竟ubuntu装软件都是默认装在根目录的）

4）**/home**:相当于windows的其他盘，**剩下的全分给它**，**逻辑分区**，**空间起始位置**，用于"**ext4日志文件系统**"，**挂载点为"/home"**

好了，分区完毕.

**启动位置**：

注意这个启动位置，在分区界面的下方，选择安装启动项的位置，我们刚刚不是创建了**1G的efi分区**吗，现在你看看这个区前面的编号是多少，比如我的是**/dev/nvme0n1p7**,不同的机子会有不同的编号。 下拉列表“**安装启动引导器的设备**”，选择这个efi分区编号 /dev/nvme0n1p7（这里一定要注意，windows的启动项也是efi文件，大小大概是500M，而我们创建的ubuntu的efi大小是1G，一定要选对），之后点击"**Install Now**" <img src="https://img-blog.csdnimg.cn/8f7a3d1ad75643c6b5feb726ca6eb47d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 2.全部完成之后，会提醒你重启，点"现在重启"，**黑屏后把U盘拔了**，如果卡死就强制关机再重启就好。

我的设备：暗夜精灵7
