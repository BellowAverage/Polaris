
--- 
title:  php中laravel、thinkphp报错Array to string conversion的解决办法及原因说明 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解：php中laravel、thinkphp报错Array to string conversion的解决办法及原因说明 作者：任聪聪 日期：2023年4月22日 


### 现象说明

检查代码没有发现具体的问题，但是报错Array to string conversion。

### 原因：拼接的字符串中有数组类型

这只是一个小问题，仔细检查一下就会发现这个问题的报错。

#### 解决办法：

依次排查找到那个拼接数组的代码片段，并将其修改为字符串类型即可。
