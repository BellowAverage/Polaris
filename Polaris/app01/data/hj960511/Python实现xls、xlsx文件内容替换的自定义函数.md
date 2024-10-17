
--- 
title:  Python实现xls、xlsx文件内容替换的自定义函数 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解通过python批量替换xls、xlsx文件中的字符串的函数代码实例教程 日期：2023年5月9日 作者：任聪聪 版本：python3.9 


### 前提准备

安装：xlrd,xlwt,openpyxl

```
pip install 包名

```

引入：

```
import xlrd,xlwt,openpyxl

```

### 实际效果：

可批量替换xls、xlsx两种文件类型，效果如下：

#### xls文件替换前：

<img src="https://img-blog.csdnimg.cn/d30bf9da179b45b1909b51574a2f441c.png" alt="在这里插入图片描述">

#### xls文件替换后

<img src="https://img-blog.csdnimg.cn/def3269025244ae798de8bb12f01717d.png" alt="在这里插入图片描述">

#### xlsx文件替换前

<img src="https://img-blog.csdnimg.cn/a702249113214c3a8ebd80029c76b32e.png" alt="在这里插入图片描述">

#### 
