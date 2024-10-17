
--- 
title:  网友发给我一个钓鱼网站，我用 Python 渗透了该网站所有信息 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/f35debe82b4a048512ed4c104c1ca807.png">

前言：

这篇文章不是像评论区的某些大佬所想的那样是来炫技的，更多的是来给大家科普一些实用的渗透工具和方法，我相信不是所有的人都用过文中提到的这些方法。

<img src="https://img-blog.csdnimg.cn/img_convert/9ea9b2483e28b383a6f5a97fbda02b79.png">

刚才在知乎上看到一篇文章《你的QQ号是这么被偷走的！》，但是文章只是简单提到了一个伪造的 LOL 站点，嗯，就是这个【uvu.cc/ixMJ】，这明显是一个经过缩短链接处理的网站，打开后跳转到这个真实网址

```
【http://mfspfgp.top】

```

页面是下面这样的：

<img src="https://img-blog.csdnimg.cn/img_convert/1cd27e9b5f0c7d8f8d2688ae1fdee48c.png">

点击登录弹出一个对话框，让输入QQ号和密码，随便输入了一个进去，居然都可以登录，看来是一个简单盗号的网站无疑咯。

<img src="https://img-blog.csdnimg.cn/img_convert/84f9f3860cd0d03bd3beac4126b2367f.png">

我很好奇的是，现在人们的安全意识这么高，这么低级的盗号网站还能骗到人吗？

算了，不管了，习惯性打开浏览器的开发者工具，先来看看这个盗号的 POST 过程。找到了，POST 到这个地址：

```
http://mfspfgp.top/lollove.php

```

参数只有两个：name 和 pass。

<img src="https://img-blog.csdnimg.cn/img_convert/644bb5aff1760fbd866f63dfae3b721b.png">

有了 POST 的链接和参数，就可以先来玩一下了，首先使用 Python 伪造浏览器头，生成随机的 QQ 号和密码，然后利用 requests 来循环 POST 垃圾数据到对方的服务器，毕竟主要目的是警示一下网站管理员，数据量就少点吧，10000差不多了，而且 IP 代理和多线程并发都懒得加了。

<img src="https://img-blog.csdnimg.cn/img_convert/49bf5a357053b64a442ec364a39d446d.png">

代码跑起来了，非常鼓励大家（尤其新手）采用类似手段给这个站点注入点垃圾信息，我估计钓鱼站长看到数据库中的这些垃圾数据，而且来自很多的 IP 地址，心理应该是崩溃的。

<img src="https://img-blog.csdnimg.cn/img_convert/c06f83c85d3f0b97beb187a9b732a0a0.png">

好了，就让它继续跑着吧，下面来看看能不能挖掘些其他的东西。

注：

这个钓鱼网站获取到的账号密码不一定就写入数据库，而且写入数据库后也不一定有页面进行显示出来，所以 XSS 的难度很大。

而且网站也有可能是通过发邮件或者写入文本等方式进行保存数据，现在邮箱系统更新补丁很快，感觉 XSS 也不好弄。评论中有人说很轻松就可以 XSS 的，烦请告知具体的实现方法，非常感谢！

先 PING 一下这个域名（mfspfgp.top），得到服务器的 IP 地址（103.98.114.75）。

<img src="https://img-blog.csdnimg.cn/img_convert/7c674ffb7de3dcc37a527e3ec154528c.png">

查了一下这个地址，是个香港的服务器，也难怪，这样不备案的域名也只敢挂在外面的服务器上了。

<img src="https://img-blog.csdnimg.cn/img_convert/fb10703ae0161f75a47fa880668bc77c.png">

之后查了一下这个域名的 whois 信息，得到一个 QQ 邮箱和一个手机号，当然这两个联系方式也不一定是真的。

<img src="https://img-blog.csdnimg.cn/img_convert/56740126d2baace19929ce6a760d6dd4.png">

用 QQ 搜了一下这个 QQ 号，显示是一个江西吉安的少年，而且他的 QQ 空间是开放的，进去看了一下，也没有发现什么有价值的东西，只看出这个小兄弟喜欢玩英雄联盟和王者荣耀。

<img src="https://img-blog.csdnimg.cn/img_convert/28b9e2f18e72fbd75fe2d52683a7b3d8.png">

在搜索引擎上检索这个 QQ 号以及对应的 QQ 邮箱也没有找到任何有价值的信息，所以，上面这个 QQ 号的主人应该不是钓鱼网站的主人，很有可能是被这个网站盗号了。

在微信里搜索了一下这个手机号，显示地区是河南洛阳，而且他的微信头像应该是他本人了。但是我不能确定他就是网站的所有者，所以就不放他的照片了。

<img src="https://img-blog.csdnimg.cn/img_convert/7a27430c91d9cd4c1645751322583a35.png">

之后，利用邮箱反查工具，查了一下这个邮箱还注册了哪些网站，结果找出 9 个，发现其中有 6 个可以正常访问。

<img src="https://img-blog.csdnimg.cn/img_convert/fa845d8d85b8bc4db09f0cd431f68868.png">

这 6 个可以访问的网址分别是：

```
http://fjkskda.top 、http://jligyts.top 、http://pfdqlql.top 、http://yiqilin.top 、http://zykjgkd.top 、http://mfspfgp.top 。

```

对应三种形式的诈骗网页，分别是刚才展示的【生日祝福】、【酷秀一夏】、【2017赛事正式开始】，后两个页面截图分别如下：

<img src="https://img-blog.csdnimg.cn/img_convert/6543a9fdab4a67e33345a11796dbf4cb.png">

<img src="https://img-blog.csdnimg.cn/img_convert/2562e79a7941fd368e995d62a3db210a.png">

这三种页面的盗号方式全部一样，所以顺便将上面的程序对着其他的站点跑了一下，不用谢，我的名字叫雷锋~

之后，将上面提到的网址全部 Ping 了一下，获取了全部的 IP 地址，择其中物理位置最详细的那个 IP 来试试吧。

<img src="https://img-blog.csdnimg.cn/img_convert/d8c57ba2e89ca064154ed8a0936e8edc.png">

首先在 WhatWeb 里面检索一下这个 IP 地址，即可知道这个网站采用的是 nginx 1.8.1 服务器，使用的是 5.5.38 版本的 PHP。

<img src="https://img-blog.csdnimg.cn/img_convert/d94790326211a16f96f971c4a5144141.png">

然后用 nmap 扫了一下端口和运行的服务，发现开放的端口还是蛮多的。

<img src="https://img-blog.csdnimg.cn/img_convert/ecb9cc25f811b6982c183b4e22752a12.png">

```
PORT STATE SERVICE
1/tcp open tcpmux
3/tcp open compressnet
4/tcp open unknown
6/tcp open unknown
7/tcp open echo
9/tcp open discard
...省略...
61900/tcp open unknown
62078/tcp open iphone-sync
63331/tcp open unknown
64623/tcp open unknown
64680/tcp open unknown
65000/tcp open unknown
65129/tcp open unknown
65389/tcp open unknown

```

（题外话：上面那个 62078 端口对应的 iphone-sync 服务感觉有点像苹果同步啥的~）

然后用 w3af 来检测网站的一些弱点，进而获取一些重要信息。但是不知道怎么回事，这次运行 w3af 出现了线程出错，导致没有顺利完成扫描，所幸的是，扫出来一个敏感链接：

```
http://103.27.176.227/OGeU3BGx.php。

```

<img src="https://img-blog.csdnimg.cn/img_convert/a21b322e28a71c2a1198199a84a18e16.png">

用浏览器访问这个链接，显示的是一个错误页面，但是下面出现了一个关键信息：Powered by wdcp

<img src="https://img-blog.csdnimg.cn/img_convert/f5b8e65f49f790964039a9eae6e243af.png">

点击 wdcp 进入其官方页面，看到了如下重要信息，这个网站还贴心地给出了一个体验站点：

```
http://demo.wdlinux.cn

```

大家可以去试试。

<img src="https://img-blog.csdnimg.cn/img_convert/b7c495a5cbf67ca998c0524186aa2763.png">

这样就知道了上面那个钓鱼网站的后台地址了：

```
http://103.27.176.227:8080

```

<img src="https://img-blog.csdnimg.cn/img_convert/6eeb475a1d95d92e06f2c1ef6c8d940e.png">

另外，我刚才去那个体验站点试了试，发现在修改密码的时候，用户名一直是 admin，修改不了，加上原来的登录页面没有验证码，估计可以尝试暴力破解。

<img src="https://img-blog.csdnimg.cn/img_convert/0395cdbeedf617245bec1ddc221e1972.png">

用 sqlmap 扫了一下登录表单的注入点，发现并没有找到。

<img src="https://img-blog.csdnimg.cn/img_convert/f097499485bbdf18be73ef1826af75c7.png">

难道真的只有通过密码库来暴力破解了吗？还在思考中。。。

结束语：

使用 DDOS 等技术也许可以很轻松击垮这样的钓鱼站点，但是站长分分钟给你再造几十个出来，这样受害的人也许会更多。

所以本篇文章的目的就是给那些入门的人科普一下常见的渗透工具，这样当自己遇到类似情况的时候能有所帮助，只有让更多的知友认识到钓鱼网站的危险，学会利用上面的方法来保护自己的信息安全，这样才有意义，你们说呢？

声明：本文于网络整理，版权归原作者所有。

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/4231c764414c55e58e0aec7f1f8d97d4.gif">

微信扫码关注，了解更多内容
