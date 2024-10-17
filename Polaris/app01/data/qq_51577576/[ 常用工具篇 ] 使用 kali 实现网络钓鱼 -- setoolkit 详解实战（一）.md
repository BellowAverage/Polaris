
--- 
title:  [ 常用工具篇 ] 使用 kali 实现网络钓鱼 -- setoolkit 详解实战（一） 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - - <ul><li>- - - - - - - - - 


>  
 本文只是一次简单的实操，后续我会详细的讲解setoolkit。 


## 本文仅用于学习使用，切勿用于真实环境，否则，后果自负

## 1、setoolkit原理

>  
 用setoolkit进行钓鱼攻击，kali是根据要克隆的网址将网站保存在某个文件夹下，并且添加一些其他的信息，主要是将受害者输入的信息截获下来，并保存到有一个文本文件中，还有截获完之后，使浏览器跳转到正常页面。 


## 2、实验环境

>  
 攻击机：Kali：192.168.233.128 靶机：192.168.233.1 目标网站：http://192.168.233.1/pikachu-master/vul/burteforce/bf_form.php 我是在靶机搭建了一个pikachu的环境采取了暴力破解里边的一个登录页面 目标用户：使用目标网站的所有用户都可以是目标用户 


## 3、克隆页面

### 1.进入social-engineer-toolkit

>  
 登录到kali，在kali的工具包里找到social-engineer-toolkit，并打开， 


<img src="https://img-blog.csdnimg.cn/b0a2eca41fab4193a2bf8b4281ba6dbf.png" alt="在这里插入图片描述">

>  
 第一次打开会显示如下界面，且“同意服务条款” 


<img src="https://img-blog.csdnimg.cn/501f649f052e4cf7b05892d5788dbb9e.png" alt="在这里插入图片描述">

### 2.选择Social-Engineering Attacks

>  
 在出现的界面中，选择1）Social-Engineering Attacks选项，即社会工程学攻击方式。 


<img src="https://img-blog.csdnimg.cn/a27f632a6a744a50980a5d0e6cc22a0d.png" alt="在这里插入图片描述">

### 3.选择Website Attack Vectors

>  
 接着选择2）Website Attack Vectors选项，即以网站为载体攻击的方式。 


<img src="https://img-blog.csdnimg.cn/fe4fd702fa10472bb5d923532e2c9457.png" alt="在这里插入图片描述">

### 4.选择Web jacking Attack Method

>  
 接着选择5）Web jacking Attack Method选项，即网站劫持方式。 


<img src="https://img-blog.csdnimg.cn/fe877a0327db45dc8303db40776ed2a0.png" alt="在这里插入图片描述">

### 5.选择Site Cloner

>  
 接着选择2）Site Cloner，即网址克隆方式。 


<img src="https://img-blog.csdnimg.cn/fbf45bc7cd4845a589ea5ea68983d8ad.png" alt="在这里插入图片描述">

### 6.输入本机的IP

>  
 接着输入本机的IP地址。 


<img src="https://img-blog.csdnimg.cn/59f67a1fe3a8401ba8ccd7bec808c01a.png" alt="在这里插入图片描述">

### 7.输入目标url

>  
 在Enter the url to clone：后面输入需要进行克隆的网站URL，以便针对访问网站进行钓鱼操作，本实验采用的是靶机，如下 


```
http://192.168.233.1/pikachu-master/vul/burteforce/bf_form.php

```

<img src="https://img-blog.csdnimg.cn/c12d2a794b0f4fb480f58ce29d82f8db.png" alt="在这里插入图片描述">

### 8.克隆成功

>  
 出现以下界面说明克隆网站成功，一旦有数据通过克隆网站发送出去，就会被监听到。 


<img src="https://img-blog.csdnimg.cn/379e2129e9a6475082699e00f968ee92.png" alt="在这里插入图片描述">

## 4、寻找目标用户

>  
 将克隆的页面以各种形式发送给你需要攻击的目标用户。 这里我就没有这个环节了，我省掉了，我使用的是靶机。 


## 5、钓鱼成功

### 1.用户访问

>  
 接着打开kali的浏览器，在url栏中输入“192.168.233.128/index2.html”，会显示出克隆网站，跟真的一样。 


<img src="https://img-blog.csdnimg.cn/18957ae9d15343c0a51e5addfb49fd48.png" alt="在这里插入图片描述">

>  
 访问之后，我们进入kali查看，发现访问者是192.168.233.1 


<img src="https://img-blog.csdnimg.cn/653873a0ca1c487ca4a2d6d30500c910.png" alt="在这里插入图片描述">

### 2.用户输入账号密码

>  
 目标用户在该网站上输入邮件地址和密码。 


<img src="https://img-blog.csdnimg.cn/943ad39fcf394354a51b6491624fb0c4.png" alt="在这里插入图片描述">

>  
 登陆后跳转到真实网站 


<img src="https://img-blog.csdnimg.cn/4816af816c1046978e8ebaa1b302fce8.png" alt="在这里插入图片描述">

>  
 到kali查看，已经得到了刚刚192.168.233.1用户输入的账号密码123，123 


<img src="https://img-blog.csdnimg.cn/cbae5ca4b6d345f1af7d2644aeccec25.png" alt="在这里插入图片描述">

>  
 到这里钓鱼基本上就结束了。 


## 本文仅用于学习使用，切勿用于真实环境，否则，后果自负
