
--- 
title:  1Panel面板容器无法使用localhost、127.0.0.1配置链接的问题说明及解决办法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解1panel容器面板创建运行环境后无法通过localhost、127.0.0.1配置链接的问题说明及解决办法。 日期：2024年1月8日 作者：任聪聪 (rccblogs.com) 


### 报错现象：

mysql：报错信息一览

```
SQLSTATE[HY000] [2002] Connection refused

```

redis报错：

```
Connection refused [tcp://127.0.0.1:6379]

```

#### 1.使用localhost 报错无法链接redis、mysql。

#### 2.使用127.0.0.1报错无法链接redis、mysql。

### 主要原因：

1panel的运行环境为docker创建的容器，故此我们无法通过localhost、127.0.0.1进行直接访问和使用mysql、redis、memache等服务。

这是由于docker每个容器都是单独的一个ip造成的，故此每个容器环境中的127.0.0.1和localhost都是独立的，就相当于两个世界那样，完全无法进行联通。

### 解决办法：

如果使用公网ip、内网ip端是可以进行访问的。但是由于公网访问会造成延迟、内网ip会在容器重启后进行变化，故此不建议通过这两种方式进行解决。

#### 使用容器名称配置连接信息，有效解决办法。

如容器名称如下类型： <img src="https://img-blog.csdnimg.cn/direct/db21b02a78964e2a9e8f0a1d34b06cdb.png" alt="在这里插入图片描述"> 复制容器名称并在你的网站配置文件host处填写替换localhost、127.0.0.1：

```
DB_HOST=1Panel-mysql-HROs

```

配置容器名称后再次连接数据库，你会发现后续重启容器和服务器都不需要重新填写配置信息。redis和其他数据库或服务也是如此配置，使用容器名称进行连接。
