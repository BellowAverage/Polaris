
--- 
title:  【去重】php正则过滤字符串中多次重复出现内容为1个 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解，使用用正则去重字符串中的多次出现的字符信息 作者：任聪聪 


### 重复现象

以空格为例： <img src="https://img-blog.csdnimg.cn/c6ed322088c347a79240e4423639a12f.png" alt="在这里插入图片描述">

### 解决办法一、foreach+explode+implode进行替换

思路：利用foreach+explode+implode进行替换 特点：效率较低，适合少量数据

代码片段：

```
header('Content-type: text/html; charset=utf-8');

$str = "1 2    3 4          5";
$str_arr = explode
```
