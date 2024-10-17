
--- 
title:  Windows下nginx+tomcat的负载均衡 
tags: []
categories: [] 

---
 **一、为什么需要对Tomcat服务器做负载均衡： **

 Tomcat服务器作为一个Web服务器，其并发数在300-500之间，如果有超过500的并发数便会出现Tomcat不能响应新的请求的情况，严重影响网站的运行。另外，在访问量大的情况下，Tomcat的线程数会不断增加。由于Tomcat自身对内存的占用有控制，当对内存的占用达到最大值时便会出现内存溢出，对网站的访问严重超时等现象，这时便需要重新启动Tomcat以释放占用的内存，这样做便会阻断网站运行。 

 所以对Tomcat做负载均衡便很有必要。目前可以和Tomcat做负载均衡的主流服务器是Apache，但是Nginx由于功能多、配置简单等优点逐渐成为很多负载均衡服务器的首选。Nginx的并发数可达到50000，所以理论上可以和Tomcat以1:100的比例来配置，这样便可以很好的解决网站并发瓶颈问题。而且Nginx、apache是基于http反向代理方式，位于ISO模型的第七层应用层。直白些就是TCP UDP 和http协议的区别，Nginx不能为基于TCP协议的应用提供负载均衡。

 ** 二. 配置方法**

   1.下载相应的服务器,本人两个Tomcat的版本都采用6.0的.Nginx采用1.5.6版本

   

   **2. Nginx介绍**

      目录结构

      Nginx-

               |_  conf   配置目录

               |_  contrib

               |_  docs 文档目录

               |_  logs  日志目录

               |_  temp 临时文件目录

               |_  html 静态页面目录

               |_  nginx.exe 主程序

    window下安装Nginx极其简单，解压缩到一个无空格的英文目录即可（个人习惯，担心中文出问题），双击nginx启动，这里我安装到：D:\test目录. 若果想停止nginx，dos环境运行命令：nginx -s stop.

 nginx.conf配置

    Nginx配置文件默认在conf目录，主要配置文件为nginx.conf，我们安装在D:\server\nginx-0.8.20、默认主配置文件为D:\server\nginx-0.8.20\nginx.conf。下面是nginx作为前端反向代理服务器的配置。

 
1.  Nginx.conf代码  1.    1.    #Nginx所用用户和组,window下不指定  1.  #user  nobody;  1.    1.  #工作的子进程(通常等于CPU数量或者1倍于CPU)  1.  worker_processes  1;  1.    1.  #错误日志存放路径  1.  #error_log  logs/error.log;  1.  #error_log  logs/error.log  notice;  1.  #error_log  logs/error.log  info;  1.    1.  #指定pid存放文件  1.  #pid        logs/nginx.pid;  1.    1.    1.  events {  1.      #允许最大连接数  1.      worker_connections  1024;  1.  }  1.    1.    1.  http {  1.      include       mime.types;  1.      default_type  application/octet-stream;  1.         1.       #定义日志格式  1.      #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '  1.      #                  '$status $body_bytes_sent "$http_referer" '  1.      #                  '"$http_user_agent" "$http_x_forwarded_for"';  1.    1.      #access_log  logs/access.log  main;  1.    1.      sendfile        on;  1.      #tcp_nopush     on;  1.    1.      #keepalive_timeout  0;  1.      keepalive_timeout  65;  1.        1.      #客户端上传文件大小控制  1.      client_max_body_size 8m;  1.        1.      #gzip  on;  1.        upstream localhost {    1.                    server localhost:8080;  1.                    server localhost:8000;  1.           #根据ip计算将请求分配各那个后端tomcat，许多人误认为可以解决session问题，其实并不能。                 1.           #同一机器在多网情况下，路由切换，ip可能不同                  1.                 ip_hash;    1.                     }   1.                       1.      server {  1.          listen       9999;  1.          server_name  localhost;  1.    1.          #charset koi8-r;  1.    1.          #access_log  logs/host.access.log  main;  1.    1.          location / {  1.              root html;  1.              index index.html index.htm;  1.              #此处的 http://localhost与upstream localhost对应  1.              proxy_pass  http://localhost;  1.                1.              proxy_redirect off;  1.              proxy_set_header Host $host;  1.              proxy_set_header X-Real-IP $remote_addr;  1.              proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;  1.              client_max_body_size   10m;   1.              client_body_buffer_size  128k;  1.              proxy_connect_timeout  100;  1.              proxy_send_timeout   100;  1.              proxy_read_timeout 100;  1.              proxy_buffer_size 4k;  1.              proxy_buffers  4 32k;  1.              proxy_busy_buffers_size 64k;  1.              proxy_temp_file_write_size  64k;  1.          }  1.    1.          #error_page  404              /404.html;  1.    1.          # redirect server error pages to the static page /50x.html  1.          #  1.          error_page   500 502 503 504  /50x.html;  1.          location = /50x.html {  1.              root   html;  1.          }  1.    1.          # proxy the PHP scripts to Apache listening on 127.0.0.1:80  1.          #  1.          #location ~ \.php$ {  1.          #    proxy_pass   http://127.0.0.1;  1.          #}  1.    1.          # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000  1.          #  1.          #location ~ \.php$ {  1.          #    root           html;  1.          #    fastcgi_pass   127.0.0.1:9000;  1.          #    fastcgi_index  index.php;  1.          #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;  1.          #    include        fastcgi_params;  1.          #}  1.    1.          # deny access to .htaccess files, if Apache's document root  1.          # concurs with nginx's one  1.          #  1.          #location ~ /\.ht {  1.          #    deny  all;  1.          #}  1.      }  1.    1.    1.      # another virtual host using mix of IP-, name-, and port-based configuration  1.      #  1.      #server {  1.      #    listen       8000;  1.      #    listen       somename:8080;  1.      #    server_name  somename  alias  another.alias;  1.    1.      #    location / {  1.      #        root   html;  1.      #        index  index.html index.htm;  1.      #    }  1.      #}  1.    1.    1.      # HTTPS server  1.      #  1.      #server {  1.      #    listen       443 ssl;  1.      #    server_name  localhost;  1.    1.      #    ssl_certificate      cert.pem;  1.      #    ssl_certificate_key  cert.key;  1.    1.      #    ssl_session_cache    shared:SSL:1m;  1.      #    ssl_session_timeout  5m;  1.    1.      #    ssl_ciphers  HIGH:!aNULL:!MD5;  1.      #    ssl_prefer_server_ciphers  on;  1.    1.      #    location / {  1.      #        root   html;  1.      #        index  index.html index.htm;  1.      #    }  1.      #}  
 

 

 修改Nginx配置文件nginx.conf

 ①       在#gzip  on;后面加入下面配置: 

        
1.  upstream localhost {     1.             server localhost:8080;     1.             server localhost:8088;     1.            ip_hash;   1.  }   
 

 其中serverlocalhost:8080为第一个Tomcat的启动地址，server localhost:8088为第二个Tomcat的启动地址，ip_hash用于做session同步其实是不起作用的。

 
1.  location / {  1.            root   html;    1.            index  index.html index.htm;   1.  }    1.  改为：   1.  location / {  1.                          root html;  1.              index index.html index.htm;  1.              #此处的 http://localhost与upstream localhost对应  1.              proxy_pass  http://localhost;  1.                1.              proxy_redirect off;  1.              proxy_set_header Host $host;  1.              proxy_set_header X-Real-IP $remote_addr;  1.              proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;  1.              client_max_body_size   10m;   1.              client_body_buffer_size  128k;  1.              proxy_connect_timeout  100;  1.              proxy_send_timeout   100;  1.              proxy_read_timeout 100;  1.              proxy_buffer_size 4k;  1.              proxy_buffers  4 32k;  1.              proxy_busy_buffers_size 64k;  1.              proxy_temp_file_write_size  64k;  1.          }  
 

 **3.tomcat的配置**

   修改其中一个tomcat的server.xml配置文件即可

 第一处端口修改:

 
1.  &lt;!--  修改port端口：18006 俩个tomcat不能重复，端口随意，别太小--&gt;    1.  lt;Server port="8000" shutdown="SHUTDOWN"&gt;    
 

 
1.  &lt;!-- port="18081" tomcat监听端口，随意设置，别太小 --&gt;    1.  &lt;Connector port="18081" protocol="HTTP/1.1"     1.                 connectionTimeout="20000"     1.                 redirectPort="8443" /&gt;    
 

  第三处端口修改：

 Java代码 

 
1.  "8009" protocol="AJP/1.3" redirectPort="8443" /&gt;  
 

 ** ** 首先测试nginx配置是否正确，测试命令：nginx -t  (默认验证:conf\nginx.conf),也可以指定配置文件路径 

 <img src="https://img-blog.csdn.net/20131118124638703?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvemxfamF5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="" style="border:none; max-width:100%"> 

 最后验证配置负载均衡，启动nginx双机nginx.exe文件或者用start nginx启动 打开浏览器输入地址http://localhost:9999看到下面画面表示成功：<img src="https://img-blog.csdn.net/20131118125638359?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvemxfamF5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="" style="border:none; max-width:100%">

 此图说明已经成功跳转到tomcat 输入测试路径可以看到测试项目的首页就表示基本成功。

 <img src="https://img-blog.csdn.net/20131118131754609?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvemxfamF5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="" style="border:none; max-width:100%">      至此window下nginx+tomcat负载均衡配置结束，关于tomcat Session的问题通常是采用memcached，或者采用nginx_upstream_jvm_route，他是一个Nginx的扩展模块，用来实现基于 Cookie的 Session Sticky的功能。如果tomcat过多不建议session同步，server间相互同步session很耗资源，高并发环境容易引起Session风暴。请根据自己应用情况合理采纳session解决方案。
