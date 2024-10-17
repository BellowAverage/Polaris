
--- 
title:  在Python中启动mitmproxy，脱离命令行启动mitmproxy监听 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/6c5ea9cc21114f5a80e9c4e463b67252.jpeg#pic_center" alt="在这里插入图片描述">

## 前言

>  
 本文解决了只能通过命令行启动 **mitmproxy** 的痛点。 


在使用 **mitmproxy** 时候存在这样一个问题，就是每次启动它时候都需要通过命令行启动。 加上最近有位读者向我提问（以前也有读者提问该问题）：不通过命令行如何启动 **mitmproxy**监听？

<img src="https://img-blog.csdnimg.cn/8f0b2034186941ea87f1ac4ce76b62fd.png" alt="在这里插入图片描述">

不得不说，在刚接触**mitmproxy**时候，我的确很头疼这个问题。 好在后面研究了一下下，也算是找到了解决方案。

恰好这个时间点，
- 之前研究过该问题，- 有读者再次提问，- 加上周末有时间码字。
新仇旧恨一起算，遂有此文。

本文记录了无需通过命令行去启动 **mitmproxy**，也是统一回复读者问！！！

另：如果对本文中的小工具感兴趣，可以移步到我的 这个专栏，学习工具的制作，后面我将会更新一系列的**PySide6**的使用。

## 知识点📖📖

|标题|链接
|------
|**🎈🎈妙用PySide6**|
|**【Python】通过 Python 设置电脑代理端口**|

## 实现

>  
 我更想分享的是解决问题的思路，而不仅仅是分享答案。 


之前写过一篇关于在**Python**设置 **Windows**系统代理的文章，，本篇文章在此基础之上，

结合了**Python** 的 **os** 和 **subprocess** 模块来调用系统命令； 当然也还有一些零散的**Windows**系统网络管理命令，这些就不在这里赘述啦！

从而实现了脱离命令行，在**ide** 就可以启动 **mitmproxy**。

### 思路

>  
 这里阐述一下我是如何处理这个问题的。 


**启动mitmproxy**
- 在**Python**中可以使用**winproxy**模块去设置**Windows**系统代理（**mitmproxy**默认监听**8080**端口；- **Python** 中的 **os** 和 **subprocess**，可以执行**Windows**系统的**cmd**命令；- So，以上就解决了设置代理和启动**mitmproxy**监听；
**关闭mirmproxy**
- 结合**Windows**系统的网络管理命令，使用**netstat**能够查找到占用**8080**端口的进程号（**PID**- 然后再调用**Windows**系统的网络管理命令的 **taskkill**去杀死指定的 **PID**- 这里又解决了关闭或说是结束**mitmproxy**监听。
以上，就是整个的思路。 很多时候，思路发散一下，解决问题的方法还是很多的。

## 小工具展示

>  
 该工具可以采集某公众号留言，某乎文章，某博热点等等，仅用于展示。不提供代码 


小工具结合了**Qt**来实现，可视化工具是 **PySide6**，主要用于展示启动**mitmproxy**的效果~

另：如果对本文中的小工具感兴趣，可以移步到我的 这个专栏，学习工具的制作，后面我将会更新一系列的**PySide6**的使用。

<mark>不提供小工具代码，跟着上面的免费`Pyside2`专栏学习，你可以做出更好的工具</mark> <mark>不提供小工具代码，跟着上面的免费`Pyside2`专栏学习，你可以做出更好的工具</mark> <mark>不提供小工具代码，跟着上面的免费`Pyside2`专栏学习，你可以做出更好的工具</mark>

### 工具展示

使用步骤如下：
1. 执行程序1. 打开监听1. 保存文件1. 即可看到评论数据了
<img src="https://img-blog.csdnimg.cn/5c734347b75e42d1b400fa1040803d32.gif#pic_center" alt="在这里插入图片描述">

### 工具界面展示

运行程序，小工具的界面如下图框选内容所示，
- 选择平台：对应**某公众号留言，某乎文章，某博热点等**- 开始监听：打开**Windows**系统代理- **在按下开始监听按钮后，按钮会自动变成停止监听按钮。**- 停止监听：关闭**Windows**系统代理- 保存文件：点击即可保存**mitmproxy**监听缓存下来的文件。
<img src="https://img-blog.csdnimg.cn/7c6d1879bbe34942adc6cdcdbcc75ad5.png" alt="在这里插入图片描述">

### 打开

注意看，这里点击了**开始监听** 按钮后，按钮文本就 变成了 **停止监听**， 这时候去查看**Windows**系统代理，发现是已经打开了的，并且是预设好的**8080**端口。

<img src="https://img-blog.csdnimg.cn/9dee3250b21d42dc9a6f9fb9ae2cc4f8.gif#pic_center" alt="在这里插入图片描述">

### 关闭

注意看，这里点击了**停止监听** 按钮后，按钮文本就 变成了 **开始监听** 这时候再去查看Windows系统代理，发现是已经关闭了的。

<img src="https://img-blog.csdnimg.cn/2fb3c9d25df845b1954bf9dc83042ae9.gif#pic_center" alt="在这里插入图片描述">

## 代码

>  
 代码这里一共就几行，注释我不加了，懒得加。自己看。 


无非就是设置Windows系统代理，打开代理，调用cmd执行 **mitmproxy**的命令，调用Windows系统网络管理命令等，在上面的思路中已经介绍过了。

```
# -*- coding: utf-8 -*-
# @author: Frica01

import os
import time
from subprocess import Popen


def start_listen():
    Popen('winproxy set --all 127.0.0.1:8080').communicate()
    time.sleep(0.2)
    Popen('winproxy on').communicate()
    time.sleep(0.2)
    Popen(f'mitmdump -s &lt;file_path&gt;/script.py')


def close_listen():
    Popen('winproxy off').communicate()
    result = os.popen('netstat -ano | findstr 8080 | findstr LISTENING')
    port = result.read().split('      ')[-1]
    if port:
        Popen(f'taskkill /f -t /pid {<!-- -->port}')


```

## 后话🧐🧐

本次分享到此结束， see you~
