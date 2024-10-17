
--- 
title:  Redis 主从配置教程 linux 
tags: []
categories: [] 

---
        本文学习如何做Redis的主从配置，这里我们演示时我们并没有真实的Redis主服务器和从服务器，我们通过开通不同端口的Redis服务来代替一台服务器，所以下文中提到的端口对应的就是一台不同的服务器。

首先需要的前提条件：

1. 机器中已经安装好了redis

2. 需要开放端口 6379 6380 6381 ，6379是redis默认使用的端口 6380和6381是我们等会需要创建的2个从redis的端口

一、在redis的配置文件目录下创建3个文件，分别是

redis6379.conf

redis6380.conf

redis 6381.conf

<img alt="" height="124" src="https://img-blog.csdnimg.cn/744b06bb06c948138efa80ce83be82a7.png" width="706">

 二、在配置文件中写配置项

>  
 include /usr/local/redis/redis.conf  //引入redis的配置文件 pidfile /var/run/redis_6379.pid  // 配置 pid文件 port 6379 //配置端口号 dbfilename dump6379.rdb  //配置数据的持久化存储的文件名 # masterauth root（主服务器redis密码）//如果redis设有密码的话需要加上 


这里分别对 redis6379.conf 、redis6380.conf 、redis 6381.conf 这三个文件进行配置只需要把端口号对应修改就行。

三、启动这3台redis服务

>  
 redis-server redis6379.conf 
 redis-server redis6380.conf 
 redis-server redis6381.conf 


查看redis启动情况

<img alt="" height="128" src="https://img-blog.csdnimg.cn/92337a3f903243e28a22a3340b8ce8c6.png" width="693">

 目前这3台redis服务器已经启动了并且这三台服务器是独立的都是主服务器

查看redis服务器情况 可以进入到redis客户端使用 info replication命令查看

<img alt="" height="252" src="https://img-blog.csdnimg.cn/84b7fc9d8b3645259e96b446b50c7bd5.png" width="825">

 如图服务role为master代码是主服务器 slave 则为从服务器

三、配置从服务器

这里我们使用6379作为主服务器 6380和6381作为从服务器

进入到6380 和 6381服务器中配置输入以下命令

>  
 slaveof 127.0.0.1 6379 


<img alt="" height="398" src="https://img-blog.csdnimg.cn/a5f753112bb249c29b5ff1bfe4320ee5.png" width="716">

如图可以查看到6380服务器的 role为slave 并且master_port为6379

这时进入到6379服务器中查看<img alt="" height="252" src="https://img-blog.csdnimg.cn/4283d1f29e5b430097500b6b539310db.png" width="675">

 如图所示 6379 role: master   同时 connected_slaves有2台

四、验证主从数据同步

在主服务器(6379) 批量添加 arr1  arr2  arr3 的数据，同时在6380和6381中都可查看

<img alt="" height="411" src="https://img-blog.csdnimg.cn/02f5931ffe2d4446be4190a9fca52b0a.png" width="737">

6380和6381从服务器不允许写入，写数据时都出现以下提示

 READONLY You can't write against a read only replica<img alt="" height="113" src="https://img-blog.csdnimg.cn/d89c14fd6cb544c29af6839e07a59881.png" width="802">

 到此redis的主从配置就算完成了

以下有几个redis主从服务器的特性：

1. 当从服务挂机后再次重启该从服务器，该从服务器则变成主服务器需要重新使用slaveof命令绑定，绑定后主服务器的数据将会被同步到从服务器中。

2. 当主服务器挂机后从服务器不会变为主服务器，主服务器重新启动后原主从关系依然存在，且数据将从从服务器中同步到主服务器 ，除非在从服务器中执行 slaveof no one 将从服务器变成主服务器。

3. 从服务器依然可以绑定从服务器实现多层级的主从关系。




