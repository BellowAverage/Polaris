
--- 
title:  论文记录3_CycleGAN-损失函数部分 
tags: []
categories: [] 

---
论文地址：https://arxiv.org/abs/1703.10593 

#### 文章目录
- - 


<img src="https://img-blog.csdnimg.cn/70b5f6b17a824f419d483c4dcab30efd.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 网络架构

<img src="https://img-blog.csdnimg.cn/953f288c7ff7433e9c62455054a7af22.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/0ca6f914d6f54b8ab4146fc06b7a0eb7.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/3be37bebdcbf4afa941c75b5add35453.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 损失函数

**生成对抗损失：** 生成器G的目标是将X空间中的样本转化成Y空间中的样本，将学习X-&gt;Y的映射。 根据交叉摘损失，可以构造下面的损失函数

<img src="https://img-blog.csdnimg.cn/0fb0074a326345519789d3e7fc435c55.png" alt="在这里插入图片描述"> D为判别器，输出值[0,1]，Dy=1代表输出来自Y空间 <img src="https://img-blog.csdnimg.cn/74325c7736c0480fb56d125dc9b0f564.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 引入生成器F，目标是将Y空间中的样本转化为X空间中的样本，学习Y-&gt;X的映射。 <img src="https://img-blog.csdnimg.cn/94bf5b5a923746dbb5eaa9cfeee16cdd.png" alt="在这里插入图片描述"> F的损失函数与G相似。

**循环一致性损失：** <img src="https://img-blog.csdnimg.cn/8076cb6e05fa4224a091f79522eb612f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

**最终的损失函数：** <img src="https://img-blog.csdnimg.cn/ab572876b84448de921d85306c9ee5ae.png" alt="在这里插入图片描述">

**注：此文为阅读笔记，参考了其他的论文，博客，如有侵权请联系，我附上原出处。**
