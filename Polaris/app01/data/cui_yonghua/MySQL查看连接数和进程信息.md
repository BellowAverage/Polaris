
--- 
title:  MySQL查看连接数和进程信息 
tags: []
categories: [] 

---
1、查看连接信息

```
 myusql &gt; show status like '%connect%';
Aborted_connects     尝试连接到MySQL服务器失败的次数，
Threads_connected    当前打开的连接的数量
Connections		     表示MySQL从启动至今，成功建立连接的连接数，这个值是不断累加的。
max_connect_errors   允许单用户连接错误最大值，超过后在不刷新状态的情况下，禁止该用户新连接
max_connections      实例最大连接数限制
max_user_connections 但用户连接最大限制，默认0表示无限制
connect_timeout     用户连接超时限制，超过10秒，如果依旧无法连接到mysql，则终止连接

```

2、连接线程参数(thread variabls and status)

```
mysql&gt;  show variables like 'thread%'; 
thread_cache_size    设置连接线程缓存的数目。这个缓存相当于MySQL线程的缓存池
thread_handling      默认值是： one-thread-per-connection 表示为每个连接提供或者创建一个线程来处理请求，直至请求完毕，连接销毁或者存入缓存池。当值是no-threads 时，表示在始终只提供一个线程来处理连接，一般是单机做测试使用的。
thread_stack stack   是堆的意思
thread_concurrency   参数用于向操作系统建议期望的并发线程数，mysql 5.6后不再使用

```

3、查看正在执行的连接进程信息

```
mysql &gt; show processlist;   常用
关闭正在执行的链接进程
mysql&gt; kill ID值;

```

4、查看用户和当前实际登录的用户名

```
SELECT USER(),current_user();

```
