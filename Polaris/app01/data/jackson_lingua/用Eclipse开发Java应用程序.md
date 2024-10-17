
--- 
title:  用Eclipse开发Java应用程序 
tags: []
categories: [] 

---
## 用Eclipse开发Java应用程序

### Develop Java Program with Eclipse

>  
 Eclipse是一个开源的、跨平台的集成开发环境（IDE），用于开发Java、C++、PHP、Python等语言的应用程序。它提供了一整套插件和工具，可以帮助开发者在开发和测试过程中提高效率和准确性。 


本文简要介绍如何获取和安装配置Eclipse IDE集成开发环境，从而用来开发Java应用程序。供广大程序员、开发者参考。

#### 1. 获取Eclipse

访问Eclipse官网，https://www.eclipse.org/ ，点击Download进入下载页面。

<img src="https://img-blog.csdnimg.cn/f3930e22bd5545fdae7b1209c5a7104b.png" alt="在这里插入图片描述"> 点击页面右上角**Download**按钮，进入下载选择页面。

<img src="https://img-blog.csdnimg.cn/dc65ce03b2be4a9c9ee00ecda737e809.png" alt="在这里插入图片描述"> 根据当前使用的操作系统Windows 10/11, 须考虑安装最新的64位版本，选择左侧的Eclipse desktop IDE，点击**Download x86_64**按钮进入下载页面。

<img src="https://img-blog.csdnimg.cn/e3d78837f2f44aacbdc763e863d55917.png" alt="在这里插入图片描述">

于是，Chrome浏览器开始下载安装文件，该文件名为：**eclipse-inst-jre-win64.exe**, 是个可执行文件。

下载完毕后，在Windows的下载文件夹找到这个安装文件，双击该文件进行安装。
1. 安装Eclipse
<img src="https://img-blog.csdnimg.cn/d4aa63ca82ad4afca1e4ee5967a6c294.png" alt="在这里插入图片描述">

上图为安装向导欢迎画面，由于要进行Java开发，故选择最上方**Eclipse IDE for Java Developers**选项。 <img src="https://img-blog.csdnimg.cn/eb2263ae2a164c1fb71035d38f33a41c.png" alt="在这里插入图片描述"> 出现安装路径时，选择默认**Installation Folder**路径，但是对应JDK安装文件夹改为D:\JDK20 （如果之前安装JDK 20在此路径）, 点击**INSTALL**进行安装。

<img src="https://img-blog.csdnimg.cn/4a283688f14d4591882e6e304d93cf45.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9bbf9bf2cbf44fa381edc5c24bbbb939.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/3ac38f123cb84822b30e91388781331d.png" alt="在这里插入图片描述"> 出现eclipse 2023-03的炫彩欢迎画面。

<img src="https://img-blog.csdnimg.cn/f50b8b9ec5884d768eceeeff7655ba15.png" alt="在这里插入图片描述"> 选择Workspace,按照图示默认路径，点击**Launch**启动 Eclipse IDE欢迎对话框， 如下图：<img src="https://img-blog.csdnimg.cn/eb7ba020809443a2b6a9be7cc8ed3312.png" alt="在这里插入图片描述"> 点击**Create a new Java project**, 创建一个新的Java项目。

可以看到，随后启动Eclipe IDE开发环境，如下图。

<img src="https://img-blog.csdnimg.cn/886cea944a5646249e9bf7f762bc787e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/3ee95027235e4aedb6f415540f95a24d.png" alt="在这里插入图片描述"> 此时，输入新的Java项目名称为HelloJava, 而JRE选择变为特定的版本JDK20, 和安装在D:\JDK20文件夹的版本对应一致。

点击**Finish**完成初始配置。

在Hello Java项目处，新增类文件（即Class文件），名为HelloJava, 然后复选创建”public static void main（String[] args）,点击Finish完成。

<img src="https://img-blog.csdnimg.cn/71ebfa1867ee45a6ade55cceeed76dce.png" alt="在这里插入图片描述"> **注意：** 如果需要作为运行的类，则须选中上图中public static void main(String[] args) 复选项；否则，在新的类中要手动添加这个静态main函数。

编写第一个Java应用程序HelloJava，代码如下图： <img src="https://img-blog.csdnimg.cn/81dd15edee2142b5bec7191418947543.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/c7f2b6cf80e04d5fa5c71285a30a85fa.png" alt="在这里插入图片描述"> 弹出对话框，已默认复选/HelloJava/src/HelloJava.java作为要保存的资源文件，点击OK完成运行。

<img src="https://img-blog.csdnimg.cn/92ca4efd882147ee862016148c13c1c2.png" alt="在这里插入图片描述">

在下方Console（控制台）区域，运行结果为**Hello, Java!**。

至此，第一个Java程序编写和运行成功！让我们继续遨游在Java有趣的海洋吧。

#### #替换eclipse主题为夜间背景

有时候，程序员可能需要变换不同的主题，来丰富开发环境的场景，例如由白天背景，更换为夜间背景主题。

点击eclipse程序的Window菜单，选择点击Preferences, 进入外观配置对话框。

<img src="https://img-blog.csdnimg.cn/29a8c1e6fa54420fb31464a93eb18a71.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a7fc981c2faa463e905a88c8da5516b8.png" alt="在这里插入图片描述"> 在General &gt; Appearance 中，在Theme下拉菜单里，点选**Dark**, 点击该对话框右下角Apply按钮，应用该主题，随即进入黑色主题。

<img src="https://img-blog.csdnimg.cn/c89ad4627a1344b9ad4933c40fa99123.png" alt="在这里插入图片描述"> 若要安装新的eclipse主题，则选择Help菜单，点击Eclipse MarketPlace, 进入MarketPlace网页。 这里有各种待安装theme, 选择第一个eclipse theme, 然后用鼠标拖放到eclipse程序MarketPlace对话框区域，即自动开始安装主题。

安装完毕后，再次打开eclipse，就是下图这样端庄的夜景主题样式。

<img src="https://img-blog.csdnimg.cn/890bd14f7d3c41fd8243ce1f189d2939.png" alt="在这里插入图片描述"> 喜欢就点赞哈。😃

技术好文持续推出，欢迎关注。

**All rights reserved. @ 2023, 版权所有，侵权必究。**
