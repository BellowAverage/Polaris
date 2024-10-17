
--- 
title:  linux上redis升级 
tags: []
categories: [] 

---
## linux上redis升级

>  
 redis版本升级。 


我原本的redis 版本是6.2.1，现在就对他做一下升级处理。

### 1、下载redis 源码包：

 根据下载地址选择自己要安装的redis 版本的源码包。这里我下载的是 redis-6.2.6.tar.gz。

这里你可以先下载到本地，在通过ftp 的方式上传到服务器，也可以直接 wget 下载。

```
#安装 wget
yum install -y wget

#下载 redis
wget http://download.redis.io/releases/redis-6.2.6.tar.gz

#解压源码包
tar -zxvf redis-6.2.6.tar.gz

#停止旧版的redis
ps -ef|grep redis
kill -9 进程id

```

### 2、备份数据：

在升级前，可以根据情况来决定是否需要备份数据和配置文件。
- 如果持久化用的是rdb，备份.rdb文件，默认叫 dump.rdb。- 如果持久化用的是aof，备份.aof文件，默认叫 appendonly.aof- 配置文件是 redis.conf文件。也可以备份下，这样可以省去修改配置文件。
在启动新版的redis 时，可以将数据文件放到启动目录下。不知道启动目录，可以 `redis-cli` 下输入：`config get dir` 查看。

redis.conf 只需要替换新版的redis.conf 即可。

### 3、编译安装：
- 在编译安装前，查看下gcc 的版本：
```
#查看gcc 版本
gcc -v
#如果是4.* 的就要升级，因为redis6.2 以上需要gcc 9.*的版本，不然make 编译redis时会报错。
#安装gcc
yum -y install gcc
#升级gcc
yum -y install centos-release-scl
yum -y install devtoolset-9-gcc devtoolset-9-gcc-c++ devtoolset-9-binutils

#切换到升级的gcc 版本
#临时)
scl enable devtoolset-9 bash
#永久)
echo "source /opt/rh/devtoolset-9/enable" &gt;&gt; /etc/profile

#查看版本是否切换成功：
gcc -v              #如果gcc版本为9.*以上则成功，4.*反之

```
- 进入新版的redis 目录编译安装
```
cd redis-6.2.6
#编译安装
make &amp;&amp; make install

#将旧版的配置文件和备份数据文件复制到新版redis 中
cp -p redis-6.2.1/redis.conf ./redis-6.2.6/
cp -p redis-6.2.1/dump.rdb ./redis-6.2.6/src/

```

>  
 因为这里是使用旧版的redis.conf ，所以可以不用配置redis.conf 文件的参数，如果没有使用旧版的话，可以配置以下参数： 
 - 注释 bind 127.0.01 允许外部连接- 修改protected-mode 为 no 关闭保护模式- 修改daemonize 为 yes 允许后台运行- port 端口，可以根据需求修改，比如修改成：16379- requirepass 可以设置密码，将注释去掉 
 <pre><code class="prism language-shell">#这个也可以在redis 中设置密码：
127.0.0.1:6379&gt; config set requirepass 123123
127.0.0.1:6379&gt; config get requirepass
</code></pre> 


### 4、启动新版redis

```
cd redis-6.2.6/src
./redis-server /root/redis-6.2.6/redis.conf
#查看redis 是否启动
ps -ef |grep redis

#查看redis 版本
#可以直接看
redis-cli -v

#也可以进redis 中查看
redis-cli -h localhost -p 16379 -a 123123
info
#这里连接时可以直接输入密码，也可以连接后输入密码
127.0.0.1:6379&gt; auth 123123
127.0.0.1:6379&gt; info

```

>  
 redis-cli -h 192.168.111.100 -p 6379 -a 123123 -n 数据库序号（0-15） -h:指定远程主机地址 -p：指定redis服务端口 -a：指定密码，未设置数据库密码可以省略-a选项 -n：指定数据库序号，默认是序号0，redis有16个库（0-15） 
 若不添加任何选型表示，则使用127.0.0.1:6379 连接本机上的redis 数据库 

