
--- 
title:  Nessus简介（转载） 
tags: []
categories: [] 

---
一、Nessus简介 Nessus是一个功能强大而又易于使用的远程扫描器，它不仅而 且更新极快。安全扫描器的功能是对指定网络进行安全检查，找出该网络是否存在有导致对手攻击的安全漏洞。该系统被设计为client/sever模式，服 务器端负责进行安全检查，客户端用来配置管理服务器端。在服务端还采用了plug-in的体系，允许用户加入执行特定功能的插件，这插件可以进行更快速和 更复杂的安全检查。在Nessus中还采用了一个共享的信息接口，称之知识库，其中保存了前面进行检查的结果。检查的结果可以HTML、纯文本、 LaTeX（一种文本文件格式）等几种格式保存。 在未来的新版本中，Nessus将会支持快速更快的安全检查，而且这种检查将会占用更少的带宽，其中可能会用到集群的技术以提高系统的运行效率。 Nessus的优点在于： 1、 其采用了基于多种安全漏洞的扫描，避免了扫描不完整的情况。 2、 它是免费的，比起商业的安全扫描工具如ISS具有价格优势。 3、 在Nmap用户参与的一次关于最喜欢的安全工具问卷调查中（评选结果附后），在与众多商用系统及开放源代码的系统竞争中，Nessus名列榜首。群众的眼睛是雪亮的：）。 4、 Nessus扩展性强、容易使用、功能强大，可以扫描出多种安全漏洞。

Nessus的安全检查完全是由plug-ins的插件完成的。到本文完成时为止，Nessus提供的安全检查插件已达18类705个，而且这个数量以后 还会增加。比如：在“useless services”类中，“Echo port open”和”Chargen”插件用来测试主机是否易受到已知的echo-chargen攻击。在“backdoors”类中，”pc anywhere”插件用来检查主机是否运行了BO、PcAnywhere等后台程序，可喜的是其中包括了最近肆虐一时的CodeRed及其变种的检测。 在Nessus主页中不但详细介绍了各种插件的功能，还提供了解决问题的相关方案。有关plug-in的详细说明，请看[url]http://cgi.nessus.org/plugins/dump.php3?viewby=family[/url]

除了这些插件外，Nessus还为用户提供了描述攻击类型的脚本语言，来进行附加的安全测试，这种语言称为Nessus攻击脚本语言（NSSL），用它来完成插件的编写。 在 客户端，用户可以指定运行Nessus服务的机器、使用的端口扫描器及测试的内容及测试的IP地址范围。Nessus本身是工作在多线程基础上的，所以用 户还可以设置系统同时工作的线程数。这样用户在远端就可以设置Nessus的工作配置了。安全检测完成后，服务端将检测结果返回到客户端，客户端生成直观 的报告。在这个过程当中，由于服务器向客户端传送的内容是系统的安全弱点，为了防止通信内容受到监听，其传输过程还可以选择加密。

二、安装Nessus 前面讲到，Nessus由客户端和服务器端两部分组成。我们先来看服务器端的安装。

1、 与安装 你可以到[url]http://www.nessus.org/download.html[/url]去下载nessus的最新版本。Nessus分为服务器端和客户端两部分，而服务器端又分为稳定版和实验版两种版本，建议你下载稳定的版本，如果你不是太急于看到实验版本中的新功能的话。 同样，nessus的客户端有两个版本，JAVA版本及C版本，JAVA版本的可以在多个平台中运行，C版本的支持Windows，有了这两个客户端的版本你就可以在的任何的一台机器上进行安全检查了。 下面我们来看看服务器端的安装。服务器端共有四个安装包组成： · nessus-libraries-x.x.tar.gz · libnasl-x.x.tar.gz · nessus-core.x.x.tar.gz · nessus-plugins.x.x.tar.gz 一定要按照以上的顺序安装各个包。首先用tar –xzvf nessus-* 将这四个软件包解开。第一个先安装nessus的lib库： cd nessus-libaries ./configure make 以root身份执行make install。 然后以同样的方法按照上面的顺序安装其它三个软件包。 在安装完毕后，确认在/etc/ld.so.conf文件加入安装已安装库文件的路径：/usr/local/lib。如果没有，你只需在该文件中加入这个路径，然后执行ldconfig，这样nessus运行的时候就可以找着运行库了。

2、 创建一个用户 Nessus服务端有自己的用户资料库，其中对每个用户都做了约束。用户可以在整个网络范围内通过nessusd服务端进行安全扫描。 创建用户的方法如下： $ nessus-adduser

Addition of a new nessusd user ------------------------------

Login : admin //输入用户名 Pass : secret //用户口令 Authentification type (cipher or plaintext) [cipher] : cipher //选择过程是否加密， Now enter the rules for this user, and hit ctrl-D once you are done : (the user can have an empty rule set) ^D

Login : admin Pssword : secret Authentification : cipher Rules :

Is that ok (y/n) ? [y] y

user added.

Nessus-adduser是Nessusd的附带工具，安装完毕后，在安装目录下会产生这个程序。

3、 配置Nessus服务端程序Nessusd 它的配置文件为nessusd.conf，位于/usr/local/etc/nessus/目录下。一般情况下，不建议你改动其中的内容，除非你确实有需要。 4、 启动nessusd 在上面的准备工作完成后，以root用户的身份用下面的命令启动服务端：nessusd –D

三、进行安全扫描 按照上面的方法启动Nessus的服务进程后，就可以执行客户端程序进行安全扫描了。

上面就是启动界面了。首先提示你登录到nessus服务器，在Nessus Host后面输入Nessus服务器所在的机器IP地址，端口号及加密方式不需要做改动。下面输入用户名，点击Log in登录。一旦登录，Log in的按钮会变为Log out，对话框的旁边还会有connected的提示。 好了，下面我们通过选择Plug-in插件来进行相应的安全扫描：

如上图所示，在上半部分的是插件选择，下面是插件所能检查的攻击方法，点击每个攻击方法会弹出一个对话框介绍它的危害性及解决方法，如下图所示：

建议选择全部的插件以增加安全扫描的完整性。 下面选择扫描的目标主机，点击“target selection”

在窗口中输入目标地址，如上面所输入的：192.168.6.26，这里作者用的是一个内部地址，你还可以用192.168.6.26/24的方式指定扫 描192.168.6.1-192.168.6.255整个网段，抑或用x.y.z及选中下面的Perform a DNS zone transfer选项一起通过系统查找目标的IP，

最后还有一个可选项是用户规则，规则是用来对用户所做的扫描操作进行约束，比如我想对除了192.168.6.4这个地址以外的所有192.168.6网段主机进行扫描，那就可以在规则设置中输入： reject 192.168.6.4 default accept 这一切都OK后，点击start 开始进行扫描。

四、扫描结果

当扫描结束后，会生成如下形式的报表：

在窗口的左边列出了所有被扫描的主机，只要用鼠标点击主机名称，在窗口右边就列出了经扫描发现的该主机的安全漏洞。再点击安全漏洞的小图标会列出该问题的严重等级及问题的产生原因及解决方法。 最后，你还可以将扫描结果以多种格式存盘，做为参考资料供以后使用
- **[](javascript:;)赞**- **[](javascript:;)收藏**- **[](javascript:;)评论**- **[](javascript:;)分享**- **[](javascript:;)举报**
上一篇：

下一篇：



提问和评论都可以，用心的回复会被更多人看到 **评论**

**发布评论**

**全部评论** () 最热 最新

**相关文章**
-  [ 对比学习简介 1. 引言在本教程中，我们将介绍对比学习领域中的相关概念。首先，我们将讨论这种技术背后相关的理论知识；接着，我们将介绍最常见的对比学习的损失函数和常见的训练策略。闲话少说，我们直接开始吧！2. 举个栗子首先，让我们通过简单的例子来增加对对比学习概念的理解 。我们不妨来玩一个许多孩子经常玩的游戏：这个游戏的目标是从右侧的候选图片中，寻找看起来最像左侧动物的图像。在我们的例子中，孩子必须在右边的四张图 ](https://blog.51cto.com/u_15506603/9050254) 损失函数 特征空间 对比学习 -  [ 无涯教程-PDFBox - 简介 Portable Document Format(PDF)是一种文件格式，可帮助以独立于应用程序软件，硬件和操作系统的方式显示… ](https://blog.51cto.com/u_14033984/9324220) pdfbox -  [ ​Azure Update Manager简介 Azure 更新管理器不仅仅是一个管理更新的工具；它是一个全面的解决方案，旨在帮助组织维护其系统的完整性、安全性和性能。对于致力于在不断发展的数字世界中实现卓越运营和合规性的企业来说，这是一项必不可少的服务 ](https://blog.51cto.com/wuyvzhang/9793269) Azure Windows 补丁更新 安全 -  [ Nessus简介 全力以赴，利用Nessus完成好这个项目 ](https://blog.51cto.com/billowg/64447) 职场 网络安全 休闲 Nessus -  [ [转载]WAP简介 WAP（wireless application protoc ](https://blog.51cto.com/u_15082498/5531194) 服务器 web服务器 数据 -  [ 转载：VSS简介 vss VSS 的全称为 Visual Source Safe 。作为 Microsoft Visual Studio 的一名成员，它主要任务就是负责项目文件的管理，几乎可以适用任何软件项目。 源代码版本控制机制是现代软件开发中必不可少的管理机制之一，通常借助版本控制软件即Source Code Management(SCM) systems或者Version Control syste ](https://blog.51cto.com/u_15082498/5854488) 服务器 数据库 microsoft -  [ TensorRT简介-转载 前言 NVIDIA TensorRT是一种高性能神经网络推理(Inference)引擎，用于在生产环境中部署深度学习应用程序，应用有图像分类、分割和目标检测等，可提供最大的推理吞吐量和效率。TensorRT是第一款可编程推理加速器，能加速现有和未来的网络架构。TensorRT需要CUDA的支持。TensorRT包含一个为优化生产环境中部署的深度学习模型而创建的库，可获取经过训练的神经网络(通常使用 ](https://blog.51cto.com/u_15711436/5462678) 神经网络 数据 深度学习 -  [ GeeXBox简介-01 转载 GeeXboX 是一个集成了mplayer播放器的迷你Linux系统，基本上可以播放所有常见的媒体文件，支持中文字幕，你甚至还可以用来看网络电视（鸟语的——！）。它的体积仅有40多M而且完全免费！你除了可以安装在电脑的硬盘上，也可以刻录成光盘，甚至还可以安装在U盘上，通过光盘/U盘启动来看电影。下面我们主要教大家制作一个U盘影音系统……GeeXBox播放视频的配置要求相当低，超级适合旧电脑使用将 ](https://blog.51cto.com/u_15082498/5527252) u盘 ios 启动顺序 -  [ netfilter/iptables 简介（转载） -  [ 【转载】TMS协议简介 tms协议TMS简介TMS是tile map service的简写。是一种瓦片服务。Tile Map Service或TMS是由开放源码地理空间基金会开发的平铺web地图规范。这个定义通常… ](https://blog.51cto.com/xosg/4637572) java linux python http mysql -  [ 【转载】RFID技术简介 众所周知，奥运会是目前世界上规模最宏大的综合性体育赛事，集体育比赛、休闲、交流、游玩、购物及其它商业活动于一体，因此承载这个赛事的奥运场馆必将接纳庞大的观众、运动员、管理人员、服务人员等，且人群身份极其复杂并处于不停的移动之中。 如何验证人员所持的票卡和证件是否有效？如何及时跟踪和查询人员是否进入到指定区域？当人员误入或非法闯入禁入区域时又如何警示和引导其迅速离开？如何实时查询某区域人员拥挤程 ](https://blog.51cto.com/ssdguy/336434) 职场 技术 简介 休闲 RFID -  [ [转载]MongoDB入门简介 原文地址：MongoDB入门简介作者：Harry 有关于MongoDB的资料现在较少，且大多为英文网站，以上内容大多由笔者翻译自官网，请翻译或理解错误之处请指证。之后笔者会继续关注MongoDB，并翻译“Developer Zone”和“Admin Zone”的相关内容，敬请期待下期内容。 MongoDB是一个基于分布式文件存储的数据库开源项目。由C++语言编写。旨在为WEB应用提供可护展的高性 ](https://blog.51cto.com/openpy/1572394) 入门 简介 mongodb -  [ (转载)Instrumentation 框架简介 原文地址：http://www.cnblogs.com/xirihanlin/archive/2010/06/15/1758677.html Android提供了一系列强大的测试工具，它针对Android的环境，扩展了业内标准的JUnit测试框架。尽管你可以使用JUnit测试Android工程，但Android工具允许你为应用程序的各个方面进行更为复杂的测试，包括单元层面及框架层面。 An ](https://blog.51cto.com/techgogogo/1608458) framework 自动化测试 android instrumentation -  [ Nessus之——Nessus的整理 5.1 使用NessusNessus号称是世界上最流行的漏洞扫描程序，全世界有超过75000个组织在使用它。该工具提供完整的电脑漏洞扫描服务，并随时更新其漏洞数据库。Nessus不同于传统的漏洞扫描软 ](https://blog.51cto.com/binghe001/3247124) Kali linux系统 unix -  [ Event Logging 技术简介（转载） EventLog简单介绍（转载） ](https://blog.51cto.com/13713878410/1538624) Windows EventLog -  [ 【转载】 Sun RPC 编程简介 原文地址： http://blog.chinaunix.net/uid-1724205-id-2813082.html 一、 概述 在传统的编程概念中，过程是由程序员在本地编译完成，并只能局限在本地运行 ](https://blog.51cto.com/u_15642578/5316852) 文件系统（磁盘文件系统） 分布式系统 Linux 客户端 句柄 -  [ 转载 ~shell简介 Shell本身是一个用C语言编写的程序，它是用户使用Unix/Linux的桥梁，用户的大部分工作都是通过Shell完成的。Shell既是一种命令语言，又是一种程序设计语言。作为命令语言，它交互式地解释和执行用户输入的命令；作为程序设计语言，它定义了各种变量和参数，并提供了许多在高级语言中才具有的控制 ](https://blog.51cto.com/u_15069489/4055742) unix linux bash shell脚本 商业 -  [ Mock简介、场景（转载） 一、关于Mock测试 1、什么是Mock测试？ Mock 测试就是在测试过程中，对于某些不容易构造（如 HttpServletRequest 必须在Servlet 容器中才能构造出来）或者不容易获取的比较复杂的对象（如 JDBC 中的ResultSet 对象），用一个虚拟的对象（Mock 对象）来创 … ](https://blog.51cto.com/u_15127673/4352619) json 数据 配置文件 单元测试 post请求 -  [ nessus密码 nessus使用教程 1、 打开浏览器输入IP加端口8834登录Nessus 2、 输入账号密码，均为admin 3、 登录成功后，进入到首页4、 点击侧边栏policies，显示策略界面 5、 点击new policy，显示策略模板 6、 选择advanced scan，填写策略名称 7、 点击permission，选择can use，设置所有人可用 8、 单击Plugins标签，该界面显示了所有插件程序，默认全部是 ](https://blog.51cto.com/u_16099219/9670751) nessus密码 IP 自定义 界面显示 -  [ Nessus NessusNessus 是目前全世界最多人使用的系统漏洞扫描与分析软件。总共有超过75,000个机构使用Nessus 作为扫描该机构电脑系统的软件。 
## 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

###

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉***<strong>嘿客必备开发工具*****👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**[](https://mp.weixin.qq.com/s/og1thH9PAOLBmRvANz_Hng)
