
--- 
title:  vue history 配置 
tags: []
categories: [] 

---
前言： 小编把vue项目部署在nginx, 想在访问某一个页面时（如：http://192.168.8.132/newpage），留下访问记录，因此使用 vue 的History 模式

### vue history 配置

我如果想访问 History 模式， /newpage
1. 路由配置
```
export default new Router({<!-- -->
  
  mode: 'history', // 访问路径不带井号  需要使用 history模式
  // base: '/bank/page',  // 基础路径， 不需要可以注释掉
  routes: [
    {<!-- -->
      path: '/', name: 'qianmenhu', component: qianmenhu
    },
    {<!-- -->
      path: '/newpage',
      name: 'newpage',
      component: resolve =&gt; require(['@/views/newpage'], resolve) // 使用懒加载
    },
  ]
})


```
1. nginx 配置 <img src="https://img-blog.csdnimg.cn/15c0141899f646489cf2a640b7cead76.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 修改上面的两处位置的内容即可 完整的配置如下：
```

#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {<!-- -->
    worker_connections  1024;
}


http {<!-- -->
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {<!-- -->
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {<!-- -->
            root   html;
            index  index.html index.htm;
            try_files $uri $uri/ /index.html;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {<!-- -->
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {<!-- -->
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {<!-- -->
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {<!-- -->
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {<!-- -->
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {<!-- -->
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {<!-- -->
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {<!-- -->
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}

```
1. 访问特定的页面（demo的形式展示） <img src="https://img-blog.csdnimg.cn/d1f6d814eb3041048418a97169ae5fe0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">1. 日志内容： <img src="https://img-blog.csdnimg.cn/9a04d67354e4466684838f1af6493398.png" alt="在这里插入图片描述">