
--- 
title:  ftp服务器21端口无法连接 
tags: []
categories: [] 

---
## ftp服务器21端口无法连接

>  
 个人测试需要嘛，就在前几天搭了个 ，今天要传文件和一些包上去，但是突然发现上传不了，并且用21端口无法连接到服务器，这下大感不妙，要是给别人使用这服务器的话，总不可能给root权限、22端口吧，然后自己又捣鼓了一会儿，终于成功了。 
 现在总结一下，分享给大家！！！ 


前几天我们是关闭了匿名用户访问的，提供了一个uftp用户用于远程连接，这里远程连接工具用 winscp或 xftp都是可以的。我连接过程中发现uftp 用的是22端口连接，这我立马不干了，22端口给出去这能忍。于是我寻思着该怎么改呢？

<mark>发现是21端口没开放，下面给大家演示一下：</mark>

### 开启FTP的21端口

#### 1、先运行vsftpd服务：

```
service vsftpd start
service vsftpd status

```

#### 2、通过iptables开放21端口

```
#先查看iptables设置：
iptables -nL

#将 21端口插入到INPUT的ACCEPT中
iptables -I INPUT 5 -p tcp --dport 21 -j ACCEPT

#插入到INPUT的ACCEPT后查看
iptables -nL --line-numbers

#加载ip_conntrack_ftp
modprobe ip_conntrack_ftp

```

#### 3、ftp工作方式

>  
 FTP协议有两种工作方式：PORT方式和PASV方式，中文意思为主动式和被动式。 
 PORT（主动）方式的连接过程是：客户端向服务器的FTP端口（默认是21）发送连接请求，服务器接受连接，建立一条命令链路。当需要传送数据时，客户 端在命令链路上用PORT命令告诉服务器：“我打开了XXXX端口，你过来连接我”。于是服务器从20端口向客户端的XXXX端口发送连接请求，建立一条 数据链路来传送数据。 
 PASV（被动）方式的连接过程是：客户端向服务器的FTP端口（默认是21）发送连接请求，服务器接受连接，建立一条命令链路。当需要传送数据时，服务 器在命令链路上用PASV命令告诉客户端：“我打开了XXXX端口，你过来连接我”。于是客户端向服务器的XXXX端口发送连接请求，建立一条数据链路来 传送数据。 


#### 4、解决能下载不能上传的问题

在使用过程中发现不能上传，分析了一波，发现是文件的权限和所属主和属组的问题；

因为我用的是`uftp` 用户，所以他的主目录在 `/home/uftp` 目录下，当我`ls -l`查看时发现全是root，于是二话不说改权限；

```
chown -R uftp:uftp /home/uftp

```

<img src="https://img-blog.csdnimg.cn/cf76770bebb545978ff3704e007e09f2.png#pic_center" alt="在这里插入图片描述">

>  
 经过一番折腾后，可以正常用21端口连接，使用了。 


<img src="https://img-blog.csdnimg.cn/7e4050e4046145a1a7d4cb047004e966.png#pic_center" alt="在这里插入图片描述">
