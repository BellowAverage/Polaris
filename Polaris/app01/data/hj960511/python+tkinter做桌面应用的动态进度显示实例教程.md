
--- 
title:  python+tkinter做桌面应用的动态进度显示实例教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解通过python的tkinter库来做动态的桌面应用的运行信息的进度显示效果实例。 日期：2022年4月29日 作者：任聪聪 文章附件： 


动态展示不是说for循环以后才展示而是在for循环中不断的展示动态进度信息，以便于避免exe桌面应用出现无响应的问题。

### 实例效果展示

1.文本类型的动态进度显示。 <img src="https://img-blog.csdnimg.cn/f5de691c9ef44048a02b7e5e066a8891.gif" alt="在这里插入图片描述"> 2.进度条类型的动态进度显示。 <img src="https://img-blog.csdnimg.cn/a64247d011ae48798585cbd810242dce.gif" alt="在这里插入图片描述">

### 前置环境

python版本大于3.79，且tkinter是最新的。

### 环境准备

如果不确定是否是最新则利用pip重装下tkinter。

```
pip install tkinter

```

tips：默认每个版本自带的tkinter版本都不同。

### 使用方法

对count进行替换，如替换为数组，进行处理数据࿰
