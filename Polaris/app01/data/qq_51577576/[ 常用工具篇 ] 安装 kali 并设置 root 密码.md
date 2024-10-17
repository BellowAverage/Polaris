
--- 
title:  [ 常用工具篇 ] 安装 kali 并设置 root 密码 
tags: []
categories: [] 

---
​

>  
 🍬 博主介绍 👨‍🎓 博主介绍：大家好，我是 _PowerShell ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - 


## 一、下载kali

```
https://www.kali.org/get-kali/#kali-virtual-machines

```

<img src="https://img-blog.csdnimg.cn/627de2e06cf1451fae1080951e884b96.png" alt="在这里插入图片描述">

## 二、在VMware中打开kali

>  
 把下载的压缩包进行解压 


<img src="https://img-blog.csdnimg.cn/0a6cb7ee1c4e457ea134b2052a41d2b8.png" alt="在这里插入图片描述">

>  
 解压完成之后双击打开vmx文件 


<img src="https://img-blog.csdnimg.cn/0a497917f9754bb59621398e1cad217f.png" alt="在这里插入图片描述">

>  
 自动跳转到vm并打开 


<img src="https://img-blog.csdnimg.cn/4bf7e331c7e94d6488dc2518bb1a1d86.png" alt="在这里插入图片描述">

## 三、设置root密码

### 1、首先使用默认账户密码登录

```
kali	
Kali

```

<img src="https://img-blog.csdnimg.cn/5a88d793be3743939960c2a28464e534.png" alt="在这里插入图片描述">

### 2、设置root密码

```
sudo passwd root

```

>  
 输入命令：sudo passwd root [sudo] password for kali: （输入默认密码kali） New password: （root密码） Retype new password: （root密码确认） passwd: password updated successfully 


<img src="https://img-blog.csdnimg.cn/f947bd758bfb4e228a4dc0b23de04cdf.png" alt="在这里插入图片描述">

>  
 切换到root权限 


```
su root

```

<img src="https://img-blog.csdnimg.cn/f22af1523fa94db9a55ffe721af5363a.png" alt="在这里插入图片描述">

>  
 提示符$代表一般用户，提示符#代表 root用户 


### 3、采用root账号登录

>  
 刚刚设置的账号密码 


<img src="https://img-blog.csdnimg.cn/396cea7273d742f4acae20bce077e8dd.png" alt="在这里插入图片描述">

>  
 打开终端看，直接就是root权限了 


<img src="https://img-blog.csdnimg.cn/3951944e50cd46bda3ed096d7d172435.png" alt="在这里插入图片描述">

## 四、kali修改密码

```
sudo passwd root

```

>  
 打开terminal，输入sudo passwd root 要求输入新密码：root，回车，（root为新密码，terminal默认不显示） 要求再次输入新密码：root，回车（root为刚刚输入的新密码，terminal默认不显示） 提示“passwd:passwd updated successfully”这说明密码修改成功 修改完成 


<img src="https://img-blog.csdnimg.cn/59b044a995c34e9d8ade9e6f033374f5.png" alt="在这里插入图片描述">
