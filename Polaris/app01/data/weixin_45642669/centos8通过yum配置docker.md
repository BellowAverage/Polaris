
--- 
title:  centos8通过yum配置docker 
tags: []
categories: [] 

---
不推荐用压缩包安装：
- 环境依赖太多难以梳理- 需要手写配置文件，对刚入门非常不友好
#### 配置镜像源（全新）

首先，centos8的镜像源已经失效，需要删除。如果已经配置不要动

```
cd /etc/yum.repos.d/
rm -r *

```

然后重新下载配置。

```
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo
或者
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo

```

然后重新加载配置文件

```
yum clean all
 yum makecache

```

### 配置docker源

```
yum install -y yum-utils device-mapper-persistent-data lvm2

yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum makecache

```

#### 下载docker

```
 yum -y install docker-ce

```

#### 启动docker

```
systemctl start docker

systemctl  enable docker.service

systemctl restart docker

```

当无法使用sysmctl的时候：
-  不是root权限不够 <li> 是root但是被占用权限 <pre><code>kill -TERM 1
</code></pre> </li>
当提示无法安装：
- 已经安装了，需要覆盖安装- 版本无法匹配导致安装失败
按照提示操作即可。
