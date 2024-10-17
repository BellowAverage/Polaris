
--- 
title:  [ 数据库小技巧 ] mysql 命令行执行 sql 文件 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - - 


## 一、进入数据库文件目录

>  
 进入db文件目录 


<img src="https://img-blog.csdnimg.cn/f1ada0067d8e4951835f775c2bea7080.png" alt="在这里插入图片描述">

## 二、进入终端

### 1、连接数据库

```
mysql -u root -p ;

```

### 2、创建数据库

```
create database demo;

```

<img src="https://img-blog.csdnimg.cn/35b194bd63b042d4a183a6a32a47d028.png" alt="在这里插入图片描述">

### 3、进入创建的数据库

```
use demo;

```

<img src="https://img-blog.csdnimg.cn/04ff665367cd41e6bcb214d1cc51df7a.png" alt="在这里插入图片描述">

### 4、执行sql文件

```
source demo.sql;

```

<img src="https://img-blog.csdnimg.cn/e28b0ca96fae492e8a3db5799510f75b.png" alt="在这里插入图片描述">
