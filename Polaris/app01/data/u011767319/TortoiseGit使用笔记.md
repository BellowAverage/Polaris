
--- 
title:  TortoiseGit使用笔记 
tags: []
categories: [] 

---
### 简介

>  
 为什么要使用TortoiseGit 因为git的工具的命令很多，如果那超喜欢使用命令的话，请忽略这篇文章 这个是git的可视化工具，能大量简化git的使用 


### 下载



### 它支持多语言

<img src="https://img-blog.csdnimg.cn/2021051016003568.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 安装完TortoiseGit可以再下载自己喜欢的语言，我就安装了中文的 <img src="https://img-blog.csdnimg.cn/20210510160153892.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 生成凭证

<img src="https://img-blog.csdnimg.cn/20210510160516426.png" alt="在这里插入图片描述"> 点击指向哪个按钮生成key，然后等进度条完成就可以了（多动鼠标让进度条加快，它有bug，等是没有用的） <img src="https://img-blog.csdnimg.cn/20210510160542874.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 然后在保存公钥和私钥就可以了 <img src="https://img-blog.csdnimg.cn/20210510160851262.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### gitlab 如何使用与TortoiseGit 对接呢

<img src="https://img-blog.csdnimg.cn/20210510161051649.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 将上面的key黏贴到gitlab上就可以了，然后就可以ssh拉取数据啦
