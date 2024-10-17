
--- 
title:  Python趣味小案例 - 根据图片背景色二十五行代码生成祝福词云 
tags: []
categories: [] 

---
 https://blog.csdn.net/meenr/article/details/107325270



#### 目录
- - <ul><li>- <ul><li>- - - - - - 


## Python二十五行代码生成祝福词云

### 概述

本文介绍的内容是，利用python语言编写25行代码，生成一朵漂亮的玫瑰词云。可用来做生日祝福、高考祝福等等，是一款小众而又有创意的Python礼物。

#### 原图

<img src="https://img-blog.csdnimg.cn/20200715141723417.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="原图1" width="200" height="350"> <img src="https://img-blog.csdnimg.cn/20200715141852180.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="原图2" width="200" height="350"> 以上面这两张图片为背景生成生日祝福词云。

#### 效果图

示例效果如下： <img src="https://img-blog.csdnimg.cn/20210607101557715.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="300" height="300">

<img src="https://img-blog.csdnimg.cn/20210607101438973.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="300" height="220">

<img src="https://img-blog.csdnimg.cn/20210607101356237.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="300" height="220">

<img src="https://img-blog.csdnimg.cn/2021060709575552.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="350" height="200">

### 代码设计

三个函数。少废话，上代码。

#### 图片预处理函数

<img src="https://img-blog.csdnimg.cn/2021060709593891.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_80,color_00FF0F,t_70#pic_center" alt="在这里插入图片描述" width="350" height="200">

#### 生成词云函数

<img src="https://img-blog.csdnimg.cn/20210607101111104.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_100,color_00FF0F,t_70#pic_center" alt="在这里插入图片描述" width="450" height="280">

#### 主函数

<img src="https://img-blog.csdnimg.cn/20210607100611304.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_60,color_00FF0F,t_70#pic_center" alt="在这里插入图片描述" width="420" height="200">

### 示例图片与.py源文件

感兴趣的读者若需要源代码的.py文件和示例图片可通过下面两种途径获取。

#### 途径一

请移步微信 第一步：扫描下方二维码，或打开微信搜索并关注“ **2贰进制** ”公众号； 第二步：回复:“ **祝福词云** ”即可获取上文所述的全部参考代码。 <img src="https://img-blog.csdnimg.cn/2020070300554991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="二维码" width="250" height="250">

#### 途径二

请移步QQ 扫描下方二维码，加入学习交流QQ群“ **480558240** ”，联系管理员获取包括但不限于本篇内容的更多学习资料。 <img src="https://img-blog.csdnimg.cn/2020071217121655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="300" height="300"> **2贰进制–Echo 2020年3月** 我认同兴趣是最好的老师，但是除了兴趣其次是侮辱，所以如果您觉得本文还不错，请点赞＋评论＋收藏，要是关注那更是对我极大地羞辱了，您的羞辱便是我前进的动力！ 如果本文对你有所帮助，解决了您的困扰，可以通过赞赏来给予我更大支持： <img src="https://img-blog.csdnimg.cn/20210424133535613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="400" height="200"> 此致 感谢您的阅读、点赞、评论、收藏与打赏。
