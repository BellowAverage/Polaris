
--- 
title:  Python实现疫情医疗信息管理系统(附源码) 
tags: []
categories: [] 

---
### 前言 

本项目使用Python的pymssql第三方库连接sqlserver数据库，使用tkinter进行UI界面开发，使用ttkthemes ttkbootstrap进行界面美化，详细介绍项目执行过程。

### 环境 

Python3.8、sqlserver2019

### 数据库准备 

使用MSSQL Manager Studio导入数据库文件

**数据库使用sqlserver身份验证，使用sa账户登录，密码123456，端口1433**

首次使用可能会遇到无法连接的情况，需要进行特殊配置，可以找一找相关资料，这里大致说一下，首先要在MSSQLMS中启用sa的登录名，修改密码为123456，然后查看sql资源配置管理器的TCP/IP协议127.0.0.1是否开启，TCP/IP协议是否开启，开启后重启sql服务。（插播一条广告：需要开通正版PyCharm的可以联系我，56元一年，正版授权激活，官网可查有效期，有需要的加我微信：poxiaozhiai6，备注：907。）

### Python环境配置 

使用miniconda配置python38环境（已配置可以忽略，不会配置可以私信我，我发给你教程。）

进入项目文件夹，输入以下命令安装第三方库：

```
&gt; pip install -r requirements
```

至此环境已经配置完毕。

### 如何运行项目？ 

#### 第一种运行方式：在命令行执行

首先打开这个EIMSystem文件夹

打开后界面如下：

在地址栏输入cmd

然后回车

输入conda activate python38 进入python虚拟环境，地址前会有（python38）字样

输入python main.py运行文件

用户名：admin 密码：123456

添加病例截图

修改病例截图

#### 第二种运行方式：Visual Studio执行

使用VS打开项目文件夹，点击main.py文件，选择Python38的环境，然后点击运行即可，我没有VS就不截图了。

### 源码获取 

在公众号**Python小二**👆后台回复**py医疗**获取

推荐阅读  点击标题可跳转
- - - - - - - - 