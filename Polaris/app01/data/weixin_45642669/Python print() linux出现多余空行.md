
--- 
title:  Python print() linux出现多余空行 
tags: []
categories: [] 

---
#### 问题：

使用了print还有readlines等。在windows下没有空行，但是在linux上打印出了大量空行。

```
文字

文字

文字

```

 

#### 问题

在windows下和在linux下实现不同。 简单来说：用readlines截取的字符会自带\n,然后print也会生成\n   print输出的时候会以\n作为结尾符。然后当打印数据到out流给每个print加上\n，所以出现了两次。

#### 解决方案

```
print(data.rstrip())

```
