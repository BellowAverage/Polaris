
--- 
title:  Unexpected fatal error while intitailizing Python runtime报错 
tags: []
categories: [] 

---
### 一、出现报错时

```
初始化Python运行时时发生意外致命错误。请运行idapyswitch以确认或更改已使用的Python运行时

```

<img src="https://img-blog.csdnimg.cn/f786c0c1d09849bf900b149c0b4f38ac.png" alt="在这里插入图片描述"> Unexpected fatal error while intitailizing Python runtime报错

### 二、解决办法方法

1.确定IDA关联的python所在位置，添加用户变量：创建新的**用户变量**PYTHONHOME，路径为：D:\Anaconda3 <img src="https://img-blog.csdnimg.cn/3cc9c0b1dbe94905a7c0753ba7d586ea.png" alt="在这里插入图片描述">

2.添加系统环境变量：在Path里创建新路径，路径为：D:\Anaconda3\Lib(上面的路径+Lib) <img src="https://img-blog.csdnimg.cn/f9cccf45f5a043a3af75d55214c71db7.png" alt="在这里插入图片描述">
