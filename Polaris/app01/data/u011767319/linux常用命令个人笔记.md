
--- 
title:  linux常用命令个人笔记 
tags: []
categories: [] 

---
### linux常用命令

**以centos为例（这篇文章是佛系记录，不会全部写的。见谅）**

>  
 如果用的是ubuntu 请在命令前面加**sudo** 


```

//查看防火墙状态 
systemctl status firewalld.service
//关闭防火墙
systemctl stop firewalld.service
//禁止防火墙服务器（一旦重启操作系统，防火墙就自动开启了，该怎么设置才能永久关闭防火墙呢？）
systemctl disable firewalld.service

//创建文件
mkdir
//查询端口
netstat -tln|grep 80(端口)
//查看端口是否被占用
lsof -i :80(端口)
//查看当前所在地址
pwd
//ps系列的命令
ps 
参数：
-A ：所有的进程均显示出来，与 -e 具有同样的效用；
-a ： 显示现行终端机下的所有进程，包括其他用户的进程；
-u ：以用户为主的进程状态 ；
x ：通常与 a 这个参数一起使用，可列出较完整信息。
输出格式规划：
l ：较长、较详细的将该PID 的的信息列出；
j ：工作的格式 (jobs format)
-f ：做一个更为完整的输出。
//例子查询nginx的路径及信息
ps -ef|grep nginx

```

### 查看linux基本信息

```
//查看信息
top

```

**运行结果：** <img src="https://img-blog.csdnimg.cn/20210531155133904.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**信息描述**

```
top - 　　　　　　系统当前时间
up 　　　　　 系统已开机多长时间
user 　　　　 当前用户数
load average cpu平均负载，三个数值分别为，1分钟，5分钟，15分钟
Tasks 　　 系统当前进程数，total：总进程数，running：正在运行的进程数，sleeping：睡眠的进程数，stopped：停止的进程数，zombie：僵尸进程数
%Cpu(s) cpu使用率，us：用户使用cpu百分百，sy：系统内核使用cpu百分百，id：剩余的cpu百分百
Mem 　　　 内存使用信息，total：总内存大小，free：空闲的内存，used：已使用的内存，buff/cache：缓存的内存大小
Swap 　　 虚拟内存信息
PID　　　　 进程id
USER　　　　 进程所有者
PR　　　　　　 优先级
NI　　　　　　　nice值，负值表示高优先级，正值表示低优先级
VIRT 　　　　　 进程使用的虚拟内存总量
RES 　　　　　 进程使用的物理内存大小
SHR 　　　　　 共享内存大小
S 　　　　　　 进程状态，D：不可中断的睡眠状态，R：运行，S：睡眠，T：跟踪/停止，Z：僵尸进程
%CPU 　　　　 进程使用的CPU占用百分比
%MEM 　　　　 进程使用的物理内存百分比
TIME+ 　　　　 进程使用的CPU时间总计
COMMAND　　 命令名

```

**如何让top更改内存单位显示**

>  
 进入top页面后 按shift+e 就可以更改内存单位显示 


**效果图如下：**

<img src="https://img-blog.csdnimg.cn/20210531155512317.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
