
--- 
title:  utools插件开发之监听按键的命令和状态 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解utools插件开发，监听按键命令的方法 作者：任聪聪 


### 前提说明

1.utools没有自带的监听enter等按键的api 2.utools赋值需要通过js的全局变量来复制

### enter接收参数

在js端中进行接收 <img src="https://img-blog.csdnimg.cn/8ffde772a9d048ec8cea98ac6146e7c1.png" alt="在这里插入图片描述"> 赋值需要在preload.js <img src="https://img-blog.csdnimg.cn/67a0e620eb1e4797be54537fa2361060.png" alt="在这里插入图片描述">

### 实际效果

输入内容sddd <img src="https://img-blog.csdnimg.cn/cd879266e6374e948fd7f50951b8541c.png" alt="在这里插入图片描述">

按下enter后实际的取得参数 <img src="https://img-blog.csdnimg.cn/fac1d3a401cb4713974350f32c8bf50d.png" alt="在这里插入图片描述">

完整的文章附件：
