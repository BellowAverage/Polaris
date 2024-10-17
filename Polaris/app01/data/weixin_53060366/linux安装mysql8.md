
--- 
title:  linux安装mysql8 
tags: []
categories: [] 

---
## linux部署mysql8

在服务器上部署mysql8版本。这里没用容器部署，是因为数据问题，以及服务的稳定性考虑，加上出故障可以有效的处理，我决定直接在系统上部署mysql服务。

### 1、下载mysql8版本

```
wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.26-linux-glibc2.12-x86_64.tar.xz

```

这里mysql的版本可以修改，`mysql-8.0.26`这里可以修改成自己想要的版本。

### 2、解压

```
xz -d mysql-8.0.26-linux-glibc2.12-x86_64.tar.xz
tar -xf mysql-8.0.26-linux-glibc2.12-x86_64.tar
mv mysql-8.0.26-linux-glibc2.12-x86_64 mysql
mv mysql /usr/local/mysql

```

### 3、创建mysql用户及用户组并修改权限

```
#创建mysql用户和组
useradd -s /sbin/nologin mysql
id mysql
uid=1002(mysql) gid=1002(mysql) 组=1002(mysql)

#修改文件的所有者和属组
cd /usr/local/mysql
mkdir data
chown -R mysql:mysql /usr/local/mysql/


```

### 4、编辑my.cnf 文件

```
vi /etc/my.cnf

[mysqld]
user=root
datadir=/usr/local/mysql/data
basedir=/usr/local/mysql
port=3306
max_connections=200
max_connect_errors=10
character-set-server=utf8
default-storage-engine=INNODB
default_authentication_plugin=mysql_native_password
lower_case_table_names=1
group_concat_max_len=102400
log-error=/usr/local/mysql/data/mysql.log
pid-file=/usr/local/mysql/data/mysql.pid
[mysql]
default-character-set=utf8
[client]
port=3306
default-character-set=utf8

```

<mark>****注意：** MySQL 8.0 版本的忽略大小写配置 `lower_case_table_names=1` 一定要在执行初始化前写在配置文件里，我之前遇到过这坑，当时像用 5.7 版本一样先初始化然后再改的配置文件，导致 mysql 无法启动，所以不同版本间的差异一定要注意！**</mark>

### 5、安装依赖及初始化

```
#初始化
[root@localhost ~]# cd /usr/local/mysql/bin/
[root@localhost bin]# ./mysqld  --initialize-insecure --defaults-file=/etc/my.cnf --basedir=/usr/local/mysql/ --datadir=/usr/local/mysql/data/ --user=mysql 

# 初始化报错，请执行以下命令，查看是否安装齐全
yum search libaio
yum install libaio
yum -y install numactl
yum install libnuma
yum install ld-linux.so.2
yum install libaio.so.1
yum install libnuma.so.1
yum install libstdc++.so.6
yum install libtinfo.so.5

```

>  
 - mysqld –initialize-insecure 自动生成无密码的root用户，- mysqld –initialize 自动生成带随机密码的root用户。 


>  
 **查看密码** 一般在datadir=/usr/local/mysql/data/路径下的err里面有记录，但我用的是无密码初始化所有没有密码直接登录. 
 有密码的话可以查看 `/usr/local/mysql/data/mysql.log` 日志文件。 
 `grep password /usr/local/mysql/data/mysql.log` 


### 6、添加mysqld服务到系统

```
cd /usr/local/mysql/
 cp -a ./support-files/mysql.server /etc/init.d/mysql
 
 #授权以及添加服务
 chmod +x /etc/init.d/mysql

chkconfig --add mysql

#将mysql添加到命令服务
ln -s /usr/local/mysql/bin/mysql /usr/bin

```

### 7、启动mysql服务

```
service mysql start
netstat -nap | grep 3306

#登录mysql
mysql -u root -p
Enter password:        //这里输入刚刚初始化操作时的初始密码,没有密码直接回车

alter user 'root'@'localhost' identified by '你的新密码';
flush privileges;


#设置允许远程登录,更改root连接权限
use mysql;

update user set host='%' where user = 'root';

flush privileges;

#exit; 退出mysql，现在就可以通过连接工具登录root账户进行远程连接了

```
