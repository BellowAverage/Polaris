
--- 
title:  [ 系统安全篇 ] 拉黑IP - 火绒安全软件设置IP黑名单 && windows使用系统防火墙功能设置IP黑名单 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - - - - - - - - - - - - - - 


## 一、火绒安全软件设置IP黑名单

### 1、打开火绒安全软件

>  
 双击打开火绒安全软件 下载链接 


```
https://www.huorong.cn

```

<img src="https://img-blog.csdnimg.cn/67f13fa5af374b059f1116b736844b52.png" alt="在这里插入图片描述">

### 2、进入安全设置

<img src="https://img-blog.csdnimg.cn/1931737610c741099a26636a8cf5d0e2.png" alt="在这里插入图片描述">

### 3、添加ip黑名单

>  
 加入需要拉黑的ip 


<img src="https://img-blog.csdnimg.cn/da67608185974451917f0c0a52b7b791.png" alt="在这里插入图片描述">

### 4、启动策略

>  
 启动使其生效即可 


<img src="https://img-blog.csdnimg.cn/96e9ea3f94b74da8bb010d48239be8ec.png" alt="在这里插入图片描述">

>  
 此时火绒弹出告警信息，查看告警信息发现，我们的黑名单规则已经生效 


<img src="https://img-blog.csdnimg.cn/5c0116f2ec3149a98686f0ac098f74a2.png" alt="在这里插入图片描述">

## 二、windows使用系统防火墙功能设置IP黑名单

### 1、进入控制面板

<img src="https://img-blog.csdnimg.cn/f0dee2ea2d14403c9cc029bf8a866c19.png" alt="在这里插入图片描述">

### 2、点系统和安全

<img src="https://img-blog.csdnimg.cn/0a8533bb1149478eb8ffc9cdefaa3ebc.png" alt="在这里插入图片描述">

### 3、点windows防火墙<img src="https://img-blog.csdnimg.cn/42c483e5420c4c5e9fea16077906e323.png" alt="在这里插入图片描述">

### 4、点高级设置

<img src="https://img-blog.csdnimg.cn/3013e899286e471c9c9e828ade49beaf.png" alt="在这里插入图片描述">

### 5、点入站规则，点新建规则

>  
 注：入站规则：别人电脑访问自己电脑。 


<img src="https://img-blog.csdnimg.cn/9593bbb47c9a49a19378b112c767081b.png" alt="在这里插入图片描述">

### 6、选中自定义，下一步

<img src="https://img-blog.csdnimg.cn/90fa388ff5c4432381db1dbca26efd50.png" alt="在这里插入图片描述">

### 7选择所有程序，点击下一步

<img src="https://img-blog.csdnimg.cn/abf2ce6eb9434c29a8c7ed0887b4c6c7.png" alt="在这里插入图片描述">

### 8、端口协议等可设可不设

<img src="https://img-blog.csdnimg.cn/5c2715a7ab7c4ea8b426414458aa0c7e.png" alt="在这里插入图片描述">

### 9、限制IP（关键步骤）

>  
 我这里是拉黑局域网ip，也就是本地ip地址，如果需要拉黑外网ip地址则需要选择远程ip地址 


<img src="https://img-blog.csdnimg.cn/74dd2cac25ff4b67abc8b74747253fcc.png" alt="在这里插入图片描述">

### 10、执行阻止操作

<img src="https://img-blog.csdnimg.cn/13c1acb6f6004278992f74bdf761d7fb.png" alt="在这里插入图片描述">

### 11、所有网络使用该规则

<img src="https://img-blog.csdnimg.cn/928d9a9f780e4f1887e4df1a9f23cfa3.png" alt="在这里插入图片描述">

### 12、设置名称，点击完成

<img src="https://img-blog.csdnimg.cn/9227bc577ae546859da3d65ed557981b.png" alt="在这里插入图片描述">

### 13、查看我们设置的规则

<img src="https://img-blog.csdnimg.cn/2eb3f63ac55348f6b0dafc634220138f.png" alt="在这里插入图片描述">
