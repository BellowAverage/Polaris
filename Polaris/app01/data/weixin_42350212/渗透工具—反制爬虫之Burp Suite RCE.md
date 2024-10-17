
--- 
title:  渗透工具—反制爬虫之Burp Suite RCE 
tags: []
categories: [] 

---
## 一、前言

Headless Chrome是谷歌Chrome浏览器的无界面模式，通过命令行方式打开网页并渲染，常用于自动化测试、网站爬虫、网站截图、XSS检测等场景。

近几年许多桌面客户端应用中，基本都内嵌了Chromium用于业务场景使用，但由于开发不当、CEF版本不升级维护等诸多问题，攻击者可以利用这些缺陷攻击客户端应用以达到命令执行效果。

本文以知名渗透软件Burp Suite举例，从软件分析、漏洞挖掘、攻击面扩展等方面进行深入探讨。

### 二、软件分析

以Burp Suite Pro v2.0beta版本为例，要做漏洞挖掘首先要了解软件架构及功能点。

将`burpsuite_pro_v2.0.11beta.jar`进行解包，可以发现Burp Suite打包了Windows、Linux、Mac的Chromium，可以兼容在不同系统下运行内置Chromium浏览器。

<img alt="-w869" src="https://img-blog.csdnimg.cn/img_convert/daa911e8dd10a1637d58dc04ea67e375.png">

在Windows系统中，Burp Suite v2.0运行时会将`chromium-win64.7z`解压至`C:\Users\user\AppData\Local\JxBrowser\browsercore-64.0.3282.24.unknown\`目录

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/36e68a430f7e6e598bf2ec99af47a282.png">

从目录名及数字签名得知Burp Suite v2.0是直接
