
--- 
title:  nginx详细教程 
tags: []
categories: [] 

---
### 一、nginx简介

#### 1. 概述

Nginx 是一款轻量级的 Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，在 BSD-like 协议下发行。其特点是占有内存少，并发能力强，事实上 nginx 的并发能力在同类型的网页服务器中表现较好。

#### 2. 特点
- 更快：单次请求响应更快，高并发可以更快的处理响应- 高拓展性：设计极具扩展性，由多个不同功能、不同层次、不同类型且耦合度极低的模块组成- 高可靠性：很多高流量网站都在核心服务器上大规模使用 Nginx- 低内存消耗：一般1万个非活跃的 HTTP Keep-Alive 连接在 Nginx 中仅消耗2.5MB内存- 高并发：单机支持10万以上的并发连接- 热部署：master 管理进程与 worker 工作进程的分离设计，使得 Nginx 能够支持热部署- 开源协议：使用 BSD 许可协议，免费使用，且可修改源码
#### 3. 应用场景
-  HTTP 服务器 Nginx 本身也是一个静态资源的服务器，当只有静态资源的时候，就可以使用 Nginx 来做服务器，如果一个网站只是静态页面的话，那么就可以通过这种方式来实现部署。 -  静态资源服务 静态服务器，通常会提供一个上传的功能，其他应用如果需要静态资源就从该静态服务器中获取。 -  反向代理服务 反向代理 (Reverse Proxy) 方式是指以代理服务器来接受 Internet 上的连接请求，然后将请求转发给内部网络上的服务器，并将从服务器上得到的结果返回给 Internet 上请求连接的客户端，此时代理服务器对外就表现为一个反向代理服务器。 -  负载均衡 负载均衡也是 Nginx 常用的一个功能，负载均衡其意思就是分摊到多个操作单元上进行执行，例如 Web 服务器、FTP 服务器、企业关键应用服务器和其它关键任务服务器等，从而共同完成工作任务。 -  动静分离 动静分离是让动态网站里的动态网页根据一定规则把不变的资源和经常变的资源区分开来，动静资源做好了拆分以后，我们就可以根据静态资源的特点将其做缓存操作，这就是网站静态化处理的核心思路。 
>  
 **正向代理与反向代理的区别？** 
  
 虽然正向代理服务器和反向代理服务器所处的位置都是客户端和真实服务器之间，所做的事情也都是把客户端的请求转发给服务器，再把服务器的响应转发给客户端，但是二者之间还是有一定的差异的。 
 1、**正向代理其实是客户端的代理**，帮助客户端访问其无法访问的服务器资源。**反向代理则是服务器的代理**，帮助服务器做负载均衡，安全防护等。 
 2、**正向代理一般是客户端架设的**，比如在自己的机器上安装一个代理软件。而**反向代理一般是服务器架设的**，比如在自己的机器集群中部署一个反向代理服务器。 
 3、**正向代理中，服务器不知道真正的客户端到底是谁**，以为访问自己的就是真实的客户端。而在**反向代理中，客户端不知道真正的服务器是谁**，以为自己访问的就是真实的服务器。 
 4、正向代理和反向代理的作用和目的不同。**正向代理主要是用来解决访问限制问题。而反向代理则是提供负载均衡、安全防护等作用。二者均能提高访问速度。** 


### 二、nginx安装部署

官网下载地址：

选择稳定版本进行下载；

<img alt="" height="749" src="https://img-blog.csdnimg.cn/direct/ca6316ef66504aacaee32af55c33d48e.png" width="701">
-  <h5>下载完成后，解压缩，在解压后的文件夹路径下运行cmd，使用命令进行操作，不要直接双击nginx.exe，不要直接双击nginx.exe，不要直接双击nginx.exe</h5> 
一定要在dos窗口启动，不要直接双击nginx.exe，这样会导致修改配置后重启、停止nginx无效，需要手动关闭任务管理器内的所有nginx进程，再启动才可以
- 启动nginx服务，启动时会一闪而过是正常的
```
start nginx
```
-  <h5>查看任务进程是否存在，dos或打开任务管理器都行</h5> 
```
tasklist /fi "imagename eq nginx.exe"
```

 如果都没有可能是启动报错了查看一下日志；

<img alt="" height="258" src="https://img-blog.csdnimg.cn/direct/67f51a377ad64919881a4b9b0d9e3d5d.png" width="705">

在nginx目录中的logs文件夹下error.log是日志文件 

```
2024/02/21 12:16:21 [emerg] 77964#80600: bind() to 0.0.0.0:80 failed (10013: An attempt was made to access a socket in a way forbidden by its access permissions)
```

错误为默认端口号80被占用；

修改配置文件，进入解压缩目录，直接文件夹点击进去即可，不需要从dos操作；

在conf目录下找到nginx.conf使用txt文本打开即可，找到server这个节点，修改端口号

 <img alt="" height="249" src="https://img-blog.csdnimg.cn/direct/795dff6919ed4a4784a3321e67183d3d.png" width="352">

修改完成后保存，使用以下命令检查一下配置文件是否正确，后面是nginx.conf文件的路径，successful就说明正确了；这里注意路径一定要输入正确，为D盘后面的完整路径。

```
.\nginx -t -c /nginx-1.24.0/nginx-1.24.0/conf/nginx.conf
```

<img alt="" height="132" src="https://img-blog.csdnimg.cn/direct/3e8f11037c194c8abec15d926ed71edc.png" width="1047">

如果程序没启动就直接start nginx启动，如果已经启动了就使用以下命令重新加载配置文件并重启

```
nginx -s reload
```

启动成功 

<img alt="" height="138" src="https://img-blog.csdnimg.cn/direct/af6744142f884865b058b8fa77523f91.png" width="706">

之后就打开浏览器访问刚才的域名及端口http://localhost:8080，出现欢迎页就说明部署成功了 

<img alt="" height="279" src="https://img-blog.csdnimg.cn/direct/886c4eb17a3f45a9a184982b1782e152.png" width="1171">

>  
 ps:打开任务管理器在进程中 
 看不到nginx.exe的进程（双击nginx.exe时会显示在这里），需要打开详细信息里面能看到隐藏的nginx.exe进程 
 <img alt="" height="407" src="https://img-blog.csdnimg.cn/img_convert/fad2817e580b71247780ae24b4277105.png" width="462"> 

<li> <h5>关闭nginx服务使用以下命令，同样也是一闪而过是正常的，看一下是否进程已消失即可</h5> <pre><code class="language-bash"># 快速停止
nginx -s stop
# 完整有序的关闭
nginx -s quit</code></pre> </li>
### 三、nginx配置静态资源页面

在conf目录下找到nginx.conf使用txt文本打开即可，修改主页目录，默认为nginx安装包中自带的html目录，修改成存放自己静态资源页面的文件夹路径；

<img alt="" height="246" src="https://img-blog.csdnimg.cn/direct/949ae365ba80489eb5445f3e1395b1d5.png" width="479">

之后访问http://localhost:8080，出现的页面即为自己写好的html页面啦！

在 Nginx 中，`location /` 是一个特殊的配置块，它匹配所有以 `/` 开头的请求。这意味着如果客户端发送了一个请求，路径是 `/`，或者是类似 `/path`、`/path/to/resource` 等以 `/` 开头的路径，都会被匹配到这个 `location /` 配置块。

例如：
- 请求 `http://example.com/`：匹配到根路径 `/`。- 请求 `http://example.com/path/to/resource`：同样匹配到根路径 `/`。- 请求 `http://example.com/images/logo.png`：同样匹配到根路径 `/`。
`root` 指令指定了 Nginx 在处理这个位置的请求时，应该在文件系统中查找文件的根路径。在这个配置中，`root` 指令设置为 `D:\Graduation_project\kg-course\kg3.0\kg3.0\vis`，意味着当有请求匹配到这个位置时，Nginx 将在该路径下寻找相应的文件来返回给客户端。

`index` 指令指定了当请求匹配到的路径是一个目录时，默认返回的文件。在这个配置中，`index` 指令设置为 `index.html index.htm`，意味着如果请求的路径是一个目录，Nginx 将尝试返回 `index.html` 或者 `index.htm` 文件作为默认文件。

综合起来，这段配置的意思是，当有请求匹配到根路径 `/` 时，Nginx 将会在 `D:\Graduation_project\kg-course\kg3.0\kg3.0\vis` 目录下寻找对应的文件，如果请求的路径是一个目录，则尝试返回 `index.html` 或者 `index.htm` 文件。

>  
 `root` 和 `alias` 都是 Nginx 中用于指定静态文件路径的指令，但它们之间有一些重要的区别： 
 <ol><li> **root：** 
   - `root` 指令用于指定请求的文件在文件系统中的根路径。- 当请求的 URI 匹配到了某个 `location` 块，并且使用了 `root` 指令，Nginx 将会在这个根路径下寻找请求的文件或目录。- 如果请求的 URI 是 `/path/to/resource`，那么 Nginx 将会在 `root` 指定的路径下寻找 `/path/to/resource` 文件或目录。- 如果请求的 URI 是 `/path/to/resource/file.html`，那么 Nginx 将会在 `root` 指定的路径下寻找 `/path/to/resource/file.html` 文件。</li><li> **alias：** 
   - `alias` 指令也用于指定静态文件的路径，但它可以用于更灵活地指定不同的路径。- `alias` 指令用于替换请求的 URI 中的部分内容，并指定相应的文件路径。- 当请求的 URI 匹配到了某个 `location` 块，并且使用了 `alias` 指令，Nginx 将会使用指定的路径替换请求的 URI 中匹配到的部分，然后在这个新的路径下寻找请求的文件或目录。- 例如，如果请求的 URI 是 `/path/to/resource/file.html`，并且使用了 `alias /some/other/path/` 指令，那么 Nginx 将会在 `/some/other/path/to/resource/file.html` 路径下寻找文件。</li></ol> 
 总的来说，`root` 指令用于指定根路径，在请求路径上直接附加，而 `alias` 指令用于替换请求路径中的部分内容，并指定文件路径。 


### 四、nginx设置代理转发规则

如果你的前端代码通过 Nginx 代理发送请求到后端，你需要在 Nginx 的配置文件中设置代理转发规则，将请求转发到若依后端对应的端口上。假设若依后端服务运行在本地的某个端口（比如 8080 端口），以下是一个简单的 Nginx 配置示例：

```
server {
    listen 80;
    server_name localhost;

    location / {
        # 设置代理转发规则，将请求转发到若依后端服务的地址和端口上
        proxy_pass http://localhost:8080;
        # 设置一些代理头信息，可选
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

```

在上面的配置中，`proxy_pass` 指令将所有请求转发到 `http://localhost:8080`，也就是若依后端服务所在的地址和端口。这样设置后，当客户端发送请求到 Nginx 时，Nginx 会将请求转发到若依后端服务，从而实现了前端代码通过 Nginx 代理发送请求到后端的目的。

如果你只想将接口为 `/api/flask` 开头的请求转发到若依后端服务，你可以在 Nginx 的配置中使用 `location` 指令来匹配这些请求，并设置相应的代理转发规则。以下是一个示例配置：

```
server {
    listen 80;
    server_name yourdomain.com;

    location /api/flask {
        # 设置代理转发规则，将请求转发到若依后端服务的地址和端口上
        proxy_pass http://localhost:8080;
        # 设置一些代理头信息，可选
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # 如果有其他的请求需要处理，可以继续添加其他 location 块
    # location / {
    #     # 其他处理逻辑
    # }
}

```

在上面的配置中，只有请求路径以 `/api/flask` 开头的请求才会被匹配到这个 `location` 块，并被转发到若依后端服务。其他请求将不受影响，可以根据需要添加其他的 `location` 块来处理不同的请求。

### 五、优化配置

打开nginx.conf按照自己需求进行配置，下面列出简单的一些常规调优配置

（参考博客：）

```
#user  nobody;

#==工作进程数，一般设置为cpu核心数
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {

    #==最大连接数，一般设置为cpu*2048
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    
    #==客户端链接超时时间
    keepalive_timeout  65;

    #gzip  on;

    #当配置多个server节点时，默认server names的缓存区大小就不够了，需要手动设置大一点
    server_names_hash_bucket_size 512;

    #server表示虚拟主机可以理解为一个站点，可以配置多个server节点搭建多个站点
    #每一个请求进来确定使用哪个server由server_name确定
    server {
        #站点监听端口
        listen       8800;
        #站点访问域名
        server_name  localhost;
        
        #编码格式，避免url参数乱码
        charset utf-8;

        #access_log  logs/host.access.log  main;

        #location用来匹配同一域名下多个URI的访问规则
        #比如动态资源如何跳转，静态资源如何跳转等
        #location后面跟着的/代表匹配规则
        location / {
            #站点根目录，可以是相对路径，也可以使绝对路径
            root   html;
            #默认主页
            index  index.html index.htm;
            
            #转发后端站点地址，一般用于做软负载，轮询后端服务器
            #proxy_pass http://10.11.12.237:8080;

            #拒绝请求，返回403，一般用于某些目录禁止访问
            #deny all;
            
            #允许请求
            #allow all;
            
            add_header 'Access-Control-Allow-Origin' '*';
            add_header 'Access-Control-Allow-Credentials' 'true';
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
            add_header 'Access-Control-Allow-Headers' 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type';
            #重新定义或者添加发往后端服务器的请求头
            #给请求头中添加客户请求主机名
            proxy_set_header Host $host;
            #给请求头中添加客户端IP
            proxy_set_header X-Real-IP $remote_addr;
            #将$remote_addr变量值添加在客户端“X-Forwarded-For”请求头的后面，并以逗号分隔。 如果客户端请求未携带“X-Forwarded-For”请求头，$proxy_add_x_forwarded_for变量值将与$remote_addr变量相同  
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            #给请求头中添加客户端的Cookie
            proxy_set_header Cookie $http_cookie;
            #将使用代理服务器的主域名和端口号来替换。如果端口是80，可以不加。
            proxy_redirect off;
            
            #浏览器对 Cookie 有很多限制，如果 Cookie 的 Domain 部分与当前页面的 Domain 不匹配就无法写入。
            #所以如果请求 A 域名，服务器 proxy_pass 到 B 域名，然后 B 服务器输出 Domian=B 的 Cookie，
            #前端的页面依然停留在 A 域名上，于是浏览器就无法将 Cookie 写入。
            
　　         #不仅是域名，浏览器对 Path 也有限制。我们经常会 proxy_pass 到目标服务器的某个 Path 下，
            #不把这个 Path 暴露给浏览器。这时候如果目标服务器的 Cookie 写死了 Path 也会出现 Cookie 无法写入的问题。
            
            #设置“Set-Cookie”响应头中的domain属性的替换文本，其值可以为一个字符串、正则表达式的模式或一个引用的变量
            #转发后端服务器如果需要Cookie则需要将cookie domain也进行转换，否则前端域名与后端域名不一致cookie就会无法存取
　　　　　　  #配置规则：proxy_cookie_domain serverDomain(后端服务器域) nginxDomain(nginx服务器域)
            proxy_cookie_domain localhost .testcaigou800.com;
            
            #取消当前配置级别的所有proxy_cookie_domain指令
            #proxy_cookie_domain off;
            #与后端服务器建立连接的超时时间。一般不可能大于75秒；
            proxy_connect_timeout 30;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

    }
    
　　#当需要对同一端口监听多个域名时，使用如下配置，端口相同域名不同，server_name也可以使用正则进行配置
　　#但要注意server过多需要手动扩大server_names_hash_bucket_size缓存区大小
　　server {
　　　　listen 80;
　　　　server_name www.abc.com;
　　　　charset utf-8;
　　　　location / {
　　　　　　proxy_pass http://localhost:10001;
　　　　}
　　}
　　server {
　　　　listen 80;
　　　　server_name aaa.abc.com;
　　　　charset utf-8;
　　　　location / {
　　　　　　proxy_pass http://localhost:20002;
　　　　}
　　}
}
```


