
--- 
title:  【已解决】No Python at ‘D:\Python\python.exe‘ 
tags: []
categories: [] 

---
## 错误：

运行项目出现错误：No Python at ‘D:\Python\python.exe’

<img src="https://img-blog.csdnimg.cn/da01d8b7ccbe49098d89e69d3aed076e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 错误原因：

由于python版本更新，需要升级，先将原来的python卸载了，然后安装新版本（3.8.0），结果pycharm找不到python编辑器； 或者由于Python路径发生了更改。

## 解决办法：

### 一、关闭该项目，建立新项目

### 二、在原项目中进行修改

有些小伙伴的原项目中没有太多有用信息，但有些小伙伴原项目比较重要，此时第一种方法就不是特别合适啦，需要在原项目中进行修改，方法如下：

点击左上角File - - Settings <img src="https://img-blog.csdnimg.cn/ecedacc3972545c7b1ec9fc460278127.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_18,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 点击Project: Demo01 - - Python Interpreter ,进入下面界面；<img src="https://img-blog.csdnimg.cn/229321abcda14098afcd721b2e625839.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 点击路径后面设置符号，点击Add； <img src="https://img-blog.csdnimg.cn/cfe4fbd8c9614eaa863f4fce6eab10ad.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/1884950d277945da815af5fa9cda2c7a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

选择Existing environment， 然后点击后面三个点； <img src="https://img-blog.csdnimg.cn/221ab2bde6d8482b9ff7743df2297e48.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 选择自己的Python路径，点击OK； <img src="https://img-blog.csdnimg.cn/00608b92f15f434bbafd477dca01b746.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_16,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

此处先点击Apply，再点击OK； <img src="https://img-blog.csdnimg.cn/91d8192862934f77a797b9f0c9e56ee2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 运行成功！！ <img src="https://img-blog.csdnimg.cn/2238ca318bf545688fbb012c36dacb22.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
