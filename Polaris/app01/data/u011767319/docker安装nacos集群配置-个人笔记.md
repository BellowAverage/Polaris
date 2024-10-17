
--- 
title:  docker安装nacos集群配置-个人笔记 
tags: []
categories: [] 

---
### 使用docker 的形式集群

>  
 安装请参考 




### 创建mysql数据库

>  
 nacos集群将使用mysql 作为数据储存点  


### docker 集群启动

>  
 **记得关闭虚拟机的防火墙，不然会导致nacos jdbc连接不上docker 中的mysql** 如何关闭防火墙呢，请看我另外一篇文章： 各位也可以考虑使用官方的docker-compose 集群部署 


**配置描述（部分）：**

```
JVM_XMN: 256m  //设置年轻代大小
JVM_XMS: 512m //初始化内存
JVM_XMX: 512m //最大可用内存
MODE: cluster //模式 ：cluster（集群）standalone (单机)
MYSQL_SERVICE_DB_NAME: nacos_config //数据库名称
MYSQL_SERVICE_HOST: 192.168.1.50 //数据库主机
MYSQL_SERVICE_PASSWORD: '123456' //数据库密码
MYSQL_SERVICE_USER: root //数据库账号
NACOS_APPLICATION_PORT: '8000' //nacos应用端口
NACOS_AUTH_ENABLE: "true" //是否启用nacos身份认证
NACOS_SERVERS: xxx.xxx.xxx.xxx:8000 xxx.xxx.xxx.xxx:8001 xxx.xxx.xxx.xxx:8002 //nacos集群
NACOS_SERVER_IP: xxx.xxx.xxx.xxx //nacos主机ip
PREFER_HOST_MODE: ip //首选模式 hostname(主机模式) ip(ip模式)

```

可修改nacos启动虚拟机的配置

```
JVM_XMN: 256m
JVM_XMS: 512m
JVM_XMX: 512m

//用法
-e JVM_XMN=256m
-e JVM_XMS=512m
-e JVM_XMX=512m

```

**PREFER_HOST_MODE 两种模式 ：hostname和ip两个目录分别对应**

>  
 两种模式的配置完全不同 


**ip模式**

```
docker run -d --name nacos1
-p 8848:8848
-e MODE=cluster
-e PREFER_HOST_MODE=ip
-e NACOS_SERVERS="192.168.1.50:8848 192.168.1.50:8849"

```

**hostname模式**

```
docker run -d --name nacos1 
--hostname=nacos1 
-p 8848:8848
-e MODE=cluster
-e PREFER_HOST_MODE=ip
-e NACOS_SERVERS="nacos1:8848 nacos2:8849"

```

1.主服务节点-部署代码

```
//主服务节点

//ip
docker run -d --name nacos1 \
-p 8848:8848 \
-e MODE=cluster \
-e PREFER_HOST_MODE=ip \
-e NACOS_SERVER_IP=192.168.1.50 \
-e NACOS_APPLICATION_PORT=8848 \
-e NACOS_SERVERS="192.168.1.50:8848 192.168.1.50:8849" \
-e SPRING_DATASOURCE_PLATFORM=mysql \
-e MYSQL_SERVICE_HOST=192.168.1.50 \
-e MYSQL_SERVICE_DB_NAME=nacos_config \
-e MYSQL_SERVICE_USER=root \
-e MYSQL_SERVICE_PASSWORD=root \
-e MYSQL_SERVICE_PORT=3306 \
nacos/nacos-server

//hostname
docker run -d --name nacos1 \
--hostname=nacos1 \
-p 8848:8848 \
-e MODE=cluster \
-e PREFER_HOST_MODE=hostname \
-e NACOS_SERVER_IP=192.168.1.50 \
-e NACOS_APPLICATION_PORT=8848 \
-e NACOS_SERVERS="nacos1:8848 nacos1:8849" \
-e SPRING_DATASOURCE_PLATFORM=mysql \
-e MYSQL_SERVICE_HOST=192.168.1.50 \
-e MYSQL_SERVICE_DB_NAME=nacos_config \
-e MYSQL_SERVICE_USER=root \
-e MYSQL_SERVICE_PASSWORD=root \
-e MYSQL_SERVICE_PORT=3306 \
nacos/nacos-server


//加日志映射
-v /root/nacos/config/custom.properties:/home/nacos/init.d/custom.properties \
-v /root/nacos/logs:/home/nacos/logs \


```

2.从服务节点部署

```
//ip
docker run -d --name nacos1 \
-p 8849:8849 \
-e MODE=cluster \
-e PREFER_HOST_MODE=ip \
-e NACOS_SERVER_IP=192.168.1.50 \
-e NACOS_APPLICATION_PORT=8849 \
-e NACOS_SERVERS="192.168.1.50:8848 192.168.1.50:8849" \
-e SPRING_DATASOURCE_PLATFORM=mysql \
-e MYSQL_SERVICE_HOST=192.168.1.50 \
-e MYSQL_SERVICE_DB_NAME=nacos_config \
-e MYSQL_SERVICE_USER=root \
-e MYSQL_SERVICE_PASSWORD=root \
-e MYSQL_SERVICE_PORT=3306 \
nacos/nacos-server

//hostname
docker run -d --name nacos2 \
-p 8849:8849 \
-e MODE=cluster \
-e PREFER_HOST_MODE=hostname \
-e NACOS_SERVER_IP=192.168.1.50 \
-e NACOS_APPLICATION_PORT=8849 \
-e NACOS_SERVERS="nacos1:8848 nacos2:8849" \
-e SPRING_DATASOURCE_PLATFORM=mysql \
-e MYSQL_SERVICE_HOST=192.168.1.50 \
-e MYSQL_SERVICE_DB_NAME=nacos_config \
-e MYSQL_SERVICE_USER=root \
-e MYSQL_SERVICE_PASSWORD=root \
-e MYSQL_SERVICE_PORT=3306 \
nacos/nacos-server

//加日志映射
-v /root/nacos/config/custom.properties:/home/nacos/init.d/custom.properties \
-v /root/nacos/logs:/home/nacos/logs \
nacos/nacos-server


```

**结束（ip模式）**：

>  
 这里就装了两个，官方建议3个集群 8848 


<img src="https://img-blog.csdnimg.cn/20210403170420649.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

>  
 8849 


<img src="https://img-blog.csdnimg.cn/20210403170507835.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
