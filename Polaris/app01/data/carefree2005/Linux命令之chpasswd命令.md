
--- 
title:  Linux命令之chpasswd命令 
tags: []
categories: [] 

---
## 一、chpasswd命令简介

  chpasswd命令用于同时更改多个用户的密码。它可以从标准输入或指定的文件中读取用户名和密码的组合，并将其应用于系统中的用户。chpasswd命令通常用于批量更改用户密码，特别是在自动化脚本或批处理任务中，该命令需要root账户权限才可以执行。使用chpasswd命令时，可以通过以下两种方式提供用户名和密码的组合：
- 从标准输入读取：可以通过管道或重定向操作符将用户名和密码的组合传递给chpasswd命令。每个用户名和密码的组合应占据一行，并使用冒号分隔用户名和密码。- 从文件读取：可以通过指定文件路径作为chpasswd命令的参数来读取用户名和密码的组合。文件中的每个用户名和密码的组合应占据一行，并使用冒号分隔用户名和密码。
## 二、chpasswd命令使用示例

### 1、获取命令帮助

>  
 [root@s152 ~]# chpasswd -h 用法：chpasswd [选项]  选项： -c, --crypt-method 方法 加密方法(NONE DES MD5 SHA256 SHA512 中的一个) -e, --encrypted 提供的密码已经加密 -h, --help 显示此帮助信息并推出 -m, --md5 使用 MD5 算法加密明文密码 -R, --root CHROOT_DIR chroot 到的目录 -s, --sha-rounds SHA* 加密算法中的 SHA 旁边的数字 


### 2、修改单个用户密码

>  
 [root@s152 ~]# useradd username1 [root@s152 ~]# echo “username1:password1” | chpasswd <img src="https://img-blog.csdnimg.cn/9d494066a0404767a370628540095ed4.png" alt="在这里插入图片描述"> 


### 3、从标准输入批量修改用户密码

  输入chpasswd命令后直接回车，交互窗口下按照如下格式输入用户名和密码，使用ctl+D结束输入。

>  
 [root@s152 ~]# chpasswd username1:123456 username2:123456 username3:12345678 [root@s152 ~]# su - username1 上一次登录：五 8月 25 15:24:34 CST 2023pts/0 上 [username1@s152 ~]$ su - username3 密码： 上一次登录：五 8月 25 15:47:27 CST 2023pts/0 上 最后一次失败的登录：五 8月 25 15:47:43 CST 2023pts/0 上 最有一次成功登录后有 1 次失败的登录尝试。 


### 4、从文件读取密码批量修改用户密码

  当然我们也可以使用cat结合|管道符的方式，可以完成批量用户密码修改。

>  
 [root@s152 ~]# cat pass.txt username1:1234567 username2:1234567 username3:12345678 [root@s152 ~]# cat pass.txt | chpasswd 


### 5、使用密码密文修改用户密码

  我们可以使用openssl生成密码的密文内容，将密文内容写入到文件中，然后通过使用-e参数批量修改密码。

```
[root@s152 ~]# openssl passwd -1 Wuhs@pass
$1$1lP9KfKx$uj1QJqB4EjMXTGN9YOk3G1
[root@s152 ~]# cat pass.txt 
username1:$1$1lP9KfKx$uj1QJqB4EjMXTGN9YOk3G1
username2:$1$1lP9KfKx$uj1QJqB4EjMXTGN9YOk3G1
username3:$1$1lP9KfKx$uj1QJqB4EjMXTGN9YOk3G1
&gt;[root@s152 ~]# cat pass.txt |chpasswd -e
[root@s152 ~]# su - username1           
上一次登录：五 8月 25 16:12:24 CST 2023pts/0 上
[username1@s152 ~]$ su - username2
密码：
上一次登录：五 8月 25 16:12:46 CST 2023pts/0 上
[username2@s152 ~]$ 

```

### 5、指定加密算法修改用户密码

>  
 [root@s152 ~]# cat pass2.txt username1:123456 username2:12345678 username3:12345678 [root@s152 ~]# cat pass2.txt | chpasswd -m 


## 三、使用语法及参数说明

### 1、使用语法

>  
 [root@s152 ~]# chpasswd [选项] 


### 2、参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-c, --crypt-method 方法</td><td align="left">加密方法(NONE DES MD5 SHA256 SHA512 中的一个)</td>
<td align="left">-e, --encrypted</td><td align="left">提供的密码已经加密</td>
<td align="left">-h, --help</td><td align="left">显示此帮助信息并推出</td>
<td align="left">-m, --md5</td><td align="left">使用 MD5 算法加密明文密码</td>
<td align="left">-R, --root CHROOT_DIR</td><td align="left">chroot 到的目录</td>
<td align="left">-s, --sha-rounds</td><td align="left">SHA* 加密算法中的 SHA 旁边的数字</td>

## 四、chpasswd命令使用实践

### 1、修改主机所有普通用户密码为随机密码
- 获取主机普通用户列表
```
[root@s152 ~]# grep -A100 "1000" /etc/passwd
wuhs:x:1000:1000::/home/wuhs:/bin/bash
username1:x:1001:1001::/home/username1:/bin/bash
username2:x:1002:1002::/home/username2:/bin/bash
username3:x:1003:1003::/home/username3:/bin/bash
user1:x:1004:1004::/home/user1:/bin/bash
user2:x:1005:1005::/home/user2:/bin/bash
user3:x:1006:1006::/home/user3:/bin/bash

```
- 截取用户名
```
[root@s152 ~]# grep -A100 "1000" /etc/passwd |awk -F ":" '{print $1}'
wuhs
username1
username2
username3
user1
user2
user3

```
- 生产随机密码 为了主机安全，我们可以使用rand命令给每个用户生成随机密码。 <img src="https://img-blog.csdnimg.cn/1894da868c91407c82c992a511a9c1f2.png" alt="在这里插入图片描述">
```
[root@s152 ~]# grep -A100 "1000" /etc/passwd |awk -F ":" '{print $1}'|while read username; do echo "$username:$(openssl rand -base64 12 | tr -d '/+=' | cut -c1-10)"; done
wuhs:5alFTKDlx4
username1:sk6cLRudWd
username2:dmXUNwtbfV
username3:9uSatzk4o5
user1:u7oyTpJNsU
user2:skPUFLSBph
user3:N9H26K9DAn

```
- 写入密码文件
```
[root@s152 ~]# grep -A100 "1000" /etc/passwd |awk -F ":" '{print $1}'|while read username; do echo "$username:$(openssl rand -base64 12 | tr -d '/+=' | cut -c1-10)"; done &gt; passwords.txt 

```
- 批量修改用户密码
```
[root@s152 ~]# cat passwords.txt | chpasswd 

```

### 2、修改主机所有普通用户为指定密码
- 获取用户列表并生成指定密码的密文文件
```
[root@s152 ~]# grep -A100 "1000" /etc/passwd |awk -F ":" '{print $1}'|while read username; do echo "$username:`openssl passwd -1 123456`"; done | tee &gt; passwords.txt    
[root@s152 ~]# cat passwords.txt 
wuhs:$1$btyaR2sN$FveCHL1OmoXlxOchhGfcS0
username1:$1$G91mrc9c$Mk8WfCDlAdkF7rBeVqKRA/
username2:$1$w3fDQoya$IB68pOvfFsF8Q3o9.bl3S/
username3:$1$otFkp13s$XaKllMYpAEw..O86v5mGo.
user1:$1$NwidAVMb$dGtoik4PJveKhaD8ETwv6.
user2:$1$ILVS7XnP$N8LA9lu1UusMqaecEG33Z1
user3:$1$ybXJAUnb$oFLxTE4qi8J7/AuneQQzV0

```
- 批量修改密码
>  
 [root@s152 ~]# cat passwords.txt |chpasswd -e [root@s152 ~]# su - wuhs 上一次登录：五 8月 25 16:52:48 CST 2023pts/0 上 [wuhs@s152 ~]$ su - user1 密码： 上一次登录：五 8月 25 16:52:55 CST 2023pts/0 上 

