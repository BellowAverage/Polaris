
--- 
title:  [ 问题解决篇 ] 设置windows密码策略并且更改用户密码 -- 解决windwos密码无法设置为1的问题 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - - - - - - - - - - - - 


## 一、前言

>  
 由于我们给客户制作的演示环境中，靶场密码传不需要设置为1，而windows有一些安全策略，需要绕过安全策略修改密码为简单口令 这里我演示两台机器，一台win10，一台winserver2008 


## 二、win10更改密码复杂度

### 1、打开运行窗口

>  
 在桌面上按下Win键+R键，打开“运行”窗口。 


<img src="https://img-blog.csdnimg.cn/e37c594f021f46daac00b2ac8ee91762.png" alt="在这里插入图片描述">

### 2、打开组策略窗口

>  
 输入“gpedit.msc”，打开“组策略”窗口。 


<img src="https://img-blog.csdnimg.cn/364a85e62706415f981296559ec452b5.png" alt="在这里插入图片描述">

### 3、进入密码策略窗口

>  
 在“组策略”窗口中依次选择“计算机配置”&gt;“Windows设置”&gt;“安全设置”&gt;“账户策略”&gt;“密码策略”。进入“密码策略”设置窗口。 


<img src="https://img-blog.csdnimg.cn/f0304156f62d4d6aa14447fcae02a4f9.png" alt="在这里插入图片描述">

### 4、根据自己要求设置密码复杂度

>  
 因为我要把我的靶机密码设置为1，我就吧密码复杂度相关的全部关了 


<img src="https://img-blog.csdnimg.cn/30146b9c679046d4bff827c11da1a88a.png" alt="在这里插入图片描述">

## 二、win10更改密码

### 1、打开你的账户信息

>  
 进入电脑“搜索”功能搜索“账户”，打开“你的账户信息”； 


<img src="https://img-blog.csdnimg.cn/89905ee09dc0417989f68c437fb607f1.png" alt="在这里插入图片描述">

### 2、更改密码

>  
 在出现的账户界面，左边列表栏找到“登陆选项”，点击选择。找到密码，选择点击更改的按钮。 


<img src="https://img-blog.csdnimg.cn/12ecdf5d922f4e58aaafbdaf3741fd73.png" alt="在这里插入图片描述">

>  
 填写当前密码 


<img src="https://img-blog.csdnimg.cn/7d16ab9090694e8d876fecf7d460f3eb.png" alt="在这里插入图片描述">

>  
 填写新密码 


<img src="https://img-blog.csdnimg.cn/09a8f02f71f74e12bfb0826a6b043990.png" alt="在这里插入图片描述">

### 3、修改完成

>  
 修改完成 


<img src="https://img-blog.csdnimg.cn/f98ce12e337546d5b39932a5707c702a.png" alt="在这里插入图片描述">

>  
 填入密码1<img src="https://img-blog.csdnimg.cn/b97f5bc743ac49dbbd2f24718dc111d6.png" alt="在这里插入图片描述"> 


## 三、winserver2008更改密码复杂度

### 1、打开组策略窗口

<img src="https://img-blog.csdnimg.cn/3bf228c6d4754427ba3bbbe978f3a1d2.png" alt="在这里插入图片描述">

>  
 搜索“gpedit.msc”，打开“组策略”窗口。 


<img src="https://img-blog.csdnimg.cn/177de7882de544b290ddd017032b816a.png" alt="在这里插入图片描述">

### 2、进入密码策略窗口

>  
 在“组策略”窗口中依次选择“计算机配置”&gt;“Windows设置”&gt;“安全设置”&gt;“账户策略”&gt;“密码策略”。进入“密码策略”设置窗口。 


<img src="https://img-blog.csdnimg.cn/95dd4abb30bf4f53ac84ce6cd10ae709.png" alt="在这里插入图片描述">

## 四、winserver2008更改密码

### 1、打开控制面板

<img src="https://img-blog.csdnimg.cn/97bc5c4c8fa148b58b7000b40922a9bf.png" alt="在这里插入图片描述">

### 2、找到用户账户

<img src="https://img-blog.csdnimg.cn/0788d36c55f84b498d61004312d6d9e4.png" alt="在这里插入图片描述">

### 3、选择更改密码

<img src="https://img-blog.csdnimg.cn/c817eb8fac7f42e28bd138805317b47e.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/284b12a129094019bf1d5e3c81ad712f.png" alt="在这里插入图片描述">

### 4、输入新密码

<img src="https://img-blog.csdnimg.cn/49556ace7edd4cb9adc547910e305715.png" alt="在这里插入图片描述">

### 5、修改完成

>  
 登录成功 


<img src="https://img-blog.csdnimg.cn/2e2f6d0569154e22a66c7b8e82e4ff5e.png" alt="在这里插入图片描述">
