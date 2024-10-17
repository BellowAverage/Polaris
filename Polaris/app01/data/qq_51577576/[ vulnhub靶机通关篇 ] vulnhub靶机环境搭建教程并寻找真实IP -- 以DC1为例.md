
--- 
title:  [ vulnhub靶机通关篇 ] vulnhub靶机环境搭建教程并寻找真实IP -- 以DC1为例 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - - <ul><li>- 


## 一、下载靶场环境

>  
 靶场下载地址： 


```
https://www.vulnhub.com/entry/dc-1,292/

```

>  
 下载下来的文件如下 


<img src="https://img-blog.csdnimg.cn/309f5ee0a42e48d783bee7430c906bc6.png" alt="在这里插入图片描述">

## 二、启动靶场环境

>  
 下载下来是虚拟机压缩文件，直接用Vmvare导入就行。 


<img src="https://img-blog.csdnimg.cn/9d09f819066c42d79cd9e0a71ac0722a.png" alt="在这里插入图片描述">

>  
 设置虚拟机名称 


<img src="https://img-blog.csdnimg.cn/b41a1752383342bba5d2d85621ee4f63.png" alt="在这里插入图片描述">

>  
 导入中 


<img src="https://img-blog.csdnimg.cn/28154c6fa37f44588d09978e4ee7f02d.png" alt="在这里插入图片描述">

## 三、调节网络模式

>  
 导入完成之后打开后把网络模式设置为NAT模式，当然允许桥接的情况下也可以使用桥接 


<img src="https://img-blog.csdnimg.cn/952cc9f061634c1985192a7bfaed48f7.png" alt="在这里插入图片描述">

>  
 虚拟机开启之后界面如下，我们不知道ip，需要自己探活，网段就是你虚拟机使用的网段 


<img src="https://img-blog.csdnimg.cn/1b6cfcb9c93e46e58c18d79807bcb6d9.png" alt="在这里插入图片描述">

## 四、寻找靶机真实IP

### 1、目标：

>  
 目标就是我们搭建的靶场，靶场IP为：192.168.233.0/24 


### 2、信息收集：寻找靶机真实IP

```
nmap -sP 192.168.233.0/24

```

<img src="https://img-blog.csdnimg.cn/a3533b9331584fff8b9a0dc1c3591449.png" alt="在这里插入图片描述">

>  
 本机ip为192.168.233.130 所以分析可得靶机ip为192.168.233.177 


```
192.168.233.1		vm8网卡
192.168.233.2		网关
192.168.233.177	靶机
192.168.233.254	DHCP服务器
192.168.233.130

```
