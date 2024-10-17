
--- 
title:  【Selenium & Other】一键摸鱼 & 一键采集数据 
tags: []
categories: [] 

---
## 前言

>  
 将Selenium程序编写为 .bat 可执行文件，从此一键启动封装好的Selenium程序，省时省力还可以复用，岂不美哉✨✨ 


## 应用场景

>  
 写好 `.bat` 可执行程序，从此快速摸鱼🐟🐟~ 


|作用|释义
|------
|一键摸鱼|一次性打开多个共上班摸鱼的网页（如：B站，虎牙…
|一键数据采集|执行 `.bat` 可执行文件，即完成数据的采集
|给到他人使用自己写的脚本|`.bat` 可执行文件给到对方，即可畅快运行（忽略环境安装
|开机后一键启动多个程序|自动打开多个指定程序
|…|…

当然，还可以将 `.bat` 可执行文件添加到系统的 **定时计划**，那样就可以定时运行啦！

应该还有其它用途，但是我实在是编不下去了…

## 代码

### 一键摸鱼（打开多个网页

>  
 下面的代码是伪代码，随手✍的 


这里不局限于是 摸鱼链接，它也可以是学习链接。 反正它可以一键打开N多个网页，省去你手动打开多个网页的烦恼，可谓是一劳永逸！！！

**batch_open_website.py**

```
# -*- coding: utf-8 -*-
# Name:         batch_open_website.py
# Author:       小菜
# Date:         2022/8/29 19:00
# Description:

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://blog.csdn.net/weixin_45081575')

js = 'window.open("{url}")'

# 摸鱼链接
urls = [
    'http://mo.fish/',  # 摸鱼
    'https://bcy.net/',  # 半次元
    'http://jandan.net/',  # 煎蛋
    'https://www.huya.com/',  # 虎牙直播
    'https://dig.chouti.com/',  # 抽屉新热榜
    'https://www.bilibili.com',  # B站
]

for url in urls:
    driver.execute_script(js.format(url=url))


```

可以看到，已经打开浏览器并访问多个网页的了 <img src="https://img-blog.csdnimg.cn/dd85ffb5f16e4f80882180b8e3a4b754.gif" alt="">

### 编写bat

>  
 这一步比较简单， 


**demo.bat**

```
@echo off
f:
cd F:\_selenium

start D:\Python3.10.4\python.exe batch_open_website.py

```

代码释义：
- 第一行是默认写法- 第二、三行是切换路径，切换到Python脚本所在的路径- 最后一行是指定Python 运行的路径，当然，如果只安装了一个Python版本的，改成 **`start python`** 即可
`demo.bat` 可执行文件，运行效果如下：

<img src="https://img-blog.csdnimg.cn/0410f28ce5e94b8d9e5081a392b76d6c.gif" alt="">

### 一键数据采集

>  
 本文有标题党的嫌疑，但确实可以实现这个功能~ 


这个自己去完成吧。毕竟只有自己才知道自己需要采集啥数据，Selenium也是可以采集数据的，虽然有点慢，嗯。。。就是慢！但胜在简单！

## 开机自启N个程序

>  
 思路发散一下，可以指定打开多个电脑程序，不局限于Selenium浏览器的使用。 


这里指定打开多个电脑程序，省去一个个打开的繁琐~

**batch_start_application.bat**

```
@echo off

start chrome.exe

timeout /t 1

start wps.exe

timeout /t 1

start D:\WeChat\WeChat.exe

timeout /t 1

start D:\Typora\Typora.exe

```

代码释义：
- `timeout /t 1`：等待一秒- `start path/application`：打开指定路径的程序（也可以不指定路径
代码运行效果如下：
- 可以看到，电脑依次打开了在代码中指定的程序（chrome、wps、WeChat、typora…
<img src="https://img-blog.csdnimg.cn/a5b06fe91efb4526b154c4e6d17a1c33.gif" alt="">

这里思路再发散一下，将这个 `batch_start_application.bat` 可执行文件放置到 开机自启动目录，那就每次电脑开机都会启动对应的程序了~

步骤如下：
1. 【Win+R】（按下 键盘的`Win +R`，打开Windows系统的“运行”窗口1. shell:startup（然后在窗口中输入 `shell:startup`，回车后会弹出一个文件夹1. 拷贝 `batch_start_application.bat` 到弹出来的文件夹中 即可
<img src="https://img-blog.csdnimg.cn/39276084299a4ff6a2aec62bd05bd9a7.png" alt="">

上述操作完成后，电脑每次开机启动时候都会打开你指定的程序啦！是不是很省事呢✨✨

## 后话

本次文章介绍到此结束，后续再有想法时候，再做分享。

see you🍬🍬
