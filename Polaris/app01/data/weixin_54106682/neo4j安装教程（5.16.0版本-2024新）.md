
--- 
title:  neo4j安装教程（5.16.0版本-2024新） 
tags: []
categories: [] 

---
**引言：**前段时间下载了21版本的java，但neo4j是3.5的旧版本，需要jdk1.8的支持，不想来回切换，干脆把neo4j也换成最新版本。然后进到neo4j的官网，我勒个豆，官网布局也是一整个大变动，找了好久zip安装包的下载地方。所以咧，将教程也同步分享给大噶。另外，再感慨一下！java更新的也忒快了，之前印象里11就挺新的了，一下子干到21版本了！

#### Neo4j 版本和 JVM 要求

neo4j依赖需求官方文档：

我们这里主要注意neo4j与java的兼容版本：

<img alt="" height="505" src="https://img-blog.csdnimg.cn/direct/c4177f002e574a1f828c1b290c489a2d.png" width="1200">由于目前我电脑上其他软件依赖于java21，因此，这里neo4j我选择的是最新版5.16.0版本，其他版本neo4j下载大家可以参考上述表格与自己所有java环境进行决定。

java21版本下载教程与多版本java自由切换教程，大家可以参考该篇文章：

#### 安装教程

官方下载网址：

<img alt="" height="823" src="https://img-blog.csdnimg.cn/direct/07b7ff3d582f4074bbb9168d2c841205.png" width="1200"> 下载成功后，将zip压缩包进行解压。

进入D:\neo4j-community-5.16.0-windows\neo4j-community-5.16.0\bin目录下，点击鼠标右键，选择在终端打开，在cmd中输入命令：neo4j.bat console

<img alt="" height="714" src="https://img-blog.csdnimg.cn/direct/476700e3d9044fe4a18e710ae041a4a6.png" width="1200">

如图，之后访问

<img alt="" height="1183" src="https://img-blog.csdnimg.cn/direct/4e7b19736a5d4b6da167d5c42c90fc46.png" width="1200">

成功启动neo4j图数据库。

#### 新发现

上文提到neo4j3.5版本的兼容java版本为jdk1.8，我的电脑是jdk1.8与jdk21多版本共存的，但项目中同时使用到fuseki与neo4j，fuseki依赖jdk21，neo4j依赖jdk1.8，我感觉反复通过更改环境变量来改变当前使用的java版本实在是有点麻烦，索性下载了最新版的neo4j。但刚刚我发现一个不用修改环境变量即可单独使neo4j3.5版本运行时，依赖jdk1.8的环境。下面一起来看看吧~

##### 方法：

打开"D:\neo4j-community-3.5.35\bin\Neo4j-Management\Get-Java.ps1"文件，找到$javaPath = ' '，这行代码，在单引号部分粘贴上自己jdk1.8的路径即可。

<img alt="" height="830" src="https://img-blog.csdnimg.cn/direct/0c8bc643c05b44dbaf84e8ff618f845a.png" width="900">

之后正常启动neo4j3.5即可成功运行。
