
--- 
title:  Docker部署可道云，搭建个人网盘 
tags: []
categories: [] 

---
### 

**目录**











### 前言

本文使用docker搭建可道云个人网盘，系统使用的是Debian10。



### 1、安装docker

下载docker安装脚本

```
curl -fsSL https://get.docker.com -o get-docker.sh
```

安装docker

```
sh get-docker.sh
```

执行指令查看docker信息

```
docker version
```

<img alt="" height="384" src="https://img-blog.csdnimg.cn/1bed8f6e9ebd497ab1fa892d831ac6b1.png" width="453">



### 2、配置dockers网络环境、安装镜像、运行容器

配置docker网络，这一步是为了重启机子后可道云仍能连上mysql和redis

```
docker network create --driver bridge --subnet 172.18.0.0/16 my_network
```

运行mysql容器

```
docker run -itd --name mysql-kodbox --restart=always --network=my_network --ip=172.18.0.2 -p 127.0.0.1:3306:3306 -e MYSQL_ROOT_PASSWORD=ajfkgusagifs mysql
```

运行redis容器

```
docker run -itd --name redis-kodbox --restart=always --network=my_network --ip=172.18.0.3 -p 127.0.0.1:6379:6379 redis
```

**创建证书目录并进入。我的目录为/root/kodbox_cert**

依次输入以下指令创建自签证书，要求输入的信息随意，一直按回车也可以

```
openssl genpkey -algorithm RSA -out privkey.pem
openssl req -new -key privkey.pem -out request.csr
openssl x509 -req -days 365 -in request.csr -signkey privkey.pem -out cert.pem
cat cert.pem privkey.pem &gt; fullchain.pem
```

证书目录如下

<img alt="" height="215" src="https://img-blog.csdnimg.cn/91132a3d6b814cfd9fdcb0984666cfb4.png" width="907">



**创建要挂载数据的目录，如果你有附加磁盘也可以挂载到这里，但是记得要把UUID写进/etc/fstab配置文件，这样才能每次重启自动挂载。我的目录为/mnt/kodbox**

运行可道云容器

```
docker run -d --name kodbox --network my_network --ip 172.18.0.4 --restart=always -v /mnt/kodbox:/var/www/html -v /root/kodbox_cert:/etc/nginx/ssl  -p 443:443 kodcloud/kodbox
```



### 3、进入可道云，配置数据信息

浏览器地址栏输入https://ip进入可道云配置页面

<img alt="" height="527" src="https://img-blog.csdnimg.cn/76d9e08e10ad4057a11b7e24a1d3c56b.png" width="988">



点击下一步

<img alt="" height="696" src="https://img-blog.csdnimg.cn/3898fc070dc0472d9c281c03914d3688.png" width="1200">



输入指令可以看到我们刚才配置的网络信息

```
docker ps -q | xargs -n 1 docker inspect -f '{<!-- -->{.Name}} - {<!-- -->{range .NetworkSettings.Networks}}{<!-- -->{.IPAddress}}{<!-- -->{end}}'
```

<img alt="" height="137" src="https://img-blog.csdnimg.cn/bee034d294054be2ad4dc9ae9b4103a3.png" width="1156">

依次填入信息，mysql密码在创建docker容器时候已经设置，参考自己给的参数

<img alt="" height="726" src="https://img-blog.csdnimg.cn/09a6dc5090084be9bb2ac10dbe1c88bd.png" width="852">

创建管理员账号

<img alt="" height="537" src="https://img-blog.csdnimg.cn/213631df81f048e285d80bf5330e2e1d.png" width="1200">

随后就可以愉快地使用了<img alt="" height="567" src="https://img-blog.csdnimg.cn/91468987141e45a2a3677d29240395f5.png" width="1200">




