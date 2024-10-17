
--- 
title:  Python 人脸识别 + 手机推送，老板来了你就会收到短信提示 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/72bb81a6f9e721826e337b22aa7ab9bc.png">

来源：python

## 前言

在你上班的时候刷知乎，看视频，玩手机的时候，老板来了！不用担心，不用着急，基于最新的人脸识别 + 手机推送做出的 BossComing。老板站起来的时候，BossComing 会通过人脸识别发现老板已经站起来，然后通过手机推送发送通知 BossComing，并且震动告诉你有情况。

## 效果展示

不明真相吃瓜群众和身后领导：

<img src="https://img-blog.csdnimg.cn/img_convert/2bb06c13964552cf32732035cda697e8.png">

身后领导扭头过来，马上被人脸识别程序发现，并标记为 boss：

<img src="https://img-blog.csdnimg.cn/img_convert/9fd73dbb92ff3243846feecef39cc389.png">

手机收到推送，并震动：

<img src="https://img-blog.csdnimg.cn/img_convert/16f4d6ef110fd104e460fa7992774e90.png">

Boss Coming：

<img src="https://img-blog.csdnimg.cn/img_convert/7b10a4a880dafb1aba3aae82ed012e55.png">

是不是就像学生时代“同桌的他”，用胳膊肘不停地戳你，并且小声的说：老师来啦，来时来啦。

技术介绍

人脸识别技术

face_recognition

The world's simplest facial recognition api for Python and the command line

ageitgey/face_recognition

手机推送技术

jpush-api-python-client

JPush's officially supported Python client library for accessing JPush APIs.

jpush/jpush-api-python-client

依赖安装

>  
  pip install face_recognition 
  pip install jpush 
 

使用教程

1. 添加 boss image

<img src="https://img-blog.csdnimg.cn/img_convert/89da8216f1b56cd896ffe295b663b7a5.png">

2. 配置文件

修改 bosscoming 文件中的 load_image_file 参数

<img src="https://img-blog.csdnimg.cn/img_convert/276c614acc552dd26c61f15f80f9cabb.png">

3. JPush 配置，这样你的手机才可以收到推送。

<img src="https://img-blog.csdnimg.cn/img_convert/e9338f9074a89ad5614edad2208bcfb9.png">

4. 可以直接使用 JPush 官方提供的 Demo 用来接收通知。

JPush 文档：JPush 产品简介 - 极光文档

5. 运行命令

>  
  python bosscoming.py 
 

体验人脸识别部分命令：

>  
  python bosswatching.py 
 

打开电脑上摄像头，开始捕捉画面。然后调整角度，对准需要观察的位置。

GitHub地址：https://github.com/fendouai/BossComing/tree/dev

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/0d9a395bc043f81040edbc993d6e4689.gif">

微信扫码关注，了解更多内容
