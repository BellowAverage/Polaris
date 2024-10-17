
--- 
title:  在Linux操作系统里实现MySQL用户的密码破解 
tags: []
categories: [] 

---


#### 文章目录
- - - - <ul><li>- - <ul><li>- - - - - - - - 


## 在Linux操作系统里实现MySQL用户的密码破解

## 一、普通用户忘记密码

可直接登录超级用户root进行修改

```
root@(none) 09:34  mysql&gt;alter user 'sc'@'%' identified by '123456';
Query OK, 0 rows affected (0.00 sec)

```

## 二、超级用户root忘记密码

### 1.如果有另外一个管理员账户

（被授予权限的账户，例如 grant all on **.** to ‘sc’@’%’ identified by ‘123456’ ,则sc用户除了没有grant授权权限以外。具有其他的所有权限 ），可以使用这个管理员账户修改超级用户root的密码。

```
[root@scchen ~]# mysql -usc -p'12345678'  --》使用管理员账户登录
MySQL [(none)]&gt; alter user 'root'@'localhost' identified by 'Sanchuang123#';
Query OK, 0 rows affected (0.00 sec)

```

### 2.如果只有一个超级用户root，没有其他的管理员账户

#### 1.停止mysqld进程

`service mysqld stop`

#### 2.修改配置文件 /etc/my.cnf

在mysqld进程里添加语句

```
[mysqld]
skip-grant-tables   #跳过需要权限的表即跳过密码验证

```

#### 3.启动mysqld进程

`service mysqld restart`

#### 4.登录超级用户（不接密码）

`mysql -uroot -p` 如果此时修改密码会报错，因为没有加载表，修改密码本质上是修改mysql库里面的user表。

#### 5.刷新权限

`flush privileges；`（刷新权限加载数据库里面的表）

#### 6.修改密码

`alter user 'root'@‘localhost' identified by 'Sanchuang123#';` (mysql里完整的用户信息是 用户名@主机名)

#### 7.重新修改配置文件 /etc/my.cnf

```
[mysqld]
#skip-grant-tables 

```

#### 8.刷新服务

`service mysqld restart`

#### 9.验证密码是否修改成功

`mysql -uroot -p'Sanchuang123#'`

## 总结

以上简单介绍了在Linux操作系统里进行MySQL用户密码破解的几种情况。
