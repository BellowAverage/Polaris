
--- 
title:  超详细，Wireshark 3.6.3安装教程（Windows系统） 
tags: []
categories: [] 

---
## 环境准备

操作系统：Windows 10 企业版 安装包：Wireshark-win32-3.6.3.exe <img src="https://img-blog.csdnimg.cn/140d12fd938f46508756fdca69d8e7b7.png#" alt="在这里插入图片描述">

## 初始安装

双击安装包，进入安装向导界面。

1）点击下一步，开始安装

<img src="https://img-blog.csdnimg.cn/62a0294df5d1450ba80556d9ae569c19.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 2）同意许可协议，点击下一步

<img src="https://img-blog.csdnimg.cn/393cf67d596f4600b6c09403f981c6cb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 3）组件选择界面，保持默认，点击下一步

<img src="https://img-blog.csdnimg.cn/e4c754a724804500828834acba272e24.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 4）快捷方式界面，勾选桌面快捷方式，点击下一步

<img src="https://img-blog.csdnimg.cn/11fd7e93ac354e54af87cde2b7559247.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 5）选择安装位置，点击下一步

<img src="https://img-blog.csdnimg.cn/03c7ef44280d4323892b6c5cfb394440.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 6）安装 WinPcap（Wireshark通过WinPcap接口获取网卡的网络流量），保持默认，点击下一步 <img src="https://img-blog.csdnimg.cn/f97bfde8241e4758bf44b6495516dfa1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 7）USB捕获，按需安装即可，这里不安装，点击 Install，安装过程会持续几分钟。

<img src="https://img-blog.csdnimg.cn/8547383d86ce4523acf4e19b50e1af66.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 7.1 安装过程中，会弹出 Npcap的安装界面，正常安装即可，许可协议界面，点击我同意

<img src="https://img-blog.csdnimg.cn/69361570b03c4adeaa0e99e922d8ea12.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 7.2 安装选项界面，保持默认，点击安装，等待若干分钟

<img src="https://img-blog.csdnimg.cn/07371ae6ccf44979b2d163bcc37728b9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 7.3 Npcap安装完成，点击下一步

<img src="https://img-blog.csdnimg.cn/2cc54c34c06a463db4389ce16cfc9a99.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 7.4 点击完成按钮，完成Npcap的安装

<img src="https://img-blog.csdnimg.cn/9c04360f6c904702879406f2a13b957c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 8）安装完Npcap后，回到 Wireshark 的安装界面，点击下一步

<img src="https://img-blog.csdnimg.cn/8e5653b43651436da99c358b5f4818c0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 9）重启电脑完成安装（不方便可以稍后重启），点击完成

<img src="https://img-blog.csdnimg.cn/7aa1f2cdd004436bab3d9986ff203af6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 10）重启电脑后，打开 Wireshark，开始使用吧

<img src="https://img-blog.csdnimg.cn/930b4f61dbc944bb91e164c205c6dd7b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aOr5Yir5LiJ5peld3l4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

## 学习计划安排

<img src="https://img-blog.csdnimg.cn/8bb5de58644d4dbc8bf419bd78b38454.png" alt=""> 我一共划分了六个阶段，但并不是说你得学完全部才能上手工作，对于一些初级岗位，学到第三四个阶段就足矣~

这里我整合并且整理成了一份【282G】的网络安全从零基础入门到进阶资料包，需要的小伙伴可以扫描下方CSDN官方合作二维码免费领取哦，无偿分享！！！

如果你对网络安全入门感兴趣，那么你需要的话可以

<img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述"> 你对网络安全入门感兴趣，那么你点击这里**👉**
