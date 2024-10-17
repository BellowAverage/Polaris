
--- 
title:  python环境配置教程 
tags: []
categories: [] 

---
## 一、下载和安装软件

进入，下载所需的python版本 <img src="https://img-blog.csdnimg.cn/00d23f8a663d4553a319e3e06d411a32.png" alt="在这里插入图片描述"> 进入，下载社区版即可 <img src="https://img-blog.csdnimg.cn/f457198fbe984653afe740f5e190d707.png" alt="在这里插入图片描述"> 两个软件安装，基本安装默认配置即可，选择环境变量时建议选一下（或者后面自行添加）

## 二、建立代码项目

本地建个文件夹，然后打开pycharm，选择open project（截图错过了，很简单就不补了）

## 三、配置虚拟环境

也可以使用安装的python本身作为解释器，但还是建议创建虚拟环境，因为这样便于项目管理。 <img src="https://img-blog.csdnimg.cn/3a176699a962422fadd526db29311098.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1ad57a5c410d4b75876ff776b69a7190.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c24ac84ab49644dba9be551d072e9f6e.png" alt="在这里插入图片描述"> 然后返回，选择刚才配置的虚拟环境就行。 <img src="https://img-blog.csdnimg.cn/33ff8a90883043d8906c8329c2769155.png" alt="在这里插入图片描述">

## 四、安装需要的包

### 安装方式

可以用cmd打开命令行窗口，也可以直接pycharm打开终端窗口编辑。 然后采用pip install 命令安装所需要的包 <img src="https://img-blog.csdnimg.cn/5e4d3f30bbd445c6bc1100e4a182b162.png" alt="在这里插入图片描述">

### 打开终端报异常的问题修复

对于上图红字的部分，是报错了，需要按照以下方法解决：
1. 用管理员身份打开"Windows Powershell"1. 输入set-executionpolicy remotesigned1. 键入 [Y]
### 安装需要的包

<img src="https://img-blog.csdnimg.cn/22e25ede3f81409c8b320a798b701da7.png" alt="在这里插入图片描述">

### 数据分析常用的包

pip install pandas === 这个会自动把其他一些依赖包安装好，比如numpy等 pip install pymysql pip install seaborn

**<font color="red">未完待续~~~</font>**
