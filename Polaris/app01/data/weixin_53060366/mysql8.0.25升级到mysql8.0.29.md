
--- 
title:  mysql8.0.25升级到mysql8.0.29 
tags: []
categories: [] 

---
## mysql8.0.25升级到mysql8.0.29

最近，扫描出了数据库存在中、高危漏洞，于是迫切需要进行数据库升级。上网查了各种资料，说法很多，也到自己虚拟机上试了好多方法，终于倒腾出来，做下小总结记录一下。

### 1、备份原数据库

进入旧mysql的bin目录下，把所有数据都导出到/data/mysqlData/all.sql

```
./mysqldump -uroot -p123456 --all-databases &gt; /data/mysqlData/all.sql

```

### 2、安装新的数据库

先停掉旧的数据库服务：

```
systemctl mysql stop

```

```
#上传mysql-8.0.29-linux-glibc2.12-x86_64.tar.xz到指定目录，并解压
tar -xvf mysql-8.0.29-linux-glibc2.12-x86_64.tar.xz
mv mysql-8.0.29-linux-glibc2.12-x86_64 mysql

#修改原/etc/my.cnf文件，文件目录指向新版本mysql文件地址
[mysqld]
basedir = /usr/local/mysql
datadir = /usr/local/mysql/data
log_error = /usr/local/mysql/mysql-error.log
port = 3306
socket = /usr/local/mysql/mysql.sock
pid_file = /usr/local/mysql/mysqld.pid

character-set-server=utf8
lower_case_table_names=1
max_connections=1000
sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'
#skip-grant-tables

[mysql]
default-character-set=utf8

[client]
default-character-set=utf8
socket = /usr/local/mysql/mysql.sock


```

### 3、初始化数据库

进入新mysql的bin目录下，执行：

```
 ./mysqld --defaults-file=/etc/my.cnf --basedir=/usr/local/mysql/ --datadir=/usr/local/mysql/data/ --user=mysql --initialize


```

把mysql服务链接到/usr/bin目录下：

```
ln -s /usr/local/mysql/bin/mysql /usr/bin

```

查看初始密码，启动数据库：

```
cat /usr/local/mysql/mysql-error.log

#启动mysql
systemctl mysql start

#查看mysql版本
mysql -V

#修改初始密码
mysql -uroot -p'初始密码'

ALTER USER 'root'@'localhost' IDENTIFIED BY '新密码';
FLUSH PRIVILEGES;

#恢复备份文件
use mysql
source /data/mysqlData/all.sql #第一步备份文件的地址

```

到此，版本升级完成，登录到mysql，可以看到旧版本的数据
