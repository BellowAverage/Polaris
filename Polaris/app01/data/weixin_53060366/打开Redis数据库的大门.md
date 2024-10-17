
--- 
title:  打开Redis数据库的大门 
tags: []
categories: [] 

---
## 打开Redis数据库的大门



#### 文章目录
- - <ul><li>- - <ul><li>- - - - 


### 1、Redis是什么？

**非关系型数据库：NoMsql**

主流的 NoSQL 数据库有Redis、 MongBD、 Hbase、 Memcached 等。

Redis译为“远程字典服务”，它是一款基于内存实现的键值型 NoSQL 数据库， 通常也被称为数据结构服务器，这是因为它可以存储多种数据类型，比如 string（字符串），hash（哈希散列），list（列表），set（集合）和 sorted set（有序集合）等。

Redis 遵守 BSD 协议，实现了免费开源，其最新版本是 6.20，常用版本包括 3.0 、4.0、5.0。

自 Redis 诞生以来，它以其超高的性能、完美的文档和简洁易懂的源码广受好评，国内外很多大型互联网公司都在使用 Redis，比如腾讯、阿里、Twitter、Github 等等。

<img src="https://img-blog.csdnimg.cn/6abc08263a5740dfbf890eaaf998859e.png#pic_center" alt="在这里插入图片描述">

### 2、Redis特点：
- Redis 不仅可以将数据完全保存在内存中，还可以通过磁盘实现数据的持久存储；- Redis 支持丰富的数据类型，包括 string、list、set、zset、hash 等多种数据类型，因此它也被称为“数据结构服务器”；- Redis 支持主从同步，即 master-slave 主从复制模式。数据可以从主服务器向任意数量的从服务器上同步，有效地保证数据的安全性；- Redis 支持多种编程语言，包括 C、C++、Python、Java、PHP、Ruby、Lua 等语言。
Redis 6.0版本前一直是单线程方式处理用户的请求；

#### 单线程为何如此快?
- 纯内存- 非阻塞- 避免线程切换和竞态消耗
Redis 没有提供新建数据库的操作，因为它自带了 16 （0—15）个数据库（默认使用 0 库）。在同一个库中，key 是唯一存在的、不允许重复的，它就像一把“密钥”，只能打开一把“锁”。键值存储的本质就是使用 key 来标识 value，当想要检索 value 时，必须使用与 value 相对应的 key 进行查找。

### 3、redis 对比 memcached

||memcached|redis
|------
|类型|key-value|key-value
|过期策略|支持|支持
|数据类型|单一数据类型|五大数据类型
|持久化|不支持|支持
|主从复制|不支持|支持
|虚拟内存|不支持|支持

### 4、redis 典型应用场景：
- Session 共享：常见于web集群中的Tomcat或者PHP中多web服务器session共享；- 缓存：数据查询、电商网站商品信息、新闻内容；- 计数器：访问排行榜、商品浏览数等和次数相关的数值统计场景；- 微博/微信社交场合：共同好友,粉丝数,关注,点赞评论等；- 消息队列：ELK的日志缓存、部分业务的订阅发布系统；- 地理位置: 基于GEO(地理信息定位),实现摇一摇,附近的人,外卖等功能；
### 5、Redis下载与安装：

注意：Windows 系统可以下载安装非官方的 Redis 版本，不过其使用性能远不如 Linux 系统。

这里我们在centos7上部署安装Redis 5.0.7版本：

rpm源码包下载地址：wget https://download.redis.io/releases/redis-5.0.7.tar.gz

```
#关闭防火墙和SELinux
systemctl stop firewalld
setenforce 0

#安装依赖包
yum install -y gcc gcc-c++ make

#下载软件包
cd /opt
wget https://download.redis.io/releases/redis-5.0.7.tar.gz
tar zxf redis-5.0.7.tar.gz 
cd redis-5.0.7/
make
make PREFIX=/usr/local/redis install

```

#由于Redis源码包中直接提供了Makefile 文件，所以在解压完软件包后，不用先执行./configure进行配置，可直接执行make与make install 命令进行安装。

<img src="https://img-blog.csdnimg.cn/065de142915246b5aced792acecafe40.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1b6e365d9a93416ca3ed97a0a88c9f98.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

```
cd /opt/redis-5.0.7/utils
./install_server.sh
#。。。。一直回车到这一步
#需要手动修改为可执行文件路径，注意要一次性正确输入
Please select the redis executable path [] /usr/local/redis/bin/redis-server

```

<img src="https://img-blog.csdnimg.cn/e798f9fb5607407ba822dae766c2aad2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

**把redis的可执行程序文件放入路径环境变量的目录中便于系统识别；**

```
ln -s /usr/local/redis/bin/* /usr/local/bin/

#当install_server.sh 脚本运行完毕，Redis 服务就已经启动，默认侦听端口为6379
ss -natp | grep 6379

```

<img src="https://img-blog.csdnimg.cn/41b8bdc4c270421d8289b36a9ebc40f1.png#pic_center" alt="在这里插入图片描述">

#### Redis服务控制：

```
/etc/init.d/redis_6379 stop                    #停止
/etc/init.d/redis_6379 start                   #启动
/etc/init.d/redis_6379 restart                 #重启
/etc/init.d/redis_6379 status                  #查看状态

```

```
#修改配置/etc/redis/6379.conf 参数
#70行，添加，监听的主机地址
vim /etc/redis/6379.conf
bind 127.0.0.1 192.168.111.100

#修改配置后要重启Redis
/etc/init.d/redis_6379 restart

```

<img src="https://img-blog.csdnimg.cn/a8c99124428047ce8bb21b73e04587b8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

#### Redis 命令工具：

|redis-server|用于启动 Redis的工具
|------
|redis-benchmark|用于检测Redis在本机的运行效率
|redis-check-aof|修复AoF持久化文件
|redis-check-rdb|修复RDB持久化文件
|redis-cli|Redis 命令行工具

#### redis-benchmark 测试工具

语法： redis-benchmark [选项] [选项值]

-h ：指定服务器主机名。 -P ：指定服务器端口。 -s ：指定服务器socket -c ：指定并发连接数。 -n ：指定请求数。 -d ：以字节的形式指定SET/GET值的数据大小。 -k ： 1=keep alive 0=reconnect 。 -r ： SET/GET/INCR 使用随机key， SADD 使用随机值。 -P ：通过管道传输请求。 -q ：强制退出redis。 仅显示query/sec值。 –csv ：以 CSV 格式输出。 -l ：生成循环，永久执行测试。 -t ：仅运行以逗号分隔的测试命令列表。， -I ：Idle 模式。仅打开 N 个 idle 连接并等待。

```
#向IP地址为192.168.111.100、 端口为6379的Redis 服务器发送100 个并发连接与100000 个请求测试性能
redis-benchmark -h 192.168.111.100 -P 6379 -c 100 -n 100000
#测试存取大小为100字节的数据包的性能
redis-benchmark -h 192.168.111.100 -P 6379 -q -d 100
#测试本机上 Redis 服务在进行 set 与lpush 操作时的性能
redis-benchmark -t set，lpush -n 100000 -q

```

#### redis-cli 命令行工具：

```
---redis-cli 命令行工具------
redis-cli  -h 192.168.111.100 -p 6379 -a 123123 -n 数据库序号（0-15）
-h:指定远程主机地址
-p：指定redis服务端口
-a：指定密码，未设置数据库密码可以省略-a选项
-n：指定数据库序号，默认是序号0，redis有16个库（0-15）
若不添加任何选型表示，则使用127.0.0.1:6379 连接本机上的redis 数据库

```

<img src="https://img-blog.csdnimg.cn/0284606ae747451b935567b8f4fa4440.png#pic_center" alt="在这里插入图片描述">
