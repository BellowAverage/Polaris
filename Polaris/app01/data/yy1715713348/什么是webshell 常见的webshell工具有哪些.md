
--- 
title:  什么是webshell 常见的webshell工具有哪些 
tags: []
categories: [] 

---
Webshell是黑客经常使用的一种恶意脚本，其目的是获得服务器的执行操作权限，比如执行系统命令、窃取用户数据、删除web页面、修改主页等，其危害不言而喻。黑客通常利用常见的漏洞，如SQL注入、远程文件包含(RFI)、FTP，甚至使用跨站点脚本攻击(XSS)等方式作为社会工程攻击的一部分，最终达到控制网站服务器的目的。

常见的webshell编写语言为asp、jsp和php。本文将以php Webshell为示例，详细解释Webshell的常用函数、工作方式以及常用隐藏技术。

攻击者在入侵网站时，通常要通过各种方式写入Webshell，从而获得服务器的控制权限，比如执行系统命令、读取配置文件、窃取用户数据，篡改网站页面等操作。 本文介绍十款常用的Webshell管理工具，以供你选择，你会选择哪一个？

1、中国菜刀(Chopper)

中国菜刀是一款专业的网站管理软件，用途广泛，使用方便，小巧实用。只要支持动态脚本的网站，都可以用中国菜刀来进行管理！在非简体中文环境下使用，自动切换到英文界面。UNICODE方式编译，支持多国语言输入显示。

<img src="https://img-blog.csdnimg.cn/e4ea6f406ffc4b0db08eefac4489cf38.jpeg" alt="">

2、蚁剑(AntSword)

AntSword是一个开放源代码，跨平台的网站管理工具，旨在满足渗透测试人员以及具有权限和/或授权的安全研究人员以及网站管理员的需求。 github项目地址：https://github.com/AntSwordProject/antSword

<img src="https://img-blog.csdnimg.cn/ff0544967e124bfaae341bbfcad6cf56.jpeg" alt="">

3、C刀(Cknife)

这是一款跨平台的基于配置文件的中国菜刀，把所有操作给予用户来定义。 github项目地址：https://github.com/Chora10/Cknife

<img src="https://img-blog.csdnimg.cn/9db6686345d94ee49a7868baff3954ab.jpeg" alt="">

4、冰蝎(Behinder)

冰蝎”是一款动态二进制加密网站管理客户端。 github地址：https://github.com/rebeyond/Behinder

<img src="https://img-blog.csdnimg.cn/05a9b93439684560a9ebf56fdf1844ec.jpeg" alt="">

5、Xise XISE WebShell管理工具。

<img src="https://img-blog.csdnimg.cn/1f0fcc964c494a9ab75598efd18e9dcc.jpeg" alt="">

6、Altman

Altman3是一款渗透测试软件，基于.Net4.0开发，依托Eto.Form可以完美运行在Windows、Linux、Mac等多个平台。 github项目地址：https://github.com/keepwn/Altman <img src="https://img-blog.csdnimg.cn/702e790212ba4c8592e25469fadd967f.jpeg" alt="">

7、Weevely

Weevely是一种Python编写的webshell管理工具，跨平台，只支持PHP。 github项目地址：https://github.com/epinna/weevely3 用法示例：

weevely generate 
 <path>
   weevely [cmd] 
  <img src="https://img-blog.csdnimg.cn/34e7ffcb96b74cdfbe200fbe875f4a7b.jpeg" alt=""> 
 </path>

同时，在Kali 2.0 版本下，集成了三款Web后门工具：WebaCoo、weevely、PHP Meterpreter。

8、QuasiBot

QuasiBot是一款php编写的webshell管理工具，可以对webshell进行远程批量管理。 github项目地址：https://github.com/Smaash/quasibot <img src="https://img-blog.csdnimg.cn/476004a4fdb6482992e14392a7539e08.jpeg" alt="">

9、Webshell-Sniper 这是一款基于终端的webshell管理工具，仅支持在类Unix系统上运行。 github项目地址：https://github.com/WangYihang/Webshell-Sniper 用法示例：

Usage : python webshell-sniper.py [URL] [METHOD] [AUTH] Example : python webshell-sniper.py http://127.0.0.1/c.php POST c <img src="https://img-blog.csdnimg.cn/0e9bb3fa092e40088090b3c16a3ef1c0.jpeg" alt="">

10、WebshellManager

一款用PHP+Mysql写的一句话WEB端管理工具，目前仅支持对PHP的一句话进行操作。 github项目地址：https://github.com/boy-hack/WebshellManager

<img src="https://img-blog.csdnimg.cn/894639f2c92c4800a3cfeeb649ffa4a9.jpeg" alt="">

### 网络安全工程师(白帽子)企业级学习路线

#### 第一阶段：安全基础（入门）

<img src="https://img-blog.csdnimg.cn/img_convert/c1e5320ff55483f152585656dfd55aeb.png" alt="img">

#### 第二阶段：Web渗透（初级网安工程师）

<img src="https://img-blog.csdnimg.cn/img_convert/e405401641899e43efeccc3c599f1e89.png" alt="img">

#### 第三阶段：进阶部分（中级网络安全工程师）

<img src="https://img-blog.csdnimg.cn/img_convert/932e81f180ce1d110f4fc5cd828eed51.png" alt="img">

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**
