
--- 
title:  [ 常用工具篇 ] 解决kali英文操作不方便的问题 -- kali 设置中文界面 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - - - - - - 


## 一.前言

>  
 在安装完 kali linux时，操作系统默认语言为英文的，我们操作起来比较麻烦，这里出大家一个汉化教程，有需要的可以把操作系统设置为中文 


## 二.操作步骤

### 1、进入kali操作系统，打开终端查看默认语言

>  
 当前系统语言为英文 


<img src="https://img-blog.csdnimg.cn/8931b80d1bd84f14ae6ff76ff5c811b0.png" alt="在这里插入图片描述">

### 2、在终端中执行dpkg-reconfigure locales命令

```
dpkg-reconfigure locales

```

<img src="https://img-blog.csdnimg.cn/32869c144d7f4287a3163a12852e598c.png" alt="在这里插入图片描述">

>  
 注意： 如果是root用户可直接执行dpkg-reconfigure locales命令 如果是kali用户则需先切换成root用户登陆再进行执行 Kali用户切换到root，执行su root输入密码即可完成切换 


### 3.回车之后跳转到该页面

<img src="https://img-blog.csdnimg.cn/01774fd1cb9d49e5b678d50601fee696.png" alt="在这里插入图片描述">

### 4.取消en_US.UTF-8 UTF-8

>  
 找到en_US.UTF-8 UTF-8选项，按空格键将其进行取消 


<img src="https://img-blog.csdnimg.cn/7c5d3f4b1fef46d28c0a27e22f6d71b6.png" alt="在这里插入图片描述">

>  
 取消完成之后，en_US.UTF-8 UTF-8已取消 


<img src="https://img-blog.csdnimg.cn/3e5f4a9da7754c95b00a4b5ad3b1f9d4.png" alt="在这里插入图片描述">

### 5.勾选zh-CN.UTF-8.UTF-8

>  
 勾选zh-CN.UTF-8.UTF-8 


<img src="https://img-blog.csdnimg.cn/237019ce8d174bab8b40495d775e74cd.png" alt="在这里插入图片描述">

### 6.勾选完毕以后，按回车（enter），进行下一步

<img src="https://img-blog.csdnimg.cn/f364de918d3c421bbe357d0fb2cc3b5d.png" alt="在这里插入图片描述">

### 7. 选择zh_CN.UTF-8字符编码

>  
 选择zh_CN.UTF-8字符编码，按回车（enter）就完成了设置，但是我们操作系统还是英文的，我们需要重启才能生效 


<img src="https://img-blog.csdnimg.cn/7fc8c7cbcbb843b88a66bb05636677d5.png" alt="在这里插入图片描述">

### 8.重启kali操作系统

>  
 重启完毕以后，可以看到相关登陆登陆页面已经是中文显示了，至此配置完毕。 


<img src="https://img-blog.csdnimg.cn/a6669034d40146a0b8b4493c88384275.png" alt="在这里插入图片描述">

## 三.总结

>  
 1.打开终端，查看当前系统语言为默认英文 2.在终端中执行dpkg-reconfigure locales命令 3.使用空格键取消勾选en_US.UTF-8 UTF-8选项 4.勾选[ ] zh-CN.UTF-8.UTF-8两个选项 5.使用reboot命令重启机器使其配置生效 

