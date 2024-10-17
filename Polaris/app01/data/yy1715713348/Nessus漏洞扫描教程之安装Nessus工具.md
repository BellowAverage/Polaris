
--- 
title:  Nessus漏洞扫描教程之安装Nessus工具 
tags: []
categories: [] 

---
### Nessus基础知识

Nessus号称是世界上最流行的漏洞扫描程序，全世界有超过75000个组织在使用它。该工具提供完整的电脑漏洞扫描服务，并随时更新其漏洞数据库。Nessus不同于传统的漏洞扫描软件，Nessus可同时在本机或远端上遥控，进行系统的漏洞分析扫描。对应渗透测试人员来说，Nessus是必不可少的工具之一。

### Nessus概述

Nessus通常包括成千上万的最新的漏洞，各种各样的扫描选项，及易于使用的图形界面和有效的报告。Nessus之所以被人们喜爱，是因为该工具具有几个特点。如下所示：
- 提供完整的电脑漏洞扫描服务，并随时更新其漏洞数据库。- 不同于传统的漏洞扫描软件。Nessus可同时在本机或远程控制，进行系统的漏洞分析扫描。- 其运作效能随着系统的资源而自行调整。如果将主机配置更多的资源（如加快CPU速度或增加内存大小），其效率表现可因为丰富资源而提高。- 可自行定义插件。- NASL（Nessus Attack Scripting Language）是由Tenable所发出的语言，用来写入Nessus的安全测试选项。- 完全支持SSL（Secure Socket Layer）。
### 获取Nessus软件包

在安装Nessus工具之前，首先要获取该工具的安装包。而且，Nessus工具安装后，必须要激活才可使用。所以，下面将分别介绍获取Nessus安装包和激活码的方法。

1.获取Nessus安装包

Nessus的官方下载地址是：

http://www.tenable.com/products/nessus/select-your-operating-system 2.下载Nessus软件包

从该界面可以看到Nessus有两个版本，分别是Home（家庭版）和Professional（专业版）。这两个版本的区别如下所示：
- 家庭版：家庭版是免费的，主要是供非商业性或个人使用。该版比较适合个人使用，并且可以用于非专业的环境。- 专业版：专业版是需要付费的。但是，可以免费使用七天。该版主要是供商业人士使用。它包括技术支持或附加功能，如无线并发连接等。
.获取激活码

在使用Nessus之前，必须先激活该服务才可使用。如果要激活Nessus服务，则需要到官网获取一个激活码。下面将介绍获取激活码的方法。具体操作步骤如下所示：

（1）在浏览器中输入以下地址：

http://www.nessus.org/products/nessus/nessus-plugins/obtain-an-activation-code

成功访问以上链接后，将打开如图所示的界面。 <img src="https://img-blog.csdnimg.cn/img_convert/3354e5f864818c0789ac1c231e999e8d.png" alt="">

（2）在该界面单击Nessus Home Free下面的Register Now按钮，将显示如图所示的界面。 <img src="https://img-blog.csdnimg.cn/img_convert/a77a0ff113b88f6090a95d30a24f5e95.png" alt="">

（3）在该界面填写一些信息，为了获取激活码。在该界面First Name和Last Name文本框中，用户可以任意填写。但是，Email下的文本框必须填写一个合法的邮件地址，用来获取邮件。当以上信息设置完成后，单击Register按钮。接下来，将会在注册的邮箱中收到一份关于Nessus的邮件。进入邮箱打开收到的邮件，将会看到一串数字，类似XXXX-XXXX-XXXX-XXXX，即激活码。

（4）当成功安装Nessus工具后，就可以使用以上获取到的激活码来激活该服务了。

## 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**
