
--- 
title:  搭建私有云:owncloud(用Docker构建owncloud私有云盘) 
tags: []
categories: [] 

---
网上各种云盘都要收费，又或有速度限制，感觉用起来不方便，想抽时间想搭建一个私有云盘。下面讲解下搭建私有云:owncloud。

### 搭建私有云:owncloud(用Docker构建owncloud私有云盘)分为6个步骤：

####     搭建私有云:owncloud第一步：首先在服务器上安装docker服务，在操作yum install docker的时候，发现用service docker start的时候不成功，发现是跟操作系统版本有关，在Centos低版本的时候，应该使用 yum install docker-io,安装成功后，可以用docker -v 查看版本；

####     搭建私有云:owncloud第二步：启动docker服务。service docker start；

####     搭建私有云:owncloud第三步：进入docker，下载owncloud镜像，使用命令docker pull owncloud;

####     搭建私有云:owncloud第四步：运行docker run -d -p 9090:80 owncloud,映射端口号，启动owncloud镜像；

####     搭建私有云:owncloud第五步：在浏览器中输入“服务器的IP地址:9090”就看见owncloud的网页界面了，我对云盘要求不高，默认使用SQLite数据库，输入用户名和密码然后确认就可以了。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/5849a566d552ab592b82bbcda1905a22.jpeg">

####     搭建私有云:owncloud第六步：在浏览器界面输入刚刚输入的用户名和
