
--- 
title:  [ 攻防演练演示篇 ] 利用 shiro 反序列化漏洞获取主机权限 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ Vulhub是一个面向大众的开源漏洞靶场，无需docker知识，简单执行两条命令即可编译、运行一个完整的漏洞靶场镜像。旨在让漏洞复现变得更加简单，让安全研究者更加专注于漏洞原理本身。 




#### 文章目录
- - - - <ul><li>- - - - - - - - - - - 


## 一、前言

>  
 本次使用于协助搭建一个演示环境，用于给领导演示，这里我利用了一个shiro反序列化漏洞获取主机权限 需要注意的是： 1.靶机环境：我这里采用的是win10 2.靶机采用tomcat启动shiro 3.攻击机采用shiro反序列化工具一键获取主机权限 4.攻击机和靶机都需要有java环境 


## 二、演示环境搭建

>  
 为避免部分小伙伴无法下载，百度网盘下载链接在文末给出 


### 1、靶机和攻击机安装java环境

```
https://download.csdn.net/download/qq_51577576/87379246

```

### 2、下载shiro文件

```
https://download.csdn.net/download/qq_51577576/87380187

```

### 3、下载tomcat

```
https://download.csdn.net/download/qq_51577576/87346570
https://download.csdn.net/download/qq_51577576/87380179

```

### 4、把shiro文件移到tomcat的webapps目录下

```
apache-tomcat-8.5.84\webapps

```

<img src="https://img-blog.csdnimg.cn/f2f07aa9c9dc43219299025319b8d569.png" alt="在这里插入图片描述">

## 三、蓝方操作

### 1、启动tomcat

>  
 进入tomcat目录的bin目录，以管理员身份运行startup.bat 


<img src="https://img-blog.csdnimg.cn/c16642ecfcaa4dfd814a8975f106aa10.png" alt="在这里插入图片描述">

### 2、Tomcat启动成功

<img src="https://img-blog.csdnimg.cn/7e6182e137dc4197977182547a31e89c.png" alt="在这里插入图片描述">

### 3、验证Tomcat启动成功

```
http://靶机ip:8080/shiro/login.jsp

```

<img src="https://img-blog.csdnimg.cn/5d60fa6ee311494d9e54c070850256e7.png" alt="在这里插入图片描述">

## 四、红方操作

### 1、检测shiro框架

>  
 shiro反序列化漏洞检测工具ShiroExp-1.3.1-all.jar下载链接： 


```
https://download.csdn.net/download/qq_51577576/87380651

```

>  
 攻击机双击打开ShiroExp-1.3.1-all.jar，填入url：http://靶机IP:8080/shiro/login.jsp，点击shiro框架检测 


<img src="https://img-blog.csdnimg.cn/845ebf6db0c74f108a43da31ebf64990.png" alt="在这里插入图片描述">

### 2、爆破密钥

>  
 上面的步骤我们发现shiro框架，点击爆破密钥 


<img src="https://img-blog.csdnimg.cn/431077bb2b5348c4afb6fdfe540750b7.png" alt="在这里插入图片描述">

### 3、执行whoami

>  
 上面的步骤结束，我们爆破出了密钥并自动进行了填充 接下来我们就可以执行命令了 我们执行whoami，直接点击执行命令就ok了 


<img src="https://img-blog.csdnimg.cn/e2d5eecac9f94934a8f5e32b668061f7.png" alt="在这里插入图片描述">

### 4、执行dir

<img src="https://img-blog.csdnimg.cn/f167b50fc5a84e26a100d81c95bd013e.png" alt="在这里插入图片描述">

### 5、打开图片

>  
 由于我们是用于演示使用，我们预先再靶机c盘下放了一个1.jpg的图片 


```
start C:\1.jpg

```

<img src="https://img-blog.csdnimg.cn/65a10ac8dfec4f8aa8ca12f44cbc794d.png" alt="在这里插入图片描述">

>  
 蓝方弹出恶意图片 


<img src="https://img-blog.csdnimg.cn/9c0f01c319d541cf85b8d74ac5eae845.png" alt="在这里插入图片描述">

## 六、相关资源

     
