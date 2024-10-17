
--- 
title:  nginx配置 
tags: []
categories: [] 

---
### nginx配置静态服务器

**在/usr/local/目录下新建upload文件**

```
配置nginx.conf文件
    listen 80;
            server_name localhost;
    location /upload/
            {
                root   /usr/local/;
                autoindex on;
            }

```

**在nginx的html文件下新建upload文件**

### 配置ssl

安装nginx ：

```
yum install nginx

```

nginx的命令：

```
service nginx start //启动
service nginx stop //关闭
service nginx restart //重启

nginx -t //检查配置是否正确
nginx -s reload //重载配置

```

先安装ssl模块：

```
yum install openssl
yum install openssl-devel

```

申请ssl证书（步骤忽略，最好申请阿里云的免费ssl）

配置

```
server {  
    listen  80;   //配置端口
    server_name test.com;  //配置域名
      
    rewrite ^(.*)$  https://$host$1 permanent;  //强制将http的访问，跳转到https的访问 
}  

#阿里云的根据阿里的配置，忽略一下配置
server {
        listen       443;                                                                       //监听端口为443
        server_name  www.localhost.cn;
  
        ssl                  on;        　　　　　　　　　　//开启ssl
        ssl_certificate      /etc/pki/tls/certs/server.crt;      //证书位置 
        ssl_certificate_key  /etc/pki/tls/certs/server.key;      //私钥位置
        ssl_session_timeout  5m;
        ssl_protocols  SSLv2 SSLv3 TLSv1;       　　　　 //指定密码为openssl支持的格式
        ssl_ciphers  HIGH:!aNULL:!MD5;              //密码加密方式
        ssl_prefer_server_ciphers   on;             //依赖SSLv3和TLSv1协议的服务器密码将优先于客户端密码
  
        location / {
            root   html;                        //根目录的相对位置
            index  index.html index.htm;
        }
    }

```

### 单页面开发的nginx配置（webpack+vue3.0）刷新报404错误的解决办法

```
例子：
location /assets {
                try_files $uri $uri/ /assets/index.html;  #地址不是index.html的重定向到index.html上，
        }


```
