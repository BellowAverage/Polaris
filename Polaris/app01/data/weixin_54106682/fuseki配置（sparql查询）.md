
--- 
title:  fuseki配置（sparql查询） 
tags: []
categories: [] 

---
####  下载fuseki



<img alt="" height="795" src="https://img-blog.csdnimg.cn/direct/a0b4052567ec4891af1de328025bc0c6.png" width="1200">

**注意：4版本的fuseki需要11版本及以上的java支持。**

若不是11版本及以上java，在运行fuseki-server.bat时会出现闪退的情况。

java21版本安装教程以及多版本java自由切换教程可参考该博客：

####  运行

解压zip文件夹，找到fuseki-server.bat文件，双击运行。

<img alt="" height="635" src="https://img-blog.csdnimg.cn/direct/53c7b569eabb4394ade447f81579a457.png" width="1129">

访问

<img alt="" height="950" src="https://img-blog.csdnimg.cn/direct/d19003c0ab9f47778c8ece595eeea10c.png" width="1200">

####  创建数据库

点击add one；

<img alt="" height="423" src="https://img-blog.csdnimg.cn/direct/012e98be32a3413dbbd1a7a9162b0dd4.png" width="1114">

注意：这里第二步要选择persistent持久化，以确保数据能够永久保存，而in-memorary是关闭Fuseki之后数据就会消失的，可以当作小练习的时候选择，如果是做项目建议选择persistent。这样就创建好了一个数据库了。

点击add data;

<img alt="" height="464" src="https://img-blog.csdnimg.cn/direct/620143f5c81e4ba5a0aaba8b40e6cfe3.png" width="1200">

点击 upload now;

<img alt="" height="526" src="https://img-blog.csdnimg.cn/direct/b90b6409f12148dd978507bb1f1d8a0d.png" width="1200">

#### 查询

点击query；

<img alt="" height="927" src="https://img-blog.csdnimg.cn/direct/1b93b661bbde4f87b5f028e3e6fda838.png" width="1200">
