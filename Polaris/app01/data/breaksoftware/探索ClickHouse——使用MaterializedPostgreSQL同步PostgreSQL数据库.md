
--- 
title:  探索ClickHouse——使用MaterializedPostgreSQL同步PostgreSQL数据库 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- - - - - 


## 安装PostgreSQL

```
sudo apt install postgresql

```

### 修改配置

```
sudo vim /etc/postgresql/14/main/postgresql.conf 

```

解开并修改wal_level 的配置项

>  
 wal_level = logical 


### 重启服务

```
/etc/init.d/postgresql restart

```

>  
 Restarting postgresql (via systemctl): postgresql.service==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units === Authentication is required to restart ‘postgresql.service’. Multiple identities can be used for authentication: 
 - fangliang- , (kafka) 
 Choose identity to authenticate as (1-2): 1 Password: ==== AUTHENTICATION COMPLETE === . 


### 设置密码

切换用户

```
sudo su - postgres

```

使用下面命令进入PostgreSQL命令行交互页面

```
psql

```

输入下面命令设置密码为postgres_pwd

```
\password postgres

```

>  
 Enter new password for user “postgres”: Enter it again: 


## 创建数据库和表

使用下面命令创建数据库

```
CREATE DATABASE test_db;
\c test_db
CREATE TABLE accounts(user_id INT PRIMARY KEY, username VARCHAR(50) UNIQUE NOT NULL, password VARCHAR(50) NOT NULL, email VARCHAR(255) UNIQUE NOT NULL);

```

## 数据同步

开启一个新的窗口，使用下面指令进入交互页面

```
clickhouse-client

```

### 创建表

```
CREATE TABLE postgresql_replica(user_id UInt64, username String, password String, email String) ENGINE = MaterializedPostgreSQL('127.0.0.1:5432', 'test_db', 'accounts', 'postgres', 'postgres_pwd') PRIMARY KEY user_id;

```

>  
 CREATE TABLE postgresql_replica ( `user_id` UInt64, `username` String, `password` String, `email` String ) ENGINE = MaterializedPostgreSQL(‘127.0.0.1:5432’, ‘test_db’, ‘accounts’, ‘postgres’, ‘postgres_pwd’) PRIMARY KEY user_id Query id: 16f796bc-e979-47b4-8f1c-33471cfd7b12 0 rows in set. Elapsed: 0.013 sec. Received exception from server (version 23.7.5): Code: 1001. DB::Exception: Received from localhost:9000. DB::Exception: pqxx::sql_error: ERROR: logical decoding requires wal_level &gt;= logical . (STD_EXCEPTION) 


### 数据库写入数据

在psql的交互页面输入

```
INSERT INTO accounts(user_id, username, password, email) VALUES(0, 'fangliang', 'pwd', 'fangliang@123.com');

```

检查数据

```
select * from accounts;

```

>  
 user_id | username | password | email ---------±----------±---------±------------------ 0 | fangliang | pwd | fangliang@123.com (1 row) 


### ClickHouse同步数据

在clickhouse-client交互页面输入

```
select * from postgresql_replica;

```

>  
 SELECT * FROM postgresql_replica Query id: eef3fc8e-82ce-4e69-bf0b-0c2afe047daf ┌─user_id─┬─username──┬─password─┬─email─────────────┐ │ 0 │ fangliang │ pwd │ fangliang@123.com │ └─────────┴───────────┴──────────┴───────────────────┘ 1 row in set. Elapsed: 0.012 sec. 


## 参考资料
- 