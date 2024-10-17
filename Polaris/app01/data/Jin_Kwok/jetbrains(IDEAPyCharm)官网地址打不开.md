
--- 
title:  jetbrains(IDEA/PyCharm)官网地址打不开 
tags: []
categories: [] 

---
## jetbrains(IDEA/PyCharm)官网地址打不开

今天新换了Mac Pro M1，准备重新下载 IDEA 并安装，却发现IDEA  根本打不开，于是我又尝试下载 PyCharm ，同样打不开。考虑到两个 IDE 的开发商相同，初步判断是某种配置问题。

### 1.官网地址
- IDEA：；- PyCharm：
### 2.问题溯源

打开 hosts 文件（目录：/etc/hosts），发现如下信息：

>  
 #config for idea 0.0.0.0 account.jetbrains.com 


很明显，通过配置hosts，将 jetbrains 官网地址进行了转义，因此无法打开相应网址。为什么会这样呢？原来，之前安装过破解版的 IEDA，破解的时候在host文件中禁止了与Idea的联网（防止自动更新）。更换新电脑时，使用了Mac自带的迁移助理（实用工具/迁移助理），因此将旧Mac的hosts文件也迁移了。

### 3.问题解决

知道了原因，解法也就简单了——修改hosts文件，将 0.0.0.0 account.jetbrains.com 注释掉（或者删除）即可。
