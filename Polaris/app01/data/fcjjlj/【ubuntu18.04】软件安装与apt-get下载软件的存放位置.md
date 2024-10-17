
--- 
title:  【ubuntu18.04】软件安装与apt-get下载软件的存放位置 
tags: []
categories: [] 

---
##### 系统：Ubuntu18.04

##### 服务器：阿里云

常用的软件安装方式有两种：

#### 第一种：`apt-get`（安装后略类似于windows中的安装版软件）：

例：`apt-get install ssh` 1.下载的软件存放位置 `/var/cache/apt/archives` 2.安装后软件默认位置 `/usr/share` 3.可执行文件位置 `/usr/bin` 4.配置文件位置 `/etc` 5.lib文件位置 `/usr/lib`

#### 第二种：手动下载软件安装包（安装后略类似于绿色版软件）：

好处：看着干净（个人觉得） 坏处：版本对应与依赖问题，要搞清楚需要多少依赖包。。。。
