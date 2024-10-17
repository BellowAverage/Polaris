
--- 
title:  redis 5.0.3 安装部署 
tags: []
categories: [] 

---
<img alt="" height="566" src="https://img-blog.csdnimg.cn/713345c0793b49c4a261a91c4bb9d49c.png" width="1200"> 

>  
 **本次部署方式：编译安装redis 5.0.3** 
   


>  
 **redis部署目录：/usr/local** 


```
[ec2@redis local]$ cd /usr/local
```

>  
 **下载redis 5.0.3压缩包** 


```
[ec2@redis local]$ sudo wget http://download.redis.io/releases/redis-5.0.3.tar.gz
```

>  
 **解压redis压缩包** 


```
[ec2@redis local]$ sudo tar -xvf redis-5.0.3.tar.gz
```

>  
 **进入redis目录** 


```
[ec2@redis local]$ cd redis-5.0.3/
```

>  
 **编译redis源码** 


```
[ec2@redis redis-5.0.3]$ sudo make
```

>  
 **安装redis，并指定安装路径** 


```
[ec2@redis redis-5.0.3]$ sudo make install PREFIX=/usr/local/redis
```

>  
 **将redis配置文件copy到安装路径** 


```
[ec2@redis redis-5.0.3]$ cd /usr/local/redis-5.0.3
[ec2@redis redis-5.0.3]$ sudo copy redis.conf /usr/local/redis/bin/
```

>  
 **安装完以后进入redis安装目录** 


```
[ec2@redis local]$ cd /usr/local/redis
[ec2@redis redis]$ cd bin
redis-benchmark  redis-check-aof  redis-check-rdb  redis-cli  redis-sentinel  redis-server
```

>  
 **配置redis服务** 


```
[ec2@redis multi-user.target.wants]$ cd /usr/lib/systemd/system/
[ec2@redis system]$ sudo vim redis.service
[Unit]
Description=redis-server
After=network.target
[Service]
Type=forking
ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/bin/redis.conf
PrivateTmp=true
[Install]
WantedBy=multi-user.target
```

>  
 **制作软链接** 


```
[ec2@redis system]$ sudo ln -s redis.service /etc/systemd/system/multi-user.target.wants/redis.service
```

>  
 **设置redis开机自启** 


```
[ec2@redis system]$ sudo service redis restart
Redirecting to /bin/systemctl restart redis.service
[ec2@redis system]$ ps -ef |grep redis
ec2-user 11527     1  0 03:42 ?        00:00:00 ./redis-server 0.0.0.0:6379
ec2-user 11867  5170  0 03:49 pts/0    00:00:00 grep --color=auto redis
[ec2@redis system]$ sudo systemctl enable redis
```
