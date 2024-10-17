
--- 
title:  linux部署ftp服务器 
tags: []
categories: [] 

---
## linux部署ftp服务器

由于工作需要，这边搭建一个简易的ftp文件服务器。

### 1、查看是否安装有ftp相关的安装包

```
rpm -qa |grep vsftpd

```

看到我的系统中没有安装相关的包，所以先把安装包装上。

# yum -y install vsftpd //这里如果没有配置yum源，可以直接用rpm的方式安装也是一样的

```
yum install -y vsftpd

#查看一下是否安装成功
rpm -qa |grep 'vsftpd'

```

### 2、启动服务

```
#启动ftp命令
service vsftpd start
#停止ftp命令
service vsftpd stop
#重启ftp命
service vsftpd restart
#重载
service vsftpd reload

```

### 3、vsftpd的配置

ftp的配置文件主要有三个，位于/etc/vsftpd/目录下，分别是：

```
ftpusers //用来指定哪些用户不能访问ftp服务器

user_list //这个文件中的用户是否可以登录到服务器，取决于vsftpd.conf文件中的userlist_enable和userlist_deny这两个选项。

vsftpd.conf //ftp服务器的主配置文件

```

### 4、匿名用户访问

```
#设置匿名用户访问
vi /etc/vsftpd/vsftp.conf
anon_upload_enable=YES
anon_mkdir_write_enable=YES
#一般默认已经有了的，将前面的'#'去掉就行了

```

### 5、非匿名用户的访问

```
vi /etc/vsftpd/vsftp.conf
#先将匿名用户访问关掉： 
anon_upload_enable=NO

#在配置文件末尾添加：
userlist_enable=YES
userlist_file=/etc/vsftpd/vsftpd.user_list
userlist_deny=NO

#创建用户
useradd ftp1
passwd ftp1

#将用户ftp1放入/etc/vsftpd/vsftpd.user_list文件中。
vi /etc/vsftpd/vsftpd.user_list
ftp1

#重启服务
service vsftpd reload

```

使用ftp1用户，可以登录到ftp服务器。
