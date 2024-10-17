
--- 
title:  openshift部署前后端项目 
tags: []
categories: [] 

---
## 一、部署前端

### 1.1搜索nginx

<img alt="" height="247" src="https://img-blog.csdnimg.cn/20210511161432370.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="479">

### 1.2填写项目名，前端项目git地址

<img alt="" height="361" src="https://img-blog.csdnimg.cn/20210511161655356.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="570"><img alt="" height="360" src="https://img-blog.csdnimg.cn/20210511162036967.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="493">

### 1.3点击build

<img alt="" height="177" src="https://img-blog.csdnimg.cn/20210511162227815.png" width="1200">

出错原因：git仓库需要账号和密码，所以clone的时候报错。可以点击“View log”查看报错信息：<img alt="" height="42" src="https://img-blog.csdnimg.cn/20210511162429996.png" width="427">

解决方法：

**①创建secrets（点击Resources-&gt;Secrets-&gt;create Secrets）**

<img alt="" height="327" src="https://img-blog.csdnimg.cn/20210511162715832.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="396">

**②.点击刚才创建的镜像(Builds-&gt;镜像名)**

<img alt="" height="162" src="https://img-blog.csdnimg.cn/20210511162949846.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="831">     <img alt="" height="163" src="https://img-blog.csdnimg.cn/20210511163108550.png" width="582">

**③.点击Start Build**

<img alt="" height="227" src="https://img-blog.csdnimg.cn/20210511163319305.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1049">

### 1.4创建nginx配置文件与容器内部关联

**①Resource-&gt;Config Maps**

<img alt="" height="514" src="https://img-blog.csdnimg.cn/20210511163642346.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="557">

**②点击该ConfigMap，点击Add to Application**

/etc/opt/rh/rh-nginx116/nginx/nginx.conf

<img alt="" height="313" src="https://img-blog.csdnimg.cn/20210511164001193.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="586">

**③设置subPath，直接挂载会导致覆盖整个目录，如果想要不覆盖原目录则在挂载完成后修改dc的yaml**

<img alt="" height="315" src="https://img-blog.csdnimg.cn/20210511165933807.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="821">  <img alt="" height="98" src="https://img-blog.csdnimg.cn/20210511170013715.png" width="540">

## 二、部署jar包

<img alt="" height="170" src="https://img-blog.csdnimg.cn/20210702115508864.png" width="513">

持续更新

>  
 /etc/opt/rh/rh-nginx116/nginx 











