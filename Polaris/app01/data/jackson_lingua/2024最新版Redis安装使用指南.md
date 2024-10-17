
--- 
title:  2024最新版Redis安装使用指南 
tags: []
categories: [] 

---
## 2024最新版Redis安装使用指南

### Installation and Usage Guide to the Latest Redis in 2024

By Jackson@ML

#### 1. 什么是Redis?

**The open-source, in-memory data store used by millions of developers as a cache, vector database, document database, streaming engine, and message broker.**

按照官网定义，Redis是一个开源的、用作缓存数据存储、向量数据库、文档数据库、流式处理引擎，和消息代理的内存数据存储。

>  
 Redis ( Remote DIctionary Server ) 通常被称为数据结构服务器，因为值 ( value ) 可以是字符串 ( String ) , 哈希 ( Map ) , 列表 ( list ) , 集合 ( Sets ) 或有序集合 ( Sorted Sets) 等类型。 Redis 是开源的，遵守 BSD 协议，使用 C 语言开发。 Redis 是互联网技术中使用最为广泛的中间件之一，随着它在新浪微博等众多门户网站的使用而逐渐风靡国内。 


本文简要介绍Redis下载安装和基本使用步骤，希望对广大读者有所帮助。

#### 2. 获取Redis

打开Chrome浏览器，访问Redis官网链接： ，如下图：

<img src="https://img-blog.csdnimg.cn/direct/7afac22133114e16b61707221307ec91.png" alt="在这里插入图片描述"> 点击上方导航栏右侧的蓝色Download按钮。进入到下载页面。

<img src="https://img-blog.csdnimg.cn/direct/b6610db3dda8478da0d61097c90e60ba.png" alt="在这里插入图片描述"> 在左侧Redis区域，点击Download 72.4, 进入到下载页面。

#### 3. 安装Redis

##### 3.1 在Windows Subsystem for Linux安装Redis

打开Windows Subsystem for Linux (即WSL)，最简单的方法是在Windows搜索栏搜索关键字”WSL”, 找到后点击以管理员身份运行。如下图：

<img src="https://img-blog.csdnimg.cn/direct/78a431f07ca24ee985d25872bed42b19.png" alt="在这里插入图片描述"> 此时，打开WSL命令行窗口，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/c152b2eaeb864a58a25f58ba470635e5.png" alt="在这里插入图片描述"> 我们要开始在WSL环境安装Redis，接下来的步骤简明扼要。

###### 1） 添加redis的repository:

运行以下命令，可实现添加redis到repository.

```
sudo apt-add-repository ppa:redislabs/redis

```

如下图所示:

<img src="https://img-blog.csdnimg.cn/direct/9e4612fb4aeb4da59c0364d375c22967.png" alt="在这里插入图片描述"> 按Enter（回车）键继续。如果需要取消，就按Ctrl-C组合键。

<img src="https://img-blog.csdnimg.cn/direct/e664cd6b937140faaf28d667a9f9ee16.png" alt="在这里插入图片描述">

###### 2） 更新软件包

运行以下命令，更新系统软件包：

```
sudo apt-get update

```

更新完毕，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/ace181bfdc2449b6b49785314855e91a.png" alt="在这里插入图片描述">

###### 3） 升级系统软件包

运行以下命令，以升级系统软件包：

```
sudo apt-get upgrade

```

如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/3b365895ac9041cd8c801ff3d910aed0.png" alt="在这里插入图片描述">

###### 4） 安装redis server

运行以下命令，以安装redis server:

```
sudo apt-get install redis-server

```

如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/598919b76466450e9e28465da268e6fb.png" alt="在这里插入图片描述">

###### 5） 重新启动Redis Server

为了启动Redis服务，需要重新启动Redis Server，运行以下命令：

```
sudo service redis-server restart

```

如下图所示:

<img src="https://img-blog.csdnimg.cn/direct/052723aa1956434fa2d9b86952d10f04.png" alt="在这里插入图片描述"> ***注：** 如果需要停止redis-server, 则需运行以下命令：

```
sudo service redis-server stop

```

###### 6） 验证Redis Server在运行状态

运行以下命令:

```
redis-cli

```

出现本地主机提示符（带端口号）。

###### 7） 连接到数据库命令：

```
set user:1 “Jackson”

```

如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/2ac0eb26ef7c4cf7b3e4e1544c153861.png" alt="在这里插入图片描述"> 看到**用户Jackson被设置成功！显示OK**。

再运行get user命令，获取用户信息：

```
get user:1

```

如下图所示： <img src="https://img-blog.csdnimg.cn/direct/22df8402b3ed40eda42cc3968f5e19c8.png" alt="在这里插入图片描述">

*注：默认情况下，Redis 有 0-15 个数据库索引，你可以在 redis.conf 中更改该编号的数据库 NUMBER。

##### 3.2 用MSI安装包安装Redis

###### 1） 下载Redis的MSI安装包

使用以下链接，下载用于Windows安装向导的安装包： , 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/34c25c2f4ea94fb7b21011bd9b2ba4cc.png" alt="在这里插入图片描述"> 点击Assets列表中列出的Redis-x64-3.0.504.msi安装包，进行下载。

###### 2） 完成安装

***注：** 下载完毕后，可以双击安装包可执行文件，依照安装向导提示，完成安装。

由于github上这个版本不是最新的安装包，上传于2016年，因此，安装过程不再详述。

技术好文陆续推出，敬请关注。 您的认可，我的动力！😃

#### 相关阅读
1. 1. 1. 1. 