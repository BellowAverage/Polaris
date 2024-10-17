
--- 
title:  一、mysql的安装部署 
tags: []
categories: [] 

---
**目录**





















## 一、mysql的安装部署

### 1.mysql的版本
<li> 商业版 
  <ul>-  标准，企业，集群 <li> 社区版 
  <ul>-  开源免费。 -  老，稳定，很多公司都在使用。 
**############################################# **

### 2.下载mysql 5.7.34

1.进入mysql官网：





**点击downloads**

<img alt="" height="284" src="https://img-blog.csdnimg.cn/417bda776dbc4ada8f1749ad067689cb.png" width="794">

**点击社区版下载**

<img alt="" height="384" src="https://img-blog.csdnimg.cn/a51c22ef02f64502a7aa49a795b862e0.png" width="789">

 <img alt="" height="397" src="https://img-blog.csdnimg.cn/918e4980b6e745e794751cb9254658d2.png" width="772">

 <img alt="" height="222" src="https://img-blog.csdnimg.cn/85b91b4337e34af58f65a009c9f58ae2.png" width="722">

 <img alt="" height="296" src="https://img-blog.csdnimg.cn/01dc4f1d3c2a4bb49df4114c110b17fb.png" width="778">

** 下载好了以后使用xftp传到linux系统里面**

<img alt="" height="323" src="https://img-blog.csdnimg.cn/dbd2ad4ad0de4dc3ad0a631f1f3290db.png" width="1200">

 **############################################# **

### 3.一键安装脚本

一键安装脚本如下：

```
[root@localhost ~]# cat onekey_install_mysql_binary_v3.sh 
#!/bin/bash

#解决软件的依赖关系
yum  install cmake ncurses-devel gcc  gcc-c++  vim  lsof bzip2 openssl-devel ncurses-compat-libs -y

#解压mysql二进制安装包
tar  xf  mysql-5.7.34-linux-glibc2.12-x86_64.tar.gz

#移动mysql解压后的文件到/usr/local下改名叫mysql
mv mysql-5.7.34-linux-glibc2.12-x86_64 /usr/local/mysql

#新建组和用户 mysql
groupadd mysql
#mysql这个用户的shell 是/bin/false 属于mysql组 
useradd -r -g mysql -s /bin/false mysql

#关闭firewalld防火墙服务，并且设置开机不要启动
service firewalld stop
systemctl  disable  firewalld

#临时关闭selinux
setenforce 0
#永久关闭selinux
sed -i '/^SELINUX=/ s/enforcing/disabled/'  /etc/selinux/config

#新建存放数据的目录
mkdir  /data/mysql -p
#修改/data/mysql目录的权限归mysql用户和mysql组所有，这样mysql用户可以对这个文件夹进行读写了
chown mysql:mysql /data/mysql/
#只是允许mysql这个用户和mysql组可以访问，其他人都不能访问
chmod 750 /data/mysql/

#进入/usr/local/mysql/bin目录
cd /usr/local/mysql/bin/

#初始化mysql
./mysqld  --initialize --user=mysql --basedir=/usr/local/mysql/  --datadir=/data/mysql  &amp;&gt;passwd.txt

#让mysql支持ssl方式登录的设置
./mysql_ssl_rsa_setup --datadir=/data/mysql/

#获得临时密码
tem_passwd=$(cat passwd.txt |grep "temporary"|awk '{print $NF}')
  #$NF表示最后一个字段
  # abc=$(命令)  优先执行命令，然后将结果赋值给abc 

# 修改PATH变量，加入mysql bin目录的路径
#临时修改PATH变量的值
export PATH=/usr/local/mysql/bin/:$PATH
#重新启动linux系统后也生效，永久修改
echo  'PATH=/usr/local/mysql/bin:$PATH' &gt;&gt;/root/.bashrc

#复制support-files里的mysql.server文件到/etc/init.d/目录下叫mysqld
cp  ../support-files/mysql.server   /etc/init.d/mysqld

#修改/etc/init.d/mysqld脚本文件里的datadir目录的值
sed  -i '70c  datadir=/data/mysql'  /etc/init.d/mysqld

#生成/etc/my.cnf配置文件
cat  &gt;/etc/my.cnf  &lt;&lt;EOF
[mysqld_safe]

[client]
socket=/data/mysql/mysql.sock

[mysqld]
socket=/data/mysql/mysql.sock
port = 3306
open_files_limit = 8192
innodb_buffer_pool_size = 512M
character-set-server=utf8

[mysql]
auto-rehash
prompt=\\u@\\d \\R:\\m  mysql&gt;
EOF

#修改内核的open file的数量
ulimit -n 1000000
#设置开机启动的时候也配置生效
echo "ulimit -n 1000000" &gt;&gt;/etc/rc.local
chmod +x /etc/rc.d/rc.local


#启动mysqld进程
service mysqld start

#将mysqld添加到linux系统里服务管理名单里
/sbin/chkconfig --add mysqld
#设置mysqld服务开机启动
/sbin/chkconfig mysqld on

#初次修改密码需要使用--connect-expired-password 选项
#-e 后面接的表示是在mysql里需要执行命令  execute 执行
#set password='Sanchuang123#';  修改root用户的密码为Sanchuang123#
mysql -uroot -p$tem_passwd --connect-expired-password   -e  "set password='Sanchuang123#';"


#检验上一步修改密码是否成功，如果有输出能看到mysql里的数据库，说明成功。
mysql -uroot -p'Sanchuang123#'  -e "show databases;"

```

**############################################# ** 

### 4.如何判断MYSQL服务是否运行？

#### 01.看端口

```
[root@localhost ~]# lsof -i:3306
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
mysqld  1725 mysql   20u  IPv6  23706      0t0  TCP *:mysql (LISTEN)

```

```
[root@localhost ~]# netstat -anplut|grep mysqld
tcp6       0      0 :::3306                 :::*                    LISTEN      1725/mysqld       
```

```
[root@localhost ~]# ss -anplut|grep mysqld
tcp    LISTEN     0      80     [::]:3306               [::]:*                   users:(("mysqld",pid=1725,fd=20))

```

**############################################# ** 

#### 02.看进程

```
[root@localhost ~]# ps aux|grep mysqld
root       1571  0.0  0.1  11824  1608 pts/0    S    21:50   0:00 /bin/sh /usr/local/mysql/bin/mysqld_safe --datadir=/data/mysql --pid-file=/data/mysql/localhost.localdomain.pid
mysql      1725  0.0 19.8 1544156 197744 pts/0  Sl   21:50   0:01 /usr/local/mysql/bin/mysqld --basedir=/usr/local/mysql --datadir=/data/mysql --plugin-dir=/usr/local/mysql/lib/plugin --user=mysql --log-error=localhost.localdomain.err --open-files-limit=8192 --pid-file=/data/mysql/localhost.localdomain.pid --socket=/data/mysql/mysql.sock --port=3306
root       1938  0.0  0.0 112824   988 pts/0    R+   22:10   0:00 grep --color=auto mysqld

```

**############################################# ** 

#### 03.登录

```
[root@localhost ~]# mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.7.34 MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

root@(none) 22:12  mysql&gt;show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

root@(none) 22:12  mysql&gt;

```

**############################################# ** 

### 5.卸载mysql脚本

```
[root@localhost ~]# cat uninstall_binary_mysql.sh 
#!/bin/bash

# 停止mysqld服务
service mysqld stop
# 删除用户
userdel -r mysql

# 删除数据目录和base目录
rm -rf /usr/local/mysql
rm -rf /data/
rm -rf /etc/init.d/mysqld

```


