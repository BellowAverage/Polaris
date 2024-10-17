
--- 
title:  【20天搞定Python】第4天：if语句的多种形式和while循环 
tags: []
categories: [] 

---
上次我们提到了一些if语句的内容，知道在开发的时候很多情况都会使用if判断，比如：用户登陆、付款、人脸识别、或者指纹识别开门等等都会用到判断。这个最基本的知识。

## 分支判断

上一章提到了

>  
 if 要判断的条件:     条件成立时，要做的事情 


想一想：在使用if的时候，它只能做到满足条件时要做的事情。那万一需要在不满足条件的时候，做某些事，该怎么办呢？

>  
 答：使用 if-else 


if...else就像你走在一个人字路口，面前有两条路，你会选择走哪一条路。每一条路的结局不同。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/d8e8e994dc2c6ebfeae7f98f55b8c3c9.webp?x-oss-process=image/format,png">

if-else的使用格式：

>  
 if 条件:     满足条件时的操作 else:     不满足条件时的操作 


按照这个格式我们写一个例子吧！

```
ticket = 1 # 用1代表有车票，0代表没有车票
if ticket == 1:
    print("有车票，可以上火车")
    print("终于可以见到Ta了，美滋滋~~~")
else:
    print("没有车票，不能上车")
   
```
