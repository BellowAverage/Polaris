
--- 
title:  《 Python笔记》— 将pyinstalller打包封装的exe文件反编译为pyc文件和python文件 
tags: []
categories: [] 

---


#### 目录
- - <ul><li>- - - 


## 将pyinstalller打包封装的exe文件反编译为pyc文件和py文件

很多开发者没有发布源程序代码，而是将代码封装为exe可执行文件，这样不仅更有利于程序传播，方便了普通用户使用，而且相当于源程序更加保密或者说不公开自己的源码，但是对于同样也是开发者的话，就比较麻烦了。 那么难得真的就不能获得源码了吗，此时需要怎么办呢？ 答案是：逆向反编译

对于用pyinstaller包将python程序代码打包封装的.exe文件怎么将其反编译出原始的python代码？ 大体分为两步，提取.pyc文件和反编译，下面本文将提供详细步骤。

**如何将Python程序打包为exe可执行文件？** 请阅读另一篇文章： 

### 1 提取.pyc文件

第一步提取.pyc文件，从 .exe文件提取.pyc文件 首先需要用到pyinstxtractor.py脚本文件，从exe文件中提取出pyc文件。 **1：** 将.exe文件和pyinstxtractor.py文件放到同一路径下 pyinstxtractor.py文件的下载链接如下：  https://pan.baidu.com/s/1J2FIomqpkIRm41JVJZy4Sw 提取码: 6yik

>  
 注：pyinstxtractor.py文件是一个专门用来反向解析pyinstaller打包的exe文件的脚本 


**2：** 在当前路径下打开powershell 或 cmd命令行 cd 到该路径下

**3：** 在命令行中输入下面内容，并回车执行

```
python pyinstxtractor.py main.exe

```

运行完成后，在当前路径下回出现一个新的文件夹，打开则可以找到.pyc文件。

### 2 反编译

将获得的.pyc文件反编译为python程序 **第1步：** 安装uncompyle

```
pip install uncompyle

```

**第2步：** 文件所在文件目录执行如下命令：

```
uncompyle6 main.pyc &gt; out.py

```

>  
 注：uncompyle6 包可以将python的二进制代码反向转换为python源代码 


### 文件结构

以2贰进制小工具-批量给图片加水印应用程序（详见下面批量添加水印链接博文：）为例： 做如下总结： **exe文件**通过pyinstxtractor.py脚本可直接反向编译为 → Watermark.pyc (**Python二进制文件**) 再通过uncompyle包将Watermark.pyc (Python二进制文件)转为 → out.py (**Python源码**) <img src="https://img-blog.csdnimg.cn/606dd13a2348444aaa9a6db44bf9d70d.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_222FFF,t_70#pic_center" alt="在这里插入图片描述" width="300">

### 更多内容

公众号地址： 

CSDN主页地址： 
