
--- 
title:  叫你别随便重启Redis！！！怎么样,数据全丢了吧~~~ 
tags: []
categories: [] 

---
**目录**























### 事情是这样的...

**今天，跑的好好的程序突然挂球了，问了一下负责redis维护的同事。同事说，根据领导的要求，对Redis的备份模式进行了修改，开启了AOF（AppendOnlyFile）的增量备份模式。**

**我一听心里就慌了。。。**

**问他："你是不是改了配置文件？然后。。。重启了？！？！"**

**同事说：“是啊”**

<img alt="" height="280" src="https://img-blog.csdnimg.cn/20210403195615638.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="482">

**还说：“RDB模式默认开启的，全量备份一直开着，怕什么？”**

**我听他说完，心里一万只羊驼掠过。。。**

<img alt="" height="295" src="https://img-blog.csdnimg.cn/20210403171951730.png" width="289">

**emmm~~~~为什么重启一下会出这么大篓子**

<img alt="" height="183" src="https://img-blog.csdnimg.cn/20210402120458825.png" width="189">

**心里当时就很崩溃~~~~**

**但还是强忍着跟他说了一下 Redis数据本地化的两种模式**

<img alt="" height="287" src="https://img-blog.csdnimg.cn/20210403184548755.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="306">

### Redis持久化数据的两种模式

#### 一、RDB模式

1、Redis默认启用的本地化模式。

2、每隔一段时间全量备份；系统将导出的dump.rdb文件备份。

```
save 900 1   #900秒内 至少1个key 被更新 就全量备份RDB
save 300 10
save 60 10000
```

3、原理：redis会fork一个新的进程来进行rdb全量结构化。（redis本身读写是单进程的）

4、缺点：备份后和故障间 数据丢失；新fork的子进程会copy父进程里的内存数据进行备份，会造成内存瞬间翻倍。



#### 二、AOF模式

1、AppendOnlyFile的缩写，是一种增量备份模式，Redis默认不开启。

2、类似mysql数据库的binlog，记录所有的redis操作记录

```
appendonly yes #开启AOF
appendfilename "appendonly.aof" #设置备份文件名
appendfsync	everysec #每秒更新一次操作记录
```

3、Redis会在原有进程的基础上，重新fork一个子进程进行记录

4、日志形式记录写操作;以文件追加的方式记录（在同一个备份文件上追加操作记录）



#### 三、RDB和AOF之间的关系

**1、优先级AOF&gt;RDB **

**2、RDB和AOF之间是不会相互通信的**



#### 四、问题回顾分析

同事改完配置文件打开AOF

```
#开启AOF
appendonly yes
```

重启了redis--server

```
redis-server redis.conf
```

AOF在重启redis之后才开始生效。

重启之后，redis 首先加载AOF的备份文件（因为开了AOF开关），但是AOF是空的，所有Redis内存就被加载为空了。

这个时候，一旦触发或满足了RDB全量备份的条件，Redis会对整个内存数据库进行全量备份，并且覆盖掉原先的备份文件。

BUT 这个时候，Redis的内存是空的，完整RDB之后，就把空内存库全量备份 覆盖了原有的RDB备份文件。

所以，内存空了，AOF还啥都没有，之前的RDB备份文件也被覆盖了。。。

完美 平滑 不留痕迹的 技术手段删库

当时就想给这个大佬跪下了

<img alt="" height="219" src="https://img-blog.csdnimg.cn/2021040317431889.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="457">

emmm...总结一下，就是一波操作下来，重启之后的AOF占领了内存，内存又全量覆盖了之前重启之前全量备份的RDB，数据全没了。

最后，幸好redis的RDB的备份文件，每天都会备份一次，但是从上次备份到重启这段时间里的数据还是找不回来了。



**-----------------End Of The Story----------------**



### 那么该如何开启AOF增量备份模式呢？

### 解决方法:

**在线修改AOF开关**

不要随便重启Redis！！！因为重启就会涉及到Redis内存的重新加载。

#### 1、登录到redis

```
#链接到redis
[root@mail ~]# redis-cli -a 123456[你的密码] -p 6379
```

#### 2、在线修改AOF开关

```
#redis中查看AOF状态
127.0.0.1:7001&gt; config get appendonly
1) "appendonly"
2) "no"

#在线设置AOF开关为yes
127.0.0.1:7001&gt; config set appendonly yes
OK
127.0.0.1:7001&gt; 
```

#### 3、查看数据

```
#数据都在
127.0.0.1:7001&gt; keys *
1) "name"
2) "gender"
3) "age"
127.0.0.1:7001&gt; 
```

而且备份文件AOF和RDB也都正常持久化中

<img alt="" height="169" src="https://img-blog.csdnimg.cn/202104031835190.png" width="718">

###  推荐阅读

**优质资源**
- **Java实现照片GPS定位【完整脚本】**- - **Python实现照片GPS定位【完整脚本】**- - **女神忘记相册密码 python20行代码打开【完整脚本】**- - ****- 
**【Java资源下载】**
- 【JDK5】jdk1.5x64位 windows版.zip- - 【JDK6】jdk-6u45-windows-x64 jdk1.6 64位 Windows版- - 【JDK7】jdk-7u72-windows-i586-32位- - 【JDK8】jdk-8u131-linux-x64.tar.gz- - 【JDK8】jdk-8u131-linux-x64.tar.gz- 
**【python实战】**
- ****- ****- **...**- ****- ****- ****
**【pygame开发实战开发30例 完整源码】**
- 
**【pygame游戏开发专栏，获取完整源码+教程】**
- ****- ****- ****- ****- ** **- ****
#### CSDN官方学习推荐 ↓ ↓ ↓

为了帮助更多小白从零进阶 Java 工程师，从CSDN官方那边搞来了一套 《Java 工程师学习成长知识图谱》

尺寸 `870mm x 560mm`，知识汇总非常齐全，还可以折叠成一本书大小。

<img alt="" height="828" src="https://img-blog.csdnimg.cn/20210704222452239.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="475">
