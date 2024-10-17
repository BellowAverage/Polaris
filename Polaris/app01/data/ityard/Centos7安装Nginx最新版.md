
--- 
title:  Centos7安装Nginx最新版 
tags: []
categories: [] 

---
### 1. 下载

直接到官网下载最新版，官网地址：`https://nginx.org/en/download.html`。

<img src="https://img-blog.csdnimg.cn/d0a8e7941bc248b582225d9fc52a97de.png" alt="">

版本说明：
- Mainline version：Mainline 是 Nginx 目前主力在做的版本，可以说是开发版- Stable version：最新稳定版，生产环境上建议使用的版本- Legacy versions：遗留的老版本的稳定版
使用命令下载：`wget -c https://nginx.org/download/nginx-1.22.1.tar.gz`。

### 2. 安装

**安装依赖**：
- gcc：`yum install gcc-c++`- PCRE：`yum install -y pcre pcre-devel`- zlib：`yum install -y zlib zlib-devel`- OpenSSL：`yum install -y openssl openssl-devel`
**解压**：`tar -zxvf nginx-1.22.1.tar.gz`

**配置**：

方式一(使用默认配置)：

```
./configure

```

方式二(自定义配置，不推荐)：

```
./configure \
--prefix=/usr/local/nginx \
--conf-path=/usr/local/nginx/conf/nginx.conf \
--pid-path=/usr/local/nginx/conf/nginx.pid \
--lock-path=/var/lock/nginx.lock \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--with-http_gzip_static_module \
--http-client-body-temp-path=/var/temp/nginx/client \
--http-proxy-temp-path=/var/temp/nginx/proxy \
--http-fastcgi-temp-path=/var/temp/nginx/fastcgi \
--http-uwsgi-temp-path=/var/temp/nginx/uwsgi \
--http-scgi-temp-path=/var/temp/nginx/scgi

```

注：将临时文件目录指定为：`/var/temp/nginx`，需要在`/var`下创建temp及nginx目录。

**编译安装** ：`make &amp;&amp; make install`

**启动停止**：

```
cd /usr/local/nginx/sbin/
./nginx 
./nginx -s stop
./nginx -s quit
./nginx -s reload

```

查看nginx进程：`ps aux|grep nginx`

**配置环境变量：**

打开配置文件：`vim /etc/profile`

在文件末尾添加如下内容：

```
export NGINX_HOME=/usr/local/nginx
export PATH=$PATH:$NGINX_HOME/sbin

```

刷新配置：`source /etc/profile`

将Nginx设置为系统服务，创建文件：`touch /lib/systemd/system/nginx.service`，打开文件`vim /lib/systemd/system/nginx.service`，添加如下配置：

```
[Unit]
Description=nginx service
After=network.target
[Service]
Type=forking
ExecStart=/usr/local/nginx/sbin/nginx
ExecReload=/usr/local/nginx/sbin/nginx -s reload
ExecStop=/usr/local/nginx/sbin/nginx -s quit
PrivateTmp=true
[Install]
WantedBy=multi-user.target

```

设置开机自启：`systemctl enable nginx`

管理Nginx命令：

```
systemctl start nginx               启动服务
systemctl stop nginx               停止服务
systemctl restart nginx             重新启动服务
systemctl list-units --type=service     查看所有已启动的服务
systemctl status nginx                查看服务当前状态
systemctl enable nginx               设置开机自启动
systemctl disable nginx               停止开机自启动

```
