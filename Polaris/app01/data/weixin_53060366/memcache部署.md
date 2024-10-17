
--- 
title:  memcache部署 
tags: []
categories: [] 

---
## memcached部署



#### 文章目录
- - <ul><li>- <ul><li><ul><li>- - 


### 1、简介
- Memcached是一个自由开源的，高性能，分布式内存对象缓存系统。- Memcached是一种基于内存的key-value存储，用来存储小块的任意数据（字符串、对象）。这些数据可以是数据库调用、API调用或者是页面渲染的结果。- Memcached简洁而强大。它的简洁设计便于快速开发，减轻开发难度，解决了大数据量缓存的很多问题。它的API兼容大部分流行的开发语言。
memcache使用的母目的：通过缓存数据库查询结果，减少数据库访问次数，以提高动态Web应用的速度、提高可扩展性。

##### 特点：

memcached作为高速运行的分布式缓存服务器，具有以下的特点。
- 协议简单- 基于libevent的事件处理- 内置内存存储方式- memcached不互相通信的分布式
<img src="https://img-blog.csdnimg.cn/745eb3310b4f4ed1a66fc8a4bbb15e08.png#pic_center" alt="在这里插入图片描述">

### 2、memcached部署

#### yum安装

Memcached 支持许多平台：Linux、FreeBSD、Solaris、Mac OS，也可以安装在Windows上。

Linux系统安装memcached，首先要先安装libevent库。

```
#自动下载安装
yum install libevent libevent-devel
#yum安装
yum install memcached
#安装完后，可以使用whereis 查看命令路径：
whereis memcached

```

#### 源码编译安装

从其官方网站（http://memcached.org）下载memcached最新版本。

```
wget http://memcached.org/latest                    #下载最新版本

tar -zxvf memcached-1.x.x.tar.gz                    #解压源码

cd memcached-1.x.x                                  #进入目录

./configure --prefix=/usr/local/memcached           #配置

make &amp;&amp; make install                                   #编译安装

#启动memcached
/usr/local/memcached/bin/memcached -p 11211 -m 64m -d

```

**启动选项：**
- -d 是启动一个守护进程；- -m 是分配给Memcache使用的内存数量，单位是MB；- -u 是运行Memcache的用户；- -l 是监听的服务器IP地址，可以有多个地址；- -p 是设置Memcache监听的端口，，最好是1024以上的端口；- -c 是最大运行的并发连接数，默认是1024；- -P 是设置保存Memcache的pid文件。
### 3、memcached使用

Memcached **set** 命令用于将 **value(数据值)** 存储在指定的 **key(键)** 中。

如果set的key已经存在，该命令可以更新该key所对应的原来的数据，也就是实现更新的作用。

```
#语法
set key flags exptime bytes
value 

```
- **key：**键的名字- **flags**：类似于ID- **exptime**：在缓存中保存键值对的时间长度（以秒为单位，0 表示永远）- **bytes**：在缓存中存储的字节数- **value**：存储的值（始终位于第二行）
```
#举例
set runoob 0 900 9
memcached
STORED    #保存成功后输出，ERROR在保存失败后输出

get runoob
VALUE runoob 0 9
memcached
END

```

Memcached **replace** 命令用于替换已存在的 **key(键)** 的 **value(数据值)**。

如果 key 不存在，则替换失败，并且您将获得响应 **NOT_STORED**。

```
add mykey 0 900 10
data_value
STORED

get mykey
VALUE mykey 0 10
data_value
END

replace mykey 0 900 16
some_other_value

get mykey
VALUE mykey 0 16
some_other_value
END

```

Memcached **append** 命令用于向已存在 **key(键)** 的 **value(数据值)** 后面追加数据 。

```
set runoob 0 900 9
memcached
STORED

get runoob
VALUE runoob 0 9
memcached
END

append runoob 0 900 5
redis
STORED

get runoob
VALUE runoob 0 14
memcachedredis
END

```

Memcached **prepend** 命令用于向已存在 **key(键)** 的 **value(数据值)** 前面追加数据 。

```
set runoob 0 900 9
memcached
STORED

get runoob
VALUE runoob 0 9
memcached
END

prepend runoob 0 900 5
redis
STORED

get runoob
VALUE runoob 0 14
redismemcached
END

```

**delete** 命令用于删除已存在的 key(键)。

```
delete key

```
