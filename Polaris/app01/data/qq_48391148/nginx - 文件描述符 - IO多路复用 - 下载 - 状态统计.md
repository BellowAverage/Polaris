
--- 
title:  nginx - 文件描述符 - IO多路复用 - 下载 - 状态统计 
tags: []
categories: [] 

---
**目录**















































## 知识点1：文件描述符

### ulimit -a 命令  -a选项  列出所有可以使用资源的限制

>  
 **ulimit -a 命令可以列出用户可以使用资源的所有限制** 


```
[root@nginx-server conf]# ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 3795
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 2048
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 3795
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited

```

   **#############################################################################################** 

###  -n 选项 ：每个进程可以同时打开的最大文件数

```
[root@nginx-server conf]# ulimit -n
1024

```

#### 修改进程可以同时打开文件数

#### 临时修改：

```
[root@nginx-server conf]# ulimit -n 2048
[root@nginx-server conf]# ulimit -n
2048

```

#### 永久修改： 可以将 ulimit -n 2048 放到 /etc/rc.local文件里面

注：/etc/rc.local 必须有可执行权限

```
[root@nginx-server conf]# vim /etc/rc.local 
[root@nginx-server conf]# ll /etc/rc.local 
lrwxrwxrwx. 1 root root 13 7月  20 11:23 /etc/rc.local -&gt; rc.d/rc.local

```

#### 修改 limits.conf文件

注意：修改文件以后要重启系统才能生效

```
[root@nginx-server conf]# vim /etc/security/limits.conf 
* sort nofile 4096
* hard nofile 4096

```

**#############################################################################################** 

## 知识点2：IO多路复用

### 什么是IO多路复用？

>  
 **IO多路复用是一种同步IO模型，实现一个线程可以监视多个文件句柄；一旦某个文件句柄就绪，就能够通知应用程序进行相应的读写操作；没有文件句柄就绪时会阻塞应用程序，交出cpu。多路是指网络连接，复用指的是同一个线程** 


### IO多路复用解决了什么问题？

>  
 **Io多路复用解决了大并发的问题 ** 


###  IO多路复用的三种实现方式

#### select

>  
 **select也是linux的一个系统调用，即系统发出select系统调用，等待内核主动将可用的文件描述符信息发送给应用一端，fd未准备好，应用会阻塞住socket请求，当fd就绪后，select 会****遍历****维护的文件描述符发现可用的文件描述符。** 
 **因为select是采用遍历的方式来查找可用的fd资源，所以效率较低** 


#### epoll

>  
 **   epoll是linux下的一个系统调用，用来监听大量文件描述符并对其上的触发事件进行处理。它是select/poll的增强版本，也是linux下多路复用io最常用的接口。** 
 **用户进行io操作需要经过内核，而如果所请求的io目前不满足条件(如需要从标准输入读取数据，而用户还未输入)，这个时候内核就会让应用程序陷入等待，即阻塞状态。个人理解，io复用技术就是通过特定接口，将这种阻塞进行了转移，转嫁到了如select/poll/epoll之类多系统调用上，并且支持多个文件描述符多监测，即多路复用。这样epoll便可以替应用程序同时监听多个文件描述符，一旦有触发发生，内核就会通知应用程序进行处理。** 


**优点：**

>  
 **1.每当fd就绪，系统采用回调函数将fd放入就绪列表，效率非常高。 2.最大连接数没有限制** 


**#############################################################################################**

## 知识点3：隐藏nginx版本

### 哪些地方可能会暴露我们NGINX服务的版本号？ 1、404页面未找到的时候

<img alt="" height="309" src="https://img-blog.csdnimg.cn/e0c13ddc99ba4a8892c7cbaa4bda1608.png" width="1200">

####  2、成功访问时候响应报文respon  头部字段

<img alt="" height="745" src="https://img-blog.csdnimg.cn/c43616401f9b433dab158ab89f8aa56d.png" width="1200">

**#############################################################################################** 

###  怎么隐藏版本号？

#### 查看官方文档描述：

<img alt="" height="222" src="https://img-blog.csdnimg.cn/21df9bfe8e1f4ae691cabc3f4c88078e.png" width="1133">

>  
 ** 启用或禁用在错误页面和“服务器”响应头字段中发出 nginx 版本。** 
 **可以在 http块，或者server块 或者location块里面加入 server_tokens off  来隐藏版本号** 
 **在http块里面添加会影响所有虚拟主机的，在server块里面只会影响一个虚拟主机** 


 **#############################################################################################**

####  在配置文件里面添加 server_tokens off来隐藏版本号

<img alt="" height="286" src="https://img-blog.csdnimg.cn/a3e55efef9134c8b80ddb2c760c59d76.png" width="1012">

####  修改配置文件以后刷新nginx服务

可以看到，成功隐藏nginx版本号

<img alt="" height="823" src="https://img-blog.csdnimg.cn/c97002f27fbc4292911ac44a078af192.png" width="1200">

 

  **#############################################################################################**

## 知识点4：利用nginx做网站提供下载功能

**官方文档关于 authindex的说明**

<img alt="" height="187" src="https://img-blog.csdnimg.cn/cac656fa39ac453183feed1001e1da88.png" width="1126">

>  
 ** 启用或者禁止目录列表输出** 


 <img alt="" height="536" src="https://img-blog.csdnimg.cn/654dc8862a094227889ca8e7fa07bed4.png" width="996">

>  
 ** 在/html/liming/目录下面新建一个目录download里面存放提供用户下载的文件** 


```
[root@nginx-server html]# cd liming/
[root@nginx-server liming]# ls
download
[root@nginx-server liming]# ls download/
file  hosts  index.html.bak

```

>  
 ** 修改配置文件以后记得刷新nginx服务，刷新服务以后就可以进行下载文件操作了。** 
 **点击文件就能下载。** 


<img alt="" height="402" src="https://img-blog.csdnimg.cn/c7f89261addb410d9773e09deb652d59.png" width="1200">

   **#############################################################################################**

## 知识点5：状态统计

示例：在虚拟主机wang.com里面添加状态统计

<img alt="" height="269" src="https://img-blog.csdnimg.cn/e808459a8257479299d174d51e905ded.png" width="860">

<img alt="" height="322" src="https://img-blog.csdnimg.cn/a8eb8121abe54c03828d6e9e0d355a53.png" width="1031">

 

参考




