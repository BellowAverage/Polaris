
--- 
title:  [ 解决报错篇 ] VMware 报错 -- VMware Workstation 无法连接到虚拟机请确保您有权运行该程序访问该程序使用的所有目录以及访问所有临时文件目录 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - - 


## 一、前言

>  
 给用户搭建攻防演示系统，之前搭建了说效果不明显，我想这那就给弄个威力十足的bat吧,然后我就随手写了个bat 


<img src="https://img-blog.csdnimg.cn/832287e71296401ea59ad5f23ea713dd.png" alt="在这里插入图片描述">

>  
 运行了bat 


<img src="https://img-blog.csdnimg.cn/f9a57d30569f4b9bb1579a5d43761184.png" alt="在这里插入图片描述">

>  
 结果，哈哈哈哈哈，紧张又刺激，手速够快，还能截张图（图片是复现的时候截的，碰到问题的时候没敢截图） 


<img src="https://img-blog.csdnimg.cn/199b38e7170c42809bec835aedccffaa.png" alt="在这里插入图片描述">

>  
 结果我选择可强制关掉VMware，结果VMware 就报错了 


>  
 刚开始还以为是只有执行bat的虚拟机报错，后面发现所有虚拟机都打不开，问题锁定再vmware，然后百度，然后解决了问题，哈哈哈哈哈，自己作，瞎倒腾，没办法 


## 二、VMware 报错

>  
 VMware Workstation 无法连接到虚拟机。请确保您有权运行该程序、访问该程序使用的所有目录以及访问所有临时文件目录。VMware Authorization Service 当前未运行。 


<img src="https://img-blog.csdnimg.cn/f490fa0d8caa46b3bd29dadb62fc5b6c.png" alt="在这里插入图片描述">

## 三、问题分析

>  
 我想这应该是我强制关掉VMware导致的，VMware强制关机导致内部系统非正常关机。在网上找了找果真是这个原因，然后着手解决问题 


## 四、问题解决

>  
 Windows电脑使用Win+R 然后输入services.msc，然后回车调出服务 


<img src="https://img-blog.csdnimg.cn/943fd3c9f7fd479c870b0174f7401b96.png" alt="在这里插入图片描述">

>  
 在服务里面寻找vmware workstation service 


<img src="https://img-blog.csdnimg.cn/4b8db216058a437fbe91920d13be102e.png" alt="在这里插入图片描述">

>  
 找到之后右键点击打开属性将启动类型换成（自动延时启动），然后确认退出，重启电脑，再次打开虚拟机即可正常使用。 


<img src="https://img-blog.csdnimg.cn/01d99192fc2f405aaf051eb54c1adc64.png" alt="在这里插入图片描述">

## 五、解决成功

>  
 重新启动电脑之后重新打开VMware，正常启动win10虚拟机 


<img src="https://img-blog.csdnimg.cn/6110524e1a974b978e593ccb0d4f5df2.png" alt="在这里插入图片描述">
