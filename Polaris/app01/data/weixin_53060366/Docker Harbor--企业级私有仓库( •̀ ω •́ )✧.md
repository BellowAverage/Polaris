
--- 
title:  Docker Harbor--企业级私有仓库( •̀ ω •́ )✧ 
tags: []
categories: [] 

---
## Docker Harbor–企业级私有仓库



#### 文章目录
- - <ul><li>- - - - - - <ul><li><ul><li>- 


### 1、Harbor简介：

Harbor是一个灯塔的形状。

<img src="https://img-blog.csdnimg.cn/85138f6f649d455791ba6e925a73ff7d.png#pic_center" alt="在这里插入图片描述">
- Harbor 是 VMware 公司开源的企业级 Docker Registry 项目，其目标是帮助用户迅速搭建一个企业级的 Docker Registry 服务。- Harbor以 Docker 公司开源的 Registry 为基础，提供了图形管理 UI 、基于角色的访问控制(Role Based AccessControl) 、AD/LDAP 集成、以及审计日志(Auditlogging) 等企业用户需求的功能，同时还原生支持中文。- Harbor 的每个组件都是以 Docker 容器的形式构建的，使用 docker-compose 来对它进行部署。用于部署 Harbor 的 docker-compose 模板位于 harbor/docker-compose.yml。
### 2、Harbor特性
- 基于角色控制：用户和仓库都是基于项目进行组织的，而用户在项目中可以拥有不同的权限。- 基于镜像的复制策略：镜像可以在多个 Harbor 实例之间进行复制（同步）。- 支持 LDAP/AD：Harbor 可以集成企业内部已有的 AD/LDAP（类似数据库的一张表），用于对已经存在的用户认证和管理。- 镜像删除和垃圾回收：镜像可以被删除，也可以回收镜像占用的空间。- 图形化用户界面：用户可以通过浏览器来浏览，搜索镜像仓库以及对项目进行管理。- 审计管理：所有针对镜像仓库的操作都可以被记录追溯，用于审计管理。- 支持 RESTful API：RESTful API 提供给管理员对于 Harbor 更多的操控, 使得与其它管理软件集成变得更容易。- Harbor和docker registry的关系：Harbor实质上是对docker registry做了封装，扩展了自己的业务模板。
### 3、Harbor的组件

Harbor 在架构上主要有 Proxy、Registry、Core services、Database（Harbor-db）、Logcollector（Harbor-log）、Job services 六个组件。

<img src="https://img-blog.csdnimg.cn/61bb0615d3664e7db282b2d32a9d6e66.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/4f400a25df254747b77b0a8a1d11f924.png#pic_center" alt="在这里插入图片描述">

|Proxy|通过一个前置的反向代理统一接收浏览器、Docker客户端的请求，并将请求转发给后端不同的服务。
|------
|Registry(核心组件)|负责储存Docker镜像，并处理docker push/pull命令。
|Core services|Harbor 的核心功能， 包括 UI、webhook、 token 服务。
|Database|为core services提供数据库服务，负责储存用户权限、审计日志、Docker 镜像分组信息等数据。
|Log collector|负责收集其他组件的log，供日后进行分析。
|Job services|主要用于镜像复制，本地镜像可以被同步到远程 Harbor 实例上。

**注意：**Harbor 的每个组件都是以 Docker 容器的形式构建的，因此，使用 Docker Compose 来对它进行部署。

### 4、Docker Harbor部署

```
#首先要下载好Harbor包
cd /opt
#将下好的Harbor包拉进去
#解压
tar zxf harbor-offline-installer-v1.2.2.tgz -C /usr/local

#修改Harbor 配置文件
cd /usr/local/harbor/
vim harbor.cfg    #这里修改主机地址
hostname = 192.168.111.40

#启动docker Harbor，注意：启动之前先确认Docker-Compose 版本安装是否成功
docker-compose -v
cd /uar/local/harbor
bash install.sh
#查看当前服务运行的容器
docker-compose ps
#查看docker-compose.yml 的信息
cat docker-compose.yml


```

<img src="https://img-blog.csdnimg.cn/945fc35e1abc47e9b5d269723e57df9b.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/609dd6920c9340ca8b3e6193d6ccfd64.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/58b9df712a5042749808c0f4cfcd762e.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/164352c4a6f04e1cbc415860c7b6da6d.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/56a7a2d4150942b6af9f67dee1686cb8.png#pic_center" alt="在这里插入图片描述">

### 5、访问Harbor的UI界面
- 浏览器访问：192.168.111.40/harbor- 用户名：admin- 密码 ：Harbor12345
<img src="https://img-blog.csdnimg.cn/611ede3ece32405eabf7a0fd1ad6223e.png#pic_center" alt="在这里插入图片描述">

登录之后；

<img src="https://img-blog.csdnimg.cn/d288ec09938843bfb862f6cf610517e3.png#pic_center" alt="在这里插入图片描述">

### 6、创建镜像仓库及push镜像

首先要新建项目仓库；

<img src="https://img-blog.csdnimg.cn/eaafd19bf5444f829865181e1b674557.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f0302c5412e242d09454a23d8f5017d0.png#pic_center" alt="在这里插入图片描述">

##### 登录Harbor

在我们要push 镜像到Harbor 时，我们要先登录 Docker Harbor；

```
docker login -u admin -p Harbor12345 http://192.168.111.40
#或者
docker login -u admin -p Harbor12345 http://127.0.0.1

```

<img src="https://img-blog.csdnimg.cn/70de9d608b2b41f2bf3b0aac07306659.png#pic_center" alt="在这里插入图片描述">

再将镜像打上标签，push到 Harbor 仓库；

```
#下载镜像和打标签
docker pull cirros
docker tag cirros:latest 127.0.0.1/my-harbor/cirros:v1
#push 镜像
docker push 127.0.0.1/my-harbor/cirros:v1

```

<img src="https://img-blog.csdnimg.cn/830fb732f31045dcb9b5b49e4e01ed5f.png#pic_center" alt="在这里插入图片描述">

这里我们就push 到了Harbor仓库中了。

<img src="https://img-blog.csdnimg.cn/4cc916455c9c4da4894ce13a0b823cf8.png#pic_center" alt="在这里插入图片描述">

##### 测试 pull仓库中的镜像

<img src="https://img-blog.csdnimg.cn/74a6efdf6e474381bfa78b3c7a69795f.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/06abcbe511164f6db9127f9ae09b0e92.png#pic_center" alt="在这里插入图片描述">

**注意：这里你先前push 的是啥地址，pull 时也要是啥IP地址。**

所以上面pull 自己IP的时候会报错。
