
--- 
title:  Python实现智能互动拍照系统(毕设源码) 
tags: []
categories: [] 

---
### 前言 

本系统旨在探索先进的计算机视觉算法在大熊猫主题的互动拍照场景上的应用。

系统结合人脸及人体关键点识别，人像分割，目标检测，图像风格迁移，以及自己设计实现的熊猫分割PandaSeg，动作识别PoseRecognition等算法，依托Django框架搭建的Web应用，在服务器端使用 tensorflow、pytorch等深度学习框架搭建的智能图像处理模块处理前端通过单目相机捕获的图片并实时返回处理结果，目前可以实现实时视频挂件，人脸表情包生成，人像与熊猫照片创意融合，多动作互动拍照，分区风格化等功能。

### 系统结构 

### 系统注册、登录界面： 

<img src="https://img-blog.csdnimg.cn/img_convert/c3facc4d51c850305b202bc186d9e9ef.png" alt="c3facc4d51c850305b202bc186d9e9ef.png">

<img src="https://img-blog.csdnimg.cn/img_convert/b5e647d4c9e723ca7183f2bdf16e1c48.png" alt="b5e647d4c9e723ca7183f2bdf16e1c48.png">

### 系统主界面： 

<img src="https://img-blog.csdnimg.cn/img_convert/d6c1dfc75e266c36076fd33b551c546a.png" alt="d6c1dfc75e266c36076fd33b551c546a.png">

### 熊猫贴纸拍照模块： 

<img src="https://img-blog.csdnimg.cn/img_convert/7e7006d18c643172a096ab55086e31a6.png" alt="7e7006d18c643172a096ab55086e31a6.png">

<img src="https://img-blog.csdnimg.cn/img_convert/8a5caaa4c1b45aedff2f53236d471c09.png" alt="8a5caaa4c1b45aedff2f53236d471c09.png">

### 熊猫头表情包拍照模块： 

<img src="https://img-blog.csdnimg.cn/img_convert/ba04171f0eb9ce5dbeff5e13a2ac8c38.png" alt="ba04171f0eb9ce5dbeff5e13a2ac8c38.png">

<img src="https://img-blog.csdnimg.cn/img_convert/73b2c521f8acddd8f384a28c2d3fb8e4.png" alt="73b2c521f8acddd8f384a28c2d3fb8e4.png">

### 熊猫背景环境创意融合模块： 

<img src="https://img-blog.csdnimg.cn/img_convert/26fa1e29df0b8ed82c03577718a8b955.png" alt="26fa1e29df0b8ed82c03577718a8b955.png">

### 动作识别拍照（互动融合）： 

<img src="https://img-blog.csdnimg.cn/img_convert/360f308e54bf87759a02d01b3db49743.png" alt="360f308e54bf87759a02d01b3db49743.png">

<img src="https://img-blog.csdnimg.cn/img_convert/7945270acbb10fac4cb8fecf83b9345e.png" alt="7945270acbb10fac4cb8fecf83b9345e.png">

### 定时拍照（自动融合）： 

<img src="https://img-blog.csdnimg.cn/img_convert/4568cc0ec836d96e0d1281a98a3719d9.png" alt="4568cc0ec836d96e0d1281a98a3719d9.png">

<img src="https://img-blog.csdnimg.cn/img_convert/81256ef3be30b696c300cece8c67cb84.png" alt="81256ef3be30b696c300cece8c67cb84.png">

### 视频背景替换： 

<img src="https://img-blog.csdnimg.cn/img_convert/e9f089b612cd540e25bddb9883e4872b.png" alt="e9f089b612cd540e25bddb9883e4872b.png">

<img src="https://img-blog.csdnimg.cn/img_convert/2cc21d86471acaa2de3603cae725697d.png" alt="2cc21d86471acaa2de3603cae725697d.png">

<img src="https://img-blog.csdnimg.cn/img_convert/12e1d64c5e5f667b85dc0d0b0ca454ca.png" alt="12e1d64c5e5f667b85dc0d0b0ca454ca.png">

<img src="https://img-blog.csdnimg.cn/img_convert/dfd27ec61eebdb8d22b3347a5b193ef3.png" alt="dfd27ec61eebdb8d22b3347a5b193ef3.png">

### 风格化处理： 

<img src="https://img-blog.csdnimg.cn/img_convert/84b56dac84df36daa78588a31ddfc6f4.png" alt="84b56dac84df36daa78588a31ddfc6f4.png">

<img src="https://img-blog.csdnimg.cn/img_convert/69e796fae0c96e943bfbca356ee33413.png" alt="69e796fae0c96e943bfbca356ee33413.png">

<img src="https://img-blog.csdnimg.cn/img_convert/903589cf789f0662438dcc60438004fe.png" alt="903589cf789f0662438dcc60438004fe.png">

<img src="https://img-blog.csdnimg.cn/img_convert/ef41c6a37134446762300d26b1082667.png" alt="ef41c6a37134446762300d26b1082667.png">

### 动漫头像生成模块： 

<img src="https://img-blog.csdnimg.cn/img_convert/e15ff9841d35cc7f82f4f5ddd7f087e3.png" alt="e15ff9841d35cc7f82f4f5ddd7f087e3.png">

<img src="https://img-blog.csdnimg.cn/img_convert/bad6f2bc24a9ef2339c04a25b8867545.png" alt="bad6f2bc24a9ef2339c04a25b8867545.png">

### 完整源码获取 

1、点击**下方**图片拉到文末点**喜欢作者**赞赏 **1** 元



2、我核实后会直接回复你源码下载链接，如未能及时回复可以添加小二微信，小二直接用微信发你~

<img src="https://img-blog.csdnimg.cn/img_convert/540d2abf6b92475748c464b4b911275a.jpeg" alt="540d2abf6b92475748c464b4b911275a.jpeg">

**不是机器人**

**耐心等待，不要着急**
- - - 