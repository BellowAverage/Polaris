
--- 
title:  Docker - docker镜像的制作 
tags: []
categories: [] 

---
**目录**



































### 知识点1：容器里的常见文件:

docker 容器里的文件存放在/var/lib/docker/containers目录下面，以容器id的形式存放

<img alt="" height="595" src="https://img-blog.csdnimg.cn/ce00c9a4f8ed407d93c019682cac2ac9.png" width="1200">

 

>  
 **resolv.conf ：容器里的dns服务器的地址使用的是宿主机的dns的配置** 
 **                        复制的宿主机的resolv.conf里的内容** 
 **hostname：存放主机名** 
 **hosts：存放域名解析的** 




### 知识点2：多容器之间的链接

**使用场景：**

>  
 **假设现在有一个redis容器和一个flask容器，flask容器需要访问redis容器，于是就在/etc/hosts文件里面添加一条域名映射，这样就可以通过域名来访问redis容器了** 


<img alt="" height="418" src="https://img-blog.csdnimg.cn/197c20b7206d40b5874d1046f9c2c5f0.png" width="1110">

** 示例：**

**创建一个容器，使用nginx镜像，容器名叫zhangj-nginx-1**

```
[root@docker1 lianxi]# docker run -d -p 6601:80 --name zhangj-nginx-1 nginx
78b5edcfae49dfb046e64a6ec07cf56a70c536601e2a106ebb0a755bb54396c1
[root@docker1 lianxi]# docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
78b5edcfae49   nginx     "/docker-entrypoint.…"   4 seconds ago   Up 3 seconds   0.0.0.0:6601-&gt;80/tcp, :::6601-&gt;80/tcp   zhangj-nginx-1

```

**再创建一个容器，使用nginx镜像，容器名叫zhangj-nginx-2，并链接到zhangj-nginx-1容器**

```
[root@docker1 lianxi]# docker run -d -p 6602:80 --name zhangj-nginx-2 --link zhangj-nginx-1:zhangjian  nginx
bea28a46374734a977ba069d4a0c32496e1f204f5fedc5863aec7e52ba766664

```

>  
 ** --link zhangj-nginx-1:zhangjian** 
 **           要链接的容器名：在zhangj-nginx-2容器的/etc/hosts里的名字** 


**进入/var/lib/docker/container/对应zhangj-nginx-2的容器id目录查看hosts文件，可以看到已经成功添加域名映射**

```
[root@docker1 lianxi]# cd /var/lib/docker/containers/
[root@docker1 containers]# cd bea28a46374734a977ba069d4a0c32496e1f204f5fedc5863aec7e52ba766664/
[root@docker1 bea28a46374734a977ba069d4a0c32496e1f204f5fedc5863aec7e52ba766664]# ls
bea28a46374734a977ba069d4a0c32496e1f204f5fedc5863aec7e52ba766664-json.log  hostconfig.json  mounts
checkpoints                                                                hostname         resolv.conf
config.v2.json                                                             hosts            resolv.conf.hash
[root@docker1 bea28a46374734a977ba069d4a0c32496e1f204f5fedc5863aec7e52ba766664]# cat hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.17.0.2	zhangjian 78b5edcfae49 zhangj-nginx-1
172.17.0.3	bea28a463747
[root@docker1 bea28a46374734a977ba069d4a0c32496e1f204f5fedc5863aec7e52ba766664]# 

```

### 知识点3：什么是docker镜像？

>  
 **A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.** 
 **一个docker容器镜像是一个轻量级的独立的，可执行的软件包，包含了运行应用程序所需的一切:代码、运行时、系统工具、系统库和设置。 ** 


>  
 **镜像是一个软件单元** 
 **镜像是各个不同的层组合而成的，镜像的分层思想** 
 **        最底层是基础镜像 ，base image** 
 **FROM openjdk:8-jdk  指定的基础镜像** 
 **镜像里的系统使用宿主机的内核，基础镜像有操作系统的库，** 


 <img alt="" height="434" src="https://img-blog.csdnimg.cn/53bfbd9849f64013b17735bbe568bb1e.png" width="846">

 base镜像

>  
 **base镜像是提供的最小安装的linux发行版** 


scratch ：

>  
 **        FROM scratch** 
 **        官方说明：该镜像是一个空的镜像，用于构建busybox等超小镜像，可以说实真正的从零开始构建属于自己的镜像** 




#### 如何使镜像的大小尽可能小？

>  
 **尽可能使用较小的基础镜像** 
 **减少run和copy的次数** 


>  
 **在镜像制作的过程中每执行一次RUN命令，镜像里就会多一些内容，镜像就会大一些** 
 **镜像是要加载到容器里去运行的，一个容器对应一个进程，进程是需要消耗cpu和内存的** 
 **每层里会记录发生哪些事情，有哪些数据** 
 **所以制作镜像的过程中要尽量减少RUN的次数，减少镜像的层数** 




 **####################################################################### **

### **知识点4：制作一个docker镜像**

>  
 **从镜像的制作到代码编写，启动容器** 


#### **创建一个mydocker空目录，用来存放制作镜像的一些文件 **

```
[root@docker lianxi]# cd mydocker/
[root@docker mydocker]#  vim Dockerfile
[root@docker mydocker]# ls
Dockerfile

```

#### 第1步：编辑Dockerfile

```
[root@sc-docker-server mydocker]# vim Dockerfile
FROM python:2.7-slim
WORKDIR /app # 进入到容器后进入的文件夹
ADD . /app # 将linux系统当前目录下的内容到容器的/app目录下，类似于docker cp
RUN pip install --trusted-host  pypi.python.org -r requirements.txt  # 在容器内部执行的命令
EXPOSE 80   # 暴露80端口
ENV NAME World   # 定义了环境变量NAME赋值world
ENV AUTHOR cali  # 定义了环境变量AUTHOR ccali
CMD ["python","app.py"]  # 容器启动的时候执行命令  python app.py
```

**####################################################################### **

#### 第2步：编辑requirements.txt文件

```
[root@sc-docker-server mydocker]# vim requirements.txt  # 解决依赖关系
Flask
Redis
```

**####################################################################### ** 

#### 第3步：编辑app.py文件，我们的程序文件

```
[root@sc-docker-server mydocker]# vim app.py
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "&lt;i&gt;cannot connect to Redis, counter disabled&lt;/i&gt;"

    html = "&lt;h3&gt;Hello {name}!&lt;/h3&gt;" \
           "&lt;b&gt;Hostname:&lt;/b&gt; {hostname}&lt;br/&gt;" \
           "&lt;b&gt;Visits:&lt;/b&gt; {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

**####################################################################### ** 

####  第4步：生成镜像文件

```
[root@docker mydocker]# docker build -t sc-hello_1 .

```

查看制作好的镜像

```
[root@docker /]# docker images
REPOSITORY   TAG        IMAGE ID       CREATED         SIZE
sc-hello_1   latest     e1134340fb3b   4 hours ago     159MB

```

**####################################################################### ** 

#### 第5步使用镜像，启动容器

```
[root@docker mydocker]# docker run -d -p 5544:80 --name tang-flask-1 sc-hello_1
1512dfd39b295f7812e02c727e4ddfe09c629fa7a9cdb095f5b7eb2942309072
[root@docker mydocker]# docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS             PORTS                                                    NAMES
1512dfd39b29   sc-hello_1     "python app.py"          6 seconds ago       Up 6 seconds       0.0.0.0:5544-&gt;80/tcp, :::5544-&gt;80/tcp                    tang-flask-1

```

**####################################################################### ** 

#### 第6步：访问容器的web服务

>  
 **因为redis数据库容器没有启动，flask web服务不能连接到redis数据库** 


<img alt="" height="353" src="https://img-blog.csdnimg.cn/0c1a1f77f5714edb95c4a5e85106d0d3.png" width="1017">

**####################################################################### ** 

####  第7步： 启动redis容器



```
[root@docker mydocker]# docker run -d -p 6379:6379 --name sc-redis-1 redis

```

**####################################################################### ** 

#### 第8步： 再次启动一个自己制作镜像的容器，链接到redis容器

```
[root@docker /]# docker run -d --name tang-flask-2 -p 5545:80 --link sc-redis-1:redis sc-hello_1
04a4ac0e44c29b5a4f0789d9d4ba9f181d7f8aa8f261409ea5dd79710bddcd24
[root@docker /]# docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                                    NAMES
04a4ac0e44c2   sc-hello_1     "python app.py"          4 seconds ago   Up 4 seconds   0.0.0.0:5545-&gt;80/tcp, :::5545-&gt;80/tcp                    tang-flask-2

```

**####################################################################### ** 

#### 第9步：访问容器的web服务

>  
 **curl或者chrome浏览器访问** 
 **宿主机ip：端口** 


 <img alt="" height="260" src="https://img-blog.csdnimg.cn/c9cab32141d5464099e5c1dcbb89611c.png" width="1200">

 **####################################################################### **


