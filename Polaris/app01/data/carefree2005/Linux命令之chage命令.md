
--- 
title:  Linux命令之chage命令 
tags: []
categories: [] 

---
## 一、命令简介

  系统进行等保评测的时候会检查账户密码复杂度、有效期等内容。chage用于密码的实效管理，用来修改帐号和密码的有效期。chage命令更改密码更改与上次密码更改日期之间的天数。系统使用此信息确定用户何时必须更改其密码。chage命令修改的都是/etc/shadow文件最后6项的值。 <img src="https://img-blog.csdnimg.cn/ba09d1528252464fa2f43a785172ac36.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/306e0bcca5c2406a952ace81464520d0.png" alt="在这里插入图片描述">

## 二、使用示例

### 1、获取命令帮助

>  
 [root@s142 etc]# chage -h Usage: chage [options] LOGIN … 


### 2、查看用户密码有效期信息

>  
 [root@s142 etc]# chage -l wuhs Last password change : Aug 24, 2022 Password expires : never Password inactive : never Account expires : Aug 20, 2122 Minimum number of days between password change : 0 Maximum number of days between password change : 99999 Number of days of warning before password expires : 7 <img src="https://img-blog.csdnimg.cn/c6576bc5500941a18bdc4847f5eff49a.png" alt="在这里插入图片描述"> 


### 3、设置密码最近一次修改日期为指定日期

>  
 [root@s142 etc]# chage -d 2022-8-22 wuhs <img src="https://img-blog.csdnimg.cn/346eb0a592b24fd2857a0e2d8021e60a.png" alt="在这里插入图片描述"> [root@s142 etc]# chage -d 0 wuhs <img src="https://img-blog.csdnimg.cn/caf2b54c864a4ccca50b61b057d1b170.png" alt="在这里插入图片描述"> [root@s142 etc]# chage -d -1 wuhs 


### 4、设置账户过期时间

>  
 [root@s142 etc]# chage -E 0 wuhs [root@s142 etc]# chage -E 2022-8-25 wuhs [root@s142 etc]# chage -E -1 wuhs<img src="https://img-blog.csdnimg.cn/e7929042fbaf4c3997fb6bb693f6beed.png" alt="在这里插入图片描述"> 


### 5、设置密码过期指定天数后失效

>  
 [root@s142 etc]# chage -I 3 wuhs 


### 6、设置密码修改间隔最小和最大天数

>  
 [root@s142 etc]# chage -m 30 wuhs [root@s142 etc]# chage -M 180 wuhs [root@s142 etc]# chage -l wuhs Last password change : never Password expires : never Password inactive : never Account expires : never Minimum number of days between password change : 30 Maximum number of days between password change : 180 Number of days of warning before password expires : 7 


### 7、设置密码到期提前提醒天数

>  
 [root@s142 etc]# chage -W 3 wuhs [root@s142 etc]# chage -l wuhs Last password change : never Password expires : never Password inactive : never Account expires : never Minimum number of days between password change : 30 Maximum number of days between password change : 180 Number of days of warning before password expires : 3 


## 三、使用语法及参数说明

### 1、使用语法

>  
 用法：chage [options] 账户 


### 2、参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-d, --lastday LAST_DAY</td><td align="left">将最近一次密码修改时间设为“LAST_DAY”</td>
<td align="left">-E, --expiredate EXPIRE_DATE</td><td align="left">将帐户过期时间设为“EXPIRE_DATE” 0表示马上过期，-1表示永不过期</td>
<td align="left">-h, --help</td><td align="left">获取命令帮助信息</td>
<td align="left">-I, --inactive INACTIVE</td><td align="left">过期 INACTIVE 天数后，设定密码为失效状态</td>
<td align="left">-l, --list</td><td align="left">列出用户以及密码的有效期</td>
<td align="left">-m, --mindays MIN_DAYS</td><td align="left">将两次改变密码之间相距的最小天数设为“MIN_DAYS”</td>
<td align="left">-M, --maxdays MAX_DAYS</td><td align="left">密码保持有效的最大天数</td>
<td align="left">-R, --root CHROOT_DIR</td><td align="left">chroot 到的目录</td>
<td align="left">-W, --warndays WARN_DAYS</td><td align="left">密码过期前，提前收到警告信息的天数</td>
