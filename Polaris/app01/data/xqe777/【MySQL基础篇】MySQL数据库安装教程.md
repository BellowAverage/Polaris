
--- 
title:  【MySQL基础篇】MySQL数据库安装教程 
tags: []
categories: [] 

---
>  
 ✅作者简介：大家好我是hacker707,大家可以叫我hacker，新星计划第三季python赛道Top1🏆 📃个人主页： 🔥系列专栏： 💬个人格言：但行好事，莫问前程 


<img src="https://img-blog.csdnimg.cn/3fc50c19b27b48d09f1cc17f1493ba8a.png#pic_center" alt="在这里插入图片描述">



#### MySQL数据库安装教程
- - - - - 


## MySQL相关概念

|名称|全称|简称
|------
|数据库|存储数据的仓库，数据是有组织的进行存储|DataBase(DB)
|数据库管理系统|操纵和管理数据库的大型软件|DataBase Management System(DBMS)
|SQL|操作关系型数据库的编程语言，定义了一套操作关系型数据库统一标准|Structured Query Language(SQL)

## MySQL安装教程

MySQL下载地址：

<img src="https://img-blog.csdnimg.cn/2bff324aaed849f5a13b69be25365c7b.png" alt="在这里插入图片描述"> <mark>对应系统选择相应的版本</mark>

<img src="https://img-blog.csdnimg.cn/3f9739a2a85c4d9da0482a2144e13698.png" alt="在这里插入图片描述"> <mark>点击download</mark>

<img src="https://img-blog.csdnimg.cn/cde488eeba5648e2b02c762a801d4631.png" alt="在这里插入图片描述"> <mark>找到下载文件双击安装</mark>

<img src="https://img-blog.csdnimg.cn/4e48e3a3322244439c67dc0478a3b8c1.png" alt="在这里插入图片描述"> <mark>点击Next</mark>

<img src="https://img-blog.csdnimg.cn/94751fac5de644aba801df9eb436a251.png" alt="在这里插入图片描述"> <mark>点击Next</mark>

<img src="https://img-blog.csdnimg.cn/1f6e1850470a4cb58755a9f025076064.png" alt="在这里插入图片描述"> <mark>点击Next</mark>

<img src="https://img-blog.csdnimg.cn/dd385d392edd4cc1a0ec839d39508338.png" alt="在这里插入图片描述"> <mark>点击Yes</mark>

<img src="https://img-blog.csdnimg.cn/eabe9ab6c95544838c76711f5ed7eb06.png" alt="在这里插入图片描述"> <mark>点击Execute</mark> <img src="https://img-blog.csdnimg.cn/ce58f65e33c14d8ebc0ddc6038dd8be4.png" alt="在这里插入图片描述"> <mark>点击Next</mark>

<img src="https://img-blog.csdnimg.cn/88754067402e4ca28cf5340ba275bbe4.png" alt="在这里插入图片描述"> <mark>点击Next</mark>

<img src="https://img-blog.csdnimg.cn/9b051556d42c459183b068f1b4e764e4.png" alt="在这里插入图片描述"> <mark>点击Next</mark>

<img src="https://img-blog.csdnimg.cn/ecfbeb3672424e9282bf10448df43c44.png" alt="在这里插入图片描述"> <mark>点击Next</mark>

<img src="https://img-blog.csdnimg.cn/dc228490e1ed48788fc385f4afd3c2ed.png" alt="在这里插入图片描述"> <mark>设置密码</mark>

<img src="https://img-blog.csdnimg.cn/d08b6521f7f44edfb4406847125ed206.png" alt="在这里插入图片描述"> <mark>点击Next</mark>

<img src="https://img-blog.csdnimg.cn/7302d8ae3d8849e9a61df4681d608a1b.png" alt="在这里插入图片描述"> <mark>点击Execute</mark>

<img src="https://img-blog.csdnimg.cn/b916462fd0b44139a59218f6a47528d0.png" alt="在这里插入图片描述"> <mark>点击Finish完成安装</mark>

<img src="https://img-blog.csdnimg.cn/967f6c064e0f403d8fc7dbadd99011de.png" alt="在这里插入图片描述">

## MySQL服务启动与停止

✅**第一种方法** win+R输入<mark>services.msc</mark>打开电脑服务找到MySQL80右键启动或停止(MySQL服务默认开机自启动)

<img src="https://img-blog.csdnimg.cn/e7de7aca21e84bc6a6ee7e74088840a3.png" alt="在这里插入图片描述">

✅**第二种方法**

命令行以管理员身份运行输入 <mark>net start mysql80</mark> 开启MySQL服务 <mark>net stop mysql80</mark> 停止MySQL服务

<img src="https://img-blog.csdnimg.cn/aeea0c09376e4e5898c1902553a44082.png" alt="在这里插入图片描述">

## 连接客户端

✅方式一：使用MySQL提供的客户端命令行工具 <img src="https://img-blog.csdnimg.cn/cb3f5ac6019646a6974c0eb01c8b59a0.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/af7e45b81ed943f98ec9240e7b0a1571.png" alt="在这里插入图片描述"> ✅方式二：使用系统自带的命令行工具执行指令

💡注意：首先需要<mark>配置一下环境变量</mark> 找到MySQL的**bin**路径 找到系统的环境变量，新建后输入复制的bin路径并确定即可 <img src="https://img-blog.csdnimg.cn/d831053689264e1da3fbf6a46441c7c6.png" alt="在这里插入图片描述"> 1：输入<mark>mysql -u root -p</mark> 2：输入密码

<img src="https://img-blog.csdnimg.cn/34351570e6674f5fb4b50e5a1f944507.png" alt="在这里插入图片描述">

## 结束语🏆

以上就是MySQL基础篇之MySQL数据库安装教程以及配置环境变量，连接数据库。 持续更新MySQL教程，欢迎大家订阅系列专栏  你们的支持就是hacker创作的动力💖💖💖

<img src="https://img-blog.csdnimg.cn/9eb99bb30ab141feadb6bce49e56d265.gif#pic_center" alt="在这里插入图片描述">
