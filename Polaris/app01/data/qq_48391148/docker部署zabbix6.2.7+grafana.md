
--- 
title:  docker部署zabbix6.2.7+grafana 
tags: []
categories: [] 

---
**目录**





































**################################################################# ** 

### 1、下载docker

```
yum install -y yum-utils

yum-config-manager \
&gt;     --add-repo \
&gt;     https://download.docker.com/linux/centos/docker-ce.repo


yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y

```

>  
 **设置开机自启，启动docker** 


```
[root@monitor-vm yum.repos.d]# systemctl start docker
[root@monitor-vm yum.repos.d]# systemctl enable docker
Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/doce.



[root@monitor-vm yum.repos.d]# ps aux | grep docker
root      1663  2.1  4.7 1101972 48320 ?       Ssl  04:03   0:00 /usr/bin/dockerd -H fd:// --containerd=/run/ccontainerd.sock
root      1804  0.0  0.0 112808   964 pts/1    S+   04:03   0:00 grep --color=auto docker
```

>  
 **查看docker** 


```
[root@monitor-vm yum.repos.d]# docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[root@monitor-vm yum.repos.d]# docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE

```

**################################################################# ** 

### 2、下载相关镜像文件

```
docker pull zabbix/zabbix-web-nginx-mysql:centos-6.2.7

```

```
docker pull zabbix/zabbix-server-mysql:centos-6.2.7

```

```
docker pull zabbix/zabbix-agent:centos-6.2.7

```

```
docker pull mysql:8.0.32

```

**################################################################# **  

### 3、创建一个供zabbix系统使用的网络环境

```
docker network create -d bridge zbx_net

```

**################################################################# **  

### 4、创建一个供mysql数据库存放文件的目录

```
mkdir -p /data/dockerdata/zabbix/db

```

**################################################################# **  

### 5、启动mysql容器

```
[root@monitor-vm yum.repos.d]# docker run -itd -p 3306:3306 \
&gt; --name zabbix-mysql --network zbx_net \
&gt; --restart always -v /etc/localtime:/etc/localtime -v /data/dockerdata/zabbix/db:/var/lib/mysql -e MYSQL_USER\
&gt; -e MYSQL_PASSWORD="zabbix" -e MYSQL_ROOT_PASSWORD="123qwe" mysql:8.0.32 \
&gt; --default-authentication-plugin=mysql_native_password --character-set-server=utf8 \
&gt; --collation-server=utf8_bin
eb471d309a9dd52f7e5841e6f3152e12c4b5d6c2bd00c503a446bd6995a1660a

```

**################################################################# **  

### 6、为zabbix-server创建一个持久卷

```
docker volume create zbx_vo1
```

**################################################################# **  

### 7、启动zabbix-server容器

```
[root@monitor-vm yum.repos.d]# docker run -itd -p 10051:10051 --mount source=zbx_vo1,target=/etc/zabbix \
&gt; -v /etc/localtime:/etc/localtime -v /usr/lib/zabbix/alertscripts:/usr/lib/zabbix/alertscripts \
&gt; --name=zabbix-server-mysql --restart=always --network zbx_net -e DB_SERVER_HOST="zabbix-mysql" \
&gt; -e MYSQL+DATABASE="zabbix" -e MYSQL_USER="zabbix" -e MYSQL_PASSWORD="zabbix" -e MYSQL_ROOT_PASSWORD="123qwe"
&gt; -e ZBX_JAVAGATEWAY="zabbix-java-gateway" -e ZBX_JAVAGATEWAY_ENABLE="true" \
&gt; -e ZBX_JAVAGATEWAYPORT=10052 zabbix/zabbix-server-mysql:centos-6.2.7
1f26df5d326ccaa4f069561f7a6b6983aa2e74e5675d8243a5d66977a42f0236

```

**################################################################# ** 

### 8、创建语言存放目录

```
[root@monitor-vm yum.repos.d]# mkdir -p /data/dockerdata/zabbix/db/fonts
[root@monitor-vm yum.repos.d]# cd /data/dockerdata/zabbix/db/fonts/
[root@monitor-vm fonts]# wget https://dl.cactifans.com/zabbix_docker/msty.ttf


[root@monitor-vm fonts]# ls
msty.ttf
[root@monitor-vm fonts]# mv msty.ttf DejaVuSans.ttf
[root@monitor-vm fonts]# ls
DejaVuSans.ttf

```

**################################################################# **  

### 9、启动zabbix-web容器

```
[root@monitor-vm fonts]# docker run -itd -p 8080:8080 -v /etc/localtime:/etc/localtime \
&gt; -v /data/dockerdata/zabbix/fonts/DejaVuSans.ttf:/usr/share/zabbix/assets/DejaVuSans.ttf \
&gt; --name zabbix-web-nginx-mysql --restart=always --network zbx_net -e DB_SERVER_HOST="zabbix-mysql" \
&gt; -e MYSQL_DATABASE="zabbix" -e MYSQL_USER="zabbix" -e MYSQL_PASSWORD="zabbix" -e MYSQL_ROOT_PASSWORD="123qwe"
&gt; -e ZBX_SERVER_HOST="zabbix-server-mysql" zabbix/zabbix-web-nginx-mysql:centos-6.2.7
c92c56f65c7005e7f67f2a1a77c8d91021834f1360e3ce762684c23796e47ad8

```

**################################################################# **  

### 10、启动zabbix-agent容器

```
[root@monitor-vm fonts]# docker run -itd --privileged=true --name zabbix-agent -p 10050:10050 --network zbx_net -e ZBX_HOSTNAME=rver" \
&gt; -e ZBX_SERVER_HOST="zabbix-server-mysql" -e ZBX_SERVER_PORT=10051 zabbix/zabbix-agent:centos-6.2.7
359d665e8766941d90b4b07bd06ae6afd4ce45a3c2c9f7d3f48dbf8d798f380e

```

**################################################################# ** 

### 11、访问zabbix web页面（端口8080） 

<img alt="" height="580" src="https://img-blog.csdnimg.cn/2b943bec283f4d18a25df612867ed9a7.png" width="922">

 **################################################################# ** 

### 12、docker部署grafana

#### 拉取grafana镜像

```
# 此方式，即拉取最新的镜像，等同于 docker pull grafana/grafana:lastest
docker pull grafana/grafana

# 也可以拉取指定版本的
docker pull grafana/grafana:9.3.2

```

**################################################################# ** 

#### 准备相关挂载目录及文件,授予权限

```
# /data/dockerdata/grafana/data 目录，准备用来挂载放置grafana的数据
# /data/dockerdata/grafana/plugins 目录，准备用来放置grafana的插件
# /data/dockerdata/grafana/config 目录，准备用来挂载放置grafana的配置文件


[root@monitor-vm dockerdata]# mkdir /data/dockerdata/grafana/{data,plugins,config} -p

# 给grafana数据目录授予权限

chmod 777 data/
chmod 777 plugins/
chmod 777 config/

pwd
/data/dockerdata/grafana
# ll
总用量 0
drwxrwxrwx 2 root root  25 3月  13 09:56 config
drwxrwxrwx 7 root root 101 3月  13 10:22 data
drwxrwxrwx 5 root root 101 3月  13 10:22 plugins

```

**################################################################# ** 

**准备grafana的配置文件**

>  
 **这里先启动一个临时的grafana容器，然后复制出它的配置文件 ，然后删除临时容器** 


```
[root@monitor-vm dockerdata]# docker run --name grafana-tmp -d -p 3000:3000 grafana/grafana
Unable to find image 'grafana/grafana:latest' locally
latest: Pulling from grafana/grafana
895e193edb51: Pull complete 
c2be1f0caaf8: Pull complete 
3ca3d9c55e02: Pull complete 
52780f3d3c6c: Pull complete 
aa864f3aa62f: Pull complete 
2c572284d613: Pull complete 
92772a6ef26e: Pull complete 
16eb4b4d6afe: Pull complete 
cadcd7e83b1e: Pull complete 
Digest: sha256:e4fbf663447ba23f820f44b83b9b2febf9857c12d546497ac25746428c082d2b
Status: Downloaded newer image for grafana/grafana:latest
83a2142fc56dfae88cff605dcf171532f116fec78fcd89c78e87a3c8663287a2

```

```
[root@monitor-vm dockerdata]# docker cp grafana-tmp:/etc/grafana/grafana.ini /data/dockerdata/grafana/config/
Successfully copied 55.81kB to /data/dockerdata/grafana/config/

```

```
# 移除临时容器
docker stop grafana-tmp
docker rm grafana-tmp
```

**################################################################# ** 

#### 启动grafana容器

```
docker run -d \
     -p 3000:3000 \
     --name=grafana \
     --restart=always \
     -v /etc/localtime:/etc/localtime:ro \
     -v /data/dockerdata/grafana/data:/var/lib/grafana \
     -v /data/dockerdata/grafana/plugins/:/var/lib/grafana/plugins \
     -v /data/dockerdata/grafana/config/grafana.ini:/etc/grafana/grafana.ini \
     -e "GF_SECURITY_ADMIN_PASSWORD=admin" \
     -e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource,grafana-piechart-panel" \
     grafana/grafana
```

**################################################################# ** 

#### 访问grafana页面

>  
 **启动容器的时候创建了一个临时密码admin** 
 **登录时候使用 admin/admin登录以后会重置一个密码** 


<img alt="" height="600" src="https://img-blog.csdnimg.cn/acef2f6afb5745d2a74c095923fb01aa.png" width="664">  

>  
 <img alt="" height="1200" src="https://img-blog.csdnimg.cn/8f9cc2fd03684ff6892741bad3498f43.png" width="1200">** 默认grafana是没有zabbix数据源的，需要我们自己去下载一个zabbix数据源**  


**################################################################# ** 

####  下载zabbix插件

>  
 **进入grafana容器，使用 grafana-cli plugins install 命令下载zabbix插件** 


```
[root@monitor-vm dockerdata]# docker exec -it grafana bash
bash-5.1$ 
bash-5.1$ grafana-cli plugins install alexanderzobnin-zabbix-app
? Downloaded and extracted alexanderzobnin-zabbix-app v4.2.10 zip successfully to /var/lib/grafana/plugins/alexanderzobnin-zabbix-app

Please restart Grafana after installing plugins. Refer to Grafana documentation for instructions if necessary.


```

>  
 ** 重启grafana容器，然后进入grafana的挂载目录，就能看到下载的插件了** 


```
[root@monitor-vm plugins]# docker restart grafana
grafana
[root@monitor-vm ~]# cd /data/dockerdata/grafana/
[root@monitor-vm grafana]# ls
config  data  plugins
[root@monitor-vm grafana]# cd plugins/
[root@monitor-vm plugins]# ls
alexanderzobnin-zabbix-app  grafana-clock-panel  grafana-piechart-panel  grafana-simple-json-datasource

```

>  
 **下载插件以后重启grafana容器，然后grafana web页面就可以看到zabbix插件** 


```
docker restart grafana
```

**################################################################# **

#### 在grafana页面启用zabbix插件

<img alt="" height="554" src="https://img-blog.csdnimg.cn/8ba992f4083245b8acfbc28aa56cab9f.png" width="538">

 <img alt="" height="664" src="https://img-blog.csdnimg.cn/6b4a649ea8c643c1adb0b24ca781f5d0.png" width="1200">

>  
 ** 然后添加数据源就可以看到zabbix源了** 


<img alt="" height="377" src="https://img-blog.csdnimg.cn/2d62b0ca615d439bbc7376b5399ca95b.png" width="1200">

 <img alt="" height="1200" src="https://img-blog.csdnimg.cn/819922841aa744b2b9a2a9351b053d67.png" width="1200">
