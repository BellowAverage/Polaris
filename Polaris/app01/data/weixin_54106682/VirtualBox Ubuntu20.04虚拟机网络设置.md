
--- 
title:  VirtualBox Ubuntu20.04虚拟机网络设置 
tags: []
categories: [] 

---
**目录**









#### 一.虚拟机网络连接方式设置

打开virtualBox 点击设置

<img alt="" height="740" src="https://img-blog.csdnimg.cn/532fe36f523b436f9eb13a096b9b9171.png" width="1200">

 点击网络，连接方式选择NAT网络<img alt="" height="1016" src="https://img-blog.csdnimg.cn/d7e9d29a866a4bfd8e37839411da88d9.png" width="1200">

 若上述界面中界面名称为未指定，则回到管理器主页面，点击管理--&gt;点击全局设定

<img alt="" height="740" src="https://img-blog.csdnimg.cn/8700f38fc9764b27ba2c15066e834ce8.png" width="1200">

 之后按照下图界面序号依次点击，活动名称下一栏出现NatNetwork即可

<img alt="" height="700" src="https://img-blog.csdnimg.cn/55d907947fb74f5f990297f9578f5cf8.png" width="992">

 完成上述操作后，回到网络连接方式，选择NAT网络即可。

#### 二.Ubuntu网络代理设置

打开Ubuntu设置页面 选择网络 将网络代理设为手动

<img alt="" height="729" src="https://img-blog.csdnimg.cn/7b23f0b40f1f4211877bae4b9ed875f1.png" width="1200">

需填写内容如下图所示

 <img alt="" height="610" src="https://img-blog.csdnimg.cn/3301e75c51ac44b3946b37c9e5005eb7.png" width="649">

 其中ip可以直接在主机上查看。打开cmd命令提示符，输入ipconfig命令，显示如图，要用VirtualBox那个IP

<img alt="" height="1050" src="https://img-blog.csdnimg.cn/d5d9ee4187764da896a59b31419af05f.png" width="1200">

 端口号输入主机所用代理端口号， 之后，Ubuntu虚拟机浏览器工作正常



<img alt="" height="1200" src="https://img-blog.csdnimg.cn/c600b98805334521a1cd0358e569da9d.png" width="1200">

####  三. git设置代理

```
git config --global http.proxy http://192.168.56.102:7890
git config --global https.proxy https://192.168.56.102:7890

```

#### 四.一些碎碎念

虚拟机网络设置这一块，之前看了很多大佬的博客，跟着设置了代理之类的，虚拟机浏览器上网没什么问题，但是git clone时一直报错，例如超时或拒绝连接。后续，自己捣鼓了一下，发现可以git成功了。但是对于Virtualbox提供的网络连接方式中NAT网络和网络地址转换类型，我不太清除有什么区别，因为我用网络地址转换方式时，git依然失败，555欢迎评论区大佬指点一二！
