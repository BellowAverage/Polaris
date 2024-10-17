
--- 
title:  linux高级篇基础理论四（rsync，inotify，squid，KVM虚拟机） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


运维人员辛苦和汗水总结的干货理论希望对你有所帮助

<img alt="" height="80" src="https://img-blog.csdnimg.cn/fd3fee85df1d4cffba97164ba01cdf81.gif" width="640">

\

**目录**







































### rsync

#### 1、rsync的作用：

一款快速增量备份工具 支持本地复制，或者与其他ssh、rsync主机同步

#### 2、配置源的两种表示方法（服务器端）

方法一：  用户名@主机地址::共享模块名 方法二：  rsync://用户名@主机地址/共享模块名

#### 3、reync客户端的上行和下行：

下行（下载）：     rsync  -avz   用户名@服务器IP地址::共享名    /本地目录 上行（上传）：     rsync  -avz   /本地目录、   用户名@服务器IP地址::共享名

##### 4、rsync配置文件说明：

主配置文件：    /etc/rsyncd.conf 端口号：   tcp   873 启动服务：   rsync   --daemon 停止服务：   kill    $(cat    /var/run/rsyncd.pid)

##### 5、实施同步的优点：

一旦同步源出现变化，立即启动备份 职业同步源无变化，则不执行备份

##### 6、配置实施同步：

需要配置inotify+rsync同步执行，只能实现上行。需要写脚本来实现 inotify软件和脚本都在客户端操作。

### squid

#### 1、squid代理的作用：

缓存网页对象，减少重复请求

#### **2、代理的基本类型**

传统代理：适用于Internet互联网，需要明确指定服务端（浏览器需要配置） 透明代理：适用于共享上网网关，不需要指定服务端（浏览器不需要配置）

#### 3、使用代理的好处

提高web访问速度 隐藏客户机真实ip地址

##### 4、查看linux网关

##### route  -n   5、ACL访问控制：

(1)定义格式 acl 列表名   列表类型     列表内容 （2）应用ACL： httpd_access  allow  列表名   （允许） httpd_access  deny  列表名   （拒绝） 备注：应用acl规则,一定要放在httpd_access   deny  all   前面 （3）常用的列表类型： src   (源地址) dst（目标地址） port（目标端口） dstdomain（目标域） time（访问时间，MTWHF分别2表示周一至周五）

##### 6、squid配置文件说明

主配置文件：/etc/squid.conf 端口号：tcp    3128 检查语法： squid    -k    parse 初始化：squid  -z 启动服务：squid 重新加载服务： squid  -k    reconfigure

### KVM

#### 1、KVM的作用：

是linux系统中的一个虚拟化程序，可以模拟安装多个虚拟机

#### 2、KVM的两种网络类型：

（1）用户模式，即NAT模式，是默认网络模式，Teddy是KVM中虚拟机能访问外部网络，但是外部网络不能访问KVM中的虚拟机。 （2）桥接模式：特点是KVM中的虚拟机和外部网络可以互相访问。

#### 3、虚拟机磁盘文件格式类型：

raw,  qcow2(支持快照)，qed


