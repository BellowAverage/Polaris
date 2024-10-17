
--- 
title:  Centos7 使用docker安装oracle数据库（超详细） 
tags: []
categories: [] 

---
在linux中采用解压安装包的方式安装oracle非常麻烦，并且稍微不注意就会出现问题，因此采用docker来安装，下面为详细的步骤： 若不知道是否安装docker可查看这篇文章：

#### 1、拉取oracle镜像

```
docker pull registry.cn-hangzhou.aliyuncs.com/helowin/oracle_11g

```

<img src="https://img-blog.csdnimg.cn/74c12ed6049f4aa48df427a9afc30541.png" alt="在这里插入图片描述">

#### 2、查看镜像

```
docker images

```

<img src="https://img-blog.csdnimg.cn/df195b209c7a4b1f9053c498a43819d2.png" alt="在这里插入图片描述">

#### 3、创建容器

oracle是为它指定的别名，必须唯一；

```
docker run -d -p 1521:1521 --name oracle registry.cn-hangzhou.aliyuncs.com/helowin/oracle_11g

```

<img src="https://img-blog.csdnimg.cn/9c5c030a38ce4cb1966cc30e58a9e039.png" alt="在这里插入图片描述">

查看容器是否创建成功：

```
docker ps

```

<img src="https://img-blog.csdnimg.cn/4a69786045f949ad900131d3aa23ce3d.png" alt="在这里插入图片描述">

#### 4、启动容器

启动刚刚创建的容器，可以使用 oracle，也可以使用id来操作；

```
docker start oracle

```

```
[root@hecs-207177 ~]# docker start oracle
oracle

```

#### 5、进入容器并进行配置

##### 5.1 进入容器

```
docker exec -it oracle bash

```

若想切回root用户，只需使用 exit 即可： <img src="https://img-blog.csdnimg.cn/2cdfdd6b4215467fa46f96d69d95c542.png" alt="在这里插入图片描述">

##### 5.2 编辑环境变量

```
vim /etc/profile
source /etc/profile

```

在文件结尾添加如下环境变量：

```
export ORACLE_HOME=/home/oracle/app/oracle/product/11.2.0/dbhome_2
export ORACLE_SID=helowin
export PATH=$ORACLE_HOME/bin:$PATH

```

##### 5.3 运行

再次进入到容器里，此时自动切换到oracle用户，加载一下用户环境变量：source ~/.bash_profile，然后进入到oracle数据库里：sqlplus /nolog <img src="https://img-blog.csdnimg.cn/477540b71e014c0ea96cf5c28447b3d1.png" alt="在这里插入图片描述"> 至此安装完成！
