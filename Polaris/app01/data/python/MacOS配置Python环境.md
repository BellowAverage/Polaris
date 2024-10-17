
--- 
title:  MacOS配置Python环境 
tags: []
categories: [] 

---
## python简介

>  
 Python是用来编写应用程序的高级编程语言。 Python就为我们提供了**非常完善的基础代码库**，覆盖了网络、文件、GUI、数据库、文本等大量内容，被形象地称作“内置电池（batteries included）”。 用Python开发，许多功能不必从零编写，直接使用现成的即可。 


Python适合的开发项目：

>  
 网络应用，包括网站、后台服务等等； 许多日常需要的小工具，包括系统管理员需要的脚本任务等等； 另外就是把其他语言开发的程序再包装起来，方便使用。 


当然，python也有缺点：

>  
 python和C程序相比非常慢。 因为Python是解释型语言，你的代码在执行时会一行一行地翻译成CPU能理解的机器码，这个翻译过程非常耗时，所以很慢。 而C程序是运行前直接编译成CPU能执行的机器码，所以非常快。 


## Mac下配置python开发环境

（1）Mac OS X系统自带python，可以在终端输入python查看版本【输入exit()即可退出】，如下：

当然，可以看出，系统自带的python2.7版本已经不推荐使用了，通俗一点说，也就是绝版了。

（2）Python安装方法：

Mac OS下安装Python主要方式有两种：
-  Homebrew安装 -  官网下载安装 
### **Homebrew安装**
1. 安装套件管理工具-Homebrew
Homebrew官网获取安装指令，官网地址：https://brew.sh/

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

若以上安装失败，并提醒：

Failed to connect to  port 443: Connection refused.

则可以尝试使用国内源进行安装，详情请看 。（或者科学上网）
1. 安装python3，终端指令安装
```
安装指令：brew install python3

```
1. 验证安装成功
终端输入指令：python3，显示下图信息即安装成功

### **官网下载安装**
1. 访问（https://www.python.org/downloads，下载安装Python安装包，一路点击安装即可。
### 其他操作

终端输入以下命令，查看Python安装位置 `which python`

终端输入以下命令，查看Python当前版本 `python --version`

终端输入以下命令，进入Python交互模式 `python`
