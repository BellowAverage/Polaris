
--- 
title:  mysql windows安装版 报错Can‘t create test file 
tags: []
categories: [] 

---
问题描述：
- 使用的windows安装版mysql- mysql8- 第一次连接成功，但是第二次无法正常启动
故障排查：进入mysql安装目录，执行MySQL Server 8.0\bin\mysqld.exe启动服务。 启动服务失败，报错：

```
2023-01-12T03:29:53.567436Z 0 [Warning] [MY-010091] [Server] Can't create test file D:\usr\MySQL\MySQL Server 8.0\data\mysqld_tmp_file_case_insensitive_test.lower-test

```

然后在对应路径新建data文件夹。服务正常启动。

    原因描述：windows版本没有新建data文件夹，然后第二次启动的时候试图写入dump文件（因为第一次启动的时候被杀掉，肯定有dump文件） dump文件和日志无法正常写入导致服务挂掉。    
