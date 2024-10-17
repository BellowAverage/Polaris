
--- 
title:  [ web基础知识点 ] 解决端口被占用的问题(关闭连接)(杀死进程) 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - - - - 


## 一、前言

>  
 今天想用小皮搭建一个环境，发现80端口被占用，然后想到之前后粉丝问过我端口被占用咋办。 这里提供一个简单粗暴的办法，直接把进程干掉。 


## 二、Windows下杀死进程

>  
 由于上面截图来自于windows所有这里先讲windows下杀死进程的方法 


### 1、端口被占用

>  
 端口被占用截图如下 


<img src="https://img-blog.csdnimg.cn/a3aa74944269404990e57b5890cdce15.png" alt="在这里插入图片描述">

### 2、查找占用80端口的进程

>  
 查看PID对应的应用程序名 


```
netstat -aon | findstr “端口”

```

<img src="https://img-blog.csdnimg.cn/c111da9084e94d76aa65382429d839ef.png" alt="在这里插入图片描述">

### 3、杀死这个进程

```
tasklist | findstr “PID”

```

<img src="https://img-blog.csdnimg.cn/b359299cc9d34d2983d32795faca6712.png" alt="在这里插入图片描述">

### 4、小皮成功启动环境

<img src="https://img-blog.csdnimg.cn/a2a18d3577834b58b4c4db65e7b28e6f.png" alt="在这里插入图片描述">

## 三、linux 杀死进程

### 1、查找占用80端口的进程

```
ps -ef|grep 80

```

<img src="https://img-blog.csdnimg.cn/08afd4ea07314c478e413ed9703c4119.png" alt="在这里插入图片描述">

### 2、杀死进程

```
kill -9 254861

```

<img src="https://img-blog.csdnimg.cn/2d10bb9864bc47a1ab331c79cc7560d2.png" alt="在这里插入图片描述">
