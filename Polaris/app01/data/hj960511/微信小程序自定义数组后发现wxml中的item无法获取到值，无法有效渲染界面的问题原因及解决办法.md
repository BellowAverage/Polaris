
--- 
title:  微信小程序自定义数组后发现wxml中的item无法获取到值，无法有效渲染界面的问题原因及解决办法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解：微信小程序自定义数组后发现wxml中的item无法获取到值，无法有效渲染界面的问题原因及解决办法 日期：2022年12月17日 作者：任聪聪 


### 问题现象和描述

使用.push函数对数组进行了重新匹配，形成了新的数组并复制到小程序中，结果发现无法渲染wxml中元素。

```
old_arr.push(new_arr)

```

现象： <img src="https://img-blog.csdnimg.cn/4698650775eb4eb4b2d36f535e1a0ce1.png" alt="在这里插入图片描述"> wxml中代码： <img src="https://img-blog.csdnimg.cn/bd80d359ca4e4d3e9124da7f7eb18a60.png" alt="在这里插入图片描述">

### 问题排查及具体原因

wxml中代码没有变动，那么只有一种可能是重组数组时数据类型发生了问题导致的。

##### 具体原因：

<img src="https://img-blog.csdnimg.cn/f35498ada9d3461e954695c347f7a028.png" alt="在这里插入图片描述"> 打印前后数据后发现，最新的数组形式为多为数组类型，而旧数据时对象类型。

##### 问题代码

重组数组小程序中错误的写法&lt;
