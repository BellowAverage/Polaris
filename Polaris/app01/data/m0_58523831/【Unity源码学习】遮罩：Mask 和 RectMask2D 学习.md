
--- 
title:  【Unity源码学习】遮罩：Mask 和 RectMask2D 学习 
tags: []
categories: [] 

---
### 前言

>  
 UGUI的裁切分为Mask和Mask2D两种 


### 目录

 - Mask原理分析
 - RectMask2D原理分析
 - RectMask2D和Mask的性能区分

### 一、Mask原理分析

>  
 Mask：IMaskable，IMaterialModifier 


我们先来看Mask。它可以给Mask指定一张裁切图裁切子元素。我们给Mask指定了一张圆形图片，那么子节点下的元素都会被裁切在这个圆形区域中。

<img src="https://img-blog.csdnimg.cn/img_convert/32d99a8622c5eb458711f2d544c439a5.jpeg" alt="">

**Mask的实现原理：**

>  
 1. Mask会赋予Image一个特殊的材质，这个材质会给Image的每个像素点进行标记，将标记结果存放在一个缓存内（这个缓存叫做 **Stencil Buffer**） 2. 当子级UI进行渲染的时候会去检查这个 Stencil Buffer内的标记，如果当前覆盖的区域存在标记（即该区域在Image的覆盖范围内），进行渲染，否则不渲染 


#### 1.1 StencilBuffer

看起来好像挺简单的，那么背后的功臣——StencilBuffer，究竟是何方神圣呢？

简单来说，GPU
