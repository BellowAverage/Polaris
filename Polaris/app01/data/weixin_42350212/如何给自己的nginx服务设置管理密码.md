
--- 
title:  如何给自己的nginx服务设置管理密码 
tags: []
categories: [] 

---
**目录**











#### **1.安装Nginx编译所依赖的包**

**　　**正常centos中可以使用yum安装一下依赖包：

```
make: *** No rule to make target `build', needed by `default'. Stop.
```

 如果使用yum安装不上pcre时，可以去官网（）

下载对应的压缩包，再解压安装：

```
tar zxvf pcre-8.43.tar.gz

cd pcre-8.43

./configure

make &amp;&amp; make install
```

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/8b23ad7a06d6d825c6c41f438504a87c.gif">

如果使用yum安装OpenSSL失败是，可以去()下载OpenSSL压缩包，

解压安装：

```
tar zxvf openssl-1.0.2t.tar.gz

cd openssl-1.0.2t

./config --prefix=/usr/local/ --openssldir=/usr/local/openssl -g3 shared zlib-dynamic enable-camellia

make &amp;&amp; make install
```

测试是否可用：

```
[root@etcd01 sbin]# openssl version
OpenSSL 1.0.2k-fips  26 Jan 2017
```

如果zlib使用yum安装失败，可以去下载压缩包，解压安装：

```
tar zxvf zlib-1.2.11.tar.gz

cd zlib-1.2.11

./configure

make &amp;&amp; make install
```

#### ** 2.下载安装Nginx**
- 去官网下载Nginx： wget https://nginx.org/download/nginx-1.16.1.tar.gz- 解压安装：　　　**　**
```
tar zxvf nginx-1.16.1.tar.gz
cd nginx-1.16.1
./configure --prefix=/opt/nginx/server 
make &amp;&amp; make install
```

  这样Nginx安装的sbin，conf相关的目录就会

-在/opt/nginx/server中生成，如果不知道prefix，则默认生成到/usr/local/nginx目录下
- 测试安装是否成功：
```
[root@s1 sbin]# ./nginx -V
nginx version: nginx/1.16.1
built by gcc 4.4.6 20120305 (Red Hat 4.4.6-4) (GCC) 
built with OpenSSL 1.0.1e-fips 11 Feb 2013
TLS SNI support enabled
configure arguments: --prefix=/opt/nginx/server --with-http_stub_status_module --with-http_ssl_module
```

　　这里的 --with-http_stub_status_module --with-http_ssl_module 是配置https时需要添加的ssl模块，后面会有介绍，如果没有这两个模块使用https时会有报错：

```
nginx: [emerg] the "ssl" parameter requires ngx_http_ssl_module in /opt/nginx/server/conf/nginx.conf:37
```
- 启动Nginx：
```
cd /opt/nginx/server/sbin
./nginx
```

在启动nginx时可能会报错：

```
nginx：error while loading shared libraries: libpcre.so.1: cannot open shared object file: No such file or directory  
```

在redhat 64位机器上, nginx可能读取的pcre文件为/lib64/libpcre.so.1文件.需要建立一个软连接：

>  
 <pre>ln -s /usr/local/lib/libpcre.so.1 /lib64/ 
</pre> 


```
./nginx -t                #验证nginx.conf文件正确性
./nginx -s reload         #重新加载nginx.conf文件
./nginx -s stop           #停止Nginx服务
```
- 验证服务是否启动成功：
可以查看端口：

>  
 <pre>[root@s1 sbin]# netstat -ntlp | grep nginx
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      349/nginx: master </pre> 


```
openssl genrsa -des3 -out nginx.key 1024 #此处使用的密码是1024
```

然后他会要求你输入这个key文件的密码。

以后要给nginx使用。每次reload nginx配置时候都要你验证这个PAM密码的。



**2.然后使用openssl 根据这个key文件生成证书请求文件:**

```
openssl req -new -key nginx.key -out nginx.csr
```

以上命令生成时候要填很多东西 一个个看着写吧（可以随便，毕竟这是自己生成的证书，但是如果使用java程序访问时，需要将在输入用户名或服务器名时，输入自己的域名，不然会报找不到匹配的域名证书错误）

**3.最后根据这2个文件生成crt证书文件：**

```
openssl x509 -req -days 3650 -in nginx.csr -signkey nginx.key -out nginx.crt
```

**4.最后使用到的文件是key和crt文件。如果需要用pfx 可以用以下命令生成:**

```
openssl pkcs12 -export -inkey nginx.key -in nginx.crt -out nginx.pfx
```

#### **配置nginx https：**

需要在nginx.conf配置文件中添加：

```
server {
            listen       443 ssl;
            server_name  localhost;

            ssl_protocols SSLv2 SSLv3 TLSv1;
            #ssl_ciphers ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP;

            ssl_certificate      /opt/nginx/ssl/nginx.crt;
            ssl_certificate_key  /opt/nginx/ssl/nginx.key;
            ssl_session_cache    shared:SSL:1m;
            ssl_session_timeout  5m;
            ssl_ciphers ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP;
            ssl_prefer_server_ciphers  on;
            location / {
                proxy_pass http://httpfs/;
            }
         }
```

完整nginx.conf配置文件：

```
#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;



    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    upstream httpfs {
    server 127.0.0.1:14000;
    }

    server {
        listen       80;
        server_name  httpfs.test.com;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
          proxy_pass http://httpfs/;
     }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

    }


    # HTTPS server
    server {
        listen       443 ssl;
        server_name  httpfs.test.com;

        ssl_protocols SSLv2 SSLv3 TLSv1;
    
        ssl_certificate      ssl/nginx.crt;
        ssl_certificate_key  ssl/nginx.key;
        ssl_session_cache    shared:SSL:1m;
        ssl_session_timeout  5m;
        ssl_ciphers ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP;
        #ssl_ciphers  HIGH:!aNULL:!MD5;
            ssl_prefer_server_ciphers  on;
        location / {
            proxy_pass http://httpfs/;
        }
     }
}
```

重启nginx后，使用https访问就可以了。

```
[root@etcd01 sbin]# ./nginx -s reload
Enter PEM pass phrase:
[root@etcd01 sbin]# 

#此时会提示你需要输入密码，只有输入密码才能重启成功
```
