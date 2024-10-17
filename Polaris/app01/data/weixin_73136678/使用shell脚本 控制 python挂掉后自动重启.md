
--- 
title:  使用shell脚本 控制 python挂掉后自动重启 
tags: []
categories: [] 

---
我们经常需要在后台运行一些python脚本，来监控系统或者做一些其他事情；但是 由于各种各样的问题，不是python脚本代码的问题；脚本运行过程中会挂掉。手动重启 不现实，天天耗在上面等重启。。。

所以我们写一个shell脚本来控制 python挂了之后 自动重启：

shell脚本如下：非常简单：

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/a2c41900eb708668f3d3dfd5cafbf271.png">

然后我们使用该shell脚本启动python程序：启动之后：我们来测试一下：

在后台kill -9 杀掉python的进程；看python脚本自动重启了

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/64621fa2196b7e42ae9fbdeee0f9b904.png">
