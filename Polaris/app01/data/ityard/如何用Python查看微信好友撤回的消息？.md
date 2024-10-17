
--- 
title:  如何用Python查看微信好友撤回的消息？ 
tags: []
categories: [] 

---
首先声明，本文主要就是在试图复现这篇文档中所说的：

https://cloud.tencent.com/developer/article/1701130

因此要是下文中有什么讲的不清楚的地方，大家也可以参考上面这篇文档。

### **一、pip Install itchat**

既然都用python解决问题了，第一步当然是明确用什么库啦，直接执行pip install itchat：

<img src="https://img-blog.csdnimg.cn/img_convert/7efd03f0bc058d696f563b35e22a4620.png" alt="7efd03f0bc058d696f563b35e22a4620.png">

👌 done!

### **二、itchat.login()**

下完了库，就得试下库的最入门用法啦，啦啦啦：<img src="https://img-blog.csdnimg.cn/img_convert/ef9581901845420bf80aca59027e8b44.png" alt="ef9581901845420bf80aca59027e8b44.png">

但没想到，复现到这一步时就出问题了。直接用itchat库像上面这样操作，登陆的会是微信的网页版，而腾讯之前为了防止大家用计算机自动化操作微信从而可能会导致一些安全问题，封停了网页版微信API，如果只是像上面这样做的话，控制台会提醒说“由于安全原因，此微信号不能使用网页版微信。你可以使用+Windows+版微信或+Mac+版微信登录。”

ok，男人要有耐心，遇事心平气和，google+知乎，若没试过七七四十九种解决方案，万不可直接考虑砸电脑。

很好，经过几次试错以后，找到一种简单便捷的解决方案：<img src="https://img-blog.csdnimg.cn/img_convert/7055da1241d490ea64e569ad8b576157.png" alt="7055da1241d490ea64e569ad8b576157.png">

很好，如上操作完，登陆成功！哦耶✌️！

### **三、itchat.search_friends() + send()**

很好，登陆成功，来试着给好友发条消息？

我大概执行了下面这样的代码：

<img src="https://img-blog.csdnimg.cn/img_convert/9998a02d79cb2f06e9d8ebd9ecae88e1.png" alt="9998a02d79cb2f06e9d8ebd9ecae88e1.png">

执行结果：<img src="https://img-blog.csdnimg.cn/img_convert/5f90a439f060d0116b22a7c372c46d88.png" alt="5f90a439f060d0116b22a7c372c46d88.png">

很好，发送成功！

### **四、@itchat.msg_register()**

接下来我们要监听一下好友发送的消息，尝试在本机执行参考文档中的这段代码：<img src="https://img-blog.csdnimg.cn/img_convert/4a8df91215ac93e74838d07d5e924c60.png" alt="4a8df91215ac93e74838d07d5e924c60.png">

在我本机复现的效果，没毛病，效果杠杠的，发啥我都能在控制台监听到了，嘿嘿嘿：<img src="https://img-blog.csdnimg.cn/img_convert/f121e0847d7133115498a97af914bb78.png" alt="f121e0847d7133115498a97af914bb78.png">

### **五、def reserver_info(msg)**

接下来我们来复现下面👇这一段：<img src="https://img-blog.csdnimg.cn/img_convert/39a1a5a965a72f34366a3482b56dde50.png" alt="39a1a5a965a72f34366a3482b56dde50.png">我本机上的情况（抄的我好开心啊[捂脸]）:<img src="https://img-blog.csdnimg.cn/img_convert/6483a103e7eac833a05bf0cd1ee2bcad.png" alt="6483a103e7eac833a05bf0cd1ee2bcad.png">

### **六、@itchat.msg_register([TEXT, PICTURE, RECORDING])**

上面完成了对于文字内容的监听，接下来要感受一下图片、语音什么的如何处理了。

尝试复现下面的代码：

<img src="https://img-blog.csdnimg.cn/img_convert/f6337d259f11e69d3a5358a9d9e2f14f.png" alt="f6337d259f11e69d3a5358a9d9e2f14f.png">

本机复现成功，结果我就先不放了，不然又得打码，好麻烦[捂脸]

原文中对于图片格式和音频格式的讲解：<img src="https://img-blog.csdnimg.cn/img_convert/aec7996f029232f7d5ed1466ac9aebc2.png" alt="aec7996f029232f7d5ed1466ac9aebc2.png">

### **七、os.mkdir() + info()**

我们现在牵扯到应该怎么存储图片和语音信息了。

而我接下来继续的行为，低情商的说法叫：继续抄；高情商的说法：人家代码的可复用性好高。

在本机复现这段代码：<img src="https://img-blog.csdnimg.cn/img_convert/093e508e7f4ab502611f320330995ad1.png" alt="093e508e7f4ab502611f320330995ad1.png">

执行结果：<img src="https://img-blog.csdnimg.cn/img_convert/e4aa8334b4ea8a4355715a5eff4c999c.png" alt="e4aa8334b4ea8a4355715a5eff4c999c.png">

是python就是这么容易顺利执行，让人感觉枯燥且乏味吗？Hhh，当年劳资要是想用别人的C++的代码，没个取经的精神，过上那么九九八十一难是绝对调不通滴呀，再一次，手动捂脸：[捂脸]

### **八、note_info(msg)**

现在我们能够存储聊天信息了，就是既然是要做防撤回软件，我们应该只需要存那些撤回了的信息，那么靠什么来判别哪些信息是撤回消息呢？Content模块为我们提供了NOTE类型，该类型指的是系统消息：

<img src="https://img-blog.csdnimg.cn/img_convert/d70daf414c4e116d44a1f6ee6ab86c8e.png" alt="d70daf414c4e116d44a1f6ee6ab86c8e.png">

好，我们继续在本地复现上面的程序：

<img src="https://img-blog.csdnimg.cn/img_convert/30575f4c43f9d10d63c77058f67a20dc.png" alt="30575f4c43f9d10d63c77058f67a20dc.png">复现成功，枯燥。

### **九、完整程序代码**

如果对本文内容感兴趣，可以添加小二微信：**ityard**，备注**撤回******

免费获取本文源码****

<img src="https://img-blog.csdnimg.cn/img_convert/2f1f63920d502d0f979104d80e0960a2.png" alt="2f1f63920d502d0f979104d80e0960a2.png">

******长按识别上方********<img src="https://img-blog.csdnimg.cn/img_convert/17dbb65efee113865395ddf5b765ae5e.png" alt="17dbb65efee113865395ddf5b765ae5e.png">二维码添加小二微信**

运行结果：

<img src="https://img-blog.csdnimg.cn/img_convert/d65a5987a1bc099115ca50d09c15cfd9.png" alt="d65a5987a1bc099115ca50d09c15cfd9.png">













～～～over～～～

PS：如果觉得我的分享不错，欢迎大家随手点赞、在看。
