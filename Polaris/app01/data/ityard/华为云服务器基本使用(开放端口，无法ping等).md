
--- 
title:  华为云服务器基本使用(开放端口，无法ping等) 
tags: []
categories: [] 

---
官网地址：

<img src="https://img-blog.csdnimg.cn/e50258d374fb47a5bde79b4df950ee32.png" alt="">

选择：IAM用户

<img src="https://img-blog.csdnimg.cn/7dfc2a877e5c425aa126eb85d289693f.png" alt="">

选择：弹性云服务器

<img src="https://img-blog.csdnimg.cn/41875e6885e348c0b45f447c1ecbafef.png" alt="">

如下所示：

<img src="https://img-blog.csdnimg.cn/4854bd00d2bc4549ace5c32f0367c9ed.png" alt="">

使用Xshell等工具远程连接之前需先开放`22`端口，选择要远程的服务器，点`更多`，之后选`网络设置`，再点击`安全组规则配置`，如下所示：

<img src="https://img-blog.csdnimg.cn/93eacd3a9f4d4a15965c50fbfb569ae5.png" alt="">

点击`配置规则`，如下所示：

<img src="https://img-blog.csdnimg.cn/6317c481240e4bbeacc6164be009faac.png" alt="">

添加入向规则即可。

开放`ping`命令，选`入方向规则`，点击`添加规则`，添加`ICMP`入方向规则即可。

<img src="https://img-blog.csdnimg.cn/499051a1f8a54658940a4a5d88d51a99.png" alt="">
