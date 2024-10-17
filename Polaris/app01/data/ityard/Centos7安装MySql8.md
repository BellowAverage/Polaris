
--- 
title:  Centos7安装MySql8 
tags: []
categories: [] 

---
### 1. 卸载

卸载系统默认mariadb。

查看版本：`rpm -qa|grep mariadb`

卸载：`rpm -e --nodeps 文件名`

检查是否卸载干净：`rpm -qa|grep mariadb`

### 2. 下载配置

直接到官网下载，官网地址：`https://dev.mysql.com/downloads/mysql/`。

<img src="https://img-blog.csdnimg.cn/23e0e00663cc4c889f587f8042e52ff5.png" alt=""> 解压：

```
.tar.gz后缀：tar -zxvf 文件名
.tar.xz后缀：tar -Jxvf 文件名

```

重命名：

```
# 创建一个用户组：mysql
groupadd mysql
# 创建一个系统用户：mysql，指定用户组为mysql
useradd -r -g mysql mysql

```

授权：

```
# chown：改变文件(目录)的所有组和所有人(全能改变)
# chgrp: 只能改变文件(目录)的所有组
# chmod: 字符方式修改文件权限(如何修改权限)
chown -R mysql /usr/local/mysql/data/
chgrp -R mysql /usr/local/mysql/data/

```

创建my.cnf：`touch /etc/my.cnf`，添加如下配置：

```
[mysqld]
basedir = /usr/local/mysql/mysql8
datadir = /usr/local/mysql/data
port = 3306
socket = /var/lib/mysql/mysql.sock
pid-file = /home/mysql/mysql.pid

max_connections = 10240
wait_timeout=7200
interactive_timeout=7200
read_buffer_size = 2M
character_set_server=utf8
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
lower_case_table_names = 1

[client]
default-character-set=utf8

```

在tomcat的bin目录下执行：

```
./mysqld --user=mysql --basedir=/usr/local/mysql/mysql8 --datadir=/usr/local/mysql/data/ --pid-file=/home/mysql/mysql.pid --initialize

```

进行初始化。如需重新初始化删除data文件夹：`rm -rf /usr/local/mysql/data`

```
[Note] A temporarypassword is generated for root@localhost:xxmjT,#x_5sW

```

记住root的初始化密码：xxmjT,#x_5sW。

设置mysql开机自启动：

```
cp /usr/local/mysql8/support-files/mysql.server /etc/init.d/mysqld

chmod 755 /etc/init.d/mysqld     # 增加执行权限
chkconfig --add mysqld           # 如果没有就添加mysqld
chkconfig --list mysqld          # 检查自启动项列表中没有mysqld
chkconfig mysqld on              # 用这个命令设置开机启动

```

管理MySql命令：`service mysqld xxx`

问题：`error: 'Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)' Check that mysqld is running and that the socket: '/tmp/mysql.sock' exists!`，建立软链接：`ln -s /var/lib/mysql/mysql.sock /tmp`。

修改初始化密码：

```
./mysqladmin -uroot -p password
Enter password:   //输入初始化的密码
New password:    //重新输入新密码
Confirm new password: //重新输入新密码

```

登录mysql：`mysql -u root -p`

开启远程访问：

```
mysql&gt; use mysql; 
mysql&gt; update user set host = '%' where user = 'root'; 
mysql&gt; select host, user from user; 
mysql&gt; flush privileges;

```
