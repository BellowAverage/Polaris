
--- 
title:  Docker使用具体流程 
tags: []
categories: [] 

---
### 一、创建与启动容器

docker run

 -i :表示运行容器

-t：表示容器启动后会进入其命令行。加入这两个参数之后，容器创建就能登录进去。即分配一个伪终端

--name：为创建的容器命名（容器名称不能重复）

-v：表示目录映射关系（前者是宿主机目录，后者是容器目录），可以使用多个-v做多个目录或文件映射。注意：最好是做目录映射，在宿主机上做修改，然后共享到容器上。

-p：表示端口映射时 ，前者是宿主机端口，后者是容器内的映射端口。可以使用多个-p做端口映射。

一般使用的命令：docker run -it 镜像名称 为交互式方式创建容器(-i-t可以缩写成-it)，之所以称之为交互式，即运行该命令后直接进入一个伪终端。

docker run后该镜像的容器就被创建了，系统会自动为该容器分配一个container id，若不指定容器名，那么随机一个名字，一般为了区分容器，方便下次启动该容器，会使用--name参数自定义容器名；例如：docker run --name=pymesh pymesh/pymesh

注意：如果docker run 后不加参数-i那么容器只是被创建了，并没有被启动。

### 二、启动容器

docker start

docker start 容器名称，即可启动相应容器。

### 三、进入容器

docker exec

常用命令：docker exec -it 容器名称 /bin/bash

进入容器绑定的伪终端。进入后先前终端的文件目录将不能够在该容器下访问，所以为了在伪终端与终端互访相关目录，可以在创建容器时，使用-v参数，进行目录挂载。

例如：

docker run -di -v /home/rui/work/csy:/home/csy --name=pymesh pymesh/pymesh

docker run -di -v 宿主机目录:容器目录 --name=容器名称 镜像名

退出容器时，输入命令exit即可。

### 四、关闭容器

docker stop 容器名
