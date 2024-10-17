
--- 
title:  100天精通Python（数据分析篇）——第63天：Pandas使用自定义函数案例（pipe、apply、map、applymap、agg） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/9633f3bb7c3643d0a6989e51c0470ac6.gif#pic_center" alt="在这里插入图片描述">



#### 文章目录

  - 
  <li>
   <ul>
    - 
    - 
    - 
    - 
    - 
   


## 一、Pandas自定义函数

>  
 自定义函数是指：有时候需要对 pandas 里的值进行一些特殊操作，但是没有内置函数，或者把其他库中的函数应用到 Pandas 对象中，这时候可以自己写的一个函数 


### 1. pipe()

>  
 通过给 pipe() 函数传递一个自定义函数和适当数量的参数值，从而操作 DataFrme 中的所有元素 


**语法格式**：
