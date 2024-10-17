
--- 
title:  基于Python tensorflow机器学习的人脸识别登陆系统源码、人脸注册系统源码 
tags: []
categories: [] 

---
## face_login

代码下载地址：

##### 介绍

本项目基于tensorflow机器学习，实现web端人脸识别登陆，人脸注册。

提供手机端页面(face_login_app)和网页端页面(vue_element-admin)。

用户注册后进行一次机器学习，将用户的面部特征加入到模型中。

希望大家多多指教。

<img src="https://img-blog.csdnimg.cn/img_convert/2238dbb10a18e13b2b1924fc27999ec7.jpeg" alt="pc端登陆">

<img src="https://img-blog.csdnimg.cn/img_convert/f63e171335d5013e79da821c0d9a5096.jpeg" alt="pc端注册">

<img src="https://img-blog.csdnimg.cn/img_convert/38f90e7fe0a578b187567614d1fdd9ed.jpeg" alt="移动端">

<img src="https://img-blog.csdnimg.cn/img_convert/204c029ed18cd5379c5a75f697658d5d.jpeg" alt="">

##### 软件架构
1.  tensorflow 用于人脸识别的机器学习 1.  vue web端开发 1.  redis 保存token，因为方便失效 1.  MongoDB 保存人脸已编码的数据和用户信息 1.  flask 用于开发web接口，和返回静态页面 1.   人脸识别python库，可以从照片中识别人脸 
##### 安装教程
<li> 运行app 配置app.py中redis和mongodb的地址和端口 <pre><code class="prism language-shell">python app.py
</code></pre> </li>
##### 使用说明
1.  app 文件夹中保存项目的核心代码，提供数据访问接口，返回网页，训练模型，生成模型，验证图片等 1.  face_login_app 文件夹中保存移动端代码，使用weui+vue，build后的dist代码放入到APP的dist中 1.  vue-element-admin 文件夹为网页边人脸识别登陆前端代码 
##### 特别说明
1.  手机端访问摄像头需要https 1.  目前iPhone的页面显示还有问题 1.  每次注册时，系统会将用户头像进行特征编码，然后进行一次全局的神经网络训练，这个如果用户多了性能会不好，有待提高 
##### TODO
1. 解决苹果手机无法使用问题1. 提高tensorflow的训练效率1. 开发小程序端1. 开发树莓派版人脸识别1. 活体检测
代码下载地址：
