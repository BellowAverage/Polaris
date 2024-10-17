
--- 
title:  [ 常用工具篇 ] 解决 kali 拉取docker容器慢的问题 -- kali修改 Docker 镜像服务器 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - <ul><li>- - <ul><li>- - - - <ul><li>- 


## 一、Docker Hub介绍

>  
 Docker Hub 是我们分发和获取 Docker 镜像的中心，但由于服务器位于海外，经常会出现拉取/上传镜像时速度太慢或无法访问的情况。再加上运营方不断对 Docker Hub 的免费使用进行限制，导致我们在国内使用时不尽如意。 使用 Docker 时也经常有人拉取镜像速度慢或拉取失败的情况，可以尝试改用国内的 Docker Hub 镜像服务器。 


## 二、免费Docker Hub 镜像服务器

>  
 网易云 


```
https://hub-mirror.c.163.com

```

>  
 百度云 


```
https://mirror.baidubce.com

```

>  
 DaoCloud 


```
http://f1361db2.m.daocloud.io

```

>  
 阿里云 


```
https://ustc-edu-cn.mirror.aliyuncs.com

```

>  
 Github 


```
https://ghcr.io

```

## 三、修改Docker Hub 镜像服务器

### 1、修改 /etc/docker/daemon.json 配置文件

>  
 使用vi命令修改/etc/docker/daemon.json配置文件，将国外docker hub镜像库换成国内的 


```
vi /etc/docker/daemon.json

```

<img src="https://img-blog.csdnimg.cn/e262ff7f95a14af6a1377834784a499f.png" alt="在这里插入图片描述">

>  
 原有docker hub镜像库如下 <img src="https://img-blog.csdnimg.cn/575b420ece964d509a96afc54f6c2f14.png" alt="在这里插入图片描述"> 


>  
 直接删掉原来的，把下面这段话复制进入，就ok了，当然你也可以换上其他的镜像库，我这里使用的是网易云和百度云的 


```
{<!-- -->
  "registry-mirrors": [
    "https://hub-mirror.c.163.com",
    "https://mirror.baidubce.com"
  ]
}

```

>  
 改完成之后如下，然后保存退出 <img src="https://img-blog.csdnimg.cn/4950f900ac0c417e9af6def9f7023cae.png" alt="在这里插入图片描述"> 


### 2.重启docker服务使配置文件生效

#### 1、重启docker服务

>  
 下面的命令应该都行 


```
sudo systemctl daemon-reload 	守护进程重启
sudo systemctl restart docker		systemctl方式重启docker服务
sudo service docker restart		service方式重启docker服务

```

<img src="https://img-blog.csdnimg.cn/6ce7c2a80a7c42e7ad6f084e55d99aae.png" alt="在这里插入图片描述">

#### 2.检查设置是否生效

```
sudo docker info

```

<img src="https://img-blog.csdnimg.cn/a5f4bf7c1fc2423c9f8787e0d0010191.png" alt="在这里插入图片描述">

>  
 结果中显示了我们设置的镜像服务器地址，则说明设置已经生效，返回的信息类似下面这样： 


```
 Registry Mirrors:
  https://hub-mirror.c.163.com/
  https://mirror.baidubce.com/

```

<img src="https://img-blog.csdnimg.cn/93e141cd3e00477cabcf21172163f80d.png" alt="在这里插入图片描述">

#### 3.重新测试拉取容器速度

>  
 直接飞起完美解决 


<img src="https://img-blog.csdnimg.cn/ea4e696596f34111adeb24978134326b.png" alt="在这里插入图片描述">

## 四、问题解决

### 1、/etc/docker/daemon.json文件不存在

#### 1.创建配置文件目录

```
sudo mkdir /etc/docker

```

#### 2.编辑配置文件，如果文件不存在，以下命令会自动创建

```
sudo nano /etc/docker/daemon.json

```
