
--- 
title:  【去重】java字符串重复出现符号、空格、其他字符类型后，通过过滤仅保留1个 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解，java字符串重复出现符号、空格、其他字符类型后，通过过滤仅保留1个。 标签：java字符串去重解决办法 作者：任聪聪 


### 去重效果

以空格为例： <img src="https://img-blog.csdnimg.cn/3eb22c00d07547d6bfae6800e604a247.png" alt="在这里插入图片描述"> 可以看到是不规则的重复出现，单纯的使用replace函数是无法替换的。

### 方法一、正则去重的方法说明

代码实例：

```
 		String str;
        str = " 1 2   3      4      5 6 ";
        str = str.replaceAll("\\s{2,}", " ");
 
```
