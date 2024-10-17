
--- 
title:  [ 应急响应基础篇 ] 使用 Autoruns 启动项分析工具分析启动项（附Autoruns安装教程） 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - - - - <ul><li>- 


## 一、背景介绍

>  
 当服务器被攻击后，基本都会留下后门，木马程序等，维护人员就需要找到他们并清除。 而对于木马后门，都需要有一个加载选项，例如直接以程序文件的形式运行，插入其他进程中运行，以服务的形式加载，以activex控件形式加载等。 


>  
 随后木马病毒肯定会访问网络，从我们检查角度一般需要对运行的进程、启动的加载项、端口连接等方面进行。 


>  
 Autoruns可以查看加载在启动、activex、explorer、logon、services等中的木马程序。 


## 二、Autoruns介绍

### 1、Autoruns简介

>  
 Windows官方提供的Autoruns工具，从字面来看很难理解其用途，因为直接翻译为“自动运行”，听上去好像是实现程序自动化运行的工具，但实际上，微软提供的这一款工具（Windows Sysinternals Autoruns For Windows）是用来查看、监视以及禁用自启动程序的最佳工具之一。 


### 2、Msconfig查看启动项的弊端

>  
 通常，通过任务管理器或者Msconfig命令可以看到windows操作系统下自动运行的程序，但msconfig只显示启动和服务，并不检查数字签名，因此恶意程序很容易绕过msconfig隐藏起来。 


### 3、查看那些启动项

>  
 Autoruns不仅仅显示在startup文件夹下的自动启动程序，也会显示通过Run/RunOnce或者其他注册表项实现自动启动的程序，也会详细显示文件管理器和IE扩展、工具栏、上下文菜单、驱动程序、服务、Winlogon项目乃至编解码器甚至Winsocks提供的程序等等，简言之，Autoruns几乎监控了windows系统下所有程序和启动项以供管理。 


## 三、Autoruns下载

>  
 使用Autoruns工具查看服务器所有的进程，其中背景颜色为粉红色的程序，经排查均不是恶意程序，服务器不存在恶意程序 


```
https://pan.baidu.com/s/1PmVo4nXbSyGaMmdJTZesSA?pwd=y0h8 

```

>  
 Autoruns汉化版下载链接： 


```
https://pan.baidu.com/s/1SUNy9ChbmcAcfojV_wik7w?pwd=b37t 

```

>  
 下载下来文件如下 


<img src="https://img-blog.csdnimg.cn/48be7b6549d0486c8879c0ad333802ee.png" alt="在这里插入图片描述">

## 四、Autoruns使用

### 1、使用介绍

>  
 打开autoruns后会看到everything栏，可罗列出使用该软件能查看的所有项。 


<img src="https://img-blog.csdnimg.cn/f7f5717b4b85482585efc0ee87655c55.png" alt="在这里插入图片描述">

>  
 点击计划任务，也可以查看所有的计划任务，如下图发现两个恶意计划任务。其他功能模块也可同理查看。 


<img src="https://img-blog.csdnimg.cn/fb6d3357b5b74564837b719b451b5aac.png" alt="在这里插入图片描述">

### 2、确认恶意程序

#### 1.检查手段

>  
 通过autoruns检查木马程序，主要通过如下信息来判断是否为木马程序： 


```
1.文件是否有数字签名
2.在公司和描述栏中是否有相应的内容
3.程序的物理路径

```

#### 2.操作方法

>  
 木马程序是没有数字签名的，我们可以多关注其描述(description)和出版商(publisher)栏，如果都为空，而又不确定是否为木马程序，则可以选中右键search online进行在线搜索，如果搜索没有相应的名称结果，则木马可能性比较大，木马取个名称是攻击者随意取的，搜出来的概率不大。 


<img src="https://img-blog.csdnimg.cn/7f181f540f314855b7c7fc7f80a8267d.png" alt="在这里插入图片描述">

>  
 其他选项也类似，autoruns对于木马常用的加载都有列出，everything启动加载，logon登录加载，explorer windows管理器加载，ie浏览器加载，scheduled tasks定时任务加载，services服务加载，drivers设备加载等。如果确认为恶意程序之后可右键选择删除。 


<img src="https://img-blog.csdnimg.cn/7e5f7eec3c1241fbaa2e09e8faa4ce15.png" alt="在这里插入图片描述">

### 3、验证代码签名

>  
 选择验证代码签名(Verify Code Signatures)，选下图勾选并点击重新扫描(Rescan) 按钮 


<img src="https://img-blog.csdnimg.cn/2cb6f84281fe434fad769ac52cf22f5b.png" alt="在这里插入图片描述">

>  
 如果不想在下次启动或登录时激活某个条目，可以禁用或删除。要禁用条目，把前面小框框的勾去掉就行。要删除它，请右键单击该条目并选择Delete。 


<img src="https://img-blog.csdnimg.cn/6c995927a42a4e7f972f5914e33f2050.png" alt="在这里插入图片描述">

### 4、Autoruns具体功能模块介绍

```
1、登录（Logon）：
此条目会扫描标准自动启动位置，例如当前用户和所有用户的启动文件夹、(Startup)运行注册表(Run Registry)项和标准应用程序启动位置。
2、资源管理器（Explorer）：
此条目显示Explorer shell 扩展、浏览器帮助对象、资源管理器工具栏、活动设置执行和 shell 执行挂钩。
3、IE浏览器（Internet Explorer）：
此条目显示浏览器帮助程序对象(Browser Helper Objects)(BHO)、Internet Explorer工具栏和扩展。
4、计划任务（Scheduled Tasks）：
任务(Task)计划程序任务配置为在引导或登录时启动。
5、服务（Services）：
它显示所有配置为在系统启动时自动启动的Windows服务。
6、驱动（Drivers）：
这将显示系统上注册的所有内核模式驱动程序，但禁用的驱动程序除外。
7、已知DLL（AppInit DLL）：
这有 Autoruns 显示注册为应用程序初始化DLL。
8、引导执行（Boot Execute）：
在启动过程早期运行的本机映像（与Windows映像相反）。
9、镜像劫持（Image Hijacks）：
图像文件执行选项和命令提示符自动启动。
10、应用初始化（AppInit）：
显示注册为应用程序初始化DLL的DLL。

11、已知的 DLL（Known DLLs）：
这会报告 Windows 加载到引用它们的应用程序中的DLL的位置。(DLLs)
12、Winlogon （win登录通知）：
显示注册登录事件的Winlogon通知的DLL 。(Shows DLLs)
13、Winsock 提供商（Winsock Providers）： 
显示已注册的Winsock 协议，包括Winsock 服务提供程序。恶意软件(Malware)通常将自身安装为Winsock 服务提供商，因为很少有工具可以删除它们。自动运行可以禁用它们，但不能删除它们。
14、LSA 提供者（LSA Providers）：
显示(Shows)注册本地安全机构(Local Security Authority)( LSA ) 身份验证、通知和安全包。
打印机监视器驱动程序（Printer Monitor Drivers）：
显示加载到后台打印服务中的DLL 。(DLLs)恶意软件(Malware)已使用此支持自动启动自身。
15、侧边栏（Sidebar Gadgets）：
显示 Windows 边栏小工具。

```

## 五、相关资源

 
