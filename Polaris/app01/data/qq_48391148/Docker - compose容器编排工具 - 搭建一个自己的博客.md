
--- 
title:  Docker - compose容器编排工具 - 搭建一个自己的博客 
tags: []
categories: [] 

---
 

**目录**





































场景：

**例如：我们现在需要启动10个容器，其中3个nginx，2个redis，3个mysql，1个zabbix，1个ansible       有些容器需求先启动，有容器需要后启动，在启动的时候是有先后顺序的。**

>  
 **批量启动容器，而且启动的时候容器之间是有依赖关系，需要考虑启动顺序的** 
 **编排的内容全部写到一个yaml文件里，docker 的compose根据这个yaml文件里的安排去启动容器。** 


### 知识点1：什么是 compose？

>  
 **compose 是一个容器编排工具：** 
 **        启动一个容器，进行哪些配置，例如端口，进程，卷，是否链接其他容器等** 
 **        compose 是Docker容器进行编排的工具，** 
 **Compose 是 Docker 容器进行编排的工具，定义和运行多容器的应用，可以一条命令启动多个容器，使用Docker Compose不再需要使用shell脚本来启动容器。** 


<img alt="" height="467" src="https://img-blog.csdnimg.cn/a8a685ebfac24c1d867ec509d1e23e76.png" width="1174">

**###############################################################################################**

## 知识点2：compose的安装

```
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}

 mkdir -p $DOCKER_CONFIG/cli-plugins

 curl -SL https://github.com/docker/compose/releases/download/v2.7.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
```

### 其实在家目录创建了一个目录：/root/.docker/cli-plugins

>  
  因为compose源码在github上面，所以下载速度比较慢 


### 授予可执行权限

<img alt="" height="306" src="https://img-blog.csdnimg.cn/1466831e14dd4e27ac3f48f56e0e91c3.png" width="950">

###  测试compose是否安装成功

```
[root@docker cli-plugins]# docker compose version
Docker Compose version v2.7.0
[root@docker cli-plugins]# pwd
/root/.docker/cli-plugins

```

### 知识点3：构建一个在 Docker Compose 上运行的简单 Python Web 应用程序

#### 1、为项目创建一个目录：

```
[root@docker1 /]# mkdir composetest
[root@docker1 /]# cd composetest/

```

#### 2、在项目目录中创建一个名为的文件<font face="monospace">app.py</font>

```
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
```

#### 3、在您的项目目录中创建另一个名为的文件`requirements.txt`

```
flask
redis
```

#### 4、创建一个Dockerfile

>  
 **编写一个构建 Docker 映像的 Dockerfile。该映像包含 Python 应用程序所需的所有依赖项，包括 Python 本身。** 


```
# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

>  
 - **从 Python 3.7 映像开始构建映像。**- **将工作目录设置为`/code`.**- **设置命令使用的环境变量`flask`。**- **安装 gcc 和其他依赖项**- **复制`requirements.txt`并安装 Python 依赖项。**- **向镜像添加元数据以描述容器正在侦听端口 5000**- **将项目中的当前目录复制`.`到镜像中的workdir `.`。**- **将容器的默认命令设置为`flask run`.** 


#### 5、 创建一个docker-compose.yml文件定义服务

```
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:5000"
  redis:
    image: "redis:alpine"
```

#### 6、使用compose构建程序

```
[root@docker1 composetest]# ls
app.py  docker-compose.yml  Dockerfile  requirements.txt
[root@docker1 composetest]# docker compose up

```

### 知识点4：使用compose 搭建个人博客网站

#### 1、创建一个空目录

```
[root@docker1 /]# mkdir my_wordpress
[root@docker1 /]# cd my_wordpress/

```

#### 2、创建一个`docker-compose.yml`用于启动您的 `WordPress`博客的文件和一个带有卷挂载的单独`MySQL`实例以实现数据持久性

```
services:
  db:
    # We use a mariadb image which supports both amd64 &amp; arm64 architecture
    image: mariadb:10.6.4-focal
    # If you really want to use MySQL, uncomment the following line
    #image: mysql:8.0.27
    command: '--default-authentication-plugin=mysql_native_password'
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=somewordpress
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=wordpress
      - MYSQL_PASSWORD=wordpress
    expose:
      - 3306
      - 33060
  wordpress:
    image: wordpress:latest
    ports:
      - 80:80
    restart: always
    environment:
      - WORDPRESS_DB_HOST=db
      - WORDPRESS_DB_USER=wordpress
      - WORDPRESS_DB_PASSWORD=wordpress
      - WORDPRESS_DB_NAME=wordpress
volumes:
  db_data:
```

#### 3、构建项目

```
[root@docker1 my_wordpress]# docker compose up -d
[+] Running 2/2
 ⠿ Container my_wordpress-wordpress-1  Started                                                       2.6s
 ⠿ Container my_wordpress-db-1         Started    
```

- d 表示在后台运行容器服务

docker compose ps 表示列出目前项目中的所有容器

```
[root@docker1 my_wordpress]# docker compose ps
NAME                       COMMAND                  SERVICE             STATUS              PORTS
my_wordpress-db-1          "docker-entrypoint.s…"   db                  running             3306/tcp, 33060/tcp
my_wordpress-wordpress-1   "docker-entrypoint.s…"   wordpress           running             0.0.0.0:80-&gt;80/tcp, :::80-&gt;80/tcp

```

#### 4、在浏览器中打开 WordPress

完成所需资料，然后点击安装wordpress 

<img alt="" height="992" src="https://img-blog.csdnimg.cn/175b53b91b40471086eaedf9750c046f.png" width="1200">

 <img alt="" height="641" src="https://img-blog.csdnimg.cn/c9093f47a4094530995bd6defcc272b8.png" width="1012">

 wordpress后台管理：

<img alt="" height="998" src="https://img-blog.csdnimg.cn/0cf9188d13ba47d8855fe2cda7e01832.png" width="1200">

 

 
