
--- 
title:  [ 常用工具篇 ] kali 忘记 root 密码 -- 修改 root 密码 
tags: []
categories: [] 

---
>  
 🍬 博主介绍 👨‍🎓 博主介绍：大家好，我是 _PowerShell ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - - - - - 


## 一、登录态修改密码

```
sudo passwd root

```

>  
 打开terminal，输入sudo passwd root 要求输入新密码：root，回车，（root为新密码，terminal默认不显示） 要求再次输入新密码：root，回车（root为刚刚输入的新密码，terminal默认不显示） 提示“passwd:passwd updated successfully”这说明密码修改成功 修改完成 


<img src="https://img-blog.csdnimg.cn/0a1a694938d741b29cc5466c3d6a105c.png" alt="在这里插入图片描述">

## 二、非登录态修改密码

### 1、重启kali系统

>  
 重启kali操作系统 


<img src="https://img-blog.csdnimg.cn/f21ecd0aaaee40e29187d83389d1d105.png" alt="在这里插入图片描述">

### 2、重启之后进入这个界面

<img src="https://img-blog.csdnimg.cn/80f6b0eade5d4cbfae89be63da2e1ba8.png" alt="在这里插入图片描述">

### 3、跳转到配置页面

>  
 按下”E“键后，跳到下面这个界面 


<img src="https://img-blog.csdnimg.cn/89b72e67f77c4d84a3caf547e3b673ee.png" alt="在这里插入图片描述">

### 4、修改文件

>  
 将linux行的“ro”改成“rw”，然后空一格，在行末加上init=/bin/bash 


<img src="https://img-blog.csdnimg.cn/7de5ba9f5bbf4fb4be70a6839f06a0a3.png" alt="在这里插入图片描述">

### 5、进入单用户模式

>  
 修改确认无误之后，按F10或者Ctrl+C或者Ctrl+X即可进入单用户模式，如下 


<img src="https://img-blog.csdnimg.cn/bd5837e142c444ebb8e89eeeb055da50.png" alt="在这里插入图片描述">

### 6、修改密码

>  
 修改密码的命令是 


```
passwd 用户名

```

>  
 这里也可以修改其他账户得的密码，不过也没必要，你进入到root模式就可以随便修改普通用户的密码了 这里因为要修改root的密码，所以键入命令 


```
passwd root

```

>  
 然后回车就可以输入新密码了，一共输入两次，密码不显示出来 


<img src="https://img-blog.csdnimg.cn/35c44bdbb3314468aaa80aa3f5e2cc9f.png" alt="在这里插入图片描述">

>  
 输完之后回车就可以了 


### 7、重启kali

>  
 然后ctrl+Alt退出鼠标 然后ctrl+R重启kali 


<img src="https://img-blog.csdnimg.cn/9147bea0ef264613ab168e0e9669ad7f.png" alt="在这里插入图片描述">

### 8、重新登录

>  
 采用更改设置的root密码进行登录 


<img src="https://img-blog.csdnimg.cn/82e86d9d8ef84e90a86ba5a8678dae7c.png" alt="在这里插入图片描述">
