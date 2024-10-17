
--- 
title:  用XAMPP在Windows系统构建一个本地Web服务器 
tags: []
categories: [] 

---
## 用XAMPP在Windows系统构建一个本地Web服务器

### Build a Local Web Server for Windows with XAMPP

By Jackson@ML

本文简要介绍如何获取和安装XAMPP以实现Windows环境下本地Web服务器的过程，希望对广大网友和学生有所帮助。

>  
 所谓本地Web服务器，即使用本地主机名即可访问的Web站点，例如：在浏览器中打开https://127.0.0.1，或者https://localhost可打开的非空页面，就说明存在本地主机，并配置了Web Server服务，可访问该站点的主页。 


我们尝试一下当前计算机的浏览器，如下图： <img src="https://img-blog.csdnimg.cn/direct/6b5e16b19da24d27a17ee2bd1cf15bed.png" alt="在这里插入图片描述"> 可以看到，由于没有创建Web Server，导致提示“无法访问此网站”。 接下来，根据以往的经验，让我们一起来逐步搭建一个Web Server.

#### 1. 获取XAMPP

XAMPP通常在Linux和macOS系统可用，但Windows也不例外，有一个专门在Windows可用的版本。 在Chrome浏览器中，打开其官网链接：

<img src="https://img-blog.csdnimg.cn/direct/6ae73e1c959d477e9a5a7d3cbd0d58bc.png" alt="在这里插入图片描述"> 点击XAMPP for Windows进入下载页面，如下图：

<img src="https://img-blog.csdnimg.cn/direct/5ed93bf4df8d40f387fba946923badc2.png" alt="在这里插入图片描述"> Chrome浏览器开始下载。（如果因浏览器问题没有下载，直接点击页面上方If it doesn’t, click here. 即可马上下载。

#### 2. 安装XAMPP

当下载完毕，双击该安装包，即可执行文件 **xampp-windows-x64-8.2.12-0-VS16-installer.exe**，即可启动安装向导。

点击确定继续，出现如下对话框。

<img src="https://img-blog.csdnimg.cn/direct/fe54e46c81924250a1c06be281f5526d.png" alt="在这里插入图片描述">

在Select Components(选择组件)对话框，仅仅选择Apache（Web Server）功能，继续完成安装；如果计划使用MySQL数据库，则可以复选MySQL.

<img src="https://img-blog.csdnimg.cn/direct/a70858905bf84890a5115551f51508ef.png" alt="在这里插入图片描述"> 仅复选了MySQL，以备数据库管理之用。

<img src="https://img-blog.csdnimg.cn/direct/980d574228344ac99f05824d9467141a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/baa35bc50a12469291aa8ca340688a8e.png" alt="在这里插入图片描述"> 提示C:\xampp文件夹不是空的，因此必须修改路径为D:\xampp, 点击Next进行下一步。

<img src="https://img-blog.csdnimg.cn/direct/4dbd83add8e64ebe88a2bc43bea77402.png" alt="在这里插入图片描述"> 随即开始安装直到安装结束。

<img src="https://img-blog.csdnimg.cn/direct/f3e2a2332e1741ab9bf1c302177fb79e.png" alt="在这里插入图片描述"> 安装完毕后，启动该程序Apache HTTP Server，需选择专用网络（而不是按照默认选项公用网络），点击允许访问。

<img src="https://img-blog.csdnimg.cn/direct/d96374e696d34999852c3e085a492683.png" alt="在这里插入图片描述"> 安装向导安装完毕，点击Finish结束安装。此时，自动启动XAMPP Control Panel v3.2.4,如下图：

<img src="https://img-blog.csdnimg.cn/direct/11d8867ecc1d4ccd989edbe15039ce04.png" alt="在这里插入图片描述"> 在Apache右侧选取点击按钮Start，即启动Apache HTTP Server。弹出对话框为XAMAPP Control Panel设置改变，如下图：

<img src="https://img-blog.csdnimg.cn/direct/631e82d3fbb24a1ab50cd23552b2cc67.png" alt="在这里插入图片描述"> 启动Web服务后，在Chrome浏览器的地址栏中，输入**http://localhost** 访问主机，即打开XAMPP默认页面，如下图：

<img src="https://img-blog.csdnimg.cn/direct/92f4ad92946648e29aa9ca9385caa48b.png" alt="在这里插入图片描述"> 这说明本地Web服务器搭建完成。

接下来，如果需要完成Apaceh+MariaDB+PHP+Perl编程，开发新的站点，那么就勇敢的向前迈进吧！

技术好文陆续推出，敬请关注。

喜欢就点赞哈！您的认可，我的动力。😃
