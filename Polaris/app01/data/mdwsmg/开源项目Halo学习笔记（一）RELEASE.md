
--- 
title:  开源项目Halo学习笔记（一）RELEASE 
tags: []
categories: [] 

---
项目部署相关问题 已经变成我的形状了.jpg



#### 目录
- <ul><li><ul><li>- <ul><li>- - 


#### 对项目信息进行修改

##### 修改端口

修改端口后，直接访问博客页面，加载不了CSS <img src="https://img-blog.csdnimg.cn/20210129094450388.png" alt="在这里插入图片描述"> 可以看到**CSS引用的端口没有改变** <img src="https://img-blog.csdnimg.cn/2021012909481857.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 检查了代码，没有看到端口体现，最后在后台管理的设置找到原因了。 在8090端口时创建的博客页面，当然不可以引用9611端口启用后的CSS。 修改博客地址就可以解决问题了。我是傻帽。 <img src="https://img-blog.csdnimg.cn/20210129101701298.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

#### 项目部署

halo有相关详尽部署文档 

##### 使用Docker部署

可能会出现docker找不到的问题

>  
 -bash: docker: command not found 


使用下面的命令查看当前docker版本

>  
 yum list docker-ce --showduplicates | sort -r 


我的情况是CentOS 8 没带Docker，推荐大佬的教程 

##### Linux直接部署

 注意JDK版本，已经运行时使用可以后台运行的命令

>  
 nohup java -jar halo.jar &amp; 


直接部署并没有成功——初次成功运行后，并没有设置后台运行，再次通过XShell连接至服务器运行报错了，有服务占用、JDK版本不对（百度说是）等各种问题，有些理解不了。 但是docker很快就成功了。 容器化，好！
