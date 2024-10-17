
--- 
title:  windows安装mysql数据库 
tags: []
categories: [] 

---
## 下载mysql zip版本

https://dev.mysql.com/downloads/mysql/
- 最好要记录mysql的版本。从网络上下载mysql，下载以后解压
在解压路径配置my.ini,然后写入：

```
[mysqld]
# 设置3306端口
port=3306
# 设置mysql的安装目录 ,需要修改
basedir=E:\\mysql8
# 设置mysql数据库的数据的存放目录，如果不存在需要提前创建
datadir=E:\mysql\data
# 允许最大连接数
max_connections=200
# 允许连接失败的次数。
max_connect_errors=10
# 服务端使用的字符集默认为utf8
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
# 默认使用“mysql_native_password”插件认证
#mysql_native_password
default_authentication_plugin=mysql_native_password
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8
[client]
# 设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8

```

mysql8.0修改了mysql_native_password认证方式，这种方式可能会失效。

#### 注册环境变量

注册 {解压路径}\bin到环境变量。

cmd 执行（实时刷新path）

```
set Path = C
exit

```

测试一下Path

```
Path

```

发现已经写入Path

cmd执行

```
mysql

```

提示数据库没有初始化。

#### 初始化数据库

```
mysqld --initialize --console

```

会生成默认密码，记录一下。

##### 注册为服务

使用管理员权限执行

```
mysql --install

```

如果已经安装过mysql，会报错。需要

```
sc delete mysql

```

以后重新执行

#### 测试登陆

在cmd执行

```
mysql -	u root -p

```

登陆以后修改密码：

```
set password for username @localhost = password({password});

```

#### 允许远程登陆

```
use mysql;
select user,host from user;

```

查看权限。、

```
update user set host='%' where user='root';

```

即可赋权给root远程登陆的权限

## 使用msi安装

https://dev.mysql.com/downloads/mysql/

下载以后，直接下一步。 选择msi安装方式   配置一个账号密码
