
--- 
title:  mysql 无法killed的一个原因和解决 
tags: []
categories: [] 

---
## 问题描述

前天遇见了一个mysql无法killed的问题，记录下。

数据库数据执行了以后可能会锁表或者死锁，这时候，我一般是

```
show processlist;

```

以后

```
kill id;

```

可是今天失效了，killed不掉了。 提交killed以后这个id应该消失，而实际上一直被置为killed状态无法清除。

描述一下故障情况
1. select锁了无法执行（我知道select不加锁，可是也kill不掉）1. killed进程标为killed， 查了百度，提示说delete数据量过大会比较慢，需要等indo和undo处理到0为止。可是问题是：待处理数据数据半个小时没变了。 3.可以select，可是不能update、insert和delete。只要提交了就锁。 4.断开连接以后就再也连接不上了。
登陆服务器，发现磁盘没问题，登陆以后不卡，内存极低，无大量读写。 登陆服务器调用mysql，提示：too many connetions。 成功定位。连接数泄露

## 解决问题
- 重启可以释放连接数，增加最大连接数- 定位连接数泄露的原因  
重启了以后，查看连接数是否一直在增加。如果一直在增加则是连接数泄露。 简单来说：现在用框架已经封装了线程池，一般不会出现连接数泄露的问题；个人猜想是某个脚本小子try忘了写finally。 服务都是调用接口，不会申请连接数。  

操作：第一个是修改MySQL数据库的最大连接数，默认似乎是1000，可以改大（这个是正常业务），进行增大   最后定位是：脚本小子写了一个定时任务，try没写finally导致连接数泄露  

## 复盘

无法连接或者锁的莫名其妙（比如说不可能锁的数据被锁了，没有死锁条件的被锁了），这时候新开一个connect，查看是否报错too many connections。 最快的方案
- 重启mysql服务，直接kill -9或者stop.sh。MySQL不太可能kill以后起不来（如果是单体的话），这时候连接数就置为0了。- 是核实连接数被谁用了，是否还在随着时间增加。