
--- 
title:  dblink+trigger实现两个Oracle数据库中两个表的数据同步 
tags: []
categories: [] 

---
本文演示当 database1 的 test 表中新增数据时，将新增的数据同步到 database2 的 test 表中，两个表的表结构一致。

### 1. 创建 dblink

在 database1 中创建 dblink（uname、pwd、ip、port、sname 为 database2 中信息）

```
create database link dl_test 
connect to uname identified by "pwd"
using '(DESCRIPTION =
(ADDRESS_LIST =
(ADDRESS = (PROTOCOL = TCP)(HOST = ip)(PORT = port)))
(CONNECT_DATA = (SERVICE_NAME = sname)
)
)'

```

测试 dblink 是否联通：

```
select * from dual@dl_test;

```

对需要同步的表建立别名（下面 test 为 database2 中的表）：

```
create public synonym t for test@dl_test;

```

测试别名：

```
select * from t;

```

### 2. 创建触发器

在 database1 中创建触发器：

```
create or replace trigger tg_test 
before INSERT ON test FOR EACH ROW 
BEGIN
    IF inserting THEN
        insert into t(id, name, age) 
		values 
		(:NEW.id, :NEW.name, :NEW.age); 
    END IF;
END;

```

### 3. 同步测试

在 database1 中执行如下 sql：

```
insert into test(id, name, age) values('8a8a8cac7d7b76ff017d7e398a580kjx', '张三', '34');

```

执行完成后查看 database2 的 test 表中是否同步了新增的数据。
