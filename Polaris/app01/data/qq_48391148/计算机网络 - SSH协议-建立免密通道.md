
--- 
title:  计算机网络 - SSH协议-建立免密通道 
tags: []
categories: [] 

---
###  

**目录**







































### 知识点1：什么是SSH？

>  
 **SSH叫安全外壳协议（Secure Shell），是一种加密的网络传输协议，可在不安全的网络中网络服务提供安全的传输环境。它通过在网络中创建安全隧道来实现 SSH 客户端和服务器之间的连接。** 
 **ssh协议工作在****应用层** 


### **知识点2：SSH解决了什么问题？**

>  
 **对传输的数据进行加密，保护传输数据的安全** 
 **SSH 是较可靠，专为会话和其他网络服务提供安全性的协议。利用 SSH 协议可以有效防止远程管理过程中的信息泄露问题。** 


### 知识点3：什么是openssh?

>  
 **OpenSSH 是使用 SSH 协议进行远程登录的首要连接工具。它加密所有流量以消除窃听、连接劫持和其他攻击。此外，OpenSSH 提供了大量的安全隧道功能、多种身份验证方法和复杂的配置选项。** 
 **openssh开源免费的，是一个C/S架构的软件** 


#### 查看机器上面安装的openssh

```
[root@wangsh lianxi]# rpm -qa |grep openssh
openssh-clients-7.4p1-21.el7.x86_64
openssh-server-7.4p1-21.el7.x86_64
openssh-7.4p1-21.el7.x86_64

```

### 知识点4：SSH服务介绍

>  
 **远程Shell应用程序 ·允许用户在远程机器上执行任意命令 ·让标准输出在本地 ·早期明文远程协议：telnet** 
 **SSH（Secure Shell，安全的外壳） ·为客户机提供安全的Shell环境，用于远程管理 ·默认端口：TCP 22** 
 **SSH基于公钥加密（非对称加密）技术 ·数据加密传输 ·客户端和服务器的身份验证** 
 **#注：23号端口是明文的，已经淘汰了** 


#### 查看sshd服务是否启动： 1、看进程

```
[root@wangsh .ssh]# ps -ef | grep sshd
root       1059      1  0 8月08 ?       00:00:00 /usr/sbin/sshd -D
root       7080   1059  0 23:07 ?        00:00:00 sshd: root@pts/0
root       7168   7084  0 23:27 pts/0    00:00:00 grep --color=auto sshd

```

#### 2、看端口

```
[root@wangsh .ssh]# lsof -i:22
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd    1059 root    3u  IPv4  20976      0t0  TCP *:ssh (LISTEN)
sshd    1059 root    4u  IPv6  20992      0t0  TCP *:ssh (LISTEN)
sshd    7080 root    3u  IPv4 256692      0t0  TCP wangsh:ssh-&gt;192.168.44.1:58874 (ESTABLISHED)
[root@wangsh .ssh]# 
```

### 知识点5：SSH的配置文件

>  
 **/etc/ssh/sshd_config   sshd服务器端的配置文件** 
 **/etc/ssh/ssh_config  ssh客户端命令的配置文件** 


#### 一些常见的配置文件内容

>  
 **Port 22  --  默认端口：22** 
 **ListenAddress 192.168.2.1  --  监听ip** 
 **PubkeyAuthentication yes  --  启用公钥认证** 
 **PermitRootLogin yes --  允许root用户登录** 
 **MaxAuthTries 6  --  最多6次密码尝试** 
 **DenyUsers zhangsan  --  不允许zhangsan登录** 


### 知识点6：如何使用ssh批量管理服务器？

**示例：在100台机器上面安装nginx服务**

>  
 **1、使用一台中心服务器作为中心控制机器，与100台要操作的机器建立免密通道** 
 **2、编写一键安装nginx脚本，使用scp命令将脚本传递到100台服务器上面** 
 **3、然后再100台服务器上面执行脚本，一键安装nginx服务** 


### 知识点7：SSH的密钥认证

>  
 **公钥（Public Key）和 私钥 （Private Key）** 
 **        公钥和私钥是成双成对的，这两个密钥互不相同，两个秘钥可以相互解密和加密** 
 **        不能根据一个密钥而退出另外一个密钥** 
 **        公钥对外公开，私钥只有私钥的持有人才知道** 
 **        私钥应该由密钥的持有人妥善保管** 


#### **根据实现功能的不同可以分为数据加密和数字签名**

 <img alt="" height="456" src="https://img-blog.csdnimg.cn/c6ef7254dc174612a770b67f03dfa265.png" width="1099">

####  **ssh身份验证过程**

<img alt="" height="671" src="https://img-blog.csdnimg.cn/3827f5a288f1462d84a79343b8cab982.png" width="1200">

 

#### **ssh公钥认证流程**

<img alt="" height="787" src="https://img-blog.csdnimg.cn/dc9f669d7dca49919957f886482c6f65.png" width="1200">

### 知识点 8：建立免密通道

** 示例：在两台机器之间建立免密通道**

>  
 **准备两台服务器 A：****192.168.44.132****， B：****192.168.44.160****，都使用root用户** 


#### ** 第一步，生成密钥对，在192.168.44.132上面使用root用户生成密钥对**

>  
 **ssh-keygen -t rsa -t  指定加密算法 为 rsa算法** 
 **生成密钥对的时候会让你指定一个目录来存放密钥对，默认是家目录下面的.ssh目录里面，这里采用默认就行，直接敲回车** 
 **这里还可以生成一个密钥对的密码，但是我们的目的就是建立免密通道，所以这里也是直接敲回车，不设置密钥对密码。** 


```
[root@wangsh ~]# ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
/root/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:nUBGQTh4CKCGv7OLKTC2lMjBFgebIFkxAdprGp36XBk root@wangsh
The key's randomart image is:
+---[RSA 2048]----+
|=*B+ o +*.       |
|Boooo +o         |
|=++  . ..        |
|.* o     o .     |
|= O E   S o      |
|+X . o           |
|*.+ o            |
|.* +             |
|+ =.             |
+----[SHA256]-----+



```

**可以看到，公钥其他人是有读的权限的，但是私钥只有属主有rw权限**

```
[root@wangsh .ssh]# ll
总用量 12
-rw-------. 1 root root 1679 8月  10 23:08 id_rsa
-rw-r--r--. 1 root root  393 8月  10 23:08 id_rsa.pub
-rw-r--r--. 1 root root  527 7月  27 15:06 known_hosts


```

#### **第二步、上传公钥文件**

```
[root@wangsh .ssh]# ssh-copy-id -p 22 -i id_rsa.pub root@192.168.44.160
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
root@192.168.44.160's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -p '22' 'root@192.168.44.160'"
and check to make sure that only the key(s) you wanted were added.

[root@wangsh .ssh]# 


```

#### **第三步、登录验证我们的免密通道，可以看到不用密码就能登录了。**

```
[root@wangsh .ssh]# ssh root@192.168.44.160
Last login: Wed Aug 10 23:06:29 2022 from 192.168.44.132
[root@network ~]# 


```

#### **建立免密通道以后我们对两台机器进行操作就很方便了。不用再进行密码认证**

**ssh和scp都可以直接进行，无需密码。**

```
[root@wangsh .ssh]# ssh root@192.168.44.160 mkdir ~/wangsh
[root@wangsh lianxi]# scp 1.txt root@192.168.44.160:~/
1.txt                                                          100%    0     0.0KB/s   00:00    
[root@wangsh lianxi]# ssh root@192.168.44.160
Last login: Wed Aug 10 23:34:50 2022 from 192.168.44.132
[root@network ~]# ls
1.txt  8yue10  anaconda-ks.cfg  os_fork.py  wangsh

```


