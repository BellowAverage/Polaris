
--- 
title:  Ubuntu中 GParted分区编辑器的安装，卸载与启动 
tags: []
categories: [] 

---
这里介绍一款Ubuntu中磁盘管理工具–**GParted分区编辑器：** <img src="https://img-blog.csdnimg.cn/8d40b457914443bcaf6abb521266d4a3.png" alt="GParted分区编辑器" width="128"> 安装命令如下：

```
$ sudo apt-get update
$ sudo apt-get install gparted

```

<img src="https://img-blog.csdnimg.cn/bb792127ffb148b998ad2a9b92a56d61.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="安装GParted" width="680"> 安装成功后搜索GParted即可看到上图软件，当然也可使用命令进行启动，如下：

```
$ sudo gparted

```

<img src="https://img-blog.csdnimg.cn/a21ce9f20cb045a590d3b6e0846232c4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="启动GParted" width="680"> 使用完成后如不需要可进行卸载，命令如下：

```
$ sudo apt-get remove gparted

```

<img src="https://img-blog.csdnimg.cn/070480fbed8a459596f1327ce2ac77f1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA54K55bm0576K,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="卸载GParted" width="680">
