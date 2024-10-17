
--- 
title:  Docker - 卷 - 数据持久化 
tags: []
categories: [] 

---
**目录**



























































## 知识点1：镜像本质就是一个文件

>  
 **镜像其实就是一个包含了程序代码，基础操作系统，以及程序启动所依赖的软件和库，在容器运行的整体单元** 


### docker save -o nginx.tar nginx  将docker容器里的镜像导出

```
[root@docker ~]# docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
mysql        5.7.39    daff57b7d2d1   27 hours ago   430MB
nginx        latest    2b7d6430f78d   2 days ago     142MB
[root@docker ~]# ls
anaconda-ks.cfg
[root@docker ~]# docker save -o nginx.tar nginx
[root@docker ~]# ls
anaconda-ks.cfg  nginx.tar
[root@docker ~]# 

```

**######################################################## **

### docker load &lt;nginx.tar 将镜像导入docker

<img alt="" height="289" src="https://img-blog.csdnimg.cn/d26a4d86104e41b89c879952336c4d90.png" width="1156">

### docker export -o my_nginx.tar my_nginx  导出正在运行的容器里的文件系统成一个归档文件

**######################################################## ** 

## 知识点2：根据镜像创建容器  docker create

### docker create -p 7000:80 --name sc-nginx-2 nginx:1.22.0

<img alt="" height="365" src="https://img-blog.csdnimg.cn/ad27ad1fb0784c698d46a7c7135002b4.png" width="1200">

** 启动创建好的容器**

<img alt="" height="187" src="https://img-blog.csdnimg.cn/789b3aab04d945d794eb7c13b1ae9fd8.png" width="1200">

>  
 ** 所以创建容器使用docker run比较方便** 
 **docker run = docker create + docker pull + docker start** 


 **######################################################## ** 

## 知识点3:容器有哪些状态？

```
created（已创建）
restarting（重启中）
running（运行中）
removing（迁移中）
paused（暂停）
exited（停止）
dead（死亡）

```

 **######################################################## ** 

## 知识点4：限制cpu和内存使用

<img alt="" height="135" src="https://img-blog.csdnimg.cn/b6e7dbe6205f46b495604284c520b983.png" width="1200">

>  
 **--rm 一旦退出容器，容器会自动删除** 
 **-m 限制内存 byte** 
 **--cpu-shares 2  限制使用cpu计算资源（算力）** 
 **--cpus 1 限制使用1个cpu** 
 **-it centos:7 : ** 
 **--cpuset-cpus 0 ：限制使用编号为0的cpu** 


<img alt="" height="154" src="https://img-blog.csdnimg.cn/7597458e843f481c927f4d3ec1ab7dbe.png" width="1200">

  **######################################################## ** 

## 知识点5：docker inspect + 容器名 查看容器详细信息

```
[root@docker scdocker]# docker inspect sc-nginx
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "ab6c8af427413561c62c317f8fca4a00f2302985659369b7864e525343d587cb",
                    "EndpointID": "31ee662cb4cf61a28da11561e8d822fabf64908f083b980e391a7ef9157af0c9",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null

```

  **######################################################## **  

## 知识点6：微服务

**微服务：**

>  
 **        微小的服务，尽量将某个功能或者服务独立出来，跑在单独的容器里面** 
 **        将一个复杂的系统，拆分成很多小的系统，很多小的系统都需要单独开发，然后单独地部署使用，部署到容器里面，独立地对外提供服务，这个小的服务就简称微服务，人力的成本，部署服务器的成本** 
 **使用容器的优点：降低成本，省钱** 
 **微服务背后就是容器** 


  **######################################################## **   

## 知识点7：IaaS，PaaS，SaaS，BaaS 的概念

>  
 **Iaas：Infrastructure as a service 基础设施即服务** 
 **        作用是提供虚拟机或者其他资源作为服务提供给用户，** 
 **        卖基础设施--卖云服务器  --阿里云，腾讯云，google云等** 
 **PaaS：Platform as a service 平台即服务** 
 **        背后有一个公司搭建好了平台，我们去购买服务就可以了** 
 **SaaS：Software as a Service ** 
 **        作用是提供应用作为服务给客户，通过这种模式，用户只要接上网络，** 
 **        并通过浏览器，就能直接使用在云端上运行的应用，而不需要考虑类似安装琐事** 
 **BaaS： BlockChain as a Service ** 
 **        卖区块链服务的。** 


<img alt="" height="483" src="https://img-blog.csdnimg.cn/583122d18efa432b9b06742059aa6cc4.png" width="879">



   **######################################################## **   

##  知识点8：多容器之间数据共享问题

### 容器的数据保存问题 - 数据持久化

#### 正常停止容器，容器里面的数据会丢失吗？

>  
 **不会丢失，数据会保存到卷里面** 


#### 示例：连接上容器里的数据库，新建一个表，里面添加内容

 <img alt="" height="619" src="https://img-blog.csdnimg.cn/a5192a4141e844afbf73d1d5ddbae77f.png" width="989">

<img alt="" height="456" src="https://img-blog.csdnimg.cn/66512e7269c84011874f4783d6aa5c56.png" width="1200">

<img alt="" height="678" src="https://img-blog.csdnimg.cn/af118a4716f94f2b9cc6a1a923e39ff1.png" width="1200">

 **######################################################## **   

####  怎么查看卷id分别对应哪个容器？ 示例：使用docker inspect 过滤来查看卷id

```
[root@docker volumes]# docker inspect sc-mysql-1 | egrep "volumes"
                "Source": "/var/lib/docker/volumes/71394fb4bfe1cdacd3622a435063ac43f8638c806dcffeca4bdada2a6d1cf953/_data",

```

#### docker volume ls   ： 查看卷id

```
[root@docker wangsh]# docker volume ls
DRIVER    VOLUME NAME
local     71394fb4bfe1cdacd3622a435063ac43f8638c806dcffeca4bdada2a6d1cf953
local     5774708aa65ec9a5adc2b7ebd32b43e858169bacfd8dd3d8d3f153d5feccd983
local     a19c532653e262509d1e0316c60d7a87f0c878c8586cad5cf9c11f731ce50fa4
local     ecbbfaa3571c0e62e7436ab4381cbfecf3b5b47a6f8e0d9d3f2ba3f91b2fc57c
local     ed39f0259834f200157f7ec1a2fd95199173eed1e1ff07bba8ea82f504f7001f
local     my_wordpress_db_data
local     my_wordpress_wordpress_data

```

**######################################################## **   

## 知识点9：容器共享宿主机的文件

### 使用nginx镜像，运行一个容器

>  
 **docker run -d -p 8803:80 --name yangyj-nginx nginx ** 


### 在宿主机上面新建文件夹/web，新建index.html文件

#### 将宿主机的/web/index.html文件docker cp到容器里面

```
[root@docker web]# docker cp /web/index.html yangyj-nginx:/usr/share/nginx/html

```

```
[root@docker web]# cat index.html 
welcome to yang yong jie's web!!

```

但是现在我们修改宿主机的文件，容器内部的index文件并不会修改

### 怎么让容器里的文件共享使用宿主机的文件？

**重新启动一个容器使用/web目录，挂载进入容器，避免频繁的cp到容器里面**

>  
 **docker run -d -p 8803:80 --name yangyj-nginx -v /web:/usr/share/nginx/html  nginx** 
 **-v  :指定宿主机的文件夹挂载到容器里面的路径  volume  --》文件夹和文件夹之间的映射** 


**######################################################## **    

##  知识点10：一台机器的多个容器之间共享数据

### 创建和管理volume 数据卷

#### docker  volume  create  +  数据卷名  创建一个数据卷

```
[root@docker web]# docker volume create nginx-web
nginx-web
[root@docker web]# docker volume ls
DRIVER    VOLUME NAME
local     71394fb4bfe1cdacd3622a435063ac43f8638c806dcffeca4bdada2a6d1cf953
local     5774708aa65ec9a5adc2b7ebd32b43e858169bacfd8dd3d8d3f153d5feccd983
local     a19c532653e262509d1e0316c60d7a87f0c878c8586cad5cf9c11f731ce50fa4
local     ecbbfaa3571c0e62e7436ab4381cbfecf3b5b47a6f8e0d9d3f2ba3f91b2fc57c
local     ed39f0259834f200157f7ec1a2fd95199173eed1e1ff07bba8ea82f504f7001f
local     my_wordpress_db_data
local     my_wordpress_wordpress_data
local     nginx-web
[root@docker web]# cd /var/lib/docker/volumes/
[root@docker volumes]# ls
5774708aa65ec9a5adc2b7ebd32b43e858169bacfd8dd3d8d3f153d5feccd983  backingFsBlockDev                                                 metadata.db                  nginx-web
71394fb4bfe1cdacd3622a435063ac43f8638c806dcffeca4bdada2a6d1cf953  ecbbfaa3571c0e62e7436ab4381cbfecf3b5b47a6f8e0d9d3f2ba3f91b2fc57c  my_wordpress_db_data
a19c532653e262509d1e0316c60d7a87f0c878c8586cad5cf9c11f731ce50fa4  ed39f0259834f200157f7ec1a2fd95199173eed1e1ff07bba8ea82f504f7001f  my_wordpress_wordpress_data
[root@docker volumes]# cd nginx-web/
[root@docker nginx-web]# ls
_data
[root@docker nginx-web]# cd _data/

```

### docker  inspect  nginx-web ： 查看卷信息

```
[root@docker _data]# docker inspect nginx-web
[
    {
        "CreatedAt": "2022-08-31T21:49:46+08:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/nginx-web/_data",
        "Name": "nginx-web",
        "Options": {},
        "Scope": "local"
    }
]
[root@docker _data]# 

```

### 在创建好的数据卷里面新建index.html文件

```
[root@docker _data]# vim index.html
[root@docker _data]# ls
index.html
[root@docker _data]# cat index.html 
welcome to sanchunag

```

### 新建几个容器，使用nginx-web卷

```
[root@docker _data]# docker run -d -p 8805:80 --name yangyj-nginx-2 -v nginx-web:/usr/share/nginx/html nginx
0f255c218081b17b1777acdff2a8ef8bffe743aa50f77772f7098b5fa0effaca
[root@docker _data]# docker run -d -p 8806:80 --name yangyj-nginx-3 -v nginx-web:/usr/share/nginx/html nginx
5896e0abc9bddc81960cc99926360df4a020f51858c5c7355ea13a0eaad4427e
[root@docker _data]# docker run -d -p 8807:80 --name yangyj-nginx-4 -v nginx-web:/usr/share/nginx/html nginx
eda9896eb1677bb68747464ea9c422ddfe91ae7d6e69a5a1c8b86063081d9d3f
[root@docker _data]# docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                                                    NAMES
eda9896eb167   nginx          "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8807-&gt;80/tcp, :::8807-&gt;80/tcp                    yangyj-nginx-4
5896e0abc9bd   nginx          "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        0.0.0.0:8806-&gt;80/tcp, :::8806-&gt;80/tcp                    yangyj-nginx-3
0f255c218081   nginx          "/docker-entrypoint.…"   4 minutes ago        Up 4 minutes        0.0.0.0:8805-&gt;80/tcp, :::8805-&gt;80/tcp                    yangyj-nginx-2
```

访问nginx服务：

<img alt="" height="174" src="https://img-blog.csdnimg.cn/65ba752a63cf457f8de50c43f4fae51c.png" width="912">

 <img alt="" height="171" src="https://img-blog.csdnimg.cn/d84161e5c2ea40999a8ac226abbcf317.png" width="914"><img alt="" height="165" src="https://img-blog.csdnimg.cn/d96304f1376a4e899c92e40e2aaaa884.png" width="905">

>  
 ** 当这几个容器使用的一个数据卷发送变化以后，所有容器的数据都会变化** 


<img alt="" height="205" src="https://img-blog.csdnimg.cn/5e42305d24ec47788d4e6a62641da6aa.png" width="905">

 <img alt="" height="227" src="https://img-blog.csdnimg.cn/07ec8d0876fb42aea34f9898ce0b733d.png" width="903"><img alt="" height="163" src="https://img-blog.csdnimg.cn/86d030addb3849a6b30356bfafa8da9e.png" width="906">**######################################################## **   






