
--- 
title:  chrome打开网站视频显示no cimpatable source was found for this media 
tags: []
categories: [] 

---
        在写了一个视频播放的网页挂在网站后，在edge、ie等浏览器上都是正常的，但是在chrome升级了之后，突然就不能使用了，而是出现了no cimpatable source was found for this media，如下图所示：

     <img src="https://img-blog.csdn.net/20171219154428495" alt="">

      在查阅了相关的资料后，发现是因为chrome对flash的禁止加载导致的，那么下面我们来更改下相关的设置，解决这个问题：

（1）点击如下图箭头所指的标志处：

<img src="https://img-blog.csdn.net/20171219155145550" alt=""> 

（2）在得到下图所示的时候，点击图中所示的“网站设置”：

<img src="https://img-blog.csdn.net/20171219155249471" alt=""> 

（3）得到下图后，会看到flash的默认是询问，我们知道有些情况下它确实会询问，但是现在这种情况就是没有询问了，所以我们要选择“允许”：

<img src="https://img-blog.csdn.net/20171219155526585" alt=""> 

（4）选择允许后，回到刚刚的视频界面，会看到重新加载的按钮，单击此按钮：

<img src="https://img-blog.csdn.net/20171219155802664" alt=""> 

（5）这样问题就解决了，如下图所示：

<img src="https://img-blog.csdn.net/20171219155957952" alt=""> 
