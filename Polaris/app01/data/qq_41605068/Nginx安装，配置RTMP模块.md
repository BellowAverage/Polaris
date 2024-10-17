
--- 
title:  Nginx安装，配置RTMP模块 
tags: []
categories: [] 

---
## 一、什么是Nginx？

**Nginx** (engine x) 是一个高性能的和web服务器，同时也提供了IMAP/POP3/SMTP服务。Nginx是由伊戈尔·赛索耶夫为访问量第二的Rambler.ru站点（俄文：Рамблер）开发的。

Nginx是一款的 服务器/服务器及（IMAP/POP3）代理服务器，在BSD-like 协议下发行。其特点是占有内存少，能力强。

专门为性能而开发。

## 二、能干什么？

### 2.1反向代理

正向代理：在客户端（浏览器）配置代理服务器，通过代理服务器进行互联网访问。

反向代理：客户端对代理是无感知的，因为客户端不需要任何配置就可以访问，我们只需要请求发送到反向代理服务器，由反向代理服务器去选择目标服务器获取数据后，在返回给客户端，此时反向代理服务器和目标服务器就是有个服务器，暴露的是代理服务器地址，隐藏真实服务器IP地址。

### 2.2负载均衡

单个服务器解决不了，增加服务器数量，然后将请求分发到各个服务器上，将原先请求集中到单个服务器上的情况改为将请求分发到多个服务器上，将负载分发到不同的服务器，也就是我们所说的负载均衡。

### 2.3动静分离

为了加快网站的解析速度，可以把动态页面和静态页面由不同的服务器来解析，加快解析速度，降低原来单个服务器的压力。

## 三、安装

```
#nginx安装
wget http://nginx.org/download/nginx-1.12.1.tar.gz  
tar -zxvf nginx-1.12.1.tar.gz  
cd nginx-1.12.1  

# rtmp模块安装包
wget https://github.com/arut/nginx-rtmp-module/archive/master.zip
unzip master.zip

#--prefix安装目录   --add-module安装第三方模块，以rtmp为例
./configure --prefix=/etc/nginx  --add-module=nginx-rtmp-module-master    --with-http_ssl_module       
    
make 
make install  




location /fvs {
		alias  /home/images/fvs;
		autoindex off;
		proxy_connect_timeout 1200;
		proxy_read_timeout 1200; 
		proxy_send_timeout 6000; 
		proxy_buffer_size 32k;
		proxy_buffers 4 64k; 
		proxy_busy_buffers_size 128k;
		proxy_temp_file_write_size 10M; 
	}
	location /www {
		alias  /home/file;
                autoindex off;
                proxy_connect_timeout 1200;
                proxy_read_timeout 1200;
                proxy_send_timeout 6000;
                proxy_buffer_size 32k;
                proxy_buffers 4 64k;
                proxy_busy_buffers_size 128k;
                proxy_temp_file_write_size 10M;

	}

```

**安装报错：**

<img alt="" height="51" src="https://img-blog.csdnimg.cn/6d8a8c933c634b7d95398a7958724949.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

>  
 **解决方法**：系统中没有安装make环境。 **GCC——GNU编译器集合（GCC可以使用默认包管理器的仓库（repositories）来安装，包管理器的选择依赖于你使用的Linux发布版本，包管理器有不同的实现：yum是基于Red Hat的发布版本；apt用于Debian和Ubuntu；yast用于SuSE Linux等等。** 
 **运行：yum install -y gcc pcre pcre-devel openssl openssl-devel gd gd-devel** 


** 运行报错：**

<img alt="" height="135" src="https://img-blog.csdnimg.cn/9188c7aec291425390b99a486d8a36b7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

>  
 ** 解决方法**：阿里云更新了下载源地址。阿里云镜像地址 


>  
 <pre><code class="language-bash">cd /etc/yum.repos.d

rm *.repo

ls</code></pre> 
 <img alt="" height="925" src="https://img-blog.csdnimg.cn/8afffe05e2d147f08fcbec9afc149c47.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"> 
 <pre><code class="language-bash">#下载最新的
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo</code></pre> 


>  
 <img alt="" height="253" src="https://img-blog.csdnimg.cn/0d80059729a6437fa85487dd0f3e9f8d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"> 
 <pre><code class="language-bash">#生成缓存
yum makecache </code></pre> 
  就ok了！ 
 然后 
 <pre>`yum update`</pre> 


>  
  重新./configure一下就行了 


 **配置全局启动：**

1.找到安装路径：

<img alt="" height="69" src="https://img-blog.csdnimg.cn/12c125408cfb4c058bb29e560ebf76bc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_10,color_FFFFFF,t_70,g_se,x_16" width="417">

2.配置命令

>  
 vim /etc/profile 
 PATH=$PATH:/etc/nginx/sbin export PATH 
 注意：Linux严格区分大小写，所以export 为小写。 
 <img alt="" height="554" src="https://img-blog.csdnimg.cn/664dbc44468949689bbd50286e58a335.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"> 
 <pre>`source /etc/profile`</pre> 
 <img alt="" height="72" src="https://img-blog.csdnimg.cn/d3406c3141194434b50f13d97d5c6bcb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="951"> 


 

## 四、配置文件                    

### 4.1 location下的alias与root的用法

#### 4.1.1 root的用法

```
句法：	root path;
默认：	root html;
语境：	http，server，location，if in location
```

示例：

```
location ^~ /request_path/dirt/ {
    root /local_path/dirt/;
  }
```

当客户端请求 /request_path/file.ext的时候，Nginx把请求解析映射为 /local_path/dirt/ request_path/dirt/file.ext

#### 4.1.2 alias的用法

```
句法：	alias path;
默认：	-
语境：	location
```

示例：

<u>使用alias时，目录名后面一定要加"/"，不然会认为是个文件。</u>

```
location /request_path/dirt/ {
    alias /local_path/dirt/file/;
}
```

当客户端请求 /request_path/dirt/file.ext 的时候，Nginx把请求映射为 /local_path/dirt/file/file.ext 注意这里是file目录，因为alias会把location后面配置的路径丢弃掉（比如/request_path/dirt/one.html,到alias那里就剩one.html了），把当前匹配到的目录指向到指定的目录。

### 4.2上传大文件相关配置

>  
 client_max_body_size     50m;  # 限制请求体的大小，若超过所设定的大小，返回413错误，默认1m client_header_timeout    1m;  # 读取请求头的超时时间，若超过所设定的大小，返回408错误 client_body_timeout      1m; # 读取请求实体的超时时间，若超过所设定的大小，返回413错误 proxy_connect_timeout     60s; # http请求无法立即被容器(tomcat, netty等)处理，被放在nginx的待处理池中等待被处理。此参数为等待的最长时间，默认为60秒，官方推荐最长不要超过75秒 proxy_read_timeout      1m;  # http请求被容器(tomcat, netty等)处理后，nginx会等待处理结果，也就是容器返回的response。此参数即为服务器响应时间，默认60秒 proxy_send_timeout      1m; # http请求被服务器处理完后，把数据传返回给Nginx的用时，默认60秒   


###  4.3proxy_pass加/的区别

#### 4.3.1**(末尾加斜杠，**proxy_pass**中不包含路径）：**

>  
  
 location  /proxy/ {<!-- --> 
 proxy_pass http://127.0.0.1:81/; 
 } 
 **结论**：会被代理到http://127.0.0.1:81/test.html  (proxy_pass+请求url匹配的location路径后的内容） 


####  4.3.2(**末尾不加斜杠,**proxy_pass**不包含路径**)

>  
 location  /proxy/ {<!-- --> 
 proxy_pass http://127.0.0.1:81; 
 } 
 **结论**：会被代理到http://127.0.0.1:81/proxy/test.html (proxy_pass替换请求url的ip和端口） 


## 五、RTMP、HLS配置



```
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;
#error_log  logs/error.log  debug;

#pid        logs/nginx.pid;

events {
    worker_connections  1024;
}

# 添加RTMP服务
rtmp {

    server {
        listen 1935;
        application live {  
            live on;
        }
	}

}
# 添加http-flv服务
http {
    server {
        listen       8080;
        server_name	 localhost;
		
		location /live {
			flv_live on;
            chunked_transfer_encoding  on; #open 'Transfer-Encoding: chunked' response
			add_header 'Access-Control-Allow-Credentials' 'true'; #add additional HTTP header
			add_header 'Access-Control-Allow-Origin' '*'; #add additional HTTP header
			add_header Access-Control-Allow-Headers X-Requested-With;
			add_header Access-Control-Allow-Methods GET,POST,OPTIONS;
			add_header 'Cache-Control' 'no-cache';
        }
	}
}


```

```
rtmp {
    #开启一个rtmp应用服务
    server {
        listen 1935;
        chunk_size 4096; #默认流切片大小
        # create an application with rtmp
        application live {
                live on;
                record off;
                hls on;
                hls_path /opt/nginx/html/hls;
                hls_fragment 2s;
                #在接收到推流时，自动进行流格式转换并推送到本地的hls中，具体参数可以参考ffmpeg官方参数手册
                #exec ffmpeg -i rtmp://localhost/live/$name -threads 1 -c:v libx264 -profile:v baseline -b:v 350K -s 640x360 -f flv -c:a aac -ac 1 -strict -2 -b:a 56k rtmp://localhost/live360p/$name;
                #在启动nginx时就执行以下ffmpeg命令 将一个在线的rtmp转成本地的hls流（测试使用,替换成可使用的rtmp地址即可）
                exec_static ffmpeg -i rtmp://xxxxx.hd -c copy -f flv rtmp://localhost/hls360p/bk;
          }
        application hls360p {
                live on;
                hls on;
                #hls流保存位置，将该目录映射到宿主主机方便查看
                hls_path /opt/nginx/html/hls2;
                hls_fragment 2s;
        }
    }
}
 
http {
    access_log /dev/stdout combined;
    ssl_ciphers         HIGH:!aNULL:!MD5;
    ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
    ssl_session_cache   shared:SSL:10m;
    ssl_session_timeout 10m;
    server {
        listen 80;
        location /hls {
            types {
                application/vnd.apple.mpegurl m3u8;
                video/mp2t ts;
            }
            #hls的访问实际路径，例如访问http://localhost/hls/${name}.m3u8 则会访问对应目录下的m3u8文件
            alias /opt/nginx/html/hls2;
            expires -1;
            add_header Cache-Control no-cache;
            #设置允许跨域访问
            add_header Access-Control-Allow-Origin *;
        }
    }
}
```


