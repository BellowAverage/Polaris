
--- 
title:  linux高级篇基础理论三（详细文档、SSH、YUM） 
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

**目录**































### SSH

#### 1、ssh协议的功能：

为客户机提供安全的shell环境（字符），用于远程管理

#### 2、openssh的服务说明：

服务名：sshd 重启服务：systemctl   restart     sshd 主配置文件：  /etc/ssh/sshd_config 端口号 ： tcp    22/

#### 3、主配置文件说明（/etc/ssh/）：

修改端口：  prot    22 禁用DNS反向解析： UseDNS   no 禁止root用户：PermitRootLogin   no 禁止空密码用户：PermitEmptyPassword   no 只允许个别用户登录：AllowUsers     zhangsan    lisi@192.168.1.20 只拒绝个别用户登录：DenyUsers     zhangsan 备注： AllowUsers和DenyUsers  不能同时配置

#### 4、登录验证方式：

密码验证： 核对用户名、密码是否匹配 密钥对验证：核对客户的私钥、服务端公钥是否匹配

#### 5、linux客户端远程登录：

（1）ssh命令———远程安全登录 ssh  -p    端口号   用户名@IP地址 （2）scp命令———远程安全赋值 下载：scp   -P    端口号    用户名@IP地址:/路径/文件名/    /本地目录 上传：scp   -P    端口号    /本地路径/文件名     用户名@IP地址：/路径/ 大写P （3）sftp命令———安全ftp上下载（不常用）

#### 6、Windows客户端远程登录工具：

xshell，putty，securCRT    xshell的命令     上传文件：rz          下载文件：sz   /路径/文件名

#### 7、TCP wrapper  软件的两个访问控制策略文件:

/etc/hosts.allow(允许的) /etc/hosts.deny(拒绝的)

#### 8、两个策略文件的应用顺序：

先检查hosts.allow，找到匹配则允许访问 否则再坚持hosts.deny，找到则拒绝访问 若两个文件中均无匹配策略，则默认允许访问

### YUM

#### 1、YUM的功能:

基于rpm包构建的软件更新机制 可以自动解决依赖关系 所有软件包由集中的yum软件仓库提供

#### 2、软件仓库的提供方式:

FTP服务：ftp://... HTTP服务：http://... 本地目录：file：///...

#### 3、客户端yum命令：

（1）清空yum缓存： yum clean   all （2）查询软件包 yum   list   软件名 yum   info  软件名 yum   search   关键字 （3）安装软件包 yum    -y   install   软件名 （4）软件包升级 yum   -y   update （5）卸载软件 yum  -y   remove   软件名

#### 4、linux的PXE技术的作用：

用于远程批量部署linux操作系统。

>  
 人生要尽全力度过每一关,不管遇到什么困难不可轻言放弃！！！ 

