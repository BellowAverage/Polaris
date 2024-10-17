
--- 
title:  如何在Linux系统上刷抖音 
tags: []
categories: [] 

---
自从抖音出了网页版

很多小伙伴，上班刷起来了

今天，写一篇教大家如何使用linux刷抖音

<img alt="" height="201" src="https://img-blog.csdnimg.cn/de0537b9d45a460cba5fd5209798925b.png" width="298">

 



抖音入驻PC端之后，其实就是一个终端的网站页面

看看我们如何在Linux端，

完成搜索、截图、访问网页等等功能



#### **一、首先增加一下新yum**

```
vim /etc/yum.repo.d/google-chrome111.repo   
```

#### **二、调整内容**

>  
 [yum源名称] name=google-chrome baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64 enabled=1 gpgcheck=1 gpgkey=https://dl.google.com/linux/linux_signing_key.pub 


<img alt="" height="119" src="https://img-blog.csdnimg.cn/4baf8d424f034bfdabf88a16dc81d139.png" width="582">

 

#### **三、yum安装goglechrome**

```
#安装
[root@harxxx ~]# yum -y install google-chrome-stable --nogpgcheck
```

<img alt="" height="293" src="https://img-blog.csdnimg.cn/86fc81cfd5cb46ed9f203796a06a5e86.png" width="654">

 

#### **四、我们来看看是啥版本**

```
#查看-版本-信息
[root@har ~]# google-chrome -version
Google Chrome 91.0.4472.106 
[root@har ~]# 
```

#### **五、shell脚本玩转浏览器**

**1、shell使用浏览器**

>  
 #直接输入百度及搜索内容 #截屏百度 [root@harbor tmp]# google-chrome --no-sandbox --headless --disable-gpu --screenshot https://www.baidu.com/ 
 [0615/170830.274431:WARNING:headless_browser_main_parts.cc(106)] Cannot create Pref Service with no user data dir. [0615/170830.329462:ERROR:gpu_init.cc(440)] Passthrough is not supported, GL is swiftshader [0615/170831.542038:INFO:headless_shell.cc(648)] Written to file screenshot.png. 


**2、查询搜索结果**

>  
 #截屏百度 [root@harbor tmp]# google-chrome --no-sandbox --headless --disable-gpu --screenshot https://www.baidu.com/ 
 [0615/170830.274431:WARNING:headless_browser_main_parts.cc(106)] Cannot create Pref Service with no user data dir. [0615/170830.329462:ERROR:gpu_init.cc(440)] Passthrough is not supported, GL is swiftshader [0615/170831.542038:INFO:headless_shell.cc(648)] Written to file screenshot.png. 


**效果如下 ↓ ↓ ↓**

<img alt="" height="548" src="https://img-blog.csdnimg.cn/20210620223506395.gif" width="1019">

**4、命令行搜索欧洲杯足球宝贝**

linux会在命令行搜索并保存 足球宝贝的搜索结果

```
#我们看看都搜到了什么
[root@harbor tmp]# google-chrome --no-sandbox --headless --disable-gpu 
--screenshot https://www.baidu.com/s?wd=%E8%B6%B3%E7%90%83%E5%AE%9D%E8%B4%9D

[0615/170830.274431:WARNING:headless_browser_main_parts.cc(106)] Cannot create Pref Service with no user data dir.
[0615/170830.329462:ERROR:gpu_init.cc(440)] Passthrough is not supported, GL is swiftshader
[0615/170831.542038:INFO:headless_shell.cc(648)] Written to file screenshot.png.
```

**5、在命令行打开抖音直播页面 是这样的**

<img alt="" height="651" src="https://img-blog.csdnimg.cn/80c5354a4cb54424a07c41a08d0ce4bb.png" width="982">



#### 六、linux上使用百度搜索

**1、搜索命令**

>  
 [root@localhost tmp]# google-chrome-stable --no-sandbox --headless --disable-gpu --dump-dom https://www.baidu.com/ 


**2、直接访问，看结果**

<img alt="" height="614" src="https://img-blog.csdnimg.cn/20210620221714816.gif" width="916">

**3、搜到效果如下**

例如，使用浏览器 打开 抖音网址 结果如下：

#### <img alt="" height="613" src="https://img-blog.csdnimg.cn/8e5242de1df1411ca2f8ed3b174ea670.png" width="1200">



#### 推荐阅读

**<strong>**</strong>

**<strong>**</strong>

**<strong>** </strong>

**<strong>**</strong>



**<strong>**</strong>



















#### **渗透测试专用系统**












