
--- 
title:  Python用20行代码实现完整邮件功能 [完整代码+建议收藏] 
tags: []
categories: [] 

---
>  
 大家好，我是Lex 喜欢欺负超人那个Lex 
 擅长领域：python开发、网络安全渗透、Windows域控Exchange架构 
 今日重点：python脚本实现发送邮件，邮件添加附件，读取接收邮件等功能。 
 包含完整脚本哦，【建议收藏】 


 今天带大家实现一下，不登录邮箱界面

通过python代码实现发送邮件、添加附件、接收邮件的功能。

如下：使用网易126邮箱进行演示。

还可以添加小姐姐的可可爱爱的照片作为附件

<img alt="" height="400" src="https://img-blog.csdnimg.cn/20210715104717168.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="403">



#### **先上效果**

<img alt="" height="627" src="https://img-blog.csdnimg.cn/2021071510171259.gif" width="628">



#### 一、邮箱端设置

首先，要对邮件进行一下设置，在邮箱端获取一个授权码。

**1、首先登录网页版126邮箱**


