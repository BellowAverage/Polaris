
--- 
title:  一款基于嵌入式AI的人脸识别课堂签到系统源码+完整开发文档，基于Python的智慧教室人脸考勤系统 
tags: []
categories: [] 

---
### 项目名称

智慧教室人脸考勤系统 代码及文档下载地址：

### 项目介绍

该系统主要用于基于人脸识别的课堂考勤场景，技术实现如下：

#### ①客户端

包括一台搭载摄像头的微型运算设备，具有基于深度学习AI的人脸识别功能，并通过socket网络通信将人脸特征发送至服务器；该程序运行在单片机等嵌入式系统上；

#### ②服务器

包括学生个人信息数据库，能够通过socket网络通信接收人脸特征并与数据库中的信息进行匹配，并回复客户端匹配结果与个人信息；该程序运行在个人PC上。

### 效果展示

<img src="https://img-blog.csdnimg.cn/img_convert/88d605a4a15e64c032698a70d64a74c7.jpeg" alt="image text"> <img src="https://img-blog.csdnimg.cn/img_convert/1414e5bef0651d679c5ddc6d35c926fc.jpeg" alt="image text">

### 创新点

该系统巧妙地将网络通信、嵌入式边缘AI、人脸识别技术运用于课堂考勤场景下，无需借助钉钉、学习通等第三方应用程序，只需进入教室前进行人脸识别，系统即可进行学生身份验证并自动汇总课堂签到结果，实现智能化课堂考勤功能。该系统成本低廉，复用性强，对未来高校智慧教室的实现与推广具有巨大积极作用。

### requirements

opencv_python<mark>4.5.1.48 numpy</mark>1.19.3 pandas<mark>0.24.2 face_recognition</mark>1.3.0 PyQt5==5.15.4

代码及文档下载地址：
