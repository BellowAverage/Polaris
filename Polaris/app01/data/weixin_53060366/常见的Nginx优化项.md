
--- 
title:  常见的Nginx优化项 
tags: []
categories: [] 

---
### 常见的Nginx优化项

在对Nginx进行优化前，我们需要部署好Nginx服务。

下面我们列举一些常见的Nginx优化项。

#### 1、隐藏版本号：

**查看版本号：**

```
curl -I http://192.168.111.10

```

<img src="https://img-blog.csdnimg.cn/9cef798dcec342e9b2f0f730d8a06fb9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LyK5rKz5paw5p2R,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

**隐藏版本信息：**

##### （1）修改配置文件：

```
1、#修改配置文件
vim /usr/local/nginx/conf/nginx.conf
http {<!-- -->
    include       mime.types;
    default_type  application/octet-stream;
    server_tokens off;                              #添加，关闭版本号
    ......
}

2、#重启nginx
systemctl restart nginx

3、#查看版本是否被隐藏
curl -I http://192.168.111.10

```

<img src="https://img-blog.csdnimg.cn/980c1b937a8e43a1b7a6ea3030218ae9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LyK5rKz5paw5p2R,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/845ad7a47bb34345b2d3226ae3b12c9b.png#pic_center" alt="在这里插入图片描述">

##### （2）修改源码文件，重新编译：

```
1. #停止nginx服务
systemctl stop nginx.service
2. #切换至安装目录
cd /opt/nginx-1.12.0/
3. #切换至内核目录
cd src/core/

4. #进入配置文件
vim nginx.h
#define NGINX_VERSION      "swl"
#define NGINX_VER          "swl/" NGINX_VERSION

5. #重新编译
cd /opt/nginx-1.12.0
./configure \
--prefix=/usr/local/nginx \
--user=nginx \
--group=nginx \
--with-http_stub_status_module

6. #安装
make &amp;&amp; make install -j2

7. #将配置文件下的之前关闭版本信息开启
vim /usr/local/nginx/conf/nginx.conf
server_tokens on;

8. #重启nginx
systemctl restart nginx

9. #查看版本信息
curl -I http://192.168.111.10

```

#### 2、修改用户与组：

```
1. #修改配置文件
vim /usr/local/nginx/conf/nginx.conf

user  lisi lisi;  #取消注释，修改用户为 lisi ,组为 lisi

2. #创建非登录用户
useradd -s /sbin/nologin lisi

3. #重启服务
systemctl restart nginx

4. #查看是否修改成功
ps aux | grep nginx

```

<img src="https://img-blog.csdnimg.cn/848c9f082f054bf7b4c00791d0008939.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/3f62e419049d4cd9b3e412b2e9b4b7e1.png#pic_center" alt="在这里插入图片描述">

#### 3、设置缓存时间：

当nginx将网页数据返回给客户端后，可设置缓存时间，以方便在日后进行相同内容的请求时直接返回，避免重复请求，加快了访问速度一般针对静态网页设置，对动态网页不设置缓存时间。

```
1. #修改配置文件
vim /usr/local/nginx/conf/nginx.conf
        #添加以下内容
        location / {<!-- -->
            root   html;
            index  index.html index.htm test.html;
            expires 1d;
        }


2. #重启服务
systemctl restart nginx.service 

3.#在网页中查看服务
http://192.168.111.10/test.html

```

<img src="https://img-blog.csdnimg.cn/c0d1db54695e466da45ea25bb3df0c62.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c99905c7bec843d5822abadd10b8db45.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LyK5rKz5paw5p2R,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

#### 4、日志分割：

随着Nginx服务的应用，产生的日志也会逐渐增加，为了方便掌握Nginx的运行状态，需要时刻关注Nginx日志文件。太大的日志文件对监控是一个大灾难，不便于分析排查，需要定期的进行日志文件的切割。

下面我们可以写个脚本来对Nginx日志进行分割：

```
1. #写脚本
vim /usr/local/nginx/nginx_log.sh 

#!/bin/bash
#this is for divide nginx log
d=$(date +%F -d -1day)                                       #显示前一天的时间
path="/var/log/nginx"   
pid="/usr/local/nginx/logs/nginx.pid"

[ -d $path ] ||mkdir -p $path                                #创建日志文件目录
mv /usr/local/nginx/logs/access.log ${path}/www.yxp.com-$d   #移动并重命名日志文件
kill -USR1 $(cat $pid)                                       #重建新日志文件
find $path -mtime +30 -delete                                #删除30天之前的日志文件

2. #赋予权限
chmod +x /usr/local/nginx/nginx_log.sh 

3. #计划任务
[root@localhost nginx]#crontab -e
30 1 * * * /usr/local/nginx/nginx_log.sh

```

<img src="https://img-blog.csdnimg.cn/e0245f0b57b44420b4016fec358f678e.png#pic_center" alt="在这里插入图片描述">

#### 5、连接超时：

HTTP有一个KeeepAlive模式，它告诉web服务器在处理完一个请求后保持这个TCP连接的打开状态。 若接受的来自客户端的其他请求，服务端会利用这个未被关闭的连接，而不需要再建立一个连接。 KeepAlive 在一段时间内保持打开状态，它们会在这段时间内占用资源，占用过多就会影响性能。

```
vim /usr/local/nginx/conf/nginx.conf
http {<!-- -->
......
     keepalive_timeot 65 180;
	 client_header_timeout 80;
	 client_body_timeout 80;
......
}
systemctl restart nginx


```

<img src="https://img-blog.csdnimg.cn/a7e268bf3cc8484694f68b2fe62e1634.png#pic_center" alt="在这里插入图片描述">

#### 6、更改进程数：

在高并发场景，需要启动更多的Nginx进程以保证快速响应，以处理用户的请求，避免造成阻塞。

```
1. #统计cpu核数
cat /proc/cpuinfo |grep processor|wc -l
或
cat /proc/cpuinfo |grep -c processor

2. #查看目前有的核数
ps -aux |grep nginx

3. #修改 Nginx 的配置文件worker_processes 参数，一般设为 CPU 的个数或者核数，在高并发的情况下可设置为 CPU 个数或者核数的 2 倍，可以查看 CPU 的核数以确定参数。
vim /usr/local/nginx/conf/nginx.conf
worker_processes 2;                 #修改为核数相同或者2倍
worker_cpu_affinity 01 10;          #设置每个进程由不同cpu处理，进程数配为4时0001 0010 0100 1000
4. #重启服务并查看
systemctl restart nginx.service
#查看nginx主进程中包含几个子进程
ps aux |grep nginx

```

<img src="https://img-blog.csdnimg.cn/d21719a0d4b845e093a265ad17ea36db.png#pic_center" alt="在这里插入图片描述">

#### 7、网页压缩：
- Nginx的ngx_http_gzip_module压缩模块提供对文件内容压缩的功能- 允许Nginx服务器将输出内容在发送客户端之前进行压缩，以节约网站带宽，提升用户的访问体验，默认已经安装可在配置文件中加入相应的压缩功能参数对压缩性能进行优化。
```
vim /usr/local/nginx/conf/nginx.conf
http {<!-- -->
......
   gzip on;                #取消注释，开启gzip压缩功能
   gzip_min_length 1k;     #最小压缩文件的大小
   gzip_buffers 4 64k;     #压缩缓冲区，大小为4个64k缓冲区
   gzip_http_version 1.1;  #压缩版本（默认1.1，前端如果是squid2.5请使用1.0）
   gzip_comp_level 6;      #压缩比率
   gzip_vary on;           #支持前端缓存服务器存储压缩页面
   gzip_types text/plain text/javascript application/x-javascript text/css text/xml application/xml application/xml+rss image/jpg image/jpeg image/png image/gif application/x-httpd-php application/javascript application/json;  #压缩类型，表示哪些网页文档启用压缩功能
}  

cd /usr/local/nginx/html
先将game.jpg文件传到/usr/local/nginx/html目录下
vim index.html
&lt;img src="game.jpg"/&gt;           #网页中插入图片
#重启Nginx
systemctl restart nginx

在Linux系统中，打开火狐浏览器，右击点查看元素
选择网络 ---&gt; 选择 HTML、WS、其他
访问 http://196.168.111.10 ，双击200响应消息查看头包含 Content-Encoding：gzip

```

#### 8、fpm参数优化：

```
vim /usr/local/php/etc/php-fpm.conf 
pid = run/php-fpm.pid

vim /usr/local/php/etc/php-fpm.d/www.conf
pm = dynamic                    # 96行，fpm进程启动方式，动态的
pm.max_children=20              #107行，fpm进程启动的最大进程数
pm.start_servers = 5            #112行，动态方式下启动时默认开启的进程数，在最小和最大之间
pm.min_spare_severs = 2         #117行，动态方式下最小空闲进程数
pm.max_spare_severs = 8         #122行，动态方式下最大空闲进程数

kill -USR2 `cat /usr/local/php/var/run/php-fpm.pid`   #重启php-fpm 
netstat -anpt | grep 9000

```
