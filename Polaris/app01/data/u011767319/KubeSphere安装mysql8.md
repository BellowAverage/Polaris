
--- 
title:  KubeSphere安装mysql8 
tags: []
categories: [] 

---
>  
 需要持久化储存数据的，建立有状态服务。 无状态服务是不会持久化的，重启就归零 KubeSphere 创建自建应用后，创建有状态服务，但是自己应用的有状态服务不能外放端口，需要在服务哪里删除pod，在创建负载指定相关的有状态服务，就可以外放端口了 


### 安装mysql8

<img src="https://img-blog.csdnimg.cn/c4297fbeb1344e5cb413b70c19779063.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7c643ff4d0694d6c82c94c4277250949.png" alt="在这里插入图片描述">

**添加初始化密码参数**

<img src="https://img-blog.csdnimg.cn/4a51032a9bc8423c8e305f73f2b179af.png" alt="在这里插入图片描述">

```
MYSQL_ROOT_PASSWORD

```

**数据库要指定持久化卷,不然重启pod数据就会归零** <img src="https://img-blog.csdnimg.cn/42ee817d738440e884746f3e513b196c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e146d55785764cd1870c373c97ba57d3.png" alt="在这里插入图片描述"> **数据库将的cnf配置映射出来** <img src="https://img-blog.csdnimg.cn/c88fe3e46ee340ad92db000a539f4e8d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b38f45f31f7d4b1c94670ce9b627b435.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e1ab87f011c24f62a5c87999bfda4da7.png" alt="在这里插入图片描述">

```
my.cnf

```

```
[mysqld]
port         = 3306
#basedir        = /var/lib/mysql
datadir        = /var/lib/mysql
pid-file    = /var/run/mysqld/mysqld.pid
socket        = /var/run/mysqld/mysqld.sock
#secure-file-priv= NULL
secure-file-priv= /var/lib/mysql-files
lower_case_table_names=1
character-set-server=utf8mb4

collation-server=utf8mb4_unicode_ci
max_connections=1500
max_connect_errors=100
default-storage-engine=INNODB
default_authentication_plugin=mysql_native_password
wait_timeout    = 1800
interactive_timeout = 1800
#lock_wait_timeout = 3600
#tmp_table_size = 64M
#max_heap_table_size = 64M
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
#log-error    = /var/log/mysql/error.log
# By default we only accept connections from localhost
#bind-address    = 127.0.0.1
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

[mysql]
default-character-set=utf8mb4

[client]
port=3306
default-character-set=utf8mb4

#!includedir /etc/mysql/conf.d/

```

<img src="https://img-blog.csdnimg.cn/866ca9e49ec247e480e70ca857172512.png" alt="在这里插入图片描述">

```
/var/lib/mysql

```

<img src="https://img-blog.csdnimg.cn/1bddc7ff97e14cc987f8c959299b1743.png" alt="在这里插入图片描述">

```
/etc/mysql/my.cnf

my.cnf

```

<img src="https://img-blog.csdnimg.cn/dc9d9c1d460b43bcbc1edd260ba552e2.png" alt="在这里插入图片描述"> **启动效果** <img src="https://img-blog.csdnimg.cn/0f19c5531e53402db7ebf47a40e86292.png" alt="在这里插入图片描述">
