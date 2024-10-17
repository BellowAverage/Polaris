
--- 
title:  向docker hub推送镜像 拉取镜像 
tags: []
categories: [] 

---1. 登录 docker hub docker login <img src="https://img-blog.csdnimg.cn/f60c64c76f5841c4bb3a8cd67f9216cc.png" alt="在这里插入图片描述">1. 列出所有的镜像：
```
docker images

```

<img src="https://img-blog.csdnimg.cn/b761cd06e235403eb89cd757522a4de4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 3. 以nginx为例，给镜像打上 tag

```
docker tag nginx:latest qinenqi/nginx:0.0.1

```

<img src="https://img-blog.csdnimg.cn/adf8238304cb4b1e964f82503112d6a7.png" alt="在这里插入图片描述"> nginx:latest 镜像及版本号 qinenqi： dockerhub 的用户名 nginx:0.0.1 新的镜像名称和版本号
1. 将刚才打好的镜像（nginx:0.0.1） 推送到dockerhub上
```
docker push qinenqi/nginx:0.0.1

```

qinenqi/nginx:0.0.1 分别是用户名/镜像:版本 <img src="https://img-blog.csdnimg.cn/f3a554c1634443e782f4f4bae8ad8a53.png" alt="在这里插入图片描述"> 5. 网页登录docker hub（https://hub.docker.com/），并在页面上查看 <img src="https://img-blog.csdnimg.cn/d05efcd31bd24821b37bbcc1d108ca82.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 6. 拉取镜像

```
docker pull qinenqi/nginx:0.0.1

```

<img src="https://img-blog.csdnimg.cn/6bfc8171b3014f78917d34fe05899291.png" alt="在这里插入图片描述">
