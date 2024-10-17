
--- 
title:  gitlab访问报错： Whoops, GitLab is taking too much time to respond 
tags: []
categories: [] 

---
**目录**









#### 问题描述：

同学们玩gitlab的时候，通过网页访问报错：

Whoops, GitLab is taking too much time to respond

<img alt="" height="503" src="https://img-blog.csdnimg.cn/786b26d50f6b43e18dfd3685517bb798.png" width="571">

#### **解决方法**

等着就好了。。。。。

#### 问题原因

我们来分析一下原因：

1.gitlab是一个非常消耗内存的庞大项目，启动加载需要消耗很长的时间。

2.我们在gitlab报错的时候，可以动态观察一下服务器的内存占用情况。

```
[root@localhost ~]# free -mh
```

```
[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        2.9G        3.1G        143M        1.6G        4.3G
Swap:          2.0G          0B        2.0G

------------

[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        3.5G        2.5G        145M        1.7G        3.7G
Swap:          2.0G          0B        2.0G

-------------

[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        3.6G        2.4G        145M        1.7G        3.6G
Swap:          2.0G          0B        2.0G

-------------

[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        3.6G        2.3G        145M        1.7G        3.6G
Swap:          2.0G          0B        2.0G

-------------

[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        3.6G        2.3G        145M        1.7G        3.6G
Swap:          2.0G          0B        2.0G

-------------

[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        3.6G        2.3G        145M        1.7G        3.6G
Swap:          2.0G          0B        2.0G

-------------

[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        3.7G        2.3G        145M        1.7G        3.5G
Swap:          2.0G          0B        2.0G

-------------

[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        3.7G        2.3G        145M        1.7G        3.5G
Swap:          2.0G          0B        2.0G

-------------

[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        4.0G        2.0G        146M        1.7G        3.2G
Swap:          2.0G          0B        2.0G

-------------

[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        4.0G        2.0G        147M        1.7G        3.2G
Swap:          2.0G          0B        2.0G

-------------

[root@localhost ~]# free -mh
              total        used        free      shared  buff/cache   available
Mem:           7.6G        4.0G        2.0G        147M        1.7G        3.2G
Swap:          2.0G          0B        2.0G
```

在观察free内存的使用情况的时候，我们发现这段时间里，free的内存一直在减少，

说明，有程序在一直加载使用内存。

当然 这正是 gitlab的启动过程。

启动完成之后，free内存数量不再减少的时候。就说明gitlab启动完成了，我们这时访问，正常了

<img alt="" height="459" src="https://img-blog.csdnimg.cn/fb4dcd3c1da04e57bcee2a2eab0ae78b.png" width="758">

 
