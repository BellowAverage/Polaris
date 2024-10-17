
--- 
title:  用 Python 写了一个表白神器，照片隐藏表白话语！ 
tags: []
categories: [] 

---
## 来源：blog.csdn.net/qq_44809707

### 

## 前言

<img alt="30ca14b39d3d99c9d853e31fd6e4fdbb.png" src="https://img-blog.csdnimg.cn/img_convert/30ca14b39d3d99c9d853e31fd6e4fdbb.png"> 最近天气好冷，感觉整个人都是冰冰的！程序员如何用python表白自己的女神呢？我想用最近学的图像处理知识，在照片上加隐藏字（手机正常浏览是一张照片，放大才可以看到里面的文字）

大家也可以用这个代码去表白自己的对象呀。

## 一、具体过程

### 1、代码思路

先用cv2中的imread方法读取冰冰的照片，再用PIL的Image方法创建一个相同大小的图像（初始填充白色），最后在图片上每一个块加字。

### 2、python完整代码

```
# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import cv2
font_path='./font-family/MiNiJianPangWa-1.ttf'
def draw(image_path, draw_text):
  img = cv2.imread(image_path)#读取图片文件
  img_temp = Image.new("RGB", [img.shape[1],img.shape[0]], "white")#以指定的模式和大小创建一个新图像（白色填充）,img.shape[1]为像素大小
  drawObj = ImageDraw.Draw(img_temp)#创建一个可以在给定图像上绘图的对象。
  n = 8#间隔大小
  m = 8#字体大小
  font = ImageFont.truetype(font_path,size = m)
  for i in range(0, img.shape[0], n):#通过两个for循环，依次定位到每个文字所在的色块
    for j in range(0, img.shape[1], n):
      drawObj.text([j, i],draw_text[int(j / n) % len(draw_text)],fill = (img[i][j][2], img[i][j][1],img[i][j][0]),font = font)
  img_temp.save('img_' + image_path)
draw('bingbing.jpg', "都是冰冰的")#可以自己更改哦
```

### 

### 3、代码补充

font_path需要自己更改，可以去网上下载字体。我试过几个字体，发现一个效果比较好。

百度网盘链接：https://pan.baidu.com/s/1e7zwvHgmr-90QH5j0vPGBg 提取码：8owp

m和n的值也可以自己更改，不过我试过很多值，发现两者都为8的效果比较理想。

## 二、结果

这是我用的冰冰的照片（选的照片尽量像素大一点）：

<img alt="fd12c31ba80f5c870143ae5608e2da45.png" src="https://img-blog.csdnimg.cn/img_convert/fd12c31ba80f5c870143ae5608e2da45.png"> 这是结果图（手机预览看不到文字）

<img alt="e189150568f9c1cc8463152ac7ad9421.png" src="https://img-blog.csdnimg.cn/img_convert/e189150568f9c1cc8463152ac7ad9421.png"> 放大后可以清楚看到文字内容

<img alt="e89ebcccf6a04b55c2e5bf4a5cad0efb.png" src="https://img-blog.csdnimg.cn/img_convert/e89ebcccf6a04b55c2e5bf4a5cad0efb.png">

### 

## 补充

最后生成的图片放大后可能会失真，文字模糊。我在网上发现一个网站，可以无损放大图片。上传图片，选择放大倍数，选择最高降噪，两分钟左右就可以生成。

<img alt="7c103d3580ce49d112be34fcc7a465d2.png" src="https://img-blog.csdnimg.cn/img_convert/7c103d3580ce49d112be34fcc7a465d2.png"> 最后把这个网站分享给大家：https://bigjpg.com/

PS：如果觉得我的分享不错，欢迎大家随手点赞、在看。

&lt; END &gt;

<img alt="d9431314aca9f1bed5ef18f9b83dd5b2.gif" src="https://img-blog.csdnimg.cn/img_convert/d9431314aca9f1bed5ef18f9b83dd5b2.gif">

微信扫码关注，了解更多内容
