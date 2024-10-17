
--- 
title:  2024最新版MySQL安装使用指南 
tags: []
categories: [] 

---
## 2024最新版MySQL安装使用指南

### Installation and Usage Guide to the Latest Oracle MySQL in 2024

By Jackson@ML

#### 1. MySQL简介

>  
 MySQL是世界上最受欢迎的开源数据库之一。MySQL属于Oracle（甲骨文）公司的产品，其具有强大的功能，但非常易于配置和使用。 包括 Facebook、Twitter、Booking.com 和 Verizon 在内的许多全球规模最大、发展最快的组织都依靠 MySQL 来节省时间和金钱，为其大容量网站、关键业务系统和打包软件提供支持。 


本文简要介绍MySQL安装配置的简单步骤，及启动并运行 MySQL，同时介绍如何使用 mysql 客户端对 MySQL 执行一些基本操作。

#### 2. MySQL最新世界排名

根据db-enginenes.com 相关报道，2024年2月MySQL排名世界最流行的数据库第二位。Oracle当之无愧地排名第一，而微软的SQL Server则位列第三，PostgreSQL, MongoDB, Redis紧随其后。

#### 3. 安装和启动MySQL

##### 1） 下载MySQL

打开Chrome浏览器，访问MySQL官网链接： ，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/cbaaa37ee5844f978fb884466edfc2b3.png" alt="在这里插入图片描述"> 在导航栏点击 **DOWNLOADS** (下载)， 进入到下载页面。

<img src="https://img-blog.csdnimg.cn/direct/9a37e669ab294a3b8b5fa6d26d46ea0b.png" alt="在这里插入图片描述"> 将鼠标滚轮下滑，到页面下方点击MySQL Community Server, 点击进入分类下载页面。

<img src="https://img-blog.csdnimg.cn/direct/f4147e9d985c4af294051998ebe7d4b8.png" alt="在这里插入图片描述"> 按照默认选项，及最新版8.3.0 Innovation, 以及Microsoft Windows操作系统。 <img src="https://img-blog.csdnimg.cn/direct/d7f4b3eac8fb41d6a33010050eb5e9d9.png" alt="在这里插入图片描述"> 选择Windows MSI Installer， 点击 **Download** 开始下载。

<img src="https://img-blog.csdnimg.cn/direct/e7280a667a944db7878433f83b2e0cc9.png" alt="在这里插入图片描述"> 要求登录，使用先前注册的帐号登录。

*如果没有注册，可以点击 **Sign Up**按钮注册新账号；注册完毕系统会发邮件验证，打开邮箱点击Verify Your Email即可验证完成。

验证成功后，页面显示Success. Your account is ready to use. 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/9924b8514c5c4931a24ef21c8661f72c.png" alt="在这里插入图片描述"> 返回到下载页面。

或者，无需注册直接点击 No thanks, just start my download, 则Chrome浏览器开始下载。

##### 2） 安装MySQL Shell

下载完毕，在Windows下载文件夹，找到安装可执行文件 **mysql-shell-8.3.0-windows-x86-64bit.msi**, 双击它开始安装向导。

<img src="https://img-blog.csdnimg.cn/direct/68961d706ad2427b9d17fad322a12c79.png" alt="在这里插入图片描述"> 点击Next继续下一步。 <img src="https://img-blog.csdnimg.cn/direct/90da296663244ff199588ea89114bd8f.png" alt="在这里插入图片描述"> 复选I accept the terms in the License Agreement (我同意许可证协议条款)， 点击Next继续。

<img src="https://img-blog.csdnimg.cn/direct/ebaefd1e72144d9c88c8cacce654509a.png" alt="在这里插入图片描述"> 在目的文件夹对话框，修改默认路径为D:\MySQL8.3，点击Next继续。

<img src="https://img-blog.csdnimg.cn/direct/85a9ef78904c4aa09d4e5017524c80df.png" alt="在这里插入图片描述"> 点击Install安装，如下图：

<img src="https://img-blog.csdnimg.cn/direct/a6a83d2391e240019012592e4e540e85.png" alt="在这里插入图片描述"> 安装很快完成，如下图。

<img src="https://img-blog.csdnimg.cn/direct/db9e2f440826405b99e5f2e193b84eb6.png" alt="在这里插入图片描述"> 点击Finish结束安装向导。

#### 3） 启动MySQL

在安装结束的同时，安装向导默认选择Launch MySQL Shell, 此时会自动启动MySQL Shell。如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/cbb8009a67524ff7aaa214c430ed65ba.png" alt="在这里插入图片描述"> 或者，在Windows启动后，在命令行提示符(cmd)下执行以下命令：

```
mysqlsh

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/67727d5b2dd94bbdaa6c339e13a73f6f.png" alt="在这里插入图片描述"> 很显然，启动MySQL效果相同。

#### 4. 创建和使用MySQL数据库

由于MySQL是典型的关系型数据库，因此，SQL（结构化查询语言）理所当然地畅行无阻。现在，我们需要创建一个新的数据库。

因默认环境以JS提示符启动，意味着可用JavaScript连接数据库。 但是现在需要使用SQL来创建和连接，则用以下命令：

```
\sql

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/37e60c95dee54e96be6e4388e37f2360.png" alt="在这里插入图片描述"> 切换到SQL提示符，可以使用SQL语言来操作了！
- 创建数据库，运行以下命令：
```
CREATE DATABASE JACKSON_DB;

```
- 查看已创建的数据库：
```
SHOW DATABASES;

```

*查看已创建的数据库表：

```
SHOW TABLES FROM JACKSON_DB;

```
- 使用创建的数据库：
```
USE JACKSON_DB;

```
- 删除创建的数据库：
```
DROP DATABASE JACKSON_DB;

```

虽然用到MySQL Shell, 但仍有Windows版安装向导，可用GUI管理数据库；后续将持续介绍。

技术好文陆续推出，敬请关注。

您的鼓励，我的动力！ 😃

#### 相关阅读
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 