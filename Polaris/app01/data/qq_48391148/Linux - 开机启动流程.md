
--- 
title:  Linux - 开机启动流程 
tags: []
categories: [] 

---
**目录**



































## 一、掌握开机启动流程的意义：

开机启动流程

### **1.1  为什么需要了解开机启动流程？**

### **1.2  在日常的运维过程中，是否会遇到机器出现问题启动不了？**

1.自己的机房 --》自建机房 --》大量的物理机器 --》真实的服务器 --》成本高

2.大量的云服务器 --》阿里云，腾讯云，aws，华为云等，成本低，性价比高

### **1.3  开机启动流程的意义**

1.掌握让某个软件或服务开机自动运行的方法

2.开机不能正常启动，是什么原因，或者那个环节出现了问题

3.防止黑客植入木马，去查询黑客会把木马放到哪些地方？

 **##############################################**

## 二、开机启动流程

### 2.1  开机启动流程图

<img alt="" height="893" src="https://img-blog.csdnimg.cn/067aa99a8b6b4d379fe403d4846bea87.jpeg" width="887">

 **##############################################** 

### 2.2  开机启动流程

#### 2.2.1  pwoer on 开机

#### 2.2.2  POST开机自检

**开机自检** ：上电自检（POST， Power  On Self  Test）

        **谁去检查？**

                由主板上面的BIOS程序去完成，BIOS（Basic Input Output System）程序，基本输入输出系统。

        **自检什么东西？**

                对CPU、系统主板、基本内存、扩展内存、系统ROM BIOS等器件的测试。如发现错误，给操作者提示或警告。简化或加快该过程，可使系统能够快速启动。

**        电脑里有哪些基本的硬件？**                 主板（motherboard）、cpu、内存，磁盘，网卡，显卡，声卡，电源，鼠标，键盘、显示器等

**##############################################**

#### 2.2.3  BIOS程序对硬件进行检测

**BIOS程序：** BIOS是个人电脑启动时加载的第一个软件。 它是一组固化到计算机内主板上一个**ROM芯片**上的程序，它保存着计算机最重要的基本输入输出的程序、开机后自检程序和系统自启动程序，它可从CMOS中读写系统设置的具体信息。 其主要功能是为计算机提供最底层的、最直接的硬件设置和控制。此外，BIOS还向作业系统提供一些系统参数。系统硬件的变化是由BIOS隐藏，程序使用BIOS功能而不是直接控制硬件。现代作业系统会忽略BIOS提供的抽象层并直接控制硬件组件。

**ROM存储器** ： read only memory  --》只读的存储器  断电信息丢失

**RAM存储器**： random access memory  随机存取存储器  --》可读可写  断电信息不丢失

**既然BIOS程序是固化到只读存储器上面的那么BIOS的一些基本配置保存到哪里？**

BIOS的配置固化到了主板上面的CMOS芯片上面， BIOS是一个程序会读取CMOS芯片里的参数，了解cpu的配置，时间的配置，**启动顺序**的配置等

**CMOS芯片**：CMOS芯片是一种低耗电存储器，其主要作用是用来存放BIOS程序中的设置信息以及系统时间日期。如果CMOS中数据损坏，计算机将无法正常工作

**##############################################**

#### 2.2.4  boot启动顺序检查，启动第一启动顺序

boot  ： 引导、启动的意思

**关于boot启动顺序：**

<img alt="" height="473" src="https://img-blog.csdnimg.cn/733de77b6fad4f41906433efc93cb483.png" width="633">

 第一引导顺序：Removable Devices  可移动设备 （U盘、移动硬盘等）

第二引导顺序：Hard Drive  硬盘

第三引导顺序：CD-ROM Drive 光驱  （安装系统）

第四引导顺序：Network boot from Intel  网络中安装服务器启动

**##############################################**

#### 2.2.5  硬盘中的MBR程序

计算机在按下power键后，开始执行主板BIOS程序，进行完一系列检测和配置以后，

开始按BIOS设定的引导顺序引导系统，会从硬盘中引导系统，BIOS执行完自己的程序以后

如何将执行权交给硬盘？

**MBR程序**：master boot record 主引导记录，位于硬盘的0磁道，0柱面，1扇区，可以看成是硬盘的第一个扇区，MBR里面有一个grub2引导程序，负责启动linux系统

磁盘上面有很多磁道，每个磁道又会划分成63个扇区，每个扇区可以存储**512个字节**

**MBR主引导记录的组成：**

分区表 + grub2主引导程序 + 类型    总共512个字节

grub是linux系统的启动程序 grub2是grub的第2个版本<img alt="" height="322" src="https://img-blog.csdnimg.cn/75a0d100410246c2aeb81f065567918e.jpeg" width="744">

 **##############################################**

**2.2.6  加载/boot里面的光驱**

**/boot目录下面的内容：**<img alt="" height="274" src="https://img-blog.csdnimg.cn/a59d91f6b4e34ecea870871a1e6c04e6.png" width="1079">

 grub2程序会舒适化硬件设备，建立内存空间的映射图，从而将系统的软硬件环境带到一个合适的状态，以便为最终调用操作系统做好一切准备。

**initramfs-4.18.0-147.el8.x86_64.img 文件：**

给内核程序提供一个初始化的内存文件系统的镜像文件 --》临时的根文件系统的镜像文件--&gt;提供程序和配置文件 

        init 初始化

        ram 内存里的存储

        fs 文件系统

**vmlinuz-4.18.0-147.el8.x86_64 文件**

        内核程序文件。

 **##############################################**

**2.2.7  启动systemd进程**

        由于版本的不同，centos6里面启动的第一个进程是init，centos7里面是systemd进程

```
[root@wangsh boot]# pstree -p
systemd(1)─┬─NetworkManager(749)─┬─{NetworkManager}(757)
           │                     └─{NetworkManager}(762)
           ├─VGAuthService(671)
           ├─auditd(646)───{auditd}(647)
           ├─chronyd(679)
           ├─crond(700)
           ├─dbus-daemon(676)───{dbus-daemon}(691)
           ├─login(714)───bash(1325)
           ├─lvmetad(505)
           ├─master(1227)─┬─pickup(4840)
           │              └─qmgr(1237)
           ├─nginx(2248)───nginx(2249)
           ├─polkitd(673)─┬─{polkitd}(692)
           │              ├─{polkitd}(695)
           │              ├─{polkitd}(696)
           │              ├─{polkitd}(698)
           │              ├─{polkitd}(699)
           │              └─{polkitd}(709)
           ├─rsyslogd(1063)─┬─{rsyslogd}(1066)
           │                └─{rsyslogd}(1067)
           ├─sshd(1059)───sshd(4254)───bash(4258)───pstree(4930)
           ├─systemd-journal(488)
           ├─systemd-logind(694)
           ├─systemd-udevd(521)
           ├─tuned(1060)─┬─{tuned}(1307)
           │             ├─{tuned}(1308)
           │             ├─{tuned}(1310)
           │             └─{tuned}(1312)
           └─vmtoolsd(672)─┬─{vmtoolsd}(710)
                           └─{vmtoolsd}(717)

```

 **##############################################**

#### 2.2.8  启动对应的运行级别里面的服务。

**运行级别：runlevel（是centos6的叫法，）**

0 关机

1 单用户模式

2 多用户模式，不能使用nfs

3 完全多用户模式 --》字符界面模式 --》非常正常的模式， 默认最小化安装的模式

4 保留，没使用

5 图形界面

6 重启



init 0 关机

init 3 进入字符界面

init 6 重启

init 5 进入图形界面，但是需要安装了图形界面



**查看当前运行级别**

```
[root@wangsh boot]# runlevel 
N 3
[root@wangsh boot]# 
```

N代表之前最开始进入的模式，如果是N表示没有的模式，没有进行模式切换

3 5 代表开机是先进入运行级别3，后来切换到运行级别5

**查看/etc/inittab文件**

```
[root@wangsh boot]# vim /etc/inittab 

# inittab is no longer used when using systemd.
#
# ADDING CONFIGURATION HERE WILL HAVE NO EFFECT ON YOUR SYSTEM.
#
# Ctrl-Alt-Delete is handled by /usr/lib/systemd/system/ctrl-alt-del.target
#
# systemd uses 'targets' instead of runlevels. By default, there are two main targets:
#
# multi-user.target: analogous to runlevel 3
# graphical.target: analogous to runlevel 5
#
# To view current default target, run:
# systemctl get-default
#
# To set a default target, run:
# systemctl set-default TARGET.target

```

 可以看到这个文件里面说：

```
 multi-user.target: analogous to runlevel 3
 graphical.target: analogous to runlevel 5
```

** multi-user.target类似于第3运行级别**

** graphical.target类似于第5运行级别**

```
# To view current default target, run:
# systemctl get-default
#
# To set a default target, run:
# systemctl set-default TARGET.target
#

```

**显示当前的默认运行级别使用这条命令**

        systemctl get-default  查看默认的运行级别

**设置开机进入图形界面**

        set-default graphical.target

```
[root@wangsh boot]# systemctl get-default
multi-user.target
[root@wangsh boot]# systemctl set-default graphical.target

```

 **##############################################**

#### 2.2.9  运行 /etc/systemd/system/multi-user.target.wants/ 下的服务

```
[root@wangsh multi-user.target.wants]# pwd
/etc/systemd/system/multi-user.target.wants
[root@wangsh multi-user.target.wants]# ls
auditd.service     irqbalance.service      remote-fs.target        tuned.service
chronyd.service    kdump.service           rhel-configure.service  vmtoolsd.service
crond.service      NetworkManager.service  rsyslog.service
firewalld.service  postfix.service         sshd.service
[root@wangsh multi-user.target.wants]# ll
总用量 0
lrwxrwxrwx. 1 root root 38 11月 12 2021 auditd.service -&gt; /usr/lib/systemd/system/auditd.service
lrwxrwxrwx. 1 root root 39 11月 12 2021 chronyd.service -&gt; /usr/lib/systemd/system/chronyd.service
lrwxrwxrwx. 1 root root 37 11月 12 2021 crond.service -&gt; /usr/lib/systemd/system/crond.service
lrwxrwxrwx. 1 root root 41 7月  26 15:03 firewalld.service -&gt; /usr/lib/systemd/system/firewalld.service
lrwxrwxrwx. 1 root root 42 11月 12 2021 irqbalance.service -&gt; /usr/lib/systemd/system/irqbalance.service
lrwxrwxrwx. 1 root root 37 11月 12 2021 kdump.service -&gt; /usr/lib/systemd/system/kdump.service
lrwxrwxrwx. 1 root root 46 11月 12 2021 NetworkManager.service -&gt; /usr/lib/systemd/system/NetworkManager.service
lrwxrwxrwx. 1 root root 39 11月 12 2021 postfix.service -&gt; /usr/lib/systemd/system/postfix.service
lrwxrwxrwx. 1 root root 40 11月 12 2021 remote-fs.target -&gt; /usr/lib/systemd/system/remote-fs.target
lrwxrwxrwx. 1 root root 46 11月 12 2021 rhel-configure.service -&gt; /usr/lib/systemd/system/rhel-configure.service
lrwxrwxrwx. 1 root root 39 11月 12 2021 rsyslog.service -&gt; /usr/lib/systemd/system/rsyslog.service
lrwxrwxrwx. 1 root root 36 11月 12 2021 sshd.service -&gt; /usr/lib/systemd/system/sshd.service
lrwxrwxrwx. 1 root root 37 11月 12 2021 tuned.service -&gt; /usr/lib/systemd/system/tuned.service
lrwxrwxrwx. 1 root root 40 11月 12 2021 vmtoolsd.service -&gt; /usr/lib/systemd/system/vmtoolsd.service

```

可以看到，这些文件其实都是链接文件，指向Linux中的要开机自启的服务。

我们使用systemctl disable firewalld这条命令其实就是将这个目录下面的链接文件去除

        使用systemctl enable firewalld这条命令就是在这个目录添加firewalld服务的链接

```
[root@wangsh multi-user.target.wants]# systemctl disable firewalld
Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
[root@wangsh multi-user.target.wants]# systemctl enable firewalld
Created symlink from /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service to /usr/lib/systemd/system/firewalld.service.
Created symlink from /etc/systemd/system/multi-user.target.wants/firewalld.service to /usr/lib/systemd/system/firewalld.service.

```

  **##############################################**

#### 2.2.10 运行 /etc/rc.local 以及 /etc/fstab文件

**rc.local文件：**

如果想执行这个文件必须给他赋予可执行权限。

```
[root@wangsh multi-user.target.wants]# cat /etc/rc.local 
#!/bin/bash
# THIS FILE IS ADDED FOR COMPATIBILITY PURPOSES
#
# It is highly advisable to create own systemd services or udev rules
# to run scripts during boot instead of using this file.
#
# In contrast to previous versions due to parallel execution during boot
# this script will NOT be run after all other services.
#
# Please note that you must run 'chmod +x /etc/rc.d/rc.local' to ensure
# that this script will be executed during boot.

touch /var/lock/subsys/local


[root@wangsh multi-user.target.wants]# ll -d /etc/rc.local
lrwxrwxrwx. 1 root root 13 11月 12 2021 /etc/rc.local -&gt; rc.d/rc.local

```

**/etc/fstab**

告诉linux正常启动过程中挂载哪个磁盘分区

```
[root@wangsh multi-user.target.wants]# cat /etc/fstab 

#
# /etc/fstab
# Created by anaconda on Fri Nov 12 20:24:42 2021
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/centos-root /                       xfs     defaults        0 0
UUID=5f971381-8a7b-4d83-8113-628cfee0a009 /boot                   xfs     defaults        0 0
/dev/mapper/centos-swap swap                    swap    defaults        0 0

```

 

 **##############################################**

**2.2.11  login登录**

login登录查询启动，用户输入用户名和密码以后

Linux系统会自动进入/etc/passwd文件查找文件名

再根据用户名到/etc/shadow文件查找密码

 **##############################################**

#### 2.2.12  加载四个配置文件

登录成功后会加载四个配置文件

**/etc/profile  **全局配置，对所有用户有效

**/etc/bashrc ** 全局配置，对所有用户有效

**~/.bash_profile **  局部配置，只对登录的用户生效

**~/.bashrc ** 局部配置，只对登录的用户生效



**来看看.bash_profile的内容：**

如果，~/.bashrc文件存在就执行这个文件

<img alt="" height="192" src="https://img-blog.csdnimg.cn/79170285c1cc455682826d756174aba5.png" width="1101">

 ~/.bashrc文件有这样一行内容

<img alt="" height="128" src="https://img-blog.csdnimg.cn/0cdda04ca31e4c48a98a93ece8d44da0.png" width="1096">

 如果/etc/bashrc文件存在就执行这个文件

 **##############################################**

## 三、思考题：

### 1.如果你编写了一个程序，需要开机自启的话有哪些方法？

将程序做成一个服务，放到/etc/systemd/system/multi-user.target.wants目录下面。

这个目录下面放的都是开机自启的服务

在/etc/rc.local文件里面添加一条运行程序的命令，就会开机自启

在四个配置文件里面添加运行程序的命令，就会开机自启

还可以添加计划任务，让程序自动运行

### 2.如何确定一个服务有没有开机自启？

在/etc/systemd/system/multi-user.target.wants目录下面查找有没有这个服务

```
[root@wangsh multi-user.target.wants]# ls | grep firewalld
firewalld.service
[root@wangsh multi-user.target.wants]# 

```











 



 
