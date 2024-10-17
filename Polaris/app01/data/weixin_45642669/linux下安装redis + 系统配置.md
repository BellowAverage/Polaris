
--- 
title:  linux下安装redis + 系统配置 
tags: []
categories: [] 

---
今天刚配置的，记录一下。

### 安装系统依赖

###### 系统有无GCC

redis是通过c++进行编译的，所以

查询一下电脑是否有GCC-C++

```
yum list installed|grep gcc

```

如果提示是：

```
gcc.x86_64                       4.8.5-44.el7                          @os
gcc-c++.x86_64                   4.8.5-44.el7                          @os
gcc-gfortran.x86_64              4.8.5-44.el7                          @os
libgcc.x86_64                    4.8.5-44.el7                          @os


```

那么不需要安装

或者，直接：

```
gcc -v

```

如果提示：

```
Using built-in specs.
COLLECT_GCC=gcc


```

那么有gcc。

需要GCC是比较新的版本，不然可能不兼容。

###### 安装GCC

需要安装jcc 命令是：

```
yum install gcc-c++

```

如果安装了，会提示：

```
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
Package gcc-4.8.5-44.el7.x86_64 already installed and latest version
Nothing to do

```

### 从网络下载redis压缩包

###### 百度获取路径

百度GCC，第一或者第二就是官网，英文的。

然后点击官网的下载按钮，即可获取linux版本的下载地址。（就3个按钮，别告诉我哪个是下载啊！！！）

复制下载路径到剪贴板

###### wget获取下载文件

cd到需要下载的路径。

输入：

```
wget wget https://download.redis.io/releases/redis-6.2.6.tar.gz

```

即可下载文件。

执行:

```
ls -alh

```

即可查看到文件

```
dr-xr-xr-x. 19 root root 4.0K Feb 24 10:26 ..
drwxr-xr-x   8 root root 4.0K Jan  8  2021 knem-1.1.4.90mlnx1
drwxr-xr-x   8 root root 4.0K Jan  8  2021 mellanox
drwxrwxr-x   8 root root 4.0K Jan 31 18:50 redis-7.0-rc1

```

会提示文件大小。

### 解压redis并编译

解压文件：

```
tar -zxvf redis-7.0-rc1.tar.gz

```

即可出现redis文件夹

在reis文件夹下对代码进行编译

```
cd redis-7.0-rc1.tar.gz
make

```

即可make文件夹

### 修改conf文件并查看系统安装位置

###### 查询是否已经成功安装。

系统默认安装的位置在：

```
 cd /usr/local/bin

ls -alh

```

会有这么几个文件：

```
-rwxr-xr-x   1 root root 5.2M Feb 24 09:53 redis-cli
lrwxrwxrwx   1 root root   12 Feb 24 09:53 redis-sentinel -&gt; redis-server
-rwxr-xr-x   1 root root  11M Feb 24 09:53 redis-server


```

###### 备份后加入bin

备份一份系统配置文件redis.conf。（作为开发或者维护我认为这个是基础）

然后把redis.conf加入系统bin路径（就是默认path）

```
copy 你原来的conf文件位置  /usr/local/bin

```

###### 修改conf文件.

默认的是前台运行（也就是如果你前台退出了那么就退出）

```
vim redis.conf

```

大概在13%的位置有一个变量：

```
daemonize no

```

把no改成yes。

### 开启服务并测试

###### 以redis.conf作为参数打开redis

```
redis-server redis.conf


```

网上说有提示：成功。不过我的没有。

###### 测试连通性

```
redis cli -p 6379

```

这样就连上redis了

###### 执行测试

```
ping

```

返回：

```
PONG

```

成功连接。

记录一下。
