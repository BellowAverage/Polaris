
--- 
title:  C++基于Qt+OpenCV+Dlib的人脸识别GUI系统源码，基于自己的人脸识别SDK实现的人脸识别系统追踪系统 
tags: []
categories: [] 

---
介绍 基于自己的opencv和dlib封装的人脸识别SDK实现的人脸识别系统追踪系统

软件架构 <img src="https://img-blog.csdnimg.cn/498b04ef9a3f46f3a8c7e41dc5ee1d9d.png" alt="在这里插入图片描述">

如图所示主要分为摄像头人脸识别模块，人脸录入模块，人脸库查看

视频处理线程

<img src="https://img-blog.csdnimg.cn/dec764a604b2480c96f01b328a1c2aca.png" alt="在这里插入图片描述">

人脸识别线程 <img src="https://img-blog.csdnimg.cn/c66fd9188a7549e6b6d0744fa25594fe.png" alt="在这里插入图片描述">

人脸追踪 <img src="https://img-blog.csdnimg.cn/57335d4c4eb44baa90114471e8f8b459.png" alt="在这里插入图片描述">

安装教程 windows上用Qt打开.pro运行即可 linux上需要重新编译人脸识别动态库，将facerecog.cpp加入工程

使用说明 GUI界面有四个按钮，对应按键的功能 <img src="https://img-blog.csdnimg.cn/8f77e1d271bd4176bdd76435e6fed8ce.png" alt="在这里插入图片描述">

参与贡献 从SDK到GUI全部由本人毕设期间完成

功能展示 一.人脸识别 1.陌生人识别（未被保存在库中） <img src="https://img-blog.csdnimg.cn/0936a714712e4ef5a67a3d76795ecfc2.png" alt="在这里插入图片描述"> 左上角显示红色圆圈表示此人为陌生人 <img src="https://img-blog.csdnimg.cn/de267508d5ec40089224f4889043f66b.png" alt="在这里插入图片描述">

2.识别出具体的人并且显示其名字 <img src="https://img-blog.csdnimg.cn/64c560cc23864852a0dc731c44fa5754.png" alt="在这里插入图片描述">

3.远处识别 <img src="https://img-blog.csdnimg.cn/60f946ce6f56473498095802ce8c2f97.png" alt="在这里插入图片描述">

4.近处识别 二.追踪功能 1.持续追踪 <img src="https://img-blog.csdnimg.cn/203bcbe651f849eab57e7a3b5e4b5b63.png" alt="在这里插入图片描述">

2.侧脸追踪 <img src="https://img-blog.csdnimg.cn/e36d92e3ffd9476eb172d322240b6a1a.png" alt="在这里插入图片描述"> 完整代码下载地址：
