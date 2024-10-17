
--- 
title:  Docker部署Mysql数据库详解 
tags: []
categories: [] 

---


####  
- - <ul><li>- <ul><li>- - - - - - - 


Docker是一种流行的容器化平台，可以简化应用程序的部署和管理。在本博客中，我们将探讨如何使用Docker部署两个广泛使用的数据库：MySQL。我们将提供详细的步骤和相应的命令，以帮助您轻松地在Docker容器中设置和运行这个数据库。

## 1. Docker部署Mysql

### 1.1 Mysql容器

#### 1.1.1 创建Mysql容器

首先我们拉取mysql镜像，要在Docker中部署MySQL数据库，我们首先需要创建一个MySQL容器。可以使用以下命令创建一个MySQL 8…0.24版本的容器：

```
docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=123456  -p 3307:3306 mysql:8.0.24

```

此命令会创建一个名为mysql-container的容器，将MySQL的root用户密码设置为123456，并将宿主机的3307端口映射到容器的3306端口。

#### 1.1.2 进入Mysql容器并

```
docker exec -it mysql-container mysql -u root -p

```

此命令将打开MySQL的命令行客户端，并要求您输入MySQL root用户的密码如下图：

<img src="https://img-blog.csdnimg.cn/8b0123c611e2403fa8b7d95e4f2e069c.png" alt="">

然后我们就可以在这里进行数据库操作。

#### 1.1.3 持久化数据

为了在容器重新启动后保留MySQL数据，可以将数据目录映射到宿主机的目录。在创建容器时，可以添加以下参数：

```
-v /docker/mysql/config/my.cnf:/etc/my.cnf #宿主机目录：mysql容器目录-v /docker/mysql/data:/var/lib/mysql 

```

这里可以进行数据卷挂载，卷就是目录或文件，存在于一个或多个容器中，由docker挂载到容器，但不属于联合文件系统，因此能够绕过Union File System提供一些用于持续存储或共享数据的特性，卷的设计目的就是数据的持久化，完全独立于容器的生存周期，因此Docker不会在容器删除时删除其挂载的数据卷。数据卷可在容器之间共享或重用数据并且卷中的更改可以直接实时生效，数据卷的生命周期一直持续到没有容器使用它为止。如下图：

<img src="https://img-blog.csdnimg.cn/8741c9d6e6df4df3933bc6ad887802f8.png" alt="">

### 1.2 远程登录Mysql

在Mysql 8.x版本当我们在云服务器上创建dockier容器后，尝试远程登录Docker容器内数据库的时候会遇见如下图问题：

<img src="https://img-blog.csdnimg.cn/ccfb4a794e464b328f321c320c20a73f.png" alt="">

** 这是什么原因呢？**

出现1251的主要原因是由于mysql版本的问题，mysql8.0版本，与mysql8.0以下版本的加密方式不同，导致错误产生。

MySql 8.0.11 换了新的身份验证插件（caching_sha2_password）,而原来的身份验证插件为（mysql_native_password）。​ 而客户端工具Navicat Premium12 中找不到新的身份验证插件（caching_sha2_password），因此报上面的错，所以我们将mysql用户使用的 登录密码加密规则还原成 mysql_native_password，即可登陆成功。

#### 1.2.1 修改root加密方式

运行下面的命令：

```
mysql -u root -p  #登陆mysqluse mysql;	# 切换mysql数据库select host, user, authentication_string, plugin from user; #查看root用户登录加密方式 

```

如下图：

<img src="https://img-blog.csdnimg.cn/3ba3276f85c34d9da04fc36ec647eaa9.png" alt="">

然后我们改变加密命令

```
alter user 'root'@'%' identified with mysql_native_password by '123456';

```

然后再次查看root用户登录的加密方式

```
select host, user, authentication_string, plugin from user; #查看root用户登录加密方式

```

#### <img src="https://img-blog.csdnimg.cn/c6832b12b2b94a078c85087c36175d2d.png" alt="">

然后我们重新使用客户端登录系统显示登录成功。

#### 1.2.2 在容器启动时配置加密方式为`mysql_native_password`

代码`-e identified=mysql_native_password`，配置了加密方式。

```
docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=123456  -p 3307:3306 -e identified=mysql_native_password mysql:8.0.24

```

### 1.3 Mysql编码

#### 1.3.1 Mysql编码问题

当我们使用客户端连接成功我们的docker容器后，然后进行创建数据库，创建表格然后添加数据如下：

```
CREATE DATABASE /*!32312 IF NOT EXISTS*/`project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */; USE `project`; /*Table structure for table `user` */ DROP TABLE IF EXISTS `user`; CREATE TABLE `user` (  `id` BIGINT NOT NULL AUTO_INCREMENT,  `username` VARCHAR(20) DEFAULT NULL,  `password` VARCHAR(20) DEFAULT NULL,  PRIMARY KEY (`id`)) ENGINE=INNODB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci; /*Data for the table `user` */ INSERT  INTO `user`(`id`,`username`,`password`) VALUES (1,'张三','123'),(2,'lisi','456');

```

然后在我们的docker容器内查询mysql数据如下图：

<img src="https://img-blog.csdnimg.cn/385ad5e903ce4630918a9d01d9e0677a.png" alt="">

然后我们发现了乱码问题，乱码一般都是因为编码引起的，所以我们来查一下数据库的编码

<img src="https://img-blog.csdnimg.cn/ce81717ba4294fe98129ebebe8f38d07.png" alt="">

#### 1.3.2 Mysql编码问题解决办法

**1.修改my.cnf文件**

```
cd /etc/mysql/ #进入my.cnf文件中的目录vim my.cnf #编辑my.cnf文件

```

**2.出现`bash: vim: command not found`提示，需要安装一下vim，使用如下命令**

```
apt-get updateapt-get install vim -y

```

重新执行vim命令。

**3. 在 my.cnf文件中[mysql] 下面添加 default-character-set=utf8mb4，然后 :wq 退出。没有 [mysql] 的话就写一个。**

如下图：

<img src="https://img-blog.csdnimg.cn/6169a376a80048c6a7a164fe43c93b5b.png" alt="">

然后看一下mysql的字符集，已经变成 utf8mb4 了，这样就可以解决问题了。

<img src="https://img-blog.csdnimg.cn/592211d4fbc94caa96f97a02ac776c5d.png" alt="">

查看表格数据

<img src="https://img-blog.csdnimg.cn/6a4e089aa55c4193b6f43b80cd5adf88.png" alt="">

至此我们的问题得到了成功解决。
