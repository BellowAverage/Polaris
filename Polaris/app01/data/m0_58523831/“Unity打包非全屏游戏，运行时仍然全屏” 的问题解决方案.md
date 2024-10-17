
--- 
title:  “Unity打包非全屏游戏，运行时仍然全屏” 的问题解决方案 
tags: []
categories: [] 

---
#### **前言**

我们在使用Unity做游戏的时候，会碰到一些需要固定分辨率的游戏，可是有时候在固定了分辨率以后，打包出来的项目却一直都是全屏的，那么有什么方法解决呢？

#### **固定分辨率**

首先需要固定分辨率，我们可以从左上角**File → Build Settings → Player Settings → Resolution and Presentation**中将默认填满屏幕取消勾选，并设置宽高。

<img src="https://img-blog.csdnimg.cn/0146d8555c784126b6627122bc81b2b7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2I5ZCO55qE6LKT,size_20,color_FFFFFF,t_70,g_se,x_16" alt="">

<img src="https://img-blog.csdnimg.cn/5a9e55d665e54cb6a2a9b17388a88f4b.png" alt="">

#### **解决打包后依然全屏的问题**

我从百度中尝试了各种各样的方法，最后在一个视频中得到了答案，原来是因为我们的注册表中曾经运行过同公司的产品，我们需要打开**运行**(Windows快捷方式Win+R) → 输入**Regedit**打开注册表 **→**打开注册表之后，在注册表中找到**HKEY_CURRENT_USER → Software → Unity → UnityEditor**下
