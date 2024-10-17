
--- 
title:  win系统下安装php8.3版本并配置环境变量的详细教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解在win系统下安装和配置php8.3版本，并配置环境变量的详细教程。 日期：2024年2月22日 作者：任聪聪 


## 一、下载php8.3版本包

php8.3版本官方下载地址：https://windows.php.net/download#php-8.3

### 步骤一、打开下载地址，进入后如图选择合适的安装包：

<img src="https://img-blog.csdnimg.cn/direct/0821f55bbef248c9b4ce1c4a3cb43a20.png" alt="在这里插入图片描述">

### 步骤二、解压缩下载好的zip包

<img src="https://img-blog.csdnimg.cn/direct/87bfe55e235b490c8035e10619a710ee.png" alt="在这里插入图片描述">

### 步骤三、复制解压的php包并移动到自己的开发目录或者专门存放环境的目录中

<img src="https://img-blog.csdnimg.cn/direct/4ee8525439844b2c96b257c3a9ab6218.png" alt="在这里插入图片描述">

## 二、配置环境变量

### 步骤一、打开搜索，输入 环境变量如下图：

<img src="https://img-blog.csdnimg.cn/direct/0583b3403b39402186fef433bfd041fe.png" alt="在这里插入图片描述">

### 步骤二、点击进入设置，找到环境变量配置，如下图。

<img src="https://img-blog.csdnimg.cn/direct/1898dcca1ee54ced869ae823ec3a29ad.png" alt="在这里插入图片描述">

### 步骤三、进入到环境变量配置界面，找到path的配置，并双击，进入到如下界面：

<img src="https://img-blog.csdnimg.cn/direct/99a747af9f0a44ce8d3bbe058406dfb1.png" alt="在这里插入图片描述">

### 步骤四、双击之前的环境变量进行替换目录，如下图。

<img src="https://img-blog.csdnimg.cn/direct/d69d56be38f84c94b3da9daa838d3bd7.png" alt="在这里插入图片描述"> or 或者点击添加，选择新的变量路径 <img src="https://img-blog.csdnimg.cn/direct/ed1db2691615431b82668d671c6489cb.png" alt="在这里插入图片描述">

### 步骤五、打开cmd，win+r，输入cmd如下图：

<img src="https://img-blog.csdnimg.cn/direct/f3960fb5fbf14c84b7c20f8b40f43113.png" alt="在这里插入图片描述"> end：点击确定，进入到cmd的界面。

## 三、cmd输入php -v 检测是否安装完成

说明：进入到cmd，输入php -v，显示如下，则为安装和配置环境变量完成，如果提示php命令不存在，记得检查路径是否存在空格，或者下载的版本不对。 <img src="https://img-blog.csdnimg.cn/direct/1e1cb52ace2940618a3550143c0f34cf.png" alt="在这里插入图片描述">
