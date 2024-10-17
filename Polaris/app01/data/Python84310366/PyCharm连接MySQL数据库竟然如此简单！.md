
--- 
title:  PyCharm连接MySQL数据库竟然如此简单！ 
tags: []
categories: [] 

---
在 PyCharm 中是可以通过内置的工具来连接、操作数据库的，并且对于市面上大多数主流数据库都是支持的。

本篇教程就教大家如何通过 Pycharm 内置的数据库工具连接 MySQL 数据库。

**连接 MySQL**

首先打开 PyCharm ，点击菜单栏的 View --&gt; Tool Windows --&gt; Database

<img src="https://img-blog.csdnimg.cn/img_convert/7d498e349a9348f3d0076449fc19ab7f.png" alt="">

或者直接点击 PyCharm 右侧的 Database

<img src="https://img-blog.csdnimg.cn/img_convert/10cebdfed6ee2f7316ddc90da79da3e5.png" alt="">

然后就会在 PyCharm 右侧就会弹出内置数据库工具的面板。

<img src="https://img-blog.csdnimg.cn/img_convert/6138cde70349b9f5abf551f159856681.png" alt="">

然后我们点击图示的 + 号 --&gt; Data Source --&gt; MySQL

<img src="https://img-blog.csdnimg.cn/img_convert/52c0778b53595b99e2a4df1f4f7b2368.png" alt="">

然后就会出现图示界面，需要我们输入对应的数据库信息，

Name：数据库的连接名称

Comment：数据库的描述简介

Host：数据库的ip地址

Port：数据库的端口号

User：数据库的用户名

Password：数据库的密码

Test Connection：测试按钮，点击这个按钮测试是否成功连接数据库

<img src="https://img-blog.csdnimg.cn/img_convert/71ec1750fc012ab1a72bcff43520def0.png" alt="">

信息填写完之后，别急着测试连接，如果和下图一样显示 Download missing driver files ，那么你就需要先点击 Download下载对应的驱动文件。

<img src="https://img-blog.csdnimg.cn/img_convert/41d825b7a5a7ecc8c77aae8931177ff8.png" alt="">

驱动文件搞定之后，点击 Test Connection 测试连接，出现图示的提示就代表数据库可以正常连接，点击右下角 OK 就行。

<img src="https://img-blog.csdnimg.cn/img_convert/426fab805dc091027e8f082ffab4ae3f.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/af531d2230b4ba83b02f7df73cc502a9.png" alt="">

**PyCharm 成功连接了 MySQL，但是没有显示所有的数据库**

很多读者第一次连接数据库都会遇到这个问题，教大家如何解决。

如图示，点击这个按钮

<img src="https://img-blog.csdnimg.cn/img_convert/f77421d77a8cc7c0591d65074af488e9.png" alt="">

再点击 Schemas，将 All Schemas 勾选上，然后点击右下角 OK 就行了！

<img src="https://img-blog.csdnimg.cn/img_convert/eb136272480cfaffa7944b63c90780da.png" alt="">

然后你就可以看到所有的数据库了。

**编写并且运行 SQL 语句**

点击如图所示的 logo，然后点击 console，然后编写 SQL 语句、点击运行就可以了。

<img src="https://img-blog.csdnimg.cn/img_convert/f3c09fbbea6aa211e53e7be7a89b6f5a.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/5f2a39f79b108cf16c98db401d92da1f.png" alt="">

**删除 MySQL 连接**

点击如图所示的按钮，

<img src="https://img-blog.csdnimg.cn/img_convert/3470b07c08d8ddef99c9178f36e58cd6.png" alt="">

在左侧选中你要删除连接的数据库，再点击上面的 — 按钮就可以了。

<img src="https://img-blog.csdnimg.cn/img_convert/d18776766721f95ed4180b7a8c911453.png" alt="">

## 关于Python学习指南

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后给大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、自动化办公等学习教程。带你从零基础系统性的学好Python！</mark>

#### 👉Python所有方向的学习路线👈

Python所有方向路线就是把Python常用的技术点做整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取）**</mark>

<img src="https://img-blog.csdnimg.cn/3c4ee87941694f3789398db3d52a2637.png#pic_center" alt="在这里插入图片描述">

#### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。

<img src="https://img-blog.csdnimg.cn/64c89bf6293d4699bf7ee8f34b9e69fd.png#pic_center" alt="在这里插入图片描述">

#### <mark>温馨提示：篇幅有限，已打包文件夹，获取方式在：文末</mark>

#### 👉Python70个实战练手案例&amp;源码👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/2017b67544f94e8898db755e2703224a.png#pic_center" alt="在这里插入图片描述">

#### 👉Python大厂面试资料👈

我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自**阿里、腾讯、字节等一线互联网大厂**最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面试资料相信大家都能找到满意的工作。

<img src="https://img-blog.csdnimg.cn/3055c54d3224495987c589f150324d73.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b0751719fe914aec8c8d09f62f772e44.png#pic_center" alt="在这里插入图片描述">

#### 👉Python副业兼职路线&amp;方法👈

学好 Python 不论是就业还是做副业赚钱都不错，但要学会兼职接单还是要有一个学习规划。

<img src="https://img-blog.csdnimg.cn/01bcd7cbfd6d43fb85ef410766735154.png#pic_center" alt="在这里插入图片描述">

**👉** **这份完整版的Python全套学习资料已经上传，朋友们如果需要可以扫描下方CSDN官方认证二维码或者点击链接免费领取**【**`保证100%免费`**】

<font color="red">**点击免费领取《CSDN大礼包》： 安全链接免费领取**</font>
