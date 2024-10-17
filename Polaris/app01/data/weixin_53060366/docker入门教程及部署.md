
--- 
title:  docker入门教程及部署 
tags: []
categories: [] 

---
## docker入门教程及部署



#### 文章目录
- - <ul><li>- - - - - - - - <ul><li>- - <ul><li>- - - - - - 


### 1、Docker简介：

01）Docker 是一个开源的应用容器引擎，基于  并遵从 Apache2.0 协议开源。

02）Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

03）容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

04）Docker 从 17.03 版本之后分为 CE（Community Edition: 社区版） 和 EE（Enterprise Edition: 企业版），我们用社区版就可以了。

在计算机安全领域，沙箱是一种程序的隔离运行机制；

### 2、谁适合阅读该教程？

教程适合运维工程师及后端开发人员，通过本教程你可以一步一步了解 Docker 的使用。

在阅读本教程前，你需要掌握 Linux 的常用命令。

### 3、Dock的应用场景：
- Web 应用的自动化打包和发布。- 自动化测试和持续集成、发布。- 在服务型环境中部署和调整数据库或其他的后台应用。- 从头编译或者扩展现有的 OpenShift 或 Cloud Foundry 平台来搭建自己的 PaaS 环境。
### 4、Docker的优点：

Docker 是一个用于开发，交付和运行应用程序的开放平台。Docker 使您能够将应用程序与基础架构分开，从而可以快速交付软件。借助 Docker，您可以与管理应用程序相同的方式来管理基础架构。通过利用 Docker 的方法来快速交付，测试和部署代码，您可以大大减少编写代码和在生产环境中运行代码之间的延迟。

01）快速，一致的交互您的应用程序；

02）响应式部署和扩展；

03）在同一硬件上运行更多的工作负载；

### 5、Docker架构：

Docker三大组件：
- **镜像（Image）**：Docker 镜像（Image），就相当于是一个 模板。- **容器（Container）**：镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的类和实例一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。- **仓库（Repository）**：仓库可看成一个代码控制中心，用来保存镜像。
Docker 使用客户端-服务器 (C/S) 架构模式，使用远程API来管理和创建Docker容器。

Docker 容器通过 Docker 镜像来创建。

<img src="https://img-blog.csdnimg.cn/6221296bfb3344cfa6a817c39845596c.png#pic_center" alt="在这里插入图片描述">

### 6、Docker底层原理：
- cgroup和namespaces两者构成了docker底层原理；- cgroup 资源控制与namespaces 结合控制管理了6个名称空间资源（以下）：- 容器隔离了6个名称空间(namespace资源隔离—用容器化技术封装）- mount 文件挂载点，一个文件系统内，不能重复挂载一个指定目录，例如:/mnt；- user 操作进程的用户和用户组；- pid 进程编号；- uts 主机名和主机域；- ipc 信号量、消息队列，共享内存（理解，不同的应用调用内存资源的时候应该使用不同的内存空间)；- net网络设备、网络协议栈、端口等； <img src="https://img-blog.csdnimg.cn/f820bc6738994f3b962646b7e9c552a8.png#pic_center" alt="在这里插入图片描述">
### 7、比较Docker和虚拟机技术的不同：

<img src="https://img-blog.csdnimg.cn/47bbee2247db417c9bc70cdbfa1e83db.png#pic_center" alt="在这里插入图片描述">

1、传统虚拟机，虚拟出一条硬件，运行一个完整的操作系统，然后在这个系统上安装和运行软件。 2、容器内的应用直接运行在宿主机的内核，容器是没有自己的内核的，也没有虚拟我们的硬件，所以就轻便了。 3、每个容器间是互相隔离，每个容器内都有一个属于自己的文件系统，互不影响。

<img src="https://img-blog.csdnimg.cn/631f4ea06599437891434c53cd9c7b14.png#pic_center" alt="在这里插入图片描述">

### 8、部署Centos Docker

#### （1）、使用官方安装脚本自动安装：

```
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
#也可以使用国内 daocloud 一键安装命令
curl -sSL https://get.daocloud.io/docker | sh

```

#### （2）手动安装：

##### 01、首先要卸载旧版本：

较旧的 Docker 版本称为 docker 或 docker-engine 。如果已安装这些程序，请卸载它们以及相关的依赖项。

```
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

```

<img src="https://img-blog.csdnimg.cn/ee047168b35946d7a59dc92d4b2da2c9.png#pic_center" alt="在这里插入图片描述">

##### 02、关闭防火墙，SELinux，修改服务器名：

```
systemctl stop firewalld.service
systemctl disable firewalld.service
setenforce 0
hostnamectl set-hostname docker

```

##### 03、使用YUM仓库安装Docker

安装依赖包：

```
yum install -y yum-utils device-mapper-persistent-data lvm2

```

设置阿里云镜像源：

```
cd /etc/yum.repo.d
yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

```

<img src="https://img-blog.csdnimg.cn/8571f9e9262047d4b54f95d5d3eb743e.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e2cb57caabfd489e81f540366f80d485.png#pic_center" alt="在这里插入图片描述">

##### 04、安装docker-ce

```
yum install -y docker-ce
systemctl start docker.service
systemctl enable docker.service

```

##### 05、镜像加速：

每个账号都有一个自己的镜像加速器；

<img src="https://img-blog.csdnimg.cn/0519a7aa776446f5ac57de4fe7b703cd.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2c7ab4b6aef54a128b09ba56498c73d3.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/21c57e95a31641f5949622925875b5d2.png#pic_center" alt="在这里插入图片描述">

```
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json &lt;&lt;-'EOF'
{
  "registry-mirrors": ["https://yagayyvn.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

```

##### 06、网络优化：

```
vim /etc/sysctl.conf
	net.ipv4.ip_forward=1
sysctl -p
systemctl restart network
systemctl restart docker
#查询镜像列表
docker images

```

<img src="https://img-blog.csdnimg.cn/ac17f02905d44f88a3f83d2d5d5de98a.png#pic_center" alt="在这里插入图片描述">

##### 07、Docker相关命令：

```
#查看docker版本
docker version
docker info

```

<img src="https://img-blog.csdnimg.cn/b440e29f664f496593cb84cc59e7784b.png#pic_center" alt="在这里插入图片描述">

这里引申一些配置文件的内容：

```
vim /etc/docker/daemon.json		##docker配置文件还可以添加以下的建立配置：
	{<!-- -->
	"graph": "/data/docker",					##数据目录
	"storage-driver": "overlay2",				##存储引擎；版本迭代：LXC——&gt;overlay——&gt;overlay2(overlayfs:文件系统，解决docker镜像分层)
	"insecure-registries": [" registry.access.redhat.com", "quary.io"]	##私有仓库位置
	"registry-mirrors": ["https://q***"]		##镜像加速
	"bip": "172.7.5.1/24",		##docker网络；控制网段的位置；需要创建新的网桥，系统默认的docker0是不变的
	"exec-opts": ["native.cgroupdriver-systemd"],		##启动时候的额外参数(驱动)
	"live-restore":true		##当docker容器引擎挂掉的时候，使用docker跑起来的容器还能运行(分离)
}

```

运行镜像：

```
#运行镜像
docker run hello-world		##运行hello-world镜像
	run代表以下：
		①：pull	dockerhub	下载仓库中项目/库/镜像
		②：start hello-world image
		
#搜索镜像
docker search nginx		##搜索镜像nginx
docker search centos: 7		##搜索镜像centos:7

#下载镜像-pull
#client端连接服务端，从docker hub上下载镜像
格式：docker pull 镜像名称
docker pull nginx		##下载nginx最新的镜像

#查看镜像
docker  images	##查看镜像列表
docker images -q	##查询镜像过滤ID
#q：代表过滤；只过滤容器ID

```

<img src="https://img-blog.csdnimg.cn/b891b2b715d145e0884890362dafb40a.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/8e9777b346944324bb2c143b40570933.png#pic_center" alt="在这里插入图片描述">
