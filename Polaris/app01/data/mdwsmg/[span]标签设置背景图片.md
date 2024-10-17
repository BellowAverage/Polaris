
--- 
title:  [span]标签设置背景图片 
tags: []
categories: [] 

---
## [span]标签设置背景图片

记录遇到的一个小问题 **这里在设置span小图标的时候图片显示不出来** ：必须设置高度和宽度，**以及转换元素类型**（因为常规为内联元素，不能设置图片）

```
	background:#000 url("图片地址") no-repeat;
	width: 100%;
	padding-top: 100%;
	/* 
	使用% 设置宽高以适应父元素的大小
	因为可能得高度坍塌，使用padding-top=（原图高/原图宽）设置高度
	*/
	background-size: cover;
	background-position: center;
	/*
	使用 background-size: cover; 自适应铺满
	background-position: center; 兼容不支持上面语句的浏览器版本
	*/
	display: inline-block;
	/*
	span为内联元素，应用为图标时要看情况进行元素类型转换
	*/

```

##### 关于padding-top的设置和 background-size:cover,请见大佬的

https://www.cnblogs.com/tugenhua0707/p/5260411.html#_labe10
