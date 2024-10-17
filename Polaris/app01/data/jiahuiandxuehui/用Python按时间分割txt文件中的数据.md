
--- 
title:  用Python按时间分割txt文件中的数据 
tags: []
categories: [] 

---
## 案例

有一个监测系统，每隔两分钟就会记录一下监测结果，如下图所示：现在要求按小时将数据提取，并存为新的txt文件，也就是1天会对应有24个txt文件。先整理一下思路：

 1. 读取数据
 1. 将每行数据的时间戳转换成“日期-小时”格式，并按此分类数据，
 1. 存入字典 按“日期-小时”分断，将写入数据到新的txt文件

使用readlines()将txt中的每一行数据读取为一个长字符串，并存入列表。数据读取如下所示。

<img src="https://img-blog.csdnimg.cn/0e7bde552fc2447f9dc3be7015283f47.png" alt="在这里插入图片描述">

## 操作

```
#读取txt文件中的数据
file = open('data.txt')
lines = file.readlines(
```
