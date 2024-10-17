
--- 
title:  centos7 docker安装记录 
tags: []
categories: [] 

---
以下所有命令都在root用户下进行，若为普通用户，需要在所有命令前加上 sudo。

#### 1、更新yum包

将yum包更新到最新

```
yum update

```

#### 2、安装需要的软件包

yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的；

```
yum install -y yum-utils device-mapper-persistent-data lvm2

```

#### 3、设置yun源

国外镜像一般很难访问，建议配置阿里云镜像：

```
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

```

#### 4、安装docker

默认安装命令为：

```
yum install docker-ce

```

查看所有仓库中所有docker版本，并且选择特定版本安装。命令为：

```
$ yum list docker-ce --showduplicates | sort -r

```

<img src="https://img-blog.csdnimg.cn/e9adb305cbed4501a3748c9fa2338682.png" alt="在这里插入图片描述"> 使用命令指定版本：

```
yum install &lt;FQPN&gt;  # 例如：sudo yum install docker-ce-17.12.0.ce

```

#### 5、启动

```
systemctl start docker

```

<img src="https://img-blog.csdnimg.cn/99101e5245fa477cbd0757c01fe51997.png" alt="在这里插入图片描述">

#### 6、加入开机启动

```
systemctl enable docker

```

```
[root@hecs-207177 ~]# systemctl enable docker
Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.

```

#### 7、查看版本

```
docker version

```

<img src="https://img-blog.csdnimg.cn/d8adf462df4846219e10870615dc378a.png" alt="在这里插入图片描述">
