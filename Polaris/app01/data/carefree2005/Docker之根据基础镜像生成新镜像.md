
--- 
title:  Docker之根据基础镜像生成新镜像 
tags: []
categories: [] 

---
## 一、Docker镜像简介

  Docker镜像是Docker容器的基础，可以理解为是一个只读的模板，包含了运行Docker容器所需的所有文件、配置和依赖关系。镜像可以从一个或多个Dockerfile构建而来，也可以从其他镜像构建而来。Docker镜像可以被存储、分享和重复使用，可以在不同的环境中部署相同的应用程序，从而实现快速、可靠的部署。Docker Hub是一个公共的镜像仓库，包含了数以万计的Docker镜像，开发者可以在其中找到自己需要的镜像，并在自己的项目中使用它们。   Docker镜像的优点包括：
1.  节省时间和成本：Docker镜像可以在不同的环境中使用，避免了重复构建和配置环境的工作，从而节省了时间和成本。 1.  提高可靠性：Docker镜像具有可移植性和一致性，可以确保应用程序在不同的环境中的运行一致性。 1.  提高安全性：Docker镜像可以在镜像构建时添加安全性检查和验证，确保应用程序的安全性。 
  创建docker镜像主要有如下四种方式：
1.  从已有的镜像创建：可以使用docker pull命令从Docker Hub或其他镜像仓库中拉取镜像，然后使用docker run命令创建容器。 1.  使用Dockerfile创建：Dockerfile是一个文本文件，包含了一系列指令，用于构建Docker镜像。可以使用docker build命令根据Dockerfile创建镜像。 1.  从容器创建：可以使用docker commit命令从一个运行中的容器创建一个新的镜像。 1.  使用外部文件创建：可以使用docker import命令从一个本地文件或远程URL创建一个新的镜像。 
  博文实验内容是根据基础镜像，安装自建服务所需的软件后创建新的镜像，博文实验环境信息如下：
- 操作系统：centos7.9- docker版本：23.0.1
## 二、安装步骤

### 1、安装docker

  docker的安装可以参考博文。也可以使用如下方式安装指定版本的docker。

>  
 #YUM软件包更新到最新 [root@s142 ~]# yum update #卸载旧版本 [root@s142 ~]# yum remove docker docker-common docker-selinux docker-engine #安装依赖 [root@s142 ~]# yum install -y yum-utils device-mapper-persistent-data lvm2 #设置yum源 [root@s142 ~]# yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo #查看仓库中的docker版本 [root@s142 ~]# yum list docker-ce --showduplicates | sort -r #安装指定版本docker，使用yum install -y docker-ce默认安装最新稳定版 [root@s142 ~]# yum install -y docker-ce-23.0.1 


### 2、启动docker服务

>  
 [root@yws55 ~]# systemctl start docker 


### 3、下载Ubuntu基础镜像

>  
 [root@yws55 ~]# docker pull ubuntu Using default tag: latest latest: Pulling from library/ubuntu dbf6a9befcde: Pull complete Digest: sha256:dfd64a3b4296d8c9b62aa3309984f8620b98d87e47492599ee20739e8eb54fbf Status: Downloaded newer image for ubuntu:latest 


### 4、启动Ubuntu容器

>  
 [root@yws55 ~]# docker run -itd --name utest ubuntu b931c65c888a2afa00f98e1a38c191602dc5e0ef92891e556243d025f84c719a [root@yws55 ~]# docker ps CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES 03cc479b5387 ubuntu “/bin/bash” 18 seconds ago Up 17 seconds utest 


### 5、登录Ubuntu容器

>  
 [root@yws55 ~]# docker exec -it utest /bin/bash root@03cc479b5387:/# 


### 6、安装基础命令

  基础镜像没有ip addr、netstat、wget等基础命令，我们先更新apt-get源，然后安装这些基础命令。

>  
 root@03cc479b5387:/# apt-get update root@03cc479b5387:/# apt-get install -y iproute2 root@03cc479b5387:/# apt-get install -y net-tools root@03cc479b5387:/# apt-get install -y wget 


### 6、创建一个普通用户

  安装anaconda3要求使用普通用户安装，我们先创建一个普通用户。

>  
 root@03cc479b5387:/# useradd test -m -s /bin/bash 


### 7、基础镜像内安装anconda3

  在容器内下载并安装anconda3，安装完成后可以找到conda命令说明安装成功。

>  
 root@03cc479b5387:/# su - test test@03cc479b5387:~$ wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2020.02-Linux-x86_64.sh test@03cc479b5387:~$ chmod u+x Anaconda3-2020.02-Linux-x86_64.sh test@03cc479b5387:~$ sh Anaconda3-2020.02-Linux-x86_64.sh … test@03cc479b5387:~$ source ~/.bashrc (base) test@03cc479b5387:~$ which conda /home/test/anaconda3/bin/conda 


### 8、生成新镜像

  使用命令docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]生成一个新的镜像。生成后可以使用docker images命令查看，已经更新到镜像列表中。 <img src="https://img-blog.csdnimg.cn/e75626b1b89848d4987d559260c3c554.png" alt="在这里插入图片描述">

>  
 #docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]] -a：提交镜像的作者 -m：镜像说明 -p：在提交镜像时将容器暂停 -c：以Dockerfile方式创建镜像 root@vanfonuat:~# docker commit -a “wuhs@123.com” -m “conda install” 03cc479b5387 ubuntu:20.04_conda 


### 9、保存镜像为tar文件

>  
 [root@yws55 ~]# docker save ubuntu_conda &gt; ubuntu_conda.tar [root@yws55 ~]# ll total 4008284 -rw-------. 1 root root 1419 Mar 16 11:40 anaconda-ks.cfg -rw-r–r-- 1 root root 4104475648 May 10 11:51 ubuntu_conda.tar 


### 10、镜像拷贝到其他主机

>  
 [root@yws55 ~]# scp ubuntu_conda.tar 192.168.0.142:/tmp/ 


### 11、加载镜像

  使用docker load命令加载tar包文件到docker中。

>  
 [root@s142 ~]# docker load &lt; /tmp/ubuntu_conda.tar <img src="https://img-blog.csdnimg.cn/7302e9f69fd540da85fb346b99498738.png" alt="在这里插入图片描述"> 


### 12、使用自建镜像创建一个容器

>  
 [root@s142 ~]# docker run -itd --name ucondatest ubuntu_conda 4b72bc2ec581837491c4869bd832e16ac40f5f7e00d0c9e98cb2735a9ec46140 


### 13、登录容器查看是否已安装anaconda3

  登录容器后，可以看到以新的镜像启动的容器已经包含了我们前面所安装的配置、命令、软件。使用这种方式可以帮助快速完成离线部署。 <img src="https://img-blog.csdnimg.cn/60d656c268e94d7c86cea116bbcbcffd.png" alt="在这里插入图片描述">
