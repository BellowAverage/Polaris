
--- 
title:  Docker - docker的安装部署 - docker常用命令 - 底层隔离机制 
tags: []
categories: [] 

---
**目录**























































### 知识点1：虚拟化 virtualization ：

>  
 **虚拟化，是指通过虚拟化技术将一台计算机虚拟为多台逻辑计算机。在一台计算机上同时运行多个逻辑计算机，每个逻辑计算机可运行不同的操作系统，并且应用程序都可以在相互独立的空间内运行而互不影响，从而显著提高计算机的工作效率。** 


#### 容器软件、云原生：

>  
 **        vmware：workstation  入门级的产品** 
 **        docker：容器技术的经典代表** 
 **        k8s： containerd** 
 **        CNCF： 云原生基金会：k8s（kubernetes）** 
 **        docker 是容器运行时的软件 -- 容器软件** 
 **        k8s是管理容器运行时软件（docker，containerd，rkt等）集群的软件** 
 **        k8s建立在docker之上的软件** 
 **        docker和k8s都是使用go语言开发的** 
 **        只要是与k8s相关的技术都叫云原生相关的技术** 


**############################################################################# **

## 知识点2：docker安装

官方网站：

### 安装步骤：

####          1、如果之前安装过的话需要先将docker卸载

```
 yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```

**############################################################################# ** 

####         2、安装yum相关工具，下载docker-ce.repo文件

```
yum install -y yum-utils
```

```
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

>  
 **下载docker-re.repo文件会存放在/etc/yum.repos.d下面** 


```
[root@docker yum.repos.d]# ls
CentOS-Base.repo       CentOS-fasttrack.repo  CentOS-Vault.repo
CentOS-CR.repo         CentOS-Media.repo      CentOS-x86_64-kernel.repo
CentOS-Debuginfo.repo  CentOS-Sources.repo    docker-ce.repo

```

 **############################################################################# **

####         3、安装docker-ce 软件

>  
 **ce：container engine 容器引擎** 
 **docker是一个容器管理的软件** 
 **docker-ce是服务器端软件** 
 **docker-ce-cli是客户端软件** 
 **containerd.io是底层用来启动容器的** 
 **docker-compose-plugin 是compose插件，用来批量启动很多容器，在单台机器上面** 


```
yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y

```

**############################################################################# **

####         4、启动docker服务

```
[root@docker yum.repos.d]# systemctl start docker
[root@docker yum.repos.d]# ps aux | grep docker 
root      11373  1.2  6.0 1086656 60408 ?       Ssl  11:40   0:00 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
root      11507  0.0  0.0 112824   980 pts/0    R+   11:40   0:00 grep --color=auto docker
[root@docker yum.repos.d]# 

```

 **############################################################################# **

####         5、设置docker开机自启

```
[root@docker yum.repos.d]# systemctl enable docker
Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
[root@docker yum.repos.d]# 

```

**############################################################################# **

##  知识点3：docker常用命令

>  
 **docker启动的每一个容器背后就是一个linux进程** 


### docker --version：查看docker版本

```
[root@docker yum.repos.d]# docker --version
Docker version 20.10.17, build 100c701

```

```
[root@docker ~]# docker version
Client: Docker Engine - Community
 Version:           20.10.17
 API version:       1.41
 Go version:        go1.17.11
 Git commit:        100c701
 Built:             Mon Jun  6 23:05:12 2022
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.17
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.17.11
  Git commit:       a89b842
  Built:            Mon Jun  6 23:03:33 2022
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.7
  GitCommit:        0197261a30bf81f1ee8e6a4dd2dea0ef95d67ccb
 runc:
  Version:          1.1.3
  GitCommit:        v1.1.3-0-g6724737
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

```

### docker ps ：看有哪些docker容器在运行

```
[root@docker ~]# docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED       STATUS       PORTS                                   NAMES
fc652e8c734a   nginx     "/docker-entrypoint.…"   3 hours ago   Up 3 hours   0.0.0.0:8090-&gt;80/tcp, :::8090-&gt;80/tcp   sc-nginx

```

### docker images：查看有哪些docker镜像

>  
 **镜像里面包含了我们需要的软件的代码和基础环境 ** 


```
[root@docker ~]# docker images
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
nginx        latest    2b7d6430f78d   2 days ago   142MB

```

### docker pull nginx ：下载nginx的镜像

```
[root@docker yum.repos.d]# docker pull nginx

```

### docker run -d -p 8090:80 --name sc-nginx nginx ：启动docker容器

>  
 **docker run是启动容器的命令** 
 ** -d  在后台运行 daemon守护进程** 
 ** -p 8090:80 指定端口映射** 
 **--name sc-nginx  指定容器名字** 
 **nginx 是镜像的名字** 


#### 查看启动的容器进程

```
[root@docker yum.repos.d]# docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
fc652e8c734a   nginx     "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   0.0.0.0:8090-&gt;80/tcp, :::8090-&gt;80/tcp   sc-nginx
[root@docker yum.repos.d]# docker images
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
nginx        latest    2b7d6430f78d   2 days ago   142MB
[root@docker yum.repos.d]# 

```

#### 在客户机上面测试能否访问宿主机的8090端口

<img alt="" height="474" src="https://img-blog.csdnimg.cn/5c7a4dc71ae4475289e78e58b4b86ec3.png" width="1200">

### docker logs + 容器id ： 查看容器启动失败的日志信息 

### <img alt="" height="235" src="https://img-blog.csdnimg.cn/76853271ba9b4dbe89c55dbb22d13bff.png" width="1200"> docker rm + 容器名字 ： 删除启动失败的容器

>  
 **正在运行的容器不能直接删除，需要先将其停止。** 


<img alt="" height="227" src="https://img-blog.csdnimg.cn/3f2fcbc350a144a086c1c32740e20519.png" width="1200">



**############################################################################# **

## 知识点4：使用docker开启mysql容器

### 1、安装mysql镜像

```
[root@docker ~]# docker pull mysql:5.7.39
5.7.39: Pulling from library/mysql
9815334b7810: Pull complete 
f85cb6fccbfd: Pull complete 
b63612353671: Pull complete 
447901201612: Pull complete 
9b6bc806cc29: Pull complete 
24ec1f4b3b0d: Pull complete 
207ed1eb2fd4: Pull complete 
27cbde3edd97: Pull complete 
0a5aa35cc154: Pull complete 
e6c92bf6471b: Pull complete 
07b80de0d1af: Pull complete 
Digest: sha256:c1bda6ecdbc63d3b0d3a3a3ce195de3dd755c4a0658ed782a16a0682216b9a48
Status: Downloaded newer image for mysql:5.7.39
docker.io/library/mysql:5.7.39

```

### 2、创建docker容器

```
[root@docker ~]# docker run -d --name sc-mysql-1 -p 33060:3306  -e MYSQL_ROOT_PASSWORD='sc123456'  mysql:5.7.39
[root@docker ~]# docker run -d --name sc-mysql-2 -p 33061:3306  -e MYSQL_ROOT_PASSWORD='sc123456'  mysql:5.7.39

[root@docker ~]# docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                                    NAMES
04f658accb02   mysql:5.7.39   "docker-entrypoint.s…"   7 seconds ago   Up 6 seconds   33060/tcp, 0.0.0.0:33061-&gt;3306/tcp, :::33061-&gt;3306/tcp   sc-mysql-2
3d6aa9a3116b   mysql:5.7.39   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   33060/tcp, 0.0.0.0:33060-&gt;3306/tcp, :::33060-&gt;3306/tcp   sc-mysql-1
fc652e8c734a   nginx          "/docker-entrypoint.…"   3 hours ago     Up 3 hours     0.0.0.0:8090-&gt;80/tcp, :::8090-&gt;80/tcp                    sc-nginx
[root@docker ~]# 

```

### 3、进入容器

```
[root@docker ~]# docker exec -it sc-mysql-1 bash

```

>  
 **exec ：进入容器** 
 **-it ： 开启一个终端** 


```
[root@docker ~]# docker exec -it sc-mysql-1 bash
bash-4.2# 
bash-4.2# ls
bin   dev			  entrypoint.sh  home  lib64  mnt  proc  run   srv  tmp  var
boot  docker-entrypoint-initdb.d  etc		 lib   media  opt  root  sbin  sys  usr
bash-4.2# mysql -uroot -p'sc123456'
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.39 MySQL Community Server (GPL)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt; show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql&gt; create database sanchuang;
Query OK, 1 row affected (0.00 sec)

mysql&gt; show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sanchuang          |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

```

当我们创建容器的时候默认会给root用户授权从本地任何机器登录

```
mysql&gt; select user,host from mysql.user;
+---------------+-----------+
| user          | host      |
+---------------+-----------+
| root          | %         |
| mysql.session | localhost |
| mysql.sys     | localhost |
| root          | localhost |
+---------------+-----------+
4 rows in set (0.00 sec)


```

使用sqlyog连接docker容器中的mysql服务器

<img alt="" height="615" src="https://img-blog.csdnimg.cn/d4b8ba15ce894d029d8596334bf49394.png" width="942">

 **############################################################################# **

## 知识点5：容器，镜像，仓库的概念

>  
 **镜像（image）：** 
 **        镜像是打包好的软件，** 
 **容器（container）：         容器是运行镜像的地方，背后就是起一个进程来运行这个镜像** 
 **仓库（）：** 
 **        仓库是存放镜像的地方   --  docker hub ** 


<img alt="" height="747" src="https://img-blog.csdnimg.cn/0c832dfa47934c7a9dade9e8869470b5.png" width="1200">



>  
 **一个docker进程就是一个docker容器 ** 


```
[root@docker ~]# ps -ef | grep docker
root      11373      1  0 14:08 ?        00:00:19 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
root      11671  11373  0 14:24 ?        00:00:00 /usr/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 8090 -container-ip 172.17.0.2 -container-port 80
root      11675  11373  0 14:24 ?        00:00:00 /usr/bin/docker-proxy -proto tcp -host-ip :: -host-port 8090 -container-ip 172.17.0.2 -container-port 80
root      12173  11373  0 15:17 ?        00:00:00 /usr/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 33060 -container-ip 172.17.0.3 -container-port 3306
root      12177  11373  0 15:17 ?        00:00:00 /usr/bin/docker-proxy -proto tcp -host-ip :: -host-port 33060 -container-ip 172.17.0.3 -container-port 3306
root      12483  11373  0 15:19 ?        00:00:00 /usr/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 33061 -container-ip 172.17.0.4 -container-port 3306
root      12487  11373  0 15:19 ?        00:00:00 /usr/bin/docker-proxy -proto tcp -host-ip :: -host-port 33061 -container-ip 172.17.0.4 -container-port 3306
root      12751  11937  0 15:20 pts/2    00:00:00 docker exec -it sc-mysql-1 bash
root      12836  12130  0 16:14 pts/3    00:00:00 grep --color=auto docker

```

 **#############################################################################**

### alpine ，beta 和 stable的关系

>  
 **alpine ： 内部测试版本，bug较多，一般开发人员和测试人员测试的版本** 
 **beta：公开测试版本，alpha的升级版，仍存在bug** 
 **stable：稳定版本，最终发行版 ** 


**############################################################################# ** 

## 知识点6：比较docker和虚拟机的区别

<img alt="" height="709" src="https://img-blog.csdnimg.cn/ca4739d8623a44f89291f6ecd667eee0.png" width="1200">

>  
 ** docker的优势** 
 **        启动速度快** 
 **        资源消耗小，因为docker容器相当于共享宿主机的内存，内核和基础镜像，消耗内存少** 
 **        扩展方便** 
 **docker的缺点** 
 **        app的隔离这块，没有虚拟机彻底** 
 **层次不一样，虚拟机多一层封装** 


 **############################################################################# **

##  知识点7：docker的底层隔离机制

>  
 **底层隔离机制：** 
 **        所有的容器运行起来后都是一个进程** 
 **        进程和进程之间的隔离靠操作系统来完成** 
 **        所有的进程都是共享linux操作系统的内核的** 
 **        如果理解为人，命名空间理解为人活动的场所** 
 **        如果进程使用了相同命名空间，那么进程之间就可以通信了，互相之间可以有交集** 
 **        linux内核里有个软件LXC_linux Container** 


>  
 **1.LXC是什么？** 
 **LXC是Linux containers的简称，是一种基于容器的操作系统层级的虚拟化技术。** 
 **2.LXC可以做什么？** 
 **LXC可以在操作系统层次上为进程提供的虚拟的执行环境，一个虚拟的执行环境就是一个容器。可以为容器绑定特定的cpu和memory节点，分配特定比例的cpu时间、IO时间，限制可以使用的内存大小（包括内存和是swap空间），提供device访问控制，提供独立的namespace（网络、pid、ipc、mnt、uts）。** 


>  
 **命名空间（name apace）的种类** 
 **        进程命名空间** 
 **        IPC命名空间** 
 **        挂载命名空间** 
 **        用户命名空间** 
 **        UTS命名空间** 


** Control Groups**

<img alt="" height="133" src="https://img-blog.csdnimg.cn/bba6af3adefb44d696eee7c14b7f6c36.png" width="1200">


