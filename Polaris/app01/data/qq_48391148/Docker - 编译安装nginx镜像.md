
--- 
title:  Docker - 编译安装nginx镜像 
tags: []
categories: [] 

---
**目录**







































>  
 **按要求编译安装nginx镜像** 
 **        1、以centos7为基础镜像** 
 **        2、在里面安装好ip，vim，ping命令** 
 **        3、编译好nginx，使用我们制定的配置文件nginx.conf** 
 **        4、启动容器的时候，就启动nginx** 
 **        5、网页代码上传到容器里：** 
 **                1.直接做到镜像里面** 
 **                2.使用数据卷挂载使用** 


### 知识点1：制作镜像的常用指令

>  
 ** FROM  指定基础镜像** 
 **WORKDIR  指定工作目录，就是进入容器的时候，在哪个目录** 
 **COPY  复制宿主机里的文件或者目录到容器里的某个目录下** 
 **ADD  复制宿主机里的文件或者目录到容器里的某个目录下** 
 **RUN  就是在容器运行命令，在制作镜像的时候运行的** 
 **CMD  是容器启动的时候运行的命令** 
 **ENTRYPOINT  是启动容器的时候运行的命令** 
 **ENV  定义环境变量** 
 **        ENV NGINX_VERSION   1.19.7： 将1.19.7这个数值赋值NGINX_VERSION这个变量** 
 **EXPOSE  申明开放的端口号** 
 **ARG  传递参数  在制作镜像的时候使用** 


####  RUN和CMD/ENTRYPOINT的区别

```
RUN 指令在制作镜像的时候运行的
CMD 和ENTRYPOINT 指令是在容器启动的时候运行的

运行的时间点不一样
```

** ENTRYPOINT和CMD的区别**

>  
 **1.docker run 启动容器的时候，可以传递参数进入给ENTRYPOINT 里面的命令** 
 **2.当2者都存在的时候，CMD里的内容会成为ENTRYPOINT里的参数** 


#### 首先需要一个安装nginx的脚本

```
[root@docker1 nginx]# vim install_nginx.sh
#!/bin/bash

#解决软件的依赖关系，需要安装的软件包
yum -y install wget zlib zlib-devel openssl openssl-devel pcre pcre-devel gcc gcc-c++ autoconf automake make
#download nginx
mkdir -p /nginx
cd /nginx
#解压 下载的nginx的源码包
wget https://nginx.org/download/nginx-1.23.1.tar.gz
tar xf nginx-1.23.1.tar.gz
cd  nginx-1.23.1
#生成编译前配置工作--&gt;Makefile
./configure --prefix=/usr/local/nginx1  --with-threads --with-http_ssl_module    --with-http_stub_status_module --with-stream
#编译
make
#编译安装--》将编译好的二进制程序安装指定目录/usr/local/nginx1
make   install
```

#### 制作Dockerfile

```
[root@docker1 nginx]# cat Dockerfile 
FROM centos:7
ENV NGINX_VERSION 1.23.1
ENV AUTHOR wangsh
LABEL maintainer="wangsh&lt;1486624726@qq.com&gt;"
ARG sg

WORKDIR /sc
COPY . /sc
RUN yum install vim iputils net-tools iproute -y \
    &amp;&amp; bash /sc/install_nginx.sh
EXPOSE 80
ENV PATH=/usr/local/nginx1/sbin:$PATH
volume /scvol
CMD ["nginx","-g","daemon off;"]

```

>  
 **CMD ["nginx", "-g", "daemon off;"]  ** 
 **#在前台启动nginx程序 ，-g  daemon  off 将off值赋给daemon这个变量，告诉nginx不要在后台启动，在前台启动 daemon是守护进程--》默认在后台运行** 
 **nginx -g选项的作用是 设置一个全局的变量 ，给它赋值** 


#### 开始制作镜像

```
[root@docker1 nginx]# docker build -t scnginx:1.23.1 --build-arg sg=wang .

```

```

make[1]: Leaving directory `/nginx/nginx-1.23.1'
Removing intermediate container 50efe23aaf2e
 ---&gt; a57b1b6d5fd2
Step 9/12 : EXPOSE 80
 ---&gt; Running in fa38a092bd49
Removing intermediate container fa38a092bd49
 ---&gt; 0a72a417abb9
Step 10/12 : ENV PATH=/usr/local/nginx1/sbin:$PATH
 ---&gt; Running in 5ff0a1828dc0
Removing intermediate container 5ff0a1828dc0
 ---&gt; b9548355e534
Step 11/12 : volume /scvol
 ---&gt; Running in 9c867f0f18af
Removing intermediate container 9c867f0f18af
 ---&gt; 634e449eae22
Step 12/12 : CMD ["nginx","-g","daemon off;"]
 ---&gt; Running in 83925e13050d
Removing intermediate container 83925e13050d
 ---&gt; ec3c99645755
Successfully built ec3c99645755
Successfully tagged scnginx:1.23.1

```

#### 查看镜像是否制作成功

```
[root@docker1 nginx]# docker images
REPOSITORY   TAG            IMAGE ID       CREATED          SIZE
scnginx      1.23.1         ec3c99645755   44 seconds ago   597MB

```

#### 启动一个容器来测试镜像

```
[root@docker1 nginx]# docker run -d -p 4433:80 --name aokang-nginx-1 scnginx:1.23.1
09a5d18c088fa27d2da7ade04888ca06893eb898fc2cb5cc3d789ef92b1dd515
[root@docker1 nginx]# docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS        PORTS                                   NAMES
09a5d18c088f   scnginx:1.23.1   "nginx -g 'daemon of…"   2 seconds ago   Up 1 second   0.0.0.0:4433-&gt;80/tcp, :::4433-&gt;80/tcp   aokang-nginx-1

```

测试访问： 

<img alt="" height="572" src="https://img-blog.csdnimg.cn/fe5acad1a8d842fa8033b276a7f587e0.png" width="1200">

### 编译安装ngixn镜像升级版 

>  
 ** 升级版：** 
 **1、指定nginx.conf配置文件** 
 **        监听8007端口** 
 **2、创建容器的时候，使用卷，加载里面的网页** 
 **        2.1 创建卷 nginx_web，新建一个index.html网页文件** 
 **        2.2创建容器，加载卷** 




#### 创建一个卷

```
[root@docker1 nginx]# docker volume create nginx_web
nginx_web
[root@docker1 nginx]# docker volume ls
DRIVER    VOLUME NAME
local     nginx_web

```

#### 查看卷的地址 

```
[root@docker1 nginx]# docker volume inspect  nginx_web 
[
    {
        "CreatedAt": "2022-09-04T14:39:10+08:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/nginx_web/_data",
        "Name": "nginx_web",
        "Options": {},
        "Scope": "local"
    }
]

```

#### 进入卷目录创建一个网页文件index.html

```
[root@docker1 nginx_web]# cd /var/lib/docker/volumes/nginx_web/_data/
[root@docker1 _data]# ls
[root@docker1 _data]# vim index.html
[root@docker1 _data]# cat index.html 
welcome to sanchuang

```

#### 将刚才使用nginx镜像制作的容器的面的配置文件docker cp 过来作为我们制作镜像的指定配置文件

```
[root@docker1 nginx]# docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                   NAMES
09a5d18c088f   scnginx:1.23.1   "nginx -g 'daemon of…"   11 minutes ago   Up 11 minutes   0.0.0.0:4433-&gt;80/tcp, :::4433-&gt;80/tcp   aokang-nginx-1
fc652e8c734a   nginx            "/docker-entrypoint.…"   10 days ago      Up 3 hours      0.0.0.0:8090-&gt;80/tcp, :::8090-&gt;80/tcp   sc-nginx
[root@docker1 nginx]# ls
Dockerfile  install_nginx.sh
[root@docker1 nginx]# docker cp aokang-nginx-1:/usr/local/nginx1/conf/nginx.conf .
[root@docker1 nginx]# ls
Dockerfile  install_nginx.sh  nginx.conf

```

#### 修改配置文件，监听端口8007

```
[root@docker1 nginx]# vim nginx.conf 

listen       8007;
```

#### 新的Dockerfile

```
[root@docker1 nginx]# cat Dockerfile 
FROM centos:7
ENV NGINX_VERSION 1.23.1
ENV AUTHOR wangsh
LABEL maintainer="wangsh&lt;1486624726@qq.com&gt;"
ARG sg

WORKDIR /sc
COPY . /sc
RUN yum install vim iputils net-tools iproute -y \
    &amp;&amp; bash /sc/install_nginx.sh
EXPOSE 80
ENV PATH=/usr/local/nginx1/sbin:$PATH
volume /scvol
COPY nginx.conf /usr/local/nginx1/conf
CMD ["nginx","-g","daemon off;"]

```

#### 制作镜像 docker build

```
[root@docker1 nginx]# docker build -t scnginx1.23.2 --build-arg sg=liqiang .
make[1]: Leaving directory `/nginx/nginx-1.23.1'
Removing intermediate container 87f946a3791c
 ---&gt; 7ac89b150903
Step 9/13 : EXPOSE 80
 ---&gt; Running in 4bde77e94b80
Removing intermediate container 4bde77e94b80
 ---&gt; b778d889aa7f
Step 10/13 : ENV PATH=/usr/local/nginx1/sbin:$PATH
 ---&gt; Running in 41d2c9d3cb4f
Removing intermediate container 41d2c9d3cb4f
 ---&gt; 64ebd146fabf
Step 11/13 : volume /scvol
 ---&gt; Running in bd335aee5579
Removing intermediate container bd335aee5579
 ---&gt; 4079a62afe00
Step 12/13 : COPY nginx.conf /usr/local/nginx1/conf
 ---&gt; c1afff975d42
Step 13/13 : CMD ["nginx","-g","daemon off;"]
 ---&gt; Running in 51caa809e192
Removing intermediate container 51caa809e192
 ---&gt; e3ebd0c99bcf
Successfully built e3ebd0c99bcf
Successfully tagged scnginx1.23.2:latest

```

#### 起一个容器，使用刚才制作好的卷

```
[root@docker1 nginx]# docker run -d -p 4455:8007 --name liq-nginx-1 -v nginx_web:/usr/local/nginx1/html scnginx1.23.2
a9276c2ca1670f135c243144fd2d42d25ed9e652d1c54273d773991b30a41ec9
[root@docker1 nginx]# 
[root@docker1 nginx]# docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                               NAMES
a9276c2ca167   scnginx1.23.2    "nginx -g 'daemon of…"   6 seconds ago    Up 6 seconds    80/tcp, 0.0.0.0:4455-&gt;8007/tcp, :::4455-&gt;8007/tcp   liq-nginx-1
09a5d18c088f   scnginx:1.23.1   "nginx -g 'daemon of…"   34 minutes ago   Up 34 minutes   0.0.0.0:4433-&gt;80/tcp, :::4433-&gt;80/tcp               aokang-nginx-1
fc652e8c734a   nginx            "/docker-entrypoint.…"   10 days ago      Up 3 hours      0.0.0.0:8090-&gt;80/tcp, :::8090-&gt;80/tcp               sc-nginx
[root@docker1 nginx]# 

```

#### **测试访问**

<img alt="" height="300" src="https://img-blog.csdnimg.cn/eb6e35066f1f4eeeb49646871ff0d8ec.png" width="1200">

#### 总结 

>  
 ** 总结：** 
 **              如果有些配置是需要固定到镜像里的，在制作镜像的时候就COPY进去** 
 **                如果容器启动可以加载的，就使用卷挂载进入容器使用** 





