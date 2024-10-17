
--- 
title:  KubeSphere安装应用-个人笔记 
tags: []
categories: [] 

---
### 可以从KubeSphere市场安装

就不做介绍了

>  
 需要持久化储存数据的，建立有状态服务。 无状态服务是不会持久化的，重启就归零 KubeSphere 创建自建应用后，创建有状态服务，但是自己应用的有状态服务不能外放端口，需要在服务哪里删除pod，在创建负载指定相关的有状态服务，就可以外放端口了 


### 安装nacos (集群)

<img src="https://img-blog.csdnimg.cn/7b740f15dbb44780a701eb31b33dcd36.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 添加application.properties 


```
# spring
fsdserver.contextPath=/nacos
server.servlet.contextPath=/nacos
server.port=8848

# 从cluster.conf配置文件中获取IP（集群模式）&lt;单节点需要注释掉&gt;
nacos.inetutils.prefer-hostname-over-ip=true

#是否自动清理不在线服务 
nacos.naming.empty-service.auto-clean=true
# 清理延迟时间
nacos.naming.empty-service.clean.initial-delay-ms=50000
# 清理间隔时间
nacos.naming.empty-service.clean.period-time-ms=30000

nacos.cmdb.dumpTaskInterval=3600
nacos.cmdb.eventTaskInterval=10
nacos.cmdb.labelTaskInterval=300
nacos.cmdb.loadDataAtStart=false

##datasource
spring.datasource.platform=mysql
 
db.num=1
db.url.0=jdbc:mysql://mysql-kqo0po.wasteland:3306/nacos?characterEncoding=utf8&amp;connectTimeout=1000&amp;socketTimeout=3000&amp;autoReconnect=true
db.user=root
db.password=root

# metrics for prometheus
#management.endpoints.web.exposure.include=*

# metrics for elastic search
management.metrics.export.elastic.enabled=false
#management.metrics.export.elastic.host=http://localhost:9200

# metrics for influx
management.metrics.export.influx.enabled=false
#management.metrics.export.influx.db=springboot
#management.metrics.export.influx.uri=http://localhost:8086
#management.metrics.export.influx.auto-create-db=true
#management.metrics.export.influx.consistency=one
#management.metrics.export.influx.compressed=true

server.tomcat.accesslog.enabled=true
server.tomcat.accesslog.pattern=%h %l %u %t "%r" %s %b %D %{<!-- -->User-Agent}i
# default current work dir
server.tomcat.basedir=

## spring security config
### turn off security
#spring.security.enabled=false
#management.security=false
#security.basic.enabled=false
#nacos.security.ignore.urls=/**

nacos.security.ignore.urls=/,/**/*.css,/**/*.js,/**/*.html,/**/*.map,/**/*.svg,/**/*.png,/**/*.ico,/console-fe/public/**,/v1/auth/login,/v1/console/health/**,/v1/cs/**,/v1/ns/**,/v1/cmdb/**,/actuator/**,/v1/console/server/**

nacos.naming.distro.taskDispatchThreadCount=1
nacos.naming.distro.taskDispatchPeriod=200
nacos.naming.distro.batchSyncKeyCount=1000
nacos.naming.distro.initDataRatio=0.9
nacos.naming.distro.syncRetryDelay=5000
nacos.naming.data.warmup=true
nacos.naming.expireInstance=true

```

>  
 添加cluster.conf 


```
#ip:port
nacos-v1-0.nacos.wasteland.svc.cluster.local:8848
nacos-v1-1.nacos.wasteland.svc.cluster.local:8848
nacos-v1-2.nacos.wasteland.svc.cluster.local:8848
其中：
nacos：创建有状态服务时的名称
v1：创建有状态服务时指定的版本
0：第0个节点
nacos.wasteland：DNS地址，即集群内部访问的域名，这个的形成规则是：创建服务时的名称.项目名称
svc.cluster.local：固定写法
8848：端口

```

<img src="https://img-blog.csdnimg.cn/29e1e16db940473a811ac4235f1efc37.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="省略简单的配置"> <img src="https://img-blog.csdnimg.cn/0128fc0b0cc742efa6496565341be124.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **增加健康检查，探针** <img src="https://img-blog.csdnimg.cn/b1322805e3564c94bba3b35414f0b57f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/17257de7a1f64b8c9b3e62797a74a734.png" alt="在这里插入图片描述">

>  
 挂载数据 文件挂载位置 


```
home/nacos/conf

```

>  
 挂载application.properties 


<img src="https://img-blog.csdnimg.cn/d194987e07cd4bdbb4fb51ad830eedf3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/318832f65ea84408b51accc19db47017.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

>  
 挂载cluster.conf，与上面同理 


直接下一步到创建就行了 <img src="https://img-blog.csdnimg.cn/e9d6f13239d7406f804c3cd05397c044.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

**单点部署，可以添加以下配置**

<img src="https://img-blog.csdnimg.cn/4e9be6cec37f42c2847f9bc1d45a1d1c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
MODE standalone

```

**字典配置**

```

#*************** Config Module Related Configurations ***************#
### If use MySQL as datasource:
spring.datasource.platform=mysql
 
### Count of DB:
db.num=1
 
### Connect URL of DB:
db.url.0=jdbc:mysql://localhost:3306/nacos?characterEncoding=utf8&amp;connectTimeout=1000&amp;socketTimeout=3000&amp;autoReconnect=true&amp;useUnicode=true&amp;useSSL=false&amp;serverTimezone=UTC
db.user.0=root
db.password.0=root

```

### 安装minio

**KubeSphere 原装的账号密码怎么查看呢，如下：** <img src="https://img-blog.csdnimg.cn/9d7c6d070d9d4c099b772138073f62cd.png" alt="在这里插入图片描述">

>  
 需要开里面的配置来看，直接点进去是加密的数据，用不了的 


<img src="https://img-blog.csdnimg.cn/5c6718e940454f5fab45be45dad9868d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/986dd6c7ae8441a8af0c3fdd28a1ef8b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6f9a0ce678cc4f18a9c832731ed44923.png" alt="在这里插入图片描述">

**放行访问** <img src="https://img-blog.csdnimg.cn/26fe66a3580c4edc9179441bf876977b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 安装seata

**先配置字典** <img src="https://img-blog.csdnimg.cn/918c824822294fe59755f3d55e2fe751.png" alt="在这里插入图片描述"> **新增 registry.conf的配置** <img src="https://img-blog.csdnimg.cn/308ca92146774b52b54c4b57be41851a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/cc8a61fe041f42a8ab9c9a1cdd89943f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 键

```
registry.conf

```

```
registry {<!-- -->
  # file 、nacos 、eureka、redis、zk、consul、etcd3、sofa
  type = "nacos"
  nacos {<!-- -->
    application = "seata-server"
    serverAddr = "nacos.wasteland:8848"
    group = "SEATA_GROUP"
    # 命名空间ID，下面会进行介绍
    namespace = "seata"
    cluster = "default"
    username = "nacos"
    password = "nacos"
  }
}
config {<!-- -->
  # file、nacos 、apollo、zk、consul、etcd3
  type = "nacos"
  nacos {<!-- -->
    serverAddr = "nacos.wasteland:8848"
    # 命名空间ID，下面会进行介绍
    namespace = "seata"
    group = "SEATA_GROUP"
    username = "nacos"
    password = "nacos"
    # 从v1.4.2版本开始，已支持从一个Nacos dataId中获取所有配置信息,你只需要额外添加一个dataId配置项
    dataId: "seataServer.properties"
  }
}

```

**指定使用1.4.2版本，latest是1.5.0以上版本配置不一样** <img src="https://img-blog.csdnimg.cn/1f2b1203c94441c8aae997f875e69b5e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **不要加健康检查，seata不支持** **配置环境变量，使用SEATA_CONFIG_NAME的形式** <img src="https://img-blog.csdnimg.cn/7c42f79483144c61be2cfe8e622e4d91.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
SEATA_CONFIG_NAME
file:/root/seata-config/registry

```

<img src="https://img-blog.csdnimg.cn/c32993f27138429d8d319d4ba9c3eaba.png" alt="在这里插入图片描述"> 配置字典：例子 <img src="https://img-blog.csdnimg.cn/41b2ffc0a96e43579321ad593e90ddbb.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/362fbd3f14e74edda91ef440f61ce6d6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
#路径
/root/seata-config/registry.conf
#子路径
registry.conf

```

<img src="https://img-blog.csdnimg.cn/8c981d230ed344ed810775290f41151a.png" alt="在这里插入图片描述"> **启动效果** <img src="https://img-blog.csdnimg.cn/d96166255a814f87a8c2dcd2dccb850d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
