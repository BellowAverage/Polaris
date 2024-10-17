
--- 
title:  volatile 关键字的作用 
tags: []
categories: [] 

---
##### 1 简介

Java 语言提供了一种稍弱的同步机制，即 volatile 变量，用来确保将变量的更新操作通知到其他线程。volatile 变量具备两种特性：变量可见性、禁止重排序。

在访问 volatile 变量时不会执行加锁操作也就不会使执行线程阻塞，因此 volatile 变量是一种比 sychronized 关键字更轻量级的同步机制。

当对非 volatile 变量进行读写的时候，每个线程先从内存拷贝变量到 CPU 缓存中。如果计算机有多个 CPU，每个线程可能在不同的 CPU 上被处理，这意味着每个线程可以拷贝到不同的 CPU cache 中。而声明变量是 volatile 的， JVM 保证了每次读变量都从内存中读，跳过 CPU cache 这一步。

##### 2 应用场景

volatile 变量的单次读/写操作是可以保证原子性的，如 long 和 double 类型变量，但是并不能保证 i++这种操作的原子性，因为本质上 i++是读、写两次操作。同时满足如下两个条件可保证在并发环境中的线程安全。

1）对变量的写操作不依赖于当前值（比如 i++），或者说是单纯的变量赋值（ boolean flag = true）。

2）该变量没有包含在具有其他变量的不变式中， 也就是说，不同的 volatile 变量之间，不能互相依赖， 只有在状态真正独立于程序内其他内容时才能使用 volatile。

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
