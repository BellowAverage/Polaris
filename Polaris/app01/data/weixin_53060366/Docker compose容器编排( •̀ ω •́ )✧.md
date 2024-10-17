
--- 
title:  Docker compose容器编排( •̀ ω •́ )✧ 
tags: []
categories: [] 

---
## Docker compose容器编排



#### 文章目录
- - <ul><li>- <ul><li>- - - - <ul><li>- - <ul><li>- - - - 


### compose简介

#### compose是啥？

Compose 是用于定义和运行多容器 Docker 应用程序的工具。通过 Compose，您可以使用 YML 文件来配置应用程序需要的所有服务。然后，使用一个命令，就可以从 YML 文件配置中创建并启动所有服务。
- Docker-Compose项目是Docker官方的开源项目，负责实现对Docker容器集群的快速编排。- Docker-Compose将所管理的容器分为三层，分别是工程（project），服务（service）以及容器（container）。- Docker-Compose运行目录下的所有文件（docker-compose.yml，extends文件或环境变量文件等）组成一个工程，若无特殊指定工程名即为当前目录名。- 一个工程当中可包含多个服务，每个服务中定义了容器运行的镜像，参数，依赖。一个服务当中可包括多个容器实例，Docker-Compose并没有解决负载均衡的问题，因此需要借助其它工具实现服务发现及负载均衡。
**Compose 使用的三个步骤：**
- 使用 Dockerfile 定义应用程序的环境。- 使用 docker-compose.yml 定义构成应用程序的服务，这样它们可以在隔离环境中一起运行。- 最后，执行 docker-compose up 命令来启动并运行整个应用程序。
#### 什么是YML文件？

YAML是一种标记语言很直观的数据序列化格式，非常适合用来表达或者编辑数据结构、各种配置文件、文件大纲等，例如：许多电子邮件标题格式和YAML非常接近。

**文件格式以及编写注意事项：**
- 大小写敏感- 使用缩进表示层级关系- 缩进时不允许使用Tab键，只允许使用空格缩进，使用缩进表示层级关系- 通常开头缩进2个空格，缩进的空格数不重要，只要相同层级的元素左对齐即可- 字符后缩进一个空格，如冒号、逗号、横杆- 用#号注释- 如果包含特殊字符用单引号引起来- 布尔值必须用引号括起
**docker-compose.yml** 的配置案列如下：

```
# yaml 配置实例
version: '3'    #版本
services:       #服务
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
      - logvolume01:/var/log
    links:
      - redis
  redis:
    image: redis
volumes:          #其他配置（如：挂载，网络，）
  logvolume01: {<!-- -->}

```

#### Docker compose的应用环境：
- 使用一个Dockerfile模板文件，可以让用户很方便的定义一个单独的应用容器。在工作中，经常会碰到需要多个容器相互配合来完成某项任务的情况。例如要实现一个Web项目，除了Web服务容器本身，往往还需要再加上后端的数据库服务容器，甚至还包括负载均衡容器等。- Compose允许用户通过一个单独的docker-compose.yml模板文件（YAML格式）来定义一组相关联的应用容器为一个项目（project）。- Docker-Compose项目由Python编写，调用Docker服务提供的API来对容器进行管理。因此，只要所操作的平台支持Docker API，就可以在其上利用Compose来进行编排管理。
#### 安装 compose

在使用Docker compose之前我们一定要先有docker 引擎，就是有docker 环境；

Linux 上我们可以从 Github 上下载它的二进制包来使用，最新发行的版本地址：https://github.com/docker/compose/releases。

运行以下命令以下载 Docker Compose 的当前稳定版本：

```
curl -L "https://github.com/docker/compose/releases/download/1.21.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
#或者这个
curl -L https://github.com/docker/compose/releases/download/1.24.0-rc3/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
#给与可执行权限
chmod +x /usr/local/bin/docker-compose
#创建软连接
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
#测试是否安装成功
docker-compose --version

```

##### Docker compose配置常用字段：

|字段|描述
|------
|build dockerfile context|指定Dockerfile文件名构建镜像上下文路径
|image|指定镜像
|command|执行命令，覆盖默认命令
|container name|指定容器名称，由于容器名称是唯一的，如果指定自定义名称，则无法scale
|deploy|指定部署和运行服务相关配置，只能在swarm模式适用
|environment|添加环境变量
|networks|添加网络
|ports|暴露容器端口，与-p相同，但端口不能低于60
|volumes|挂载宿主机路径或命令卷
|restart|重启策略，默认no,always,no-failure,unless-stoped
|hostname|容器主机名

##### Docker compose常用命令：

**基本的命令格式：**

docker-compose [选项] [命令] [参数]

|字段|解释
|------
|build|重新构建服务
|ps|列出容器
|up|创建和启动容器
|exec|在容器里面执行命令
|scale|指定一个服务容器启动数量
|top|显示容器进程
|logs|查看容器输出
|down|删除容器，网络，数据卷，镜像
|stop/start/restart|停止/启动/重启服务

### 部署Docker-compose

##### 1、准备依赖文件

<img src="https://img-blog.csdnimg.cn/76b07688fd96424b802d2bc8b2e6dce8.png#pic_center" alt="在这里插入图片描述">

```
#到opt目录下创建文件夹
cd /opt
mkdir compose
cd compose
mkdir nginx
cd nginx
#导入nginx源码包
vim Dockerfile
FROM centos:7
RUN yum -y update
RUN yum -y install pcre-devel zlib-devel gcc gcc-c++ make
RUN useradd -M -s /sbin/nologin nginx
ADD nginx-1.12.2.tar.gz /usr/local/src
WORKDIR /usr/local/src/nginx-1.12.2
RUN ./configure \
--prefix=/usr/local/nginx \
--user=nginx \
--group=nginx \
--with-http_stub_status_module &amp;&amp; make &amp;&amp; make install
ENV PATH /usr/local/nginx/sbin:$PATH
VOLUME ["/usr/local/nginx/html"]
EXPOSE 80
RUN echo "daemon off;" &gt;&gt; /usr/local/nginx/conf/nginx.conf
CMD nginx

```

##### 2、准备站点页面

```
cd /opt/compose
mkdir www
vim www/index.html
this is nginx test web!

```

##### 3、配置Docker-compose.yml文件

```
cd /opt/compose
vim docker-compose.yml
ersion: "3"
services:
  nginx:
    hostname: nginx
    build:
      context: ./nginx
      dockerfile: Dockerfile
    ports:
      - 1216:80
      - 1217:443
    networks:
      - mynginx
    volumes:
      - ./wwwroot:/usr/local/nginx/html
networks:
  mynginx:

```

##### 4、启动docker-compose ，生成镜像容器；

```
docker-compose up -d
#查看服务容器
docker-compose ps

```

<img src="https://img-blog.csdnimg.cn/966ea9af24d24753b2327c30c12cb156.png#pic_center" alt="在这里插入图片描述">

##### 5、测试访问

<img src="https://img-blog.csdnimg.cn/6fa9f6250b7e409bb0d61fcc36841805.png#pic_center" alt="在这里插入图片描述">
