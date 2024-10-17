
--- 
title:  【转】UnityVS(Visual Studio Tools For Unity)的安装与使用 
tags: []
categories: [] 

---
###  原文地址：http://www.cnblogs.com/petto/p/3886811.html

###  一些废话

 Unity 的开发者们，尤其是微软系的Unity开发者们，用Mono是不是烦死了？你是不是跟我一样，用vs来写代码，用Mono来跟踪调试？好麻烦啊好麻烦。

 也许你会说，傻逼你不会用UnityVS插件么?我会说，我擦那不是收费的么？你会说，傻逼你不知道世界上有个东西叫盗版么？我说，嗯，但是还是觉得不好用啊……

 其实在那个时代，微软大力引导Unity开发者发布WP游戏的时候，我就猜微软肯定会添加VS对Unity的调试支持。

  

 这不，前些日子微软宣布收购了UnityVS。你看看人家国外，小型的公司或者团队，靠着一个著名产品吃饭。大型公司如果稍稍花点儿人力和时间，马上就能让这个小公司没饭吃。但微软选择的是收购他们，然后推出免费产品。要是在国内……企鹅会说……阿狸会说……百毒会说……呵呵呵呵呵呵。

 然后微软增强了UnityVS的功能，改了名字（-_-)，简化了安装、配置过程。近日推出了Visual Studio Tools For Unity 1.9。

  

###  下载安装

 好了言归正传。我们接下来介绍一下这个插件。

 首选微软的官方博客地址：

 <img src="http://images.cnitblog.com/i/388462/201408/021220264939652.png" alt="" style="margin:0px; padding:0px; border:0px">

 呈上的三个链接是对、、不同的插件，我用2013，所以就下载了第三个。

  

 然后便是安装了，只有一个msi文件，是的，简单易用还很爽。MS很贴心。

 <img src="http://images.cnitblog.com/i/388462/201408/021223311029087.png" alt="" style="margin:0px; padding:0px; border:0px">

  

 同意、一路下一步。安装完毕。

  

###  导入与调试

 安装完插件后，打开Unity，选择新建工程，你会发现标准包中多了一个Visual Studio 2013 Tools.unityPackage的包。

 <img src="http://images.cnitblog.com/i/388462/201408/021226554464393.png" alt="" style="margin:0px; padding:0px; border:0px">

  

 你可以选择此刻勾选，并导入，也可以进入unity中再导入。

 在Unity中导入的方式为：

 菜单栏-&gt;Assects-&gt;ImportPackage-Visual Studio 2013 Tools

 <img src="http://images.cnitblog.com/i/388462/201408/021229408838683.png" alt="" style="margin:0px; padding:0px; border:0px">

  

 全选，导入。然后菜单栏中会多出来一项 Visual Studio Tools

 <img src="http://images.cnitblog.com/i/388462/201408/021232083836288.jpg" alt="" style="margin:0px; padding:0px; border:0px">

  

 ok，选择 Open In Visual Studio，就会用VS打开该项目的工程。

 调试起来就非常简单啦，F5，然后选择附加到Unity进程，再进入Unity，运行游戏。

 <img src="http://images.cnitblog.com/i/388462/201408/021234439159271.png" alt="" style="margin:0px; padding:0px; border:0px">

  

 然后正常调试就行啦。

  

 <img src="http://images.cnitblog.com/i/388462/201408/021236371334517.png" alt="" style="margin:0px; padding:0px; border:0px">

  

###  结束语：

 VS大法好，退Eclipse保平安。

 Windows大法好，推OSX保平安。

 微软大法好，退水果股沟保平安。

  

 微软对于程序员来讲伟大的地方很多，其中之一是，他所做的努力，都是在另人类的生活更加便捷而有趣，让专业人员更能专注于他的专业本身，而不是为了做这个东西，先得配置半天环境。

 我就理解不了那些熟练应用各种Eclipse插件的程序员有什么好鄙视用VS程序员的。你丫配好安卓环境的时候，我一个版的都上线了。
