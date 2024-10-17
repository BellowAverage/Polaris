
--- 
title:  docker的常用指令及使用方法 
tags: []
categories: [] 

---
## 容器化方案Docker

>  
 容器化方案: 
 - **Docker**- Docker的目标之一就是缩短代码从开发、测试到部署、上线运行的周期，让我们的应用程序具备可移植性、易于构建、并易于协作。 


#### 1. Docker介绍
- - Docker 是一个开源的软件部署解决方案。- Docker 也是轻量级的应用容器框架。- Docker 可以打包、发布、运行任何的应用。- Docker 就像一个盒子，里面可以装很多物件，如果需要某些物件，可以直接将该盒子拿走，而不需要从该盒子中一件一件的取。<li>Docker 是一个客户端-服务端(C/S)架构程序。 
  <ul>- 客户端只需要向服务端发出请求，服务端处理完请求后会返回结果。
>  
 Docker 包括三个基本概念: 

<li>镜像（Image） 
  <ul>- Docker的镜像概念类似于虚拟机里的镜像，是一个只读的模板，一个独立的文件系统，包括运行容器所需的数据，可以用来创建新的容器。- 例如：一个镜像可以包含一个完整的 ubuntu 操作系统环境，里面仅安装了MySQL或用户需要的其它应用程序。- Docker容器是由Docker镜像创建的运行实例，类似VM虚拟机，支持启动，停止，删除等。- 每个容器间是相互隔离的，容器中会运行特定的应用，包含特定应用的代码及所需的依赖文件。- Docker的仓库功能类似于Github，是用于托管镜像的。
#### 2. Docker安装（ubuntu 16.04）

>  
 **1.源码安装Docker CE** 


```
$ cd docker源码目录
$ sudo apt-key add gpg
$ sudo dpkg -i docker-ce_17.03.2~ce-0~ubuntu-xenial_amd64.deb

```

<img src="https://img-blog.csdnimg.cn/2020021113182814.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

>  
 **2.检查Docker CE是否安装正确** 


```
$ sudo docker run hello-world

```

出现如下信息，表示安装成功 <img src="https://img-blog.csdnimg.cn/20200211131845852.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

>  
 **3.启动与停止** 
 - 安装完成Docker后，默认已经启动了docker服务。 


```
# 启动docker

$ sudo service docker start

# 重启docker

$ sudo service docker restart

# 停止docker

$ sudo service docker stop

```

#### 3. Docker镜像操作

>  
 **1.镜像列表** 


```
$ sudo docker image ls

```

<img src="https://img-blog.csdnimg.cn/20200211131913266.png" alt="在这里插入图片描述">

```
* REPOSITORY：镜像所在的仓库名称 
* TAG：镜像标签 
* IMAGEID：镜像ID 
* CREATED：镜像的创建日期(不是获取该镜像的日期) 
* SIZE：镜像大小

```

>  
 **2.从仓库拉取镜像** 


```
# 官方镜像

$ sudo docker image pull 镜像名称 或者 sudo docker image pull library/镜像名称
$ sudo docker image pull ubuntu 或者 sudo docker image pull library/ubuntu
$ sudo docker image pull ubuntu:16.04
或者 sudo docker image pull library/ubuntu:16.04
# 个人镜像

$ sudo docker image pull 仓库名称/镜像名称
$ sudo docker image pull itcast/fastdfs

```

<img src="https://img-blog.csdnimg.cn/20200211132816474.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20200211132022485.png" alt="在这里插入图片描述">

>  
 **3.删除镜像** 


```
$ sudo docker image rm 镜像名或镜像ID
$ sudo docker image rm hello-world
$ sudo docker image rm fce289e99eb9

```

<img src="https://img-blog.csdnimg.cn/20200211132043189.png" alt="在这里插入图片描述">

#### 4. Docker容器操作

>  
 **1.容器列表** 


```
# 查看正在运行的容器

$ sudo docker container ls

# 查看所有的容器

$ sudo docker container ls --all

```

<img src="https://img-blog.csdnimg.cn/20200211132058782.png" alt="在这里插入图片描述">

>  
 **2.创建容器** 


```
$ sudo docker run [option] 镜像名 [向启动容器中传入的命令]
常用可选参数说明：
* -i 表示以《交互模式》运行容器。
* -t 表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即分配一个伪终端。
* --name 为创建的容器命名。
* -v 表示目录映射关系，即宿主机目录:容器中目录。注意:最好做目录映射，在宿主机上做修改，然后共享到容器上。 
* -d 会创建一个守护式容器在后台运行(这样创建容器后不会自动登录容器)。 
* -p 表示端口映射，即宿主机端口:容器中端口。
* --network=host 表示将主机的网络环境映射到容器中，使容器的网络与主机相同。

```

>  
 **3.交互式容器** 


```
$ sudo docker run -it --name=ubuntu1 ubuntu /bin/bash

```

<img src="https://img-blog.csdnimg.cn/20200211132125529.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20200211132134877.png" alt="在这里插入图片描述">

```
在容器中可以随意执行linux命令，就是一个ubuntu的环境。
当执行 exit 命令退出时，该容器随之停止。

```

>  
 **4.守护式容器** 


```
# 开启守护式容器

$ sudo docker run -dit --name=ubuntu2 ubuntu

```

<img src="https://img-blog.csdnimg.cn/20200211132155783.png" alt="在这里插入图片描述">

```
# 进入到容器内部交互环境

$ sudo docker exec -it 容器名或容器id 进入后执行的第一个命令
$ sudo docker exec -it ubuntu2 /bin/bash

```

<img src="https://img-blog.csdnimg.cn/20200211132216568.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

```
如果对于一个需要长期运行的容器来说，我们可以创建一个守护式容器。
在容器内部执行 exit 命令退出时，该容器也随之停止。

```

>  
 **5.停止和启动容器** 


```
# 停止容器

$ sudo docker container stop 容器名或容器id

# kill掉容器

$ sudo docker container 
kill 容器名或容器id

# 启动容器

$ sudo docker container start 容器名或容器id

```

<img src="https://img-blog.csdnimg.cn/20200211132240480.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

>  
 **6.删除容器** 
 - 正在运行的容器无法直接删除。 


```
$ sudo docker container rm 容器名或容器id

```

<img src="https://img-blog.csdnimg.cn/20200211132259123.png" alt="在这里插入图片描述">

>  
 **7.容器制作成镜像** 
 - 为保证已经配置完成的环境可以重复利用，我们可以将容器制作成镜像。 


```
# 将容器制作成镜像

$ sudo docker commit 容器名 镜像名

```

<img src="https://img-blog.csdnimg.cn/20200211132320264.png" alt="在这里插入图片描述">

```
# 镜像打包备份

$ sudo docker save -o 保存的文件名 镜像名

```

<img src="https://img-blog.csdnimg.cn/20200211132340600.png" alt="在这里插入图片描述">

```
# 镜像解压

$ sudo docker load -i 文件路径/备份文件

```

<img src="https://img-blog.csdnimg.cn/20200211132354757.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTgwNTMzOQ==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
