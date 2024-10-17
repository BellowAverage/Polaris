
--- 
title:  在浏览器访问服务器centos系统下部署的tomcat显示无法访问 
tags: []
categories: [] 

---
这是一个排查的过程

## 第一步

检查服务器是否已经开启了8080端口，或者你设置的tomcat的端口 <img src="https://img-blog.csdnimg.cn/cb7781d19bc643daa74cde7ee74859d7.png" alt="在这里插入图片描述">

## 第二部

检查你的服务器系统中防火墙是否已经将8080端口打开

<img src="https://img-blog.csdnimg.cn/201e938d084d4d08a7386abaef4854cc.png" alt="在这里插入图片描述">

## 第三步

如果你进行上面两步还是没有在浏览器访问到8080，没出现下面的页面 <img src="https://img-blog.csdnimg.cn/f30ad1e4870f4e2b89a4c64201a26287.png" alt="在这里插入图片描述"> 请你观察你的tomcat下的 <img src="https://img-blog.csdnimg.cn/2f98a079dc5a4f9090f3a3c749aed70c.png" alt="在这里插入图片描述"> 最新日志，我的是报错信息是8005端口被占用，8005端口是关闭服务的端口。有人说直接找到8005端口的进程kill就行了。但是不推荐。这样不解决病根。8005被占用是java的security <img src="https://img-blog.csdnimg.cn/ce598f010ae0424c9f2ed390cfb899fc.png" alt="在这里插入图片描述"> 我们找到它并修改 <img src="https://img-blog.csdnimg.cn/22ad44a09d3c4b0d8717b1d6d9b242df.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/18b740b208ba4c64b58fc201b035d9b3.png" alt="在这里插入图片描述"> 然后我的问题就解决了。 你可以把你的问题写在下面，一起解决。
