
--- 
title:  Docker基础，安装Tomcat、Mysql、Redis、Nginx和FTP 
tags: []
categories: [] 

---
## 一、何为Docker?

Docker是一个开源的应用容器引擎，基于Go语言并遵从Apache2.0协议开源。Docker可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的Linux机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口，更重要 的是容器性能开销极低。

Docker支持软件便于成一个镜像；然后在镜像中各种软件做好配置，将镜像发布出去，其他使用者可以直接使用这个镜像。运行中的这个镜像称为容器，容器启动时非常快的，类似windows里面的ghost操作系统，安装好了以后什么都有了。

## 二、核心概念

**docker主机（Host**）:安装了Docker程序的机器（Docker直接安装在操作系统之上）；

**docker客户端（Client）**：连接docker主机进行操作；

**docker仓库（Registry）**:用来保存各种打包好的软件镜像；

**docker镜像（Images）**:软件打包好的镜像，放在docker仓库中；

**docker容器（Container）:**镜像启动后的实例成为一个容器，独立运行的一个或一组应用；

### 2.1卸载与重装

重新安装前卸载旧版docker(本机已经安装旧版,故卸载后重新安装)

rpm list installed|grep docker 或者使用该命令 rpm -qa|grep docker //查看已经安装的docker安装包,列出入校内容 docker.x86_64 2:1.12.6-16.el7.centos @extras  docker-client.x86_64 2:1.12.6-16.el7.centos @extras  docker-common.x86_64 2:1.12.6-16.el7.centos @extra 2.分别删除 yum -y remove docker.x86_64 yum -y remove docker-client.x86_64 yum -y remove docker-common.x86_64 3.删除docker镜像 rm -rf /var/lib/docker 重新安装

3.1:yum update //确保yum包最新 3.2:yum install -y yum-utils             //apt-get install       // apt install yum   //apt-get install -y docker.io 查询是否有device-mapper-persistent-data包(rpm -qa|grep device-mapper-persistent-data,如果有则不需安装 ) ,如果没有安装,执行命令: yum install -y device-mapper-persistent-data 查询是否有lvm2包(rpm -qa|grep lvm2,如果有则不需安装 ) ,如果没有安装,执行命令: yum install -y lvm2 3.3:yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo //注意,以上为设置yum源,从Docker官方地址下载安装包 3.4:yum list docker-ce --showduplicates | sort -r //查看仓库中所有的docker版本 3.5:yum install docker-ce(默认安装)或 yum install docker-ce-17.12.0.ce(注:17.12.0是版本号,可根据列表选择)

设置docker开机自动启动和启动服务

3.6[root@localhost softs]# systemctl enable docker

3.7[root@localhost softs]# systemctl start docker

## 三、使用docker步骤

镜像加速器：

### 3.1安装Docker

1.查看centos版本：（Docker要求CentOs系统的内核版本高于3.10）

<img alt="" class="has" height="40" src="https://img-blog.csdnimg.cn/20200202190121945.png" width="320">

2.安装Docker:

<img alt="" class="has" height="24" src="https://img-blog.csdnimg.cn/20200202190410304.png" width="282">

<img alt="" class="has" height="291" src="https://img-blog.csdnimg.cn/20200202190523147.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="739">

<img alt="" class="has" height="155" src="https://img-blog.csdnimg.cn/20200202190630201.png" width="617">安装成功!

3.启动docker

<img alt="" class="has" height="56" src="https://img-blog.csdnimg.cn/20200202191026153.png" width="483">

用虚拟机测试Docker的时候 报了个错误：**Job for docker.service failed because the control process exited with error code. See “systemctl status docker.service” and “journalctl -xe” for details.** 然后Docker就是启动不起来

查了一些解决方法 有的说daemon.json的配置错了 我从未配置过daemon.json 打开一看 里面是空的

## 解决方法：

修改`/etc/sysconfig/docker`文件

**将`OPTIONS='--selinux-enabled --log-driver=journald --signature-verification=false'` 修改为`DOCKER_OPTS="--storage-driver=devicemapper"`**

4.开机自启动docker

<img alt="" class="has" height="51" src="https://img-blog.csdnimg.cn/20200202191208672.png" width="764">

5.停止docker

<img alt="" class="has" height="20" src="https://img-blog.csdnimg.cn/20200202191423897.png" width="415">

### 3.2去docker仓库找到软件对应的镜像

镜像操作：
|操作|命令|说明
|检索|docker search 关键字|去docker仓库（docker hub）查找
|下载|docker pull 关键字|docker pull  mysql:5.5 （tag为软件版本）
|列表|docker images|列出当前的所有镜像
|删除|docker rmi 镜像名|删除指定的镜像id

### 3.3使用docker运行这个镜像，就会生成一个docker容器

容器操作：
|操作|命令|
|运行|docker run --name myTomcat -d tomcat:latest| --name:自定义容器名 -d:后台运行 

-d:后台运行
|当前运行的容器|docker ps|
|停止运行中的容器|docker stop 容器id|
|显示所有容器|docker ps  -a|
|删除|docker rm 容器id|
|启动容器|docker start 容器id|
|端口映射|docker run --name myTomcat -d -p 8888:8080 tomcat| 主机名端口:容器端口 
|查看容器日志|docker logs 容器id|
|进入内部|docker exec -it 容器id  /bin/bash|
|查看容器启动参数| docker inspect 容器ID|

更多命令：

### 四、安装tomcat镜像

<img alt="" class="has" height="290" src="https://img-blog.csdnimg.cn/20200203133206968.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="677">

<img alt="" class="has" height="110" src="https://img-blog.csdnimg.cn/20200203133245717.png" width="760">

访问：

<img alt="" class="has" height="369" src="https://img-blog.csdnimg.cn/20200203133441713.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

## 五、安装mysql

<img alt="" class="has" height="337" src="https://img-blog.csdnimg.cn/20200203134206472.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="716">

<img alt="" class="has" height="168" src="https://img-blog.csdnimg.cn/20200203134945156.png" width="764">

```
docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

```
docker exec -it mysqlserver /bin/bash
docker exec -it 478bbac9137b bash
```

## 六、安装redis

<img alt="" height="517" src="https://img-blog.csdnimg.cn/20200421202304677.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="808">

<img alt="" height="215" src="https://img-blog.csdnimg.cn/2020042120232728.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="497">

>  
 daemonize yes 注释起来或者 daemonize no 设置，因为该配置和 docker run 中-d 参数冲突，会导致容器一直启动失败 


```
docker run --name myredis -d -p 6379:6379 -v /usr/redis/redis.conf:/etc/redis/redis.conf -v /usr/redis/data:/data  redis:latest --restart=always redis-server /etc/redis/redis.conf




/usr/redis/redis.conf:/etc/redis/redis.conf    本机：容器内
--privileged=true                                    容器内的root拥有真正root权限，否则容器内root只是外部普通用户权限
redis-server /etc/redis/redis.conf    这个是关键配置，让redis不是无配置启动，而是按照这个redis.conf的配置启动

```

```
docker exec -it 3c9dbd98d05b  redis-cli
```

## 七、安装Nginx

```
 docker run --name nginx -p 8080:80 -v /data/docker_v/nginx/www:/home/www -d nginx

```

其中：**–name nginx 容器的名称为nginx -p 8080:80 将主机8080端口映射到容器nginx的80端口**-v /data/docker_v/nginx/www:/home/www** 将主机/data/docker_v/nginx/www目录映射到容器/home/www目录。这里/home/www是后面nginx配置文件中我们要指定的存放静态文件的位置，映射到主机目录后，直接将静态文件放到主机目录即可。 -d 后台启动 nginx 创建容器使用的镜像及版本**

```
docker exec -it nginx bash

cd /etc/nginx/

cd conf.d
```

我们看到nginx的默认配置文件为nginx.conf，但是我们不建议将个性化配置直接放在此文件中，而是在conf.d目录下创建*.conf文件，将配置信息放在这里。 我们看到conf.d下已经有一个default.conf文件，我们直接基于此文件进行配置。

**为了配置管理方便，我们将conf.d目录下的配置文件直接映射到主机目录。** 先将default.conf从容器拷贝到主机：

```
docker cp 1e312e8cd2a5:/etc/nginx/conf.d/default.conf /usr/share/java/nginx/conf.d/default.conf
```

重新创建容器：

```
docker run --name nginx -p 8080:80 -v /usr/share/java/nginx/www:/home/www -v /usr/share/java/nginx/conf.d/default.conf:/etc/nginx/conf.d/default.conf -d nginx
```

测试：在本机/usr/share/java/nginx/www/存放一张图片，直接访问即可。

## 八、Docker内部安装vim

apt-get update apt-get install vim

## 九、安装Nacos

```
docker run --name nacos -d -p 8848:8848  --privileged=true --restart=always -e JVM_XMS=512m -e JVM_XMX=512m -e MODE=standalone -v /Users/jeikerxiao/nacos:/home/nacos/logs nacos/nacos-server



docker run -it -e MODE=standalone \
-e SPRING_DATASOURCE_PLATFORM=mysql \
-e MYSQL_MASTER_SERVICE_HOST=172.117.0.1 \
-e MYSQL_MASTER_SERVICE_DB_NAME=pig_config \
-e MYSQL_MASTER_SERVICE_PORT=3306 \
-e MYSQL_MASTER_SERVICE_USER=innoergy \
-e MYSQL_MASTER_SERVICE_PASSWORD=Innoergy123! \
-v /opt/docker/nacos/logs:/home/nacos/logs \
--restart=always \
--name nacos -p 8848:8848 nacos/nacos-server



docker run -it -e MODE=standalone -e SPRING_DATASOURCE_PLATFORM=mysql -e MYSQL_MASTER_SERVICE_HOST=127.0.0.1 -e MYSQL_MASTER_SERVICE_DB_NAME=nacos-info -e MYSQL_MASTER_SERVICE_PORT=3306 -e MYSQL_MASTER_SERVICE_USER=root -e MYSQL_MASTER_SERVICE_PASSWORD=root@tomsung --restart=always --name nacos -p 8848:8848 nacos/nacos-server

docker run -it -e MODE=standalone  -e MYSQL_SERVICE_HOST=127.0.0.1 -e MYSQL_SERVICE_DB_NAME=nacos-info -e MYSQL_SERVICE_PORT=3306 -e MYSQL_SERVICE_USER=root -e MYSQL_SERVICE_PASSWORD=root@tomsung --restart=always --name nacos -p 8848:8848 nacos/nacos-server



docker  run -d -e MODE=standalone -e MYSQL_SERVICE_HOST=192.168.123.168 -e SPRING_DATASOURCE_PLATFORM=mysql -e MYSQL_SERVICE_DB_NAME=nacos_info -e MYSQL_SERVICE_PORT=3306 -e MYSQL_SERVICE_USER=root -e MYSQL_SERVICE_PASSWORD=root@tomsung --restart=always --name nacos -p 8848:8848 nacos/nacos-server
```

## 十、FTP

```
$ docker run -d -v &lt;host folder&gt;:/home/vsftpd \
                -p 20:20 -p 21:21 -p 21100-21110:21100-21110 \
                -e FTP_USER=&lt;username&gt; \
                -e FTP_PASS=&lt;password&gt; \
                -e PASV_ADDRESS=&lt;ip address of your server&gt; \
                --name ftp \
                --restart=always fauria/vsftpd


docker run --name ftp -p 21:21 -p 20:20 -p 21100-21109:21100-21109 -v /usr/share/java/nginx/www:/home/vsftpd -e FTP_USER=用户 -e FTP_PASS=密码-e PASV_ADDRESS=ip -e PASV_MIN_PORT=21100 -e PASV_MAX_PORT=21109 -d docker.io/bogem/ftp


######添加账号
#1.进入容器
docker exec -i -t vsftpd bash
#2.编辑账号
vi /etc/vsftpd/virtual_users.txt
#3.创建目录
mkdir -p /home/vsftp/账号
#4.推送到库里
/usr/bin/db_load -T -t hash -f /etc/vsftpd/virtual_users.txt /etc/vsftpd/virtual_users.db
#5.退出
exit
#6.重启容器
docker restart ftp 
```

配置文件详例：

```
# Run in the foreground to keep the container running:
background=NO

# Allow anonymous FTP? (Beware - allowed by default if you comment this out).
anonymous_enable=NO

# Uncomment this to allow local users to log in.
local_enable=YES

# Enable virtual users
guest_enable=YES

## Virtual users will use the same permissions as anonymous
virtual_use_local_privs=YES

# Uncomment this to enable any form of FTP write command.
write_enable=YES

## PAM file name
pam_service_name=vsftpd_virtual

## Home Directory for virtual users
user_sub_token=$USER
local_root=/home/vsftpd/$USER

# You may specify an explicit list of local users to chroot() to their home
# directory. If chroot_local_user is YES, then this list becomes a list of
# users to NOT chroot().
chroot_local_user=YES

# Workaround chroot check.
# See https://www.benscobie.com/fixing-500-oops-vsftpd-refusing-to-run-with-writable-root-inside-chroot/
# and http://serverfault.com/questions/362619/why-is-the-chroot-local-user-of-vsftpd-insecure
allow_writeable_chroot=YES

## Hide ids from user
hide_ids=YES

## Enable logging
xferlog_enable=YES
xferlog_file=/var/log/vsftpd/vsftpd.log
xferlog_std_format=YES

## Enable active mode
port_enable=YES
connect_from_port_20=YES
ftp_data_port=20

## Disable seccomp filter sanboxing
seccomp_sandbox=NO

### Variables set at container runtime
pasv_address=ip
pasv_max_port=21101
pasv_min_port=21100
pasv_addr_resolve=NO
pasv_enable=YES
file_open_mode=0755
local_umask=022
xferlog_std_format=NO
reverse_lookup_enable=YES
pasv_promiscuous=NO
port_promiscuous=NO

```

**1．登录和对匿名用户的设置**

<img alt="" height="344" src="https://img-blog.csdnimg.cn/20210616181935422.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

**2．设置欢迎信息**

<img alt="" height="240" src="https://img-blog.csdnimg.cn/20210616181949770.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

**3．设置用户登录后所在的目录**

<img alt="" height="139" src="https://img-blog.csdnimg.cn/20210616182000998.png" width="1200">

**4．控制用户是否允许切换到上级目录**

<img alt="" height="306" src="https://img-blog.csdnimg.cn/20210616182020675.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

<img alt="" height="186" src="https://img-blog.csdnimg.cn/20210616182034402.png" width="1200">

 **5．设置访问控制**

<img alt="" height="363" src="https://img-blog.csdnimg.cn/20210616182047418.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

**6．设置访问速度**

<img alt="" height="139" src="https://img-blog.csdnimg.cn/20210616182058719.png" width="1200">

**7．定义用户配置文件**

<img alt="" height="137" src="https://img-blog.csdnimg.cn/20210616182116191.png" width="1200">

**8．与连接相关的设置**

<img alt="" height="724" src="https://img-blog.csdnimg.cn/20210616182131224.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

**9．FTP工作方式与端口设置**

<img alt="" height="544" src="https://img-blog.csdnimg.cn/20210616182144773.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

 **10．设置传输模式**

<img alt="" height="112" src="https://img-blog.csdnimg.cn/20210616182155135.png" width="1200">

**11．设置上传文档的所属关系和权限**

<img alt="" height="332" src="https://img-blog.csdnimg.cn/20210616182206220.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

**12．日志文件**

<img alt="" height="109" src="https://img-blog.csdnimg.cn/2021061618221596.png" width="1200">

**13．其他设置**

<img alt="" height="130" src="https://img-blog.csdnimg.cn/20210616182226761.png" width="1200">
