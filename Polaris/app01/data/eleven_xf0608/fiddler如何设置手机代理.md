
--- 
title:  fiddler如何设置手机代理 
tags: []
categories: [] 

---
fiddler这个工具，我主要用来抓包，为日常软件测试提供一些帮助。 下面介绍一下fiddler如何设置手机代理。

一、安装fiddler

这一步比较简单，大家在网上下载一个fiddler安装在电脑上即可。

 二、fiddler设置。

步骤：

在电脑上打开fiddler&gt;tools&gt;options，进入fiddler配置。允许远程电脑连接（Allow remot computers to connect），设置端口号（8888）

<img alt="" height="454" src="https://img-blog.csdnimg.cn/e718aef48cea40dbb6f10df46249e9df.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAZWxldmVuX3hmMDYwOA==,size_17,color_FFFFFF,t_70,g_se,x_16" width="674">



<img alt="" height="453" src="https://img-blog.csdnimg.cn/4d8686b9c67c42ef87d4c316101fca76.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAZWxldmVuX3hmMDYwOA==,size_17,color_FFFFFF,t_70,g_se,x_16" width="667">



三、查看自己电脑IP

在电脑上命令窗口输入ipconfig

<img alt="" height="362" src="https://img-blog.csdnimg.cn/19991420f6624a8091bb805d4bd039ce.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAZWxldmVuX3hmMDYwOA==,size_18,color_FFFFFF,t_70,g_se,x_16" width="713">



四、设置代理。

手机端抓包，需要先设置好代理，确保电脑和手机端在一个局域网内。

手机端设置代理，进入手机“设置”/WLAN/选择手机连接的wifi，长按选择“修改”，进入修改界面，按如图设置好代理服务器主机名（填写自己电脑IP）和端口（fiddler中设置的端口8888），设置好后，点击“保存”

<img alt="" height="854" src="https://img-blog.csdnimg.cn/e08846b7e4b948ebbcb294a5b20fdb37.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAZWxldmVuX3hmMDYwOA==,size_10,color_FFFFFF,t_70,g_se,x_16" width="415">



五、此时手机上的操作都能在电脑端fiddler中抓包了。


