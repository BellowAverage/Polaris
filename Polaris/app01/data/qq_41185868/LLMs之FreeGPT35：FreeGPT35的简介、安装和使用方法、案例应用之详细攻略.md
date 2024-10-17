
--- 
title:  LLMs之FreeGPT35：FreeGPT35的简介、安装和使用方法、案例应用之详细攻略 
tags: []
categories: [] 

---
LLMs之FreeGPT35：FreeGPT35的简介、安装和使用方法、案例应用之详细攻略





**目录**





































## **FreeGPT35的简介**

2024年4月3日，发布了FreeGPT35，这是一款利用无需登录的ChatGPT Web提供的无限免费GPT-3.5-Turbo API服务。

**<strong>GitHub地址**</strong>：









## **FreeGPT35的安装和使用方法**

部署和使用一个名为 FreeGPT35 的服务，该服务提供了一个基于 GPT-3.5 模型的聊天接口。其中包括了使用 Node.js 和 npm 安装和启动服务的方法，以及使用 Docker 和 Docker Compose 进行容器化部署的步骤。此外，还提供了如何配置 Nginx 反向代理和负载均衡以及请求示例和兼容性说明。



### **<strong><strong>1、部署和启动服务**</strong></strong>

安装 Node.js 和 npm。使用 npm 安装依赖。启动服务应用程序。

```
npm install
node app.js
```





### **<strong><strong>2、使用 Docker 部署服务：**</strong></strong>

#### **<strong><strong>运行 Docker 容器以部署服务**</strong></strong>

```
docker run -p 3040:3040 ghcr.io/missuo/freegpt35

docker run -p 3040:3040 missuo/freegpt35
```



#### **<strong><strong>使用 Docker Compose 进行更方便的容器化部署**</strong></strong>

##### **<strong><strong>T1、只包含 FreeGPT35 服务**</strong></strong>

```
mkdir freegpt35 &amp;&amp; cd freegpt35
wget -O compose.yaml https://raw.githubusercontent.com/missuo/FreeGPT35/main/compose.yaml
docker compose up -d
```



##### **<strong><strong>T2、带有 ChatGPT-Next-Web 的 FreeGPT35 服务**</strong></strong>

```
mkdir freegpt35 &amp;&amp; cd freegpt35
wget -O compose.yaml https://raw.githubusercontent.com/missuo/FreeGPT35/main/compose_with_next_chat.yaml
docker compose up -d
```



部署完成后，您可以直接访问 http://[IP]:3040/v1/chat/completions 使用 API。或者使用 http://[IP]:3000 直接使用 ChatGPT-Next-Web。





### **<strong><strong>3、配置 Nginx 反向代理：**</strong></strong>

#### **<strong><strong>配置 Nginx 以实现反向代理**</strong></strong>

```
location ^~ / {
        proxy_pass http://127.0.0.1:3040; 
        proxy_set_header Host $host; 
        proxy_set_header X-Real-IP $remote_addr; 
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; 
        proxy_set_header REMOTE-HOST $remote_addr; 
        proxy_set_header Upgrade $http_upgrade; 
        proxy_set_header Connection "upgrade"; 
        proxy_http_version 1.1; 
        add_header Cache-Control no-cache; 
        proxy_cache off;
        proxy_buffering off;
        chunked_transfer_encoding on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 300;
    }
```



#### **<strong><strong>可选：配置 Nginx 以实现负载均衡**</strong></strong>

```
upstream freegpt35 {
        server 1.1.1.1:3040;
        server 2.2.2.2:3040;
}

location ^~ / {
        proxy_pass http://freegpt35; 
        proxy_set_header Host $host; 
        proxy_set_header X-Real-IP $remote_addr; 
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; 
        proxy_set_header REMOTE-HOST $remote_addr; 
        proxy_set_header Upgrade $http_upgrade; 
        proxy_set_header Connection "upgrade"; 
        proxy_http_version 1.1; 
        add_header Cache-Control no-cache; 
        proxy_cache off;
        proxy_buffering off;
        chunked_transfer_encoding on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 300;
    }
```





### **<strong><strong>4、请求示例**</strong></strong>

您不必传递授权，当然，您也可以随机传递任意字符串。

提供了一个使用 cURL 发送请求的示例。

```
curl http://127.0.0.1:3040/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer any_string_you_like" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "user",
        "content": "Hello!"
      }
    ],
    "stream": true
    }'
```





### **<strong><strong>5、兼容性说明**</strong></strong>

说明了服务的兼容性，可以在不同的应用中使用，并且可以自定义 API 密钥。

您可以在任何应用中使用它，如 OpenCat、Next-Chat、Lobe-Chat、Bob 等等。随意填写一个任意字符串的 API 密钥，例如 gptyyds。







## **FreeGPT35的案例应用**

持续更新中……

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/f8175e798c0a4ce1bb7816650d64971d.png" width="1200">




