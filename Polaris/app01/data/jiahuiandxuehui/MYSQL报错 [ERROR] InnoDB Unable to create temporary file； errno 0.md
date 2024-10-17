
--- 
title:  MYSQL报错 [ERROR] InnoDB: Unable to create temporary file； errno: 0 
tags: []
categories: [] 

---
## 起因

服务器的mysql不支持远程访问，在修改完相关配置后重启服务出错。

```
2023-12-03T10:12:23.895459Z 0 [Note] C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqld.exe (mysqld 5.7.22-log) starting as process 15684 ...
2023-12-03T10:12:23.908886Z 0 [Note] InnoDB: Mutexes and rw_locks use Windows interlocked functions
2023-12-03T10:12:23.909640Z 0 [Note] InnoDB: Uses event mutexes
2023-12-03T10:12:23.910103Z 0 [Note] InnoDB: _mm_lfence() and _mm_sfence() are used for memory barrier
2023-12-03T10:12:23.910802Z 0 [Note] InnoDB: Compressed tables use zlib 1.2.3
2023-12-03T10:12:23.911354Z 0 [Note] InnoDB: Adjusting innodb_buffer_pool_instances from 8 to 1 since innodb_buffer_pool_size is less than 1024 MiB
2023-12-03T10:12:23.912817Z 0 [Note] InnoDB: Number of pools: 1
2023-12-03T10:12:23.913570Z 0 [Note] InnoDB: Not using CPU crc32 instructions
2023-12-03T10:12:23.914403Z 0 [ERROR] InnoDB: Unable to create temporary file; errno: 0
2023-12-03T10:12:23.915132Z 0 [ERROR] InnoDB: Plugin initialization aborted with error Generic error
2023-12-03T10:12:23.915812Z 0 [ERROR] Plugin 'InnoDB' init function returned error.
2023-12-03T10:12:23.916388Z 0 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
2023-12-03T10:12:23.917012Z 0 [ERROR] Failed to initialize builtin plugins.
2023-12-03T10:12:23.917546Z 0 [ERROR] Aborting

```

## 解决历程
1. 修改过配置文件 我已经在my.ini里面配置了 tmpdir=C:/ProgramData/MySQL/MySQL Server 5.7/tmp1. 更改过相关文件权限：完全控制1. 检查过ibdata1文件
都试过了还是不行。

## 最终解决方法

保存数据库文件主要是data文件夹，卸载mysql服务，依然使用旧的my.ini重新初始化安装。

```

D:\Mysql\mysql-5.7.30-winx64\bin&gt;mysqld --initialize

D:\Mysql\mysql-5.7.30-winx64\bin&gt;mysqld --install
Service successfully installed.

```

用旧的data文件替换新的，这样数据也不丢失。问题也很快解决。 <img src="https://img-blog.csdnimg.cn/direct/2ad2f7b1efd84f4dba3677647dcb9b2f.png" alt="在这里插入图片描述">
