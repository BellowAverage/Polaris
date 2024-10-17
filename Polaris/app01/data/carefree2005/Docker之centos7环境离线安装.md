
--- 
title:  Docker之centos7环境离线安装 
tags: []
categories: [] 

---
## 一、docker简介

  Docker是一个开源的应用容器引擎，可以让开发者将应用及其依赖打包在一个虚拟的容器中，方便地部署、移植、升级和管理。Docker可以运行在Linux、Windows和MacOS等操作系统上，并且可以在不同的平台之间进行交互和迁移。Docker的主要特点包括轻量级、快速、易于使用、可移植和可扩展等。Docker的生态系统非常丰富，有许多第三方工具和插件可以与之配合使用，如Docker Compose、Docker Swarm等。Docker已经成为了现代化软件开发和部署的标准之一，被广泛应用于云计算、容器化、微服务等领域。在一些不能访问互联网的局域网环境中，如果我们需要部署应用系统服务，需要安装许多的软件依赖，我们可以采用容器部署方式，将系统服务依赖的软件包提前安装到容器中，然后生成定制的镜像文件，这样就可以实现系统服务的快速离线部署。当然，既然是离线环境，容器所需的docker环境我们也需要离线部署。此博文介绍docker离线安装方式，博文实验环境如下：
- 操作系统：centos7.9- docker版本：23.0.1
## 二、安装步骤

### 1、下载docker安装包

  访问docker官网下载所需的docker版本软件包。

>  
 [root@s142 tmp]# wget https://download.docker.com/linux/static/stable/x86_64/docker-23.0.1.tgz [root@s142 tmp]# ll -h total 64M -rw-r–r-- 1 root root 64M Mar 8 19:23 docker-23.0.1.tgz 


### 2、中断网络模拟内网

  博文是在虚拟机环境下模拟隔离网络，可以通过删除DNS地址或者不配置网关地址的方式模拟隔离网络。

>  
 [root@s142 tmp]# ping www.baidu.com ping: www.baidu.com: Name or service not known 


### 3、解压软件包

>  
 [root@s142 tmp]# tar -zxvf docker-23.0.1.tgz docker/ docker/docker-proxy docker/containerd docker/dockerd docker/runc docker/docker-init docker/containerd-shim-runc-v2 docker/ctr docker/docker 


### 4、复制docker目录下的文件到/usr/bin目录下

  查看解压后的目录，我们可以发现都是一些可以执行文件，我们将这些文件全部复制到/usr/bin目录下。 <img src="https://img-blog.csdnimg.cn/e1a6e969c00a45a98b0240e16cfa2f7e.png" alt="在这里插入图片描述">

### 5、创建docker.service文件

  进入到/usr/lib/systemd/system/目录下，我们编辑创建docker.service文件，用于管理docker服务，复制黏贴如下内容即可。

>  
 [root@s142 tmp]# vim /usr/lib/systemd/system/docker.service 


```
[Unit]
Description=Docker Application Container Engine
Documentation=http://docs.docker.com
After=network.target docker.socket
[Service]
Type=notify
EnvironmentFile=-/run/flannel/docker
WorkingDirectory=/usr/local/bin
ExecStart=/usr/bin/dockerd \
                -H tcp://0.0.0.0:4243 \
                -H unix:///var/run/docker.sock \
                --selinux-enabled=false \
                --log-opt max-size=100m
ExecReload=/bin/kill -s HUP $MAINPID
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
TimeoutStartSec=0
Delegate=yes
KillMode=process
Restart=on-failure
[Install]
WantedBy=multi-user.target

```

### 6、重新加载daemon-reload

>  
 [root@s142 tmp]# systemctl daemon-reload 


### 7、查看docker版本

<img src="https://img-blog.csdnimg.cn/d798f4d64bab4acf80b42121d9fb3ed3.png" alt="在这里插入图片描述">

### 8、启动docker

>  
 [root@s142 system]# systemctl start docker 


### 9、上传本地镜像到服务器

>  
 [root@s142 system]# ll /tmp/ |grep ubuntu -rw-r–r-- 1 root root 4104475648 May 11 11:19 ubuntu_conda.tar 


### 10、加载镜像文件到docker

>  
 [root@s142 system]# docker load &lt; /tmp/ubuntu_conda.tar [root@s142 system]# docker images REPOSITORY TAG IMAGE ID CREATED SIZE ubuntu_conda latest b1ff3fd0fb2e 12 hours ago 3.99GB 


### 11、使用镜像启动容器实例

>  
 [root@s142 system]# docker run -itd --name utest ubuntu_conda 9b10eebcf96c1c2ec324356e136e76304f6a996550a538253b3d5ffa04f8bc29 


### 12、查看容器运行情况看

>  
 [root@s142 system]# docker ps CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES 9b10eebcf96c ubuntu_conda “/bin/bash” About a minute ago Up About a minute utest <img src="https://img-blog.csdnimg.cn/9895ee7b19c24ae28d826868421ae0a4.png" alt="在这里插入图片描述"> 


## 三、写在结尾

  离线安装docker百度查到的是需要手动安装依赖libcgroup库和device-mapper，博主实验时未手动安装这两个包，检查centos7.9系统已经安装了device-mapper，但是没有libcgroup库，但是docker运行并没有发现问题。肯能是因为centos7.9系统环境原因与网上博主环境有区别。所以将这部分留在最后，待后续docker运行发现有问题再进一步更新。

>  
 [root@s142 system]# rpm -qa |grep libcgroup [root@s142 system]# rpm -qa |grep device-mapper device-mapper-persistent-data-0.7.3-3.el7.x86_64 device-mapper-1.02.149-8.el7.x86_64 device-mapper-libs-1.02.149-8.el7.x86_64 device-mapper-event-libs-1.02.149-8.el7.x86_64 device-mapper-event-1.02.149-8.el7.x86_64 

